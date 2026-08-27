---
name: spec-compliance
description: >
  Audita a conformidade entre uma especificação técnica (SPEC.md, PRD, requisitos)
  e o código real implementado em ./src. Gera uma matriz de alinhamento com evidências
  e citações de linhas sem alterar o código. Usar ao validar entregas de escopo ou
  auditar aderência a requisitos.
---

# Spec Compliance — Auditoria de Conformidade Código vs Requisitos

Este skill define as diretrizes para auditar se o código implementado atende fielmente aos requisitos declarados em uma especificação (`SPEC.md` ou documentação de arquitetura), eliminando o desvio de escopo (*scope drift*).

## 📋 Quando Disparar

* Quando o usuário pedir para verificar, validar ou auditar se o código atende a um `SPEC.md`, PRD ou conjunto de requisitos de cliente/produto.
* Comandos como `"verifique conformidade com a spec"`, `"audite o SPEC.md contra ./src"`, `"/spec-to-code-compliance:spec-compliance"`.

---

## 🧠 1. Regra de Execução em Modo Somente Leitura

1. **Zero Alteração de Código**: O agente atua estritamente em modo de auditoria. Ele **NÃO** deve modificar arquivos de código durante a análise.
2. **Evidência Obrigatória**: Toda afirmação de que um requisito está "atendido" ou "não atendido" deve ser acompanhada de citação exata de arquivo e número de linha (`src/path/arquivo.ts:L45-L60`).
3. **Mapeamento de Pontos Cegos**: Requisitos declarados na documentação que não tiverem código correspondente em `./src` devem ser sinalizados como `NÃO ATENDIDO (GAP)`.

---

## 🛠️ 2. Processo de Análise em 3 Etapas

1. **Extração da Especificação (Spec-IR)**: Identifica a lista numerada de requisitos funcionais, não-funcionais e regras de negócio no documento fonte (`SPEC.md`).
2. **Mapeamento da Implementação (Code-IR)**: Localiza as funções, componentes, endpoints e tabelas responsáveis por cada requisito.
3. **Geração da Matriz de Alinhamento**: Emite o relatório formal em `spec-compliance/REPORT.md`.

---

## 📋 Formato de Saída Obrigatório (`REPORT.md`)

```markdown
# Relatório de Conformidade de Especificação (Spec Compliance)

- **Data da Auditoria**: AAAA-MM-DD
- **Documento de Referência**: SPEC.md
- **Escopo Analisado**: ./src
- **Taxa de Conformidade Global**: [XX%]

---

## 📊 Matriz de Rastreabilidade de Requisitos

| # | Requisito da Spec | Status | Evidência no Código | Confiança |
| :-: | :--- | :---: | :--- | :---: |
| **REQ-01** | [Descrição do requisito] | ✅ Atendido | `src/services/auth.ts:L34-L52` | Alta |
| **REQ-02** | [Descrição do requisito] | ❌ Ausente | Não encontrado em `./src` | N/A |
| **REQ-03** | [Descrição do requisito] | ⚠️ Parcial | `src/api/webhook.ts:L12` (falta retry) | Média |

---

## 🔍 Detalhamento das Não-Conformidades (Gaps)

### 1. [REQ-XX: Título do Requisito]
* **O que a Spec exige**: [Texto da especificação]
* **O que o código faz hoje**: [Comportamento atual]
* **Ação recomendada para correção**: [Sugestão técnica pontual]

---

## ✅ Conclusão & Próximo Passo
[Resumo executivo do que falta implementar para fechar 100% do escopo.]
```
