# AIC-P 1.0.24

Publicado em 2026-10-27 · canal: stable

Build gerada a partir do commit `1ebf806` do AIC-P.

## Requisito

- **Exige o aplicativo AIC-CR 1.1.0 ou superior** (desde a 1.0.15).

## Novidades

- Menu disponível enquanto o painel aguarda o driver: na tela de boot
  "AGUARDANDO DRIVER", a tecla M abre o menu de configurações (título "MENU -
  SEM DRIVER"). Dá para ligar o WiFi e adiantar cadastros sem driver
  conectado. A dashboard continua bloqueada: sair do menu volta para a tela
  de boot, e o painel só entra em operação quando um driver responder.
- Sem driver, a "Calib. Manual Fluxômetro" não aparece no menu.
- Nova opção "APP Android", logo após "Conexão WiFi": mostra um QR code com o
  link do aplicativo na Play Store. Por padrão é um item avançado (aparece
  ligando o painel com a tecla M pressionada, ou marcando-o em "Config.
  Menu").

## Correções

- Quando o driver só aparece depois do boot, o painel agora reenvia a ele a
  preferência de WiFi do driver e pede MAC e versão de novo.

## Atenção

- Primeira versão estável desde a 1.0.0: inclui todas as mudanças publicadas
  no canal beta da 1.0.7 à 1.0.23 (ver as notas de cada uma).
- O QR code ocupa 33x33 pixels do visor (cerca de 18 mm); a leitura pelo
  celular ainda precisa ser conferida no painel real.

## Notas de engenharia

- Build gerada com `CONFIG_APP_PROJECT_VER=1.0.24` usando ESP-IDF v6.0.
- Nova chave NVS `menuAdvConhec` (bitmap de 256 bits por idTela) com os itens
  do menu já conhecidos; item novo recebe o padrão de avançado sem mudar a
  marcação dos antigos.
