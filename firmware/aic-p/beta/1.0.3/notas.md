# AIC-P 1.0.3

Publicado em 2026-09-13 · canal: beta

## Novidades
- Nova tela "Config. Menu": permite marcar, item a item, quais opções do
  menu de configurações são "avançadas" (só aparecem no modo de menu
  avançado). Navegação com cima/baixo e marca/desmarca com a tecla "v",
  usando um checkbox (quadro com moldura) alinhado à direita de cada linha.
- Modo de menu avançado: ligar o painel com a tecla "m" pressionada durante
  o boot faz o menu principal exibir todos os itens (inclusive os
  avançados) e libera o acesso à tela "Config. Menu". No boot normal, os
  itens marcados como avançados ficam ocultos do menu principal.
- Os marcadores de item avançado são persistidos na NVS.

## Atenção
- Mesmas pendências de segurança das versões anteriores (SoftAP aberto,
  token de update fixo).
- Ainda não há nenhum item pré-marcado como avançado por padrão - o
  instalador precisa entrar no modo avançado e marcar as opções desejadas.
