---
titulo: "pstack — create-verification-skill e maintain-verification-skill"
resumo: "Par de skills da Lauren Tan (Cursor) que gera e mantém uma skill de verificação por projeto: o agente sobe o app, usa como usuário e guarda evidência. Adota agora, copiando só as duas skills, em um projeto."
tipo: referencia
dominio: murilo
tags: [murilo/ia, agentes, skills, verificacao, qualidade-de-codigo]
status: ativo
atualizado: 2026-11-09
---

# pstack — create-verification-skill e maintain-verification-skill

## 📌 Resumo

**pstack** é a coleção de skills de engenharia da Lauren Tan (*poteto*). Ela é do time do React Compiler e engenheira na Cursor. A fonte oficial é [`cursor/plugins/pstack`](https://github.com/cursor/plugins/tree/main/pstack) (MIT). O mirror que roda fora da Cursor é [`backnotprop/pstack`](https://github.com/backnotprop/pstack). Das quase 50 skills, as duas que viralizaram resolvem uma coisa só: **dar ao agente um jeito roteirizado de provar que o app funciona**, em vez de ele declarar "pronto" depois de compilar.

- `create-verification-skill` roda **uma vez**. Gera no projeto uma skill `verify-<app>/` que ensina qualquer agente a subir o app, checar se a instância está saudável, usar as features como um usuário usaria, guardar evidência e limpar o que subiu.
- `maintain-verification-skill` roda **periodicamente**. Confere a skill gerada contra o código atual e contra o app rodando, e corrige a documentação que ficou desatualizada sem nunca mexer no código do produto.

No [[adocao-de-ferramenta]]: **adota agora**, copiando só as duas skills, em um projeto. Não instale o pstack inteiro.

> 💡 **Analogia:** o roteiro de vistoria de um carro. O mecânico não diz "acho que o freio está bom". Ele segue o roteiro (liga, testa o freio, anota a distância de parada) e entrega a ficha assinada. A `create` escreve o roteiro. A `maintain` revisa o roteiro sempre que o carro muda de modelo.

## 🧠 1. O que a `create-verification-skill` faz

Fonte: [SKILL.md](https://github.com/backnotprop/pstack/blob/main/skills/create-verification-skill/SKILL.md), lido em 2026-11-09.

1. **Entrevista o repositório, não você.** Descobre pelo código qual é a superfície do app (web, CLI, API, mobile), como ele sobe, como um agente consegue dirigi-lo (primeiro Playwright e scripts que já existem, depois CDP, tmux/PTY ou HTTP), que evidência dá para capturar e se duas instâncias rodam ao mesmo tempo. Só pergunta a você o que não dá para observar.
2. **Gera `<skills>/verify-<app>/SKILL.md`** com seções obrigatórias: **Launch** (pronto quer dizer *usável*, não só "o processo respondeu"), **Doctor** (checagem só de leitura: "vale a pena dirigir esta instância?"), **Drive** (seletores reais do repo, de preferência ARIA e data-attributes), **Evidence**, **Cleanup** (mata só o que ele subiu e preserva a evidência) e **Helpers**.
3. **Semeia um feature map**, com um arquivo por feature (comece pelas 3 a 5 principais) e quatro seções fixas: sub-features, como o usuário chega, como dirigir, armadilhas. Tem uma regra forte: se a jornada falha, **não se enfraquece a jornada para ela passar**.
4. **Executa a skill gerada de ponta a ponta antes de entregar.** "Skill que nunca rodou é rascunho, não entrega."

## 🧠 2. O que a `maintain-verification-skill` faz

Fonte: [SKILL.md](https://github.com/backnotprop/pstack/blob/main/skills/maintain-verification-skill/SKILL.md).

- **Onda de leitura:** um subagente só de leitura por feature, em paralelo, explica no código como a feature funciona e aponta onde a documentação divergiu.
- **Passada ao vivo obrigatória:** um único coordenador dirige todas as features no app rodando, com *doctor* antes da primeira ação e depois de qualquer falha.
- **Triagem em três baldes:**

| O que encontrou | Classificação | Ação |
| --- | --- | --- |
| A descrição na skill está errada | Doc drift | Corrige o feature map |
| O app funciona, mas o roteiro não consegue dirigi-lo | Harness gap | Corrige o script e roda de novo ao vivo |
| O app está quebrado | Product gap | **Reporta e não esconde** (fica fora do PR) |

- **Saída:** `clean` (nada a fazer), `changed` (no máximo um PR com correções provadas) ou `blocked` (diz exatamente o que travou).

Ponto técnico relevante: as duas skills têm `disable-model-invocation: true`. Ou seja, só rodam quando você chama. Não disparam sozinhas e não ficam ocupando contexto, que é a preocupação de [[find-skills]].

## 🧠 3. Narrativa vs fato

| O que se diz por aí | Avaliação |
| --- | --- |
| "Verificação é a parte mais importante de um loop de agente confiável" (autora) | **Procede no princípio.** É o mesmo item 10 das suas diretrizes: não declarar concluído o que não foi verificado. Mas quem diz é a autora promovendo a própria stack. |
| "Rode a manutenção pelo menos uma vez por dia" (guias de terceiros) | **Exagero para o seu porte.** A própria skill diz para sugerir cadência só se o usuário pedir. Cada passada sobe um subagente por feature mais o app inteiro, e isso custa tokens e tempo. Rode quando features mudarem ou antes de release. |
| "Funciona para qualquer linguagem e plataforma" | **[PROVÁVEL]** O método é genérico, mas a qualidade depende de o app subir local a partir de um banco vazio, com seed. Projeto sem seed vai travar no primeiro passo, o que também é um diagnóstico útil. |
| "Instale o pstack" | **Cuidado com o ecossistema.** Há dezenas de forks e ports com o nome pstack, alguns sem relação nenhuma (`no-session/pstack` é fork do gstack). E o `poteto-mode` completo vem configurado para delegar código ao Grok e depende de recursos da Cursor. |

## ✅ 4. Portão de adoção

1. **Dor concreta?** Sim, quando o agente diz "feito" e você descobre no navegador que o fluxo quebrou. Num projeto com UI e fluxos (Encaixe), essa dor é real hoje.
2. **Custo total:** setup é uma execução da `create` (tokens, mais o app subindo local com seed). Manutenção é uma passada da `maintain` quando muda feature. Remover é apagar uma pasta.
3. **Substitui ou soma?** Soma, mas pouco, e completa o que já existe em vez de concorrer:
   - **Playwright e2e** ([[qualidade-automatizada]]): é teste determinístico no CI. A skill de verificação é o roteiro que o agente segue para provar a mudança na hora. Uma não substitui a outra, e a skill pode inclusive reaproveitar specs que já existem.
   - **[[playwright-mcp]] / [[agent-browser]]**: são o volante. A skill de verificação é o roteiro que diz o que dirigir e o que conta como prova.
   - **`spec-compliance`**: confere especificação contra código, de forma estática. A verificação confere o comportamento do app rodando.
   - **Skill `run` do Claude Code:** sobe e dirige o app sob demanda, de forma genérica. O `verify-<app>` é específico do projeto, fica salvo e tem manutenção.
4. **Reversível?** Totalmente. São arquivos Markdown dentro de `.claude/skills/`.

## ✅ 5. Como aplicar

1. ✅ **Feito em 2026-11-09.** Copiadas sem alteração para [create-verification-skill](../../../ia/agentes/skills/create-verification-skill/SKILL.md) e [maintain-verification-skill](../../../ia/agentes/skills/maintain-verification-skill/SKILL.md), fixadas no commit `0b239bb` do mirror. A atribuição MIT e a origem estão no `LICENSE` de cada pasta. Para atualizar, baixe de novo desse caminho em vez de usar `npx skills add backnotprop/pstack`, que lista o pacote inteiro.
2. Num projeto só (sugestão: Encaixe), rode `/create-verification-skill`. Se ele travar por falta de seed ou de variável de ambiente, resolva isso primeiro. Essa já é parte do ganho.
3. Revise o `verify-<app>/` gerado e faça commit no repositório do projeto, não no vault.
4. Rode `/maintain-verification-skill` depois de mudanças em features ou antes de release, não diariamente.
5. Só avalie o resto do pstack (`poteto-mode`, `unslop`, `tdd`, …) depois, em nota separada, skill por skill.

## 🔗 Ver também

- [[correcao-de-bug-com-agentes]]: o processo de bug fix que usa o `verify-<app>` para reproduzir e para provar.
- [[adocao-de-ferramenta]] · [[qualidade-automatizada]] · [[playwright-mcp]] · [[agent-browser]] · [[find-skills]]
- Skill [spec-compliance](../../../ia/agentes/skills/spec-compliance/SKILL.md)

## 📚 Fontes

- [cursor/plugins — pstack (oficial, MIT, Lauren Tan)](https://github.com/cursor/plugins/tree/main/pstack). Skills adicionadas em 2026-07-12 (PR #150), última mudança em 2026-10-12 (PR #573).
- [backnotprop/pstack — mirror para Claude Code, Codex e Pi](https://github.com/backnotprop/pstack)
- [Post da autora recomendando as duas skills (X)](https://x.com/poteto/status/2082874054483255805)
- [The Complete Guide to pstack Pt. 1 (X)](https://x.com/poteto/article/2094457600259842065?lang=en)
- [A deep dive into pstack — Flavio Copes](https://flaviocopes.com/pstack/) (comentário de terceiro)
