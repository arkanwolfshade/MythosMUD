"""
Container persistence operations for the unified container system.

As documented in the restricted archives of Miskatonic University, container
persistence requires careful handling to ensure proper storage and retrieval
of investigator artifacts across environmental props, wearable gear, and corpses.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from typing import cast
from uuid import UUID

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import connection as PsycopgConnection
from psycopg2.extensions import cursor as PsycopgCursor
from psycopg2.extras import RealDictCursor

from ..exceptions import DatabaseError
from ..persistence.container_create_params import ContainerCreateParams
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise
from .container_data import ContainerData
from .container_helpers import (
    allowed_roles_from_row,
    as_opt_datetime,
    as_opt_str,
    as_opt_uuid,
    as_uuid,
    fetch_container_items,
    int_from_row,
    metadata_from_row,
    opt_int_from_row,
    parse_jsonb_column,
    validate_create_container_args,
    validate_update_lock_state,
)

logger = get_logger(__name__)

# Re-export for package callers and unit tests that patch these symbols.
__all__ = [
    "ContainerData",
    "fetch_container_items",
    "parse_jsonb_column",
    "create_container",
    "delete_container",
    "get_container",
    "get_containers_by_entity_id",
    "get_containers_by_room_id",
    "update_container",
]


def _insert_container_row(conn: PsycopgConnection, bind: tuple[object, ...]) -> dict[str, object] | None:
    """INSERT containers row and return RealDict row (container_instance_id, created_at, updated_at)."""
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        """
        INSERT INTO containers (
            source_type, owner_id, room_id, entity_id, lock_state,
            capacity_slots, weight_limit, decay_at, allowed_roles,
            metadata_json, container_item_instance_id, created_at, updated_at
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, %s::jsonb, %s, %s, %s
        )
        RETURNING container_instance_id, created_at, updated_at
        """,
        bind,
    )
    row_raw = cursor.fetchone()
    conn.commit()
    cursor.close()
    if row_raw is None:
        return None
    return cast(dict[str, object], row_raw)


def _seed_container_contents(
    conn: PsycopgConnection, container_id: UUID, items_json: list[dict[str, object]] | None
) -> None:
    """Add initial items via add_item_to_container stored procedure."""
    if not items_json:
        return
    cursor = conn.cursor()
    for position, item in enumerate(items_json):
        item_instance_id = item.get("item_instance_id") or item.get("item_id")
        if item_instance_id:
            cursor.execute(
                "SELECT add_item_to_container(%s, %s, %s)",
                (container_id, item_instance_id, position),
            )
    conn.commit()
    cursor.close()


def _container_data_from_dict(
    conn: PsycopgConnection, row: dict[str, object], container_id: UUID | None = None
) -> ContainerData:
    """Build ContainerData from a containers RealDict row."""
    cid = container_id if container_id is not None else as_uuid(row["container_instance_id"])
    return ContainerData(
        container_instance_id=as_uuid(row["container_instance_id"]),
        source_type=str(row["source_type"]),
        owner_id=as_opt_uuid(row["owner_id"]),
        room_id=as_opt_str(row["room_id"]),
        entity_id=as_opt_uuid(row["entity_id"]),
        lock_state=str(row["lock_state"]),
        capacity_slots=int_from_row(row["capacity_slots"], 20),
        weight_limit=opt_int_from_row(row["weight_limit"]),
        decay_at=as_opt_datetime(row["decay_at"]),
        allowed_roles=allowed_roles_from_row(row["allowed_roles"]),
        items_json=fetch_container_items(conn, cid),
        metadata_json=metadata_from_row(row["metadata_json"]),
        created_at=as_opt_datetime(row["created_at"]),
        updated_at=as_opt_datetime(row["updated_at"]),
    )


def _complete_container_create(
    conn: PsycopgConnection,
    row: dict[str, object],
    source_type: str,
    params: ContainerCreateParams,
) -> ContainerData:
    """Seed contents, log, and return reloaded or fallback ContainerData after INSERT."""
    container_id = as_uuid(row["container_instance_id"])
    items_json = cast(list[dict[str, object]] | None, params.items_json)
    _seed_container_contents(conn, container_id, items_json)
    logger.info(
        "Container created",
        container_id=str(container_id),
        source_type=source_type,
        room_id=params.room_id,
        entity_id=str(params.entity_id) if params.entity_id else None,
    )
    existing = get_container(conn, container_id)
    if existing is not None:
        return existing
    created_at = as_opt_datetime(row["created_at"]) or datetime.now(UTC).replace(tzinfo=None)
    updated_at = as_opt_datetime(row["updated_at"]) or created_at
    metadata_json = cast(dict[str, object] | None, params.metadata_json)
    return ContainerData(
        container_instance_id=container_id,
        source_type=source_type,
        owner_id=params.owner_id,
        room_id=params.room_id,
        entity_id=params.entity_id,
        lock_state=params.lock_state,
        capacity_slots=params.capacity_slots,
        weight_limit=params.weight_limit,
        decay_at=params.decay_at,
        allowed_roles=params.allowed_roles or [],
        items_json=items_json or [],
        metadata_json=metadata_json or {},
        created_at=created_at,
        updated_at=updated_at,
    )


def create_container(
    conn: PsycopgConnection,
    source_type: str,
    params: ContainerCreateParams | None = None,
) -> ContainerData:
    """Create a new container in the database."""
    p = params or ContainerCreateParams()
    validate_create_container_args(source_type, p.capacity_slots, p.lock_state)
    try:
        current_time = datetime.now(UTC).replace(tzinfo=None)
        row = _insert_container_row(
            conn,
            (
                source_type,
                p.owner_id,
                p.room_id,
                p.entity_id,
                p.lock_state,
                p.capacity_slots,
                p.weight_limit,
                p.decay_at,
                json.dumps(p.allowed_roles or []),
                json.dumps(p.metadata_json or {}),
                p.container_item_instance_id,
                current_time,
                current_time,
            ),
        )
        if not row:
            log_and_raise(
                DatabaseError,
                "Failed to create container - no ID returned",
                operation="create_container",
                source_type=source_type,
                user_friendly="Failed to create container",
            )
        return _complete_container_create(conn, row, source_type, p)
    except psycopg2.Error as e:
        conn.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error creating container: {e}",
            operation="create_container",
            source_type=source_type,
            details={"error": str(e), "source_type": source_type},
            user_friendly="Failed to create container",
        )


def get_container(conn: PsycopgConnection, container_id: UUID) -> ContainerData | None:
    """
    Get a container by ID.

    Args:
        conn: Database connection
        container_id: Container UUID

    Returns:
        ContainerData: Container data if found, None otherwise

    Raises:
        DatabaseError: If database operation fails
    """
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
            WHERE container_instance_id = %s
            """,
            (container_id,),
        )
        row_raw = cursor.fetchone()
        cursor.close()

        if not row_raw:
            return None

        return _container_data_from_dict(conn, cast(dict[str, object], row_raw), container_id)

    except psycopg2.Error as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving container: {e}",
            operation="get_container",
            container_id=str(container_id),
            details={"container_id": str(container_id), "error": str(e)},
            user_friendly="Failed to retrieve container",
        )


