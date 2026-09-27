# AIC-DS 1.0.21

Publicado em 2026-09-26 · canal: beta

Build gerada a partir do commit `5bf814a` do AIC-DS-FW.
`CONFIG_APP_PROJECT_VER` fixado em `1.0.21`.

## Novidades

- **Resposta da Regulagem** escolhida no painel (Configurações, item 4):
  - **Suave**: mais estável e lenta. Tolerância maior (volta a corrigir com
    7% de erro, para com 3%), espera 1,8 s entre correções e usa pulsos
    menores. Menos acionamentos da válvula.
  - **Normal** (padrão): o mesmo comportamento da 1.0.20.
  - **Rápida**: corrige mais cedo e mais perto do alvo (3,5% / 1,5%),
    reavalia após 1,0 s e usa pulsos exatos a partir de 80 ms. Aciona mais
    a válvula, aquece mais o motor e pode oscilar com vazão ruidosa.

## Atenção

- **Requer AIC-P 1.0.21 ou superior** para trocar o nível. Com painel
  anterior, o driver fica em Normal (igual à 1.0.20).
- Suave e Rápida ainda não foram validados em bancada.
- Canal beta: validar em bancada e em campo antes de promover para produção.
