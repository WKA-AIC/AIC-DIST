# AIC-DS 1.0.5

Publicado em 2026-09-16 · canal: beta

Build gerada a partir do trunk do AIC-DS-FW (1.0.4), com duas mudanças de
robustez no CAN/J1939. `CONFIG_APP_PROJECT_VER` fixado em `1.0.5`.

## O que mudou desde a 1.0.4
- Filtro de PGN aplicado dentro da própria ISR de RX do TWAI
  (`twai_on_rx_done`), antes de a mensagem ocupar uma vaga no FIFO
  `xQueueCAN`: como o controlador TWAI do ESP32 não tem slots de hardware
  suficientes para isolar por PGN (as PGNs relevantes não são contíguas em
  bits), o filtro de hardware aceita todos os frames estendidos e o
  descarte passou a ser feito em software, em ISR, com uma whitelist das
  PGNs que o driver efetivamente trata (60928 Address Claimed/Cannot Claim,
  59904 Request, 65256 Vehicle Speed, 51968 sub-protocolo proprietário
  DDI). Evita que tráfego irrelevante de outras ECUs do trator (motor,
  câmbio, GPS etc., em barramentos J1939/ISOBUS cheios) estoure a fila e
  derrube mensagens que realmente importam para a comunicação
  painel↔driver. `FIFO_LENGTH` de 10 para 32 (com filtro aplicado, o
  tráfego que entra na fila já é só o relevante; o aumento é folga para
  absorver rajadas pontuais). Mesmo padrão já validado em bancada no
  firmware do painel (AIC-P-FW).
- `handlePGN65256`: a janela do buffer circular de média da velocidade GPS
  deixou de ser dimensionada assumindo 1Hz fixo (`idFreqGPS`, nunca medido
  de verdade) e passou a ser calculada a partir do período real medido
  entre mensagens (`esp_timer_get_time()`, suavizado por média móvel
  exponencial). Como a J1939 permite ECUs de GPS/velocidade transmitindo
  PGN65256 em frequências diferentes por fabricante/config do trator, a
  suposição fixa de 1Hz encolhia ou alongava a janela real de suavização
  dependendo da frequência real — o que chegava a alimentar
  `fltSpeedMetersPerSecond`, usado direto no cálculo de erro do controle
  de vazão da válvula. Mesmo padrão aplicado no painel (AIC-P-FW).

## Atenção
- Validado em bancada com driver e painel reais no mesmo barramento CAN:
  log temporário no dispatch confirmou que o filtro deixa passar só
  PGN51968 (heartbeat e DDIs do painel) e nada mais; sem panics/crashes
  observados no log serial após o flash.
- Token de streaming/OTA ainda é fixo de desenvolvimento
  (`aic-log-dev-token`/`aic-ds-ota-dev-token`) — pendência de segurança
  conhecida, não um esquecimento (mesma nota da 1.0.4).
