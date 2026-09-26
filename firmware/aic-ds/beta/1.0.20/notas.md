# AIC-DS 1.0.20

Publicado em 2026-09-26 · canal: beta

Build gerada a partir do commit `a89c1be` do AIC-DS-FW.
`CONFIG_APP_PROJECT_VER` fixado em `1.0.20`.

## Correções

- **Vazão do fluxômetro zerada durante a calibração**: com o painel em
  calibração (ou com o sensor/CAN parado) o driver zerava a medição a cada
  100 ms, e o painel/app mostravam os pulsos/s reais só por um instante e
  depois 0. Agora a parada de segurança só para a válvula reguladora e
  reinicia a lei de controle; a medição do fluxômetro (DDI 0xF101) segue
  sendo enviada normalmente.

## Atenção

- As observações da 1.0.19 continuam valendo (Wi-Fi em economia de energia,
  latência de 50–180 ms).
- Canal beta: validar em bancada e em campo antes de promover para produção.
