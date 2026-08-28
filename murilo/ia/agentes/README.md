# Agentes & Skills

Configuração, ecossistema e skills operacionais para agentes de IA (Claude, Antigravity, Cursor, Copilot, ChatGPT/Codex, etc.).

---

## Skills

Pasta [`skills/`](skills/) — skills operacionais padronizadas (pasta com `SKILL.md` + frontmatter `name`/`description`). Instalação por symlink:

```bash
./scripts/sync-skills.sh --apply
```

| Skill | Quando dispara |
| ----- | -------------- |
| [clean-code](skills/clean-code/SKILL.md) | Sempre que houver código sendo escrito, editado ou revisado |
| [context7](skills/context7/SKILL.md) | Consulta de documentações oficiais versionadas e snippets atualizados via Context7 |
| [decisao-arquitetural](skills/decisao-arquitetural/SKILL.md) | Escolha estrutural difícil de reverter (ADR) |
| [grill-me](skills/grill-me/SKILL.md) | Só sob pedido explícito — interrogatório até a ideia ficar consistente |
| [heuristicas-nielsen](skills/heuristicas-nielsen/SKILL.md) | Qualquer trabalho de interface / front-end |
| [impeccable-ui](skills/impeccable-ui/SKILL.md) | Geração, refinamento e auditoria de design/UI (59 regras anti-slop) |
| [levantamento-requisitos](skills/levantamento-requisitos/SKILL.md) | Funcionalidade nova ou pedido de cliente antes de implementar |
| [portless-dev](skills/portless-dev/SKILL.md) | Execução e gerenciamento de servidores de desenvolvimento locais via Portless |
| [prompt-engineering-agente](skills/prompt-engineering-agente/SKILL.md) | Gerar, revisar ou melhorar prompt para outra IA |
| [react-doctor](skills/react-doctor/SKILL.md) | Auditoria estática e diagnóstico de performance/anti-patterns em React |
| [semgrep-scan](skills/semgrep-scan/SKILL.md) | Segurança estática (SAST) em backend, RLS, SQL e secrets |
| [spec-compliance](skills/spec-compliance/SKILL.md) | Auditoria de conformidade entre SPEC.md e código implementado |

Formato e regras de escrita de skill: [CONVENCOES.md](../../../CONVENCOES.md) seção 6.

---

## Notas

<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->

<!-- FIM:INDICE -->

---

## Critério de Organização

| Tipo de Conteúdo | Onde fica |
| ---------------- | --------- |
| **Skills operacionais** | [`ia/agentes/skills/`](skills/) |
| **Conectores (MCP) e Configuração** | [`ia/agentes/`](./) |
| **Teoria de prompt e LLM** | [`ia/conceitos/`](../conceitos/) |
| **Personas** | [`ia/personas/`](../personas/) |
| **Regras globais e de workspace** | [`ia/regras/`](../regras/) |
