# AIC-P 1.0.17

Publicado em 2026-09-25 · canal: beta

Build gerada a partir do commit `7f07e56` do AIC-P. Inclui a 1.0.16, que não
foi publicada separadamente.

## Requisito

- **Exige o aplicativo AIC-CR 1.1.0 ou superior**, como a 1.0.15.

## Novidades

- Toda captura de log pelo Wi-Fi (`/log/stream`) começa com o motivo do
  último reinício e, se houver, o resumo do último travamento (task, PC,
  motivo e backtrace). Vêm como linhas `#LOG` comuns: aparecem no AIC-CR
  atual sem nenhuma mudança no app.
- O resumo do travamento, no log e no `GET /info` (`coredump.elf`), passa a
  informar o SHA do build que travou, necessário para decodificar o
  backtrace.
- (1.0.16) Envio ao driver AIC-DS da calibração do fluxômetro (DDI 0xF10B,
  pulsos/L): responde ao pedido do driver e reenvia quando a calibração muda
  (tela "Fluxômetro Pulsos/Litro" ou calibração pelo fluxo).

## Correções

- Pilha da task de leitura do GPS interno (`nmea_parser`) aumentada de 2048
  para 4096 bytes. O coredump de um painel em bancada registrou estouro de
  pilha nessa task, que reinicia o painel.

## Notas de engenharia

- Build gerada com `CONFIG_APP_PROJECT_VER=1.0.17` usando ESP-IDF v6.0.
- Continua valendo a observação da 1.0.15: o detalhe do travamento só existe
  em painéis gravados pela UART ao menos uma vez (partição `coredump`); o
  motivo do reinício aparece em todos.

## Atenção

- Canal beta: validar em bancada e em campo antes de promover para produção.
- A correção da pilha ainda não foi observada em uso prolongado com GPS
  interno.
- Permanecem as pendências de segurança registradas nas versões anteriores.
