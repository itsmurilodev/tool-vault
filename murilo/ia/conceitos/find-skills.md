---
titulo: "Find Skills — Descoberta de Extensões e Riscos de Inchaço de Contexto"
resumo: "Análise da CLI npx skills (skills.sh) e diretrizes de defesa contra prompt bloating e injeção de dependências em agentes."
tipo: conceito
dominio: murilo
tags: [murilo/ia, agentes, skills, seguranca, governanca]
status: ativo
atualizado: 2026-08-27
---

# Find Skills — Descoberta de Extensões e Riscos de Inchaço de Contexto

## 📌 Resumo

A CLI `npx skills` e a meta-skill **`find-skills`** ([vercel-labs/skills](https://github.com/vercel-labs/skills) / [skills.sh](https://skills.sh)) foram criadas para permitir que desenvolvedores e agentes de IA descubram, instalem e gerenciem extensões de prompt sob demanda.

No [[adocao-de-ferramenta]], o uso de auto-descoberta dinâmica pelo agente é classificado como **Descarte Imediato (P4)** devido aos riscos críticos de inchaço de contexto (*prompt bloating*), falhas de roteamento e injeção indireta de prompt.

---

## 🔍 1. Como Funciona a CLI `npx skills`

O utilitário funciona como um gerenciador de pacotes comunitário para mais de 40 clientes de IA (Claude Code, Cursor, Windsurf):

```bash
# Busca interativa de skills
npx skills find [termo]

# Instalação de uma skill comunitária
npx skills add autor/repo --skill nome-da-skill

# Verificação de atualizações
npx skills check
```

A extensão `find-skills` opera como uma *meta-skill*, permitindo que o próprio LLM pesquise no registro da Vercel Labs e decida sugerir a instalação de novos comandos dinamicamente durante uma sessão de chat.

---

## ⚠️ 2. Riscos Críticos de Engenharia

### 1. Inchaço Crônico de Contexto (Prompt Bloating)
Cada skill instalada adiciona centenas de tokens de regras ao system prompt base. O acúmulo desordenado:
* Reduz o espaço útil para o código e documentos do projeto.
* Aumenta a latência e o custo de inferência por requisição.
* Induz o agente a falhas de roteamento (*tool routing error*), selecionando ferramentas erradas para problemas simples.

### 2. Superfície de Ataque e Injeção Indireta de Prompt
Skills comunitárias abertas podem conter:
* Instruções ocultas que desviam dos guardrails de segurança do projeto.
* Exfiltração de variáveis de ambiente (`.env`) ou histórico de comandos.
* Scripts que induzem a execução de código não verificado.

---

## 🛡️ 3. Regra de Governança no Tool-Vault

No ecossistema do Murilo e da Async Studio:

1. **Curadoria Manual e Estática**: Nenhuma ferramenta ou skill é instalada dinamicamente pelo agente.
2. **Avaliação pelo Portão de Adoção**: Toda nova capacidade técnica deve passar pelo crivo de [[adocao-de-ferramenta]] antes de entrar no diretório `skills/` ou `mcp_config.json`.
3. **Isolamento de Escopo**: Ferramentas especializadas (como [[impeccable]]) devem ser invocadas apenas em contextos pertinentes, sem poluir a baseline universal do agente.

---

## 🔗 Ver também

* [[adocao-de-ferramenta]] — critérios fundamentais para adoção de ferramentas.
* [[modus-operandi]] — princípios de simplicidade e sustentabilidade técnica.
* [[semgrep-guardian]] — blindagem ativa contra vulnerabilidades em agentes.

