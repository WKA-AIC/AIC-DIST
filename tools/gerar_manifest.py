#!/usr/bin/env python3
"""Gera o manifest.json a partir da árvore de diretórios de binários.

Varre firmware/<dispositivo>/<canal>/<versao>/ e app/<dispositivo>/<canal>/<versao>/,
calcula tamanho e sha256 de cada binário e escreve o manifest.json na raiz.

Para arquivos .bin do ESP-IDF, também lê a versão embutida no cabeçalho
esp_app_desc_t e confere se ela bate com o nome do diretório -- é a rede de
segurança contra publicar uma build antiga num diretório de versão nova.

Uso:
    python3 tools/gerar_manifest.py              # escreve manifest.json
    python3 tools/gerar_manifest.py --verificar  # só valida, não escreve
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

BASE_URL = "https://raw.githubusercontent.com/WKA-AIC/AIC-DIST/main/"
SCHEMA = 1

# Nome legível de cada dispositivo, e onde a árvore dele começa.
DISPOSITIVOS = [
    {"id": "aic-p", "nome": "Painel", "tipo": "firmware", "raiz": "firmware/aic-p"},
    {"id": "aic-ds", "nome": "Driver de Sensores", "tipo": "firmware", "raiz": "firmware/aic-ds"},
    {"id": "aic-cr", "nome": "Aplicativo AIC-CR", "tipo": "apk", "raiz": "app/aic-cr"},
]

CANAIS = ("stable", "beta")

# SemVer 2.0.0, versão oficial da spec.
SEMVER = re.compile(
    r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)"
    r"(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+(?P<build>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
)

# Cabeçalho esp_app_desc_t: fica logo após o cabeçalho da imagem (24 B) e o do
# primeiro segmento (8 B), ou seja, no offset 0x20 do .bin. O campo version é
# char[32] no offset 0x10 da struct -> 0x30 no arquivo.
APP_DESC_OFFSET = 0x20
APP_DESC_MAGIC = 0xABCD5432
APP_DESC_VERSION_OFFSET = APP_DESC_OFFSET + 0x10
APP_DESC_PROJECT_OFFSET = APP_DESC_OFFSET + 0x30


class ErroValidacao(Exception):
    pass


def chave_semver(versao: str) -> tuple:
    """Chave de ordenação SemVer. Maior = mais nova.

    Um pré-lançamento é menor que o lançamento correspondente:
    1.2.0-beta.1 < 1.2.0. Por isso o flag `1` para quem não tem prerelease.
    """
    m = SEMVER.match(versao)
    if not m:
        raise ErroValidacao(f"versão fora do padrão SemVer: {versao!r}")

    nums = (int(m["major"]), int(m["minor"]), int(m["patch"]))
    pre = m["prerelease"]
    if pre is None:
        return (*nums, 1, ())

    partes = []
    for p in pre.split("."):
        # identificadores numéricos comparam como número e vêm antes dos textuais
        partes.append((0, int(p), "") if p.isdigit() else (1, 0, p))
    return (*nums, 0, tuple(partes))


def sha256_de(caminho: Path) -> str:
    h = hashlib.sha256()
    with caminho.open("rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def versao_embutida(caminho: Path) -> str | None:
    """Lê esp_app_desc_t.version de um .bin do ESP-IDF. None se não parecer um."""
    with caminho.open("rb") as f:
        f.seek(APP_DESC_OFFSET)
        cab = f.read(4)
        if len(cab) < 4 or struct.unpack("<I", cab)[0] != APP_DESC_MAGIC:
            return None
        f.seek(APP_DESC_VERSION_OFFSET)
        bruto = f.read(32)
    return bruto.split(b"\x00", 1)[0].decode("utf-8", "replace") or None


def projeto_embutido(caminho: Path) -> str | None:
    with caminho.open("rb") as f:
        f.seek(APP_DESC_OFFSET)
        cab = f.read(4)
        if len(cab) < 4 or struct.unpack("<I", cab)[0] != APP_DESC_MAGIC:
            return None
        f.seek(APP_DESC_PROJECT_OFFSET)
        bruto = f.read(32)
    return bruto.split(b"\x00", 1)[0].decode("utf-8", "replace") or None


def data_do_commit(caminho: Path) -> str:
    """Data do último commit que tocou o arquivo, em ISO-8601 UTC.

    Cai para a data de modificação do arquivo fora de um repositório git
    (ou quando o clone é raso e o commit não está presente).
    """
    try:
        saida = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", str(caminho.relative_to(RAIZ))],
            cwd=RAIZ, capture_output=True, text=True, check=True, timeout=30,
        ).stdout.strip()
        if saida:
            return datetime.fromisoformat(saida).astimezone(timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
    except (subprocess.SubprocessError, OSError, ValueError):
        pass
    return datetime.fromtimestamp(caminho.stat().st_mtime, timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def binario_de(dir_versao: Path, tipo: str) -> Path:
    ext = ".bin" if tipo == "firmware" else ".apk"
    achados = sorted(p for p in dir_versao.iterdir() if p.suffix == ext)
    if not achados:
        raise ErroValidacao(f"{dir_versao}: nenhum arquivo {ext}")
    if len(achados) > 1:
        nomes = ", ".join(p.name for p in achados)
        raise ErroValidacao(f"{dir_versao}: mais de um {ext} ({nomes}) — deixe apenas um")
    return achados[0]


def coletar_versoes(disp: dict, canal: str, erros: list[str]) -> list[dict]:
    dir_canal = RAIZ / disp["raiz"] / canal
    if not dir_canal.is_dir():
        return []

    itens = []
    for dir_versao in sorted(p for p in dir_canal.iterdir() if p.is_dir()):
        versao = dir_versao.name
        try:
            chave = chave_semver(versao)
            binario = binario_de(dir_versao, disp["tipo"])
        except ErroValidacao as e:
            erros.append(str(e))
            continue

        if disp["tipo"] == "firmware":
            embutida = versao_embutida(binario)
            if embutida is None:
                erros.append(
                    f"{binario.relative_to(RAIZ)}: não parece um binário de app do "
                    f"ESP-IDF (cabeçalho esp_app_desc_t não encontrado)"
                )
                continue
            if embutida != versao:
                erros.append(
                    f"{binario.relative_to(RAIZ)}: a versão embutida no binário é "
                    f"{embutida!r} mas o diretório diz {versao!r} — build errado publicado"
                )
                continue

        item = {
            "versao": versao,
            "arquivo": str(binario.relative_to(RAIZ)),
            "tamanho": binario.stat().st_size,
            "sha256": sha256_de(binario),
            "publicado_em": data_do_commit(binario),
        }
        if disp["tipo"] == "firmware":
            item["projeto"] = projeto_embutido(binario)

        notas = dir_versao / "notas.md"
        if notas.is_file():
            item["notas"] = str(notas.relative_to(RAIZ))

        itens.append((chave, item))

    itens.sort(key=lambda t: t[0], reverse=True)  # mais nova primeiro
    return [item for _, item in itens]


def montar() -> tuple[dict, list[str]]:
    erros: list[str] = []
    dispositivos = []

    for disp in DISPOSITIVOS:
        canais = {c: coletar_versoes(disp, c, erros) for c in CANAIS}
        dispositivos.append(
            {
                "id": disp["id"],
                "nome": disp["nome"],
                "tipo": disp["tipo"],
                "canais": canais,
            }
        )

    manifest = {
        "schema": SCHEMA,
        "gerado_em": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "base_url": BASE_URL,
        "dispositivos": dispositivos,
    }
    return manifest, erros


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--verificar",
        action="store_true",
        help="apenas valida a árvore; não escreve o manifest.json",
    )
    args = ap.parse_args()

    manifest, erros = montar()

    if erros:
        print("Problemas encontrados:", file=sys.stderr)
        for e in erros:
            print(f"  - {e}", file=sys.stderr)
        return 1

    total = sum(
        len(v) for d in manifest["dispositivos"] for v in d["canais"].values()
    )
    print(f"{total} versão(ões) catalogada(s).")
    for d in manifest["dispositivos"]:
        for canal, versoes in d["canais"].items():
            if versoes:
                print(f"  {d['id']}/{canal}: {', '.join(v['versao'] for v in versoes)}")

    if args.verificar:
        print("Modo --verificar: manifest.json não foi alterado.")
        return 0

    destino = RAIZ / "manifest.json"
    destino.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Escrito: {destino.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
