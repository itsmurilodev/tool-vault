---
titulo: "Thermo-nuclear code quality review — revisão rígida de manutenibilidade (Cursor)"
resumo: "Skill da Cursor (MIT) que faz uma auditoria implacável da branch: code judo, arquivo acima de 1.000 linhas, if solto, wrapper fino. Útil só em modo relatório e em PR grande; aplicada sozinha, viola a regra de menor alteração."
tipo: referencia
dominio: murilo
tags: [murilo/radar, radar/verificacao-e-qualidade, skills, revisao]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: avaliar
categoria: verificacao-e-qualidade
natureza: skill
quando_usar: "Em PR de feature ou refactor grande, ou em módulo chegando a 1.000 linhas, sempre em modo relatório (você aceita achado por achado)."
quando_nao_usar: "Bug fix pequeno; aplicação automática das sugestões (manda reestruturar parte do codebase, contra a regra de menor alteração segura)."
pre_requisito: "Branch com diff para revisar e alguém para decidir cada achado."
---

# Thermo-nuclear code quality review

> **Radar: ⏳ avaliar.** Bom revisor, mau executor: use para **encontrar** problemas, não para aplicar sozinho.

## O que é

`thermo-nuclear-code-quality-review`, do `cursor/plugins/cursor-team-kit` (MIT, Cursor). Faz uma revisão de qualidade muito rígida da branch atual. Uma skill irmã, `thermo-nuclear-review`, cobre bugs e segurança, e a `thermos` roda as duas em paralelo.

Regras principais:

- "seja **ambicioso**": procure *code judo*, a reestruturação que apaga complexidade em vez de só mudá-la de lugar;
- não deixar um arquivo passar de **1.000 linhas**;
- não aceitar `if` solto em fluxo alheio;
- marcar wrapper fino e indireção inútil;
- deixar a lógica na camada certa;
- rejeitar `any` e `as` sem motivo.

## Quando usar

- PR de feature ou refactor que mexe em estrutura.
- Auditoria periódica de um módulo que cresceu demais.
- Sempre pedindo **relatório**, não aplicação.

## Quando não usar

- Bug fix pequeno: aumenta o diff que deveria ficar pequeno.
- Em modo automático: a skill manda *"restructuring some of the codebase, go for it"*, o que contraria a `clean-code` e as suas diretrizes (problema fora do escopo se relata, não se corrige).
- Junto com o Ponytail aplicando as duas: uma manda subtrair, a outra reestruturar, e o diff entra em círculo.

## Como usar

1. Rode a skill sobre a branch e peça **só a lista de achados**.
2. Aceite ou recuse cada um. O que for fora de escopo vira issue.
3. Coloque as regras mecânicas da skill no CI, em vez de depender do LLM: arquivo acima de 1.000 linhas, `any` e `as` (Biome, Knip, `tsc --strict`).

## Ver também

- [[skills-de-qualidade-de-codigo]] · [[ponytail]] · [[qualidade-automatizada]] · [[categoria-verificacao-e-qualidade]]

## Fontes

- [cursor/plugins — thermo-nuclear-code-quality-review](https://github.com/cursor/plugins/tree/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review)
