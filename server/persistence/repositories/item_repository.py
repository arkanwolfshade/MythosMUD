"""
Item repository for async persistence operations.

This module provides async item instance operations using SQLAlchemy AsyncSession,
delegating to item_instance_persistence_async (no thread-pool wrappers).
"""

from typing import Any

from server.database import get_session_maker
from server.persistence.item_instance_persistence_async import (
    create_item_instance_async,
    ensure_item_instance_async,
    item_instance_exists_async,
)
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class ItemRepository:
    """
    Repository for item instance persistence operations.

    Uses async SQLAlchemy sessions; no sync wrappers or thread pool.
    """

    def __init__(self, persistence_layer: Any = None) -> None:
        """
        Initialize the item repository.

        Args:
            persistence_layer: Deprecated; kept for backward compatibility, not used.
        """
        self._persistence = persistence_layer
        self._logger = get_logger(__name__)

    async def create_item_instance(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Item creation requires many parameters and intermediate variables for complex item instantiation logic
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
        """Create a new item instance (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            await create_item_instance_async(
                session=session,
                item_instance_id=item_instance_id,
                prototype_id=prototype_id,
                owner_type=owner_type,
                owner_id=owner_id,
                location_context=location_context,
                quantity=quantity,
                condition=condition,
                flags_override=flags_override,
                binding_state=binding_state,
                attunement_state=attunement_state,
                custom_name=custom_name,
                metadata_payload=metadata,
                origin_source=origin_source,
                origin_metadata=origin_metadata,
            )

    async def ensure_item_instance(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Item instance persistence requires many parameters for context and validation
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
        """Ensure an item instance exists (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            await ensure_item_instance_async(
                session=session,
                item_instance_id=item_instance_id,
                prototype_id=prototype_id,
                owner_type=owner_type,
                owner_id=owner_id,
                quantity=quantity,
                metadata_payload=metadata,
                origin_source=origin_source,
                origin_metadata=origin_metadata,
            )

    async def item_instance_exists(self, item_instance_id: str) -> bool:
        """Check if an item instance exists (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            return await item_instance_exists_async(
                session=session,
                item_instance_id=item_instance_id,
            )
