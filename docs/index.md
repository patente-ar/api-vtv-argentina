# API de VTV en Argentina

[![Docs](https://img.shields.io/badge/docs-patente.ar-0A66C2)](https://patente.ar/api-vtv)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-public%20docs-181717)](https://patente-ar.github.io/api-vtv-argentina/)
[![Argentina](https://img.shields.io/badge/market-Argentina-38BDF8)](https://patente.ar)
[![Endpoint](https://img.shields.io/badge/endpoint-POST%20%2Fv1%2Fconsultas-111827)](https://patente.ar/api-vtv)
[![Payload](https://img.shields.io/badge/payload-JSON-334155)](../openapi/openapi.yaml)
[![Auth](https://img.shields.io/badge/auth-Bearer%20API%20key-2563EB)](#request)
[![Webhooks](https://img.shields.io/badge/webhooks-HMAC%20SHA--256-7C3AED)](#webhooks)
[![Idempotency](https://img.shields.io/badge/idempotency-Idempotency--Key-059669)](#request)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1-16A34A)](../openapi/openapi.yaml)
[![Examples](https://img.shields.io/badge/examples-curl%20%7C%20Node.js%20%7C%20Python-F97316)](#inicio-rapido)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](../LICENSE)

Automatiza control de VTV por patente para bloquear operaciones riesgosas, ordenar vencimientos y alimentar sistemas internos con datos verificables.

Este kit publico esta escrito para busquedas tecnicas y comerciales como "API VTV Argentina", "API de VTV en Argentina", "API patente Argentina", "consulta por patente API" e "integracion vehicular Argentina".

## Inicio rapido

- Endpoint: `https://api.patente.ar/v1/consultas`
- Producto: `vtv`
- Entrada: `plate`
- Ejemplo: `AB123CD`
- OpenAPI: [openapi.yaml](../openapi/openapi.yaml)
- Ejemplos: [curl](../examples/curl/consulta.sh), [Node.js](../examples/node/consulta.mjs), [Python](../examples/python/consulta.py)

## Casos de uso

- Flotas.
- Seguros.
- Rentadoras.
- Turnos.
- Documentacion.

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

## Webhooks

Los resultados asincronicos pueden recibirse por webhook firmado con HMAC SHA-256. Guardar `requestId`, validar `x-patente-signature` y usar `Idempotency-Key` para reintentos seguros.

## Confianza operativa

- Entrada por patente argentina normalizada.
- Soporte para jurisdicciones VTV configuradas por cuenta.
- Webhooks firmados y ejemplos listos para backend.



## Links

- Producto comercial: [https://patente.ar/api-vtv](https://patente.ar/api-vtv)
- Sitio principal: [https://patente.ar](https://patente.ar)
- Repositorio: [https://github.com/patente-ar/api-vtv-argentina](https://github.com/patente-ar/api-vtv-argentina)
