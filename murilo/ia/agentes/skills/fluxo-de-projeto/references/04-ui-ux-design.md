---
documento: ui-ux-design
projeto: "{{nome do projeto}}"
status: rascunho        # rascunho → em-revisao → aprovado
versao: 0.1
aprovado_por:
aprovado_em:
atualizado: AAAA-MM-DD
---

# 04 · UI/UX Design — {{nome do projeto}}

> [!NOTE]
> **Sobre este documento — leia antes de preencher ou revisar**
>
> **O que é:** define como o app **parece e responde**: tokens visuais (cor, tipografia, espaçamento), componentes, layout de cada tela, padrões de interação, acessibilidade e texto de interface.
>
> **Para que serve:** sem ele a IA gera interface genérica ("AI slop") e inconsistente — cada tela com espaçamento, cor e botão diferentes, porque cada sessão decide do zero. Este documento é a regra que o agente segue toda vez que gera front-end.
>
> **Vem de:** [Fluxo do app](03-fluxo-do-app.md) (lista de telas e estados), [TRD](02-trd.md) (biblioteca de componentes) e, se existir, a identidade visual da marca. · **Alimenta:** Plano e toda a implementação de front-end.
>
> **Não entra aqui:** regra de negócio (PRD), navegação entre telas (Fluxo), dado e permissão (Backend).

> [!IMPORTANT]
> **Revisão humana — confira antes de aprovar**
>
> - [ ] Os **tokens** vêm de uma fonte existente (brand guidelines, design system) — ou, se foram criados agora, eu escolhi conscientemente?
> - [ ] **Contraste** verificado numa ferramenta (mínimo 4.5:1 para texto normal). Não confie na palavra da IA.
> - [ ] **Toda TELA-NN** do Fluxo tem especificação aqui.
> - [ ] Cada componente tem os **estados**: normal, hover, foco, desabilitado, carregando, erro, vazio.
> - [ ] A tela principal funciona em **celular (360px)**.
> - [ ] **Mensagens de erro** dizem o que aconteceu e o que fazer — não só "Erro".
> - [ ] Tenho **ao menos um esboço/wireframe/print** aprovado das telas-chave. Texto sozinho não substitui ver.
> - [ ] Passou pelas **heurísticas de Nielsen** (skill `heuristicas-nielsen`).
>
> **Sinais de alerta:** gradiente roxo genérico, card dentro de card, emoji no lugar de ícone, fonte padrão sem decisão, "moderno e clean" como único princípio.

---

## 1. Princípios de design

_Três a cinco princípios específicos deste produto, que ajudam a desempatar decisões. Ex.: "densidade de informação acima de respiro — o usuário é operador que usa o dia todo"._

1.

## 2. Tokens

> Se o projeto já tem design system, **linke a fonte** em vez de copiar valores — cópia desatualiza.

**Cores**

| Token | Valor | Uso | Contraste sobre fundo |
| :--- | :--- | :--- | :--- |
| `--cor-primaria` | | Ação principal | |
| `--cor-fundo` | | | |
| `--cor-texto` | | | |
| `--cor-erro` | | | |

**Tipografia**

| Token | Fonte | Tamanho / altura de linha | Peso | Uso |
| :--- | :--- | :--- | :--- | :--- |
| | | | | |

**Espaçamento, raio e sombra:** _escala (ex.: 4, 8, 12, 16, 24, 32)._

## 3. Componentes base

| Componente | Origem (shadcn, custom…) | Variantes | Estados cobertos |
| :--- | :--- | :--- | :--- |
| Botão | | | |
| Campo de formulário | | | |

## 4. Layout

- **Breakpoints:**
- **Grid / largura máxima:**
- **Navegação principal:** _barra lateral, topo, inferior (mobile)._

## 5. Especificação por tela

### TELA-01 — {{nome}}

- **Objetivo da tela:** _a única coisa que o usuário precisa conseguir aqui._
- **Hierarquia:** _o que chama atenção primeiro, segundo, terceiro._
- **Componentes:**
- **Estados:** vazio · carregando · erro · sucesso
- **Esboço:** _link para Figma / imagem / wireframe._

## 6. Padrões de interação

| Situação | Padrão |
| :--- | :--- |
| Feedback de ação (salvou, enviou) | |
| Ação destrutiva (apagar) | |
| Validação de formulário | _ao sair do campo ou ao enviar?_ |
| Carregamento | _skeleton, spinner, otimista?_ |
| Movimento / animação | |

## 7. Acessibilidade

- Navegação completa por teclado, foco visível.
- Rótulo em todo campo e botão de ícone.
- Não depender só de cor para passar informação.

## 8. Texto de interface (microcopy)

- **Tom:** _link para o tom de voz, se existir._
- **Glossário:** _o mesmo conceito tem sempre o mesmo nome em todas as telas._

## 9. Perguntas em aberto

- [ ]

## 10. Registro de mudanças

| Versão | Data | Mudança | Motivo |
| :--- | :--- | :--- | :--- |
| 0.1 | | Primeira versão | |
