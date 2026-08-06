"""Row coercion, validation, and content-fetch helpers for container persistence."""

from __future__ import annotations

import json
from datetime import datetime
from typing import cast
from uuid import UUID

from psycopg2.extensions import connection as PsycopgConnection
from psycopg2.extras import RealDictCursor

from ..exceptions import ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise

logger = get_logger(__name__)


def validate_create_container_args(source_type: str, capacity_slots: int, lock_state: str) -> None:
    """Validate create_container scalars before any DB work."""
    if source_type not in ("environment", "equipment", "corpse"):
        log_and_raise(
            ValidationError,
            f"Invalid source_type: {source_type}. Must be 'environment', 'equipment', or 'corpse'",
            operation="create_container",
            source_type=source_type,
            details={"source_type": source_type},
            user_friendly="Invalid container type",
        )
    if capacity_slots < 1 or capacity_slots > 20:
        log_and_raise(
            ValidationError,
            f"Invalid capacity_slots: {capacity_slots}. Must be between 1 and 20",
            operation="create_container",
            source_type=source_type,
            capacity_slots=capacity_slots,
            details={"capacity_slots": capacity_slots},
            user_friendly="Invalid container capacity",
        )
    if lock_state not in ("unlocked", "locked", "sealed"):
        log_and_raise(
            ValidationError,
            f"Invalid lock_state: {lock_state}. Must be 'unlocked', 'locked', or 'sealed'",
            operation="create_container",
            source_type=source_type,
            lock_state=lock_state,
            details={"lock_state": lock_state},
            user_friendly="Invalid lock state",
        )


def validate_update_lock_state(lock_state: str | None, container_id: UUID) -> None:
    """Raise ValidationError when lock_state is set and invalid."""
    if lock_state is None or lock_state in ("unlocked", "locked", "sealed"):
        return
    log_and_raise(
        ValidationError,
        f"Invalid lock_state: {lock_state}. Must be 'unlocked', 'locked', or 'sealed'",
        operation="update_container",
        container_id=str(container_id),
        lock_state=lock_state,
        details={"lock_state": lock_state},
        user_friendly="Invalid lock state",
    )


def as_uuid(value: object) -> UUID:
    if isinstance(value, UUID):
        return value
    return UUID(str(value))


def as_opt_uuid(value: object) -> UUID | None:
    if value is None:
        return None
    if isinstance(value, UUID):
        return value
    return UUID(str(value))


def as_opt_str(value: object) -> str | None:
    if value is None:
        return None
    return str(value)


def as_opt_datetime(value: object) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    return None


def int_from_row(value: object, default: int) -> int:
    if isinstance(value, bool):
        return default
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return default
    if isinstance(value, float):
        return int(value)
    return default


def opt_int_from_row(value: object) -> int | None:
    if value is None:
        return None
    return int_from_row(value, 0)


def _coerce_item_quantity(value: object) -> int:
    if isinstance(value, bool):
        return 1
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value.strip())
        except ValueError:
            return 1
    if isinstance(value, float):
        return int(value)
    return 1


def parse_jsonb_column(value: object, default: object) -> object:
    """
    Parse a JSONB column value from database.

    JSONB columns may be returned as:
    - Python objects (dict/list) when using RealDictCursor
    - Strings that need parsing
    - None values

    Args:
        value: The JSONB column value from database
        default: Default value if value is None or empty

    Returns:
        Parsed Python object (dict/list) or default value
    """
    if value is None:
        return default
    if isinstance(value, str):
        return cast(object, json.loads(value)) if value else default
    # Already a Python object (dict/list)
    return value if value else default


def allowed_roles_from_row(value: object) -> list[str]:
    """Parse allowed_roles JSONB column into a list of role strings."""
    parsed = parse_jsonb_column(value, [])
    if isinstance(parsed, list):
        return [str(x) for x in cast(list[object], parsed)]
    return []


def metadata_from_row(value: object) -> dict[str, object]:
    parsed = parse_jsonb_column(value, {})
    if isinstance(parsed, dict):
        return cast(dict[str, object], parsed)
    return {}


def _normalize_container_item_metadata(metadata: object) -> dict[str, object]:
    """Normalize item metadata from DB (string JSONB, dict, or other) to a dict."""
    if isinstance(metadata, dict):
        return cast(dict[str, object], metadata)
    if isinstance(metadata, str):
        try:
            parsed = cast(object, json.loads(metadata))
        except (json.JSONDecodeError, ValueError):
            return {}
        return cast(dict[str, object], parsed) if isinstance(parsed, dict) else {}
    return {}


def _map_container_content_row(row: object, container_id: UUID) -> dict[str, object] | None:
    """Validate and map a container_contents join row to items_json shape."""
    if not isinstance(row, dict):
        logger.warning(
            "Skipping non-dictionary row in container_contents query",
            container_id=str(container_id),
            row_type=type(row).__name__,
            row=str(row)[:100],
        )
        return None

    row_dict = cast(dict[str, object], row)
    item_instance_id = row_dict.get("item_instance_id")
    if not item_instance_id:
        logger.warning(
            "Skipping row with missing item_instance_id",
            container_id=str(container_id),
            row_keys=list(row_dict.keys()),
        )
        return None

    item_id = row_dict.get("item_id")
    item_name = row_dict.get("item_name")
    quantity = row_dict.get("quantity")
    condition = row_dict.get("condition")
    position = row_dict.get("position")
    return {
        "item_instance_id": str(item_instance_id),
        "item_id": str(item_id) if item_id else None,
        "item_name": str(item_name) if item_name else "Unknown Item",
        "quantity": 1 if quantity is None else _coerce_item_quantity(quantity),
        "condition": str(condition) if condition else "pristine",
        "position": 0 if position is None else _coerce_item_quantity(position),
        "metadata": _normalize_container_item_metadata(row_dict.get("metadata")),
    }


def fetch_container_items(conn: PsycopgConnection, container_id: UUID) -> list[dict[str, object]]:
    """
    Fetch container items directly from normalized tables.

    Queries container_contents JOIN item_instances JOIN item_prototypes
    to build the items list without using stored procedures.

    Args:
        conn: Database connection
        container_id: Container UUID

    Returns:
        List of item dictionaries matching the old items_json format
    """
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        """
        SELECT
            cc.item_instance_id,
            ii.prototype_id as item_id,
            COALESCE(ii.custom_name, ip.name) as item_name,
            ii.quantity,
            ii.condition,
            ii.metadata,
            cc.position
        FROM container_contents cc
        JOIN item_instances ii ON cc.item_instance_id = ii.item_instance_id
        JOIN item_prototypes ip ON ii.prototype_id = ip.prototype_id
        WHERE cc.container_id = %s
        ORDER BY cc.position
        """,
        (container_id,),
    )
    rows = cast(list[object], cursor.fetchall())
    cursor.close()

    items: list[dict[str, object]] = []
    for row in rows:
        item = _map_container_content_row(row, container_id)
        if item is not None:
            items.append(item)
    return items
