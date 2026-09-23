# AIC-P 1.0.12

Publicado em 2026-09-23 · canal: beta

## Requisito

- **Exige o aplicativo AIC-CR 1.1.0 ou superior.** Versões anteriores do app
  exibem o log CAN do painel corrompido e não acompanham o novo estado da
  calibração remota. Atualize o app junto com este firmware.

## Novidades

- Espelho ao vivo do display do painel na tela "Controle Remoto" do app.
- Calibração remota do fluxômetro resiliente à queda do app: o painel mostra
  "App desconect." com contagem e cancela sozinho após 60 s sem reconexão; o
  app recebe o estado da calibração e o motivo do encerramento (salva,
  inválida, cancelada no app, cancelada no painel, tempo esgotado).
- Log CAN via Wi-Fi em texto, no mesmo formato do AIC-DS (`@R` recebido,
  `@T` transmitido), incluindo agora as mensagens transmitidas pelo painel.
  Só registra tráfego de dispositivos AIC; com a velocidade vinda do trator
  (GPS ISOBUS), inclui também as mensagens de velocidade, posição e
  data/hora do trator.
- Com o app em segundo plano, o painel pausa o envio dos dados do dashboard
  e retoma com um retrato completo ao voltar.

## Correções

- Conexões do app que somem sem se despedir (fora de alcance, Wi-Fi
  desligado) são detectadas em cerca de 11 s e encerradas, sem travar o
  servidor do painel.
- Confirmação de calibração com volume ou número de bicos zerado passa a ser
  informada ao app como não salva.

## Notas de engenharia

- Build gerada com `CONFIG_APP_PROJECT_VER=1.0.12` usando ESP-IDF v6.0.
- Formato do log CAN mudou de registro binário de 14 bytes para linha de
  texto: incompatível com leitores do formato antigo.

## Atenção

- Canal beta: validar em bancada e em campo antes de promover para produção.
- Ainda não testado em painel físico com o app atualizado.
- Permanecem as pendências de segurança registradas nas versões anteriores.
