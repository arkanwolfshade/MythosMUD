"""
Shared utilities for container and bundles.

Holds helpers extracted from ApplicationContainer per Phase 2 migration.
"""

import json
from json import JSONDecodeError
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def decode_json_column(value: Any, expected_type: type) -> Any:
    """
    Decode a JSON column value, returning the type's default on failure.

    Used by GameBundle item initialization and exposed on ApplicationContainer
    for backward compatibility.
    """
    result: Any
    if value is None or not value:
        result = expected_type()
    elif isinstance(value, (list, dict)):
        result = value
    else:
        try:
            decoded = json.loads(value)
            if isinstance(decoded, expected_type):
                result = decoded
            elif expected_type is list:
                result = list(decoded)
            elif expected_type is dict:
                result = dict(decoded)
            else:
                result = decoded
        except JSONDecodeError:
            logger.warning("Failed to decode JSON column; using default value", column_value=value)
            result = expected_type()
    return result


def normalize_path_from_url_or_path(raw: str, project_root: Path) -> Path | None:
    """
    Normalize an item database override into a filesystem path.

    DEPRECATED: Items are now stored in PostgreSQL. Kept for backward compatibility.
    """
    try:
        if "://" in raw:
            parsed = urlparse(raw)
            if parsed.scheme.startswith("postgresql"):
                logger.warning(
                    "Item database override with PostgreSQL URL is not supported - items are in PostgreSQL",
                    url=raw,
                )
                return None
            return Path(parsed.path or "").resolve() if parsed.path else None

        path = Path(raw)
        if not path.is_absolute():
            path = (project_root / path).resolve()
        return path
    except (ValueError, OSError) as exc:
        logger.error("Failed to normalize item database override", override=raw, error=str(exc))
        return None
