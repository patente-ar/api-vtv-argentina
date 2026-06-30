# API de VTV en Argentina

[![API examples](https://img.shields.io/badge/API-examples-blue)](https://patente.ar/api-vtv)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1-green)](./openapi/openapi.yaml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Ejemplos de integracion para api de vtv en argentina usando la API de [patente.ar](https://patente.ar).

La API publica usa un unico endpoint:

```text
POST https://api.patente.ar/v1/consultas
```

El producto queda definido por la API key emitida para `vtv`. Este repositorio contiene ejemplos, contrato OpenAPI, manejo de idempotencia y verificacion de webhooks para integrar API VTV Argentina.

## Para que sirve

- flotas.
- seguros.
- rentadoras.
- turnos.
- documentacion.

## Inicio rapido

1. Pedir una API key desde [patente.ar](https://patente.ar/api-vtv).
2. Copiar `.env.example` como `.env`.
3. Ejecutar un ejemplo:

```bash
export PATENTE_API_KEY="pa_live_xxx"
./examples/curl/consulta.sh
node examples/node/consulta.mjs
python3 examples/python/consulta.py
```

## Request

```http
POST /v1/consultas HTTP/1.1
Host: api.patente.ar
Authorization: Bearer pa_live_xxx
Content-Type: application/json
Idempotency-Key: orden-externa-001
x-token: orden-externa-001
```

```json
{
  "patente": [
    "AB123CD"
  ],
  "jurisdiccion": [
    "pba",
    "caba"
  ]
}
```

## Response aceptada

```json
{
  "code": 202,
  "status": "accepted",
  "message": "La solicitud fue aceptada y se procesara en breve.",
  "requestId": "req_01HZX...",
  "timestamp": "2026-06-30T12:00:00.000Z"
}
```

## Webhooks

Cuando el resultado esta disponible, patente.ar puede enviar un `POST` al webhook configurado para la API key.

Headers relevantes:

- `x-patente-timestamp`
- `x-patente-signature`
- `x-patente-request-id`
- `x-patente-api-key`
- `x-token` si fue enviado en el request original

La firma usa HMAC SHA-256 sobre:

```text
timestamp.raw_body
```

Ver ejemplos en:

- [Node.js](./webhooks/node/verify-signature.mjs)
- [Python](./webhooks/python/verify_signature.py)

## Errores frecuentes

| Codigo | Causa | Accion |
| --- | --- | --- |
| 401 | API key ausente, revocada o invalida | Rotar o revisar la key en patente.ar |
| 402 | Creditos insuficientes | Cargar saldo o cambiar el producto contratado |
| 409 | Idempotencia ya en curso | Reusar el `requestId` previo o cambiar `Idempotency-Key` |
| 422 | Payload fuera de contrato | Revisar el ejemplo y normalizar la entrada |
| 429 | Rate limit | Reintentar con backoff |

## Links

- Producto: [https://patente.ar/api-vtv](https://patente.ar/api-vtv)
- Patente.ar: [https://patente.ar](https://patente.ar)
- Documentacion OpenAPI: [openapi/openapi.yaml](./openapi/openapi.yaml)

## Licencia

MIT. Este repositorio contiene ejemplos de integracion; no incluye credenciales ni codigo backend de patente.ar.
