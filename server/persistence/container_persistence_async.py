"""
Async container persistence operations.

Provides async implementations using SQLAlchemy AsyncSession and raw SQL
(text) for containers and container_contents, replacing the sync
psycopg2-based container_persistence for use by ContainerRepository.
"""

from __future__ import annotations

import json
from typing import Any, cast
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..exceptions import DatabaseError, ValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise
from .container_data import ContainerData, ContainerDataCore, ContainerDataExtras
from .container_helpers import parse_jsonb_column

logger = get_logger(__name__)


def _parse_jsonb(value: Any, default: Any) -> Any:
    """Parse JSONB value (same as container_helpers.parse_jsonb_column)."""
    return parse_jsonb_column(value, default)


def _prepare_container_create_params(**params: Any) -> dict[str, Any]:
    """Prepare params dict for create_container procedure call."""
    return {
        "source_type": params.get("source_type"),
        "owner_id": str(params.get("owner_id")) if params.get("owner_id") else None,
        "room_id": params.get("room_id"),
        "entity_id": str(params.get("entity_id")) if params.get("entity_id") else None,
        "lock_state": params.get("lock_state"),
        "capacity_slots": params.get("capacity_slots"),
        "weight_limit": params.get("weight_limit"),
        "decay_at": params.get("decay_at"),
        "allowed_roles": json.dumps(params.get("allowed_roles") or []),
        "metadata_json": json.dumps(params.get("metadata_json") or {}),
        "container_item_instance_id": params.get("container_item_instance_id"),
    }


def _validate_container_create_params(source_type: str, capacity_slots: int, lock_state: str) -> None:
    """Validate create_container params. Raises ValidationError on invalid input."""
    if source_type not in ("environment", "equipment", "corpse"):
        log_and_raise(
            ValidationError,
            f"Invalid source_type: {source_type}. Must be 'environment', 'equipment', or 'corpse'",
            operation="create_container_async",
            source_type=source_type,
            details={"source_type": source_type},
            user_friendly="Invalid container type",
        )
    if capacity_slots < 1 or capacity_slots > 20:
        log_and_raise(
            ValidationError,
            f"Invalid capacity_slots: {capacity_slots}. Must be between 1 and 20",
            operation="create_container_async",
            capacity_slots=capacity_slots,
            details={"capacity_slots": capacity_slots},
            user_friendly="Invalid container capacity",
        )
    if lock_state not in ("unlocked", "locked", "sealed"):
        log_and_raise(
            ValidationError,
            f"Invalid lock_state: {lock_state}. Must be 'unlocked', 'locked', or 'sealed'",
            operation="create_container_async",
            lock_state=lock_state,
            details={"lock_state": lock_state},
            user_friendly="Invalid lock state",
        )


async def _populate_container_items_async(
    session: AsyncSession, container_id: Any, items_json: list[dict[str, Any]]
) -> None:
    """Populate container with items via ensure_item_instance and add_item_to_container."""
    from .item_instance_persistence_async import ensure_item_instance_async

    await session.execute(text("SELECT clear_container_contents(:cid)"), {"cid": str(container_id)})
    for position, item in enumerate(items_json):
        item_instance_id = item.get("item_instance_id") or item.get("item_id")
        prototype_id = item.get("item_id") or item.get("prototype_id")
        if not item_instance_id or not prototype_id:
            continue
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


def _row_to_mapping(row: Any) -> dict[str, Any]:
    """Extract row as dict by _mapping or positional fallback."""
    if hasattr(row, "_mapping"):
        return dict(row._mapping)  # pylint: disable=protected-access  # Reason: SQLAlchemy Row._mapping is standard
    cols = ("item_instance_id", "item_id", "item_name", "quantity", "condition", "metadata", "position")
    return {cols[i]: row[i] for i in range(min(len(cols), len(row)))}


def _parse_item_metadata(raw: Any) -> dict[str, Any]:
    """Parse metadata to dict. Handles None, str, dict."""
    if raw is None:
        return {}
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str):
        if not raw:
            return {}
        try:
            return cast(dict[str, Any], json.loads(raw))
        except (json.JSONDecodeError, ValueError):
            return {}
    return {}


