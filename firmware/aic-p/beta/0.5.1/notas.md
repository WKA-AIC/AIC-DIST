# AIC-P 0.5.1

Publicado em 2026-09-12 · canal: beta

## Novidades
- Mesmo pacote de Wi-Fi + OTA da `1.0.1` (ver notas dessa versão),
  portado pra branch legada (`legacy-v0.5`, mantida para compatibilidade
  com drivers AIC-DS nessa revisão).
- Passa a suportar OTA (upgrade e downgrade) - a `0.5.0` publicada
  anteriormente não tinha essa capacidade.

## Atenção
- Mesmas pendências de segurança da `1.0.1` (SoftAP aberto, token de
  update fixo).
- Equipamentos com a tabela de partições antiga precisam ser regravados
  via UART uma vez para ganhar os slots OTA.
