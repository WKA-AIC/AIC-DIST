# AIC-DS 1.0.0

Publicado em 2026-09-14 · canal: stable

Build gerada a partir do trunk do AIC-DS-FW anterior às correções de campo
de 04/09 e ao pacote WiFi/OTA (commit `61c27e4`, "Migra driver TWAI para
API nova e implementa reivindicação de endereço J1939"), com
`CONFIG_APP_PROJECT_VER` fixado em `1.0.0` - primeira versão numerada do
projeto, que até aqui só embutia o hash curto do commit como versão.

## Atenção
- Não inclui as correções de válvula reguladora, fluxômetro fora de faixa
  e J1939 aplicadas depois em campo (ver 1.0.2) nem o pacote WiFi/OTA
  (ver 1.0.3). Publicada como stable por ser o ponto de referência
  histórico do trunk antigo, não porque seja a build recomendada para uso
  atual em campo.
- Primeira publicação do AIC-DS neste repositório de distribuição; sem
  changelog anterior pra comparar.
