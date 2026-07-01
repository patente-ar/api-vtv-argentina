# API de VTV en Argentina

[![Docs](https://img.shields.io/badge/docs-patente.ar-0A66C2)](https://patente.ar/api-vtv)
[![Playground](https://img.shields.io/badge/playground-probar%20API-7C3AED)](https://patente.ar/desarrolladores/api?tab=playground)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-3.1-16A34A)](./openapi/openapi.yaml)
[![Webhooks](https://img.shields.io/badge/webhooks-HMAC%20SHA--256-7C3AED)](#webhooks)
[![Examples](https://img.shields.io/badge/examples-curl%20%7C%20Node.js%20%7C%20Python-F97316)](#inicio-rapido)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

> Automatiza control de VTV por patente para bloquear operaciones riesgosas, ordenar vencimientos y alimentar sistemas internos con datos verificables.

Este repo no es un SDK ni un wrapper instalable. Es un kit publico de integracion para equipos que quieren evaluar la API de patente.ar antes de conectarla a un CRM, ERP, backoffice, marketplace, seguro o flujo de flota.

**patente.ar** centraliza APIs vehiculares para Argentina: consultas por patente o VIN, procesamiento asincronico, trazabilidad por request y documentacion pensada para equipos de producto, datos y operaciones.

## Que resuelve

- Entrada por patente argentina normalizada.
- Soporte para jurisdicciones VTV configuradas por cuenta.
- Webhooks firmados y ejemplos listos para backend.

## Lo que trae

| Pieza | Para que sirve |
| --- | --- |
| `README.md` | Guia comercial y tecnica para integrar API VTV Argentina. |
| `openapi/openapi.yaml` | Contrato OpenAPI 3.1 para documentacion, SDKs o pruebas. |
| `examples/curl/consulta.sh` | Prueba rapida desde terminal. |
| `examples/node/consulta.mjs` | Ejemplo Node.js con `fetch`. |
| `examples/python/consulta.py` | Ejemplo Python sin dependencias externas. |
| `webhooks/*` | Verificacion HMAC SHA-256 de webhooks de patente.ar. |
| `.github/workflows/validate.yml` | Validacion de sintaxis para ejemplos. |

## Endpoint

```text
POST https://api.patente.ar/v1/consultas
```

El producto queda definido por la API key emitida para `vtv`. No hace falta inventar rutas como `/v1/multas` o `/v1/vtv`: el contrato publico se mantiene estable en `POST /v1/consultas`.

## Para que sirve

- Flotas.
- Seguros.
- Rentadoras.
- Turnos.
- Documentacion.

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

La respuesta puede ser inmediata o asincronica. Cuando queda en proceso, patente.ar responde con `202 accepted` y un `requestId`; el resultado final puede llegar por webhook.

## Activar API y probar en Playground

Para probar API VTV Argentina sin armar un backend desde cero, crea una cuenta en patente.ar, pedi habilitar la API `vtv` y usa el Playground para ejecutar requests con API keys, payloads de ejemplo, idempotencia, webhooks y logs.

| Paso | Link | Que hacer |
| --- | --- | --- |
| 1 | [Crear cuenta en patente.ar](https://patente.ar/registro) | Registrar la cuenta de empresa o equipo que va a consumir la API. |
| 2 | [Pedir habilitacion de la API](https://patente.ar/contacto?asunto=Habilitar%20API%20vtv) | Solicitar que activen el producto `vtv` y el esquema de creditos. |
| 3 | [Abrir el Playground](https://patente.ar/desarrolladores/api?tab=playground) | Probar payloads reales de integracion, revisar respuestas y validar webhooks sin publicar credenciales. |
| 4 | [Pasar a produccion](https://patente.ar/api-vtv) | Configurar API keys, webhook firmado, idempotencia y trazabilidad por `requestId`. |

El Playground requiere iniciar sesion y tener el modulo API habilitado para la cuenta. Si todavia no aparece, pedi la habilitacion desde el link anterior.


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

## Checklist de produccion

- Usar `Idempotency-Key` en todos los reintentos.
- Guardar `requestId` y `x-token` para conciliacion.
- Validar `x-patente-signature` antes de procesar webhooks.
- Reintentar `429` y errores temporales con backoff.
- No registrar API keys, webhook secrets ni payloads sensibles en logs.

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
- Crear cuenta: [https://patente.ar/registro](https://patente.ar/registro)
- Habilitar API: [https://patente.ar/contacto?asunto=Habilitar%20API%20vtv](https://patente.ar/contacto?asunto=Habilitar%20API%20vtv)
- Playground: [https://patente.ar/desarrolladores/api?tab=playground](https://patente.ar/desarrolladores/api?tab=playground)
- Patente.ar: [https://patente.ar](https://patente.ar)
- Documentacion OpenAPI: [openapi/openapi.yaml](./openapi/openapi.yaml)

## Licencia

MIT. Este repositorio contiene ejemplos de integracion; no incluye credenciales ni codigo backend de patente.ar.
