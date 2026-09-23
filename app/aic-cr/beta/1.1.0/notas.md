# AIC-CR 1.1.0

Publicado em 2026-09-23 · canal: beta

## Novidades
- Controle Remoto: espelho ao vivo do display do painel, dentro de uma
  moldura, no lugar da logo. Teclas reorganizadas: P e M à esquerda, X e V
  nos cantos direitos, setas em cruz compacta e 1-4 sob o display.
- Controle Remoto: dois toques no display salvam a tela do painel como BMP
  de 1 bit (preto e branco), com um flash rápido de confirmação. O arquivo
  fica junto com os logs do painel, com compartilhar e excluir.
- Descobrir dispositivos: busca equipamentos AIC ao mesmo tempo na rede
  Wi-Fi atual (mDNS) e nas redes "AIC-" próximas. A lista mostra o nome e a
  conexão ("Rede local" ou "Direto").
- Descobrir dispositivos: equipamentos já cadastrados no mesmo modo não
  aparecem. Em outro modo aparecem, e ao conectar o cadastro existente só
  tem o modo de conexão atualizado.
- Com o app em segundo plano, o painel para de enviar os dados do
  dashboard. A telemetria continua conectada (comandos, calibração remota)
  e a captura de log continua.

## Atenção
- O espelho do display e a pausa do dashboard em segundo plano exigem o
  firmware do painel com esse suporte, ainda não publicado (posterior ao
  AIC-P 1.0.11). Com firmware anterior, o display fica em
  "Aguardando painel…" e o resto do app funciona normalmente.
- Assinado com a chave de publicação Inootec (pacote
  br.com.inootec.taxafixa). Um celular com uma build de desenvolvimento
  instalada precisa desinstalá-la antes de instalar esta.
