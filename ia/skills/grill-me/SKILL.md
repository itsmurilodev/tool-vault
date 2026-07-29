---
name: grill-me
description: >
  Questiona uma ideia até ela ficar consistente: pergunta, espera a resposta,
  pergunta de novo, e só resume o que entendeu e pede confirmação antes de
  aplicar qualquer coisa. Usar SOMENTE quando o usuário pedir explicitamente
  — "grill me", "me grelha", "questione isso até ficar consistente", "me faça
  perguntas antes de aplicar", ou pedido equivalente. Não acionar
  automaticamente diante de qualquer ambiguidade — isso é escalada
  deliberada além do comportamento padrão de 1-2 perguntas de esclarecimento;
  o usuário está pedindo um interrogatório completo, não uma clarificação
  rápida.
---

# Grill-me — questionar até a ideia ficar consistente

Quando o usuário pede "grill me", ele está pedindo mais do que o padrão de confirmar objetivo com 1-2 perguntas — está pedindo para eu deliberadamente não seguir em frente até esgotar as inconsistências reais da ideia. É um modo, não um reflexo: só ativa sob pedido explícito.

**Idioma:** toda comunicação (perguntas, checkpoints, resumo final) é em português do Brasil, direta e simples, sem jargão desnecessário.

## Processo

### 1. Perguntar uma pergunta (ou um pequeno grupo relacionado) por vez

Nunca despejar uma lista longa de perguntas de uma vez — isso vira formulário, não interrogatório real. Cada pergunta deve ser formulada considerando a resposta anterior, não uma lista pré-pronta.

### 2. Intercalar os seis tipos de pergunta socrática

Usar essas categorias para não ficar preso só em "o que você quer dizer com isso":

- **Clarificação:** o que você quer dizer exatamente com X? Pode dar um exemplo concreto?
- **Pressuposição:** o que você está assumindo aqui que talvez não seja verdade?
- **Evidência/razão:** o que te faz achar que isso vai funcionar? Já viu isso funcionar em algum caso parecido?
- **Perspectiva alternativa:** você considerou fazer diferente? Como alguém que discorda enxergaria isso?
- **Implicação/consequência:** se isso der certo, o que acontece depois? E se der errado?
- **Pergunta sobre a pergunta:** essa é realmente a pergunta certa a se fazer aqui, ou tem uma pergunta anterior sem resposta?

Não é preciso passar pelas seis em ordem fixa — usar a que a resposta anterior abriu.

### 3. Escolher o formato certo pra cada pergunta

Usar `AskUserQuestion` quando a pergunta tiver um conjunto pequeno e discreto de respostas plausíveis (ex.: escolher entre 2-3 caminhos claros). Usar pergunta aberta em texto quando a resposta exigir explicação — não forçar tudo em botão só por conveniência.

### 4. Critério de parada — quando considerar a ideia consistente

Parar de perguntar quando, simultaneamente:
- Não há mais contradição entre as partes da ideia que o usuário já explicou.
- As suposições relevantes foram declaradas explicitamente, não deduzidas por mim.
- Eu consigo reformular a ideia inteira sem preencher nenhuma lacuna com suposição própria.

Não continuar perguntando só para parecer rigoroso: se uma pergunta a mais não mudaria o que vai ser feito, ela não vale a pena. Inventar problema que não existe pra ter mais uma pergunta é o oposto do objetivo desta skill.

Se o processo estiver ficando longo, fazer um checkpoint explícito em vez de simplesmente continuar: "Já temos X e Y resolvidos; ainda vejo uma questão em aberto sobre Z — quer continuar refinando ou seguir com o que temos?"

### 5. Resumir antes de aplicar — portão obrigatório

Quando a ideia estiver consistente (ou o usuário pedir para encerrar o interrogatório), produzir um resumo reconstruindo a ideia com as respostas já incorporadas — não um resumo genérico do pedido original.

```
## O que entendi
## Suposições que ficaram explícitas nas respostas
## O que eu ainda não sei / meu palpite, se você não corrigir
## Confirma para eu seguir com isso?
```

**Nunca aplicar, implementar ou executar antes dessa confirmação ser dada explicitamente.** Resposta ambígua, silêncio, ou mudança de assunto não contam como confirmação — nesse caso, perguntar de novo em vez de assumir que pode seguir.

## Restrições

- Não despejar todas as perguntas de uma vez.
- Não inventar problema que não existe só para ter mais uma pergunta a fazer.
- Não avançar para execução sem a confirmação explícita do resumo final, mesmo que a conversa pareça claramente encerrada.
- Se a ideia sendo grelhada for um requisito de software ou uma decisão estrutural/arquitetural, o resultado final ainda deve ser estruturado pelas skills `levantamento-requisitos` ou `decisao-arquitetural` quando aplicável — grill-me é o motor de perguntas, não substitui o formato de saída dessas skills.
