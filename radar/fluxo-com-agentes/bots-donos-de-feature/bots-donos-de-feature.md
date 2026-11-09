---
titulo: "Bots donos de feature — Grok Bot e o modelo de 'colega de trabalho' por recurso"
resumo: "Episódio 3 da série do reel: um bot persistente por feature (Grok Bot), com memória atualizada a cada merge, chat em grupo entre bots e um bot de erro que roteia para o dono. A ideia de dono por feature é boa; a memória fora do repositório e o computador compartilhado não. Para o seu porte, a versão sem ferramenta nova é um documento por feature no repositório, que é o feature map do verify-<app>."
tipo: conceito
dominio: radar
tags: [murilo/ia, agentes, contexto, processo, ferramentas]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: testar
categoria: fluxo-com-agentes
natureza: pratica
quando_usar: "Na versão documento por feature dentro do repositório (feature map do verify-<app>), atualizado no mesmo PR da mudança."
quando_nao_usar: "Memória de bot fora do repositório; chat em grupo de bots; um bot por feature com um único dev."
pre_requisito: "verify-<app> criado (o feature map é a base)."
---

# Bots donos de feature — Grok Bot e o modelo de "colega de trabalho" por recurso

## 📌 Resumo

No reel, o autor cria **um bot por feature** do app dele (AI Content Studio, Script Writer, Content Calendar…) usando o **Grok Bot**, produto da xAI distribuído junto com a Cursor (beta desde 2026-08-11). Cada bot é o "dono" da sua feature e funciona assim:

1. recebe a tarefa e dispara um agente em nuvem da Cursor para implementar;
2. depois do merge, lê o que mudou e **atualiza a própria base de conhecimento**;
3. verifica usando o app num navegador, não só com teste unitário;
4. conversa em **chat em grupo** com outros bots quando a mudança cruza features;
5. o **Error Fix Bot** faz a triagem dos erros, encaminha para o dono da feature afetada ou corrige sozinho quando o erro não tem dono.

**A ideia central é boa:** contexto persistente por área do sistema evita que cada agente redescubra a feature do zero. **A implementação não passa no** [[adocao-de-ferramenta]] para você: a memória fica fora do repositório (sem versão e sem revisão), todos os bots dividem o mesmo computador e as mesmas sessões logadas, e seria uma quarta plataforma de agentes. A versão que cabe no seu porte não precisa de ferramenta nova: **um documento por feature, dentro do repositório**.

> 💡 **Analogia:** em vez de contratar um porteiro para cada andar, que guarda de cabeça quem mora ali, você deixa um quadro atualizado na entrada de cada andar. Qualquer porteiro novo lê o quadro e sabe o mesmo, e quando alguém se muda, o quadro muda junto.

## 🧠 1. O que o reel diz vs o que a documentação diz

