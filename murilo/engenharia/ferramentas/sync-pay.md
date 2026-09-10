---
titulo: "SyncPay — Infraestrutura de Pagamentos, Pix, Recorrência e Automação via MCP"
resumo: "Gateway de pagamentos focado no mercado brasileiro com Pix instantâneo, Pix Automático, cartão tokenizado, split e servidor MCP nativo para agentes de IA."
tipo: referencia
dominio: murilo
tags: [murilo/engenharia, ferramentas, pagamentos, pix, api, ia]
status: ativo
atualizado: 2026-08-28
---

# SyncPay — Infraestrutura de Pagamentos, Pix, Recorrência e Automação via MCP

## 📌 Resumo

O **SyncPay** (`syncpayments.com.br` / `syncpay.io`) é uma plataforma brasileira de infraestrutura de pagamentos, checkout de alta conversão e APIs financeiras desenhada para infoprodutores, SaaS, e-commerces e plataformas com modelos de coprodução ou afiliados.

Diferente de gateways tradicionais que oferecem APIs legadas e complexas de integrar, o SyncPay destaca-se por três pilares técnicos:
1. **API REST moderna (OpenAPI 3.1):** foco em Pix instantâneo (Cash-In / Cash-Out), nova regulação de **Pix Automático**, assinaturas/recorrência e split dinâmico de receitas.
2. **Segurança de cartão com tokenização selada (Zero-Storage):** padrão onde o backend do lojista nunca armazena nem processa dados brutos do cartão (PAN), operando com tokens descartáveis de 15 minutos com validação Luhn em sandbox seguro.
3. **Pioneirismo em IA com MCP Nativo e `llms.txt`:** disponibiliza endpoint oficial de **Model Context Protocol (MCP)** em `https://mcp.syncpayments.com.br/mcp` e documentação otimizada em `https://syncpay.apidog.io/llms.txt`, permitindo que agentes autônomos (Antigravity, Claude, Cursor, ChatGPT) interajam diretamente com operações financeiras.

No [[adocao-de-ferramenta]], o SyncPay é classificado como **Camada de Monetização & Gateway Transacional**: ideal para projetos que exigem liquidação rápida via Pix, divisão automatizada de faturamento com parceiros e automação operacional via IA.

---

## 🧠 1. Arquitetura e Mecânica Interna

A arquitetura do SyncPay separa o fluxo de pagamentos, segurança criptográfica e a camada de integração com agentes:

```mermaid
flowchart TD
    subgraph Cliente["Camada de Interface / Cliente"]
        App["Frontend / Checkout Web"]
        Agent["Agente de IA (Cursor / Antigravity / Claude)"]
    end

    subgraph SyncPayCore["Plataforma SyncPay"]
        Auth["OAuth / Token Server (/auth-token)"]
        PixEngine["Motor Pix (CashIn / CashOut / Pix Automático)"]
        CardSealer["Card Tokenizer (/card-tokens)"]
        SplitEngine["Motor de Split & Comissões"]
        SubEngine["Motor de Assinaturas & Recorrência"]
        MCPServer["Servidor MCP (mcp.syncpayments.com.br/mcp)"]
        WebhookDispatcher["Webhook Dispatcher (HMAC-SHA256)"]
    end

    subgraph BackendMerchant["Servidor da Aplicação (Backend)"]
        APIHandler["API Handler & Business Logic"]
        WebhookReceiver["Receptor de Webhooks & Validador HMAC"]
        DB[("Banco de Dados (Idempotência event_id)")]
    end

    Agent <-->|JSON-RPC via MCP| MCPServer
    MCPServer <--> Auth
    MCPServer <--> PixEngine

    App -->|1. Selar Cartão (PAN)| CardSealer
    CardSealer -.->|2. Token Selado (15 min)| App
    App -->|3. Submeter Pedido (card_token)| APIHandler

    APIHandler -->|Bearer Token| Auth
    APIHandler -->|4. Cobrar no Cartão / Gerar Pix| SyncPayCore
    SyncPayCore --> SplitEngine
    SyncPayCore --> SubEngine

    SyncPayCore -->|5. Disparo de Notificação Assinada| WebhookDispatcher
    WebhookDispatcher -->|X-SyncPay-Signature HMAC| WebhookReceiver
    WebhookReceiver -->|6. Valida Assinatura & Janela Replay| DB
```

### 1.1. Autenticação Baseada em Bearer Token
Todas as chamadas à API de parceiros requerem autenticação via Bearer Token.
* **Endpoint:** `POST /api/partner/v1/auth-token`
* **Credenciais:** `client_id` (UUID) e `client_secret` (UUID).
* **Ciclo de Vida:** O token possui validade de **1 hora** (`3600` segundos). Boas práticas exigem que a aplicação cacheie o token em memória/Redis e apenas requisite um novo ao expirar, evitando rate-limit (`429`).

