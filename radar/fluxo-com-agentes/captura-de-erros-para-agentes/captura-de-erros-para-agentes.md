---
titulo: "Captura de erros para agentes — do alerta em produção ao PR"
resumo: "Episódio 2 da série do reel: PostHog captura o erro, um bot dispara um agente em nuvem e o agente decide sozinho o risco do merge. A captura via issue é ótima; o gatilho por evento e o agente julgando o próprio risco não passam no portão. Aqui fica o pipeline adaptado: alerta só em issue nova, issue no GitHub como chamado, label humano como gatilho e gate de risco determinístico."
tipo: conceito
dominio: radar
tags: [murilo/engenharia, agentes, observabilidade, processo, github]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: avaliar
categoria: fluxo-com-agentes
natureza: pratica
quando_usar: "Usuários reais em produção gerando erros que você só descobriria por relato, ou triagem manual tomando tempo toda semana."
quando_nao_usar: "MVP sem tráfego; um agente por ocorrência de erro; payload cru do erro dentro da issue."
pre_requisito: "verify-<app>, processo de bug fix, um único tracker decidido (ADR-001) e scrub de dados pessoais no SDK."
---

# Captura de erros para agentes — do alerta em produção ao PR

## 📌 Resumo

Continuação de [[correcao-de-bug-com-agentes]]. O reel descreve um "engenheiro de plantão de IA 24/7": o **PostHog** captura um erro em produção, envia para um bot, e o bot abre um agente em nuvem da Cursor. Esse agente reproduz o erro, corrige, verifica com as skills de verificação, **classifica sozinho o risco** e faz o merge sem humano se a correção for "pequena". Antes disso, outros dois modelos revisam.

As peças novas em relação às notas anteriores são duas: **o gatilho automático** (erro vira agente) e **o gate de risco**. A ideia de usar o erro capturado como ponto de partida é boa. Duas implementações do reel não passam no [[adocao-de-ferramenta]]: disparar um agente por erro e deixar o agente avaliar o próprio risco.

> 💡 **Analogia:** central de chamados de condomínio. O sensor de vazamento abre o chamado sozinho (ótimo), mas quem decide se manda o encanador é o síndico olhando o chamado, e quem decide se a obra precisa de aprovação é o regimento, não o encanador.

## 🧠 1. O chamado é a issue

O que você perguntou ("como capturar os chamados e o processo de cada um") tem uma resposta direta: **cada bug vira uma issue no GitHub**, e o processo do bug fica registrado nos artefatos ligados a ela:

| Artefato | Responde |
| --- | --- |
| Issue no tracker (PostHog/Sentry) | Quantas vezes, quantos usuários, em qual release |
| **Issue no GitHub** (template `01_bug_report`) | O quê: erro, link para o tracker, critério de resolução |
| PR com `Fixes #N` | Como: fixture que reproduz, teste que falha, correção |
| Evidência no PR (`verify-<app>`) | Prova: repro falhando antes e passando depois |
| Tracker marcado como resolvido no release | Fechamento. Uma regressão reabre a issue. |

Isso já é o [[fluxo-issue-pr]] que você usa. A automação só preenche a primeira linha sozinha.

## ⚠️ 2. Onde o reel quebra

### 2.1 Um agente por erro

O error tracker dispara a **cada ocorrência**. Um pico (deploy ruim, bot raspando o site, extensão de navegador quebrando o JS) vira dezenas de agentes em nuvem resolvendo o mesmo bug, com custo multiplicado. O certo é disparar **só em issue nova ou reaberta**, que é exatamente o que o alerta de error tracking do PostHog oferece (issue criada ou reaberta, mais alerta de pico separado). Junte a isso deduplicação pelo fingerprint e um teto de execuções por dia.

Também nem toda exceção é bug: há requisição cancelada pelo usuário, rede caindo, extensão de navegador. Filtre esses casos no tracker antes do alerta.

### 2.2 O agente julgando o próprio risco

"Se for uma correção pequena, mescla sem mim" é decidido **pelo próprio autor da correção**. É conflito de interesse: o mesmo modelo que errou o diagnóstico vai errar a avaliação de risco. O risco tem que ser medido **por um script no CI**, nunca pela opinião do agente:

- tamanho do diff (ex.: ≤ 30 linhas e ≤ 3 arquivos);
- **caminhos proibidos** para auto-merge: `supabase/migrations/`, políticas de RLS, auth, pagamento, `.github/workflows/`, `package.json` (dependências);
- teste novo presente no PR e CI verde;
- falhou em qualquer um desses itens, o PR vai para revisão humana.

### 2.3 Payload de erro é entrada não confiável e carrega dado pessoal

A mensagem de exceção frequentemente contém o que o usuário digitou, e o contexto do erro carrega ID, e-mail e corpo de requisição. Esse texto vai direto para um agente com permissão de escrita no repositório. O próprio `claude-code-action` avisa na documentação oficial: processar conteúdo não confiável expõe o workflow a prompt injection, e o *scrub* de segredos "reduz mas não elimina" o risco.

**Regra:** scrub de dados pessoais no SDK (`before_send`), e a issue leva **resumo sanitizado mais link** para o tracker, nunca o payload cru.

### 2.4 Narrativa

