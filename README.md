# AIC-DIST — distribuição pública de binários

Repositório **público** do projeto **AIC** (*Agricultural Implement Controller*).
Contém apenas artefatos prontos para instalação:

- firmwares do **Painel** (`AIC-P`) e do **Driver de Sensores** (`AIC-DS`);
- APKs do aplicativo **AIC-CR** (Controle Remoto / atualizador).

O código-fonte fica em repositórios privados. Aqui não há fonte, esquemático,
chave nem token — só binários, hashes e notas de versão.

---

## Canais

| Canal | Diretório | Para quem |
|---|---|---|
| **Produção** | `stable/` | Uso em campo. Versões validadas. |
| **Testes** | `beta/` | Validação. Podem conter defeitos. |

---

## Estrutura

```
firmware/<dispositivo>/<canal>/<versao>/<binario>.bin
app/<dispositivo>/<canal>/<versao>/<binario>.apk
```

Exemplos:

```
firmware/aic-p/stable/1.1.0/AIC-P-FW.bin
firmware/aic-ds/beta/1.2.0-beta.1/AIC-DS-FW.bin
app/aic-cr/stable/1.0.0/AIC-CR-1.0.0.apk
```

Cada diretório de versão pode ter um `notas.md` com o que mudou.

---

## `manifest.json`

Catálogo único, consumido pelo aplicativo:

```
https://raw.githubusercontent.com/WKA-AIC/AIC-DIST/main/manifest.json
```

**É gerado automaticamente. Não edite à mão.** A cada push que toque
`firmware/` ou `app/`, uma GitHub Action roda `tools/gerar_manifest.py` e
recommita o arquivo.

A URL de download de qualquer artefato é `base_url` + o campo `arquivo` do
manifest.

---

## Publicando uma versão nova

```bash
V=1.2.0

mkdir -p firmware/aic-p/stable/$V
cp ~/AIC/painel/AIC-P-FW/build/AIC-P-FW.bin firmware/aic-p/stable/$V/
$EDITOR firmware/aic-p/stable/$V/notas.md

git add firmware/aic-p/stable/$V
git commit -m "AIC-P $V (stable)"
git push
```

Só isso. Não calcule hash, não edite o manifest.

Para conferir antes de subir:

```bash
python3 tools/gerar_manifest.py --verificar
```

O verificador **recusa** um `.bin` cuja versão embutida
(`esp_app_desc_t.version`) não seja igual ao nome do diretório. É a proteção
contra o erro mais provável: copiar a build errada.

---

## Instalando o aplicativo AIC-CR

O APK não vem da Play Store, então o Android pede autorização uma vez:

1. Baixe o `.apk` do canal desejado.
2. Ao abrir, o Android vai pedir para permitir **"Instalar apps desconhecidos"**
   para o navegador ou gerenciador de arquivos usado. Autorize.
3. Instale.

As variantes de produção e de testes têm identificadores diferentes
(`com.wka.aic.cr` e `com.wka.aic.cr.beta`) e **convivem no mesmo celular** — dá
para testar uma versão nova sem perder a que funciona.

---

## Verificando a integridade de um download

O `sha256` de cada arquivo está no `manifest.json`.

```bash
sha256sum AIC-P-FW.bin
```

O aplicativo faz essa conferência sozinho, e o ESP32 confere de novo antes de
ativar a imagem gravada.

---

## Licença

Consulte `LICENSE`. Os binários são distribuídos para uso com equipamentos AIC.
