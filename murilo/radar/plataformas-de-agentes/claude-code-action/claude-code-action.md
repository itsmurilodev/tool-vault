---
titulo: "claude-code-action — agente disparado por issue/label no GitHub Actions"
resumo: "GitHub Action oficial da Anthropic que roda o Claude Code numa issue ou PR via @claude, label ou assignee. É o gatilho do pipeline de captura de erros, com a label aplicada por você como portão."
tipo: referencia
dominio: murilo
tags: [murilo/radar, radar/plataformas-de-agentes, github, agentes]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: avaliar
categoria: plataformas-de-agentes
natureza: ferramenta
quando_usar: "Disparar um agente a partir de uma issue quando você aplicar a label (ex.: claude), no pipeline de captura de erros."
quando_nao_usar: "Gatilho automático por bot; allowed_bots='*' ou allowed_non_write_users em repositório com segredo; antes de existir verify-<app> para o agente provar a correção."
pre_requisito: "Processo de bug fix e verify-<app> no projeto; ANTHROPIC_API_KEY ou OAuth token como secret do repositório."
---

# claude-code-action

> **Radar: ⏳ avaliar.** É a peça que liga "issue de bug" a "agente trabalhando". Só vale depois que o agente tiver como provar o que fez.

## O que é

`anthropics/claude-code-action@v1`. Roda o Claude Code num workflow do GitHub Actions. Os gatilhos, conferidos no `action.yml`, são:

- `trigger_phrase` (padrão `@claude`, num comentário ou no corpo da issue);
- `label_trigger` (padrão `claude`);
- `assignee_trigger`.

Numa issue, ele cria uma branch nova. Num PR, faz push na branch existente.

## Quando usar

- No degrau 0 da escada de autonomia ([[captura-de-erros-para-agentes]]): **você** aplica a label `claude` depois de triar a issue, e o agente segue o [[correcao-de-bug-com-agentes]].

## Quando não usar

- Com gatilho automático por bot: `allowed_bots` vem vazio por padrão, e esse padrão é bom. É o que impede uma issue aberta por bot de disparar o agente sozinha.
- Com `allowed_non_write_users`: a própria documentação avisa que conteúdo não confiável expõe o workflow a **prompt injection**, e que o *scrub* de segredos "reduz mas não elimina" o risco.
- Antes do `verify-<app>`: o agente abriria PR sem prova.

## Como usar

1. Workflow com `on: issues: types: [labeled]` e `label_trigger: claude`.
2. O prompt do workflow manda seguir o processo: reproduzir com fixture, teste falhando primeiro, `verify-<app>`, PR com `Fixes #N` e evidência.
3. Permissões mínimas no workflow. O merge continua sendo seu (branch protection).

## Ver também

- [[captura-de-erros-para-agentes]] · [[correcao-de-bug-com-agentes]] · [[categoria-plataformas-de-agentes]]

## Fontes

- [anthropics/claude-code-action — action.yml](https://github.com/anthropics/claude-code-action/blob/main/action.yml) · [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions)
