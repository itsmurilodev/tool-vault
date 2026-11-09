---
titulo: "pstack — coleção de skills de engenharia da Cursor (poteto)"
resumo: "58 skills da Lauren Tan (Cursor), analisadas uma a uma. 50 copiadas para o vault, sem alteração e manuais (só rodam com /nome); ficaram de fora o poteto-mode, as ligadas à Cursor e ao Grok, e o statechart pesado. Inclui a cola de quando usar cada uma."
tipo: referencia
dominio: radar
tags: [murilo/radar, radar/verificacao-e-qualidade, skills, agentes]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: adotar
categoria: verificacao-e-qualidade
natureza: skill
quando_usar: "Chamando /nome quando a situação aparecer (ver a cola na ficha): /bro, /ketchup, /sharpen, /how, /why, /tdd, /correct, /blast-radius, /interrogate, /architect, /arena e outras. 50 das 58 já estão no vault, todas manuais."
quando_nao_usar: "poteto-mode (age sem perguntar em ação externa e usa Grok), setup-pstack, poteto-help, make-bot-ui, ketchup-video; statechart e verificação formal só quando houver um fluxo crítico."
pre_requisito: "Nenhum para chamar. As skills de verificação precisam de app que sobe localmente com seed."
---

# pstack

> **Radar: ✅ adotar (50 skills manuais).** Ficam disponíveis via `/nome` e não fazem nada até você chamar. O `poteto-mode` e as peças ligadas à Cursor e ao Grok ficaram de fora.

## O que é

Skills e playbooks de engenharia da Lauren Tan (*poteto*), do time do React Compiler e engenheira na Cursor. A fonte oficial é `cursor/plugins/pstack` (MIT). O mirror que funciona fora da Cursor é `backnotprop/pstack`. Há dezenas de forks com o mesmo nome, alguns sem relação nenhuma.

## As 58 skills, separadas (análise de 2026-11-09)

Todas foram lidas no mirror, commit `0b239bb`. Sem dependência = funciona sozinha. Com dependência = precisa copiar junto as skills indicadas.

### 🧪 Vale copiar e testar (leves, sem dependência, alinhadas com o seu jeito)

| Skill | O que faz, em linguagem simples | Quando usar |
| --- | --- | --- |
| `bro` | Reescreve a última resposta **sem jargão**, como uma pessoa explicando para outra. São 2 linhas. | Toda vez que a resposta vier técnica demais |
| `tdd` | Bug com teste barato: escreve o teste que **falha antes**, corrige e mostra que passa. Se o teste for caro ou frágil, **não força**. | Etapa 2 do [[correcao-de-bug-com-agentes]] |
| `correct` | Acha os erros que os agentes **repetem** no repositório e torna cada um **impossível**: primeiro arquitetura, depois tipo, lint, teste, e só por último documentação. | Quando você corrigir o agente pela 2ª vez no mesmo erro |
| `sharpen` | Antes de delegar, deixa a tarefa **mais profunda, não maior**: o que um profissional faria, que fonte bruta usaria e o que provaria que ficou certo. Depois reescreve o prompt. | Antes de uma tarefa importante, junto do [[prompt-com-cenarios-de-verificacao]] |
| `how` | Explica **como uma parte do código funciona** (visão geral, conceitos, onde fica cada coisa, armadilhas) antes de mexer. Usa subagentes. | Ao entrar numa parte do Encaixe ou do AsyncHub que você não conhece |

### ⏳ Avaliar: úteis em situações específicas (ou dependem de outras)

