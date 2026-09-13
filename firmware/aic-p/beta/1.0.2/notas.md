# AIC-P 1.0.2

Publicado em 2026-09-13 · canal: beta

## Novidades
- Tela "Conexão WiFi" no menu de configurações, em duas telas sequenciais:
  "Ativar WiFi do Painel?" e "Ativar WiFi do Driver?".
- O rádio do painel só sobe (SoftAP nunca é anunciado) se o usuário ativar
  essa opção - liga/desliga em tempo real, sem precisar reiniciar.
- O painel passa a requisitar do AIC-DS (via CAN, DDIs novas 0xF108/0xF109)
  os últimos 4 dígitos do MAC dele e a versão de firmware real, exibidos
  no rodapé da tela ("SSID Driver: AIC-DS-XXXX").
- Nova mensagem CAN (DDI 0xF107) informa ao driver se ele deve ligar o
  próprio WiFi - depende do firmware do AIC-DS suportar essa DDI.
- Exibe a versão do firmware no canto superior direito da tela de boot.
- Corrige `GET /info`: `firmwareVersion` estava fixo em
  `"0.1.0-wifi-dev"`, agora reflete a versão real embutida no binário.

## Atenção
- Mesmas pendências de segurança das versões anteriores (SoftAP aberto,
  token de update fixo).
- Requer um AIC-DS com suporte às DDIs 0xF107/0xF108/0xF109 para as
  informações do driver aparecerem na tela - sem isso, ficam zeradas
  (tratado como firmware legado, não é um erro).
