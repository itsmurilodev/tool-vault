# 📓 Personal Vault

> Vault pessoal de conhecimento estruturado para organizar, documentar e versionar anotações pessoais, profissionais e técnicas utilizando Markdown, Obsidian e Git.

---

## 🗺️ Mapa do Vault

A estrutura do vault é organizada por contextos claros para facilitar a navegação e o consumo:

```text
personal-vault/
├── .obsidian/               # Configurações globais do Obsidian (aparência, plugins)
├── github/                  # Padrões e padronizações para o ecossistema GitHub
│   └── organizacao.md       # Diretrizes de nomenclatura de repositórios
├── ia/                      # Estudos, personas e automações com IA
│   ├── conceitos/           # Anotações teóricas e estudos de fundamentação
│   │   ├── clean-code/      # Princípios de código limpo e arquitetura
│   │   └── prompt-engineering/ # Técnicas de engenharia de prompt e comportamento de LLMs
│   └── praticas/            # Aplicações práticas e artefatos de agentes
│       ├── personas-agentes/# Perfis de comportamento para IAs especializadas
│       ├── rules-workflows/ # Instruções e fluxos de trabalho (global/local)
│       └── skills/          # Skills/habilidades acopláveis para agentes de IA
└── README.md                # Guia de entrada do vault (este arquivo)
```

---

## 🛠️ Diretrizes de Organização (Como contribuir)

Para manter a consistência e a portabilidade das notas, siga as seguintes diretrizes:

1. **Nomes de Arquivos:** Sempre utilize `kebab-case` (letras minúsculas, separadas por hífen, sem espaços ou caracteres especiais/acentos).
   * *Correto:* `estudo-prompt-engineering.md`
   * *Incorreto:* `Estudo Prompt Engineering.md` ou `estudo_prompt_engineering.md`
2. **Uso de Links Internos:** Utilize o formato padrão do Obsidian `[[nome-do-arquivo]]` ou links markdown relativos para conectar ideias (Backlinks).
3. **Versionamento:** Commits frequentes com mensagens diretas e claras que resumam o conhecimento adicionado ou modificado.