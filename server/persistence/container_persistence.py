"""
Container persistence operations for the unified container system.

As documented in the restricted archives of Miskatonic University, container
persistence requires careful handling to ensure proper storage and retrieval
of investigator artifacts across environmental props, wearable gear, and corpses.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from typing import Any
from uuid import UUID

import psycopg2
from psycopg2.extras import RealDictCursor

from ..exceptions import DatabaseError, ValidationError
from ..logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


class ContainerData:
    """Data class for container information."""

    def __init__(
        self,
        container_instance_id: UUID,
        source_type: str,
        owner_id: UUID | None = None,
        room_id: str | None = None,
        entity_id: UUID | None = None,
        lock_state: str = "unlocked",
        capacity_slots: int = 20,
        weight_limit: int | None = None,
        decay_at: datetime | None = None,
        allowed_roles: list[str] | None = None,
        items_json: list[dict[str, Any]] | None = None,
        metadata_json: dict[str, Any] | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ):
        self.container_instance_id = container_instance_id
        self.source_type = source_type
        self.owner_id = owner_id
        self.room_id = room_id
        self.entity_id = entity_id
        self.lock_state = lock_state
        self.capacity_slots = capacity_slots
        self.weight_limit = weight_limit
        self.decay_at = decay_at
        self.allowed_roles = allowed_roles or []
        self.items_json = items_json or []
        self.metadata_json = metadata_json or {}
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self) -> dict[str, Any]:
        """Convert container data to dictionary."""
        return {
            "container_instance_id": str(self.container_instance_id),
            "source_type": self.source_type,
            "owner_id": str(self.owner_id) if self.owner_id else None,
            "room_id": self.room_id,
            "entity_id": str(self.entity_id) if self.entity_id else None,
            "lock_state": self.lock_state,
            "capacity_slots": self.capacity_slots,
            "weight_limit": self.weight_limit,
            "decay_at": self.decay_at.isoformat() if self.decay_at else None,
            "allowed_roles": self.allowed_roles,
            "items_json": self.items_json,
            "metadata_json": self.metadata_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


def create_container(
    conn: Any,
    source_type: str,
    owner_id: UUID | None = None,
    room_id: str | None = None,
    entity_id: UUID | None = None,
    lock_state: str = "unlocked",
    capacity_slots: int = 20,
    weight_limit: int | None = None,
    decay_at: datetime | None = None,
    allowed_roles: list[str] | None = None,
    items_json: list[dict[str, Any]] | None = None,
    metadata_json: dict[str, Any] | None = None,
) -> ContainerData:
    """
    Create a new container in the database.

    Args:
        conn: Database connection
        source_type: Type of container ('environment', 'equipment', 'corpse')
        owner_id: UUID of container owner (optional)
        room_id: Room identifier for environmental/corpse containers (optional)
        entity_id: Player/NPC UUID for wearable containers (optional)
        lock_state: Lock state ('unlocked', 'locked', 'sealed')
        capacity_slots: Maximum number of inventory slots (1-20)
        weight_limit: Optional maximum weight capacity
        decay_at: Timestamp when corpse container should decay (optional)
        allowed_roles: List of role names allowed to access container (optional)
        items_json: List of InventoryStack items (optional)
        metadata_json: Optional metadata dictionary (optional)

    Returns:
        ContainerData: The created container data

    Raises:
        ValidationError: If validation fails
        DatabaseError: If database operation fails
    """
    context = create_error_context()
    context.metadata["operation"] = "create_container"
    context.metadata["source_type"] = source_type

    # Validate source_type
    if source_type not in ("environment", "equipment", "corpse"):
        log_and_raise(
            ValidationError,
            f"Invalid source_type: {source_type}. Must be 'environment', 'equipment', or 'corpse'",
            context=context,
            details={"source_type": source_type},
            user_friendly="Invalid container type",
        )

    # Validate capacity_slots
    if capacity_slots < 1 or capacity_slots > 20:
        log_and_raise(
            ValidationError,
            f"Invalid capacity_slots: {capacity_slots}. Must be between 1 and 20",
            context=context,
            details={"capacity_slots": capacity_slots},
            user_friendly="Invalid container capacity",
        )

    # Validate lock_state
    if lock_state not in ("unlocked", "locked", "sealed"):
        log_and_raise(
            ValidationError,
            f"Invalid lock_state: {lock_state}. Must be 'unlocked', 'locked', or 'sealed'",
            context=context,
            details={"lock_state": lock_state},
            user_friendly="Invalid lock state",
        )

    try:
        # Generate UUID for container
        container_id = UUID(int=0)  # Will be generated by database DEFAULT
        current_time = datetime.now(UTC).replace(tzinfo=None)

        # Prepare JSONB data
        items_jsonb = json.dumps(items_json or [])
        metadata_jsonb = json.dumps(metadata_json or {})
        allowed_roles_jsonb = json.dumps(allowed_roles or [])

        # Insert container
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            """
            INSERT INTO containers (
                source_type, owner_id, room_id, entity_id, lock_state,
                capacity_slots, weight_limit, decay_at, allowed_roles,
                items_json, metadata_json, created_at, updated_at
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, %s::jsonb, %s::jsonb, %s, %s
            )
            RETURNING container_instance_id, created_at, updated_at
            """,
            (
                source_type,
                owner_id,
                room_id,
                entity_id,
                lock_state,
                capacity_slots,
                weight_limit,
                decay_at,
                allowed_roles_jsonb,
                items_jsonb,
                metadata_jsonb,
                current_time,
                current_time,
            ),
        )
        row = cursor.fetchone()
        conn.commit()
        cursor.close()

        if not row:
            log_and_raise(
                DatabaseError,
                "Failed to create container - no ID returned",
                context=context,
                user_friendly="Failed to create container",
            )

        # RealDictCursor returns a dict-like row
        container_id = row["container_instance_id"]
        created_at = row["created_at"]
        updated_at = row["updated_at"]

        logger.info(
            "Container created",
            container_id=str(container_id),
            source_type=source_type,
            room_id=room_id,
            entity_id=str(entity_id) if entity_id else None,
        )

        return ContainerData(
            container_instance_id=container_id,
            source_type=source_type,
            owner_id=owner_id,
            room_id=room_id,
            entity_id=entity_id,
            lock_state=lock_state,
            capacity_slots=capacity_slots,
            weight_limit=weight_limit,
            decay_at=decay_at,
            allowed_roles=allowed_roles or [],
            items_json=items_json or [],
            metadata_json=metadata_json or {},
            created_at=created_at,
            updated_at=updated_at,
        )

    except psycopg2.Error as e:
        conn.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error creating container: {e}",
            context=context,
            details={"error": str(e), "source_type": source_type},
            user_friendly="Failed to create container",
        )


def get_container(conn: Any, container_id: UUID) -> ContainerData | None:
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
    context = create_error_context()
    context.metadata["operation"] = "get_container"
    context.metadata["container_id"] = str(container_id)

    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            """
            SELECT
                container_instance_id, source_type, owner_id, room_id, entity_id,
                lock_state, capacity_slots, weight_limit, decay_at,
                allowed_roles, items_json, metadata_json, created_at, updated_at
            FROM containers
            WHERE container_instance_id = %s
            """,
            (container_id,),
        )
        row = cursor.fetchone()
        cursor.close()

        if not row:
            return None

        # Convert row to ContainerData
        return ContainerData(
            container_instance_id=row["container_instance_id"],
            source_type=row["source_type"],
            owner_id=row["owner_id"],
            room_id=row["room_id"],
            entity_id=row["entity_id"],
            lock_state=row["lock_state"],
            capacity_slots=row["capacity_slots"],
            weight_limit=row["weight_limit"],
            decay_at=row["decay_at"],
            allowed_roles=row["allowed_roles"] if row["allowed_roles"] else [],
            items_json=row["items_json"] if row["items_json"] else [],
            metadata_json=row["metadata_json"] if row["metadata_json"] else {},
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )

    except psycopg2.Error as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving container: {e}",
            context=context,
            details={"container_id": str(container_id), "error": str(e)},
            user_friendly="Failed to retrieve container",
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
                allowed_roles, items_json, metadata_json, created_at, updated_at
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
            containers.append(
                ContainerData(
                    container_instance_id=row["container_instance_id"],
                    source_type=row["source_type"],
                    owner_id=row["owner_id"],
                    room_id=row["room_id"],
                    entity_id=row["entity_id"],
                    lock_state=row["lock_state"],
                    capacity_slots=row["capacity_slots"],
                    weight_limit=row["weight_limit"],
                    decay_at=row["decay_at"],
                    allowed_roles=row["allowed_roles"] if row["allowed_roles"] else [],
                    items_json=row["items_json"] if row["items_json"] else [],
                    metadata_json=row["metadata_json"] if row["metadata_json"] else {},
                    created_at=row["created_at"],
                    updated_at=row["updated_at"],
                )
            )

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
                allowed_roles, items_json, metadata_json, created_at, updated_at
            FROM containers
            WHERE entity_id = %s
            ORDER BY created_at
            """,
            (entity_id,),
        )
        rows = cursor.fetchall()
        cursor.close()

        containers = []
        for row in rows:
            containers.append(
                ContainerData(
                    container_instance_id=row["container_instance_id"],
                    source_type=row["source_type"],
                    owner_id=row["owner_id"],
                    room_id=row["room_id"],
                    entity_id=row["entity_id"],
                    lock_state=row["lock_state"],
                    capacity_slots=row["capacity_slots"],
                    weight_limit=row["weight_limit"],
                    decay_at=row["decay_at"],
                    allowed_roles=row["allowed_roles"] if row["allowed_roles"] else [],
                    items_json=row["items_json"] if row["items_json"] else [],
                    metadata_json=row["metadata_json"] if row["metadata_json"] else {},
                    created_at=row["created_at"],
                    updated_at=row["updated_at"],
                )
            )

        return containers

    except psycopg2.Error as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving containers by entity_id: {e}",
            context=context,
            details={"entity_id": str(entity_id), "error": str(e)},
            user_friendly="Failed to retrieve containers",
        )


