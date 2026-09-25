# AIC-P 1.0.15

Publicado em 2026-09-25 · canal: beta

Build gerada a partir do commit `dc8db17` do AIC-P.

## Requisito

- **Exige o aplicativo AIC-CR 1.1.0 ou superior**, como a 1.0.14.

## Novidades

- Nova origem de velocidade **Celular**: o app envia os fixes do GPS do
  celular pelo WS `/ws/telemetry` (`{"t":"phone_gps"}`) e o painel os repassa
  crus ao driver. Só em RAM: não aparece na tela "Origem Velocidade" nem é
  gravada na NVS; queda do WS ou 3 s sem frame voltam à origem anterior.
- `gnss_diag`/`gnss_data` passam a informar `fix_rate_hz` (leituras por
  segundo da origem ativa); `flow` passa a informar `work_status`.
  `gnss_diag.source` ganha o valor 4 (Celular).
- `GET /info` passa a informar `resetReason` e `coredump` (resumo do último
  pânico) para investigar reinícios sem serial.

## Correções

- Stream de log (`/log/stream`) roda em task própria: uma segunda tentativa
  ou o `/log/stop` não ficam mais travados, e sockets não se acumulam.
- Cotas de sockets separadas entre o servidor principal e o de log; antes,
  com o pool esgotado, toda conexão nova era recusada nas duas portas.
- Mensagens CAN enviadas pelo painel saem zeradas e com prioridade 6
  (antes podiam sair com prioridade/bytes aleatórios).

## Notas de engenharia

- Build gerada com `CONFIG_APP_PROJECT_VER=1.0.15` usando ESP-IDF v6.0.
- Coredump na flash habilitado, com partição `coredump` nova (64 KB em
  0x320000). **A tabela de partições não é gravada por OTA**: painéis
  atualizados só pelo app/Wi-Fi seguem sem a partição (o firmware apenas
  registra que ela não existe) até uma gravação pela UART.
- `CONFIG_LWIP_MAX_SOCKETS` 10 → 16; `CONFIG_FREERTOS_ISR_STACKSIZE`
  1536 → 2096.

## Atenção

- Canal beta: validar em bancada e em campo antes de promover para produção.
- A origem Celular depende de suporte no AIC-CR para enviar `phone_gps`.
- Permanecem as pendências de segurança registradas nas versões anteriores.
