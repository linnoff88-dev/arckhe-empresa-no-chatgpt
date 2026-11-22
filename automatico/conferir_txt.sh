#!/usr/bin/env bash
# Confere se o TXT de verificação do ChatGPT já aparece no DNS público.
# Uso: bash automatico/conferir_txt.sh seusite.com.br [host]
set -u
dom="${1:?uso: conferir_txt.sh <dominio> [host]}"
host="${2:-openai-business-profile}"
nome="$host.$dom"
for ns in 1.1.1.1 8.8.8.8; do
  v=$(dig +short TXT "$nome" @"$ns" 2>/dev/null)
  if [ -n "$v" ]; then echo "ok ($ns): $nome → $v"; else echo "ainda não ($ns): $nome"; fi
done
