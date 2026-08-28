# Convenções do vault

Regras para manter o vault consistente conforme ele cresce. Se uma regra aqui atrapalhar mais do que ajudar, mude a regra — não crie exceção silenciosa.

---

## 1. Onde colocar a nota

O vault é dividido em **dois grandes pilares canônicos** de primeiro nível:

| Pilar | Subpastas | O que entra |
| :--- | :--- | :--- |
| **`murilo/`** | `perfil/`<br>`estudos/`<br>`engenharia/`<br>`ia/` | Modus operandi, preferências de trabalho.<br>Disciplinas de faculdade e cursos.<br>Clean code, padrões, infraestrutura, ferramentas e dev geral.<br>Engenharia de prompts, personas, regras de agentes e skills. |
| **`async/`** | `identidade/`<br>`design-system/`<br>`produtos/`<br>`negocio/` | Brandbook, paleta de cores, tipografia, tom de voz.<br>Tokens CSS, componentes de UI, padrões de interface.<br>Visão dos produtos SaaS (Encaixe, AsyncHub, Site) e ADRs corporativas.<br>Marketing, vendas, prospecção B2B, SEO/AEO e growth. |

> Um estudo de Clean Code ou Docker é conhecimento de **`murilo/engenharia/`**. As decisões de marca, cores e produtos da Async vivem em **`async/`**.

**Dentro de `murilo/ia/`, há um segundo corte:** o que é conceito de prompt/LLM fica em `conceitos/`, personas em `personas/`, regras em `regras/`, e skills/conectores/configurações em `agentes/`.

---

## 2. Conhecimento vs artefato

Duas naturezas diferentes, tratadas de formas diferentes:

- **Conhecimento** (`conceitos/`, notas técnicas de domínio, brandbook) — o que foi estudado ou decidido. Escrito em formato legível para humanos e para consulta de agentes (RAG / MCP).
- **Artefato** (`murilo/ia/agentes/skills/`, `personas/`, `regras/`) — o que uma IA consome e executa operacionalmente. Deve ser enxuto, direto e sem teoria decorativa.

Quando os dois existem para o mesmo assunto, o artefato **referencia** o conhecimento em vez de copiá-lo.

---

## 3. Nomes de arquivo

- `kebab-case`: minúsculas, hífen, sem espaço, sem acento, sem underscore.
- **Descritivo e único no vault inteiro.** O Obsidian resolve `[[link]]` por nome de arquivo — dois `estudo.md` em pastas diferentes tornam todo link ambíguo.
  - ✅ `clean-code.md`, `paleta-de-cores.md`, `docker-compose.md`
  - ❌ `estudo.md`, `notas.md`, `README2.md`, `Estudo Docker.md`
- Exceção: `README.md` (índice de domínio) e `SKILL.md` (formato padrão de skill para agentes).

---

## 4. Frontmatter

Toda nota de conhecimento começa com:

```yaml
---
titulo: "Título legível da nota"
resumo: "Uma linha dizendo o que a nota entrega — é o que aparece no índice."
tipo: conceito        # conceito | referencia | persona | regra | decisao
dominio: murilo       # murilo | async
tags: [murilo/engenharia, qualidade-de-codigo]
status: ativo         # rascunho | ativo | arquivado
atualizado: 2026-08-26
---
```

- **Use aspas em `titulo` e `resumo`.**
- `tags` usa hierarquia com `/` (ex: `murilo/estudos`, `async/produtos`).
- `status: rascunho` é permitido e útil.
- **Não coloque esse frontmatter em `SKILL.md`.** Skill de agente usa frontmatter próprio (`name` + `description`).

---

## 5. Links

- Entre notas do vault: `[[nome-do-arquivo]]` (wikilink do Obsidian).
- Para arquivos de skill ou qualquer coisa fora do grafo de notas: link markdown relativo — `[clean-code](murilo/ia/agentes/skills/clean-code/SKILL.md)`.
- **O índice dos README é gerado, não escrito à mão.** Execute `./scripts/gerar-indices.py`.

---

## 6. Skills

Uma skill é uma pasta em `murilo/ia/agentes/skills/<nome>/` com:

```text
murilo/ia/agentes/skills/<nome>/
├── SKILL.md              # obrigatório: frontmatter name + description, e regras operacionais
└── references/           # opcional: material de apoio carregado sob demanda
```

Depois de criar ou editar, sincronize com os agentes locais:
```bash
./scripts/sync-skills.sh --apply
```

---

## 7. Mensagens de commit no vault

No `tool-vault`, a mensagem é em **português, no imperativo, minúsculas, sem ponto final**:

- ✅ `adiciona nota sobre redis e fila`
- ✅ `corrige frontmatter de clean-code`
- ❌ `Added redis note` / `adicionando nota...` / `nota de redis.`
