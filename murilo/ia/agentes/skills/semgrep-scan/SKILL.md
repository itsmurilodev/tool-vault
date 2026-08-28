---
name: semgrep-scan
description: >
  Audita e blinda código contra vulnerabilidades de segurança (SAST) em tempo
  real — injeção SQL, brechas em Row Level Security (RLS) do Supabase, CORS
  permissivo, segredos/tokens expostos e violações OWASP. Usar SEMPRE que for
  escrever, gerar, editar ou auditar código backend, APIs, rotas, banco de
  dados ou infraestrutura. Quando o pedido for uma auditoria explícita (ex:
  "verifique a segurança", "rode o semgrep", "audite vulnerabilidades"), seguir
  o modo de auditoria com relatório estruturado e revalidação obrigatória.
---

# Semgrep Scan — Blindagem Estática de Segurança (SAST)

Esta skill define as diretrizes para auditar e prevenir vulnerabilidades de segurança em código gerado por IA ou legado, utilizando o motor estático Semgrep no modo local (offline, sem dependência de cloud) e regras do OWASP Top 10.

**Idioma:** toda comunicação (relatórios de auditoria, justificativas de segurança) é em português do Brasil, direta e técnica.

Existem dois modos de operação. Escolha um antes de agir:

---

## 🛡️ Modo Padrão — Escrever ou Editar Código (Comportamento Default)

Aplicar silenciosamente estas salvaguardas sempre que gerar ou refatorar código de backend, endpoints, banco de dados ou autenticação, sem produzir relatórios intermediários visíveis:

1. **Zero SQL Dinâmico / Injeção**: Jamais concatenar strings ou interpolar variáveis diretamente em comandos SQL. Use sempre prepared statements, consultas parametrizadas do driver ou métodos seguros do ORM/query builder.
2. **Supabase Row Level Security (RLS) Estrito**:
   * Toda tabela pública deve conter `ALTER TABLE <nome> ENABLE ROW LEVEL SECURITY;`.
   * Políticas explícitas para cada operação (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) baseadas em `auth.uid()` ou roles seguras. Nunca criar políticas genéricas com `USING (true)` para escrita.
3. **Zero Segredos em Código**: Chaves de API, senhas, tokens JWT e connection strings jamais devem ser fixados no código. Utilize exclusivamente variáveis de ambiente (`process.env.VAR`) e garanta que arquivos `.env*` estejam no `.gitignore`.
4. **Sanitização de Payloads**: Todo dado recebido de clientes externos ou webhooks deve ser validado via schemas estritos (Zod, Yup, Pydantic) antes de ser processado ou salvo.
5. **CORS e Headers Seguros**: Endpoints de API devem restringir origens autorizadas (sem `Access-Control-Allow-Origin: *` em rotas autenticadas).

---

## 🔍 Modo Auditoria — Varredura Explícita de Segurança

Acionar quando o usuário solicitar expressamente a revisão de segurança de um arquivo, pasta ou projeto (ex: *"verifique vulnerabilidades"*, *"rode o semgrep"*, *"audite o backend"*).

### Processo de Execução:

1. **Executar a Varredura Local**:
   ```bash
   # Varredura automática no diretório
   semgrep --config auto .

   # Ou varredura direcionada por tecnologia
   semgrep scan --config "p/default" --config "p/typescript" --config "p/owasp-top-ten" --config "p/sql-injection"
   ```
2. **Classificar os Achados por Severidade**:
   * **Crítico**: Execução remota de código, injeção SQL direta, RLS desativado com dados sensíveis expostos, credencial de produção vazada.
   * **Alto**: Autenticação bypassável, CORS irrestrito em rotas privadas, tokens fracos, CSRF.
   * **Médio**: Falta de rate limiting, mensagens de erro expondo stack trace interno, headers de segurança ausentes.
   * **Baixo / Info**: Más práticas de configuração, comentários com TODO de segurança.
3. **Aplicar a Correção com Guardrail de Ouro**:
   * **Preservar o Comportamento**: Corrigir a brecha sem alterar a regra de negócio ou o contrato da API.
   * **Revalidação Obrigatória**: Rodar a mesma varredura do Semgrep após a correção para provar que o achado foi eliminado.

### Formato de Saída Obrigatório (Markdown):

```markdown
## 🛡️ Diagnóstico de Segurança (Semgrep SAST)
* **Status**: [Vulnerabilidades Encontradas | Seguro]
* **Escopo Analisado**: [Diretório / Arquivos]

### 🚨 Achados de Segurança (Ordenados por Severidade)
| # | Severidade | Vulnerabilidade (CWE/OWASP) | Arquivo:Linha | Impacto Real | Mitigação Aplicada |
| :-: | :---: | :--- | :--- | :--- | :--- |
| 1 | Crítica | SQL Injection (CWE-89) | `src/api/search.ts:L32` | Acesso não autorizado ao banco | Parametrização com Zod/Prisma |
| 2 | Alta | Supabase RLS Missing | `supabase/schema.sql:L14` | Leitura pública de dados | Adicionado ENABLE RLS + Policy |

### 🛠️ Código Corrigido (Antes vs Depois)
[Diff ou snippets concisos mostrando a correção]

### ✅ Validação Pós-Correção
- [ ] Varredura do Semgrep reexecutada — 0 novos alertas encontrados.
- [ ] Comportamento e regras de negócio preservados.
```

---

## ⚠️ Restrições Rígidas da Skill

* **Não delegar regras de negócio ao autofix**: Se o Semgrep acusar um falso positivo ou se a correção exigir mudança no banco de dados, alerte o desenvolvedor antes de executar reescritas profundas.
* **Privacidade Total**: A execução do Semgrep é 100% local (`uvx semgrep` ou `semgrep scan`). Não envie código ou chaves para servidores de terceiros.

---

## 📚 Referência Ampliada

Consulte `references/padroes-seguranca-sast.md` para ver exemplos de código vulnerável vs código blindado em Next.js, Supabase, TypeScript e Node.js.
