"""
Item repository for async persistence operations.

This module provides async wrappers for item instance operations,
delegating to the existing item_instance_persistence module.
"""

import asyncio
from typing import Any

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class ItemRepository:
    """
    Repository for item instance persistence operations.

    Provides async wrappers around existing item_instance_persistence functions
    for gradual async migration.
    """

    def __init__(self, persistence_layer):
        """
        Initialize the item repository.

        Args:
            persistence_layer: Reference to PersistenceLayer for sync operations
        """
        self._persistence = persistence_layer
        self._logger = get_logger(__name__)

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
        return await asyncio.to_thread(
            self._persistence.create_item_instance,
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
        return await asyncio.to_thread(
            self._persistence.ensure_item_instance,
            item_instance_id,
            prototype_id,
            owner_type,
            owner_id,
            quantity,
            metadata,
            origin_source,
            origin_metadata,
        )

    async def item_instance_exists(self, item_instance_id: str) -> bool:
        """Check if an item instance exists (async wrapper)."""
        return await asyncio.to_thread(self._persistence.item_instance_exists, item_instance_id)
