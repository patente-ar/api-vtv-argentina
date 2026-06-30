const apiBase = process.env.PATENTE_API_BASE_URL ?? "https://api.patente.ar/v1/consultas";
const apiKey = process.env.PATENTE_API_KEY;
const idempotencyKey = process.env.PATENTE_IDEMPOTENCY_KEY ?? "vtv-demo-001";
const xToken = process.env.PATENTE_X_TOKEN ?? "orden-externa-001";

if (!apiKey) {
  throw new Error("Set PATENTE_API_KEY before running this example.");
}

const payload = {
  "patente": [
    "AB123CD"
  ],
  "jurisdiccion": [
    "pba",
    "caba"
  ]
};

const response = await fetch(apiBase, {
  method: "POST",
  headers: {
    "authorization": `Bearer ${apiKey}`,
    "content-type": "application/json",
    "idempotency-key": idempotencyKey,
    "x-token": xToken,
  },
  body: JSON.stringify(payload),
});

const body = await response.json().catch(() => null);
console.log(JSON.stringify({ status: response.status, body }, null, 2));
