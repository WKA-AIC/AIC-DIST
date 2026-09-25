# AIC-DS 1.0.18

Publicado em 2026-09-25 · canal: beta

Build gerada a partir do commit `35f0d7f` do AIC-DS-FW.
`CONFIG_APP_PROJECT_VER` fixado em `1.0.18`. Inclui as versões 1.0.10 a 1.0.17,
que não foram publicadas separadamente.

## Novidades

- **Controle da válvula reguladora em dois regimes** (1.0.16/1.0.17):
  - Longe do alvo (erro acima de 15%): motor contínuo, sem limite de tempo,
    até a projeção do erro indicar que vai chegar perto; depois espera a
    vazão assentar.
  - Perto do alvo: pulso proporcional ao erro, dimensionado pela velocidade
    da válvula aprendida no próprio equipamento, seguido de espera.
  - As decisões perto do alvo usam a média das leituras tomadas com o motor
    parado, e a banda morta passou de 2,5%/1,0% para 5%/2%.
  - Em bancada, contra a 1.0.14: erro médio de 16,6% para 3,6%, motor ligado
    de 40 s para 2 s a cada 2 min, inversões de 70 para 7.
- **WebSocket `/ws/telemetry`** para o app AIC-CR:
  - Sentido de giro da válvula e duração exata de cada ordem (frame `valve`).
  - Comando manual da válvula pelo app, com botões de segurar para atuar.
    O comando expira sozinho 600 ms após o último frame e na queda da conexão.
  - Vazão, alvo e velocidade usados no controle, a 5 Hz (frame `flow`).
  - Calibração do fluxômetro (pulsos por litro) do painel, sob pedido do app
    (frame `flow_calib`).
- **DDI 0xF10B:** o driver pede ao painel a calibração do fluxômetro e guarda
  só em RAM, para repassar ao app. Requer painel AIC-P 1.0.16 ou superior.
- **Motivo do último reinício e coredump** do último travamento no `GET /info`
  (`resetReason`, `coredump`) e no início de cada captura de log pela rede
  (linhas `#LOG`), no mesmo formato do painel.
- **Log pela rede** (`/log/stream`) roda em task própria: o servidor segue
  atendendo o app (`/info`, lista de redes, atualização) com o log aberto.
- **Wi-Fi sem economia de energia:** latência de 3–8 ms em vez de 50–180 ms.

## Correções

- **PGN 65267** (posição GNSS) era descartada no filtro de recepção CAN desde
  a 1.0.8, e o driver considerava a posição sempre inválida.
- **Queda da captura de log pelo app a cada ~20 s:** o stream prendia o
  servidor HTTP, e as outras requisições do app estouravam o tempo limite.

## Atenção

- **O coredump só funciona em drivers gravados pela UART ao menos uma vez.**
  A partição `coredump` (64 KB em 0x320000) não é gravada por atualização via
  Wi-Fi. Sem ela, o `resetReason` funciona normalmente e o `coredump` vem
  `null`.
- **A lei de controle mudou bastante.** Validada só em bancada, com a vazão
  perto do alvo. O movimento contínuo com erro grande (degrau de velocidade ou
  partida com a válvula toda aberta) ainda não foi testado.
- Com a banda de 5%, um erro persistente entre 2% e 5% não é corrigido.
- A leitura do fluxômetro no GPIO36 continua ruidosa (variação de 8–12% com
  bomba elétrica estável). O controle agora ignora esse ruído, mas a leitura
  enviada ao painel segue oscilando.
- O log pela rede aceita um consumidor por vez: com o app capturando log,
  outra conexão de log recebe 409.
- Canal beta: validar em bancada e em campo antes de promover para produção.
