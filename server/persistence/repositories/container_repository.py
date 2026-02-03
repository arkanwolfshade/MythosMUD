"""
Container repository for async persistence operations.

This module provides async container operations using SQLAlchemy AsyncSession,
delegating to container_persistence_async and container_query_helpers_async
(no thread-pool wrappers).
"""

import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from server.database import get_session_maker
from server.persistence.container_data import ContainerData
from server.persistence.container_persistence_async import (
    create_container_async,
    delete_container_async,
    get_container_async,
    update_container_async,
)
from server.persistence.container_query_helpers_async import (
    get_containers_by_entity_id_async,
    get_containers_by_room_id_async,
    get_decayed_containers_async,
)
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _container_data_to_dict(result: ContainerData) -> dict[str, Any]:
    """Convert ContainerData to dict with items_json/metadata_json for compatibility."""
    result_dict = result.to_dict()
    if "items" in result_dict:
        result_dict["items_json"] = result_dict.pop("items")
    if "metadata" in result_dict:
        result_dict["metadata_json"] = result_dict.pop("metadata")
    return result_dict


@dataclass
class ContainerCreateParams:  # pylint: disable=too-many-instance-attributes  # Reason: Container creation params requires many fields to capture complete container creation context
    """Parameters for creating a container."""

    owner_id: uuid.UUID | None = None
    room_id: str | None = None
    entity_id: uuid.UUID | None = None
    lock_state: str = "unlocked"
    capacity_slots: int = 20
    weight_limit: int | None = None
    decay_at: datetime | None = None
    allowed_roles: list[str] | None = None
    items_json: list[dict[str, Any]] | None = None
    metadata_json: dict[str, Any] | None = None


class ContainerRepository:
    """
    Repository for container persistence operations.

    Uses async SQLAlchemy sessions; no sync wrappers or thread pool.
    """

    def __init__(self) -> None:
        """Initialize the container repository."""
        self._logger = get_logger(__name__)

    async def create_container(
        self,
        source_type: str,
        params: ContainerCreateParams,
    ) -> dict[str, Any]:
        """Create a new container (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            result = await create_container_async(
                session=session,
                source_type=source_type,
                owner_id=params.owner_id,
                room_id=params.room_id,
                entity_id=params.entity_id,
                lock_state=params.lock_state,
                capacity_slots=params.capacity_slots,
                weight_limit=params.weight_limit,
                decay_at=params.decay_at,
                allowed_roles=params.allowed_roles,
                items_json=params.items_json,
                metadata_json=params.metadata_json,
            )
            return _container_data_to_dict(result)

    async def get_container(self, container_id: uuid.UUID) -> dict[str, Any] | None:
        """Get a container by ID (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            result = await get_container_async(session, container_id)
            if not result:
                return None
            return _container_data_to_dict(result)

    async def get_containers_by_room_id(self, room_id: str) -> list[dict[str, Any]]:
        """Get all containers in a room (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            results = await get_containers_by_room_id_async(session, room_id)
            return [_container_data_to_dict(r) for r in results]

    async def get_containers_by_entity_id(self, entity_id: uuid.UUID) -> list[dict[str, Any]]:
        """Get all containers owned by an entity (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            entity_id_uuid = uuid.UUID(str(entity_id)) if not isinstance(entity_id, uuid.UUID) else entity_id
            results = await get_containers_by_entity_id_async(session, entity_id_uuid)
            return [_container_data_to_dict(r) for r in results]

    async def update_container(
        self,
        container_id: uuid.UUID,
        items_json: list[dict[str, Any]] | None = None,
        lock_state: str | None = None,
        metadata_json: dict[str, Any] | None = None,
    ) -> dict[str, Any] | None:
        """Update a container (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            result = await update_container_async(
                session=session,
                container_id=container_id,
                items_json=items_json,
                lock_state=lock_state,
                metadata_json=metadata_json,
            )
            if not result:
                return None
            return _container_data_to_dict(result)

    async def get_decayed_containers(self, current_time: datetime | None = None) -> list[dict[str, Any]]:
        """Get decayed containers (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            results = await get_decayed_containers_async(session, current_time)
            return [_container_data_to_dict(r) for r in results]

    async def delete_container(self, container_id: uuid.UUID) -> bool:
        """Delete a container (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            return await delete_container_async(session, container_id)