### 1.2. Pix Cash-In e Cash-Out
* **Cash-In (`POST /api/partner/v1/cash-in`):** Recebe o valor (`amount`), dados cadastrais do pagador (`client`: nome, CPF, email, telefone), URL de callback e parâmetros opcionais de split. Retorna imediatamente a string `pix_code` (código copia-e-cola e QRCode) e o `identifier` (UUID exclusivo da transação).
* **Cash-Out:** Permite transferências e saques automatizados para contas bancárias ou chaves Pix cadastradas.

### 1.3. Cartão de Crédito em Duas Etapas (Zero Custódia)
Para eliminar a responsabilidade de PCI-DSS severo do servidor da aplicação:
1. **Selagem (`POST /api/partner/v1/card-tokens`):** Recebe `number`, `holder_name`, `expiry_month`, `expiry_year` e `cvv`. Valida o algoritmo de **Luhn** e data de validade. Retorna um token com prefixo `card_token.xxxx`, bandeira inferida (`brand`) e `last4`.
2. **Cobrança (`POST /api/partner/v1/credit-card`):** O backend consome o `card.token`. É proibido reenviar o PAN/CVV (retorna `422`). É obrigatório enviar o bloco `device` (`ip` real do cliente, `user_agent`, `page_url`) para cálculo do risco no motor de antifraude. Se o token já tiver sido utilizado, a API rejeita com `409 DUPLICATE_CARD_TOKEN`.

### 1.4. Recorrência & Pix Automático
A API oferece suporte a planos (`/plans`), assinantes (`/subscribers`), upgrades/downgrades de plano, suspensão temporária e cobrança via cartão de crédito recorrente ou **Pix Automático** (onde o usuário autoriza uma cobrança periódica direta no aplicativo de seu banco).

### 1.5. Split Dinâmico de Pagamentos
Permite dividir faturamentos brutos entre múltiplos recebedores automaticamente:
* **Transacional:** Especificando o array `split: [{ user_id: "uuid", percentage: 30 }]` no ato do Cash-In ou cobrança de cartão (até 3 parceiros).
* **Em Assinaturas:** Convites de split associados a planos (`POST /plans/{token}/splits`), com ciclo de aprovação formal (`accept` / `reject`) pelo recebedor.

---

## 🔒 2. Mecânica de Webhooks & Segurança Criptográfica

Para evitar ataques de injeção de pagamentos falsos, replay attacks ou manipulação em trânsito, o SyncPay utiliza assinatura digital **HMAC-SHA256**:

### Cabeçalhos HTTP Enviados
* `X-SyncPay-Event`: Identifica o tipo de evento (ex.: `transaction.created`, `transaction.updated`, `cobranca_paga`, `mandato_ativado`).
* `X-SyncPay-Delivery`: UUID exclusivo da tentativa de entrega (útil para auditoria e logs de retry).
* `X-SyncPay-Signature`: Assinatura com timestamp no formato `t=<unix_timestamp>,v1=<hex_signature>`.

### Algoritmo de Validação Obrigatória
```typescript
import crypto from "node:crypto";

interface WebhookValidationParams {
  rawBody: string;          // O corpo bruto recebido (Buffer/String ANTES do JSON.parse)
  signatureHeader: string;  // Valor do cabeçalho X-SyncPay-Signature
  secret: string;           // Token secreto do webhook configurado
  toleranceSeconds?: number; // Tolerância máxima contra replay (padrão: 300s = 5 min)
}

export function verifySyncPayWebhook({
  rawBody,
  signatureHeader,
  secret,
  toleranceSeconds = 300,
}: WebhookValidationParams): boolean {
  // 1. Extrai o timestamp (t) e a assinatura (v1)
  const parts = Object.fromEntries(
    signatureHeader.split(",").map((part) => part.trim().split("="))
  );
  const timestamp = Number.parseInt(parts.t, 10);
  const signature = parts.v1;

  if (!timestamp || !signature) {
    return false;
  }

  // 2. Proteção contra Replay Attack: valida se o timestamp está dentro da janela
  const now = Math.floor(Date.now() / 1000);
  if (Math.abs(now - timestamp) > toleranceSeconds) {
    return false; // Fora da janela de 5 minutos
  }

  // 3. Monta a string de validação: "{t}.{corpo bruto}"
  const payloadToSign = `${timestamp}.${rawBody}`;

  // 4. Calcula o HMAC-SHA256 com o segredo
  const expectedSignature = crypto
    .createHmac("sha256", secret)
    .update(payloadToSign, "utf8")
    .digest("hex");

  // 5. Comparação em tempo constante (evita timing attacks)
  if (signature.length !== expectedSignature.length) {
    return false;
  }

  return crypto.timingSafeEqual(
    Buffer.from(signature, "hex"),
    Buffer.from(expectedSignature, "hex")
  );
}
```