def get_containers_by_room_id(conn: PsycopgConnection, room_id: str) -> list[ContainerData]:
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
        rows = cast(list[object], cursor.fetchall())
        cursor.close()

        containers: list[ContainerData] = []
        for row_raw in rows:
            row = cast(dict[str, object], row_raw)
            containers.append(_container_data_from_dict(conn, row))

        return containers

    except psycopg2.Error as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving containers by room_id: {e}",
            operation="get_containers_by_room_id",
            room_id=room_id,
            details={"room_id": room_id, "error": str(e)},
            user_friendly="Failed to retrieve containers",
        )


def get_containers_by_entity_id(conn: PsycopgConnection, entity_id: UUID) -> list[ContainerData]:
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
            (entity_id,),
        )
        rows = cast(list[object], cursor.fetchall())
        cursor.close()

        containers: list[ContainerData] = []
        for row_raw in rows:
            row = cast(dict[str, object], row_raw)
            containers.append(_container_data_from_dict(conn, row))

        return containers

    except psycopg2.Error as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving containers by entity_id: {e}",
            operation="get_containers_by_entity_id",
            entity_id=str(entity_id),
            details={"entity_id": str(entity_id), "error": str(e)},
            user_friendly="Failed to retrieve containers",
        )


def _replace_container_items(cursor: PsycopgCursor, container_id: UUID, items_json: list[dict[str, object]]) -> None:
    """Clear container contents and re-add items via stored procedures."""
    cursor.execute("SELECT clear_container_contents(%s)", (container_id,))
    for position, item in enumerate(items_json):
        item_instance_id = item.get("item_instance_id") or item.get("item_id")
        if item_instance_id:
            cursor.execute(
                "SELECT add_item_to_container(%s, %s, %s)",
                (container_id, item_instance_id, position),
            )


