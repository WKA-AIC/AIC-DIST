# AIC-DS 1.0.19

Publicado em 2026-09-26 · canal: beta

Build gerada a partir do commit `84b44d5` do AIC-DS-FW.
`CONFIG_APP_PROJECT_VER` fixado em `1.0.19`.

## Correções

- **Reinício por brownout ~1,8 s após o boot** em drivers alimentados só pelo
  chicote (LM7805 -> DevKitC): o Wi-Fi volta a usar economia de energia
  (`WIFI_PS_MIN_MODEM`), desfazendo a mudança da 1.0.11/1.0.18 que mantinha o
  rádio sempre ligado.

## Atenção

- A latência do Wi-Fi volta a 50–180 ms (na 1.0.18 era 3–8 ms). App, log pela
  rede e atualização continuam funcionando, só respondem mais devagar.
- As observações da 1.0.18 continuam valendo (coredump só após gravação pela
  UART, lei de controle validada só em bancada, banda de 5%/2%).
- Canal beta: validar em bancada e em campo antes de promover para produção.