| Skill | O que faz | Gatilho |
| --- | --- | --- |
| `ketchup` (+ `bro`) | Resume **o que mudou** numa sessão longa e lista **o que espera decisão sua** | Sessões longas, voltar de uma pausa |
| `benchmark-checklist` + `principle-explain-the-number` | 7 perguntas antes de confiar num número de performance (está medindo a coisa certa? repetiu 5 vezes? deu erro?) | Junto do modo auditoria da `performance-web` |
| `typescript-best-practices` (+ `principle-type-system-discipline`) | Regras de tipo TS: union discriminada, `unknown` no lugar de `any`, sem `as`, validação na borda | Bug de tipo recorrente em projeto TS |
| `statechart` | Modela um fluxo de estados (ex.: agendamento → fila de espera → encaixe) em TLA+, **acha o caminho que quebra uma regra** e desenha o diagrama | Fluxo de estados do Encaixe com bug difícil. Instala Java e TLC na 1ª vez. |
| `interrogate` (+ `arena`) | Vários "adversários" tentam **quebrar** a mudança; só vale achado provado rodando | PR de risco (auth, RLS, pagamento) |
| `blast-radius` (+ `arena`, `how`, `why`, `unslop`) | Descobre o que a mudança quebra **fora do diff**, provando com código rodando | Mudança pequena em que você não confia |
| `show-me-your-work` | Registro de decisões (por quê, evidência, resultado) em tarefas longas e sem supervisão | Tarefa longa em [[claude-code-na-nuvem]] |
| `reflect` | Tira aprendizados da sessão e propõe edições nas skills, **pedindo aprovação antes** | Ao fim de uma sessão em que você corrigiu muito o agente |
| `teach` (+ `how`, `why`, `unslop`) | Explica uma parte do sistema em ritmo de conversa, com diagramas | Quando quiser **entender** algo a fundo |
| `why` (+ `how`) | Explica **por que** algo é assim, buscando evidência (commits, issues, docs via MCP) | Regressão, decisão antiga sem registro |
| `architect` (+ `arena`, `how`) · `arena` · `swarm` · `figure-it-out` | Desenho antes de codar, várias tentativas em paralelo, roteiro de migração grande | Mudança estrutural grande. Custam muitos tokens. |
| `unslop` · `technical-writing` | Tirar "cara de IA" de texto; padrão de escrita técnica | Os padrões são de inglês e servem pouco para texto em PT-BR |
| `recall` · `automate-me` | Reconstruir contexto pelo histórico; transformar o seu estilo numa skill | Baixa prioridade: o seu `CLAUDE.md` e as suas regras globais já fazem isso |

### 📚 Os 25 "principles": usar como referência, não instalar

São regras curtas do tipo "aplique quando…". Instalar as 25 encheria a lista de skills, e várias repetem o que você já tem:
- `laziness-protocol` e `subtract-before-you-add` já estão no Ponytail;
- `prove-it-works` é o `verify-<app>`;
- `encode-lessons-in-structure` é a `correct`;
- `minimize-reader-load` está na `clean-code`.

As que **acrescentam** e valem virar referência dentro de uma skill sua:

| Principle | Ideia | Onde encaixaria |
| --- | --- | --- |
| `test-behavior-not-implementation` | Teste o que o usuário observa. Um teste bom falha quando o comportamento quebra e continua passando quando só o interno muda. | `tdd` / processo de bug |
| `make-operations-idempotent` | Rodar duas vezes, ou depois de um crash, dá o mesmo resultado | Webhook, pagamento (SyncPay), fila de espera do Encaixe |
| `boundary-discipline` | Valida na borda (API, formulário, webhook) e confia nos tipos dentro do sistema | Rotas de API e Supabase |
| `attack-the-premise` | Duas correções falharam? Teste a **premissa** comum antes da terceira | Processo de bug |
| `fix-root-causes` | Corrija onde o sistema errou primeiro. Uma *guard* só é correção se o estado for legítimo. | Processo de bug |

### ⛔ Evitar

| Skill | Por quê |
| --- | --- |
| `poteto-mode` · `poteto-help` · `setup-pstack` | Centrados na Cursor e em escolher modelos (o código vai para o Grok por padrão) |
| `make-bot-ui` | Só serve para o Grok Bot, que está como evitar |
| `ketchup-video` | Gera vídeo de slides: ferramenta extra sem ganho para você |
| `no-comments` | Depende de `how`, `why` e `architect`; o Ponytail já cobre ("comente só o porquê") |
| `in-your-own-words` | Já está nas suas regras globais ("entender o objetivo real") |
| `create/maintain-formal-verification-skill` | Verificação formal: pesada demais para o estágio atual |

