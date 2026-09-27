# AGENTS.md — como um agente de IA usa este vault

> Ponto de entrada para qualquer agente (Claude, Codex, Cursor, Gemini, Antigravity). Humano: comece pelo [README.md](README.md).

Este repositório é o **segundo cérebro do Murilo**: preferências, métodos, decisões e conhecimento técnico verificado. Quando a pergunta envolver como o Murilo trabalha, qual stack usar, o que já foi decidido ou como a marca Async se apresenta, **a fonte é este vault — não a sua memória de treino**.

---

## 1. Protocolo de consulta

1. **Comece pelo índice, não pelas pastas.** O [README.md](README.md) (seção *Índice Consolidado*) lista toda nota com uma linha de `resumo`. Leia o resumo e só abra a nota que responde a pergunta — economiza contexto.
2. **Use a rota certa:**

| Se a pergunta é sobre… | Leia primeiro |
| :--- | :--- |
| Como se comportar, tom, quando perguntar | `murilo/ia/regras/global-rules.md` |
| Como o Murilo trabalha, stack padrão | `murilo/perfil/modus-operandi.md` |
| Começar um projeto/app/produto novo | skill `murilo/ia/agentes/skills/fluxo-de-projeto/` |
| Método: código, requisito, ADR, UI, segurança | `murilo/ia/agentes/skills/` (tabela em `murilo/ia/agentes/README.md`) |
| Adotar ferramenta/biblioteca nova | `murilo/engenharia/adocao-de-ferramenta.md` |
| Infra (banco, auth, email, fila, observabilidade) | `murilo/engenharia/infra/` |
| Marca, cores, tipografia, tom de voz da Async | `async/identidade/` e `async/design-system/` |
| Produtos da Async e decisões (ADRs) | `async/produtos/` |

3. **Confira a confiabilidade no frontmatter antes de afirmar algo:**
   - `status: rascunho` → ideia em construção, não decisão. Diga isso ao usar.
   - `tipo: decisao` (ADR) → decisão registrada; vence nota de conceito em caso de conflito.
   - `atualizado` → preço, limite de free tier, versão e benchmark mudam rápido. Se a nota tem mais de ~6 meses, verifique a fonte atual antes de usar o número numa decisão.
   - Número de benchmark em nota de ferramenta é **alegação da fonte citada**, não fato medido pelo Murilo. Trate como hipótese.
4. **Conflito entre regras:** regra do projeto > regra global, desde que não viole segurança, escopo ou honestidade técnica (`global-rules` §14).
5. **Não achou no vault?** Diga que não está registrado. Não preencha com suposição apresentada como preferência do Murilo.

---

## 2. Escrevendo no vault

- Siga [CONVENCOES.md](CONVENCOES.md): dois pilares (`murilo/`, `async/`), nome `kebab-case` único no vault inteiro, frontmatter obrigatório.
- Crie nota com `./scripts/nova-nota.sh <pilar/subpasta> <nome>` — já sai com frontmatter.
- **Nunca edite à mão** o trecho entre `<!-- INICIO:INDICE -->` e `<!-- FIM:INDICE -->`. Depois de criar ou renomear nota:

```bash
./scripts/gerar-indices.py && ./scripts/validar-vault.py
```

- Conteúdo não verificado entra como `status: rascunho`, com a seção **Fontes** preenchida. Separe fato, hipótese e opinião.
- **Skill é método, não fato de projeto.** Arquitetura, requisitos e docs de um projeto específico vivem no repositório do projeto, não aqui.
- Commit em português, imperativo, minúsculas, sem ponto final: `adiciona nota sobre redis`.
