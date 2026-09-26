# AIC-P 1.0.18

Publicado em 2026-09-25 · canal: beta

Build gerada a partir do commit `97031e6` do AIC-P.

## Requisito

- **Exige o aplicativo AIC-CR 1.1.0 ou superior**, como a 1.0.15.

## Correções

- Painel sem comunicação com o driver depois de trocar ou desligar o driver
  sem reiniciar o painel. O painel guardava o driver antigo para sempre:
  continuava mandando os comandos para o endereço dele e descartava o
  heartbeat do driver novo. Agora, driver que fica 3 s sem mandar nada sai
  da lista de drivers conhecidos.
- Se o driver escolhido sai do ar e sobra um único driver respondendo, o
  painel passa a usar esse e grava a escolha. Não troca sozinho quando o
  operador escolheu entre vários drivers.
- Sem nenhum driver respondendo, o painel pede o anúncio de endereço a cada
  2 s, para achar um driver que já estava no barramento.

## Notas de engenharia

- Build gerada com `CONFIG_APP_PROJECT_VER=1.0.18` usando ESP-IDF v6.0.

## Atenção

- Canal beta: validar em bancada e em campo antes de promover para produção.
- Correção ainda não testada em hardware: validar trocando o driver com o
  painel ligado.
- Permanecem as pendências de segurança registradas nas versões anteriores.
