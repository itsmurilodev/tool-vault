---
titulo: "Spec to Code Compliance — Auditoria Determinística de Requisitos por IA"
resumo: "Plugin da Trail of Bits para verificação formal de conformidade entre especificações (SPEC.md/PRD) e código implementado."
tipo: referencia
dominio: murilo
tags: [murilo/engenharia, ferramentas, seguranca, auditoria, testes, ia]
status: ativo
atualizado: 2026-08-27
---

# Spec to Code Compliance — Auditoria Determinística de Requisitos por IA

## 📌 Resumo

O **Spec to Code Compliance** ([trailofbits/skills](https://github.com/trailofbits/skills/tree/main/plugins/spec-to-code-compliance)), desenvolvido pela conceituada empresa de segurança **Trail of Bits**, é um plugin de auditoria determinística que compara linha a linha se o código implementado (`./src`) atende fielmente aos requisitos declarados em uma especificação técnica (`SPEC.md`, PRD ou PDF de arquitetura).

Diferente do conteúdo viral de influenciadores, esta é uma ferramenta de **AppSec e QA formal**: ela gera evidências e relatórios rastreáveis (`REPORT.md`) sem alterar o código-fonte.

No [[adocao-de-ferramenta]], é classificada como **Prioridade Alta (P1)** para validação de escopo e entregas em projetos da Async Studio.

---

## 🧠 1. Como Funciona a Auditoria

A ferramenta utiliza uma representação intermediária (IR) em 3 etapas para eliminar alucinações:

1. **Spec-IR**: Extrai os requisitos e regras de negócio da documentação (`SPEC.md`).
2. **Code-IR**: Mapeia as funções, rotas, tipos e comportamentos reais no código (`./src`).
3. **Alignment-IR**: Cruza as duas camadas gerando uma **matriz de rastreabilidade** com pontuação de confiança e citação de linhas exatas onde cada requisito foi atendido ou violado.

> 🛡️ **Regra de Execução**: O agente atua em modo estritamente analítico (somente leitura). Ele não altera o código; registra evidências e buscas realizadas.

---

## 🛠️ 2. Como Usar

### 1. Instalação do Marketplace da Trail of Bits
```bash
# Adiciona o marketplace de plugins da Trail of Bits
codex plugin marketplace add trailofbits/skills

# Instala a skill de compliance
codex plugin add spec-to-code-compliance@trailofbits
```

### 2. Execução da Auditoria no Projeto
```text
/spec-to-code-compliance:spec-compliance ./src
```

### 3. Prompt de Verificação Recomendado
```text
Compare ./src com SPEC.md e verifique a conformidade de todos os requisitos funcionais e não-funcionais.
Não altere o código; registre evidências e buscas realizadas.
Gere o relatório em spec-compliance/REPORT.md com a matriz de alinhamento.
```

---

## 🎯 3. Impacto nos Produtos da Async Studio

* **[[app-encaixe]]**: Garante que regras críticas de negócio (como concorrência de horários e políticas de cancelamento descritas nos requisitos) estejam 100% implementadas antes do deploy.
* **[[app-asynchub]]**: Audita se os contratos de API e regras de isolamento multi-tenant atendem às especificações técnicas.
* **Projetos de Clientes**: Gera relatórios formais de entrega e conformidade de escopo para validação com contratantes.

---

## ⚖️ 4. Sinergia com as Skills do Vault

* **Skill [levantamento-requisitos](../../ia/agentes/skills/levantamento-requisitos/SKILL.md)**: Gera o `SPEC.md` / PRD estruturado antes de implementar.

* **`spec-to-code-compliance`**: Audita se o código gerado após o desenvolvimento respeitou o `SPEC.md` sem sofrer desvios (*scope drift*).
* **[[clean-code]]**: Garante que o código auditado seja mantido limpo e sustentável.

---

## 🔗 Ver também

* [[semgrep-guardian]] — análise estática de segurança complementar.
* [[adocao-de-ferramenta]] — portão de adoção técnica.
* [[qualidade-automatizada]] — testes determinísticos de regressão.
* [levantamento-requisitos](../../ia/agentes/skills/levantamento-requisitos/SKILL.md) — elicitação e estruturação de requisitos.
