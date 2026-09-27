# AIC-P 1.0.23

Publicado em 2026-09-26 · canal: beta

Build gerada a partir do commit `6df1026` do AIC-P.

## Requisito

- **Exige o aplicativo AIC-CR 1.1.0 ou superior**, como a 1.0.15.

## Novidades

- Tela "Resposta da Regulagem" no menu de configurações, logo após
  "Velocidade de Trabalho": Suave, Normal (padrão) ou Rápida. Define o quão
  rápido e o quão de perto a válvula reguladora do driver corrige a vazão. A
  escolha fica salva no painel e é enviada ao driver ao salvar e quando o
  driver pede, ao ligar. Depende de um driver AIC-DS com suporte a esse
  ajuste; sem ele, o driver continua no comportamento Normal.
- O aplicativo passa a poder mostrar a mesma vazão (L/ha) que o visor do
  painel, com a trava no alvo, em vez da leitura instantânea. Aplicativos que
  não conhecem o novo campo continuam funcionando.

## Mudanças

- Removido do menu o item "Média Sementes", que não tinha função.

## Atenção

- Na atualização, a escolha de quais itens do menu são "avançados" (tela
  "Config. Menu") volta ao padrão: todos os itens aparecem, exceto o próprio
  "Config. Menu". Remarque os itens que quiser esconder.
- Canal beta: validar em bancada e em campo antes de promover para produção.
  As novidades desta versão ainda não foram testadas em hardware.
- Permanecem as pendências de segurança registradas nas versões anteriores.

## Notas de engenharia

- Build gerada com `CONFIG_APP_PROJECT_VER=1.0.23` usando ESP-IDF v6.0.
- Telemetria: frame "flow" ganha `l_ha_display` (float, L/ha).
- CAN: DDI 0xF10C (PGN 51968), Info[0] = 0 Suave / 1 Normal / 2 Rápida.
- Marcadores de menu avançado agora na chave NVS `menuAdvTelas`, por tela e
  não por posição; a chave antiga `menuAdvFlags` não é mais lida.
