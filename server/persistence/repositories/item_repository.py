"""
Item repository for async persistence operations.

This module provides async wrappers for item instance operations,
delegating to the existing item_instance_persistence module.
"""

import asyncio
from contextlib import contextmanager
from typing import Any

import psycopg2

from server.config import get_config
from server.structured_logging.enhanced_logging_config import get_logger
from server.persistence import item_instance_persistence

logger = get_logger(__name__)


class ItemRepository:
    """
    Repository for item instance persistence operations.

    Provides async wrappers around existing item_instance_persistence functions
    for gradual async migration.
    """

    def __init__(self, persistence_layer=None):
        """
        Initialize the item repository.

        Args:
            persistence_layer: Reference to PersistenceLayer for sync operations (deprecated)
        """
        self._persistence = persistence_layer
        self._logger = get_logger(__name__)

    @contextmanager
    def _get_sync_connection(self):
        """Get a synchronous psycopg2 connection for item_instance_persistence functions."""
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

    async def create_item_instance(
        self,
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
        """Create a new item instance (async wrapper)."""

        def _create_sync():
            with self._get_sync_connection() as conn:
                return item_instance_persistence.create_item_instance(
                    conn,
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
                )

        return await asyncio.to_thread(_create_sync)

    async def ensure_item_instance(
        self,
        item_instance_id: str,
        prototype_id: str,
        owner_type: str = "room",
        owner_id: str | None = None,
        quantity: int = 1,
        metadata: dict[str, Any] | None = None,
        origin_source: str | None = None,
        origin_metadata: dict[str, Any] | None = None,
    ) -> None:
        """Ensure an item instance exists (async wrapper)."""

        def _ensure_sync():
            with self._get_sync_connection() as conn:
                return item_instance_persistence.ensure_item_instance(
                    conn,
                    item_instance_id,
                    prototype_id,
                    owner_type,
                    owner_id,
                    quantity,
                    metadata,
                    origin_source,
                    origin_metadata,
                )

        return await asyncio.to_thread(_ensure_sync)

    async def item_instance_exists(self, item_instance_id: str) -> bool:
        """Check if an item instance exists (async wrapper)."""

        def _exists_sync():
            with self._get_sync_connection() as conn:
                return item_instance_persistence.item_instance_exists(conn, item_instance_id)

        return await asyncio.to_thread(_exists_sync)
