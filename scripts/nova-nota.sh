#!/usr/bin/env bash
#
# Cria uma nota nova já com frontmatter preenchido e regenera os índices.
#
# Uso:
#   ./scripts/nova-nota.sh <pilar/subpasta> <nome-em-kebab-case> ["Título da nota"]
#   ./scripts/nova-nota.sh murilo/engenharia/infra docker-compose
#   ./scripts/nova-nota.sh murilo/engenharia testes "Estratégia de testes"
#   ./scripts/nova-nota.sh async/identidade brand-tokens
#   ./scripts/nova-nota.sh async/produtos app-novo "Novo SaaS"
#

set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RAIZ"

if [[ $# -lt 2 ]]; then
  echo "uso: ./scripts/nova-nota.sh <pilar/subpasta> <nome-em-kebab-case> [\"Título\"]" >&2
  echo "pilares raiz: murilo, async (ex: murilo/engenharia, async/produtos)" >&2
  exit 1
fi

DOMINIO_COMPLETO="${1%/}"
NOME="$2"
DOMINIO_RAIZ="${DOMINIO_COMPLETO%%/*}"

case "$DOMINIO_RAIZ" in
  murilo|async) ;;
  *)
    echo "erro: pilar raiz '$DOMINIO_RAIZ' inválido." >&2
    echo "use caminhos dentro de 'murilo' ou 'async' (ex: murilo/engenharia, async/produtos)." >&2
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

# Nome de arquivo precisa ser único no vault inteiro
EXISTENTE="$(find . -name "$NOME.md" -not -path "./.git/*" -print -quit)"
if [[ -n "$EXISTENTE" ]]; then
  echo "erro: já existe uma nota chamada '$NOME.md' em $EXISTENTE." >&2
  echo "escolha um nome único — ver CONVENCOES.md seção 3." >&2
  exit 1
fi

if [[ $# -ge 3 ]]; then
  TITULO="$3"
else
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
tags: [$DOMINIO_COMPLETO]
status: rascunho
atualizado: $HOJE
---

# $TITULO

## 📌 Resumo

_O que é isso e por que importa, em 3-5 linhas._

## 🧠 Conceitos principais

## ⚠️ Erros comuns e trade-offs

## ✅ Como aplicar na prática

## 🔗 Ver também

## 📚 Fontes
EOF

echo "criada: $DESTINO"

# Regenera os índices para a nota nova já entrar
./scripts/gerar-indices.py
