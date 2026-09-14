# AIC-DS 0.5.0

Publicado em 2026-09-14 · canal: beta

Build gerada a partir da branch `legacy-v0.5` do AIC-DS-FW (commit
`8732ec3`, "Corrige resets do LEDC e oscilação da válvula"), com
`CONFIG_APP_PROJECT_VER` fixado em `0.5.0` para esta publicação.
Compilada com ESP-IDF 5.3.5 (o legacy usa a driver TWAI antiga e a API
`gpio_config_t` anterior, incompatíveis com o toolchain 6.0 usado nas
demais versões).

## Atenção
- Linha de código legada, anterior à reescrita do controle de válvula/J1939
  do trunk atual. Mantida como beta de referência, não como recomendação
  de uso sobre o trunk (1.0.2/1.0.3).
