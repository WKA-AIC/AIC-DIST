# AIC-DS 1.0.6

Publicado em 2026-09-18 · canal: beta

Build gerada a partir do commit `31b95cf` do AIC-DS-FW.
`CONFIG_APP_PROJECT_VER` fixado em `1.0.6`.

## O que mudou desde a 1.0.5
- Priorização automática da fonte de velocidade: usa o painel selecionado
  quando ele transmite e aceita outra ECU J1939 como fallback após três
  segundos sem mensagens do painel.
- Novo modo sem GPS quando nenhuma fonte de velocidade transmite por três
  segundos. Nesse modo, o controle usa a velocidade de trabalho configurada
  no painel em vez de continuar operando com a última leitura GPS congelada.
- Leitura da velocidade de trabalho configurada pelo novo DDI `0xF10A`, com
  solicitação automática durante a inicialização e atualização quando o
  operador salva um novo valor no painel.
- Telemetria do controle ampliada para indicar o modo sem GPS e registrar a
  velocidade efetivamente usada no cálculo.

## Atenção
- Versão beta para validação. O modo sem GPS depende de painel compatível com
  o DDI `0xF10A`; até receber a primeira resposta válida, o driver mantém a
  parada de segurança.
- Recomenda-se validar em bancada e em campo a troca entre painel, fonte J1939
  externa e modo sem GPS antes de uso em produção.
- Token de streaming/OTA ainda é fixo de desenvolvimento
  (`aic-log-dev-token`/`aic-ds-ota-dev-token`) — pendência de segurança
  conhecida, mantida das versões beta anteriores.
