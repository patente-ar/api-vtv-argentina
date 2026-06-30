#!/usr/bin/env bash
set -euo pipefail

api_base="${PATENTE_API_BASE_URL:-https://api.patente.ar/v1/consultas}"
api_key="${PATENTE_API_KEY:?set PATENTE_API_KEY}"
idempotency_key="${PATENTE_IDEMPOTENCY_KEY:-vtv-demo-001}"
x_token="${PATENTE_X_TOKEN:-orden-externa-001}"

curl -sS -X POST "$api_base" \
  -H "Authorization: Bearer $api_key" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $idempotency_key" \
  -H "x-token: $x_token" \
  --data '{"patente":["AB123CD"],"jurisdiccion":["pba","caba"]}'
