# Convenções do vault

Regras para manter o vault consistente conforme ele cresce. Se uma regra aqui atrapalhar mais do que ajudar, mude a regra — não crie exceção silenciosa.

---

## 1. Onde colocar a nota

Decida por **domínio** (o assunto), não por como você aprendeu.

| Domínio        | O que entra                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| `ia/`          | LLMs, prompt engineering, personas, regras — e config específica de cada agente |
| `engenharia/`  | Código, arquitetura, padrões, testes, refatoração, qualidade                 |
| `infra/`       | Cloud, containers, redes, Linux, CI/CD, observabilidade, banco de dados      |
| `ferramentas/` | Git/GitHub, editor, terminal, CLIs, produtividade                            |

> Um estudo de Clean Code feito conversando com uma IA é conhecimento de **engenharia**, não de IA. O domínio é o assunto da nota, não a ferramenta usada para produzi-la.

**Dentro de `ia/`, há um segundo corte:** o que funciona em qualquer agente fica em `conceitos/`, `personas/` e `regras/`; o que só funciona num agente específico fica em `agentes/<nome>/`. Teste: se a nota começa com "no Claude você faz assim", ela é de `agentes/`. Se começa com "prompt bom tem objetivo explícito", é de `conceitos/`.

**Quando criar um domínio novo:** só quando existirem 3+ notas que não cabem em nenhum dos atuais. Antes disso, coloque no domínio mais próximo.

**Quando criar subpasta:** só quando o tópico tiver 3+ arquivos. Um tópico com uma nota só é um arquivo solto no domínio (`engenharia/clean-code.md`), não uma pasta com um arquivo dentro.

---

## 2. Conhecimento vs artefato

Duas naturezas diferentes, tratadas de formas diferentes:

- **Conhecimento** (`conceitos/`, notas de domínio) — o que eu aprendi. Pode ser longo, ter analogia, exemplo, contexto histórico. Escrito para o meu eu do futuro.
- **Artefato** (`ia/agentes/claude/skills/`, `ia/personas/`, `ia/regras/`) — o que uma IA consome e executa. Deve ser enxuto, operacional e sem teoria decorativa. Escrito para uma máquina seguir.

Quando os dois existem para o mesmo assunto, o artefato **referencia** o conhecimento em vez de copiá-lo. Conteúdo duplicado nas duas pontas sempre diverge.

---

## 3. Nomes de arquivo

- `kebab-case`: minúsculas, hífen, sem espaço, sem acento, sem underscore.
- **Descritivo e único no vault inteiro.** O Obsidian resolve `[[link]]` por nome de arquivo — dois `estudo.md` em pastas diferentes tornam todo link ambíguo.
  - ✅ `clean-code.md`, `padrao-de-repositorios.md`, `docker-compose.md`
  - ❌ `estudo.md`, `notas.md`, `README2.md`, `Estudo Docker.md`
- Exceção: `README.md` (índice de domínio) e `SKILL.md` (formato fixo do Claude).

---

## 4. Frontmatter

Toda nota de conhecimento começa com:

```yaml
---
titulo: "Título legível da nota"
resumo: "Uma linha dizendo o que a nota entrega — é o que aparece no índice."
tipo: conceito        # conceito | referencia | persona | regra | decisao
dominio: engenharia   # ia | engenharia | infra | ferramentas
tags: [engenharia/clean-code, qualidade-de-codigo]
status: ativo         # rascunho | ativo | arquivado
atualizado: 2026-08-09
---
```

- **Use aspas em `titulo` e `resumo`.** Sem aspas, um `:` no meio do texto quebra o YAML e a nota some do índice.
- `resumo` é opcional para o validador, mas é ele que faz o índice ser útil. Nota sem resumo aparece só com o título.
- `tags` usa hierarquia com `/` — o painel de tags do Obsidian agrupa sozinho.
- `status: rascunho` é permitido e útil: melhor uma nota incompleta marcada do que nenhuma nota.
- Atualize `atualizado` quando mudar o conteúdo de verdade, não a cada vírgula.

**Não coloque esse frontmatter em `SKILL.md`.** Skill do Claude usa frontmatter próprio (`name` + `description`) e campos extras podem quebrar o carregamento. Arquivos dentro de `references/` de uma skill também ficam sem frontmatter — eles fazem parte do pacote da skill, não são notas do vault.

---

## 5. Links

