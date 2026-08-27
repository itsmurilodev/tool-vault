---
titulo: Padrão de nomes de repositórios GitHub
resumo: "Prefixos oficiais e formato `<contexto>-<projeto>-<tipo>` em kebab-case."
tipo: referencia
dominio: murilo
tags: [ferramentas/github, convencao]
status: ativo
atualizado: 2026-08-09
---

# Padrão de nomes de repositórios GitHub

Padrão para organizar os repositórios do GitHub de forma clara, consistente e fácil de manter. A ideia é evitar nomes soltos, genéricos ou misturados, separando os repositórios por contexto e tipo de projeto.

## Formato

```text
<contexto>-<nome-do-projeto>-<tipo>
```

Exemplo:

```text
study-jogo-numero-secreto-exercise
```

Sempre em `kebab-case`:

- tudo em letras minúsculas;
- palavras separadas por hífen;
- sem espaços;
- sem acentos;
- sem PascalCase;
- sem mistura desnecessária de idiomas.

O sufixo `<tipo>` é opcional quando o nome do projeto já deixa a natureza óbvia (`tool-vault`). Use quando o mesmo projeto puder existir em mais de uma forma (`exercise`, `api`, `web`, `docs`).

## Prefixos oficiais

O prefixo indica o contexto principal do repositório.

| Prefixo    | Uso                                                       |
| ---------- | --------------------------------------------------------- |
| `study-`   | Faculdade, cursos, exercícios e atividades de aprendizado |
| `lab-`     | Testes, experimentos e provas de conceito                 |
| `app-`     | Aplicações reais ou sistemas completos                    |
| `site-`    | Sites, landing pages, portfólios e páginas institucionais |
| `tool-`    | Ferramentas internas, automações e utilitários            |
| `client-`  | Projetos de clientes ou freelas                           |
| `company-` | Projetos internos da empresa/marca                        |
| `archive-` | Repositórios antigos, parados ou sem manutenção ativa     |

## Como usar na prática

- Ao criar um repositório novo, escolha o prefixo antes do nome — se nenhum prefixo servir, o repositório provavelmente não tem contexto definido ainda.
- Ao aposentar um projeto, renomeie para `archive-<nome-antigo>` em vez de deletar: preserva histórico e tira do caminho.
- A mesma regra de `kebab-case` vale para nomes de arquivo dentro deste vault — veja [[CONVENCOES]].
