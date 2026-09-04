"""Helper functions for container persistence operations."""

import json
from typing import cast
from uuid import UUID

from psycopg2.extensions import connection as PsycopgConnection
from psycopg2.extensions import cursor as PsycopgCursor
from psycopg2.extras import RealDictCursor
from structlog.stdlib import BoundLogger

from ..exceptions import DatabaseError, ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise
from ..utils.int_coercion import coerce_int

logger: BoundLogger = get_logger(__name__)

# Column list shared by every containers.sql read procedure that returns a full container row
# (get_container, get_containers_by_room_id, get_containers_by_entity_id, get_decayed_containers)
# -- kept as one constant so the four call sites (container_persistence.py,
# container_query_helpers.py) can't drift, and so none of them writes a bare "SELECT *" (the raw-SQL
# lint guard flags that unconditionally, #633).
CONTAINER_ROW_COLUMNS = (
    "container_instance_id, source_type, owner_id, room_id, entity_id, lock_state, "
    "capacity_slots, weight_limit, decay_at, allowed_roles, metadata_json, created_at, "
    "updated_at, container_item_instance_id"
)


def _coerce_row_quantity(value: object) -> int:
    """Normalize quantity/position from DB row cells; bool -> 1 (not coerce_int(False)==0)."""
    if isinstance(value, bool):
        return 1
    return coerce_int(value, default=1)


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
        return json.loads(value) if value else default
    # Already a Python object (dict/list)
    return value if value else default


# Backed by db/procedures/containers.sql's fetch_container_items() (#633).
_FETCH_CONTAINER_ITEMS_SQL = (
    'SELECT item_instance_id, item_id, item_name, quantity, condition, metadata, "position" '
    "FROM fetch_container_items(%s)"
)


def _metadata_dict_from_cell(md_raw: object | None) -> dict[str, object]:
    if isinstance(md_raw, str):
        try:
            loaded = cast(object, json.loads(md_raw))
            return cast(dict[str, object], loaded) if isinstance(loaded, dict) else {}
        except (json.JSONDecodeError, ValueError):
            return {}
    if isinstance(md_raw, dict):
        return cast(dict[str, object], md_raw)
    return {}


def _item_dict_from_contents_row(row: dict[str, object], container_id: UUID) -> dict[str, object] | None:
    item_instance_id: object | None = row.get("item_instance_id")
    if not item_instance_id:
        logger.warning(
            "Skipping row with missing item_instance_id",
            container_id=str(container_id),
            row_keys=list(row.keys()),
        )
        return None

    item_id: object | None = row.get("item_id")
    item_name: object | None = row.get("item_name")
    quantity: object | None = row.get("quantity")
    condition: object | None = row.get("condition")
    position: object | None = row.get("position")
    meta_out = _metadata_dict_from_cell(row.get("metadata"))

    return {
        "item_instance_id": str(item_instance_id) if item_instance_id else None,
        "item_id": str(item_id) if item_id else None,
        "item_name": str(item_name) if item_name else "Unknown Item",
        "quantity": 1 if quantity is None else _coerce_row_quantity(quantity),
        "condition": str(condition) if condition else "pristine",
        "position": 0 if position is None else _coerce_row_quantity(position),
        "metadata": meta_out,
        # Items pulled from containers re-enter general inventory, not an equipped wearable slot.
        "slot_type": "inventory",
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
    container_id_str = str(container_id)
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(_FETCH_CONTAINER_ITEMS_SQL, (container_id_str,))
    rows_raw: list[object] = cast(list[object], cursor.fetchall())
    cursor.close()

    items: list[dict[str, object]] = []
    for row_raw in rows_raw:
        if not isinstance(row_raw, dict):
            logger.warning(
                "Skipping non-dictionary row in container_contents query",
                container_id=str(container_id),
                row_type=type(row_raw).__name__,
                row=str(row_raw)[:100],
            )
            continue
        row = cast(dict[str, object], row_raw)
        built = _item_dict_from_contents_row(row, container_id)
        if built is not None:
            items.append(built)

    return items


def validate_lock_state(lock_state: str | None) -> None:
    """
    Validate lock_state parameter.

    Args:
        lock_state: Lock state to validate

    Raises:
        ValidationError: If lock_state is invalid
    """
    if lock_state is not None and lock_state not in ("unlocked", "locked", "sealed"):
        log_and_raise(
            ValidationError,
            f"Invalid lock_state: {lock_state}. Must be 'unlocked', 'locked', or 'sealed'",
            operation="validate_lock_state",
            lock_state=lock_state,
            details={"lock_state": lock_state},
            user_friendly="Invalid lock state",
        )


def update_container_items(
    cursor: PsycopgCursor,
    container_id_str: str,
    items_json: list[dict[str, object]],
    conn: PsycopgConnection,
) -> None:
    """
    Update container items using stored procedures.

    Args:
        cursor: Database cursor
        container_id_str: Container ID as string
        items_json: List of items to add
        conn: Database connection
    """
    cursor.execute("SELECT clear_container_contents(%s)", (container_id_str,))

    from .item_instance_persistence import ensure_item_instance

    for position, item in enumerate(items_json):
        item_instance_id = item.get("item_instance_id")
        prototype_id = item.get("item_id") or item.get("prototype_id")

        if item_instance_id and prototype_id:
            try:
                qty = _coerce_row_quantity(item.get("quantity", 1))
                md_raw: object = item.get("metadata", {})
                md: dict[str, object] = cast(dict[str, object], md_raw) if isinstance(md_raw, dict) else {}
                ensure_item_instance(
                    conn,
                    item_instance_id=str(item_instance_id),
                    prototype_id=str(prototype_id),
                    options={
                        "owner_type": "container",
                        "owner_id": container_id_str,
                        "quantity": qty,
                        "metadata": md,
                    },
                )
            except (DatabaseError, ValidationError) as e:
                logger.warning(
                    "Failed to ensure item instance exists, skipping item",
                    item_instance_id=item_instance_id,
                    prototype_id=prototype_id,
                    error=str(e),
                )
                continue

            cursor.execute(
                "SELECT add_item_to_container(%s, %s, %s)",
                (container_id_str, item_instance_id, position),
            )
