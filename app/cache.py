from __future__ import annotations
import hashlib
import json
import time
from pathlib import Path
from typing import Any

CACHE_DIR = Path(".cache")
TTL_SECONDS = 60 * 60 * 6

def _path(namespace: str, key: str) -> Path:
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
    CACHE_DIR.mkdir(exist_ok=True)
    return CACHE_DIR / f"{namespace}_{digest}.json"

def get(namespace: str, key: str) -> Any | None:
    path = _path(namespace, key)
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        if time.time() - payload["created_at"] > TTL_SECONDS:
            path.unlink(missing_ok=True)
            return None
        return payload["value"]
    except (OSError, KeyError, json.JSONDecodeError):
        return None

def set(namespace: str, key: str, value: Any) -> None:
    path = _path(namespace, key)
    path.write_text(
        json.dumps({"created_at": time.time(), "value": value}),
        encoding="utf-8",
    )
