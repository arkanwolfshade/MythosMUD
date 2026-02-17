"""Async query helpers for container persistence."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import log_and_raise
from .container_data import ContainerData
from .container_helpers import parse_jsonb_column
from .container_persistence_async import fetch_container_items_async

logger = get_logger(__name__)


def _parse_jsonb(value: Any, default: Any) -> Any:
    """Parse JSONB value."""
    return parse_jsonb_column(value, default)


async def _build_container_data_from_row_async(
    session: AsyncSession, row: tuple[Any, ...], container_id: UUID
) -> ContainerData:
    """Build ContainerData from a database row (async)."""
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


async def get_containers_by_room_id_async(session: AsyncSession, room_id: str) -> list[ContainerData]:
    """Get all containers in a room (async)."""
    try:
        result = await session.execute(
            text("""
                SELECT
                    container_instance_id, source_type, owner_id, room_id, entity_id,
                    lock_state, capacity_slots, weight_limit, decay_at,
                    allowed_roles, metadata_json, created_at, updated_at,
                    container_item_instance_id
                FROM containers
                WHERE room_id = :room_id
                ORDER BY created_at
            """),
            {"room_id": room_id},
        )
        rows = result.fetchall()
        containers = []
        for row in rows:
            container_id = row[0]
            containers.append(await _build_container_data_from_row_async(session, tuple(row), container_id))
        return containers
    except SQLAlchemyError as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving containers by room_id: {e}",
            operation="get_containers_by_room_id_async",
            room_id=room_id,
            details={"room_id": room_id, "error": str(e)},
            user_friendly="Failed to retrieve containers",
        )
    # log_and_raise always raises; no return needed here.


async def get_containers_by_entity_id_async(session: AsyncSession, entity_id: UUID) -> list[ContainerData]:
    """Get all containers owned by an entity (async)."""
    entity_id_str = str(entity_id) if isinstance(entity_id, UUID) else entity_id
    try:
        result = await session.execute(
            text("""
                SELECT
                    container_instance_id, source_type, owner_id, room_id, entity_id,
                    lock_state, capacity_slots, weight_limit, decay_at,
                    allowed_roles, metadata_json, created_at, updated_at,
                    container_item_instance_id
                FROM containers
                WHERE entity_id = :entity_id
                ORDER BY created_at
            """),
            {"entity_id": entity_id_str},
        )
        rows = result.fetchall()
        containers = []
        for row in rows:
            container_id = row[0]
            containers.append(await _build_container_data_from_row_async(session, tuple(row), container_id))
        return containers
    except SQLAlchemyError as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving containers by entity_id: {e}",
            operation="get_containers_by_entity_id_async",
            entity_id=str(entity_id),
            details={"entity_id": str(entity_id), "error": str(e)},
            user_friendly="Failed to retrieve containers",
        )
    # log_and_raise always raises; no return needed here.


async def get_decayed_containers_async(
    session: AsyncSession, current_time: datetime | None = None
) -> list[ContainerData]:
    """Get all decayed containers (async)."""
    if current_time is None:
        current_time = datetime.now(UTC)
    else:
        if current_time.tzinfo is None:
            current_time = current_time.replace(tzinfo=UTC)
        else:
            current_time = current_time.astimezone(UTC)
    try:
        result = await session.execute(
            text("""
                SELECT
                    container_instance_id, source_type, owner_id, room_id, entity_id,
                    lock_state, capacity_slots, weight_limit, decay_at,
                    allowed_roles, metadata_json, created_at, updated_at,
                    container_item_instance_id
                FROM containers
                WHERE decay_at IS NOT NULL AND decay_at < :current_time
                ORDER BY decay_at
            """),
            {"current_time": current_time},
        )
        rows = result.fetchall()
        containers = []
        for row in rows:
            container_id = row[0]
            containers.append(await _build_container_data_from_row_async(session, tuple(row), container_id))
        return containers
    except SQLAlchemyError as e:
        log_and_raise(
            DatabaseError,
            f"Database error retrieving decayed containers: {e}",
            operation="get_decayed_containers_async",
            details={"current_time": current_time.isoformat(), "error": str(e)},
            user_friendly="Failed to retrieve decayed containers",
        )
    # log_and_raise always raises; no return needed here.
