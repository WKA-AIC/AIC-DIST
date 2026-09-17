# AIC-P 1.0.7

Publicado em 2026-09-17 · canal: beta

## Novidades
- Seleção de driver AIC-DS (SA/NAME) persistida na NVS: se dois (ou mais)
  drivers aparecerem no barramento, o painel exige que o operador escolha
  qual usar; em boots seguintes, se o mesmo conjunto de candidatos
  reaparecer, a escolha é reaplicada automaticamente sem perguntar de novo.
- Recepção de telemetria do driver (PGN51968) agora filtrada pelo SA do
  driver selecionado - mensagens de qualquer outro dispositivo no barramento
  com o mesmo DDI são ignoradas.
- Painel envia um pedido (Request) de Address Claimed ao iniciar a busca por
  driver, para descobrir também drivers que já estavam ligados antes do
  painel.
- A busca por driver agora dura o boot inteiro (antes eram só 500ms fixos):
  o painel não abre a tela principal sem pelo menos um driver confirmado -
  sem nenhum, mostra "AGUARDANDO DRIVER" na própria tela de inicialização e
  continua tentando sozinho, sem precisar reiniciar; a tecla de ligar/desligar
  continua funcionando normalmente nesse estado.
- Novo alerta "DRIVER DESCONECTADO": se o heartbeat do driver falhar por
  1,5s seguidos, o painel força as seções para fechado (evita mostrar
  "trabalhando" com o driver fora do ar) e exibe o alerta periodicamente até
  o driver voltar a responder, quando a operação normal é restaurada
  automaticamente.

## Notas de engenharia
- Sequência de inicialização (boot) do painel reordenada e auditada: o relé
  que energiza o driver remoto agora é acionado bem cedo, isolado de
  qualquer comunicação serial (SPI/I2C/UART), para evitar interferência
  eletromagnética da bobina em uma transação em andamento.
- Pequenas correções de ordem de inicialização sem impacto funcional
  observável (cálculo de largura efetiva antes da task que o consome,
  deduplicação da lógica de conexão do GPS).

## Atenção
- Mesmas pendências de segurança das versões anteriores (SoftAP aberto,
  token de update fixo, tokens de log fixos de desenvolvimento).
- Testado em bancada com simulador de barramento (dois drivers simulados);
  ainda não validado em campo com dois drivers AIC-DS físicos reais.
