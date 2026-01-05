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
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

from ..exceptions import DatabaseError, ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


def _parse_jsonb_column(value: Any, default: Any) -> Any:
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


def _fetch_container_items(conn: Any, container_id: UUID) -> list[dict[str, Any]]:
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
        """
        Convert container data to dictionary.

        Returns dictionary with model field names (container_id, items, metadata)
        to match ContainerComponent model expectations.
        """
        return {
            "container_id": str(self.container_instance_id),
            "source_type": self.source_type,
            "owner_id": str(self.owner_id) if self.owner_id else None,
            "room_id": self.room_id,
            "entity_id": str(self.entity_id) if self.entity_id else None,
            "lock_state": self.lock_state,
            "capacity_slots": self.capacity_slots,
            "weight_limit": self.weight_limit,
            "decay_at": self.decay_at.isoformat() if self.decay_at else None,
            "allowed_roles": self.allowed_roles,
            "items": self.items_json,
            "metadata": self.metadata_json,
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
    container_item_instance_id: str | None = None,
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
        container_item_instance_id: Item instance ID that IS this container (optional)

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

        # Prepare JSONB data (items are now stored in container_contents table)
        metadata_jsonb = json.dumps(metadata_json or {})
        allowed_roles_jsonb = json.dumps(allowed_roles or [])

        # Insert container (items_json column removed - items go in container_contents)
        # Convert UUID objects to strings for psycopg2 compatibility
        owner_id_str = str(owner_id) if owner_id and isinstance(owner_id, UUID) else owner_id
        entity_id_str = str(entity_id) if entity_id and isinstance(entity_id, UUID) else entity_id

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
            (
                source_type,
                owner_id_str,
                room_id,
                entity_id_str,
                lock_state,
                capacity_slots,
                weight_limit,
                decay_at,
                allowed_roles_jsonb,
                metadata_jsonb,
                container_item_instance_id,
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

        # Add items to container_contents using stored procedure
        # First ensure item instances exist, then add them to container
        if items_json:
            cursor = conn.cursor()
            for position, item in enumerate(items_json):
                item_instance_id = item.get("item_instance_id") or item.get("item_id")
                prototype_id = item.get("item_id") or item.get("prototype_id")

                if item_instance_id and prototype_id:
                    # Ensure item instance exists in database before adding to container
                    # This is required for foreign key constraint on container_contents
                    from .item_instance_persistence import ensure_item_instance

                    try:
                        ensure_item_instance(
                            conn,
                            item_instance_id=item_instance_id,
                            prototype_id=prototype_id,
                            owner_type="container",
                            owner_id=str(container_id),
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

                    # Now add item to container
                    cursor.execute(
                        "SELECT add_item_to_container(%s, %s, %s)",
                        (container_id, item_instance_id, position),
                    )
            conn.commit()
            cursor.close()

        logger.info(
            "Container created",
            container_id=str(container_id),
            source_type=source_type,
            room_id=room_id,
            entity_id=str(entity_id) if entity_id else None,
        )

        # Get container with items using get_container (which uses stored procedure)
        return get_container(conn, container_id) or ContainerData(
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
        # Convert UUID to string for psycopg2 compatibility
        container_id_str = str(container_id) if isinstance(container_id, UUID) else container_id
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
            (container_id_str,),
        )
        row = cursor.fetchone()
        cursor.close()

        if not row:
            return None

        # Fetch items directly from normalized tables
        items_json = _fetch_container_items(conn, container_id)

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
            allowed_roles=_parse_jsonb_column(row["allowed_roles"], []),
            items_json=items_json,
            metadata_json=_parse_jsonb_column(row["metadata_json"], {}),
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
            # Fetch items directly from normalized tables
            items_json = _fetch_container_items(conn, row["container_instance_id"])

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
                    allowed_roles=_parse_jsonb_column(row["allowed_roles"], []),
                    items_json=items_json,
                    metadata_json=_parse_jsonb_column(row["metadata_json"], {}),
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
            # Fetch items directly from normalized tables
            items_json = _fetch_container_items(conn, row["container_instance_id"])

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
                    allowed_roles=_parse_jsonb_column(row["allowed_roles"], []),
                    items_json=items_json,
                    metadata_json=_parse_jsonb_column(row["metadata_json"], {}),
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
        # Convert container_id to string for psycopg2 compatibility
        container_id_str = str(container_id) if isinstance(container_id, UUID) else container_id

        # Build update query dynamically
        updates: list[str] = []
        params: list[Any] = []
        current_time = datetime.now(UTC).replace(tzinfo=None)
        cursor = conn.cursor()

        if items_json is not None:
            # Use stored procedures to update container contents
            # First, clear existing contents
            cursor.execute("SELECT clear_container_contents(%s)", (container_id_str,))

            # Then add each item using stored procedure
            # First ensure item instances exist, then add them to container
            from .item_instance_persistence import ensure_item_instance

            for position, item in enumerate(items_json):
                # Require both item_instance_id and (item_id or prototype_id)
                # Items missing either should be skipped
                item_instance_id = item.get("item_instance_id")
                prototype_id = item.get("item_id") or item.get("prototype_id")

                if item_instance_id and prototype_id:
                    # Ensure item instance exists in database before adding to container
                    # This is required for foreign key constraint on container_contents
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

                    # Now add item to container
                    cursor.execute(
                        "SELECT add_item_to_container(%s, %s, %s)",
                        (container_id_str, item_instance_id, position),
                    )

        if lock_state is not None:
            updates.append("lock_state = %s")
            params.append(lock_state)

        if metadata_json is not None:
            updates.append("metadata_json = %s::jsonb")
            params.append(json.dumps(metadata_json))

        # Initialize row variable
        row = None

        if updates:
            # Always update updated_at
            updates.append("updated_at = %s")
            params.append(current_time)
            params.append(container_id_str)

            # Use psycopg2.sql to safely construct the query
            # Column names are hardcoded in code (not user input), but we use
            # sql.SQL to satisfy static analysis tools
            set_clauses = sql.SQL(", ").join([sql.SQL(clause) for clause in updates])
            query = sql.SQL("""
                UPDATE containers
                SET {}
                WHERE container_instance_id = %s
                RETURNING container_instance_id
            """).format(set_clauses)

            cursor.execute(query, params)
            row = cursor.fetchone()
        elif items_json is not None:
            # If only items_json was provided, still update updated_at
            updates.append("updated_at = %s")
            params.append(current_time)
            params.append(container_id_str)

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
            # Fetch items directly from normalized tables
            items_json = _fetch_container_items(conn, row["container_instance_id"])

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
                    allowed_roles=_parse_jsonb_column(row["allowed_roles"], []),
                    items_json=items_json,
                    metadata_json=_parse_jsonb_column(row["metadata_json"], {}),
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
        # Convert UUID to string for psycopg2 compatibility
        container_id_str = str(container_id) if isinstance(container_id, UUID) else container_id
        cursor.execute(
            "DELETE FROM containers WHERE container_instance_id = %s RETURNING container_instance_id",
            (container_id_str,),
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
