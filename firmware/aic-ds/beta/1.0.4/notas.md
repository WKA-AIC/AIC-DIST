# AIC-DS 1.0.4

Publicado em 2026-09-15 · canal: beta

Build gerada a partir do trunk do AIC-DS-FW (1.0.3) com o streaming de log
em tempo real via WiFi (protocolo AIC-LOG/1): `GET /log/stream` e
`POST /log/stop`, consumidos pelo app AIC-CR. `CONFIG_APP_PROJECT_VER`
fixado em `1.0.4`.

## O que mudou desde a 1.0.3
- `GET /log/stream?token=aic-log-dev-token`: sessão de streaming em texto
  puro, chunked, de duração indefinida. Produtor (ciclo de controle da
  válvula, 100ms) nunca bloqueia - só copia o estado atual pra um snapshot
  compartilhado; consumidor roda na task própria do servidor HTTP.
- Início da sessão: `#GLOBALS` (várias linhas, nome=valor, com todas as
  variáveis globais do driver - heap, endereço J1939, diagnóstico TWAI,
  sensores/seções, heartbeat do painel, GPS, contadores de fluxo) seguido
  do `#MAP` (nome/posição/largura/escala de cada campo do controle da
  válvula) e então os registros `#SNAP`/`#D`/`#HB` - formato compacto de
  largura fixa em hexadecimal, sem rótulo por campo, pensado pra análise
  automatizada (não leitura humana direta).
- `POST /log/stop?token=aic-log-dev-token`: encerra a sessão.
- Telemetria/debug que saía pela UART sempre (`CTRL_TELEMETRY`,
  `VALVE_ACTUATOR_VERBOSE`, `TWAI_STATUS_LOG`) voltou a ficar desligada por
  padrão - só liga com troca explícita no código + recompilação.

## Atenção
- Requer o AIC-P numa versão que já solicite as DDIs 0xF108/0xF109 (mostrar
  versão/MAC do driver na tela WiFi) - mesma pendência já anotada na 1.0.3.
- Token de streaming/OTA ainda é fixo de desenvolvimento
  (`aic-log-dev-token`/`aic-ds-ota-dev-token`) - pendência de segurança
  conhecida, não um esquecimento.
