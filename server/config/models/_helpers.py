"""
Shared helpers for config model parsing and validation.

Used by server_db, nats, and other config submodules.
"""

import json
import os
from typing import Any

from ...structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _parse_list_from_string(s: str) -> list[str]:
    """Parse non-empty string as JSON list or CSV. Used by _parse_env_list."""
    try:
        loaded = json.loads(s)
        if isinstance(loaded, list):
            return [str(item).strip() for item in loaded if str(item).strip()]
    except json.JSONDecodeError:
        pass
    return [item.strip() for item in s.split(",") if item.strip()]


def _parse_env_list(candidate: Any) -> list[str]:
    """Parse a string from the environment as JSON list or CSV."""
    if candidate is None:
        return []
    s = str(candidate).strip()
    if not s:
        return []
    return _parse_list_from_string(s)


def _default_cors_origins() -> list[str]:
    """Derive default CORS origins with environment taking precedence."""
    raw = (
        os.getenv("CORS_ALLOW_ORIGINS")
        or os.getenv("CORS_ORIGINS")
        or os.getenv("CORS_ALLOWED_ORIGINS")
        or os.getenv("ALLOWED_ORIGINS")
    )
    parsed = _parse_env_list(raw) if raw is not None else []
    if parsed:
        return parsed
    return ["http://localhost:5173", "http://127.0.0.1:5173"]


def _apply_url_fallback(data: dict[str, Any]) -> None:
    """
    If url is missing, set it from npc_url in data or from DATABASE_* env vars.
    Mutates data in place. Used by DatabaseConfig.ensure_url_set.
    """
    if "url" in data and data.get("url"):
        return
    if "npc_url" in data and data["npc_url"]:
        logger.debug("url missing but npc_url available, using npc_url as url fallback")
        data["url"] = data["npc_url"]
        return
    db_url = os.getenv("DATABASE_URL")
    npc_url = os.getenv("DATABASE_NPC_URL")
    if not db_url and npc_url:
        logger.debug("DATABASE_URL missing but DATABASE_NPC_URL available, using as fallback")
        data["url"] = npc_url


def _validate_tls_files_and_maybe_update_url(config: Any) -> None:
    """
    When TLS is enabled, validate cert/key (and optional CA) exist and update url to tls://.
    Raises ValueError on missing/invalid files. Mutates config.url if it starts with nats://.
    """
    from pathlib import Path

    if not config.tls_cert_file or not config.tls_key_file:
        logger.error(
            "TLS enabled but certificate or key file not provided",
            cert_file=config.tls_cert_file,
            key_file=config.tls_key_file,
        )
        raise ValueError("TLS certificate and key files are required when TLS is enabled")
    cert_path = Path(config.tls_cert_file)
    key_path = Path(config.tls_key_file)
    if not cert_path.exists():
        raise ValueError(f"TLS certificate file not found: {config.tls_cert_file}")
    if not key_path.exists():
        raise ValueError(f"TLS key file not found: {config.tls_key_file}")
    if config.tls_ca_file:
        ca_path = Path(config.tls_ca_file)
        if not ca_path.exists():
            raise ValueError(f"TLS CA file not found: {config.tls_ca_file}")
    if config.url.startswith("nats://"):
        logger.info("TLS enabled, updating URL scheme to tls://", old_url=config.url)
        config.url = config.url.replace("nats://", "tls://", 1)
