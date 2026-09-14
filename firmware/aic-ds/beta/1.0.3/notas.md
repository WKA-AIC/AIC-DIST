# AIC-DS 1.0.3

Publicado em 2026-09-14 · canal: beta

Build gerada a partir do trunk do AIC-DS-FW (1.0.2) com o pacote WiFi/OTA
mesclado: servidor HTTP, `wifi_manager`, `ota_manager` e as DDIs
0xF106-0xF109 (heartbeat com versão de firmware embutida, SSID
`AIC-DS-XXXX` a partir do MAC, ativação remota do WiFi e endpoint de
atualização). `CONFIG_APP_PROJECT_VER` fixado em `1.0.3`.

## Atenção
- Requer o AIC-P também numa versão que solicite as DDIs 0xF108/0xF109
  (painel mostra versão/MAC do driver na tela WiFi) - ver
  `firmware/aic-p/beta/1.0.3` ou superior.
