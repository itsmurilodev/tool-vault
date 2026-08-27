---
name: semgrep-scan
description: >
  Audita e blinda código contra vulnerabilidades de segurança (SAST) em tempo
  real — injeção SQL, brechas em Row Level Security (RLS) do Supabase, CORS
  permissivo, segredos/tokens expostos e violações OWASP. Usar ao gerar, editar
  ou revisar código backend, APIs, rotas e infraestrutura.
---

# Semgrep Scan — Blindagem Estática de Código (SAST)

Este skill define as diretrizes para auditar e corrigir vulnerabilidades de segurança em código gerado por IA ou legado, utilizando o motor estático Semgrep no modo local (sem dependência de cloud).

## 🛡️ Quando Disparar

* **Modo Silencioso (Default)**: Ao gerar código de backend, endpoints de API, consultas a banco de dados (SQL / Supabase) ou manipulação de tokens e variáveis de ambiente.
* **Modo Auditoria Explícita**: Quando o usuário solicitar comandos como `"audite a segurança deste código"`, `"verifique vulnerabilidades"`, `"rode o semgrep"`.

---

## 🧠 1. Regras de Prevenção em Tempo de Geração

Sempre que escrever ou refatorar código backend:

1. **Zero SQL Dinâmico**: Toda query deve usar prepared statements / consultas parametrizadas do ORM ou driver. Jamais concatenar strings com entradas do usuário.
2. **Supabase RLS Estrito**: Toda tabela no PostgreSQL acessível via API client-side deve ter `ENABLE ROW LEVEL SECURITY` e policies explícitas para `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
3. **Zero Secrets Hardcoded**: Chaves de API, senhas e tokens nunca devem ser escritos diretamente em arquivos. Utilize sempre `process.env.VAR` ou arquivos `.env.local` ignorados no `.gitignore`.
4. **Sanitização de Entradas**: Todo payload de requisição deve ser validado via schemas estritos (ex: Zod, Yup, Pydantic) antes de qualquer processamento.

---

## 🛠️ 2. Execução de Varredura Local

Quando for solicitado escanear o projeto ou validar uma pasta:

```bash
# Varredura rápida automática no diretório corrente
semgrep --config auto .

# Ou varredura focada em TypeScript, Next.js e OWASP
semgrep scan --config "p/default" --config "p/typescript" --config "p/owasp-top-ten"
```

---

## ⚠️ 3. Guardrail Obrigatório de Correção

Ao aplicar correções automáticas para achados do Semgrep:

* **Preservação de Comportamento**: A correção deve mitigar a vulnerabilidade estritamente sem quebrar regras de negócio ou alterar o comportamento esperado da aplicação.
* **Validação Obrigatória**: Sempre re-execute a varredura (`semgrep scan`) após aplicar a correção para garantir que o alerta foi mitigado e nenhum novo problema foi introduzido.
* **Alerta Humano**: Se a correção exigir mudança em contrato de API pública ou schema de banco de dados, interrompa a edição e alerte o usuário com as opções disponíveis.

---

## 📋 Formato de Saída em Auditorias Explícitas

```markdown
## 🛡️ Diagnóstico de Segurança (Semgrep)
* **Status**: [Vulnerabilidades Encontradas / Seguro]
* **Arquivos Analisados**: [Lista]

### 🚨 Achados Críticos & Mitigações
1. **[Arquivo:Linha]** — [Descrição da Vulnerabilidade (ex: CWE-89 SQLi)]
   * **Risco**: [Impacto concreto]
   * **Correção Aplicada**: [Trecho de código seguro]

### ✅ Validação Pós-Correção
* [ ] Varredura semgrep limpa (0 alertas).
```
