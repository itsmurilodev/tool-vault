# Claude

Tudo que é específico do ecossistema Claude: skills, conectores, configuração e automação.

## Skills

Pasta [`skills/`](skills/) — formato de skill do Claude (pasta com `SKILL.md` + frontmatter `name`/`description`). Instalação por symlink:

```bash
./scripts/sync-skills.sh --apply
```

| Skill | Quando dispara |
| ----- | -------------- |
| [clean-code](skills/clean-code/SKILL.md) | Sempre que houver código sendo escrito, editado ou revisado |
| [decisao-arquitetural](skills/decisao-arquitetural/SKILL.md) | Escolha estrutural difícil de reverter (ADR) |
| [grill-me](skills/grill-me/SKILL.md) | Só sob pedido explícito — interrogatório até a ideia ficar consistente |
| [heuristicas-nielsen](skills/heuristicas-nielsen/SKILL.md) | Qualquer trabalho de interface / front-end |
| [impeccable-ui](skills/impeccable-ui/SKILL.md) | Geração, refinamento e auditoria de design/UI (59 regras anti-slop) |
| [levantamento-requisitos](skills/levantamento-requisitos/SKILL.md) | Funcionalidade nova ou pedido de cliente antes de implementar |
| [prompt-engineering-agente](skills/prompt-engineering-agente/SKILL.md) | Gerar, revisar ou melhorar prompt para outra IA |
| [semgrep-scan](skills/semgrep-scan/SKILL.md) | Segurança estática (SAST) em backend, RLS, SQL e secrets |
| [spec-compliance](skills/spec-compliance/SKILL.md) | Auditoria de conformidade entre SPEC.md e código implementado |


Formato e regras de escrita de skill: [CONVENCOES.md](../../../../CONVENCOES.md) seção 6.

## Notas

<!-- INICIO:INDICE (gerado por scripts/gerar-indices.py — não editar à mão) -->

- [Conectores do Claude (MCP)](conectores.md) — Conector é MCP remoto que roda na infra da Anthropic; custo de contexto e critério para conectar.
- [Configuração e automação do Claude](configuracao.md) — Qual instrução vai para CLAUDE.md, qual vira skill e qual precisa ser hook. *(rascunho)*

<!-- FIM:INDICE -->

---

## Backlog

- [ ] Subagentes: quando delegar vale mais que fazer inline
- [ ] Comparar skill vs `CLAUDE.md` vs regra de projeto — qual mecanismo para qual tipo de instrução
- [ ] Documentar os hooks que estiverem realmente em uso
