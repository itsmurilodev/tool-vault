---
name: context7
description: >
  Consulta documentação oficial versionada e snippets de código atualizados
  utilizando o Context7 (servidor MCP ou CLI ctx7 da Upstash). Elimina alucinações
  de APIs, métodos depreciados e breaking changes em bibliotecas modernas (Next.js 15,
  Tailwind v4, Drizzle ORM, TanStack, Supabase SSR, etc.). Usar ao implementar, refatorar
  ou depurar código que envolva bibliotecas de rápida evolução, ou quando o usuário
  solicitar expressamente consulta a documentações oficiais ("/context7", "use context7",
  "consulte os docs de X").
---

# Context7 — Consulta de Documentação Oficial e Snippets Atualizados

Esta skill define o protocolo operacional para consultar documentações oficiais versionadas e extrair snippets de código sem *context bloat*, utilizando o **Context7** ([upstash/context7](https://github.com/upstash/context7)) via MCP ou CLI (`ctx7`).

**Idioma:** toda comunicação (respostas, explicações de código, diagnósticos de breaking changes) é em português do Brasil, técnica e direta.

---

## 🚪 Portão — Vale aplicar o Context7 agora?

Nem toda linha de código exige consulta a documentação externa. Avalie antes de acionar a ferramenta:

### ✅ Aplicar quando:
- Trabalhar com **bibliotecas de rápida evolução** ou versões com quebras recentes de compatibilidade (Next.js 14/15 App Router, Server Actions, Tailwind CSS v4, Drizzle ORM, TanStack Router/Query v5, Supabase SSR, Zod v4, bibliotecas de IA/GenAI).
- O compilador TypeScript/linter acusar erro de tipo, propriedade inexistente ou método depreciado em um pacote npm/pip recente.
- O usuário solicitar explicitamente: `"/context7"`, `"use context7"`, `"consulte a documentação oficial de X"`.

### ❌ NÃO aplicar (usar conhecimento estático nativo):
- **Linguagem pura e APIs padrão:** JavaScript Vanilla, TypeScript base, Node.js core (`fs`, `path`, `http`), Python standard library (`os`, `sys`, `json`).
- **Bibliotecas estáveis e consolidadas há anos:** `lodash`, `axios`, `express`, `uuid`, `dotenv`, `cors`.
- **Bibliotecas internas ou módulos privados da empresa:** o índice público do Context7 indexa apenas repositórios abertos.

---

## ⚡ Modo 1 — Resolução e Consulta Silenciosa (Default)

Ao implementar ou refatorar código envolvendo dependências voláteis:

1. **Resolver o ID da Biblioteca:**
   Se tiver acesso a MCP tools (`resolve-library-id`) ou terminal:
   ```bash
   npx ctx7 library <nome-da-lib>
   ```
2. **Consultar o Snippet Específico:**
   Buscar a funcionalidade exata com foco no problema (ex: autenticação, paginação, transação):
   ```bash
   npx ctx7 docs <library-id> "<consulta-especifica>"
   ```
3. **Aplicar no Código:**
   Utilizar a assinatura exata retornada pela documentação oficial, evitando inventar flags ou métodos não documentados.

---

## 🔍 Modo 2 — Consulta Explícita de Documentação e Exemplos

Acione este modo quando o usuário pedir explicitamente documentação ou guia de migração (ex: `"/context7 drizzle-orm batch transactions"`, `"como fazer middleware no next 15 com context7"`).

### 1. Comandos Operacionais da CLI `ctx7`

```bash
# Setup inicial do ambiente / IDE
npx ctx7 setup

# Buscar o ID canônico da biblioteca
npx ctx7 library drizzle-orm
# Retorno esperado: /drizzle-team/drizzle-orm

# Consultar documentação com query focada
npx ctx7 docs /drizzle-team/drizzle-orm "batch transactions api"

# Gerar skill dedicada para uma biblioteca específica
npx ctx7 skills generate
```

### 2. Formato de Resposta Obrigatório

Ao responder a uma consulta explícita de documentação:

```markdown
### 📚 Documentação Oficial: [Nome da Biblioteca] (ID: `/org/repo`)

#### 1. Sintaxe Atual / Assinatura
```typescript
// Código tipado e atualizado conforme docs oficiais
```

#### 2. Mudanças e Atenções Críticas (Breaking Changes)
* [Diferença chave em relação a versões anteriores, se houver]
* [Parâmetros obrigatórios ou boas práticas]

#### 3. Exemplo Prático Aplicado
```typescript
// Exemplo real pronto para uso no projeto
```
```

---

## ⚠️ Cuidados Operacionais e Anti-Patterns

1. **Não poluir a busca:** Faça queries objetivas e ricas em palavras-chave técnicas (ex: `"server actions with zod validation"` em vez de `"how do i write code for my website"`).
2. **Prevenção de vazamento de dados sensíveis:** Nunca inclua tokens, senhas, URLs internas de banco ou nomes de clientes na string de consulta (`query`) enviada ao Context7.
3. **Fallback Graceful:** Se a biblioteca não estiver no índice do Context7, reporte com transparência que a documentação oficial não foi encontrada no índice e utilize a documentação local (`node_modules/@types`) ou busca alternativa.
