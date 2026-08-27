---
titulo: "Portless — Proxy Reverso Local e Domínios Estáticos com HTTPS"
resumo: "Substitui portas localhost caóticas por domínios estáticos e seguros (*.localhost) para facilitar desenvolvimento de múltiplos serviços e agentes."
tipo: referencia
dominio: murilo
tags: [murilo/engenharia, infra, devops, rede, ferramentas]
status: ativo
atualizado: 2026-08-27
---

# Portless — Proxy Reverso Local e Domínios Estáticos com HTTPS

## 📌 Resumo

O **Portless** ([vercel-labs/portless](https://github.com/vercel-labs/portless)), desenvolvido pela Vercel Labs, é um utilitário open-source de proxy reverso local que substitui a gestão caótica de portas (`localhost:3000`, `3001`, `8080`) por domínios nomeados estáveis com terminação SSL/TLS automática (`*.localhost`).

No [[adocao-de-ferramenta]], o Portless é classificado como **Backlog com Gatilho (P2)**: excelente utilitário para ecossistemas multi-serviços, mas desnecessário para fluxos de aplicação única isolada.

---

## 🧠 1. Problema que Resolve

Em desenvolvimento moderno com monorepos, micro-serviços ou múltiplos worktrees do Git:
1. **Conflito de Portas**: Dois serviços tentando escutar na porta `3000` forçam a troca para portas aleatórias (`3001`, `3002`), quebrando URLs salvas no navegador e callbacks de OAuth.
2. **Cookies `Secure` & `SameSite`**: Cookies modernos exigem HTTPS para tráfego seguro. Sem SSL local, o comportamento em desenvolvimento diverge do ambiente de produção.
3. **Previsibilidade para Agentes de IA**: Agentes e scripts de teste precisam de URLs previsíveis e determinísticas para navegar e interagir localmente.

---

## 🌐 2. Como Funciona a Mapeamento

O Portless sobe um proxy local leve que intercepta as requisições e faz o roteamento automático:

```text
localhost:3000  →  https://encaixe.localhost
localhost:3001  →  https://asynchub.localhost
localhost:8000  →  https://api.localhost
```

* **HTTPS Nativo**: Emite certificados TLS locais transparentemente.
* **Auto-Injeção de Flags**: Ajusta parâmetros de `--host` e `--port` para frameworks como Next.js, Vite e FastAPI.

---

## 🛠️ 3. Como Usar

### Instalação & Execução
```bash
# Instalação global ou via npx
npm install -g portless
# ou como skill para o agente: npx skills add vercel-labs/portless --skill=portless

# Executa aplicação com nome fixo e porta mapeada
portless minha-loja npm run dev

# Diagnóstico de rede e proxy
portless doctor
```

### Acesso no Navegador
A aplicação fica disponível com terminação SSL em:
```text
https://minha-loja.localhost
```


---

## 🎯 4. Gatilho de Adoção para Murilo & Async Studio

| Projeto | Gatilho para Adotar Portless |
| :--- | :--- |
| **[[app-asynchub]]** | **Adotar** quando o monorepo pnpm rodar simultaneamente o frontend Next.js, workers e APIs com cookies seguros compartilhados. |
| **[[app-encaixe]]** | **Manter em espera** enquanto o desenvolvimento for centrado em um único app Next.js acoplado diretamente ao Supabase. |
| **[[site-institucional]]** | **Não necessário** (site estático/SSR isolado). |

---

## ⚠️ Riscos & Dependências

* **Camada Extra de Rede**: Em caso de falha de conexão local, adiciona um ponto extra de depuração (verificar se o daemon do proxy está ativo).
* **Requisitos de Runtime**: Projetado para ecossistemas Node.js modernos (Node 20+ / 24+).

---

## 🔗 Ver também

* [[adocao-de-ferramenta]] — critérios de estágio e necessidade real.
* [[app-asynchub]] — monorepo com potencial sinergia para proxy local.