| No reel | Documentação oficial ([cursor.com/docs/grok-bot](https://cursor.com/docs/grok-bot)) |
| --- | --- |
| "Cada bot tem acesso ao **seu próprio computador**" | **Contradiz.** "All of your Bots use the same cloud computer, sharing its files, browser sessions, and app logins." Cada bot tem a própria *tela*, com uma tarefa de computer use por vez. Quem tem VM própria é o **agente em nuvem da Cursor** que o bot dispara ([[agentes-em-nuvem-vs-worktrees]]). |
| Bot "atualiza sua base de conhecimento" depois do merge | A memória existe ("preferences, role context, and summaries of prior work"), mas a atualização pós-merge **não aparece na documentação lida**. Provavelmente é uma rotina que o autor montou por conta própria. |
| Chat em grupo onde os bots "apontam os erros uns dos outros" | O chat em grupo existe ("pass work, assign ownership"). **[PROVÁVEL]** Um guia de terceiros diz que o limite é de 2 a 6 bots e recomenda **um dono por etapa** para evitar trabalho duplicado. A página oficial com esse detalhe deu 404. |
| "Parece que tenho minha própria equipe" | É linguagem de marketing da série. A própria xAI vende o produto como *"your team of always-on agents"*. |

## ⚠️ 2. Onde o modelo quebra

1. **Memória fora do repositório.** O que o bot "sabe" sobre a feature fica na memória dele: não passa por PR, não tem diff e você não revisa. Se ele resumir errado um merge, o erro vira verdade para todas as tarefas seguintes, e só aquele bot enxerga. Também fica preso ao fornecedor: Claude Code e Codex não leem essa memória.
2. **Computador e logins compartilhados.** A documentação manda tratar tudo que está no computador como disponível para **todos** os bots. Junte isso ao Error Fix Bot, que lê payload de erro (texto digitado por usuários, ver [[captura-de-erros-para-agentes]]): um prompt injection num erro alcança todas as sessões logadas da conta.
3. **Chat em grupo multiplica custo e concordância.** Cada mensagem é paga por vários modelos, e modelos tendem a concordar entre si. Para uma mudança que cruza features, um agente lendo os dois documentos das features faz o mesmo trabalho com menos ruído.
4. **Plataforma extra.** O Grok Bot exige plano pago da Cursor ou SuperGrok e está em beta. Você já tem Claude Code (local e nuvem) e Codex: entrar o Grok Bot é somar, não substituir.
5. **Escala do autor ≠ a sua.** O autor tem uma startup com várias features e receita. O Encaixe e o AsyncHub têm poucas features e um único desenvolvedor, que é você. Um "dono" por feature cuidaria de um punhado de arquivos.

## ✅ 3. A versão que cabe: dono por feature dentro do repositório

O conhecimento por feature vira **arquivo versionado**, e o "dono" vira **qualquer agente que lê esse arquivo**. Você já tem a peça certa: o **feature map do `verify-<app>`** ([[pstack-verificacao]]), que tem um arquivo por feature com sub-features, como o usuário chega, como dirigir e armadilhas.

| Peça do reel | Equivalente sem ferramenta nova |
| --- | --- |
| Bot dono da feature | `verify-<app>/features/<feature>.md`, com uma seção extra de **onde mora no código** (pastas e arquivos principais) |
| Atualizar a memória após o merge | **Regra no `CLAUDE.md`/`AGENTS.md` do projeto:** o PR que muda uma feature atualiza o arquivo dela no mesmo PR. Assim ele é revisado junto com o código. |
| Memória que não apodrece | `/maintain-verification-skill` confere cada arquivo contra o código e o app rodando |
| Error Fix Bot roteando para o dono | Os caminhos do stack trace apontam qual arquivo de feature carregar. É uma tabela de caminho para feature, sem bot nenhum. |
| Chat em grupo para mudança que cruza features | Um agente com os arquivos das features envolvidas no contexto, mais o segundo modelo na revisão ([[correcao-de-bug-com-agentes]]) |

**Vantagem:** funciona igual no Claude Code, no Codex e em qualquer agente futuro, aparece no diff, você revisa e está no Git.

**Quando reavaliar o Grok Bot:** quando houver mais gente no time ou features demais para um agente carregar o contexto. E só se o computador compartilhado puder ficar sem logins sensíveis.

## 🔗 Ver também

- [[pstack-verificacao]]: o feature map é a base de conhecimento por feature.
- [[captura-de-erros-para-agentes]] · [[correcao-de-bug-com-agentes]] · [[agentes-em-nuvem-vs-worktrees]]
- [[configuracao]]: onde vai a regra de atualizar a documentação no PR (CLAUDE.md vs hook).
- [[adocao-de-ferramenta]]

## 📚 Fontes

- Transcrição do reel (episódio 3 da série) colada pelo usuário em 2026-11-09 (autor não identificado).
- [Cursor Docs — Grok Bot](https://cursor.com/docs/grok-bot): computador compartilhado, memória, planos. As subpáginas de grupos, times e planos deram 404 em 2026-11-09.
- [xAI — Introducing Grok Bot](https://x.ai/news/introducing-grok-bot) (2026-08-11, beta)
- [Learn Cursor — Grok Bot group chats](https://www.learncursor.dev/learn/cursor-agents/grok-bot-group-chats-voice) (terceiro, não oficial)
