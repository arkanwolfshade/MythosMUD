"""Helper functions for container persistence operations."""

import json
from datetime import datetime
from typing import Any
from uuid import UUID

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

from ..exceptions import DatabaseError, ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise

logger = get_logger(__name__)


def parse_jsonb_column(value: Any, default: Any) -> Any:
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


def fetch_container_items(conn: Any, container_id: UUID) -> list[dict[str, Any]]:
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
    # Convert UUID to string for psycopg2 compatibility
    container_id_str = str(container_id) if isinstance(container_id, UUID) else container_id
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
        (container_id_str,),
    )
    rows = cursor.fetchall()
    cursor.close()

    items = []
    for row in rows:
        # Ensure row is a dictionary (RealDictCursor should guarantee this, but be defensive)
        if not isinstance(row, dict):
            logger.warning(
                "Skipping non-dictionary row in container_contents query",
                container_id=str(container_id),
                row_type=type(row).__name__,
                row=str(row)[:100],
            )
            continue

        # Ensure all required fields are present and of correct type
        item_instance_id = row.get("item_instance_id")
        item_id = row.get("item_id")
        item_name = row.get("item_name")
        quantity = row.get("quantity")
        condition = row.get("condition")
        position = row.get("position")

        # Skip if critical fields are missing
        if not item_instance_id:
            logger.warning(
                "Skipping row with missing item_instance_id",
                container_id=str(container_id),
                row_keys=list(row.keys()) if isinstance(row, dict) else None,
            )
            continue

        # Parse metadata if it's a string
        metadata = row.get("metadata")
        if isinstance(metadata, str):
            try:
                metadata = json.loads(metadata)
            except (json.JSONDecodeError, ValueError):
                metadata = {}
        elif metadata is None:
            metadata = {}
        elif not isinstance(metadata, dict):
            metadata = {}

        item: dict[str, Any] = {
            "item_instance_id": str(item_instance_id) if item_instance_id else None,
            "item_id": str(item_id) if item_id else None,
            "item_name": str(item_name) if item_name else "Unknown Item",
            "quantity": int(quantity) if quantity is not None else 1,
            "condition": str(condition) if condition else "pristine",
            "position": int(position) if position is not None else 0,
            "metadata": metadata,
            "slot_type": "backpack",  # Container items need slot_type for inventory validation
        }
        items.append(item)

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


def update_container_items(cursor: Any, container_id_str: str, items_json: list[dict[str, Any]], conn: Any) -> None:
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
                ensure_item_instance(
                    conn,
                    item_instance_id=item_instance_id,
                    prototype_id=prototype_id,
                    owner_type="container",
                    owner_id=container_id_str,
                    quantity=item.get("quantity", 1),
                    metadata=item.get("metadata", {}),
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


def build_update_query(
    updates: list[str], params: list[Any], container_id_str: str, current_time: datetime
) -> sql.Composed:
    """
    Build SQL update query for container.

    Args:
        updates: List of update clauses
        params: List of parameters
        container_id_str: Container ID as string
        current_time: Current timestamp

    Returns:
        SQL query object
    """
    updates.append("updated_at = %s")
    params.append(current_time)
    params.append(container_id_str)

    set_clauses = sql.SQL(", ").join([sql.SQL(clause) for clause in updates])
    query = sql.SQL("""
        UPDATE containers
        SET {}
        WHERE container_instance_id = %s
        RETURNING container_instance_id
    """).format(set_clauses)

    return query
