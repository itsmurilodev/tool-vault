---
name: levantamento-requisitos
description: >
  Ajuda a clarear o pensamento antes de implementar qualquer coisa nova:
  entender o problema real por trás do pedido, separar requisito funcional de
  não-funcional, priorizar (MoSCoW / Value vs Effort) e estruturar tudo em um
  formato pronto para virar trabalho futuro de arquitetura e implementação.
  Usar SEMPRE que o usuário descrever uma funcionalidade nova, um problema a
  resolver, um pedido de cliente (inclusive projetos de clientes da Async
  Studio), ou disser algo como "quero adicionar X", "preciso
  resolver Y", "o cliente pediu Z" — mesmo sem a palavra "requisito" aparecer.
  Não usar para bugs triviais, ajuste visual pontual ou tarefa cujo escopo já
  está 100% claro e é pequeno — nesses casos aplicar o portão de porte abaixo
  primeiro, que pode dispensar a elicitação completa.
---

# Levantamento e estruturação de requisitos

O objetivo desta skill não é gerar documentação por documentação — é evitar que você (ou um cliente da Async Studio) comece a implementar em cima do pedido declarado quando o problema real é outro. A elicitação de requisitos existe justamente para isso: garantir que a necessidade real do interessado seja entendida, não só o desejo declarado ou superficial. Pedido e necessidade nem sempre são a mesma coisa, e a diferença entre os dois é onde a maior parte do retrabalho nasce.

Essa skill não tenta cobrir arquitetura, design de banco, UML ou implementação — isso é escopo de outra skill (em construção). Aqui o entregável é: problema entendido, requisito classificado e priorizado, e sinalização clara do que a etapa seguinte (arquitetura/implementação) vai precisar saber.

**Idioma:** toda comunicação (perguntas, documento de requisitos, resumo) é em português do Brasil, direta e simples, sem jargão desnecessário.

## Portão de porte — decidir antes de tudo

Antes de aplicar qualquer processo, classifique o pedido. Isso evita o erro do processo pesado aplicado a tudo:

- **Trivial** (correção de bug óbvio, ajuste de texto/cor, mudança sem ambiguidade sobre o que fazer): não aplicar elicitação. Seguir direto.
- **Pequena** (funcionalidade pontual, escopo claro, sem impacto em múltiplos tenants/dados/integrações externas): fazer só 2-3 perguntas objetivas das essenciais (problema real, quem usa, critério de aceite) e seguir para estruturação simplificada.
- **Substancial** (nova capacidade, mexe com dado de múltiplos tenants, integra sistema externo, afeta segurança, ou o próprio usuário está inseguro sobre o que realmente precisa): aplicar o processo completo abaixo.

Se estiver em dúvida entre pequena e substancial, pergunte objetivamente (uma pergunta, não uma bateria) antes de decidir — não assuma o porte maior por padrão só para "ser seguro", isso recria o problema do processo pesado demais.

## Processo completo (porte substancial)

### 1. Separar pedido declarado de problema real

Antes de aceitar o pedido como está, perguntar (usando `AskUserQuestion` quando a resposta for categórica, ou pergunta aberta quando exigir explicação):

- Qual é o problema que isso resolve, na prática, para quem vai usar?
- O que acontece hoje sem essa funcionalidade — qual é a dor concreta?
- Essa é a única forma de resolver isso, ou é a forma que já veio pronta na cabeça de quem pediu?

Se a resposta revelar que o pedido declarado é um meio e não o fim (ex.: "quero um botão de exportar CSV" quando o problema real é "preciso mandar isso pro contador"), registrar os dois — o problema real primeiro, o pedido declarado depois como uma das soluções possíveis, não a única.

### 2. Perguntas de contexto (aplicar as relevantes, não todas por padrão)

- Quem usa isso de fato (lojista, vendedor, cliente final, o próprio Murilo)?
- Existe limitação de prazo, orçamento ou stack já definida?
- Isso integra com algo externo (Meta Cloud API, Nuvemshop, sistema do cliente)?
- Tem implicação legal ou de dado sensível (dado de cliente final do lojista, LGPD)?
- Tem implicação de segurança (autenticação, isolamento entre tenants)?
- Já existe algo parecido implementado que serve de referência ou de restrição?

Pular qualquer pergunta cuja resposta já seja óbvia pelo contexto da conversa — perguntar por perguntar é o mesmo erro do checklist mecânico.

### 3. Classificar

- **Requisito Funcional:** o que o sistema deve fazer (ação, fluxo, dado exibido).
- **Requisito Não-Funcional:** como deve se comportar (performance, segurança, escala, disponibilidade, usabilidade). Estes são os que mais frequentemente viram decisão de arquitetura depois — sinalizar isso na seção 5.

### 4. Priorizar

- Escopo de fase/release: **MoSCoW** (Must/Should/Could/Won't) — serve para decidir o que entra na fase atual do CRM ou do projeto de cliente.
- Ranking dentro da fase já definida: **Value vs Effort** — julgamento informado de valor e esforço. Não usar RICE agora: RICE depende de dados de alcance/impacto que um produto pré-product-market-fit (seu caso, com dois beta testers) ainda não tem — usar RICE nesse estágio é preencher a fórmula com achismo disfarçado de dado.
- Quando o requisito vem de um cliente da Async Studio, o MoSCoW também serve para negociar escopo de contrato — "Won't" documentado evita expectativa mal alinhada depois.

### 5. Sinalizar para arquitetura

Se algum requisito não-funcional for pesado o suficiente (mexe em modelo de dado multi-tenant, integração externa nova, requisito de segurança não trivial, expectativa de escala), marcar explicitamente como **"provável ADR"** na saída — isso é o gancho para a futura skill de arquitetura, sem essa skill tentar decidir a arquitetura ela mesma.

## Formato de saída (porte substancial)

```
## Problema real
## Pedido declarado (se diferente do problema real)
## Requisitos Funcionais
## Requisitos Não-Funcionais
## Contexto (quem usa, limitações, integrações)
## Prioridade (MoSCoW + Value/Effort quando houver mais de um item)
## Critério de aceite
## Sinalização para arquitetura (se houver item "provável ADR")
## Riscos ou dúvidas em aberto
```

## Formato de saída (porte pequeno)

Não gerar o documento completo — só uma versão curta, direto no fluxo da conversa:

```
Problema real: ...
Critério de aceite: ...
Prioridade: Must/Should/Could
```

## Modo estruturação — quando o usuário já sabe o que quer

Se o usuário já chega com o requisito claro e só pede para organizar/documentar, não repetir a elicitação inteira — ir direto para a classificação e o formato de saída. Mas ainda checar rapidamente se falta algo crítico (sem critério de aceite, sem prioridade, sem separação funcional/não-funcional) e sinalizar a lacuna em vez de preencher com suposição.

## Restrições

- Não inventar requisito legal, de segurança ou de integração que não foi mencionado nem é evidente pelo contexto — marcar como "não avaliado" em vez de assumir que não existe ou forçar uma resposta.
- Não avançar para decisão de arquitetura, banco de dados ou UML — isso é fora do escopo desta skill.
- Não aplicar o processo completo em pedido trivial ou pequeno só para "ser rigoroso" — isso é o erro que motivou reformular essa skill.
- Quando o pedido vier de um cliente da Async Studio, deixar claro no "Won't" do MoSCoW o que fica fora do escopo combinado, já que isso vira referência de contrato/expectativa.
