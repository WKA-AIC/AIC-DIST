# AIC-P 1.0.13

Publicado em 2026-09-23 · canal: beta

Build gerada a partir do commit `989faae` do AIC-P.

## Requisito

- **Exige o aplicativo AIC-CR 1.1.0 ou superior**, como a 1.0.12. Versões
  anteriores do app exibem o log CAN do painel corrompido e não acompanham o
  estado da calibração remota.

## Novidades

- `GET /info` passa a informar `appSha256` (hash do build rodando) e
  `uptimeMs` (tempo desde o boot). Os dois campos são novos e não mudam os que
  já existiam.
- Script `gravar.py` no repositório: grava o firmware por Wi-Fi no único
  AIC-P da rede local e confirma pelo hash do build.

## Notas de engenharia

- Build gerada com `CONFIG_APP_PROJECT_VER=1.0.13` usando ESP-IDF v6.0.
- Inclui tudo o que entrou na 1.0.12 (espelho da tela, calibração remota
  resiliente, log CAN em texto, pausa do dashboard em segundo plano).

## Atenção

- Canal beta: validar em bancada e em campo antes de promover para produção.
- Gravação por Wi-Fi com o `gravar.py` testada em painel físico. As funções
  novas da 1.0.12 ainda não foram testadas em campo com o app atualizado.
- Permanecem as pendências de segurança registradas nas versões anteriores.
