"""
Item repository for async persistence operations.

This module provides async item instance operations using SQLAlchemy AsyncSession,
delegating to item_instance_persistence_async (no thread-pool wrappers).
"""

from server.async_persistence_constants import CreateItemInstanceInput, EnsureItemInstanceInput
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

    def __init__(self) -> None:
        """Initialize the item repository."""
        self._logger = get_logger(__name__)

    async def create_item_instance(
        self,
        item_instance_id: str,
        prototype_id: str,
        options: CreateItemInstanceInput | None = None,
    ) -> None:
        """Create a new item instance (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            await create_item_instance_async(
                session=session,
                item_instance_id=item_instance_id,
                prototype_id=prototype_id,
                options=options,
            )

    async def ensure_item_instance(
        self,
        item_instance_id: str,
        prototype_id: str,
        options: EnsureItemInstanceInput | None = None,
    ) -> None:
        """Ensure an item instance exists (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            await ensure_item_instance_async(
                session=session,
                item_instance_id=item_instance_id,
                prototype_id=prototype_id,
                options=options,
            )

    async def item_instance_exists(self, item_instance_id: str) -> bool:
        """Check if an item instance exists (async)."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            return await item_instance_exists_async(
                session=session,
                item_instance_id=item_instance_id,
            )
