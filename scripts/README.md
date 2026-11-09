# 🔧 Scripts

Você só precisa lembrar de **um comando**, que roda depois de criar, mover ou editar notas e skills:

```bash
./scripts/atualizar.sh
```

Ele chama os três scripts abaixo, nesta ordem:

| Script | O que faz, em linguagem simples | Se não existisse… |
| --- | --- | --- |
| `gerar-indices.py` | Reescreve a lista de notas de cada `README.md` e monta a tabela do **catálogo do radar** lendo o topo (frontmatter) de cada nota. | Você teria que atualizar índices e catálogo à mão, e eles ficariam desatualizados. |
| `validar-vault.py` | Confere links quebrados, nomes de arquivo repetidos, frontmatter incompleto, ficha do radar com campo errado e skill mal formada. | Agentes e você poderiam bagunçar o vault sem perceber. |
| `sync-skills.sh` | Cria atalhos (symlinks) de `agentes/skills/*` em `~/.claude/skills/`. É isso que faz o Claude **enxergar** as suas skills. Editar a skill no vault já vale na hora. | Skill nova criada no vault não apareceria para o Claude. |

**No GitHub:** o workflow `.github/workflows/validar-vault.yml` roda a validação e a checagem de índices a cada push.

**Dependência opcional:** com `PyYAML` instalado (`pip install pyyaml`), a validação de frontmatter fica completa. Sem ele, funciona numa versão simplificada.
