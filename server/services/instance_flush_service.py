"""
Flushing ephemeral instances.

When an instance is torn down (tutorial exit, the player really leaving the game, server
shutdown) whatever was dropped on its floors goes to the instance owner's bank deposit box
(see bank_service), then the instance is destroyed. Only the owner can open that box, so lost
items can no longer be taken by anyone else, and a full box never discards them.
"""

from __future__ import annotations

from typing import Protocol
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError

from ..exceptions import DatabaseError
from ..game.instance_manager import InstanceManager
from ..structured_logging.enhanced_logging_config import get_logger
from .bank_service import BankBoxPersistence, forward_to_bank_box

logger = get_logger(__name__)


class RoomDropStore(Protocol):  # pylint: disable=too-few-public-methods  # Reason: single-method structural type
    """Where floor drops live (RoomSubscriptionManager)."""

    def pop_room_drops_with_prefix(self, prefix: str) -> list[dict[str, object]]:
        """Remove and return the drops of every room whose id starts with prefix."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright needs a stub body for a non-None return


class InstanceFlushService:
    """Destroy instances, moving their floor items to the owner's bank deposit box."""

    def __init__(
        self,
        instance_manager: InstanceManager,
        drops: RoomDropStore | None,
        persistence: BankBoxPersistence,
    ) -> None:
        """Wire the instance store, the floor-drop store, and bank box persistence."""
        self._instance_manager: InstanceManager = instance_manager
        self._drops: RoomDropStore | None = drops
        self._persistence: BankBoxPersistence = persistence

    async def flush(self, instance_id: str) -> int:
        """Flush one instance. Returns how many floor stacks were sent to the owner's deposit box."""
        # The owner must be read first: destroying the instance forgets it.
        instance = self._instance_manager.get_instance(instance_id)
        stacks = self._drops.pop_room_drops_with_prefix(f"{instance_id}_") if self._drops else []
        self._instance_manager.destroy_instance(instance_id)
        if not stacks:
            return 0
        item_ids = [stack.get("item_id") for stack in stacks]
        if instance is None:
            logger.error(
                "Flushed instance has no owner on record; floor items lost",
                instance_id=instance_id,
                item_ids=item_ids,
            )
            return 0
        try:
            await forward_to_bank_box(self._persistence, UUID(instance.owner_player_id), stacks)
        except (DatabaseError, SQLAlchemyError, ValueError) as e:
            logger.error(
                "Bank box deposit failed; floor items lost",
                instance_id=instance_id,
                owner_player_id=instance.owner_player_id,
                item_ids=item_ids,
                error=str(e),
            )
            return 0
        logger.info(
            "Instance floor items sent to owner's bank box",
            instance_id=instance_id,
            owner_player_id=instance.owner_player_id,
            stack_count=len(stacks),
        )
        return len(stacks)

    async def flush_all(self) -> int:
        """Flush every live instance (server shutdown). Returns the total stacks moved."""
        moved = 0
        for instance_id in self._instance_manager.list_instance_ids():
            moved += await self.flush(instance_id)
        return moved
