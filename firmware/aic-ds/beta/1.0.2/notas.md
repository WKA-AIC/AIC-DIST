# AIC-DS 1.0.2

Publicado em 2026-09-14 · canal: beta

Build gerada a partir do trunk do AIC-DS-FW após consolidar as correções
de campo testadas em 04/09 (branch `port-legacy-fixes`, promovida a
trunk nesta sessão): regulagem da válvula reguladora (acionamento GPIO
liga/desliga), fluxômetro saturando ALTO em vez de zerar acima da faixa
medível, robustez do J1939 e piso de vazão mínima (DDI 0xF103). Não
inclui o pacote WiFi/OTA (ver 1.0.3). `CONFIG_APP_PROJECT_VER` fixado em
`1.0.2`.

## Atenção
- Sem WiFi/OTA - use 1.0.3 se precisar dessas DDIs (0xF106-0xF109).
