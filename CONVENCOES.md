# Convenções do vault

Regras para manter o vault consistente conforme ele cresce. Se uma regra aqui atrapalhar mais do que ajudar, mude a regra — não crie exceção silenciosa.

---

## 1. Onde colocar a nota

Decida por **domínio** (o assunto), não por como você aprendeu.

| Domínio        | O que entra                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| `ia/`          | LLMs, agentes, prompt engineering, skills, personas, regras de comportamento |
| `engenharia/`  | Código, arquitetura, padrões, testes, refatoração, qualidade                 |
| `infra/`       | Cloud, containers, redes, Linux, CI/CD, observabilidade, banco de dados      |
| `ferramentas/` | Git/GitHub, editor, terminal, CLIs, produtividade                            |

> Um estudo de Clean Code feito conversando com uma IA é conhecimento de **engenharia**, não de IA. O domínio é o assunto da nota, não a ferramenta usada para produzi-la.

**Quando criar um domínio novo:** só quando existirem 3+ notas que não cabem em nenhum dos atuais. Antes disso, coloque no domínio mais próximo.

**Quando criar subpasta:** só quando o tópico tiver 3+ arquivos. Um tópico com uma nota só é um arquivo solto no domínio (`engenharia/clean-code.md`), não uma pasta com um arquivo dentro.

---

## 2. Conhecimento vs artefato

Duas naturezas diferentes, tratadas de formas diferentes:

- **Conhecimento** (`conceitos/`, notas de domínio) — o que eu aprendi. Pode ser longo, ter analogia, exemplo, contexto histórico. Escrito para o meu eu do futuro.
- **Artefato** (`ia/skills/`, `ia/personas/`, `ia/regras/`) — o que uma IA consome e executa. Deve ser enxuto, operacional e sem teoria decorativa. Escrito para uma máquina seguir.

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
titulo: Título legível da nota
tipo: conceito        # conceito | referencia | persona | regra | decisao
dominio: engenharia   # ia | engenharia | infra | ferramentas
tags: [engenharia/clean-code, qualidade-de-codigo]
status: ativo         # rascunho | ativo | arquivado
atualizado: 2026-08-09
---
```

- `tags` usa hierarquia com `/` — o painel de tags do Obsidian agrupa sozinho.
- `status: rascunho` é permitido e útil: melhor uma nota incompleta marcada do que nenhuma nota.
- Atualize `atualizado` quando mudar o conteúdo de verdade, não a cada vírgula.

**Não coloque esse frontmatter em `SKILL.md`.** Skill do Claude usa frontmatter próprio (`name` + `description`) e campos extras podem quebrar o carregamento. Arquivos dentro de `references/` de uma skill também ficam sem frontmatter — eles fazem parte do pacote da skill, não são notas do vault.

---

## 5. Links

- Entre notas do vault: `[[nome-do-arquivo]]` (wikilink do Obsidian).
- Para arquivos de skill ou qualquer coisa fora do grafo de notas: link markdown relativo — `[clean-code](ia/skills/clean-code/SKILL.md)`.
- Toda nota nova entra no `README.md` do seu domínio. Índice desatualizado é vault perdido.

---

## 6. Skills

Uma skill é uma pasta em `ia/skills/<nome>/` com:

```text
ia/skills/<nome>/
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

## 7. Commits

Mensagem no imperativo, dizendo o conhecimento que entrou ou mudou:

```text
adiciona nota de docker compose em infra
corrige regra de idioma da skill clean-code
reorganiza personas para ia/personas
```

Evite `update`, `wip`, `ajustes`.

---

## 8. Checklist de nota nova

- [ ] Está no domínio certo (assunto, não ferramenta usada)?
- [ ] Nome em `kebab-case`, descritivo e único no vault?
- [ ] Frontmatter preenchido (e ausente, se for `SKILL.md`)?
- [ ] Linkada no `README.md` do domínio?
- [ ] Não duplica conteúdo que já existe em outra nota ou skill?
- [ ] `./scripts/validar-vault.py` passa?

## 9. Automação disponível

| Script | O que faz |
| ------ | --------- |
| `./scripts/validar-vault.py` | Checa link quebrado, wikilink ambíguo, nome duplicado, frontmatter faltando e skill mal formada. Sai com código 1 em caso de problema — dá para virar pre-commit. |
| `./scripts/sync-skills.sh` | Liga `ia/skills/*` em `~/.claude/skills` por symlink. Sem argumento só simula; `--apply` executa. Nunca apaga diretório real. |
