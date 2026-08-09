Modelo de `SKILL.md`. Copie para `ia/skills/<nome>/SKILL.md` e apague esta linha e a próxima.

**Atenção:** o frontmatter de skill tem só `name` e `description`. Não adicione os campos do frontmatter de nota (`tipo`, `dominio`, `tags`) aqui.

---

```markdown
---
name: nome-da-skill
description: >
  O que a skill faz, em uma frase. Depois: QUANDO acionar, com gatilhos
  concretos que apareçam na fala real do usuário — é isso que o modelo lê
  para decidir usar a skill. Se houver mais de um modo de operação, dizer
  qual pedido leva a qual modo. Terminar com quando NÃO usar, se houver
  risco de disparo indevido.
---

# {{Título da skill}}

Uma ou duas linhas dizendo qual problema concreto esta skill resolve — não o que ela é, mas o que muda por ela existir.

**Idioma:** toda comunicação é em português do Brasil, direta e simples, sem jargão desnecessário.

## Portão — vale aplicar isso agora?

Nem todo pedido merece o processo completo. Aplicar quando:

- condição 1;
- condição 2.

Não aplicar quando: (casos triviais em que o processo custa mais do que entrega).

## Modo padrão — {{comportamento default}}

Aplicar silenciosamente estas regras, sem produzir relatório:

- **Regra 1.** Explicação com exemplo do errado e do certo.
- **Regra 2.**

## Modo {{secundário}} — {{quando}}

Aqui sim produzir saída visível, nesta ordem:

1. Passo.
2. Passo.

**Formato de saída obrigatório:**

```
## Seção 1
## Seção 2
```

## Guardrails

O que não fazer, mesmo que pareça uma boa ideia no momento:

- Restrição 1.
- Restrição 2.

## Referências ampliadas

- `references/<arquivo>.md` — o que tem lá e quando vale abrir. Não precisa ser lido para o uso normal.
```
