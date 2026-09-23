# AIC-DS 1.0.8

Publicado em 2026-09-23 · canal: beta

Build gerada a partir do commit `844232f` do AIC-DS-FW, com as alterações
presentes na árvore de trabalho no momento da compilação.
`CONFIG_APP_PROJECT_VER` fixado em `1.0.8`.

## Novidades
- Adiciona recepção da posição GNSS via PGN 65267, com arbitragem entre o
  painel e o trator e detecção de posição indisponível.
- Expõe a origem do último sinal de velocidade aceito e usa a validade da
  posição GNSS no controle de segurança da válvula.
- Mantém o diagnóstico de CAN, Wi-Fi e log em tempo real introduzido nas
  versões beta anteriores.

## Atenção
- Versão beta para validação em bancada e em campo.
- Inclui as alterações locais ainda não commitadas do AIC-DS-FW no momento da
  build.

