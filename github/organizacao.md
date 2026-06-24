# Organização dos Repositórios GitHub

Este documento resume o padrão definido para organizar os repositórios do GitHub de forma mais clara, consistente e fácil de manter.

A ideia principal é evitar nomes soltos, genéricos ou misturados, separando os repositórios por contexto e tipo de projeto.

---
## Padrão escolhido


```text

<contexto>-<nome-do-projeto>-<tipo>

```

Sempre usando:

```text

kebab-case

```

Ou seja:

- tudo em letras minúsculas;
- palavras separadas por hífen;
- sem espaços;
- sem acentos;
- sem PascalCase;
- sem mistura desnecessária de idiomas.

Exemplo:

```text

study-jogo-numero-secreto-exercise

```
---

  

## Prefixos oficiais

Os prefixos indicam o contexto principal do repositório.
  
| Prefixo   ->  Uso |

| `study-`    -> Faculdade, cursos, exercícios e atividades de aprendizado |

| `lab-`      -> Testes, experimentos e provas de conceito |

| `app-`      ->  Aplicações reais ou sistemas completos |

| `site-`     -> Sites, landing pages, portfólios e páginas institucionais |

| `tool-`     -> Ferramentas internas, automações e utilitários |

| `client-`   -> Projetos de clientes ou freelas |

| `company-`  -> Projetos internos da empresa/marca |

| `archive-`  -> Repositórios antigos, parados ou sem manutenção ativa |