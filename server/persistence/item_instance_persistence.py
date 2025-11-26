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

from ..exceptions import DatabaseError, ValidationError
from ..logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


def create_item_instance(
    conn: Any,
    item_instance_id: str,
    prototype_id: str,
    owner_type: str = "room",
    owner_id: str | None = None,
    location_context: str | None = None,
    quantity: int = 1,
    condition: int | None = None,
    flags_override: list[str] | None = None,
    binding_state: str | None = None,
    attunement_state: dict[str, Any] | None = None,
    custom_name: str | None = None,
    metadata: dict[str, Any] | None = None,
    origin_source: str | None = None,
    origin_metadata: dict[str, Any] | None = None,
) -> None:
    """
    Create a new item instance in the database.

    Args:
        conn: Database connection
        item_instance_id: Unique identifier for the item instance
        prototype_id: Reference to item_prototypes.prototype_id
        owner_type: Type of owner (e.g., "room", "player", "container")
        owner_id: ID of the owner (optional)
        location_context: Additional location context (optional)
        quantity: Quantity of items in this instance
        condition: Item condition (optional)
        flags_override: Override flags for this instance (optional)
        binding_state: Binding state (optional)
        attunement_state: Attunement state dictionary (optional)
        custom_name: Custom name for this instance (optional)
        metadata: Additional metadata dictionary (optional)
        origin_source: Origin source string (optional)
        origin_metadata: Origin metadata dictionary (optional)

    Raises:
        DatabaseError: If the insert fails
        ValidationError: If required parameters are invalid
    """
    if not item_instance_id:
        context = create_error_context()
        context.metadata["operation"] = "create_item_instance"
        log_and_raise(
            ValidationError,
            "item_instance_id is required",
            context=context,
            user_friendly="Invalid item instance data",
        )

    if not prototype_id:
        context = create_error_context()
        context.metadata["operation"] = "create_item_instance"
        log_and_raise(
            ValidationError,
            "prototype_id is required",
            context=context,
            user_friendly="Invalid item instance data",
        )

    cursor = conn.cursor()
    try:
        cursor.execute(
            """
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
            """,
            (
                item_instance_id,
                prototype_id,
                owner_type,
                owner_id,
                location_context,
                quantity,
                condition,
                json.dumps(flags_override or []),
                binding_state,
                json.dumps(attunement_state or {}),
                custom_name,
                json.dumps(metadata or {}),
                origin_source,
                json.dumps(origin_metadata or {}),
            ),
        )
        conn.commit()
        logger.debug(
            "Item instance created",
            item_instance_id=item_instance_id,
            prototype_id=prototype_id,
            owner_type=owner_type,
            owner_id=owner_id,
        )
    except psycopg2.IntegrityError as e:
        conn.rollback()
        context = create_error_context()
        context.metadata["operation"] = "create_item_instance"
        context.metadata["item_instance_id"] = item_instance_id
        context.metadata["prototype_id"] = prototype_id
        log_and_raise(
            DatabaseError,
            f"Database error creating item instance: {str(e)}",
            context=context,
            details={"error": str(e), "item_instance_id": item_instance_id, "prototype_id": prototype_id},
            user_friendly="Failed to create item instance",
        )
    except psycopg2.Error as e:
        conn.rollback()
        context = create_error_context()
        context.metadata["operation"] = "create_item_instance"
        context.metadata["item_instance_id"] = item_instance_id
        log_and_raise(
            DatabaseError,
            f"Database error creating item instance: {str(e)}",
            context=context,
            details={"error": str(e), "item_instance_id": item_instance_id},
            user_friendly="Failed to create item instance",
        )
    finally:
        cursor.close()


def get_item_instance(conn: Any, item_instance_id: str) -> dict[str, Any] | None:
    """
    Retrieve an item instance by ID.

    Args:
        conn: Database connection
        item_instance_id: Unique identifier for the item instance

    Returns:
        Dictionary with item instance data, or None if not found
    """
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
    """
    Check if an item instance exists in the database.

    Args:
        conn: Database connection
        item_instance_id: Unique identifier for the item instance

    Returns:
        True if the item instance exists, False otherwise
    """
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
    owner_type: str = "room",
    owner_id: str | None = None,
    quantity: int = 1,
    metadata: dict[str, Any] | None = None,
    origin_source: str | None = None,
    origin_metadata: dict[str, Any] | None = None,
) -> None:
    """
    Ensure an item instance exists in the database, creating it if necessary.

    This is a convenience function that checks if the item instance exists
    and creates it if it doesn't. Useful for ensuring referential integrity.

    Args:
        conn: Database connection
        item_instance_id: Unique identifier for the item instance
        prototype_id: Reference to item_prototypes.prototype_id
        owner_type: Type of owner (default: "room")
        owner_id: ID of the owner (optional)
        quantity: Quantity of items in this instance (default: 1)
        metadata: Additional metadata dictionary (optional)
        origin_source: Origin source string (optional)
        origin_metadata: Origin metadata dictionary (optional)
    """
    if not item_instance_exists(conn, item_instance_id):
        create_item_instance(
            conn=conn,
            item_instance_id=item_instance_id,
            prototype_id=prototype_id,
            owner_type=owner_type,
            owner_id=owner_id,
            quantity=quantity,
            metadata=metadata,
            origin_source=origin_source,
            origin_metadata=origin_metadata,
        )
        logger.debug(
            "Item instance ensured (created)",
            item_instance_id=item_instance_id,
            prototype_id=prototype_id,
        )
    else:
        logger.debug(
            "Item instance already exists",
            item_instance_id=item_instance_id,
        )
