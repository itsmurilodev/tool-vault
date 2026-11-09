---
titulo: "Cursor Cloud Agents — agentes em VM própria que testam e gravam demo"
resumo: "Agentes da Cursor que rodam numa VM isolada, usam o app no navegador e devolvem PR com vídeo e screenshot. Funciona, mas seria a terceira plataforma; o Claude Code na nuvem cobre o mesmo para você."
tipo: referencia
dominio: murilo
tags: [murilo/radar, radar/plataformas-de-agentes, agentes, nuvem]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: evitar
categoria: plataformas-de-agentes
natureza: plataforma
quando_usar: "Só se a Cursor virar seu ambiente principal de desenvolvimento."
quando_nao_usar: "Hoje: seria a terceira plataforma ao lado de Claude Code e Codex; os artefatos de vídeo e screenshot têm relatos de alucinação."
pre_requisito: "Plano pago da Cursor."
---

# Cursor Cloud Agents

> **Radar: ⛔ evitar (por enquanto).** A ideia é boa (verificar numa VM própria); a ferramenta é redundante no seu stack.

## O que é

Lançado em 2026-02-24. Cada agente recebe uma **VM isolada** com ambiente completo, usa navegador e *computer use* para testar o próprio trabalho, e devolve PR com **vídeo, screenshots e logs**. A Cursor afirma que mais de 30% dos PRs que ela mergeia internamente vêm desses agentes. Esse número é da própria empresa e não tem medição independente.

## Quando usar

- Se você adotar a Cursor como IDE e plataforma principal.

## Quando não usar

- Hoje: o Claude Code (local e [[claude-code-na-nuvem]]) e o Codex já cobrem execução em paralelo e na nuvem.
- Quando você for confiar no artefato sem conferir. No fórum da Cursor, o próprio moderador admite que o modelo às vezes **alucina** o artefato (diz que gravou um vídeo que não gravou). Postar os artefatos no GitHub é opt-in desde mar/2026.

## Como a ideia se aplica sem a Cursor

O valor está na **verificação em ambiente isolado**. Para você, isso é o `verify-<app>` ([[pstack-verificacao]]) rodando numa sessão do [[claude-code-na-nuvem]]. A comparação completa está em [[agentes-em-nuvem-vs-worktrees]].

## Ver também

- [[agentes-em-nuvem-vs-worktrees]] · [[grok-bot]] · [[categoria-plataformas-de-agentes]]

## Fontes

- [Cursor — agent computer use](https://cursor.com/blog/agent-computer-use) · [Fórum — artefatos no PR](https://forum.cursor.com/t/cursor-cloud-agents-do-not-post-their-screenshots-or-videos-to-pr/152974)
