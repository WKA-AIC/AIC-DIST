# AIC-P 1.0.10

Publicado em 2026-09-22 · canal: beta

## Novidades
- Calibração manual do fluxômetro agora pode ser disparada remotamente
  pelo app AIC-CR (WebSocket `start_remote_calibration`/
  `confirm_remote_calibration`/`cancel_remote_calibration`), espelhando a
  tela física "Calib. Manual Fluxômetro": nova tela informativa no painel
  (sem teclado numérico ativo - a digitação do ml coletado acontece no
  app), volta sozinha pra tela em que o painel estava antes de o app
  disparar o comando (não sempre pro menu), e avisa o app
  (`remote_calibration_cancelled`) se o operador cancelar pelo próprio
  painel físico.
- Telemetria "flow" (WebSocket) ganhou dois campos novos:
  `pulses_per_second` (leitura instantânea de pulsos/s do fluxômetro) e
  `pulses_per_second_avg` (média acumulada durante a calibração, ver
  abaixo).

## Correções
- Corrigido falso alerta "DRIVER DESCONECTADO" disparado ao sair de
  **qualquer** calibração do fluxômetro (física ou remota): o painel só
  processava a mensagem CAN que carrega o heartbeat do driver (e a
  contagem de pulsos do fluxômetro) enquanto em operação normal: durante
  a calibração ela ficava sendo descartada sem processar, então o
  heartbeat "envelhecia" sem atualização e o alerta disparava assim que a
  calibração terminava, mesmo com o driver nunca tendo parado de
  responder. Bug pré-existente (não introduzido nesta versão), só
  ficou mais visível com a calibração remota por durar mais tempo em
  média.
- Mesma causa acima também deixava a leitura de pulsos/segundo do
  fluxômetro congelada durante toda a calibração (parava de atualizar a
  partir do instante em que a tela era aberta) - a fórmula da calibração
  podia estar usando um valor de um único instante em vez do fluxo real
  durante a coleta do volume.

## Notas de engenharia
- Nova média incremental (cumulative moving average) de pulsos/segundo,
  acumulada durante toda a permanência na tela de calibração (memória
  O(1) - não cresce com o tempo, funciona igual para uma calibração de
  segundos ou de horas). Usada na fórmula de pulsos-por-litro e exibida
  nas telas física e remota, para diluir pequenas variações normais do
  sistema hidráulico (mangueiras, rotação da bomba etc.) com o
  equipamento parado.

## Atenção
- Mesmas pendências de segurança das versões anteriores (SoftAP aberto,
  token de update fixo, tokens de log fixos de desenvolvimento).
- Testado em bancada (calibração física e remota, com captura de log ao
  vivo do driver via Wi-Fi/serial durante a reprodução); ainda não
  validado em campo.
