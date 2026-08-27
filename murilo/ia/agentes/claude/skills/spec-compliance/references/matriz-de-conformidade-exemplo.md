# Exemplo Prático de Matriz de Conformidade (Spec-to-Code)

Demonstração de como estruturar o relatório de auditoria de conformidade entre uma especificação de SaaS e o código em `./src`.

---

## 1. Exemplo de Mapeamento

### Especificação Base (`SPEC.md`)
* `REQ-01`: "O sistema deve autenticar usuários via Magic Link por email usando Supabase Auth."
* `REQ-02`: "Após login com sucesso, o usuário deve ser redirecionado para `/dashboard`."
* `REQ-03`: "Em caso de falha de autenticação, exibir alerta amigável e registrar log de erro no Sentry."
* `REQ-04`: "Taxa de requisição no endpoint de login limitada a 5 tentativas por minuto por IP."

### Matriz Gerada

| ID | Requisito | Status | Evidência no Código | Confiança |
| :-: | :--- | :---: | :--- | :---: |
| **REQ-01** | Magic Link Supabase Auth | ✅ Atendido | `src/app/auth/actions.ts:L15-L28` (`signInWithOtp`) | Alta |
| **REQ-02** | Redirecionamento `/dashboard` | ✅ Atendido | `src/app/auth/callback/route.ts:L32` (`redirect('/dashboard')`) | Alta |
| **REQ-03** | Alerta amigável + Sentry | ⚠️ Parcial | `src/components/LoginForm.tsx:L40` exibe alerta, mas `Sentry.captureException` não foi chamado | Média |
| **REQ-04** | Rate Limiting (5 req/min) | ❌ Não Atendido | Nenhum middleware ou Upstash Redis implementado em `src/middleware.ts` | Alta |

---

## 2. Relatório de Ação Recomendada

1. **Ação para REQ-03**:
   * Adicionar `Sentry.captureException(error)` dentro do bloco `catch` em `src/components/LoginForm.tsx`.
2. **Ação para REQ-04**:
   * Implementar `middleware.ts` com `@upstash/ratelimit` configurado para 5 requisições por minuto na rota `/api/auth/*`.
