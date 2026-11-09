---
titulo: "Skills de qualidade de código — Ponytail, pstack e thermo-nuclear review empilhados"
resumo: "Episódio 4 da série do reel: rodar Ponytail + no-comments + typescript-best-practices + unslop + thermo-nuclear em todo PR. As peças são boas, mas se sobrepõem (o próprio autor admite) e duas se contradizem: Ponytail subtrai, thermo-nuclear reestrutura. Para você: uma regra na escrita (clean-code), uma revisão no PR e regra mecânica no lint/CI."
tipo: conceito
dominio: radar
tags: [murilo/ia, agentes, skills, clean-code, qualidade-de-codigo, revisao]
status: ativo
atualizado: 2026-11-09
---

# Skills de qualidade de código — Ponytail, pstack e thermo-nuclear review empilhados

## 📌 Resumo

No episódio 4, o autor responde a "como manter a qualidade com tanto código de IA sendo mesclado?" com **skills**. Em todo PR ele dispara um comando único que encadeia:

- **[[ponytail]]**: minimalismo e YAGNI. Já está no vault.
- Três skills do pstack ([[pstack-verificacao]]): **`no-comments`**, **`typescript-best-practices`** e **`unslop`**.
- **`thermo-nuclear-code-quality-review`**: revisão de manutenibilidade extremamente rígida, da Cursor (`cursor/plugins/cursor-team-kit`, MIT).

O próprio autor diz que a thermo-nuclear "faz praticamente a mesma coisa" que as outras. Esse é o ponto da análise: **empilhar cinco camadas que se sobrepõem custa tokens, aumenta o diff e cria instruções contraditórias**. Você já cobre a maior parte disso com a skill `clean-code` e com o `/simplify` e o `/code-review` do Claude Code.

> 💡 **Analogia:** cinco revisores de texto lendo o mesmo parágrafo, um mandando cortar e outro mandando reescrever o capítulo. O texto não melhora cinco vezes: ele fica rodando em círculo e cresce.

## 🧠 1. O que cada uma faz de verdade

| Skill | O que faz (lido na fonte) | Você já tem algo igual? |
| --- | --- | --- |
| **Ponytail** | Escada de decisão "lazy senior": nativo antes de lib, menos código, sem abstração especulativa | **Sim:** `clean-code` tem "sem abstração especulativa" e "sem overengineering" |
| **no-comments** (pstack) | Sobe um subagente *Comment Sicko* que caça comentários, mantém os que descrevem regra externa e oferece transformar restrição em tipo, teste ou lint. **Depende** de `references/comment-sicko.md` e de outras skills do pstack (`/how`, `/why`, `/architect`). | **Parcial:** `clean-code` diz "comentário só quando o código não consegue falar sozinho" |
| **typescript-best-practices** (pstack) | Tabela de regras de tipo: unions discriminadas, *branded types*, `unknown` em vez de `any`, sem `as`, `satisfies`, validação na borda com schema (`z.infer`), exaustividade com `never`. Depende de `principle-type-system-discipline`. | **Não.** É a peça mais nova para você. |
| **unslop** (pstack) | Remove "cara de IA" de **texto em prosa** | **Não é de código.** Serve para descrição de PR, docs e notas do vault, não para o código em si. |
| **thermo-nuclear-code-quality-review** (Cursor) | Revisão rígida da branch: "seja **ambicioso**", procure movimentos de *code judo*, **reestruture parte do codebase se houver caminho claro**, não deixe arquivo passar de 1.000 linhas, nada de `if` solto em fluxo alheio, nada de wrapper fino, logic na camada canônica | **Parcial:** `/simplify` e `/code-review` do Claude Code |

## ⚠️ 2. Onde a pilha quebra

### 2.1 Ponytail e thermo-nuclear puxam para lados opostos

O Ponytail manda **subtrair**: não criar camada, preferir o nativo. A thermo-nuclear manda **reestruturar com ambição**: extrair helper, subcomponente, *state machine*, *policy object*, e mexer em "parte do codebase". Em muitos casos as duas concordam (apagar complexidade), mas no limite uma desfaz o que a outra sugeriu, e o diff cresce a cada passada.

### 2.2 A thermo-nuclear conflita com as suas regras

