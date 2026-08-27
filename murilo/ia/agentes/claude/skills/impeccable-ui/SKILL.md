---
name: impeccable-ui
description: >
  Aplica as 59 regras determinísticas e comandos de design do Impeccable para
  eliminar 'AI slop' (gradientes roxo/azul clichês, cards aninhados, contraste
  ruim) e garantir interfaces front-end com alto padrão estético, acessibilidade
  e consistência visual em React, Next.js e Tailwind. Usar ao gerar, editar ou
  auditar componentes de UI e estilos.
---

# Impeccable UI — Linter Determinístico de Design Front-end

Este skill define as diretrizes para gerar e auditar código de interface visual, eliminando o padrão genérico produzido por modelos de linguagem ("AI slop") e garantindo acabamento profissional e acessível.

## 🎨 Quando Disparar

* **Modo Silencioso (Default)**: Ao gerar ou editar componentes React, páginas Next.js, formulários, tabelas e estilização Tailwind/CSS.
* **Modo Refinamento Explícito**: Quando o usuário solicitar comandos como `"/impeccable polish"`, `"/impeccable audit"`, `"refine esta interface"`, `"remova cara de template de IA"`.

---

## 🧠 1. As Regras Determinísticas Anti-Slop

Ao criar ou editar interfaces, aplique rigorosamente:

1. **Paletas Harmoniosas (Adeus Gradientes Clichês)**:
   * Proibido o uso de gradientes roxo-para-azul saturados padrão de IA.
   * Utilize paletas com contraste calibrado, fundos neutros elegantes (tons de cinza/chumbo calibrados) e cores de destaque intencionais alinhadas aos tokens do projeto.
2. **Eliminação de Aninhamento Excessivo de Cards**:
   * Não envolva cada elemento em um `card` com borda e sombra. Use espaços em branco (*whitespace*), tipografia e divisores sutis para criar hierarquia visual.
3. **Contraste & Tipografia Acessível (WCAG AA/AAA)**:
   * Texto secundário deve ter contraste legível. Nunca use cinza claro sobre fundo branco ou cinza escuro sobre preto.
   * Mantenha uma escala tipográfica clara (máximo de 3 tamanhos de fonte por tela para manter o ritmo).
4. **Estados Interativos Completos**:
   * Todo elemento clicável (`<button>`, `<a>`, `<input>`) deve possuir estados explícitos de: `hover`, `focus-visible`, `active`, `disabled` e `loading`.

---

## 🛠️ 2. Comandos Operacionais no Projeto

Quando o Impeccable estiver instalado no projeto (`npx impeccable install`):

* **/impeccable init**: Lê as configurações existentes e gera/atualiza `PRODUCT.md` e `DESIGN.md`.
* **/impeccable audit**: Executa o scanner local (`npx impeccable detect [path]`) e lista violações de regras.
* **/impeccable critique**: Realiza uma avaliação crítica dos componentes antes da entrega.
* **/impeccable polish**: Refatora os trechos identificados corrigindo espaçamentos, contraste e tipografia.
* **/impeccable distill**: Agrupa classes e estilos repetidos em padrões reutilizáveis.

---

## ⚠️ 3. Guardrails de Aplicação

* **Não Carregar em Backend**: Não aplique regras de UI em sessões focadas exclusivamente em bancos de dados, scripts ou infraestrutura para não desperdiçar contexto.
* **Respeitar os Tokens do Projeto**: Sempre priorize tokens de cores já existentes no projeto (como os tokens CSS da Async) sobre valores hexadecimais avulsos.

---

## 📋 Formato de Saída em Auditoria de Interface

```markdown
## 🎨 Relatório de Design & UI (Impeccable)
* **Componente Auditado**: [Nome/Arquivo]
* **Diagnóstico Geral**: [Pontos de melhoria visual e contraste]

### 🔍 Violações Identificadas & Correções
1. **[Espaçamento / Tipografia]**: [O que estava genérico] → [Como foi refinado]
2. **[Acessibilidade / Contraste]**: [Taxa de contraste corrigida para WCAG AA]
3. **[Estados de Interação]**: [Estados adicionados: hover/focus-visible/loading]

### ✅ Checklist Visual Final
- [ ] Zero gradientes clichês ou cards aninhados desnecessários.
- [ ] Contraste legível em todos os textos.
- [ ] Responsividade mobile e desktop preservada.
```
