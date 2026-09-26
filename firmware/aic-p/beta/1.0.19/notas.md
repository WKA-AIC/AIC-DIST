# AIC-P 1.0.19

Publicado em 2026-09-25 · canal: beta

Build gerada a partir do commit `2c34dcb` do AIC-P.

## Requisito

- **Exige o aplicativo AIC-CR 1.1.0 ou superior**, como a 1.0.15.

## Correções

- GPS interno mostrando zero satélites, sem posição, hora nem velocidade,
  mesmo com o módulo GPS detectado. Com módulos que não enviam todas as
  sentenças NMEA (o da bancada não envia GLL nem VTG), o painel nunca
  atualizava os dados do GPS. Agora basta o módulo enviar GGA e RMC, como no
  firmware 0.5.

## Notas de engenharia

- Build gerada com `CONFIG_APP_PROJECT_VER=1.0.19` usando ESP-IDF v6.0.

## Atenção

- Canal beta: validar em bancada e em campo antes de promover para produção.
- Correção ainda não testada em hardware: conferir na bancada se o painel
  mostra os satélites com o mesmo módulo e antena em que o 0.5 mostra.
- Permanecem as pendências de segurança registradas nas versões anteriores.
