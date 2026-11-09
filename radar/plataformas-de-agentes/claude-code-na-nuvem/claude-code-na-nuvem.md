---
titulo: "Claude Code na nuvem — sessões em VM da Anthropic"
resumo: "Sessões do Claude Code em VM Ubuntu (4 vCPU, 16 GB, Docker, Postgres, Chrome) que você já tem no plano. É a opção de nuvem quando várias tarefas precisam subir o app ao mesmo tempo ou rodar com você fora."
tipo: referencia
dominio: radar
tags: [murilo/radar, radar/plataformas-de-agentes, agentes, nuvem, claude-code]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: avaliar
categoria: plataformas-de-agentes
natureza: plataforma
quando_usar: "Duas ou mais tarefas que precisam subir o app ao mesmo tempo para verificar, ou tarefa longa para rodar enquanto você está fora."
quando_nao_usar: "Uma ou duas tarefas (worktree local basta); tarefa que precisa de credencial de produção; bug que só reproduz na sua máquina; depuração interativa."
pre_requisito: "verify-<app> subindo do zero com seed anonimizado; setup script; chaves como network secret, nunca em variável de ambiente."
---

# Claude Code na nuvem

> **Radar: ⏳ avaliar.** Você já tem acesso, sem ferramenta nova. Vale quando a verificação em paralelo passar a travar a sua máquina.

## O que é

Cada sessão roda numa VM nova: Ubuntu 24.04, 4 vCPU, 16 GB de RAM e 30 GB de disco, com **Docker, PostgreSQL 16, Redis e Chrome** já instalados. O repositório vem clonado. Um *setup script* roda antes, com cache de cerca de 7 dias, se terminar em uns 5 minutos. A rede pode ser *None*, *Trusted* (padrão), *Full* ou *Custom*, e as credenciais git ficam **fora** da sandbox. O uso conta no limite do plano (Pro, Max e acima).

## Quando usar

- 2 ou mais tarefas que precisam do app rodando ao mesmo tempo. Localmente, portas e banco colidem.
- Tarefa longa enquanto você está fora.

## Quando não usar

- 1 ou 2 tarefas: worktree local, que as sessões do app desktop já usam, junto com o [[portless]].
- Qualquer coisa que exija credencial de produção.
- Depuração interativa, ou bug que só aparece na sua máquina.

## Como usar

1. **Antes:** o `verify-<app>` funcionando localmente a partir de um banco vazio, com seed anonimizado ([[pstack-verificacao]]).
2. Setup script = o *Launch* do `verify-<app>` (instalar dependências, migrations e seed).
3. Chave de API vai como **network secret**, porque variável de ambiente é legível por quem usa o ambiente. Rede em *Trusted* ou *Custom*.
4. **[INCERTO]** Teste se o `supabase start` (várias imagens Docker) cabe na allowlist e no tempo do cache antes de contar com ele.

## Ver também

- [[agentes-em-nuvem-vs-worktrees]] · [[cursor-cloud-agents]] · [[categoria-plataformas-de-agentes]]

## Fontes

- [Claude Code — Cloud environments](https://code.claude.com/docs/en/cloud-environments) · [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web)
