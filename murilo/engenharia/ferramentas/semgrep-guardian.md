---
titulo: "Semgrep Guardian & Semgrep MCP — SAST para Agentes de Código"
resumo: "Auditoria estática de segurança integrada ao loop de agentes de IA, bloqueando vulnerabilidades em tempo real antes do commit."
tipo: referencia
dominio: murilo
tags: [murilo/engenharia, ferramentas, seguranca, qualidade-de-codigo, ia]
status: ativo
atualizado: 2026-08-27
---

# Semgrep Guardian & Semgrep MCP — SAST para Agentes de Código

## 📌 Resumo

O **Semgrep Guardian** e o **Semgrep MCP** integram análise estática de segurança (SAST) diretamente ao loop de geração de código de agentes de IA (Claude Code, Cursor, Windsurf, Antigravity). A ferramenta intercepta o código gerado em tempo real, impedindo que vulnerabilidades cheguem ao repositório ou ao ambiente de produção.

No [[adocao-de-ferramenta]], o Semgrep é classificado como **Adoção Imediata (P0)**: custo zero no modo local/community, impacto crítico de mitigação e reversibilidade imediata.

---

## 🧠 1. Como Funciona

A integração de Semgrep com agentes opera em três camadas:

1. **MCP Server (`semgrep-mcp`)**: Expõe as capacidades do motor Semgrep como ferramentas chamáveis nativamente pelo LLM para auditar trechos de código e verificar conformidade.
2. **Hooks On-Write**: Dispara varreduras automáticas sempre que o agente grava um arquivo no disco, antes de finalizar o turno ou executar commits.
3. **Rulesets Especializados para IA**: Detecta padrões comuns de alucinação e falhas de segurança geradas por LLMs:
   * Queries SQL diretas sem parametrização.
   * Políticas de Row Level Security (RLS) permissivas ou ausentes no Supabase.
   * Chaves de API, segredos e tokens expostos em código.
   * Regras inseguras de CORS e sanitização deficiente em endpoints.

---

## 💰 2. Custo, Licenciamento & Privacidade

| Modalidade | Licença / Custo | Requisitos de Rede | Recursos |
| :--- | :--- | :--- | :--- |
| **Local / Community (Recomendado)** | LGPL-2.1 / **100% Gratuito** | Offline / Zero Cloud | Rulesets públicos do Semgrep Registry (`p/default`, `p/owasp-top-ten`, `p/typescript`, `p/secrets`). |
| **Semgrep AppSec Platform** | Freemium (grátis até 10 devs) | Requer Login Cloud | Análise de taint inter-arquivos (*cross-file*) e Pro Rules corporativas. |

> 💡 **Diretriz**: Adote o modo **Local MCP** para garantir privacidade total dos arquivos do projeto, sem acoplamento a autenticação de terceiros.

---

## 🛠️ 3. Como Configurar

### Configuração via MCP Local
No arquivo de configuração MCP da IDE ou agente (`mcp_config.json` ou `.claude.json`):

```json
{
  "mcpServers": {
    "semgrep": {
      "command": "uvx",
      "args": ["semgrep-mcp"]
    }
  }
}
```

### Configuração via Skill ou CLI
```bash
# Como skill de agente:
npx skills add semgrep/skills --skill semgrep

# Ou instalação local via Python/uv:
python3 -m pip install semgrep

# Varredura automática no diretório raiz:
semgrep --config auto .
```

### Prompt de Guardrail Recomendado para o Agente
```text
@semgrep: Analise os achados deste scan.
Explique as vulnerabilidades encontradas, proponha a correção estritamente necessária e NÃO altere o comportamento ou regra de negócio do sistema.
Validação obrigatória: execute o mesmo scan após as correções para garantir conformidade.
```


---

## 🎯 4. Impacto nos Produtos da Async Studio

* **[[app-encaixe]]**: Protege as Edge Functions, rotas do Resend e políticas RLS de agendamento no Supabase contra falhas de injeção e escalada de privilégios.
* **[[app-asynchub]]**: Garante isolamento estrito entre dados de clientes no banco PostgreSQL e impede exposição acidental de credenciais em endpoints internos.
* **[[site-institucional]]**: Valida sanitização de inputs em formulários de contato e configurações seguras de headers HTTP.

---

## ⚠️ Riscos & Quando NÃO Usar

* **Loop de Falsos Positivos**: Em caso de falso positivo, a IA pode tentar refatorar código sadio e quebrar regras de negócio. Configure a diretriz do agente para alertar o desenvolvedor antes de aceitar grandes reescritas.
* **Não Substitui Testes Dinâmicos**: O Semgrep faz análise estática; ele não substitui testes funcionais e de fluxo com [[qualidade-automatizada]] (Playwright / Vitest).

---

## 🔗 Ver também

* [[adocao-de-ferramenta]] — critérios de adoção técnica.
* [[qualidade-automatizada]] — ferramentas determinísticas de lint e testes.
* [[clean-code]] — padrões de sustentabilidade e clareza de código.

