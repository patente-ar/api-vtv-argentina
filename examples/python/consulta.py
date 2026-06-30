#!/usr/bin/env python3
import json
import os
import urllib.request

api_base = os.environ.get("PATENTE_API_BASE_URL", "https://api.patente.ar/v1/consultas")
api_key = os.environ.get("PATENTE_API_KEY")
idempotency_key = os.environ.get("PATENTE_IDEMPOTENCY_KEY", "vtv-demo-001")
x_token = os.environ.get("PATENTE_X_TOKEN", "orden-externa-001")

if not api_key:
    raise SystemExit("Set PATENTE_API_KEY before running this example.")

payload = {
  "patente": [
    "AB123CD"
  ],
  "jurisdiccion": [
    "pba",
    "caba"
  ]
}

request = urllib.request.Request(
    api_base,
    data=json.dumps(payload).encode("utf-8"),
    method="POST",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Idempotency-Key": idempotency_key,
        "x-token": x_token,
    },
)

try:
    with urllib.request.urlopen(request, timeout=30) as response:
        print(response.status)
        print(response.read().decode("utf-8"))
except urllib.error.HTTPError as error:
    print(error.code)
    print(error.read().decode("utf-8"))
