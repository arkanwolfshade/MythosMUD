"""
Container repository for async persistence operations.

This module provides async wrappers for container operations,
delegating to the existing container_persistence module.
"""

import asyncio
import uuid
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from typing import Any

import psycopg2

from server.config import get_config
from server.persistence import container_persistence
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class ContainerCreateParams:
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

    Provides async wrappers around existing container_persistence functions
    for gradual async migration.
    """

    def __init__(self):
        """
        Initialize the container repository.

        No longer needs persistence_layer since we use container_persistence directly.
        """
        self._logger = get_logger(__name__)

    @contextmanager
    def _get_sync_connection(self):
        """Get a synchronous psycopg2 connection for container_persistence functions."""
        config = get_config()
        database_url = config.database.url
        # Convert async URL to sync URL
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://")
        elif database_url.startswith("postgresql://"):
            pass  # Already sync format
        else:
            raise ValueError(f"Unsupported database URL format: {database_url[:30]}...")

        conn = psycopg2.connect(database_url)
        try:
            yield conn
        finally:
            conn.close()

    async def create_container(
        self,
        source_type: str,
        params: ContainerCreateParams,
    ) -> dict[str, Any]:
        """Create a new container (async wrapper)."""

        def _create_sync():
            with self._get_sync_connection() as conn:
                result = container_persistence.create_container(
                    conn,
                    source_type,
                    params.owner_id,
                    params.room_id,
                    params.entity_id,
                    params.lock_state,
                    params.capacity_slots,
                    params.weight_limit,
                    params.decay_at,
                    params.allowed_roles,
                    params.items_json,
                    params.metadata_json,
                )
                # Convert ContainerData to dict (use to_dict but map items_json)
                result_dict = result.to_dict()
                # Map "items" back to "items_json" for compatibility
                if "items" in result_dict:
                    result_dict["items_json"] = result_dict.pop("items")
                if "metadata" in result_dict:
                    result_dict["metadata_json"] = result_dict.pop("metadata")
                return result_dict

        return await asyncio.to_thread(_create_sync)

    async def get_container(self, container_id: uuid.UUID) -> dict[str, Any] | None:
        """Get a container by ID (async wrapper)."""

        def _get_sync():
            with self._get_sync_connection() as conn:
                # Convert UUID to string for psycopg2 compatibility
                container_id_str = str(container_id) if isinstance(container_id, uuid.UUID) else container_id
                container_id_uuid = uuid.UUID(container_id_str) if isinstance(container_id_str, str) else container_id
                result = container_persistence.get_container(conn, container_id_uuid)
                if not result:
                    return None
                # Convert ContainerData to dict (use to_dict but map items_json)
                result_dict = result.to_dict()
                # Map "items" back to "items_json" for compatibility
                if "items" in result_dict:
                    result_dict["items_json"] = result_dict.pop("items")
                if "metadata" in result_dict:
                    result_dict["metadata_json"] = result_dict.pop("metadata")
                return result_dict

        return await asyncio.to_thread(_get_sync)

    async def get_containers_by_room_id(self, room_id: str) -> list[dict[str, Any]]:
        """Get all containers in a room (async wrapper)."""

        def _get_sync():
            with self._get_sync_connection() as conn:
                results = container_persistence.get_containers_by_room_id(conn, room_id)
                # Convert ContainerData objects to dicts
                return [
                    {
                        **r.to_dict(),
                        "items_json": r.to_dict().get("items", []),
                        "metadata_json": r.to_dict().get("metadata", {}),
                    }
                    for r in results
                ]

        return await asyncio.to_thread(_get_sync)

    async def get_containers_by_entity_id(self, entity_id: uuid.UUID) -> list[dict[str, Any]]:
        """Get all containers owned by an entity (async wrapper)."""

        def _get_sync():
            with self._get_sync_connection() as conn:
                # Ensure entity_id is a UUID object (psycopg2 can handle UUID objects)
                entity_id_uuid = uuid.UUID(str(entity_id)) if not isinstance(entity_id, uuid.UUID) else entity_id
                results = container_persistence.get_containers_by_entity_id(conn, entity_id_uuid)
                # Convert ContainerData objects to dicts
                return [
                    {
                        **r.to_dict(),
                        "items_json": r.to_dict().get("items", []),
                        "metadata_json": r.to_dict().get("metadata", {}),
                    }
                    for r in results
                ]

        return await asyncio.to_thread(_get_sync)

    async def update_container(
        self,
        container_id: uuid.UUID,
        items_json: list[dict[str, Any]] | None = None,
        lock_state: str | None = None,
        metadata_json: dict[str, Any] | None = None,
    ) -> dict[str, Any] | None:
        """Update a container (async wrapper)."""

        def _update_sync():
            with self._get_sync_connection() as conn:
                result = container_persistence.update_container(
                    conn, container_id, items_json, lock_state, metadata_json
                )
                if not result:
                    return None
                # Convert ContainerData to dict (use to_dict but map items_json)
                result_dict = result.to_dict()
                # Map "items" back to "items_json" for compatibility
                if "items" in result_dict:
                    result_dict["items_json"] = result_dict.pop("items")
                if "metadata" in result_dict:
                    result_dict["metadata_json"] = result_dict.pop("metadata")
                return result_dict

        return await asyncio.to_thread(_update_sync)

    async def get_decayed_containers(self, current_time: datetime | None = None) -> list[dict[str, Any]]:
        """Get decayed containers (async wrapper)."""

        def _get_sync():
            with self._get_sync_connection() as conn:
                results = container_persistence.get_decayed_containers(conn, current_time)
                # Convert ContainerData objects to dicts
                return [
                    {
                        **r.to_dict(),
                        "items_json": r.to_dict().get("items", []),
                        "metadata_json": r.to_dict().get("metadata", {}),
                    }
                    for r in results
                ]

        return await asyncio.to_thread(_get_sync)

    async def delete_container(self, container_id: uuid.UUID) -> bool:
        """Delete a container (async wrapper)."""

        def _delete_sync():
            with self._get_sync_connection() as conn:
                return container_persistence.delete_container(conn, container_id)

        return await asyncio.to_thread(_delete_sync)
