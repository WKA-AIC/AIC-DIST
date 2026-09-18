# AIC-P 1.0.8

Publicado em 2026-09-18 · canal: beta

## Novidades

- Ao fechar a última seção do implemento, a vazão instantânea é zerada: os
  campos de litros por minuto e litros por hectare não mantêm a última leitura
  depois que o trabalho é interrompido.
- A inicialização e a recuperação de cadastros incompletos usam valores mínimos
  seguros (duas seções com cinco bicos cada e espaçamento de 50 cm), evitando
  cálculos inválidos quando o operador ainda não cadastrou o implemento.
- O painel protege o cálculo de vazão quando não há largura efetiva ou nenhuma
  seção ativa, limpando também o histórico do filtro de vazão.
- Diagnósticos de CAN/TWAI e ausência de heartbeat do driver são encaminhados
  ao Log do Wi-Fi, incluindo erros, mudanças de estado e falhas de transmissão.
- Diagnósticos de GNSS/NMEA/UBX foram ampliados para facilitar a identificação
  de falhas de comunicação e de configuração do receptor.

## Notas de engenharia

- Build gerada com `CONFIG_APP_PROJECT_VER=1.0.8` usando ESP-IDF v6.0.
- Binário validado pelo verificador de versão embutida do AIC-DIST.

## Atenção

- Canal beta: validar em bancada e em campo antes de promover para produção.
- Permanecem as pendências de segurança registradas nas versões anteriores.
