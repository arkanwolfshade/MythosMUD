"""
Async container persistence operations.

Provides async implementations using SQLAlchemy AsyncSession and raw SQL
(text) for containers and container_contents, replacing the sync
psycopg2-based container_persistence for use by ContainerRepository.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from typing import Any
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.engine import Result
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..exceptions import DatabaseError, ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_error_context, log_and_raise
from .container_data import ContainerData
from .container_helpers import parse_jsonb_column

logger = get_logger(__name__)


def _parse_jsonb(value: Any, default: Any) -> Any:
    """Parse JSONB value (same as container_helpers.parse_jsonb_column)."""
    return parse_jsonb_column(value, default)


async def fetch_container_items_async(session: AsyncSession, container_id: UUID) -> list[dict[str, Any]]:
    """
    Fetch container items from container_contents JOIN item_instances JOIN item_prototypes.

    Args:
        session: Async database session
        container_id: Container UUID

    Returns:
        List of item dicts matching the items_json format
    """
    container_id_str = str(container_id) if isinstance(container_id, UUID) else container_id
    result = await session.execute(
        text("""
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
            WHERE cc.container_id = :cid
            ORDER BY cc.position
        """),
        {"cid": container_id_str},
    )
    rows = result.fetchall()
    # Row is a Row object with keys from column names
    items = []
    for row in rows:
        item_instance_id = row.item_instance_id if hasattr(row, "item_instance_id") else row[0]
        item_id = row.item_id if hasattr(row, "item_id") else row[1]
        item_name = row.item_name if hasattr(row, "item_name") else row[2]
        quantity = row.quantity if hasattr(row, "quantity") else row[3]
        condition = row.condition if hasattr(row, "condition") else row[4]
        metadata_val = row.metadata if hasattr(row, "metadata") else row[5]
        position = row.position if hasattr(row, "position") else row[6]
        if not item_instance_id:
            continue
        if isinstance(metadata_val, str):
            try:
                metadata_val = json.loads(metadata_val) if metadata_val else {}
            except (json.JSONDecodeError, ValueError):
                metadata_val = {}
        elif metadata_val is None or not isinstance(metadata_val, dict):
            metadata_val = {}
        items.append(
            {
                "item_instance_id": str(item_instance_id) if item_instance_id else None,
                "item_id": str(item_id) if item_id else None,
                "item_name": str(item_name) if item_name else "Unknown Item",
                "quantity": int(quantity) if quantity is not None else 1,
                "condition": str(condition) if condition else "pristine",
                "position": int(position) if position is not None else 0,
                "metadata": metadata_val,
                "slot_type": "backpack",
            }
        )
    return items


async def create_container_async(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Container creation requires many parameters for complex container logic
    session: AsyncSession,
    source_type: str,
    owner_id: UUID | None,
    room_id: str | None,
    entity_id: UUID | None,
    lock_state: str,
    capacity_slots: int,
    weight_limit: int | None,
    decay_at: datetime | None,
    allowed_roles: list[str] | None,
    items_json: list[dict[str, Any]] | None,
    metadata_json: dict[str, Any] | None,
    container_item_instance_id: str | None = None,
) -> ContainerData:
    """
    Create a new container (async). Returns ContainerData with generated container_instance_id.
    """
    context = create_error_context()
    context.metadata["operation"] = "create_container_async"
    context.metadata["source_type"] = source_type

    if source_type not in ("environment", "equipment", "corpse"):
        log_and_raise(
            ValidationError,
            f"Invalid source_type: {source_type}. Must be 'environment', 'equipment', or 'corpse'",
            context=context,
            details={"source_type": source_type},
            user_friendly="Invalid container type",
        )
    if capacity_slots < 1 or capacity_slots > 20:
        log_and_raise(
            ValidationError,
            f"Invalid capacity_slots: {capacity_slots}. Must be between 1 and 20",
            context=context,
            details={"capacity_slots": capacity_slots},
            user_friendly="Invalid container capacity",
        )
    if lock_state not in ("unlocked", "locked", "sealed"):
        log_and_raise(
            ValidationError,
            f"Invalid lock_state: {lock_state}. Must be 'unlocked', 'locked', or 'sealed'",
            context=context,
            details={"lock_state": lock_state},
            user_friendly="Invalid lock state",
        )

    owner_id_str = str(owner_id) if owner_id else None
    entity_id_str = str(entity_id) if entity_id else None
    allowed_roles_json = json.dumps(allowed_roles or [])
    metadata_json_str = json.dumps(metadata_json or {})
    now = datetime.now(UTC)

    try:
        result = await session.execute(
            text("""
                INSERT INTO containers (
                    source_type, owner_id, room_id, entity_id, lock_state,
                    capacity_slots, weight_limit, decay_at, allowed_roles,
                    metadata_json, container_item_instance_id, created_at, updated_at
                ) VALUES (
                    :source_type, :owner_id, :room_id, :entity_id, :lock_state,
                    :capacity_slots, :weight_limit, :decay_at, :allowed_roles::jsonb,
                    :metadata_json::jsonb, :container_item_instance_id, :now, :now
                )
                RETURNING container_instance_id, created_at, updated_at
            """),
            {
                "source_type": source_type,
                "owner_id": owner_id_str,
                "room_id": room_id,
                "entity_id": entity_id_str,
                "lock_state": lock_state,
                "capacity_slots": capacity_slots,
                "weight_limit": weight_limit,
                "decay_at": decay_at,
                "allowed_roles": allowed_roles_json,
                "metadata_json": metadata_json_str,
                "container_item_instance_id": container_item_instance_id,
                "now": now,
            },
        )
        row = result.fetchone()
        if not row:
            log_and_raise(
                DatabaseError,
                "Failed to create container - no ID returned",
                context=context,
                user_friendly="Failed to create container",
            )
        container_id = row[0]
        created_at = row[1]
        updated_at = row[2]

        if items_json:
            from .item_instance_persistence_async import ensure_item_instance_async

            await session.execute(text("SELECT clear_container_contents(:cid)"), {"cid": str(container_id)})
            for position, item in enumerate(items_json):
                item_instance_id = item.get("item_instance_id") or item.get("item_id")
                prototype_id = item.get("item_id") or item.get("prototype_id")
                if item_instance_id and prototype_id:
                    try:
                        await ensure_item_instance_async(
                            session=session,
                            item_instance_id=str(item_instance_id),
                            prototype_id=str(prototype_id),
                            owner_type="container",
                            owner_id=str(container_id),
                            quantity=item.get("quantity", 1),
                            metadata_payload=item.get("metadata", {}),
                        )
                    except (DatabaseError, ValidationError) as e:
                        logger.warning(
                            "Failed to ensure item instance exists, skipping item",
                            item_instance_id=item_instance_id,
                            prototype_id=prototype_id,
                            error=str(e),
                        )
                        continue
                    await session.execute(
                        text("SELECT add_item_to_container(:cid, :iid, :pos)"),
                        {"cid": str(container_id), "iid": str(item_instance_id), "pos": position},
                    )
        await session.commit()
        logger.info(
            "Container created",
            container_id=str(container_id),
            source_type=source_type,
            room_id=room_id,
            entity_id=entity_id_str,
        )
        out = await get_container_async(session, container_id)
        if out:
            return out
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
    except SQLAlchemyError as e:
        await session.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error creating container: {e}",
            context=context,
            details={"error": str(e), "source_type": source_type},
            user_friendly="Failed to create container",
        )


async def get_container_async(session: AsyncSession, container_id: UUID) -> ContainerData | None:
    """Get a container by ID (async)."""
    context = create_error_context()
    context.metadata["operation"] = "get_container_async"
    context.metadata["container_id"] = str(container_id)
    container_id_str = str(container_id) if isinstance(container_id, UUID) else container_id
    try:
        result = await session.execute(
            text("""
                SELECT
                    container_instance_id, source_type, owner_id, room_id, entity_id,
                    lock_state, capacity_slots, weight_limit, decay_at,
                    allowed_roles, metadata_json, created_at, updated_at,
                    container_item_instance_id
                FROM containers
                WHERE container_instance_id = :cid
            """),
            {"cid": container_id_str},
        )
        row = result.fetchone()
        if not row:
            return None
        items_json = await fetch_container_items_async(session, container_id)
        return ContainerData(
            container_instance_id=row[0],
            source_type=row[1],
            owner_id=row[2],
            room_id=row[3],
            entity_id=row[4],
            lock_state=row[5],
            capacity_slots=row[6],
            weight_limit=row[7],
            decay_at=row[8],
            allowed_roles=_parse_jsonb(row[9], []),
            items_json=items_json,
            metadata_json=_parse_jsonb(row[10], {}),
            created_at=row[11],
            updated_at=row[12],
        )
    except SQLAlchemyError as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving container: {e}",
            context=context,
            details={"container_id": str(container_id), "error": str(e)},
            user_friendly="Failed to retrieve container",
        )
    # log_and_raise always raises; no return needed here.


async def update_container_async(  # pylint: disable=too-many-locals  # Reason: Single transactional update for items, lock_state, metadata; extracting would duplicate session/context handling
    session: AsyncSession,
    container_id: UUID,
    items_json: list[dict[str, Any]] | None = None,
    lock_state: str | None = None,
    metadata_json: dict[str, Any] | None = None,
) -> ContainerData | None:
    """Update a container's items, lock_state, or metadata (async)."""
    from .container_helpers import validate_lock_state

    context = create_error_context()
    context.metadata["operation"] = "update_container_async"
    context.metadata["container_id"] = str(container_id)
    validate_lock_state(lock_state, context)

    container_id_str = str(container_id) if isinstance(container_id, UUID) else container_id
    now = datetime.now(UTC)
    updates = []
    params: dict[str, Any] = {"cid": container_id_str, "now": now}

    if items_json is not None:
        from .item_instance_persistence_async import ensure_item_instance_async

        await session.execute(text("SELECT clear_container_contents(:cid)"), {"cid": container_id_str})
        for position, item in enumerate(items_json):
            item_instance_id = item.get("item_instance_id") or item.get("item_id")
            prototype_id = item.get("item_id") or item.get("prototype_id")
            if item_instance_id and prototype_id:
                try:
                    await ensure_item_instance_async(
                        session=session,
                        item_instance_id=str(item_instance_id),
                        prototype_id=str(prototype_id),
                        owner_type="container",
                        owner_id=container_id_str,
                        quantity=item.get("quantity", 1),
                        metadata_payload=item.get("metadata", {}),
                    )
                except (DatabaseError, ValidationError) as e:
                    logger.warning(
                        "Failed to ensure item instance exists, skipping item",
                        item_instance_id=item_instance_id,
                        prototype_id=prototype_id,
                        error=str(e),
                    )
                    continue
                await session.execute(
                    text("SELECT add_item_to_container(:cid, :iid, :pos)"),
                    {"cid": container_id_str, "iid": str(item_instance_id), "pos": position},
                )
    if lock_state is not None:
        updates.append("lock_state = :lock_state")
        params["lock_state"] = lock_state
    if metadata_json is not None:
        updates.append("metadata_json = :metadata_json::jsonb")
        params["metadata_json"] = json.dumps(metadata_json)
    updates.append("updated_at = :now")
    # Run UPDATE when we changed lock_state/metadata and/or items (to bump updated_at)
    if len(updates) > 1 or items_json is not None:
        set_clause = ", ".join(updates)
        await session.execute(
            text(f"UPDATE containers SET {set_clause} WHERE container_instance_id = :cid"),
            params,
        )
    await session.commit()
    logger.info("Container updated", container_id=str(container_id))
    return await get_container_async(session, container_id)


async def delete_container_async(session: AsyncSession, container_id: UUID) -> bool:
    """Delete a container (async). Returns True if deleted, False if not found."""
    context = create_error_context()
    context.metadata["operation"] = "delete_container_async"
    context.metadata["container_id"] = str(container_id)
    container_id_str = str(container_id) if isinstance(container_id, UUID) else container_id
    try:
        result: Result[Any] = await session.execute(
            text("DELETE FROM containers WHERE container_instance_id = :cid"),
            {"cid": container_id_str},
        )
        await session.commit()
        # rowcount not in Result stubs; CursorResult has it at runtime
        rowcount: int = getattr(result, "rowcount", 0)
        return rowcount > 0
    except SQLAlchemyError as e:
        await session.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error deleting container: {e}",
            context=context,
            details={"container_id": str(container_id), "error": str(e)},
            user_friendly="Failed to delete container",
        )
    # log_and_raise always raises; no return needed here.
