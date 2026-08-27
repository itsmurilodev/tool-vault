---
titulo: "Fluxo Issue → PR → commit padronizado"
resumo: "Disciplina de fluxo, Conventional Commits e commitlint — custo zero, alto retorno."
tipo: referencia
dominio: murilo
tags: [murilo/engenharia, ferramentas/github, git, processo]
status: ativo
atualizado: 2026-08-27
---

# Fluxo Issue → PR → commit padronizado

## 📌 Resumo

A prática de mais alto retorno por custo em toda a categoria de "ferramentas de produtividade": **nenhuma ferramenta nova, nenhuma licença.** É disciplina de fluxo — toda mudança começa numa issue, vira um PR que referencia a issue, e o padrão fica gravado num arquivo que qualquer pessoa (ou agente) lê antes de trabalhar.

O ganho não é burocrático. É que o **porquê** da mudança para de morar só na sua cabeça.

## 🧠 1. Issue antes de código

A issue responde três coisas que o commit sozinho nunca responde:

- qual problema existe (não qual código mudar);
- por que resolvê-lo agora;
- como saber que foi resolvido — o critério de aceite.

Isso é a versão leve do que a skill `levantamento-requisitos` faz em profundidade. Para mudança trivial, a issue é uma linha; para funcionalidade, ela carrega o critério de aceite.

## 🧠 2. PR que referencia a issue

O PR referencia a issue (`Closes #12`), o que fecha o ciclo automaticamente e liga o diff ao contexto para sempre. Daqui a um ano, `git blame` naquela linha leva ao PR, que leva à issue, que explica o motivo.

Regra prática: **PR pequeno o suficiente para ser revisado de verdade.** PR de 40 arquivos não é revisado — é aprovado.

## 🧠 3. Padrão gravado em arquivo

O terceiro elemento é escrever o padrão num arquivo versionado do repositório (`CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`) para que qualquer pessoa ou agente siga sem precisar perguntar: como nomear branch, formato de commit, o que precisa passar antes do merge.

Instrução escrita em arquivo é a única que sobrevive à troca de contexto — sua e do agente.

## 🧠 4. Conventional Commits e commitlint

**Conventional Commits** é o padrão de mensagem: `tipo(escopo): descrição`.

```text
feat(auth): adiciona login com magic link
fix(api): corrige timeout na busca de contatos
refactor(ui): extrai botão primário para componente
docs: atualiza convenções do vault
chore(deps): sobe versão do vitest
```

**commitlint** é a ferramenta que valida a mensagem contra esse padrão e rejeita o commit fora do formato. Costuma rodar via hook de Git (Husky ou similar).

*(A entrada "Comilint" que aparece em listas virais é quase certamente commitlint com o nome errado.)*

Ganhos reais: changelog gerado automaticamente, versionamento semântico derivado do tipo do commit, e histórico legível. Custo: baixo, mas **é atrito em todo commit** — em projeto de uma pessoa sem release automatizada, o padrão sozinho já entrega quase todo o valor; o commitlint só se justifica quando há mais de uma pessoa commitando ou quando o changelog é gerado a partir do histórico.

> Isso não conflita com a convenção deste vault, que usa mensagem em imperativo e português (ver [CONVENCOES.md](../../../../CONVENCOES.md) seção 7). Vault de conhecimento não gera release. Aplicar Conventional Commits em repositório de código, e o padrão simples aqui.

## 🧠 5. Templates Padrão de Issue (`.github/ISSUE_TEMPLATE/`)

Para manter as issues concisas e orientadas à ação (tanto para você quanto para agentes de IA), use a tríade padrão:

1. **`01_bug_report.md`** (`fix: `): Comportamento ocorrido, comportamento esperado, passos de reprodução e critério de resolução.
2. **`02_feature_request.md`** (`feat: `): Dor/oportunidade, proposta de solução, regras de negócio e critérios de aceite (*Definition of Done*).
3. **`03_technical_task.md`** (`chore: ` / `refactor: `): Motivação técnica, plano de ação em checklist, riscos/áreas afetadas e validação.

> 📁 Os templates canônicos estão salvos em `.github/ISSUE_TEMPLATE/` e podem ser copiados diretamente para qualquer repositório (`app-encaixe`, `app-asynchub`, `site-institucional`).

## ✅ Como aplicar

| Estágio | O que adotar |
| ------- | ------------ |
| Qualquer um | Issue via Template → PR referenciando a issue (`Closes #NN`) → padrão escrito em arquivo. Custo zero |
| Projeto com mais de uma pessoa ou com release | Conventional Commits + commitlint em hook |
| Projeto com CI | Exigir check verde antes do merge |


## ⚠️ Erros comuns

- Issue escrita depois do PR, só para cumprir tabela — vira ruído, não contexto.
- Padrão que só existe na cabeça de quem criou o repositório.
- commitlint instalado sem ninguém gerar changelog: puro atrito sem retorno.
- Branch de vida longa: quanto mais tempo aberta, mais cara a integração.

## 🔗 Ver também

- [[padrao-de-repositorios]] — nomenclatura dos repositórios.
- [[adocao-de-ferramenta]] — por que este item é o único da categoria que não precisa de portão.
- Skill [levantamento-requisitos](../../../ia/agentes/claude/skills/levantamento-requisitos/SKILL.md) — o que entra numa issue de funcionalidade.