Suas diretrizes (item 9) e a `clean-code` dizem: **menor alteração segura**, problema fora do escopo se **relata, não se corrige**, e "não tocar em arquivo fora do escopo sem avisar". A thermo-nuclear diz *"if there is a clear path … that involves restructuring some of the codebase, go for it"*. Em modo de aplicação automática, ela **viola o seu padrão**. Em modo de **relatório**, com você decidindo o que entra, ela é útil.

### 2.3 Rodar tudo em todo PR contradiz o resto da série

No episódio 2 ([[captura-de-erros-para-agentes]]), o auto-merge só vale para correção **pequena**. Uma pilha de limpeza que reestrutura e reescreve aumenta justamente o diff que deveria ficar pequeno. Bug fix de 3 linhas não precisa de auditoria thermo-nuclear.

### 2.4 Parte disso é regra mecânica, não julgamento

"Arquivo acima de 1.000 linhas", "sem `any`", "sem `as`", "sem `console.log`", "código morto" e "import não usado" são verificáveis por **lint e CI**: Biome, Knip e `tsc` estrito, ver [[qualidade-automatizada]]. Uma ferramenta determinística não alucina, é barata e roda em todo PR. Deixe para o LLM só o que o lint não vê: desenho, camada certa e abstração ruim.

### 2.5 Narrativa

- **"Potato NX", "engenheiro da SpaceX":** é a *poteto* (Lauren Tan). O README do pstack diz que ela trabalha na Cursor. A página do Grok Bot na xAI é assinada por "SpaceX Super Intelligence LLC". A relação entre as empresas não foi verificada, e não muda nada na avaliação.
- **"Alimenta 90% dos meus PRs":** é afirmação pessoal, sem como verificar.
- **"Cada uma é uma ferramenta gigantesca de limpeza":** a eficácia não foi medida por ninguém. O Ponytail cita uma redução de 54% em linhas de código, um número do próprio autor dele.

## ✅ 3. A versão que cabe: três camadas, sem sobreposição

| Momento | O quê | Ferramenta |
| --- | --- | --- |
| **Ao escrever** (sempre) | Minimalismo, nomes, sem abstração especulativa, comentário só com motivo | Skill `ponytail` oficial (quanto escrever) + `clean-code` focada em nomenclatura (como se lê). Decisão revista em 2026-11-09: a escada embutida virou cópia congelada; a skill oficial é mantida e tem mais (escopo, teste mínimo, níveis). |
| **No CI** (todo PR) | Regras mecânicas: tamanho de arquivo, `any`/`as`, código morto, imports | Biome + Knip + `tsc --strict` + um script para "arquivo > 1.000 linhas" |
| **Na revisão** (PR de feature ou refactor, não bug fix pequeno) | Desenho, camada, abstração, *code judo* | `/simplify` ou a thermo-nuclear **só em modo relatório**: você aceita achado por achado |

**Peças para avaliar separadamente:**

- **`typescript-best-practices`**: é a que mais acrescenta. Teste num projeto TS (Encaixe), copiando junto a `principle-type-system-discipline`. Fique atento a *branded types* e tipos construtivos em MVP, que podem virar exagero. Use a regra "Simplest total type" da própria skill como freio.
- **`unslop`**: útil para descrição de PR, docs e as notas deste vault. Não tem nada a ver com qualidade de código.
- **`no-comments`**: só funciona com o resto do pstack instalado. A regra da `clean-code` já cobre o essencial. Não vale o pacote.
- **Pipeline completo do autor**: **não adotar.**

## 🔗 Ver também

- [[ponytail]] · [[pstack-verificacao]] · [[qualidade-automatizada]] · [[clean-code]]
- [[correcao-de-bug-com-agentes]] · [[captura-de-erros-para-agentes]]
- Skill [clean-code](../../agentes/skills/clean-code/SKILL.md)

## 📚 Fontes

- Transcrição do reel (episódio 4 da série) colada pelo usuário em 2026-11-09 (autor não identificado).
- [cursor/plugins — thermo-nuclear-code-quality-review (MIT, Cursor)](https://github.com/cursor/plugins/tree/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review), lido em 2026-11-09.
- [backnotprop/pstack — no-comments, typescript-best-practices, unslop](https://github.com/backnotprop/pstack/tree/main/skills), lidos em 2026-11-09.
- [ponytail.dev](https://ponytail.dev) · [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