def _build_item_dict(mapping: dict[str, Any]) -> dict[str, Any] | None:
    """Build item dict from mapping. Returns None if item_instance_id missing."""
    item_instance_id = mapping.get("item_instance_id")
    if not item_instance_id:
        return None
    metadata_val = _parse_item_metadata(mapping.get("metadata"))
    quantity = mapping.get("quantity")
    position = mapping.get("position")
    condition = mapping.get("condition")
    item_id = mapping.get("item_id")
    item_name = mapping.get("item_name")
    return {
        "item_instance_id": str(item_instance_id),
        "item_id": str(item_id) if item_id else None,
        "item_name": str(item_name) if item_name else "Unknown Item",
        "quantity": int(quantity) if quantity is not None else 1,
        "condition": str(condition) if condition else "pristine",
        "position": int(position) if position is not None else 0,
        "metadata": metadata_val,
        "slot_type": "backpack",
    }


async def fetch_container_items_async(session: AsyncSession, container_id: UUID) -> list[dict[str, Any]]:
    """
    Fetch container items via fetch_container_items procedure.

    Args:
        session: Async database session
        container_id: Container UUID

    Returns:
        List of item dicts matching the items_json format
    """
    container_id_str = str(container_id) if isinstance(container_id, UUID) else container_id
    result = await session.execute(
        text(
            """
            SELECT
                item_instance_id,
                item_id,
                item_name,
                quantity,
                condition,
                metadata,
                "position"
            FROM fetch_container_items(:cid)
            """
        ),
        {"cid": container_id_str},
    )
    rows = result.fetchall()
    items: list[dict[str, Any]] = []
    for row in rows:
        mapping = _row_to_mapping(row)
        item_dict = _build_item_dict(mapping)
        if item_dict is not None:
            items.append(item_dict)
    return items


async def _call_create_container_procedure(
    session: AsyncSession, proc_params: dict[str, Any], source_type: str
) -> tuple[Any, Any, Any]:
    """Execute create_container procedure. Returns (container_id, created_at, updated_at). Raises if no row."""
    result = await session.execute(
        text("""
            SELECT container_instance_id, created_at, updated_at
            FROM create_container(
                :source_type, :owner_id, :room_id, :entity_id, :lock_state,
                :capacity_slots, :weight_limit, :decay_at,
                CAST(:allowed_roles AS jsonb), CAST(:metadata_json AS jsonb),
                :container_item_instance_id
            )
        """),
        proc_params,
    )
    row = result.fetchone()
    if not row:
        log_and_raise(
            DatabaseError,
            "Failed to create container - no ID returned",
            operation="create_container_async",
            source_type=source_type,
            user_friendly="Failed to create container",
        )
    return row[0], row[1], row[2]


async def _finalize_container_creation(
    session: AsyncSession,
    container_id: Any,
    params: dict[str, Any],
    source_type: str,
    created_at: Any,
    updated_at: Any,
) -> ContainerData:
    """Populate items, commit, log, and return container (from get_container or fallback)."""
    items_json = params.get("items_json")
    if items_json:
        await _populate_container_items_async(session, container_id, items_json)
    await session.commit()
    logger.info(
        "Container created",
        container_id=str(container_id),
        source_type=source_type,
        room_id=params.get("room_id"),
        entity_id=params.get("entity_id"),
    )
    out = await get_container_async(session, container_id)
    if out:
        return out
    return ContainerData(
        ContainerDataCore(
            container_instance_id=container_id,
            source_type=source_type,
            owner_id=params.get("owner_id"),
            room_id=params.get("room_id"),
            entity_id=params.get("entity_id"),
            lock_state=params.get("lock_state", "unlocked"),
            capacity_slots=params.get("capacity_slots", 20),
        ),
        ContainerDataExtras(
            weight_limit=params.get("weight_limit"),
            decay_at=params.get("decay_at"),
            allowed_roles=params.get("allowed_roles") or [],
            items_json=params.get("items_json") or [],
            metadata_json=params.get("metadata_json") or {},
            created_at=created_at,
            updated_at=updated_at,
        ),
    )