### 🔎 As principais em detalhe: o que muda no Claude Code

**1. Skills "multi-modelo" perdem parte do valor no Claude Code.** `arena`, `architect`, `interrogate`, `why` e `swarm` foram desenhadas para que modelos **diferentes** (Opus e Grok, por padrão) se revisem. No Claude Code, os subagentes só rodam modelos Claude. **[PROVÁVEL]** Elas funcionam, mas com menos diversidade de opinião. Para uma revisão realmente cruzada, rode a mesma tarefa no Codex.

**2. O `poteto-mode` (o núcleo do pstack) conflita com as suas regras.** A seção *Autonomy* manda seguir sem perguntar em trabalho reversível e em **ações externas** ("team chat, ticket updates"). As suas diretrizes exigem confirmação antes de qualquer efeito externo. Ele também delega código ao Grok por padrão. **Evitar.** Vale só como leitura: os 23 *playbooks* (bug fix, feature, investigação…) servem de referência de processo.

**3. O `architect` implementa sem parar para você aprovar, por padrão.** O checkpoint humano é opcional (`/architect with checkpoint`). Para decisão difícil de reverter, a sua skill `decisao-arquitetural` (ADR) vem primeiro.

| Grupo | Skill | Peso | Detalhe que importa |
| --- | --- | --- | --- |
| **Copiar já** | `bro`, `sharpen`, `tdd`, `correct`, `how` (+2 references) | Leve | Sem dependência pesada. O `how` usa subagentes só para leitura. |
| | `ketchup` (+ `bro`) | Leve | Só leitura: não muda código nem publica nada. Bom para sessões longas. |
| **Copiar quando for usar** | `why` (+ references) | Médio | Busca o "porquê" nos MCPs conectados: **tem fonte pronta para Notion e Sentry**, que você usa ou vai usar |
| | `interrogate` (+ `arena`) | Médio | **Só reporta, não aplica.** Vale achado provado rodando código. Bom para PR de auth, RLS ou pagamento. |
| | `blast-radius` (+ `arena`, `how`, `why`, `unslop`) | Médio | Exige provar com código rodando, não com texto que "parece certo" |
| | `benchmark-checklist` | Leve | 7 perguntas antes de acreditar num número de performance. Par da `performance-web`. |
| | `reflect` (+ 4 references) | Médio | Propõe edições nas skills e **espera aprovação** antes de aplicar |
| | `typescript-best-practices` (+ `patterns.md`) | Leve | Projeto TS com bug de tipo recorrente |
| **Ocasionais e caras** | `arena` | Alto | N tentativas em paralelo; escolhe a melhor e enxerta o que as outras tinham de bom |
| | `architect` | Alto | Esboço de tipos e módulos antes de codar, via `arena` (ver ponto 3) |
| | `swarm` | Alto | Muitos trabalhadores em paralelo, um relatório só. Na Cursor roda na nuvem; no Claude Code, como subagentes. |
| | `figure-it-out` + `show-me-your-work` | Médio | Roteiro com checkpoints e registro de decisões para migração grande ou tarefa sem supervisão |
| | `teach` | Médio | Explicação didática (usa `how` + `why` + `unslop`, em inglês) |
| | `statechart` | Muito alto | Pasta com dezenas de arquivos de teste, TypeScript e TLA+; instala Java e TLC na 1ª execução. Só para um fluxo de estados crítico. |
| **Evitar** | `poteto-mode` | — | Ver ponto 2 |
| | `automate-me` · `recall` | — | O seu `CLAUDE.md`, as regras globais e a memória do Claude Code já cobrem |

### ✅ No vault (2026-11-09): 50 de 58

