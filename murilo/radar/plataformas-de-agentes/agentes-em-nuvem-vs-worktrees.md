---
titulo: "Agentes de verificação em nuvem vs git worktrees locais"
resumo: "Worktree isola só os arquivos; VM em nuvem isola o ambiente inteiro, e é a verificação (app + banco por agente) que quebra worktrees em paralelo. Você já tem nuvem no Claude Code e no Codex: não adote o Cursor por isso; use worktree local para 1–2 tarefas e nuvem quando houver verify-<app> e seed anonimizado."
tipo: conceito
dominio: murilo
tags: [murilo/ia, agentes, verificacao, paralelismo, infra]
status: ativo
atualizado: 2026-11-09
---

# Agentes de verificação em nuvem vs git worktrees locais

## 📌 Resumo

A narrativa diz que *cloud agents* (cada agente numa VM própria, que sobe o app, testa e devolve PR com vídeo e screenshots) são melhores que rodar agentes em paralelo com **git worktree** na sua máquina. **Os dois não concorrem no mesmo nível:** worktree isola **arquivos**, enquanto VM isola o **ambiente inteiro** (processos, portas, banco, CPU). Dentro da VM o agente continua usando branch e worktree.

O argumento a favor da nuvem é real, e ele vem da **verificação**. Editar código em paralelo com worktree funciona bem. O que quebra é cada agente precisar do **próprio app e do próprio banco rodando** para provar a mudança ([[pstack-verificacao]]).

No [[adocao-de-ferramenta]]: você **já tem agente em nuvem** (sessões cloud do Claude Code e Codex cloud). Adotar o Cursor só por isso seria somar uma terceira plataforma. A nuvem passa a valer quando o `verify-<app>` sobe o app do zero com seed anonimizado.

> 💡 **Analogia:** worktree é dar uma mesa para cada marceneiro na **mesma oficina**: cada um tem sua madeira, mas todos dividem a serra, a tomada e o espaço. Nuvem é dar uma **oficina inteira** para cada um. Para desenhar a peça, a mesa basta. Para testar a peça montada, a serra compartilhada vira fila.

## 🧠 1. O que cada um isola

| | Git worktree local | Agente em VM na nuvem |
| --- | --- | --- |
| Arquivos e branch | ✅ Isolados | ✅ Isolados |
| Portas (`:3000`, `:54321`) | ❌ Compartilhadas: dois `dev` colidem | ✅ Cada VM tem as suas |
| Banco local / Supabase em Docker | ❌ Um por máquina, a não ser que você configure portas e projeto por worktree | ✅ Um por VM |
| CPU e RAM | ❌ Competem com você e entre si | ✅ Dedicados (Claude Code: 4 vCPU / 16 GB) |
| `.env`, `node_modules`, build | ⚠️ Não vêm junto: cada worktree precisa de install e env | Setup script com cache |
| Suas credenciais (`~/.ssh`, tokens, prod) | ❌ O agente roda com o seu usuário | ✅ Claude Code: credenciais git ficam fora da sandbox, e há proxy com allowlist de rede |
| Rodar com o notebook fechado | ❌ | ✅ |
| Ver e depurar ao vivo | ✅ Imediato | ⚠️ Remoto, mais lento |

**A ligação com verificação:** a `create-verification-skill` tem uma seção *Isolate* justamente porque dirigir duas vezes uma instância compartilhada corrompe a sessão. Com 1 a 2 agentes, o [[portless]] (domínio `*.localhost` por serviço ou worktree) mais um banco por projeto resolve localmente. Acima disso, ou se você quiser que o trabalho continue enquanto está fora, a VM é o caminho limpo.

## ⚠️ 2. Narrativa vs fato