- **"Mais barato que contratar um engenheiro":** pode ser verdade para uma startup com receita e tráfego. No seu estágio, pré-receita e com pouco erro, não existe um plantão para substituir. O custo fixo (setup, manutenção, crédito de agente em nuvem) vem antes do benefício.
- **"Humanos também erram":** é uma falsa equivalência. Erro humano passa por revisão e tem responsável. O desenho do reel remove a revisão justamente onde o autor decide que não precisa.
- **Nomes de modelo ("GPT-4.7", "GPT-6.1", "outro 5.5"):** **[PROVÁVEL]** a transcrição embaralhou os nomes. *Grok 4.7* para código e *Opus 5.5* para revisão são os padrões do pstack. O ponto que importa é a diversidade de modelos, não a marca.

## 🧠 3. PostHog ou Sentry? Isso reabre o ADR-001

- O [[adr-001-observabilidade]] (status **proposta**) escolheu o **Sentry** e criou a regra "**uma plataforma por projeto**".
- O [[analytics-de-produto]] já adota o **PostHog**, que **também faz error tracking**. O free tier é de 100 mil exceções/mês (página oficial de preços), contra ~5 mil eventos/mês citados para o Sentry no ADR.
- O reel usa o PostHog justamente para juntar analytics e erro num vendor só.

**Não decidi isso aqui.** É uma escolha estrutural e cara de reverter depois que a instrumentação se espalha. Antes de montar o pipeline, revise o ADR com a skill `decisao-arquitetural`. O pipeline abaixo funciona com qualquer um dos dois.

**[INCERTO]** Um guia de terceiro diz que destino de webhook (*data pipelines*) não está no plano gratuito do PostHog. Não achei confirmação oficial. Confira na aba *Data pipelines* do projeto antes de contar com isso.

## ✅ 4. Pipeline adaptado

```text
erro em produção
  └─► tracker (PostHog OU Sentry, um só) ── scrub de PII no SDK, release e source maps
        └─► alerta SÓ em issue nova/reaberta (filtrando ruído)
              └─► função pequena cria a GitHub Issue (template de bug, resumo sanitizado + link)
                    └─► [VOCÊ] triagem: aplica a label `claude`  ◄── gatilho humano
                          └─► claude-code-action (label_trigger) ou sessão cloud
                                segue correcao-de-bug-com-agentes:
                                reproduzir → corrigir → verify-<app> → PR "Fixes #N"
                                └─► CI: testes + semgrep + gate de risco (script) + 2º modelo
                                      └─► [VOCÊ] merge ─► tracker resolve no release
```

- **Gatilho:** o `claude-code-action` tem `label_trigger` (padrão `claude`), conferido no `action.yml` oficial. E `allowed_bots` vem vazio por padrão, então uma issue aberta por bot não dispara o agente sozinha. **Quem aplica a label é você.** Esse é o seu gate de triagem, e custa um clique.
- **Criação da issue:** o webhook do tracker vai para uma função pequena (Supabase Edge Function, que já faz parte do seu stack) que valida, sanitiza e chama a API do GitHub. **[PROVÁVEL]** O Sentry também tem integração nativa com o GitHub para criar issues. Confira antes de escrever a função.
- **Ordem de implementação:** (1) `verify-<app>` funcionando, (2) tracker com scrub, (3) alerta + issue automática, (4) label + action. Sem o passo 1, o agente não tem como provar nada, e o resto só gera PR sem prova.

### Escada de autonomia (continua a de [[correcao-de-bug-com-agentes]])

| Degrau | Triagem (label) | Merge |
| --- | --- | --- |
| **0 — hoje** | Você | Você |
| **1** | Automática para issue nova no release das últimas 24h com ≥ N usuários afetados | Você |
| **2** | Automática | Auto-merge **só** se o gate determinístico do CI passar. Nunca em migração, auth, RLS, pagamento ou dado pessoal. |

## 🔗 Ver também

- [[correcao-de-bug-com-agentes]] · [[pstack-verificacao]] · [[agentes-em-nuvem-vs-worktrees]]
- [[bots-donos-de-feature]]: o roteamento do erro para o dono da feature, sem bot.
- [[adr-001-observabilidade]] · [[observabilidade]] · [[analytics-de-produto]]
- [[fluxo-issue-pr]] · [[github-issue-creator]]
- Skills [decisao-arquitetural](../../../agentes/skills/decisao-arquitetural/SKILL.md) · [semgrep-scan](../../../agentes/skills/semgrep-scan/SKILL.md)

## 📚 Fontes

- Transcrição do reel (episódio 2 da série) colada pelo usuário em 2026-11-09 (autor não identificado).
- [PostHog — Send error tracking alerts](https://posthog.com/docs/error-tracking/alerts) · [Error tracking pricing](https://posthog.com/docs/error-tracking/pricing)
- [StackOne — PostHog webhook setup](https://docs.stackone.com/connectors/posthog/guides/webhook-setup) (afirmação sobre o plano gratuito, não confirmada)
- [anthropics/claude-code-action — action.yml](https://github.com/anthropics/claude-code-action/blob/main/action.yml) (inputs `label_trigger`, `allowed_bots` e aviso de prompt injection) · [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions)