**Decisão revista:** 57 das 58 skills têm `disable-model-invocation: true`, ou seja, **só rodam quando você digita `/nome`**. Elas não disparam sozinhas e não pesam no contexto do dia a dia. Copiar quase tudo também resolve as dependências entre elas. Ficaram em `agentes/skills/`, sem alteração, do commit `0b239bb`, com `LICENSE` MIT em cada pasta.

**Ficaram de fora (8):**
- `poteto-mode` (age sem perguntar em ação externa e manda código ao Grok);
- `setup-pstack` (a única automática; só escolhe modelos);
- `poteto-help`;
- `make-bot-ui` (Grok Bot);
- `ketchup-video`;
- `statechart` (~3 MB, instala Java);
- `create-formal-verification-skill` e `maintain-formal-verification-skill`, que dependem do `statechart`.

Se um dia precisar de alguma, copie do mesmo commit.

### 🗒️ Cola: quando usar cada uma

Não precisa decorar: peça em português ("quero entender como funciona o agendamento") e o agente escolhe. Para chamar direto:

| Quando você… | Digite |
| --- | --- |
| achou a resposta técnica demais | `/bro` |
| quer saber o que aconteceu numa sessão longa e o que depende de você | `/ketchup` |
| vai pedir uma tarefa importante e quer pedir melhor | `/sharpen` |
| quer conferir se o agente entendeu o seu objetivo | `/in-your-own-words` |
| vai mexer numa parte do código que não conhece | `/how` |
| quer saber **por que** algo foi feito assim | `/why` |
| quer **aprender** uma parte do sistema com calma | `/teach` |
| tem um bug para corrigir | `/tdd` |
| corrigiu o mesmo erro do agente pela 2ª vez | `/correct` |
| fez uma mudança pequena, mas tem medo dela | `/blast-radius` |
| vai mexer em login, permissões ou pagamento | `/interrogate` |
| vai desenhar algo novo e grande | `/architect` (peça "with checkpoint") |
| tem dúvida entre jeitos de fazer e quer comparar | `/arena` |
| tem uma tarefa grande para dividir entre vários agentes | `/swarm` |
| vai fazer migração grande ou deixar rodando sozinho | `/figure-it-out` + `/show-me-your-work` |
| mediu performance e vai decidir com o número | `/benchmark-checklist` |
| tem bug de tipo TypeScript que volta sempre | `/typescript-best-practices` |
| quer escrever doc ou PR no padrão técnico | `/technical-writing` (em inglês) |
| quer tirar "cara de IA" de um texto | `/unslop` (em inglês) |
| terminou uma sessão em que corrigiu muito o agente | `/reflect` |
| quer o contexto do que você estava fazendo antes | `/recall` |
| quer transformar o seu jeito de trabalhar numa skill | `/automate-me` |
| quer criar um teste que prova que o app funciona | `/create-verification-skill` · `/maintain-verification-skill` |
| tem um comentário "não remova" que deveria virar regra | `/no-comments` (o Ponytail já cobre o básico) |

Os 25 `principle-*` não são para chamar no dia a dia: são regras de apoio que as outras skills consultam.

**No Claude Code:** as skills "multi-modelo" (`arena`, `architect`, `interrogate`, `why`, `swarm`) rodam só com modelos Claude. Funcionam, mas com menos diversidade de opinião.

## Como usar

1. Para atualizar: baixe de novo do mirror o commit desejado, substitua as pastas e atualize a origem no `LICENSE`. Não edite as cópias.
2. Rode `./scripts/atualizar.sh`.

Evite `npx skills add backnotprop/pstack`, que lista o pacote inteiro.

## Riscos

- Ecossistema confuso, com forks e ports chamados "pstack". Use só a fonte oficial ou o mirror.
- Várias skills chamam outras. Copiar sem as dependências quebra o fluxo.

## Ver também

- [[pstack-verificacao]] · [[skills-de-qualidade-de-codigo]] · [[categoria-verificacao-e-qualidade]]

## Fontes

- [cursor/plugins — pstack](https://github.com/cursor/plugins/tree/main/pstack) · [backnotprop/pstack](https://github.com/backnotprop/pstack)
