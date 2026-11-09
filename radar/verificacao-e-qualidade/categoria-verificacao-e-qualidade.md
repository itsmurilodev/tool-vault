---
titulo: "Categoria — Verificação & Qualidade"
resumo: "Página-guia da categoria: como provar que o código do agente funciona (verify-<app>) e como mantê-lo enxuto e legível (clean-code + escada do Ponytail, revisão rígida só em relatório, regras mecânicas no CI)."
tipo: conceito
dominio: radar
tags: [murilo/radar, radar/verificacao-e-qualidade, categoria]
status: ativo
atualizado: 2026-11-09
---

# Verificação & Qualidade

> **Em uma frase:** o agente só termina quando **prova** que funciona, e o código que ele deixa precisa ser o **menor e mais claro** possível.

## 🧠 A ideia em linguagem simples

São duas perguntas diferentes:

1. **Funciona?** Teste unitário passando não prova que o usuário consegue usar. A resposta vem de **subir o app e usar como um usuário**, guardando evidência. É o trabalho do `verify-<app>`, gerado pela skill do pstack.
2. **Está bem escrito?** Código de IA tende a inchar (lib desnecessária, wrapper, abstração "para depois"). A resposta vem em **três camadas que não se sobrepõem**: regra ao escrever, regra mecânica no CI e revisão humana ou de outro modelo no PR.

> 💡 **Analogia:** a vistoria de um carro. Primeiro você liga e anda com ele (funciona?). Depois olha se não sobrou peça solta nem fita isolante no motor (está bem feito?).

## 🗺️ Mapa da categoria

```mermaid
flowchart LR
    A["Agente escreve código"] --> B["clean-code + escada do Ponytail<br/>(regra ao escrever)"]
    B --> C["CI: Biome, Knip, tsc --strict<br/>(regras mecânicas)"]
    C --> D["verify-app<br/>(sobe o app e prova)"]
    D --> E{"PR de feature<br/>ou refactor grande?"}
    E -- "sim" --> F["Revisão: /simplify ou<br/>thermo-nuclear em relatório"]
    E -- "não" --> G["Revisão normal +<br/>2º modelo"]
    F --> H["Você faz o merge"]
    G --> H
```

## 📋 Itens da categoria

| Item | Radar | Quando usar | Ficha |
| --- | --- | --- | --- |
| Ponytail (escada de decisão) | ✅ adotar | Ao escrever código. Já está dentro da `clean-code`. | [[ponytail]] |
| pstack: `create/maintain-verification-skill` | 🧪 testar | Projeto com UI em que o agente diz "pronto" sem provar | [[pstack]] · [[pstack-verificacao]] |
| Impeccable (59 regras de UI) | ✅ adotar | Ao gerar, editar ou auditar UI, para tirar a "cara de IA" | [[impeccable]] |
| Spec to Code Compliance | ✅ adotar | Validar entrega contra SPEC, PRD ou requisito de cliente | [[spec-to-code-compliance]] |
| Thermo-nuclear review | ⏳ avaliar | PR grande ou módulo perto de 1.000 linhas, só em relatório | [[thermo-nuclear-review]] |

## 🧭 Como decidir

```mermaid
flowchart TD
    Q1{"O agente consegue provar<br/>que a feature funciona?"} -- "não" --> V["Criar verify-app<br/>/create-verification-skill"]
    Q1 -- "sim" --> Q2{"A feature mudou de<br/>comportamento ou tela?"}
    Q2 -- "sim" --> M["/maintain-verification-skill"]
    Q2 -- "não" --> Q3{"O diff é grande<br/>ou estrutural?"}
    Q3 -- "sim" --> T["Revisão rígida em modo relatório"]
    Q3 -- "não" --> N["clean-code + CI bastam"]
```

## ⚠️ O que não fazer

- Empilhar Ponytail, thermo-nuclear e as skills de limpeza do pstack em **todo** PR: elas se contradizem (subtrair vs reestruturar) e o diff cresce. Ver [[skills-de-qualidade-de-codigo]].
- Deixar uma skill de revisão **aplicar** mudanças sozinha fora do escopo da tarefa.

## 🔗 Análises da categoria

- [[skills-de-qualidade-de-codigo]]: comparação da pilha de skills de qualidade do reel.
- [[pstack-verificacao]]: o par de skills de verificação, em detalhe.
- [[qualidade-automatizada]]: lint, código morto, testes no CI.
- Voltar ao [[catalogo-do-radar]] · [[como-usar-o-radar]]
