# AIC-P 1.0.6

Publicado em 2026-09-17 · canal: beta

## Novidades
- Novo comando de telemetria `set_target_rate`
  (`{"t":"set_target_rate","v":1,"value_x10":<0-9999>}`) - permite ao app
  AIC-CR editar a taxa de aplicação alvo (L/ha × 10), mesmo efeito da tela
  física "Taxa de Aplicação", incluindo a persistência na NVS.
- Novos comandos `get_speeds`/`set_speeds` para editar pelo app as duas
  velocidades cadastradas (Velocidade de Trabalho e Velocidade Mínima):
  - `get_speeds` (sem parâmetros) responde na hora, direto na conexão
    WebSocket, com `{"t":"speeds","v":1,"work_x10":...,"min_x10":...}` - não
    depende do ciclo periódico de telemetria.
  - `set_speeds` (`{"t":"set_speeds","v":1,"work_x10":<0-999>,"min_x10":
    <0-999>}`) grava as duas de uma vez, mesmo efeito das telas físicas
    "Velocidade de Trabalho"/"Velocidade Mínima" (inclusive reenviando ao
    driver o novo mínimo de vazão), sem entrar no fluxo de configuração de
    alarme de velocidade (exclusivo da tela física).

## Notas de engenharia
- A ação de "salvar" de cada campo de cadastro numérico (grava em RAM +
  persiste na NVS) foi extraída em funções dedicadas, chamadas tanto pela
  tela física quanto pelo comando de telemetria equivalente - garante que os
  dois caminhos nunca divirjam em comportamento ou dupliquem lógica.

## Atenção
- Mesmas pendências de segurança das versões anteriores (SoftAP aberto,
  token de update fixo, tokens de log fixos de desenvolvimento).
- `set_speeds`/`set_target_rate` não têm validação de negócio além da faixa
  estrutural do campo (mesmo comportamento que as telas físicas já têm hoje).
