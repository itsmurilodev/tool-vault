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
| [levantamento-requisitos](skills/levantamento-requisitos/SKILL.md) | Funcionalidade nova ou pedido de cliente antes de implementar |
| [prompt-engineering-agente](skills/prompt-engineering-agente/SKILL.md) | Gerar, revisar ou melhorar prompt para outra IA |

Formato e regras de escrita de skill: [CONVENCOES.md](../../../CONVENCOES.md) seção 6.

## Notas

- [Conectores (MCP)](conectores.md) — o que são, onde rodam, e o critério para conectar ou não.
- [Configuração e automação](configuracao.md) — `CLAUDE.md`, `settings.json`, hooks, permissões e onde cada coisa mora.

---

## Backlog

- [ ] Subagentes: quando delegar vale mais que fazer inline
- [ ] Comparar skill vs `CLAUDE.md` vs regra de projeto — qual mecanismo para qual tipo de instrução
- [ ] Documentar os hooks que estiverem realmente em uso
