---
name: portless-dev
description: >
  Gerencia e executa servidores de desenvolvimento locais através do Portless
  (proxy reverso com terminação HTTPS e domínios *.localhost determinísticos).
  Usar SEMPRE que for iniciar, rodar, hospedar ou testar localmente aplicações
  (ex: "rode o projeto", "sobe o front", "teste localmente", "inicie com portless",
  "executar servidor", "suba a api"). Verifica se o portless está instalado,
  diagnostica o daemon e sobe os serviços com URLs seguras e previsíveis.
---

# Portless Dev — Execução e Proxy Local com HTTPS (*.localhost)

Esta skill define o protocolo operacional para executar aplicações e serviços locais utilizando o **Portless** ([vercel-labs/portless](https://github.com/vercel-labs/portless)), substituindo portas voláteis (`localhost:3000`, `8080`) por domínios determinísticos e seguros (`https://*.localhost`).

**Idioma:** toda comunicação (logs, diagnósticos, links de acesso) é em português do Brasil, direta e técnica.

---

## 🚪 Portão — Vale aplicar isso agora?

Nem todo projeto exige proxy reverso. Aplicar quando:
- Projeto for um SaaS, monorepo ou ecossistema multi-serviço (ex: frontend + API + workers ou cookies compartilhados).
- Projeto precisar de URLs determinísticas para autenticação (OAuth, Supabase Auth) ou cookies `SameSite`/`Secure`.
- O usuário pedir explicitamente para rodar com portless ou testar localmente.

**Não aplicar (usar comando direto do runtime):**
- Scripts one-off em Node/Python (ex: migrations, validações pontuais).
- Atividades acadêmicas simples em HTML estático isolado (ex: `study-*`).

---

## 🛠️ Modo Padrão — Executar e Hospedar Localmente (Default)

Quando o usuário pedir para rodar, testar ou iniciar um projeto, seguir rigorosamente este fluxo:

### 1. Identificar o Projeto e Subdomínio

Determinar o nome do subdomínio baseado no repositório ou workspace atual:

| Projeto / Diretório | Subdomínio HTTPS Padrão | Comando Alvo |
| :--- | :--- | :--- |
| `Async/app-asynchub-crm` (monorepo) | `https://asynchub.localhost` | `pnpm dev` |
| `Async/app-asynchub-crm/apps/api` | `https://asynchub-api.localhost` | `pnpm --filter @asynchub/api dev` |
| `Async/app-asynchub-crm/apps/web` | `https://asynchub.localhost` | `pnpm --filter @asynchub/web dev` |
| `Async/app-encaixe-agendamento` | `https://encaixe.localhost` | `npm run dev` |
| `Async/app-encaixe-agendamento/apps/api` | `https://encaixe-api.localhost` | `npm run dev:api` |
| `Async/app-encaixe-agendamento/apps/web` | `https://encaixe.localhost` | `npm run dev:web` |
| `Async/site-asyncpage` | `https://asyncpage.localhost` | `npm run dev` |
| *Outros projetos* | `https://<nome-do-pacote>.localhost` | `<script dev do package.json>` |

### 2. Verificar Binário do Portless

Verificar se o utilitário está disponível no sistema:
```bash
command -v portless >/dev/null 2>&1 || npx -y portless --version
```
- Se `portless` global estiver instalado: usar `portless <subdominio> <comando>`.
- Se não estiver instalado globalmente: usar `npx -y portless <subdominio> <comando>`.

### 3. Iniciar o Servidor em Background

> [!IMPORTANT]
> Servidores de desenvolvimento são processos persistentes (long-running). **Nunca execute em modo síncrono bloqueante.** Use execução em background / daemon assíncrono.

Exemplo de comando executado no diretório do projeto:
```bash
# Exemplo para Encaixe
portless encaixe npm run dev

# Exemplo para AsyncHub
portless asynchub pnpm dev
```

### 4. Reportar o Link de Acesso

Assim que o comando for enviado para background e os logs iniciais confirmarem inicialização sem erro fatal, devolver imediatamente a resposta com link markdown formatado:

```markdown
🚀 **Servidor local iniciado via Portless**
* **Aplicação**: `[Nome do Projeto]`
* **URL Local (HTTPS)**: [https://<subdominio>.localhost](https://<subdominio>.localhost)
* **Status**: Proxy ativo com certificado SSL local
```

---

## 🔍 Modo Diagnóstico — `portless doctor`

Acionar quando houver erro de conexão, porta presa ou falha no proxy reverso:

1. Rodar diagnóstico de rede:
   ```bash
   portless doctor
   ```
2. Verificar se o proxy daemon está escutando nas portas 80/443 locais.
3. Se houver processo zumbi prendendo portas, orientar o encerramento do processo ou reiniciar o daemon do portless.

---

## 🛑 Guardrails

- **Nunca travar o turno do agente**: Não aguarde a saída final de comandos como `npm run dev` ou `portless ...` — eles são daemons e rodam indefinidamente.
- **Atenção a permissões SSL do macOS**: Na primeira execução do Portless, o macOS pode exigir autorização do usuário para confiar no certificado raiz local. Avise o usuário se houver bloqueio de TLS.
- **Respeitar variáveis de ambiente**: Garantir que o `.env` local exista antes de disparar o dev server. Se faltar `.env`, alerte antes de rodar.

---

## 🔗 Referências

- Nota de infraestrutura: `murilo/engenharia/infra/portless.md`
- Critérios de adoção: `murilo/engenharia/adocao-de-ferramenta.md`
