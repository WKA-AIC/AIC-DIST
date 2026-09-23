# AIC-P 1.0.11

Publicado em 2026-09-23 · canal: beta

## Novidades

- Diagnóstico da frequência real do GNSS NMEA baseado em sentenças RMC,
  reconhecendo as taxas padrão de 1, 2, 4, 5 e 10 Hz.
- Telemetria e processamento de dados GNSS sinalizados por atualização de
  fix, em vez de depender apenas de um intervalo fixo.
- Filtro Kalman-UBX restaura as sentenças NMEA padrão ao ser desativado,
  permitindo a retomada correta dos modos Kalman-NMEA e Sinal Puro.

## Correções

- Melhorada a leitura inicial do GPS: a detecção não corta um ciclo NMEA
  longo e a medição aguarda uma janela completa após o primeiro RMC.
- Melhorada a quebra de texto nas telas de alerta de velocidade para evitar
  sobreposição e manter a leitura do valor atual.

## Notas de engenharia

- Build gerada com `CONFIG_APP_PROJECT_VER=1.0.11` usando ESP-IDF v6.0.
- Binário validado pelo verificador de versão embutida do AIC-DIST.

## Atenção

- Canal beta: validar em bancada e em campo antes de promover para produção.
- Permanecem as pendências de segurança registradas nas versões anteriores.
