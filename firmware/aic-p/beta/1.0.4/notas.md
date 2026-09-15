# AIC-P 1.0.4

Publicado em 2026-09-15 · canal: beta

## Novidades
- Novo endpoint WebSocket `GET /ws/telemetry` (porta 80): espelha em tempo
  real, pro app AIC-CR, o status/configuração das 4 seções (mesma regra de
  "pisca" da tela local). Envia o snapshot completo assim que o app conecta
  e depois a cada mudança (resolução de ~100ms). Formato extensível
  (`"t"`/`"v"`) para novas categorias de telemetria no futuro.
- O app agora pode mandar comandos pelo mesmo WebSocket:
  - `set_sensor_type`: troca o tipo de sensor de uma seção (Roda/Levante/
    Manual) em tempo real - mesmo efeito da tela local de cadastro,
    inclusive a persistência na NVS.
  - `toggle_section`: alterna uma seção em modo manual - mesmo efeito de
    apertar a tecla física da seção, com a mesma trava (só funciona se a
    seção estiver em modo manual).
- Novo servidor de log remoto em tempo real (porta 8081, `GET /log/stream` +
  `POST /log/stop`, com token): espelha pro app todo log de runtime do
  painel (o mesmo que já ia pra UART), exceto as mensagens de boot. Roda
  numa instância HTTP própria pra não travar o espelhamento de seções
  enquanto uma sessão de log estiver ativa.
- Corrigida uma condição em que uma conexão WiFi problemática (app fora de
  alcance, socket travado) podia prender a tecla power e deixar o painel
  "preso" na tela de desligamento, precisando resetar pra sair. Agora o
  socket do WebSocket de telemetria tem timeout de envio (2s), igual ao do
  log.
- O WiFi do painel (rádio + os dois servidores HTTP) agora desliga
  automaticamente ao apertar a tecla power - economiza bateria no modo
  "dormindo" aguardando ser religado. Volta a subir sozinho no próximo boot,
  conforme a preferência salva na tela "Conexão WiFi".

## Atenção
- Mesmas pendências de segurança das versões anteriores (SoftAP aberto,
  token de update fixo, tokens de log fixos de desenvolvimento).
- O comando `toggle_section` só tem efeito em seções cadastradas como
  "Manual" - em qualquer outro tipo de sensor, quem manda é a chave física
  da caixa, não o app (mesma regra de sempre).
