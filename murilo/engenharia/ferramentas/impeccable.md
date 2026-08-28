---
titulo: "Impeccable — Linter Determinístico e Design System para UI por IA"
resumo: "Ferramenta de 59 regras determinísticas e comandos de design para eliminar padrões genéricos ('AI slop') e polir interfaces no front-end."
tipo: referencia
dominio: murilo
tags: [murilo/engenharia, ferramentas, frontend, design-system, ui, ia]
status: ativo
atualizado: 2026-08-27
---

# Impeccable — Linter Determinístico e Design System para UI por IA

## 📌 Resumo

O **Impeccable** ([impeccable.style](https://impeccable.style)), criado por Paul Bakaus, é uma linguagem de design e conjunto de ferramentas determinísticas que guiam agentes de IA a gerarem código front-end de padrão profissional, eliminando o visual genérico de IA ("AI slop").

No [[adocao-de-ferramenta]], o Impeccable é classificado como **Adoção de Front-end (P1)**: execução local com custo financeiro zero, sem dependência de chaves de API para detecção, e forte sinergia com o design system da Async.

---

## 🧠 1. As 59 Regras Determinísticas

Diferente de geradores que alucinam estilos a cada prompt, o Impeccable opera com um catálogo determinístico de 59 regras divididas em dois grupos:

1. **32 Regras Anti-Slop**: Identificam vícios visuais característicos de modelos generativos:
   * Gradientes roxo-para-azul saturados e clichês.
   * Aninhamento excessivo e desnecessário de containers e cards.
   * Botões com sombras difusas e cantos arredondados descalibrados.
   * Micro-animações exageradas e sem propósito funcional.
2. **27 Regras de Qualidade**: Forçam boas práticas clássicas de design de interface:
   * Contraste acessível (WCAG AA/AAA).
   * Hierarquia tipográfica e ritmo vertical consistente.
   * Estados interativos completos (hover, active, focus-visible, disabled, loading).
   * Semântica HTML correta e espaçamentos padronizados.

---

## ⚡ 2. Arquitetura Zero-Model (Sem Custo de Tokens)

* **Motor Local**: A detecção de anti-padrões roda via CLI local em TypeScript/Node.js sem necessidade de chamar modelos de linguagem ou gastar créditos de API.
* **Comandos para Agentes**: Fornece 23 comandos especializados (como `/impeccable init`, `/impeccable audit`, `/impeccable polish`) que orientam o agente a refatorar o código existente com precisão cirúrgica.

---

## 🛠️ 3. Como Usar

### 1. Instalação no Projeto
```bash
npx impeccable install
```

### 2. Auditoria e Detecção Local
```bash
# Faz a varredura dos componentes buscando violações de regras
npx impeccable detect src/components/
```

### 3. Comandos do Agente & Arquivos de Configuração
* `/impeccable init`: Lê a configuração do projeto e gera os arquivos `PRODUCT.md` e `DESIGN.md` (armazenando preferências de cores, tipografia e componentes para guiar comandos futuros).
* `/impeccable audit`: Gera relatório com diagnósticos das violações encontradas.
* `/impeccable critique`: Faz uma análise crítica profunda da interface contra as 59 regras determinísticas.
* `/impeccable polish`: Solicita ao agente a refatoração focada nas seções com problemas de contraste, alinhamento e hierarquia.
* `/impeccable distill`: Sintetiza estilos repetidos em classes e tokens reutilizáveis.


---

## 🎯 4. Impacto nos Produtos da Async Studio

* **[[site-institucional]]**: Mantém a elegância e sofisticação visual alinhada com os [[tokens-css]] da marca, eliminando retrabalho manual de CSS.
* **[[app-encaixe]]**: Assegura legibilidade e usabilidade na interface de agendamento mobile, onde contraste de datas e clareza de botões impactam diretamente a conversão.
* **[[app-asynchub]]**: Padroniza tabelas, painéis e formulários do CRM com densidade visual adequada.

---

## ⚠️ Riscos & Quando NÃO Usar

* **Não Carregar em Projetos Backend/Infra**: Não injete as regras do Impeccable em contextos de APIs puras, scripts de banco ou pipelines para não desperdiçar janela de contexto do agente.
* **Não Substitui Heurísticas de Negócio**: O Impeccable cuida da estética e das regras de layout; o fluxo de navegação e a experiência do usuário ainda devem respeitar as [heuristicas-nielsen](../../ia/agentes/skills/heuristicas-nielsen/SKILL.md).

---

## 🔗 Ver também

* [[tokens-css]] — tokens visuais oficiais da Async Studio.
* [heuristicas-nielsen](../../ia/agentes/skills/heuristicas-nielsen/SKILL.md) — heurísticas de usabilidade para front-end.
* [[bibliotecas-de-ui]] — diretrizes sobre bibliotecas de componentes e Tailwind.
* [[adocao-de-ferramenta]] — portão de adoção técnica.