- Entre notas do vault: `[[nome-do-arquivo]]` (wikilink do Obsidian).
- Para arquivos de skill ou qualquer coisa fora do grafo de notas: link markdown relativo — `[clean-code](ia/agentes/claude/skills/clean-code/SKILL.md)`.
- **O índice dos README é gerado, não escrito à mão.** Ele vive entre os marcadores `INICIO:INDICE` / `FIM:INDICE` e sai do frontmatter. Não edite dentro dos marcadores — rode `./scripts/gerar-indices.py`. Prosa, tabelas curadas e backlog ficam fora dos marcadores e são preservados.

---

## 6. Skills

Uma skill é uma pasta em `ia/agentes/claude/skills/<nome>/` com:

```text
ia/agentes/claude/skills/<nome>/
├── SKILL.md              # obrigatório: frontmatter name + description, e as regras operacionais
└── references/           # opcional: material de apoio carregado só quando necessário
```

Regras práticas:

- `name` no frontmatter **igual** ao nome da pasta.
- `description` diz *o que faz* e *quando acionar* — é isso que o modelo lê para decidir usar a skill. Descrição vaga = skill que nunca dispara.
- `SKILL.md` enxuto (o suficiente para agir). Detalhe longo vai para `references/` e é citado no final, com uma linha dizendo quando vale abrir.
- **Uma skill por assunto.** Duas skills com o mesmo `name` fazem o carregamento ficar imprevisível e as regras se contradizerem.
- Depois de criar ou editar, rode `./scripts/sync-skills.sh --apply`.

---

## 7. ADR (registro de decisão)

- Mora **no domínio da decisão**, não numa pasta de tipo: decisão de observabilidade em `infra/`, de estrutura de código em `engenharia/`.
- Nome com número sequencial: `adr-001-observabilidade.md`. O número não reinicia por domínio.
- `tipo: decisao` no frontmatter, e a tag `adr`.
- Comece a partir de `templates/decisao.md`.
- **ADR específica de um projeto mora no repositório do projeto**, não aqui. Este vault guarda decisão de padrão pessoal — o que vale para projeto novo em geral. A arquitetura de um sistema específico vive com o sistema.
- Nem toda escolha vira ADR. O portão está na skill `decisao-arquitetural`: se é fácil de reverter, não precisa de registro formal.

---

## 8. Commits

Mensagem no imperativo, dizendo o conhecimento que entrou ou mudou:

```text
adiciona nota de docker compose em infra
corrige regra de idioma da skill clean-code
reorganiza personas para ia/personas
```

Evite `update`, `wip`, `ajustes`.

---

## 9. Checklist de nota nova

- [ ] Está no domínio certo (assunto, não ferramenta usada)?
- [ ] Nome em `kebab-case`, descritivo e único no vault?
- [ ] Frontmatter preenchido, com `titulo` e `resumo` entre aspas (e ausente, se for `SKILL.md`)?
- [ ] Não duplica conteúdo que já existe em outra nota ou skill?
- [ ] `./scripts/gerar-indices.py` rodado e o resultado commitado junto?
- [ ] `./scripts/validar-vault.py` passa?

O hook de pre-commit checa os dois últimos itens sozinho — ver seção 10.

---

## 10. Automação disponível

| Script | O que faz |
| ------ | --------- |
| `./scripts/nova-nota.sh <dominio> <nome>` | Cria a nota já com frontmatter e data preenchidos, valida o nome e regenera o índice. É o caminho normal para começar uma nota. |
| `./scripts/gerar-indices.py` | Regenera o índice de cada README a partir do frontmatter. `--check` só verifica e sai com 1 — é o que o CI roda. |
| `./scripts/validar-vault.py` | Checa link quebrado, wikilink ambíguo, nome duplicado, frontmatter inválido e skill mal formada. Sai com código 1 em caso de problema. |
| `./scripts/sync-skills.sh` | Liga `ia/agentes/claude/skills/*` em `~/.claude/skills` por symlink. Sem argumento só simula; `--apply` executa. Nunca apaga diretório real. |

**Ative o hook uma vez por clone:**

```bash
git config core.hooksPath .githooks
```

A partir daí, todo commit roda validação e checagem de índice. Para pular pontualmente: `git commit --no-verify`. O mesmo par roda no GitHub Actions (`.github/workflows/validar-vault.yml`), então pular o hook local só adia o erro.

---

## 11. Navegação no Obsidian

`vault.base` é uma Base do Obsidian com cinco visões sobre o mesmo conjunto de notas: **Todas** (agrupadas por domínio), **Rascunhos** (o que está pela metade), **Sem resumo** (o que não vai aparecer bem no índice), **Referências** e **Decisões (ADR)**.

Ela lê o frontmatter — nota sem `tipo` não aparece. É complementar ao README, não substituta: a Base é navegação dentro do Obsidian, o README é a porta de entrada no GitHub.
