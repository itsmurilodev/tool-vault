---
name: fluxo-de-projeto
description: >
  Conduz o início de um projeto novo pelo fluxo de 6 documentos — PRD, TRD,
  Fluxo do app, UI/UX Design, Esquema backend e Plano de implementação — um de
  cada vez, com aprovação humana entre eles, usando os templates em references/.
  Usar SEMPRE que o usuário for começar um projeto, app, produto, SaaS ou
  módulo grande do zero, ou pedir "PRD", "TRD", "documentação inicial",
  "planejar o projeto", "fluxo do app", "esquema do banco", "plano de
  implementação" ou "kickoff". Usar também para retomar um projeto que já tem
  docs/01-prd.md … docs/06-plano-de-implementacao.md. Não usar para bug,
  ajuste pontual ou feature pequena em projeto existente — aí basta a skill
  levantamento-requisitos.
---

# Fluxo de construção de projetos — 6 documentos

Esta skill existe para que nenhum projeto comece pelo código. A IA escreve rápido e com a mesma confiança quando acerta e quando inventa; um erro no PRD vira erro em cinco documentos e depois no código. Por isso o fluxo é **sequencial, com portão humano entre cada documento**, e cada template traz no topo o que o humano precisa conferir.

**Idioma:** toda comunicação e todos os documentos em português do Brasil, direto e simples.

## Portão — qual o porte do projeto?

Decidir antes de gerar qualquer coisa. Processo pesado em projeto pequeno é o mesmo erro que nenhum processo.

| Porte | Exemplo | Documentos |
| :--- | :--- | :--- |
| **Trivial** | script, landing page estática, protótipo descartável | Nenhum. Seguir direto. |
| **Pequeno** | ferramenta interna, uma tela + um CRUD, sem dado sensível | PRD enxuto (seções 1, 2, 5, 7) + Plano |
| **Substancial** | produto com usuários reais, login, dado de cliente, integração externa, cobrança | Os 6, na ordem |

Na dúvida entre pequeno e substancial, fazer **uma** pergunta objetiva ao usuário. Não escolher o porte maior "por segurança".

## Onde os documentos ficam

No **repositório do projeto**, não neste vault (vault guarda método; fato de projeto vive no projeto):

```text
<projeto>/docs/
├── 01-prd.md
├── 02-trd.md
├── 03-fluxo-do-app.md
├── 04-ui-ux-design.md
├── 05-esquema-backend.md
└── 06-plano-de-implementacao.md
```

Se o projeto tiver `CLAUDE.md` ou `AGENTS.md`, acrescentar uma linha apontando para `docs/` — assim toda sessão futura parte deles.

## Regras de execução

1. **Um documento por vez, na ordem.** Antes de começar o documento N, abrir o N-1 e conferir `status: aprovado` no frontmatter. Se não estiver aprovado, parar e dizer isso ao usuário. Nunca gerar os seis de uma vez.
2. **Copiar o template inteiro** de `references/` — incluindo os blocos "Sobre este documento" e "Revisão humana". Esses blocos são para o humano; **não apagar nem resumir**.
3. **Perguntar antes de inventar.** Faltou informação → escrever `❓ PERGUNTA:` no ponto exato e listar em *Perguntas em aberto*. Não preencher lacuna com suposição plausível. Número (meta, custo, prazo, limite) que o usuário não deu é marcado como **hipótese**.
4. **IDs rastreáveis.** `RF-NN` e `RNF-NN` nascem no PRD; `TELA-NN` e `FLX-NN` no Fluxo; `T-NN` no Plano. Todo item de um documento posterior cita o ID de onde veio. Item sem origem é escopo inventado — remover ou levar ao PRD.
5. **Ao terminar cada documento:** mudar para `status: em-revisao` e entregar ao usuário, nesta ordem:
   - resumo de até 10 linhas do que foi decidido;
   - os **3 pontos do checklist de revisão que mais precisam do olhar humano** neste projeto específico;
   - as perguntas em aberto.

   Só seguir para o próximo com **aprovação explícita**. Aprovado → `status: aprovado`, `aprovado_por`, `aprovado_em`.
6. **Mudança depois de aprovado:** se a implementação exigir mudar uma decisão, atualizar **primeiro o documento de origem**, registrar em *Registro de mudanças*, e avisar os documentos que dependem dele. Documento desatualizado é pior que nenhum: o próximo agente vai obedecê-lo.

## Skills que entram em cada etapa

| Documento | Usar junto | Para quê |
| :--- | :--- | :--- |
| 01 PRD | `levantamento-requisitos` | Separar pedido de problema real, MoSCoW, critério de aceite |
| 02 TRD | `decisao-arquitetural`, `context7` | ADR para escolha difícil de reverter; versão atual de biblioteca |
| 03 Fluxo | `heuristicas-nielsen` | Controle do usuário, prevenção e recuperação de erro |
| 04 UI/UX | `impeccable-ui`, `heuristicas-nielsen` | Evitar UI genérica; auditoria de usabilidade |
| 05 Backend | `semgrep-scan` | RLS, SQL, segredos |
| 06 Plano | `clean-code` | Critério de pronto das tarefas de código |
| Pós-implementação | `spec-compliance` | Auditar o código contra os RF/RNF do PRD |

Se uma skill da tabela não estiver instalada, seguir sem ela e avisar o usuário — não simular o método dela de memória.

## Retomar um projeto existente

1. Ler `docs/` na ordem e checar o `status` de cada documento.
2. Continuar do **primeiro documento não aprovado**.
3. Se todos estão aprovados, abrir o Plano e pegar a **primeira tarefa `T-NN` não marcada** cujas dependências estão concluídas. Uma tarefa por vez; ao concluir, marcar o checkbox e registrar desvios na seção de progresso.

## Guardrails

- Não pular documento porque "o usuário parece saber o que quer" — pular é decisão do usuário, registrada no PRD.
- Não escolher stack fora da preferência padrão do usuário sem justificar no TRD.
- Não escrever tecnologia no PRD, nem regra de negócio nova no Plano.
- Não marcar `aprovado` sem o usuário ter dito que aprovou.
- Não copiar valores de design system para o documento 04 quando existe fonte: linkar.

## Referências

- `references/01-prd.md` … `references/06-plano-de-implementacao.md` — templates. Abrir só o do documento da vez.
