import crypto from "node:crypto";

export function verifyPatenteWebhook({ rawBody, timestamp, signatureHeader, secret, toleranceSeconds = 300 }) {
  if (!rawBody || !timestamp || !signatureHeader || !secret) return false;
  const now = Math.floor(Date.now() / 1000);
  const ts = Number(timestamp);
  if (!Number.isFinite(ts) || Math.abs(now - ts) > toleranceSeconds) return false;

  const expected = crypto
    .createHmac("sha256", secret)
    .update(`${timestamp}.${rawBody}`)
    .digest("hex");

  const received = signatureHeader.startsWith("v1=")
    ? signatureHeader.slice(3)
    : signatureHeader;

  const expectedBuffer = Buffer.from(expected, "hex");
  const receivedBuffer = Buffer.from(received, "hex");
  return expectedBuffer.length === receivedBuffer.length
    && crypto.timingSafeEqual(expectedBuffer, receivedBuffer);
}
