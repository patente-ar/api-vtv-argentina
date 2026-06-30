#!/usr/bin/env python3
import hashlib
import hmac
import time


def verify_patente_webhook(raw_body: bytes, timestamp: str, signature_header: str, secret: str, tolerance_seconds: int = 300) -> bool:
    if not raw_body or not timestamp or not signature_header or not secret:
        return False

    try:
        ts = int(timestamp)
    except ValueError:
        return False

    if abs(int(time.time()) - ts) > tolerance_seconds:
        return False

    received = signature_header[3:] if signature_header.startswith("v1=") else signature_header
    signed_payload = timestamp.encode("utf-8") + b"." + raw_body
    expected = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, received)
