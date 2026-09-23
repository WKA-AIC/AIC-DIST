# AIC-DS 1.0.9

Publicado em 2026-09-23 · canal: beta

Build gerada a partir do commit `ad2d16f` do AIC-DS-FW.
`CONFIG_APP_PROJECT_VER` fixado em `1.0.9`.

## Novidades

- `GET /info` passa a informar `appSha256` (hash do build rodando) e
  `uptimeMs` (tempo desde o boot). Os dois campos são novos e não mudam os que
  já existiam.
- Script `gravar.py` no repositório: grava o firmware por Wi-Fi no único
  AIC-DS da rede local e confirma pelo hash do build.

## Atenção

- Versão beta para validação em bancada e em campo.
- Sem mudança no controle da válvula nem na comunicação CAN em relação à
  1.0.8.
- Ainda não testada em driver físico: nenhum AIC-DS estava na rede no
  momento da publicação.