> ⚠️ **Regra Crítica de Idempotência:** Para evitar processamento duplicado (caso o gateway retente a entrega de um webhook por latência), o backend deve salvar o `event_id` recebido no corpo e garantir que o mesmo evento não execute regras de negócio mais de uma vez.

---

## 🤖 3. Integração com IA: MCP & `llms.txt`

O SyncPay é um dos pioneiros no ecossistema brasileiro de pagamentos a expor suporte direto a agentes de Inteligência Artificial:

### 3.1. Servidor MCP (Model Context Protocol)
* **URL do MCP Server:** `https://mcp.syncpayments.com.br/mcp`
* **Como Configurar no Antigravity / Claude / Cursor:**
```json
{
  "mcpServers": {
    "syncpay": {
      "url": "https://mcp.syncpayments.com.br/mcp",
      "headers": {
        "Authorization": "Bearer SEU_TOKEN_AQUI"
      }
    }
  }
}
```
* **Capacidades via Agente:**
  * Consultar saldo e extrato financeiro em linguagem natural.
  * Gerar ordens de pagamento Pix para clientes em atendimento automatizado.
  * Verificar status de transações e chargebacks.
  * Criar e monitorar webhooks programaticamente.

### 3.2. Contexto Otimizado (`llms.txt`)
* **Endpoint:** `https://syncpay.apidog.io/llms.txt`
* Permite que IDEs baseadas em IA (Cursor, Windsurf, Copilot, Antigravity) indexem todos os contratos e tipos da API de forma enxuta, sem o ruído de páginas HTML tradicionais.

---

## 🛠️ 4. Guia Rápido de Integração (Exemplos Práticos)

### 4.1. Autenticação e Geração de Cobrança Pix

```typescript
// 1. Obter Token de Autenticação
async function getAuthToken(clientId: string, clientSecret: string) {
  const res = await fetch("https://api.syncpayments.com.br/api/partner/v1/auth-token", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ client_id: clientId, client_secret: clientSecret }),
  });
  const data = await res.json();
  return data.access_token; // Válido por 1 hora
}

// 2. Gerar Cobrança Pix com Split
async function createPixCharge(token: string) {
  const res = await fetch("https://api.syncpayments.com.br/api/partner/v1/cash-in", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization": `Bearer ${token}`,
    },
    body: JSON.stringify({
      amount: 97.00,
      description: "Acesso Plano Pro - Mensal",
      webhook_url: "https://minha-api.com.br/api/webhooks/syncpay",
      client: {
        name: "Carlos Ferreira",
        cpf: "12345678901",
        email: "carlos@exemplo.com.br",
        phone: "11988887777",
      },
      split: [
        {
          user_id: "3f1b9c02-7d64-4a5e-9f3b-2c8e1a4d6b70", // ID do parceiro/afiliado
          percentage: 20, // 20% do valor líquido
        },
      ],
    }),
  });

  const data = await res.json();
  // Retorna pix_code (QR code / Copia e Cola) e identifier (UUID)
  return data;
}
```

---

## ⚖️ 5. Avaliação pelo Portão de Adoção

| Critério | Avaliação Técnica |
| :--- | :--- |
| **Dor Concreta** | Elimina a complexidade de gateways legados; automatiza divisão de faturamento (split); permite automação financeira por agentes de IA (MCP). |
| **Custo de Setup** | Baixo: documentação padronizada em OpenAPI 3.1 e arquivo `llms.txt` facilitam onboarding em minutos. |
| **Custo de Manutenção** | Baixo: contratos de dados estáveis, tokenização de cartão isolada e webhooks com assinatura HMAC padronizada. |
| **Reversibilidade** | Média/Alta: segue padrões REST universais. A troca por outro provedor exige apenas remapear os payloads de Cash-In e Webhook. |
| **Estágio Recomendado** | **MVP com faturamento, SaaS e Plataformas Digitais**: essencial quando há necessidade de Pix de alta disponibilidade, split de vendas ou controle via IA. |

---

## 🔗 Ver também

- [[adocao-de-ferramenta]] — Critérios de avaliação de ferramentas no vault.
- [[clean-code]] — Padrões de escrita para clientes HTTP e validação de contratos.
- [[semgrep-guardian]] — Auditoria de segurança para validação de endpoints e segredos de API.
