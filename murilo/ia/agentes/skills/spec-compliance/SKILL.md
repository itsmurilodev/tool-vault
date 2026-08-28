---
name: spec-compliance
description: >
  Audita formalmente a conformidade entre uma especificação técnica (SPEC.md,
  PRD, requisitos de cliente) e o código real implementado em ./src, seguindo o
  método da Trail of Bits. Gera uma matriz de rastreabilidade com evidências e
  citações de linha sem alterar o código. Usar SEMPRE que for validar entregas
  de escopo, auditar aderência a requisitos ou quando o usuário solicitar
  verificação formal de conformidade.
---

# Spec Compliance — Auditoria Formal de Código vs Requisitos (Trail of Bits)

Esta skill aplica o método de auditoria de conformidade desenvolvido pela **Trail of Bits** ([trailofbits/skills](https://github.com/trailofbits/skills/tree/main/plugins/spec-to-code-compliance)) para comparar sistematicamente se a implementação em `./src` cumpre fielmente os requisitos estipulados em um documento de especificação (`SPEC.md`, PRD ou PDF de arquitetura).

O objetivo é eliminar o **desvio de escopo (*scope drift*)** e garantir que nenhuma regra de negócio crítica tenha sido esquecida pelo agente de IA ou desenvolvedor.

**Idioma:** toda comunicação e relatórios de conformidade são emitidos em português do Brasil.

---

## 🛡️ Regra Fundamental: Modo Estritamente Analítico (Somente Leitura)

* **ZERO Alteração de Código**: Durante a auditoria de conformidade, o agente **NÃO deve modificar nenhum arquivo de código**.
* **Evidência Obrigatória**: Toda conclusão deve ser embasada em citação exata de arquivo e número de linha (`src/servico/auth.ts:L45-L60`).
* **Detecção Imparcial**: Se um requisito não possuir código correspondente, declare explicitamente como `NÃO ATENDIDO (GAP)`. Não presuma nem alucine código existente.

---

## 🔬 O Processo de Auditoria em 3 Etapas (IR)

1. **Spec-IR (Extração de Requisitos)**:
   * Lê o arquivo de especificação (`SPEC.md` ou similar) e extrai cada requisito numerado (`REQ-01`, `REQ-02`), separando regras funcionais, não-funcionais e critérios de segurança.
2. **Code-IR (Mapeamento do Código)**:
   * Vasculha os arquivos em `./src` (rotas, hooks, componentes, esquemas de banco, services) mapeando as funções e trechos que implementam cada comportamento.
3. **Alignment-IR (Matriz de Alinhamento)**:
   * Cruza cada `REQ-NN` com a evidência encontrada e atribui o status:
     * ✅ **Totalmente Atendido**: Implementação completa e aderente à especificação.
     * ⚠️ **Parcialmente Atendido**: Implementado, mas faltam validações, tratamento de erro ou casos de borda.
     * ❌ **Não Atendido (Gap)**: Requisito ausente no código.
     * ❓ **Divergente**: O código implementou algo diferente ou oposto ao exigido pela especificação.

---

## 🛠️ Comandos & Como Executar

### 1. Invocação via Plugin ou Prompt
```text
/spec-to-code-compliance:spec-compliance ./src
```

### 2. Prompt Padrão de Auditoria
```text
Compare o diretório ./src com o documento SPEC.md e verifique a conformidade de todos os requisitos.
Restrições: Não altere o código; registre evidências e buscas realizadas.
Resultado: Gere o relatório completo em spec-compliance/REPORT.md com a matriz de alinhamento e taxa de conformidade.
```

---

## 📋 Formato de Saída Obrigatório (`REPORT.md`)

```markdown
# Relatório de Conformidade de Especificação (Spec Compliance)

- **Data da Auditoria**: AAAA-MM-DD
- **Documento de Referência**: SPEC.md
- **Escopo Analisado**: ./src
- **Taxa de Conformidade**: [XX%] ([N]/[Total] Requisitos Atendidos)

---

## 📊 Matriz de Rastreabilidade de Requisitos

| # | Requisito da Spec | Status | Evidência no Código | Confiança |
| :-: | :--- | :---: | :--- | :---: |
| **REQ-01** | [Descrição concisa do requisito] | ✅ Atendido | `src/services/auth.ts:L34-L52` | Alta |
| **REQ-02** | [Descrição concisa do requisito] | ⚠️ Parcial | `src/api/webhook.ts:L12` (sem retry) | Média |
| **REQ-03** | [Descrição concisa do requisito] | ❌ Não Atendido | Não encontrado em `./src` | N/A |

---

## 🔍 Detalhamento das Não-Conformidades e Gaps

### 1. [REQ-02: Retry de Webhook]
* **Exigência da Spec**: "O webhook deve tentar reenviar até 3 vezes com backoff exponencial."
* **Implementação Atual**: `src/api/webhook.ts:L12` executa apenas um disparo síncrono.
* **Ação Recomendada**: Implementar fila de reprocessamento no worker.

### 2. [REQ-03: Bloqueio de Concorrência]
* **Exigência da Spec**: "Horários bloqueados não podem ser agendados simultaneamente."
* **Implementação Atual**: Nenhuma transação ou lock detectado em `src/services/booking.ts`.
* **Ação Recomendada**: Adicionar constraint de exclusão no PostgreSQL via Supabase.

---

## ✅ Resumo Executivo & Próximos Passos
[Lista priorizada do que precisa ser implementado para atingir 100% de conformidade com a especificação.]
```

---

## 📚 Referência Ampliada

Consulte `references/matriz-de-conformidade-exemplo.md` para ver um exemplo prático completo de auditoria aplicada a um SaaS B2B.
