# AIC-P 1.0.9

Publicado em 2026-09-22 · canal: beta

## Novidades

- Nova rota WebSocket `GET /ws/remote`, no mesmo servidor HTTP local já usado
  pelo provisionamento Wi-Fi e pela telemetria (`/ws/telemetry`): recebe os
  toques de tecla enviados pela tela "Controle Remoto" do app AIC-CR, que
  replica a membrana física por rede local.
- Cada evento de tecla do app é injetado no mesmo array que a leitura do
  teclado físico usa, com o mesmo efeito de toque curto/longo — o teclado
  físico continua funcionando exatamente como antes, sem qualquer mudança de
  comportamento.

## Notas de engenharia

- Build gerada com `CONFIG_APP_PROJECT_VER=1.0.9` usando ESP-IDF v6.0.
- Binário validado pelo verificador de versão embutida do AIC-DIST.

## Atenção

- Canal beta: validar em bancada e em campo antes de promover para produção.
- Rota nova sem autenticação adicional, mesmo nível de confiança das demais
  rotas HTTP locais já existentes (pendência de segurança conhecida do
  projeto).
- Permanecem as pendências de segurança registradas nas versões anteriores.
