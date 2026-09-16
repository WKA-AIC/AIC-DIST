# AIC-P 1.0.5

Publicado em 2026-09-16 · canal: beta

## Novidades
- Protocolo de telemetria (`GET /ws/telemetry`) estendido com novas
  mensagens e comandos, pro app AIC-CR:
  - Outbound: `speed` (velocidade atual + fonte) e `reports` (horímetro,
    hectarímetro e odômetro, parciais e totais) - `reports` é enviado a
    cada ~3 segundos reais, sempre, sem depender de detecção de mudança.
  - Inbound: `set_speed_source` (troca a fonte de velocidade - GPS interno,
    J1939 ou simulado - sem precisar da tela local), `nudge_simulated_speed`
    (incrementa/decrementa a velocidade simulada), `toggle_all_manual_
    sections` (abre/fecha todas as seções manuais de uma vez, mesmo efeito
    das teclas físicas V/X), e `clear_partial_worktime`/`clear_partial_area`/
    `clear_partial_odometer` (zera cada relatório parcial individualmente,
    mesmo efeito da tela local "Limpar Relatórios").

## Correções
- Horímetro e hectarímetro parciais estavam inflando o valor acumulado
  sempre que uma seção era aberta/fechada durante o trabalho (a task de
  cálculo assumia um intervalo fixo de 3s por ciclo, mas podia ser
  interrompida antes da hora por essas trocas). Agora usa o tempo real
  decorrido entre medições.
- Implementado o acúmulo dos relatórios TOTAIS (horímetro, hectarímetro e
  odômetro) - antes existiam só como campos zerados, sem nenhuma lógica de
  acúmulo.
- Implementado o odômetro (parcial e total), que não existia antes.
- A leitura de velocidade (`vlSpeedMedia`) podia ficar "grudada" no último
  valor recebido para sempre - por exemplo, trocar de velocidade simulada
  para GPS/J1939 sem tráfego real no barramento mantinha exibido o valor
  simulado antigo. Agora expira automaticamente se nenhuma mensagem de
  velocidade chegar por 3 segundos, e zera imediatamente ao trocar de fonte.
- A suavização da leitura de velocidade J1939 assumia GPS transmitindo a
  1Hz fixo; ECUs de trator podem transmitir em outras frequências permitidas
  pela norma (2Hz, 4Hz...). Agora a frequência real é medida e a janela de
  suavização se ajusta automaticamente.
- Corrigido um bug de dispatch da telemetria: nomes de comando com mais de
  23 caracteres (como `toggle_all_manual_sections`) eram truncados por um
  buffer pequeno demais e nunca reconhecidos - o app via o envio ter
  sucesso, mas o painel não fazia nada, sem nenhum log de erro.
- Melhorias de eficiência no filtro de mensagens CAN/J1939 (menos
  processamento de tráfego irrelevante num barramento compartilhado com
  ISOBUS) e correção de um caso em que a fila de recebimento CAN podia
  processar só uma mensagem por ciclo mesmo com várias pendentes.

## Atenção
- Mesmas pendências de segurança das versões anteriores (SoftAP aberto,
  token de update fixo, tokens de log fixos de desenvolvimento).
- `toggle_section`/`toggle_all_manual_sections` só têm efeito em seções
  cadastradas como "Manual" - em qualquer outro tipo de sensor, quem manda é
  a chave física da caixa, não o app (mesma regra de sempre).
- `set_speed_source`/`nudge_simulated_speed` nunca gravam na NVS - são
  efêmeros, mesma garantia que o long-press físico já tinha.
