# Padrões de Segurança e Mitigações SAST (Next.js, Supabase & TypeScript)

Guia de referência rápida para correções comuns detectadas pelo Semgrep.

---

## 1. Prevenção de SQL Injection (PostgreSQL / Supabase)

### ❌ Inseguro (Concatenação de Strings)
```typescript
// NUNCA concatenar entrada do usuário em queries raw
const query = `SELECT * FROM clientes WHERE tenant_id = '${tenantId}' AND email = '${email}'`;
const { data } = await supabase.rpc('exec_sql', { sql: query });
```

### ✅ Seguro (Query Parametrizada)
```typescript
// Usando client nativo ou parâmetros preparados
const { data, error } = await supabase
  .from('clientes')
  .select('*')
  .eq('tenant_id', tenantId)
  .eq('email', email);
```

---

## 2. Blindagem de Row Level Security (RLS) no Supabase

### ❌ Inseguro (Tabela sem RLS ou com permissão aberta)
```sql
CREATE TABLE public.pedidos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cliente_id UUID NOT NULL,
  total DECIMAL NOT NULL
);
-- Esquecer o ENABLE RLS expõe toda a tabela para acesso anônimo
```

### ✅ Seguro (RLS Habilitado com Políticas Específicas)
```sql
CREATE TABLE public.pedidos (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cliente_id UUID NOT NULL,
  total DECIMAL NOT NULL
);

-- 1. Habilitar RLS obrigatoriamente
ALTER TABLE public.pedidos ENABLE ROW LEVEL SECURITY;

-- 2. Política de Leitura: Usuário só vê seus próprios pedidos
CREATE POLICY "Usuarios visualizam apenas seus pedidos"
  ON public.pedidos
  FOR SELECT
  USING (auth.uid() = cliente_id);

-- 3. Política de Inserção: Usuário só insere pedidos para si mesmo
CREATE POLICY "Usuarios inserem pedidos proprios"
  ON public.pedidos
  FOR INSERT
  WITH CHECK (auth.uid() = cliente_id);
```

---

## 3. Validação Estrita de Entrada (Zod)

### ❌ Inseguro (Payload sem tipagem ou validação)
```typescript
export async function POST(req: Request) {
  const body = await req.json();
  // Se body.email contiver payload malicioso ou tipo inesperado, quebra o fluxo
  await db.salvar(body);
}
```

### ✅ Seguro (Schema de Validação)
```typescript
import { z } from 'zod';

const PayloadSchema = z.object({
  email: z.string().email(),
  nome: z.string().min(2).max(100),
  tenantId: z.string().uuid()
});

export async function POST(req: Request) {
  const json = await req.json();
  const resultado = PayloadSchema.safeParse(json);
  
  if (!resultado.success) {
    return new Response(JSON.stringify({ erro: 'Dados invalidos', detalhes: resultado.error.format() }), { status: 400 });
  }

  await db.salvar(resultado.data);
}
```
