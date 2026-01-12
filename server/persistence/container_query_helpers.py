"""Query helper functions for container persistence operations."""

from datetime import UTC, datetime
from typing import Any
from uuid import UUID

import psycopg2
from psycopg2.extras import RealDictCursor

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_error_context, log_and_raise
from .container_data import ContainerData
from .container_helpers import fetch_container_items, parse_jsonb_column

logger = get_logger(__name__)


def _build_container_data_from_row(conn: Any, row: dict[str, Any]) -> ContainerData:
    """
    Build ContainerData object from database row.

    Args:
        conn: Database connection
        row: Database row dictionary

    Returns:
        ContainerData: Container data object
    """
    container_id = row["container_instance_id"]
    items_json = fetch_container_items(conn, container_id)

    return ContainerData(
        container_instance_id=container_id,
        source_type=row["source_type"],
        owner_id=row["owner_id"],
        room_id=row["room_id"],
        entity_id=row["entity_id"],
        lock_state=row["lock_state"],
        capacity_slots=row["capacity_slots"],
        weight_limit=row["weight_limit"],
        decay_at=row["decay_at"],
        allowed_roles=parse_jsonb_column(row["allowed_roles"], []),
        items_json=items_json,
        metadata_json=parse_jsonb_column(row["metadata_json"], {}),
        created_at=row["created_at"],
        updated_at=row["updated_at"],
    )


def get_containers_by_room_id(conn: Any, room_id: str) -> list[ContainerData]:
    """
    Get all containers in a room.

    Args:
        conn: Database connection
        room_id: Room identifier

    Returns:
        list[ContainerData]: List of containers in the room

    Raises:
        DatabaseError: If database operation fails
    """
    context = create_error_context()
    context.metadata["operation"] = "get_containers_by_room_id"
    context.metadata["room_id"] = room_id

    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            """
            SELECT
                container_instance_id, source_type, owner_id, room_id, entity_id,
                lock_state, capacity_slots, weight_limit, decay_at,
                allowed_roles, metadata_json, created_at, updated_at,
                container_item_instance_id
            FROM containers
            WHERE room_id = %s
            ORDER BY created_at
            """,
            (room_id,),
        )
        rows = cursor.fetchall()
        cursor.close()

        containers = []
        for row in rows:
            containers.append(_build_container_data_from_row(conn, row))

        return containers

    except psycopg2.Error as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving containers by room_id: {e}",
            context=context,
            details={"room_id": room_id, "error": str(e)},
            user_friendly="Failed to retrieve containers",
        )


def get_containers_by_entity_id(conn: Any, entity_id: UUID) -> list[ContainerData]:
    """
    Get all containers owned by an entity (player/NPC).

    Args:
        conn: Database connection
        entity_id: Player/NPC UUID

    Returns:
        list[ContainerData]: List of containers owned by the entity

    Raises:
        DatabaseError: If database operation fails
    """
    context = create_error_context()
    context.metadata["operation"] = "get_containers_by_entity_id"
    context.metadata["entity_id"] = str(entity_id)

    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            """
            SELECT
                container_instance_id, source_type, owner_id, room_id, entity_id,
                lock_state, capacity_slots, weight_limit, decay_at,
                allowed_roles, metadata_json, created_at, updated_at,
                container_item_instance_id
            FROM containers
            WHERE entity_id = %s
            ORDER BY created_at
            """,
            (str(entity_id) if isinstance(entity_id, UUID) else entity_id,),
        )
        rows = cursor.fetchall()
        cursor.close()

        containers = []
        for row in rows:
            containers.append(_build_container_data_from_row(conn, row))

        return containers

    except psycopg2.Error as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving containers by entity_id: {e}",
            context=context,
            details={"entity_id": str(entity_id), "error": str(e)},
            user_friendly="Failed to retrieve containers",
        )


def get_decayed_containers(conn: Any, current_time: datetime | None = None) -> list[ContainerData]:
    """
    Get all containers that have decayed (decay_at < current_time).

    Args:
        conn: Database connection
        current_time: Current time for decay comparison (defaults to now() if not provided)
                      Must be timezone-aware UTC for proper PostgreSQL timestamptz comparison

    Returns:
        list[ContainerData]: List of decayed container data

    Raises:
        DatabaseError: If database operation fails
    """
    context = create_error_context()
    context.metadata["operation"] = "get_decayed_containers"

    if current_time is None:
        current_time = datetime.now(UTC)
        logger.debug("get_decayed_containers: Using current UTC time", current_time=current_time.isoformat())
    else:
        # Normalize to UTC: if timezone-aware, convert to UTC; if naive, assume UTC
        original_time = current_time
        if current_time.tzinfo is None:
            current_time = current_time.replace(tzinfo=UTC)
            logger.debug(
                "get_decayed_containers: Normalized naive datetime to UTC",
                original_time=original_time.isoformat(),
                normalized_time=current_time.isoformat(),
            )
        else:
            current_time = current_time.astimezone(UTC)
            if current_time.tzinfo != original_time.tzinfo:
                logger.debug(
                    "get_decayed_containers: Converted timezone-aware datetime to UTC",
                    original_time=original_time.isoformat(),
                    normalized_time=current_time.isoformat(),
                )

    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            """
            SELECT
                container_instance_id, source_type, owner_id, room_id, entity_id,
                lock_state, capacity_slots, weight_limit, decay_at,
                allowed_roles, metadata_json, created_at, updated_at,
                container_item_instance_id
            FROM containers
            WHERE decay_at IS NOT NULL AND decay_at < %s
            ORDER BY decay_at
            """,
            (current_time,),
        )
        rows = cursor.fetchall()
        cursor.close()

        containers = []
        for row in rows:
            containers.append(_build_container_data_from_row(conn, row))

        return containers

    except psycopg2.Error as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving decayed containers: {e}",
            context=context,
            details={"current_time": current_time.isoformat(), "error": str(e)},
            user_friendly="Failed to retrieve decayed containers",
        )
