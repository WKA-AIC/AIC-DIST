# AIC-P 1.0.1

Publicado em 2026-09-12 · canal: beta (movida de stable em 2026-09-13 -
canal stable reservado pra 1.0.0/0.5.0, sem Wi-Fi/OTA)

## Novidades
- Wi-Fi: equipamento sobe SoftAP (`AIC-P-XXXX`) no boot, com API HTTP/JSON
  de descoberta e provisionamento (`/info`, `/wifi/scan`,
  `/wifi/configure`, `/wifi/switch-to-ap`).
- OTA via Wi-Fi: endpoint `POST /update` grava a imagem nova na partição
  OTA inativa e troca o boot pra ela. Suporta upgrade e downgrade (esta é
  a primeira versão com capacidade real de receber OTA).
- Tabela de partições migrada pro esquema dual-OTA (`ota_0`/`ota_1` +
  `otadata`), aproveitando os 4MB reais de flash do módulo (o projeto
  estava configurado para 2MB por engano).
- Rollback automático habilitado: um OTA que deixe o equipamento em loop
  de reinicialização volta sozinho pra partição anterior.

## Atenção
- Equipamentos já em campo com a tabela de partições antiga (single-app)
  precisam ser regravados via UART uma vez para ganhar os slots OTA -
  não há como migrar a tabela de partições por OTA.
- SoftAP de provisionamento ainda é aberto (sem senha) e o endpoint
  `/update` usa um token fixo de desenvolvimento - pendências de
  segurança conhecidas, a revisar antes de produto comercial final.