| Afirmação | Avaliação |
| --- | --- |
| "Mais de 30% dos PRs que mergeamos na Cursor são de cloud agents" | **Afirmação da própria Cursor**, sobre uso interno, sem metodologia. O "35%" do título da devops.com não pôde ser conferido (a página bloqueou a leitura). A Cursor vende o produto, e a autora do pstack trabalha lá. |
| "O agente testa e manda vídeo e screenshots no PR" | **Existe, mas com ressalvas.** Postar artefatos no GitHub virou opt-in em mar/2026. O próprio moderador da Cursor diz que isso depende do agente fazer o certo e que há casos de **alucinação** (agente diz que gravou o vídeo e não gravou). Evidência gerada pelo agente continua precisando de conferência. |
| "Rode 10, 20 agentes em paralelo" | **Não cabe no seu estágio.** Com o merge humano definido em [[correcao-de-bug-com-agentes]], o gargalo vira a sua revisão. Mais PRs em paralelo só aumentam a fila. |
| "Local não escala" | **Verdade para verificação em paralelo**, mas para edição em paralelo não. |

## ⚠️ 3. Custos e riscos da nuvem

- **Setup:** o app precisa subir do zero na VM, com migrations, seed e variáveis. No Claude Code, o setup script deve fechar em cerca de 5 minutos para entrar no cache, que expira em cerca de 7 dias. Processos em background não entram no cache. **[INCERTO]** Ainda não está provado se o `supabase start` (várias imagens Docker) roda dentro da allowlist de rede *Trusted* e cabe nesse tempo. Teste antes de contar com isso.
- **Segredos:** no Claude Code, variáveis de ambiente são legíveis por qualquer um que use o ambiente. Chave de API vai como *network secret*, que fica fora da VM. **Nunca coloque credencial de produção no ambiente.**
- **Dados:** a VM é mais um terceiro guardando dado. Isso reforça a regra de [[correcao-de-bug-com-agentes]]: fixture anonimizada, nunca clone de produção.
- **Custo:** sessões cloud do Claude Code contam no limite de uso do plano (Pro, Max e acima). Os limites de VM do Codex variam por plano (Plus: 2 vCPU e 8 GiB).
- **Prompt injection:** nenhuma das documentações lidas trata do tema. Um agente autônomo, sem você olhando, lendo conteúdo externo, é o cenário de maior risco. Mantenha a rede em *Trusted* ou *Custom*, não *Full*.

## ✅ 4. Regra de bolso

| Situação | Onde rodar |
| --- | --- |
| 1 tarefa, ou 2 em que só uma precisa do app rodando | **Worktree local** (as sessões do app desktop já fazem isso), com Portless |
| 2 ou mais tarefas que precisam verificar ao vivo ao mesmo tempo | **Nuvem** (sessão cloud do Claude Code) |
| Tarefa longa para rodar enquanto você está fora | **Nuvem** |
| Depuração interativa, ou bug que só aparece na sua máquina | **Local** |
| Algo que precisa de credencial de produção | **Nenhum dos dois.** Reveja a tarefa. |

**Pré-requisito para a nuvem:** o `verify-<app>` (gerado pela `create-verification-skill`) sobe o app a partir de um banco vazio, com seed anonimizado e sem segredo de produção. O setup script da nuvem é basicamente o *Launch* dessa skill, e por isso a ordem certa é **primeiro a skill local, depois a nuvem**.

## 🔗 Ver também

- [[pstack-verificacao]] · [[correcao-de-bug-com-agentes]] · [[portless]] · [[adocao-de-ferramenta]]
- [[configuracao]]: hooks e `SessionStart` no repositório

## 📚 Fontes

- [Cursor — Cloud agents with computer use (blog, 2026-02-24)](https://cursor.com/blog/agent-computer-use) · [changelog](https://cursor.com/changelog/02-24-26)
- [Fórum Cursor — artefatos não aparecem no PR (fev–abr/2026)](https://forum.cursor.com/t/cursor-cloud-agents-do-not-post-their-screenshots-or-videos-to-pr/152974)
- [devops.com — "35% of internal PRs"](https://devops.com/cursor-cloud-agents-get-their-own-computers-and-35-of-internal-prs-to-prove-it) (não lido, HTTP 403)
- [Claude Code — Cloud environments](https://code.claude.com/docs/en/cloud-environments) · [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web)
- [Codex — Cloud environments](https://developers.openai.com/codex/environments/cloud-environments)
