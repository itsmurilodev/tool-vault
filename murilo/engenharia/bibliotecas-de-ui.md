---
titulo: Ecossistema de UI copy-paste — componentes, ícones e movimento
resumo: "shadcn como núcleo, catálogos (Cult UI, Skiper UI, 21st.dev, coss ui), ícones Phosphor, Animista e princípios de movimento."
tipo: referencia
dominio: murilo
tags: [engenharia/frontend, ui, animacao, icones]
status: ativo
atualizado: 2026-08-10
---

# Ecossistema de UI copy-paste — componentes, ícones e movimento

## 📌 Resumo

Uma geração de bibliotecas trocou o modelo "instala pacote e importa" pelo **copy-paste**: o componente é colado no seu projeto e passa a ser seu código. Quase tudo que aparece em lista de "ferramentas de front-end" hoje orbita o mesmo núcleo — **shadcn/ui + Tailwind CSS + Radix + React**.

A vantagem do copy-paste é propriedade: sem dependência de versão, você edita à vontade. A desvantagem é a mesma coisa vista de outro ângulo: **não há atualização automática** — correção de bug ou de acessibilidade upstream não chega sozinha.

> 💡 Entender que existe **um núcleo e vários satélites** evita o erro de tratar cada nome novo da lista como uma decisão independente. Na prática, a decisão é uma só: adotar o padrão shadcn. O resto é catálogo.

## 🧠 1. O núcleo — shadcn/ui

shadcn/ui não é biblioteca de componentes no sentido tradicional: é uma **coleção de componentes que você copia para o projeto**, construída sobre primitivos acessíveis do Radix e estilizada com Tailwind. Não existe pacote `shadcn-ui` no `package.json` com os componentes — a CLI escreve os arquivos dentro de `components/ui/` e a partir dali o código é seu.

É por isso que ele virou padrão de fato: define um formato de componente que qualquer catálogo de terceiro consegue produzir. Cult UI, Skiper UI e 21st.dev existem *porque* esse formato existe.

Consequência prática: **a escolha real é adotar shadcn ou não.** Depois disso, escolher entre catálogos é escolha de conteúdo, não de arquitetura — e trocar de catálogo não gera migração.

## 🧠 2. Catálogos de componente

| Catálogo | Modelo | Situação |
| -------- | ------ | --------- |
| **Cult UI** | MIT, aberta, com tier pago | 75+ componentes grátis (cards com hover, grids animados, motion text, blocos de landing). O tier Cult Pro adiciona 100+ padrões de agente de IA SDK |
| **Skiper UI** | Freemium, pagamento único | ~24 grátis e ~54 premium. Compra única com atualização vitalícia, sem assinatura. Foco em animação incomum |
| **21st.dev** | Registro/marketplace | 12.000+ componentes React em shadcn/Tailwind/Radix, com componentes da comunidade e autoria de terceiros. Tem tier Pro. Ver também o item de MCP abaixo |
| **Origin UI** | MIT, gratuita | 200+ componentes. **Mudou de nome e de base** — ver abaixo |

**21st.dev merece cuidado extra na revisão.** É um registro aberto onde terceiros publicam: a média de qualidade e de acessibilidade varia por autor, diferente de uma biblioteca com curadoria única. Volume grande não é sinônimo de padrão consistente — trate cada componente como código de origem desconhecida entrando no seu projeto.

### Origin UI virou coss ui, e isso importa

Origin UI (de Pasquale Vitiello e Davide Pacilio) foi adquirida pela **Cal.com** e passou a se chamar **coss ui**. A mudança não é só de marca: coss ui é construída sobre **Base UI** em vez de Radix/shadcn, e os componentes viraram "particles" — padrões de nível mais alto compostos dos primitivos do Base UI.

Segue livre e aberta, mas **a base técnica mudou**:

- Conteúdo que fala de "Origin UI" pode estar descrevendo a versão antiga, sobre Radix.
- Se o projeto já é shadcn/Radix, misturar com Base UI adiciona um segundo sistema de primitivos.
- Biblioteca em migração de arquitetura é risco a mais em projeto de cliente. Para projeto próprio, é aceitável.

*(A entrada "OriginKit" que aparece em listas virais quase certamente é Origin UI com o nome errado.)*

## 🧠 3. Ícones — Phosphor

**Phosphor Icons** é uma família de ~9.000 ícones sob licença **MIT** — livre para uso pessoal, comercial e corporativo. Pacote React com TypeScript, ícones *tree-shakable*, e props de `size`, `color`, `weight` e `mirrored`. Tem plugin oficial de Figma.

O diferencial real são os **6 pesos** (Thin, Light, Regular, Bold, Fill, Duotone) acessíveis pela mesma prop, sem trocar o import. Isso resolve um problema concreto de consistência: quando o ícone precisa mudar de peso por estado (item selecionado vira `fill`, inativo fica `regular`), não é preciso importar dois pacotes nem improvisar.

Critério de escolha de família de ícones, que vale para qualquer uma:

