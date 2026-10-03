"""
Flushing ephemeral instances.

When an instance is torn down (tutorial exit, the player really leaving the game, server
shutdown) whatever was dropped on its floors goes to the lost-and-found chest in the instance's
exit room, then the instance is destroyed. The chest is the environment container whose
metadata role is "lost_and_found" (placed by room furniture); when it is full the oldest stacks
are evicted first so recent losses stay recoverable.
"""

from __future__ import annotations

from typing import Protocol, cast
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError

from ..exceptions import DatabaseError
from ..game.instance_manager import InstanceManager
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

LOST_AND_FOUND_ROLE = "lost_and_found"


class RoomDropStore(Protocol):  # pylint: disable=too-few-public-methods  # Reason: single-method structural type
    """Where floor drops live (RoomSubscriptionManager)."""

    def pop_room_drops_with_prefix(self, prefix: str) -> list[dict[str, object]]:
        """Remove and return the drops of every room whose id starts with prefix."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright needs a stub body for a non-None return


class LostAndFoundPersistence(Protocol):
    """The slice of AsyncPersistenceLayer the lost-and-found deposit needs."""

    async def get_containers_by_room_id(self, room_id: str) -> list[dict[str, object]]:
        """All container rows in a room."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright needs a stub body for a non-None return

    async def update_container(
        self,
        container_id: UUID,
        items_json: list[dict[str, object]] | None = None,
        lock_state: str | None = None,
        metadata_json: dict[str, object] | None = None,
        capacity_slots: int | None = None,
    ) -> dict[str, object] | None:
        """Update a container; items_json replaces its contents."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright needs a stub body for a non-None return


def _lost_and_found(containers: list[dict[str, object]]) -> dict[str, object] | None:
    for container in containers:
        metadata = container.get("metadata_json")
        if isinstance(metadata, dict) and cast(dict[str, object], metadata).get("role") == LOST_AND_FOUND_ROLE:
            return container
    return None


async def deposit_in_lost_and_found(
    persistence: LostAndFoundPersistence, room_id: str, stacks: list[dict[str, object]]
) -> None:
    """Append stacks to room_id's lost-and-found chest, evicting the oldest stacks when full."""
    chest = _lost_and_found(await persistence.get_containers_by_room_id(room_id))
    if chest is None:
        logger.warning(
            "No lost-and-found chest in exit room; floor items discarded",
            room_id=room_id,
            item_ids=[stack.get("item_id") for stack in stacks],
        )
        return
    held = chest.get("items_json")
    items = [*(cast(list[dict[str, object]], held) if isinstance(held, list) else []), *stacks]
    capacity = int(cast(int, chest.get("capacity_slots") or 1))
    evicted = items[: max(0, len(items) - capacity)]
    for stack in evicted:
        logger.info(
            "Lost-and-found full; oldest stack discarded",
            room_id=room_id,
            item_id=stack.get("item_id"),
            item_name=stack.get("item_name"),
        )
    # ponytail: read-modify-write without a container lock; a player taking from the chest in the
    # same instant can be overwritten (container writes are last-writer-wins everywhere today).
    _ = await persistence.update_container(UUID(str(chest["container_id"])), items_json=items[len(evicted) :])


class InstanceFlushService:
    """Destroy instances, moving their floor items to the exit room's lost-and-found chest."""

    def __init__(
        self,
        instance_manager: InstanceManager,
        drops: RoomDropStore | None,
        persistence: LostAndFoundPersistence,
    ) -> None:
        """Wire the instance store, the floor-drop store, and container persistence."""
        self._instance_manager: InstanceManager = instance_manager
        self._drops: RoomDropStore | None = drops
        self._persistence: LostAndFoundPersistence = persistence

    async def flush(self, instance_id: str) -> int:
        """Flush one instance. Returns how many floor stacks were sent to the lost-and-found."""
        exit_room_id = self._instance_manager.get_exit_room_id(instance_id)
        stacks = self._drops.pop_room_drops_with_prefix(f"{instance_id}_") if self._drops else []
        self._instance_manager.destroy_instance(instance_id)
        if not stacks:
            return 0
        try:
            await deposit_in_lost_and_found(self._persistence, exit_room_id, stacks)
        except (DatabaseError, SQLAlchemyError) as e:
            logger.error(
                "Lost-and-found deposit failed; floor items lost",
                instance_id=instance_id,
                item_ids=[stack.get("item_id") for stack in stacks],
                error=str(e),
            )
            return 0
        logger.info("Instance floor items sent to lost-and-found", instance_id=instance_id, stack_count=len(stacks))
        return len(stacks)

    async def flush_all(self) -> int:
        """Flush every live instance (server shutdown). Returns the total stacks moved."""
        moved = 0
        for instance_id in self._instance_manager.list_instance_ids():
            moved += await self.flush(instance_id)
        return moved
