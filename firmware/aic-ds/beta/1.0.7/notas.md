# AIC-DS 1.0.7

Publicado em 2026-09-22 · canal: beta

Build gerada a partir do commit `a3f31c8` do AIC-DS-FW.
`CONFIG_APP_PROJECT_VER` fixado em `1.0.7`.

## Novidades
- Conexão do driver à rede Wi-Fi local, pelo aplicativo AIC-CR (mesmo fluxo
  do painel): busca de redes, cadastro de SSID/senha e volta para o modo
  Ponto de Acesso. A rede fica salva no driver e é reconectada
  automaticamente a cada boot; enquanto não conecta, o Ponto de Acesso
  `AIC-DS-XXXX` continua disponível para recuperação.
- O driver passa a ser encontrado na rede local via mDNS
  (`_aic-device._tcp`).
- Para descartar a rede salva e voltar ao modo Ponto de Acesso: com o
  equipamento ligado, desative e reative o WiFi do driver pelo painel, sem
  desligar o equipamento no meio. Desativar o WiFi, desligar o equipamento e
  reativar depois **não** apaga a rede salva.
- Log em tempo real (WiFi) passa a mostrar as mensagens CAN recebidas (`@R`)
  e transmitidas (`@T`) pelo driver, em texto legível.

## Correções
- O celular não é mais desconectado do Ponto de Acesso do driver no instante
  em que envia a rede a ser cadastrada (a resposta ao aplicativo se perdia).
- Ligar/desligar o WiFi do driver pelo painel não ocupa mais a tarefa de
  recepção CAN enquanto o rádio sobe ou desce.

## Atenção
- Versão beta para validação. Requer o aplicativo AIC-CR com a correção de
  reconexão após falha no cadastro da rede; versões anteriores do app podem
  gravar o driver como "rede local" sem confirmação e exigir recadastro.
- O primeiro comando de WiFi recebido do painel após ligar o driver é
  aplicado mas não conta para o gesto de descarte da rede; se necessário,
  repita desativar/reativar.
- Durante o cadastro, se a rede escolhida estiver em outro canal, o Ponto de
  Acesso do driver acompanha esse canal e o celular pode desconectar por
  alguns segundos.
- Placas ESP32 sem antena (ou com antena externa desconectada) têm sinal
  muito fraco e podem falhar na conexão com a rede local.
- Inclui instrumentação de diagnóstico do barramento CAN no log em tempo
  real (investigação do heartbeat do driver durante a calibração remota).
- Token de streaming/OTA ainda é fixo de desenvolvimento
  (`aic-log-dev-token`/`aic-ds-ota-dev-token`) — pendência de segurança
  conhecida, mantida das versões beta anteriores.
