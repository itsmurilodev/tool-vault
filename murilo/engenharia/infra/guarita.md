---
titulo: "Guarita — Auditoria Externa de Superfície de Ataque e Conformidade LGPD"
resumo: "Plataforma automatizada de varredura externa de vulnerabilidades, headers HTTP e conformidade de privacidade em produção."
tipo: referencia
dominio: murilo
tags: [murilo/engenharia, infra, seguranca, devops, compliance]
status: ativo
atualizado: 2026-08-27
---

# Guarita — Auditoria Externa de Superfície de Ataque e Conformidade LGPD

## 📌 Resumo

O **Guarita** ([guarita.dev](https://guarita.dev)) é uma plataforma brasileira de *External Attack Surface Management* (EASM) e diagnóstico automatizado de segurança pós-deploy. Ele atua como um scanner externo não-intrusivo que avalia URLs públicas de produção para identificar exposições, certificados frágeis e desconformidades com a LGPD.

No [[adocao-de-ferramenta]], o Guarita é classificado como **Backlog com Gatilho (P2)**: ferramenta útil para auditoria periódica de sites em produção, mas que não substitui a segurança preventiva na esteira de código (SAST).

---

## 🔍 1. O que o Guarita Analisa

A ferramenta realiza varreduras externas a partir da URL fornecida, verificando:

1. **Cabeçalhos HTTP de Segurança**:
   * Ausência de `Content-Security-Policy` (CSP).
   * Ausência ou má configuração de `Strict-Transport-Security` (HSTS).
   * Headers contra clickjacking (`X-Frame-Options`) e MIME sniffing.
2. **Cookies & Sessões Expostas**:
   * Cookies sem flags `HttpOnly`, `Secure` ou `SameSite`.
3. **Conformidade LGPD & Rastreamento**:
   * Presença de scripts e trackers de terceiros sem gestão de consentimento.
   * Exposição indevida de dados pessoais em endpoints públicos.
4. **Certificados TLS/SSL**:
   * Validade, cifras fracas ou alertas de expiração iminente.

---

## 💰 2. Modelo Comercial & Preços

* **Plano Gratuito**: Diagnósticos manuais e pontuais com relatório resumido de status.
* **Planos Pagos (a partir de R$ 79/mês)**: Monitoramento contínuo, histórico de auditorias e geração de prompts automatizados para IAs realizarem a correção dos headers e configs.

---

## 🎯 3. Gatilho de Adoção para Async Studio

| Projeto | Condição para Adoção |
| :--- | :--- |
| **[[app-encaixe]]** | **Adotar plano gratuito para auditoria pontual** após lançamento do produto em produção com usuários reais. |
| **[[site-institucional]]** | **Auditoria periódica trimestral** para garantir conformidade de cookies e cabeçalhos de segurança na Vercel. |
| **[[app-asynchub]]** | **Oportuno** caso endpoints públicos de autenticação e formulários B2B sejam disponibilizados externamente. |

---

## ⚠️ Riscos & Limitações Críticas

* **Diagnóstico Reativo (Tarde Demais)**: O scanner só atua depois que a aplicação está pública. Se houver falha crítica de lógica ou RLS, ela já estará vulnerável.
* **Não Substitui SAST nem CI/CD**: A blindagem primária deve ser feita no momento da escrita com [[semgrep-guardian]] e validações de build.
* **Autorização Obrigatória**: Scans só devem ser executados em domínios próprios e autorizados.

---

## 🔗 Ver também

* [[semgrep-guardian]] — análise estática preventiva em tempo de código.
* [[adocao-de-ferramenta]] — portão de decisão técnica.
* [[site-institucional]] — portal institucional da Async.