1. **Uma família por projeto.** Misturar Lucide com Phosphor com Heroicons é a forma mais rápida de a interface parecer remendada — traços e grades diferentes brigam entre si.
2. **Licença permissiva** (MIT) se houver chance de virar projeto de cliente.
3. **Cobertura do seu domínio.** Vale checar se os ícones específicos do que você constrói existem, antes de adotar.
4. **Ponte com o design.** Plugin de Figma importa: sem ele, designer e dev acabam usando ícones diferentes.

Ícone tem uma armadilha de usabilidade: **ícone sozinho raramente comunica.** Salvo um punhado de convenções universais (lupa, lixeira, engrenagem), ícone sem rótulo obriga o usuário a adivinhar — o que contraria diretamente a heurística de reconhecimento em vez de memorização.

## 🧠 4. Movimento

### Motion principles não é biblioteca

"Motion principles" e "skeleton loading" são **padrões de design de interface**, não pacote a instalar: como a interface se comporta durante loading, transição e mudança de estado.

Isso conecta direto com a primeira heurística de Nielsen — **visibilidade do status do sistema**. Skeleton loading resolve exatamente o problema de "a tela parece travada enquanto os dados não chegam". A escolha entre spinner, skeleton e estado otimista é decisão de usabilidade, não de estética.

Regras de bolso:
- Movimento deve **explicar** uma mudança de estado (de onde veio, para onde foi), nunca decorar.
- Transição de interface curta (~150–300 ms). Acima disso, vira espera.
- Respeite `prefers-reduced-motion`. Animação que ignora isso é barreira de acessibilidade, não polish.
- Skeleton deve ter o formato do conteúdo que vai chegar. Skeleton genérico só troca uma incerteza por outra.

### Animista — gerador de CSS, não dependência

**Animista** é um gerador de animação CSS: você navega por um catálogo de efeitos prontos, ajusta duração, delay, easing, direção e iteração vendo o resultado ao vivo, e copia o CSS com os `@keyframes` já escritos. Livre para uso pessoal e comercial.

O ponto que muda como usar: **não é biblioteca, é ferramenta de autoria.** Nada é instalado, nada entra no `package.json`, não há versão para atualizar. O output é CSS puro que passa a ser seu — mesma lógica de propriedade do copy-paste, com o mesmo custo (a manutenção é sua).

Onde ele se encaixa bem:

- Efeito pontual em CSS puro, sem justificar trazer Framer Motion para o bundle.
- Aprender a sintaxe de `@keyframes` vendo o efeito antes do código.
- Projeto sem React, onde as bibliotecas de motion do ecossistema não se aplicam.

Onde não se encaixa: animação ligada a estado de componente, orquestração de entrada/saída, gesto ou layout animado — aí o trabalho é de uma biblioteca de motion, e CSS avulso vira remendo.

Cuidado prático: o catálogo é cheio de efeito chamativo (bounce, flip, jello). O portão continua sendo *o movimento explica uma mudança de estado?* — se a resposta é "não, mas fica legal", ele não entra.

## ✅ Critério de escolha

1. **Verifique a licença antes de usar em projeto de cliente.** MIT é seguro. Tier premium de pagamento único cria dependência que alguém herda, e "vitalício" vale enquanto a empresa existir.
2. **Prefira o que já casa com o seu núcleo.** Se o projeto é shadcn + Radix, componente Base UI custa integração.
3. **Copiar componente é assumir manutenção dele** — inclusive a acessibilidade. Componente animado bonito com foco quebrado no teclado é regressão de usabilidade, não polish.
4. **Animação não substitui hierarquia visual.** Se a tela só fica boa em movimento, o problema é de layout.
5. **Uma família de ícones, um núcleo de componentes.** Consistência vale mais que variedade.

| Estágio | O que vale |
| ------- | ---------- |
| MVP / validação | shadcn + Phosphor + catálogo gratuito (Cult UI MIT). Zero gasto, decisão reversível |
| Produto com identidade visual própria | Investir em movimento e skeleton nos fluxos de espera — é onde a percepção de qualidade se decide |
| Projeto de cliente | Só biblioteca com licença clara e permissiva. Componente premium é decisão do cliente, não sua |

## 🔗 Ver também

- [[adocao-de-ferramenta]] — o portão de estágio.
- [[geracao-de-ui-por-ia]] — quando é a IA que escreve o componente, incluindo o MCP do 21st.dev e o do shadcn.
- Skill [heuristicas-nielsen](../ia/agentes/claude/skills/heuristicas-nielsen/SKILL.md) — visibilidade de status, reconhecimento vs memorização e consistência aplicadas a componente.

## 📚 Fontes

- [shadcn/ui](https://ui.shadcn.com/) · [Cult UI](https://www.cult-ui.com/) · [Skiper UI](https://skiper-ui.com/) · [21st.dev](https://21st.dev/)
- [coss ui (ex-Origin UI)](https://coss.com/ui/docs/roadmap) · [anúncio da transição](https://x.com/coss_com/status/1976668768312123777)
- [Phosphor Icons — React](https://github.com/phosphor-icons/react) · [plugin de Figma](https://www.figma.com/community/plugin/898620911119764089/phosphor-icons)
- [Animista](https://animista.net/)