async def create_container_async(
    session: AsyncSession,
    source_type: str,
    **params: Any,
) -> ContainerData:
    """
    Create a new container (async). Returns ContainerData with generated container_instance_id.

    Params may include: owner_id, room_id, entity_id, lock_state, capacity_slots,
    weight_limit, decay_at, allowed_roles, items_json, metadata_json,
    container_item_instance_id.
    """
    _validate_container_create_params(
        source_type, params.get("capacity_slots", 20), params.get("lock_state", "unlocked")
    )
    proc_params = _prepare_container_create_params(source_type=source_type, **params)
    try:
        container_id, created_at, updated_at = await _call_create_container_procedure(session, proc_params, source_type)
        return await _finalize_container_creation(session, container_id, params, source_type, created_at, updated_at)
    except SQLAlchemyError as e:
        await session.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error creating container: {e}",
            operation="create_container_async",
            source_type=source_type,
            details={"error": str(e), "source_type": source_type},
            user_friendly="Failed to create container",
        )


async def get_container_async(session: AsyncSession, container_id: UUID) -> ContainerData | None:
    """Get a container by ID (async) via get_container procedure."""
    container_id_str = str(container_id) if isinstance(container_id, UUID) else container_id
    try:
        result = await session.execute(
            text(
                """
                SELECT
                    container_instance_id,
                    source_type,
                    owner_id,
                    room_id,
                    entity_id,
                    lock_state,
                    capacity_slots,
                    weight_limit,
                    decay_at,
                    allowed_roles,
                    metadata_json,
                    created_at,
                    updated_at,
                    container_item_instance_id
                FROM get_container(:cid)
                """
            ),
            {"cid": container_id_str},
        )
        row = result.fetchone()
        if not row:
            return None
        items_json = await fetch_container_items_async(session, container_id)
        return ContainerData(
            ContainerDataCore(
                container_instance_id=row[0],
                source_type=row[1],
                owner_id=row[2],
                room_id=row[3],
                entity_id=row[4],
                lock_state=row[5],
                capacity_slots=row[6],
            ),
            ContainerDataExtras(
                weight_limit=row[7],
                decay_at=row[8],
                allowed_roles=_parse_jsonb(row[9], []),
                items_json=items_json,
                metadata_json=_parse_jsonb(row[10], {}),
                created_at=row[11],
                updated_at=row[12],
            ),
        )
    except SQLAlchemyError as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving container: {e}",
            operation="get_container_async",
            container_id=str(container_id),
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

    validate_lock_state(lock_state)

    container_id_str = str(container_id) if isinstance(container_id, UUID) else container_id

    if items_json is not None:
        await _populate_container_items_async(session, container_id_str, items_json)
    # Run update_container procedure when we changed lock_state/metadata and/or items
    if lock_state is not None or metadata_json is not None or items_json is not None:
        await session.execute(
            text("SELECT update_container(:cid, :lock_state, :metadata_json)"),
            {
                "cid": container_id_str,
                "lock_state": lock_state,
                "metadata_json": json.dumps(metadata_json) if metadata_json is not None else None,
            },
        )
    await session.commit()
    logger.info("Container updated", container_id=str(container_id))
    return await get_container_async(session, container_id)


async def delete_container_async(session: AsyncSession, container_id: UUID) -> bool:
    """Delete a container (async) via delete_container procedure. Returns True if deleted."""
    container_id_str = str(container_id) if isinstance(container_id, UUID) else container_id
    try:
        result = await session.execute(
            text("SELECT delete_container(:cid)"),
            {"cid": container_id_str},
        )
        deleted = result.scalar()
        await session.commit()
        return bool(deleted)
    except SQLAlchemyError as e:
        await session.rollback()
        log_and_raise(
            DatabaseError,
            f"Database error deleting container: {e}",
            operation="delete_container_async",
            container_id=str(container_id),
            details={"container_id": str(container_id), "error": str(e)},
            user_friendly="Failed to delete container",
        )
    # log_and_raise always raises; no return needed here.
