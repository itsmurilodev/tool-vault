---
name: fluxo-de-projeto
description: >
  Conduz o início de um projeto novo pelo fluxo de 6 documentos — PRD, Fluxo
  do app, TRD, UI/UX Design, Esquema backend e Plano de implementação — um de
  cada vez, com aprovação humana entre eles e validação explícita das decisões
  críticas de cada documento, usando os templates em references/. Usar SEMPRE
  que o usuário for começar um projeto, app, produto, SaaS ou módulo grande do
  zero, ou pedir "PRD", "TRD", "documentação inicial", "planejar o projeto",
  "fluxo do app", "esquema do banco", "plano de implementação" ou "kickoff".
  Usar também para retomar um projeto que já tem docs/01-prd.md …
  docs/06-plano-de-implementacao.md. Não usar para bug, ajuste pontual ou
  feature pequena em projeto existente — aí basta a skill
  levantamento-requisitos.
---

# Fluxo de construção de projetos — 6 documentos

Esta skill existe para que nenhum projeto comece pelo código. A IA escreve rápido e com a mesma confiança quando acerta e quando inventa; um erro no PRD vira erro em cinco documentos e depois no código. Por isso o fluxo é **sequencial, com portão humano entre cada documento**, e em cada portão a IA **puxa o humano para validar as poucas decisões que vão definir o futuro do projeto** — não para reler tudo.

**Idioma:** toda comunicação e todos os documentos em português do Brasil, direto e simples.

## Portão — qual o porte do projeto?

Decidir antes de gerar qualquer coisa. Processo pesado em projeto pequeno é o mesmo erro que nenhum processo.

| Porte | Exemplo | Documentos |
| :--- | :--- | :--- |
| **Trivial** | script, landing page estática, protótipo descartável | Nenhum. Seguir direto. |
| **Pequeno** | ferramenta interna, uma tela + um CRUD, sem dado sensível | PRD enxuto (Decisões críticas + seções 1, 2, 5, 7) + Plano |
| **Substancial** | produto com usuários reais, login, dado de cliente, integração externa, cobrança | Os 6, na ordem |

Na dúvida entre pequeno e substancial, fazer **uma** pergunta objetiva ao usuário. Não escolher o porte maior "por segurança". Qualquer que seja o porte, os documentos gerados seguem as mesmas regras abaixo.

**Registrar o porte** no frontmatter do PRD (`porte: pequeno` ou `porte: substancial`). É por ele que uma sessão futura sabe quais documentos existem no projeto.

## A ordem e por quê

**PRD → Fluxo do app → TRD → UI/UX → Esquema backend → Plano**

O Fluxo vem antes do TRD porque o fluxo não depende de tecnologia, mas a tecnologia depende do fluxo: tempo real, notificação, upload, offline e pagamento aparecem nos fluxos e só então viram escolha de stack. O Fluxo termina com a seção *Necessidades técnicas reveladas*, que é a entrada do TRD.

## Onde os documentos ficam

No **repositório do projeto**, não neste vault (vault guarda método; fato de projeto vive no projeto):

```text
<projeto>/docs/
├── 01-prd.md
├── 02-fluxo-do-app.md
├── 03-trd.md
├── 04-ui-ux-design.md
├── 05-esquema-backend.md
└── 06-plano-de-implementacao.md
```

Se o projeto tiver `CLAUDE.md` ou `AGENTS.md`, acrescentar uma linha apontando para `docs/` — assim toda sessão futura parte deles.

## Regras de execução

1. **Proibido gerar mais de um documento por vez.** Nem "rascunho rápido dos seis", nem "já adianto o próximo". Antes de começar um documento, abrir o **anterior previsto para o porte** (no porte pequeno, o anterior do Plano é o PRD) e conferir `status: aprovado` no frontmatter. Se não estiver aprovado, parar e dizer isso ao usuário — mesmo que ele peça para pular: nesse caso, explicar o risco em uma frase e pedir confirmação explícita, registrando a decisão no *Registro de mudanças* do documento pulado.
2. **Copiar o template inteiro** de `references/` — incluindo os blocos "Sobre este documento", "Revisão humana" e "Decisões críticas". Esses blocos são para o humano; **não apagar nem resumir**.
3. **Perguntar antes de inventar.** No PRD, antes de escrever, fazer **uma rodada curta de até 5 perguntas** com o essencial (problema, quem sente, como resolve hoje, métrica, prazo) — usando `levantamento-requisitos`. Nos demais documentos, partir dos anteriores aprovados e perguntar só o que eles não respondem. Depois disso, o que ainda faltar → escrever `❓ PERGUNTA:` no ponto exato e listar em *Perguntas em aberto*. Não preencher lacuna com suposição plausível. Número (meta, custo, prazo, limite) que o usuário não deu é marcado como **hipótese**.
4. **IDs rastreáveis.** `RF-NN` e `RNF-NN` nascem no PRD; `TELA-NN` e `FLX-NN` no Fluxo; `T-NN` no Plano. Todo item de um documento posterior cita o ID de onde veio. Item sem origem é escopo inventado — remover ou levar ao PRD.
5. **Portão de validação das decisões críticas** — ver seção abaixo. Sem ele respondido, o documento não é aprovado.
6. **Mudança depois de aprovado:** se a implementação exigir mudar uma decisão, atualizar **primeiro o documento de origem**, registrar em *Registro de mudanças*, e avisar os documentos que dependem dele. Se a mudança atinge uma linha de *Decisões críticas*, ela volta para validação do humano. Documento desatualizado é pior que nenhum: o próximo agente vai obedecê-lo.

