# AIC-P 1.0.14

Publicado em 2026-09-23 · canal: beta

Build gerada a partir do commit `c5dbc5d` do AIC-P.

## Requisito

- **Exige o aplicativo AIC-CR 1.1.0 ou superior**, como a 1.0.13.

## Novidades

- Nenhuma alteração de código em relação à 1.0.13. Versão publicada para
  teste da atualização pelo aplicativo.

## Notas de engenharia

- Build gerada com `CONFIG_APP_PROJECT_VER=1.0.14` usando ESP-IDF v6.0.

## Atenção

- Canal beta: validar em bancada e em campo antes de promover para produção.
- O AIC-CR 1.1.0 não consegue atualizar o firmware quando o painel está
  conectado pela rede local (envia para o IP fixo 192.168.4.1). Correção em
  andamento no AIC-CR. Pela rede do próprio painel o envio segue funcionando.
- Permanecem as pendências de segurança registradas nas versões anteriores.
