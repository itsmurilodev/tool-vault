#!/usr/bin/env bash
#
# Cria uma nota nova já com frontmatter preenchido e regenera os índices.
#
# Uso:
#   ./scripts/nova-nota.sh <dominio> <nome-em-kebab-case> ["Título da nota"]
#   ./scripts/nova-nota.sh infra docker-compose
#   ./scripts/nova-nota.sh engenharia testes "Estratégia de testes"
#   ./scripts/nova-nota.sh ferramentas/github actions-base
#
# O domínio aceita subpasta (ferramentas/github). O tipo é inferido do domínio
# e pode ser trocado à mão depois — o que importa é a nota existir.

set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RAIZ"

if [[ $# -lt 2 ]]; then
  echo "uso: ./scripts/nova-nota.sh <dominio> <nome-em-kebab-case> [\"Título\"]" >&2
  echo "domínios: ia, engenharia, infra, ferramentas (subpasta permitida)" >&2
  exit 1
fi

DOMINIO_COMPLETO="${1%/}"
NOME="$2"
DOMINIO_RAIZ="${DOMINIO_COMPLETO%%/*}"

case "$DOMINIO_RAIZ" in
  ia|engenharia|infra|ferramentas) ;;
  *)
    echo "erro: domínio '$DOMINIO_RAIZ' não existe." >&2
    echo "use ia, engenharia, infra ou ferramentas — ou crie o domínio novo antes," >&2
    echo "seguindo a regra de CONVENCOES.md seção 1 (3+ notas que não cabem nos atuais)." >&2
    exit 1
    ;;
esac

if [[ ! "$NOME" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "erro: '$NOME' não está em kebab-case (minúsculas, hífen, sem acento)." >&2
  exit 1
fi

DESTINO="$DOMINIO_COMPLETO/$NOME.md"

if [[ -e "$DESTINO" ]]; then
  echo "erro: $DESTINO já existe. Não vou sobrescrever." >&2
  exit 1
fi

# Nome de arquivo precisa ser único no vault inteiro: o Obsidian resolve
# wikilink por nome, e nome repetido torna todo [[link]] ambíguo.
EXISTENTE="$(find . -name "$NOME.md" -not -path "./.git/*" -print -quit)"
if [[ -n "$EXISTENTE" ]]; then
  echo "erro: já existe uma nota chamada '$NOME.md' em $EXISTENTE." >&2
  echo "escolha um nome único — ver CONVENCOES.md seção 3." >&2
  exit 1
fi

if [[ $# -ge 3 ]]; then
  TITULO="$3"
else
  # kebab-case vira título legível: "docker-compose" -> "Docker compose"
  TITULO="$(echo "$NOME" | tr '-' ' ')"
  TITULO="$(tr '[:lower:]' '[:upper:]' <<< "${TITULO:0:1}")${TITULO:1}"
fi

HOJE="$(date +%F)"

mkdir -p "$(dirname "$DESTINO")"
cat > "$DESTINO" <<EOF
---
titulo: "$TITULO"
resumo: ""
tipo: conceito
dominio: $DOMINIO_RAIZ
tags: []
status: rascunho
atualizado: $HOJE
---

# $TITULO

## 📌 Resumo

_O que é isso e por que importa, em 3-5 linhas._

## 🧠 Conceitos principais

## ⚠️ Erros comuns

## ✅ Como aplicar na prática

## 🔗 Ver também

## 📚 Fontes
EOF

echo "criada: $DESTINO"
echo
./scripts/gerar-indices.py
echo
echo "próximo passo: preencher o resumo no frontmatter — é ele que aparece no índice."