## Portão de validação — induzir o humano a decidir o que importa

O humano não vai reler cada documento com o mesmo cuidado. O trabalho da IA é **apontar onde o cuidado precisa estar** e fazer a pergunta certa.

**Ao terminar cada documento:**

1. Preencher a seção **🎯 Decisões críticas para validar** com **de 1 a 5 pontos**. Um ponto entra se atende a pelo menos um critério:
   - **difícil ou caro de reverter** depois (modelo de dado, provedor de auth, corte do MVP, plataforma);
   - **se espalha** pelos documentos seguintes (um erro aqui vira erro em três lugares);
   - **se apoia em hipótese** que o usuário não confirmou.

   Ponto óbvio, cosmético ou já confirmado explicitamente pelo usuário **não entra** — encher a tabela dilui a atenção. Se honestamente não houver ponto crítico, escrever isso e por quê.
2. Mudar para `status: em-revisao` e entregar ao usuário, nesta ordem:
   - resumo de até 10 linhas do que foi decidido;
   - **cada decisão crítica como uma pergunta direta**, com a recomendação da IA e a consequência de errar. Formato: *"Assumi X porque Y. Se estiver errado, Z acontece lá na frente. Confirma ou ajusta?"*. Quando a resposta for de múltipla escolha, usar a ferramenta de pergunta estruturada do agente, se existir;
   - as perguntas em aberto que bloqueiam o próximo documento.
3. Registrar cada resposta na coluna **Sua resposta** da tabela. Se a resposta for "ajusto", aplicar o ajuste no documento antes de seguir.
4. **Só aprovar quando todas as linhas estiverem respondidas** e o usuário aprovar explicitamente. Aprovado → `status: aprovado`, `aprovado_por`, `aprovado_em`.

"Parece bom", "ok, segue" sem as decisões críticas respondidas **não é aprovação**: reapresentar só as linhas pendentes, de forma curta, e esperar.

## Skills que entram em cada etapa

| Documento | Usar junto | Para quê |
| :--- | :--- | :--- |
| 01 PRD | `levantamento-requisitos` | Separar pedido de problema real, MoSCoW, critério de aceite |
| 02 Fluxo | `heuristicas-nielsen` | Controle do usuário, prevenção e recuperação de erro |
| 03 TRD | `decisao-arquitetural`, `context7` | ADR para escolha difícil de reverter; versão atual de biblioteca |
| 04 UI/UX | `impeccable-ui`, `heuristicas-nielsen` | Evitar UI genérica; auditoria de usabilidade |
| 05 Backend | `semgrep-scan` | RLS, SQL, segredos |
| 06 Plano | `clean-code` | Critério de pronto das tarefas de código |
| Pós-implementação | `spec-compliance` | Auditar o código contra os RF/RNF do PRD |

Se uma skill da tabela não estiver instalada, seguir sem ela e avisar o usuário — não simular o método dela de memória.

## Retomar um projeto existente

1. Ler o `porte` no frontmatter do PRD e, em seguida, os documentos de `docs/` previstos para esse porte, checando o `status` de cada um.
2. Continuar do **primeiro documento não aprovado**. Se ele está `em-revisao`, reapresentar as decisões críticas ainda sem resposta.
3. Se todos estão aprovados, abrir o Plano e pegar a **primeira tarefa `T-NN` não marcada** cujas dependências estão concluídas. Uma tarefa por vez; ao concluir, marcar o checkbox e registrar desvios na seção de progresso.

## Projeto que já tem código, mas não tem docs

Não é "do zero" nem "retomar": é documentar o que existe e decidir o que falta.

1. Antes do PRD, **ler o repositório** (README, `package.json`, estrutura de pastas, esquema do banco/migrations) e listar o que já está implementado.
2. O que já existe entra nos documentos como **fato com evidência** (caminho do arquivo), não como decisão nova. Nota antiga do vault ou memória da IA não é evidência: se contradiz o código, vale o código, e a contradição vira pergunta.
3. Decisão já implementada que parece errada **entra nas Decisões críticas**. Estar no código não a torna certa, só mais cara de mudar — dizer quanto.

## Guardrails

- Não pular documento porque "o usuário parece saber o que quer" — pular é decisão do usuário, registrada.
- Não escolher stack fora da preferência padrão do usuário sem justificar no TRD.
- Não escrever tecnologia no PRD nem no Fluxo, nem regra de negócio nova no Plano.
- Não marcar `aprovado` sem o usuário ter dito que aprovou e sem as decisões críticas respondidas.
- Não copiar valores de design system para o documento 04 quando existe fonte: linkar.

## Referências

- `references/01-prd.md` … `references/06-plano-de-implementacao.md` — templates. Abrir só o do documento da vez.
