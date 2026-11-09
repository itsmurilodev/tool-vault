---
titulo: "pstack — coleção de skills de engenharia da Cursor (poteto)"
resumo: "Cerca de 47 skills e 23 playbooks da Lauren Tan (Cursor). Vale copiar skills isoladas quando houver dor: as duas de verificação já estão no vault. O pacote inteiro e o poteto-mode não."
tipo: referencia
dominio: murilo
tags: [murilo/radar, radar/verificacao-e-qualidade, skills, agentes]
status: ativo
atualizado: 2026-11-09
# radar (lido por gerar-indices.py e por agentes)
radar: testar
categoria: verificacao-e-qualidade
natureza: skill
quando_usar: "Copiar uma skill isolada quando a dor dela existir: create/maintain-verification-skill (já no vault), typescript-best-practices (bug de tipo recorrente), unslop (texto de PR e docs)."
quando_nao_usar: "Instalar o pacote inteiro ou o poteto-mode (delega código ao Grok, depende de recursos da Cursor); no-comments sem o resto do pstack."
pre_requisito: "Para as skills de verificação: app que sobe localmente a partir de banco vazio com seed."
---

# pstack

> **Radar: 🧪 testar.** Coleção boa de onde **tirar peças**, não um pacote para instalar inteiro.

## O que é

Skills e playbooks de engenharia da Lauren Tan (*poteto*), do time do React Compiler e engenheira na Cursor. A fonte oficial é `cursor/plugins/pstack` (MIT). O mirror que funciona fora da Cursor é `backnotprop/pstack`. Há dezenas de forks com o mesmo nome, alguns sem relação nenhuma.

## Peça por peça

| Skill | Radar | Quando usar | Situação no vault |
| --- | --- | --- | --- |
| `create-verification-skill` / `maintain-verification-skill` | 🧪 testar | Projeto com UI em que o agente diz "pronto" sem provar | ✅ Copiadas para `murilo/ia/agentes/skills/`. Análise em [[pstack-verificacao]]. |
| `typescript-best-practices` | ⏳ avaliar | Bug de tipo recorrente (`any`, `as`, `undefined`) em projeto TS | Não copiada. Depende de `principle-type-system-discipline`. |
| `unslop` | ⏳ avaliar | Texto de PR, docs e notas, nunca código | Não copiada |
| `no-comments` | ⛔ evitar | — | Depende de `/how`, `/why` e `/architect`. A `clean-code` já cobre a regra de comentário. |
| `poteto-mode` (23 playbooks) | ⛔ evitar | — | Delega código ao Grok, multi-modelo, centrado na Cursor |

## Como usar

1. Copie **só** a pasta da skill, mais as dependências que o README do mirror lista, fixando o commit, e mantenha o `LICENSE` MIT.
2. Rode `./scripts/sync-skills.sh --apply`.
3. Registre na ficha qual skill entrou e de qual commit veio.

Evite `npx skills add backnotprop/pstack`, que lista o pacote inteiro.

## Riscos

- Ecossistema confuso, com forks e ports chamados "pstack". Use só a fonte oficial ou o mirror.
- Várias skills chamam outras. Copiar sem as dependências quebra o fluxo.

## Ver também

- [[pstack-verificacao]] · [[skills-de-qualidade-de-codigo]] · [[categoria-verificacao-e-qualidade]]

## Fontes

- [cursor/plugins — pstack](https://github.com/cursor/plugins/tree/main/pstack) · [backnotprop/pstack](https://github.com/backnotprop/pstack)