def update_container(
    conn: Any,
    container_id: UUID,
    items_json: list[dict[str, Any]] | None = None,
    lock_state: str | None = None,
    metadata_json: dict[str, Any] | None = None,
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
    context = create_error_context()
    context.metadata["operation"] = "update_container"
    context.metadata["container_id"] = str(container_id)

    # Validate lock_state if provided
    if lock_state is not None and lock_state not in ("unlocked", "locked", "sealed"):
        log_and_raise(
            ValidationError,
            f"Invalid lock_state: {lock_state}. Must be 'unlocked', 'locked', or 'sealed'",
            context=context,
            details={"lock_state": lock_state},
            user_friendly="Invalid lock state",
        )

    try:
        # Build update query dynamically
        updates: list[str] = []
        params: list[Any] = []
        current_time = datetime.now(UTC).replace(tzinfo=None)

        if items_json is not None:
            updates.append("items_json = %s::jsonb")
            params.append(json.dumps(items_json))

        if lock_state is not None:
            updates.append("lock_state = %s")
            params.append(lock_state)

        if metadata_json is not None:
            updates.append("metadata_json = %s::jsonb")
            params.append(json.dumps(metadata_json))

        if not updates:
            # No updates to perform, just return current container
            return get_container(conn, container_id)

        updates.append("updated_at = %s")
        params.append(current_time)
        params.append(container_id)

        cursor = conn.cursor()
        cursor.execute(
            f"""
            UPDATE containers
            SET {", ".join(updates)}
            WHERE container_instance_id = %s
            RETURNING container_instance_id
            """,
            params,
        )
        row = cursor.fetchone()
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

    except psycopg2.Error as e:
        conn.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error updating container: {e}",
            context=context,
            details={"container_id": str(container_id), "error": str(e)},
            user_friendly="Failed to update container",
        )


