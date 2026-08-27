---
titulo: "GitHub Issue Creator — Estruturação Automatizada de Chamados"
resumo: "Skill para conversão de logs e stack traces em issues formatadas no GitHub com sanitização de segredos."
tipo: referencia
dominio: murilo
tags: [murilo/engenharia, ferramentas, github, automacao, ia]
status: ativo
atualizado: 2026-08-27
---

# GitHub Issue Creator — Estruturação Automatizada de Chamados

## 📌 Resumo

O **GitHub Issue Creator** (do repositório de skills da Microsoft / ecossistema de agentes) é uma skill projetada para capturar relatórios de erro, stack traces e dumps de execução do terminal, estruturando-os automaticamente em issues padronizadas no GitHub com mascaramento de dados sensíveis.

No [[adocao-de-ferramenta]], a ferramenta é classificada como **Backlog com Gatilho (P3)**: conveniente para times grandes com alto volume de triagem de suporte, mas dispensável para desenvolvimento solo ou equipes enxutas.

---

## ⚙️ 1. Funcionalidades & Como Usar

### 1. Instalação da Skill
```bash
npx skills add microsoft/skills
# Selecione: github-issue-creator
```

### 2. Prompt Recomendado (Com Salvamento Seguro)
```text
Use github-issue-creator neste relato e no print anexado.
Extraia: ambiente, passos de reprodução, comportamento esperado, ocorrido, erro e impacto.
REGRA DE SEGURANÇA: Remova dados sensíveis (tokens, senhas, IPs) e salve em /issues/nome-da-issue.md; NÃO publique diretamente no GitHub.
```

* **Resultado**: Gera um arquivo Markdown estruturado pronto para revisão manual antes de ser transformado em issue online.


---

## ⚖️ 2. Análise de Custo-Benefício

| Vantagem | Risco / Overhead |
| :--- | :--- |
| Reduz o tempo manual de cópia e colagem de logs de erro. | Risco de falha de sanitização (vazamento acidental de tokens parciais). |
| Padroniza a documentação de bugs para o time. | Consumo de tokens de contexto para carregar as instruções da skill. |
| Integração direta com a API do GitHub. | Tempo de setup maior que o benefício para times de 1 a 3 devs. |

---

## 🎯 3. Diretriz para o Stack Murilo & Async Studio

Para a rotina atual de engenharia da Async:
* **Decisão**: Manter o fluxo padrão de abertura rápida de issues orientadas pelo [[fluxo-issue-pr]] e [[padrao-de-repositorios]].
* **Gatilho para Ativação**: Adotar caso a triagem de bugs de clientes externos ou múltiplos mantenedores passe a consumir tempo operacional diário significativo.

---

## 🔗 Ver também

* [[fluxo-issue-pr]] — convenção oficial de Issues, PRs e Commits.
* [[padrao-de-repositorios]] — estrutura padrão dos repositórios GitHub.
* [[adocao-de-ferramenta]] — portão de adoção e limites de overhead.

