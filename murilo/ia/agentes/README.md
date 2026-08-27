# Agentes

Configuração e ecossistema de cada agente de IA usado no dia a dia. Aqui fica o que é **específico de um agente** — formato de arquivo, conectores, hooks, limites de plano.

O que é portável entre agentes **não** entra aqui:

| Portável (fica fora) | Onde está |
| -------------------- | --------- |
| Teoria de prompt e LLM | [`ia/conceitos/`](../conceitos/) |
| Personas (texto que você cola em qualquer agente) | [`ia/personas/`](../personas/) |
| Regras de comportamento (Global/Workspace Rules) | [`ia/regras/`](../regras/) |

## Agentes documentados

- [Claude](claude/) — skills, conectores (MCP), configuração e hooks.

## Ainda sem documentação

Anotar aqui conforme forem sendo usados de verdade, não por completude:

- [ ] ChatGPT / Codex — o que ele faz melhor, onde o formato de instrução difere
- [ ] Gemini / Antigravity
- [ ] Cursor — `.cursorrules` e Workspace Rules já estão em [`ia/regras/`](../regras/); falta o que é específico do editor

## Critério

A mesma persona ou regra funciona em vários agentes; o formato de empacotamento não. Quando uma nota começar com "no Claude você faz assim", ela pertence a `agentes/<nome>/`. Quando começar com "prompt bom tem objetivo explícito", pertence a `conceitos/`.