def get_decayed_containers(conn: Any, current_time: datetime | None = None) -> list[ContainerData]:
    """
    Get all containers that have decayed (decay_at < current_time).

    Args:
        conn: Database connection
        current_time: Current time for decay comparison (defaults to now() if not provided)

    Returns:
        list[ContainerData]: List of decayed container data

    Raises:
        DatabaseError: If database operation fails
    """
    context = create_error_context()
    context.metadata["operation"] = "get_decayed_containers"

    if current_time is None:
        current_time = datetime.now(UTC).replace(tzinfo=None)

    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            """
            SELECT
                container_instance_id, source_type, owner_id, room_id, entity_id,
                lock_state, capacity_slots, weight_limit, decay_at,
                allowed_roles, items_json, metadata_json, created_at, updated_at
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
            containers.append(
                ContainerData(
                    container_instance_id=row["container_instance_id"],
                    source_type=row["source_type"],
                    owner_id=row["owner_id"],
                    room_id=row["room_id"],
                    entity_id=row["entity_id"],
                    lock_state=row["lock_state"],
                    capacity_slots=row["capacity_slots"],
                    weight_limit=row["weight_limit"],
                    decay_at=row["decay_at"],
                    allowed_roles=row["allowed_roles"] if row["allowed_roles"] else [],
                    items_json=row["items_json"] if row["items_json"] else [],
                    metadata_json=row["metadata_json"] if row["metadata_json"] else {},
                    created_at=row["created_at"],
                    updated_at=row["updated_at"],
                )
            )

        return containers

    except psycopg2.Error as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving decayed containers: {e}",
            context=context,
            details={"current_time": current_time.isoformat(), "error": str(e)},
            user_friendly="Failed to retrieve decayed containers",
        )


def delete_container(conn: Any, container_id: UUID) -> bool:
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
    context = create_error_context()
    context.metadata["operation"] = "delete_container"
    context.metadata["container_id"] = str(container_id)

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
            context=context,
            details={"container_id": str(container_id), "error": str(e)},
            user_friendly="Failed to delete container",
        )
