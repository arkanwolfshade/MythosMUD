"""
Item instance persistence operations.

As documented in the restricted archives, item instances must be persisted
to the database to maintain referential integrity with containers and other
game systems that reference item instances.
"""

from __future__ import annotations

import json
from typing import Any

import psycopg2
from psycopg2.extras import RealDictCursor

from ..async_persistence_constants import CreateItemInstanceInput, EnsureItemInstanceInput
from ..exceptions import DatabaseError, ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise

logger = get_logger(__name__)

_UPSERT_ITEM_INSTANCE_SQL = """
            INSERT INTO item_instances (
                item_instance_id,
                prototype_id,
                owner_type,
                owner_id,
                location_context,
                quantity,
                condition,
                flags_override,
                binding_state,
                attunement_state,
                custom_name,
                metadata,
                origin_source,
                origin_metadata,
                created_at,
                updated_at
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), NOW()
            )
            ON CONFLICT (item_instance_id) DO UPDATE SET
                prototype_id = EXCLUDED.prototype_id,
                owner_type = EXCLUDED.owner_type,
                owner_id = EXCLUDED.owner_id,
                location_context = EXCLUDED.location_context,
                quantity = EXCLUDED.quantity,
                condition = EXCLUDED.condition,
                flags_override = EXCLUDED.flags_override,
                binding_state = EXCLUDED.binding_state,
                attunement_state = EXCLUDED.attunement_state,
                custom_name = EXCLUDED.custom_name,
                metadata = EXCLUDED.metadata,
                origin_source = EXCLUDED.origin_source,
                origin_metadata = EXCLUDED.origin_metadata,
                updated_at = NOW()
            """


def _item_instance_row_values(
    item_instance_id: str, prototype_id: str, options: CreateItemInstanceInput
) -> tuple[Any, ...]:
    return (
        item_instance_id,
        prototype_id,
        options.get("owner_type", "room"),
        options.get("owner_id"),
        options.get("location_context"),
        options.get("quantity", 1),
        options.get("condition"),
        json.dumps(options.get("flags_override") or []),
        options.get("binding_state"),
        json.dumps(options.get("attunement_state") or {}),
        options.get("custom_name"),
        json.dumps(options.get("metadata") or {}),
        options.get("origin_source"),
        json.dumps(options.get("origin_metadata") or {}),
    )


def _handle_item_instance_db_error(
    conn: Any,
    exc: Exception,
    *,
    item_instance_id: str,
    prototype_id: str | None = None,
) -> None:
    conn.rollback()
    log_and_raise(
        DatabaseError,
        f"Database error creating item instance: {exc}",
        operation="create_item_instance",
        item_instance_id=item_instance_id,
        prototype_id=prototype_id,
        details={"error": str(exc), "item_instance_id": item_instance_id, "prototype_id": prototype_id},
        user_friendly="Failed to create item instance",
    )


def _execute_item_instance_upsert(
    conn: Any,
    item_instance_id: str,
    prototype_id: str,
    options: CreateItemInstanceInput,
) -> None:
    cursor = conn.cursor()
    try:
        cursor.execute(_UPSERT_ITEM_INSTANCE_SQL, _item_instance_row_values(item_instance_id, prototype_id, options))
        conn.commit()
        logger.debug(
            "Item instance created",
            item_instance_id=item_instance_id,
            prototype_id=prototype_id,
            owner_type=options.get("owner_type", "room"),
            owner_id=options.get("owner_id"),
        )
    except psycopg2.IntegrityError as e:
        _handle_item_instance_db_error(conn, e, item_instance_id=item_instance_id, prototype_id=prototype_id)
    except psycopg2.Error as e:
        _handle_item_instance_db_error(conn, e, item_instance_id=item_instance_id)
    finally:
        cursor.close()


def create_item_instance(
    conn: Any,
    item_instance_id: str,
    prototype_id: str,
    options: CreateItemInstanceInput | None = None,
) -> None:
    """Create a new item instance in the database."""
    opts = options or {}
    if not item_instance_id:
        log_and_raise(
            ValidationError,
            "item_instance_id is required",
            operation="create_item_instance",
            user_friendly="Invalid item instance data",
        )
    if not prototype_id:
        log_and_raise(
            ValidationError,
            "prototype_id is required",
            operation="create_item_instance",
            user_friendly="Invalid item instance data",
        )
    _execute_item_instance_upsert(conn, item_instance_id, prototype_id, opts)


def get_item_instance(conn: Any, item_instance_id: str) -> dict[str, Any] | None:
    """Retrieve an item instance by ID."""
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute(
            """
            SELECT
                item_instance_id,
                prototype_id,
                owner_type,
                owner_id,
                location_context,
                quantity,
                condition,
                flags_override,
                binding_state,
                attunement_state,
                custom_name,
                metadata,
                origin_source,
                origin_metadata,
                created_at,
                updated_at
            FROM item_instances
            WHERE item_instance_id = %s
            """,
            (item_instance_id,),
        )
        row = cursor.fetchone()
        if row:
            return dict(row)
        return None
    finally:
        cursor.close()


def item_instance_exists(conn: Any, item_instance_id: str) -> bool:
    """Check if an item instance exists in the database."""
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT 1 FROM item_instances WHERE item_instance_id = %s",
            (item_instance_id,),
        )
        return cursor.fetchone() is not None
    finally:
        cursor.close()


def ensure_item_instance(
    conn: Any,
    item_instance_id: str,
    prototype_id: str,
    options: EnsureItemInstanceInput | None = None,
) -> None:
    """Ensure an item instance exists in the database, creating it if necessary."""
    opts = options or {}
    create_item_instance(
        conn=conn,
        item_instance_id=item_instance_id,
        prototype_id=prototype_id,
        options={
            "owner_type": opts.get("owner_type", "room"),
            "owner_id": opts.get("owner_id"),
            "quantity": opts.get("quantity", 1),
            "metadata": opts.get("metadata"),
            "origin_source": opts.get("origin_source"),
            "origin_metadata": opts.get("origin_metadata"),
        },
    )
    logger.debug(
        "Item instance ensured",
        item_instance_id=item_instance_id,
        prototype_id=prototype_id,
        quantity=opts.get("quantity", 1),
    )