def _apply_container_column_updates(
    cursor: PsycopgCursor,
    container_id: UUID,
    lock_state: str | None,
    metadata_json: dict[str, object] | None,
    current_time: datetime,
) -> tuple[object | None, list[str]]:
    """UPDATE lock/metadata columns; return (returning_row, update clauses incl. updated_at)."""
    updates: list[str] = []
    params: list[object] = []
    if lock_state is not None:
        updates.append("lock_state = %s")
        params.append(lock_state)
    if metadata_json is not None:
        updates.append("metadata_json = %s::jsonb")
        params.append(json.dumps(metadata_json))
    if not updates:
        return None, updates

    updates.append("updated_at = %s")
    params.append(current_time)
    params.append(container_id)
    # Column names are hardcoded constants, not user input; values are parameterized.
    set_clauses = sql.SQL(", ").join([sql.SQL(clause) for clause in updates])
    query = sql.SQL("""
        UPDATE containers
        SET {}
        WHERE container_instance_id = %s
        RETURNING container_instance_id
    """).format(set_clauses)
    # nosec B608: Using psycopg2.sql.SQL for safe SQL construction (column names are hardcoded)
    # nosemgrep: python.lang.security.audit.sql-injection.sql-injection
    # nosemgrep: python.sqlalchemy.security.sqlalchemy-execute-raw-query.sqlalchemy-execute-raw-query
    cursor.execute(query, params)
    return cursor.fetchone(), updates


def _execute_container_update(
    conn: PsycopgConnection,
    container_id: UUID,
    items_json: list[dict[str, object]] | None,
    lock_state: str | None,
    metadata_json: dict[str, object] | None,
) -> ContainerData | None:
    """Apply item/column updates, commit, and re-read the container when a row was returned."""
    current_time = datetime.now(UTC).replace(tzinfo=None)
    cursor = conn.cursor()
    if items_json is not None:
        _replace_container_items(cursor, container_id, items_json)
    row, updates = _apply_container_column_updates(cursor, container_id, lock_state, metadata_json, current_time)
    conn.commit()
    cursor.close()
    if not row:
        return None
    logger.info(
        "Container updated",
        container_id=str(container_id),
        updated_fields=len(updates) - 1,  # Exclude updated_at
    )
    return get_container(conn, container_id)


def update_container(
    conn: PsycopgConnection,
    container_id: UUID,
    items_json: list[dict[str, object]] | None = None,
    lock_state: str | None = None,
    metadata_json: dict[str, object] | None = None,
) -> ContainerData | None:
    """
    Update a container's items, lock state, or metadata.

    Args:
        conn: Database connection
        container_id: Container UUID
        items_json: New items list (optional)
        lock_state: New lock state (optional)
        metadata_json: New metadata (optional)

    Returns:
        ContainerData: Updated container data if found, None otherwise

    Raises:
        ValidationError: If validation fails
        DatabaseError: If database operation fails
    """
    validate_update_lock_state(lock_state, container_id)
    try:
        return _execute_container_update(conn, container_id, items_json, lock_state, metadata_json)
    except psycopg2.Error as e:
        conn.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error updating container: {e}",
            operation="update_container",
            container_id=str(container_id),
            details={"container_id": str(container_id), "error": str(e)},
            user_friendly="Failed to update container",
        )


def delete_container(conn: PsycopgConnection, container_id: UUID) -> bool:
    """
    Delete a container.

    Args:
        conn: Database connection
        container_id: Container UUID

    Returns:
        bool: True if container was deleted, False if not found

    Raises:
        DatabaseError: If database operation fails
    """
    try:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM containers WHERE container_instance_id = %s RETURNING container_instance_id",
            (container_id,),
        )
        row = cursor.fetchone()
        conn.commit()
        cursor.close()

        if row:
            logger.info("Container deleted", container_id=str(container_id))
            return True
        return False

    except psycopg2.Error as e:
        conn.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error deleting container: {e}",
            operation="delete_container",
            container_id=str(container_id),
            details={"container_id": str(container_id), "error": str(e)},
            user_friendly="Failed to delete container",
        )
