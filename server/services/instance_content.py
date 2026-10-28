"""
Filling and emptying an instance: the things a template room declares besides its description.

A template room can declare, in ``attributes``:

    furniture      environment containers (see room_furniture_loader)
    items          floor items (see room_item_seeder)
    instance_npcs  NPC definition names to spawn, e.g. ["Lamplighter"]

``populate`` gives a freshly cloned instance all three, in the instance's own rooms. ``teardown``
undoes it before the instance is destroyed: its NPCs are despawned, its containers deleted, and
whatever those containers held is handed back so the flush can bank it (instance-bound items are
dropped there). Nothing here knows about any one tutorial or dungeon; it is all room data.
"""

from __future__ import annotations

from typing import Protocol, cast
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError

from ..exceptions import DatabaseError, ValidationError
from ..game.instance_manager import Instance
from ..game.items.item_factory import ItemFactory
from ..game.items.prototype_registry import PrototypeRegistry, PrototypeRegistryError
from ..models.room import Room
from ..structured_logging.enhanced_logging_config import get_logger
from .room_furniture_loader import FurniturePersistence, sync_room_furniture
from .room_item_seeder import RoomDropSink, seed_room_items

logger = get_logger(__name__)


class InstanceContentPersistence(FurniturePersistence, Protocol):
    """FurniturePersistence plus deleting a container, for teardown."""

    async def delete_container(self, container_id: UUID) -> bool:
        """Delete one container row; False if it was already gone."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body, as in FurniturePersistence


class InstanceNpcHost(Protocol):
    """Where instance NPCs live: spawns them by definition name and clears a set of rooms."""

    def spawn(self, definition_name: str, room_id: str) -> str | None:
        """Spawn the named NPC definition in room_id; the new NPC's id, or None if it could not be spawned."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body

    def despawn_in_rooms(self, room_prefix: str) -> int:
        """Despawn every NPC whose room id starts with room_prefix; returns how many."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: Protocol stub body


def _npc_names(room: Room) -> list[str]:
    """NPC definition names from attributes["instance_npcs"]; malformed entries are skipped."""
    raw = cast(object, room.attributes.get("instance_npcs"))
    if not isinstance(raw, list):
        return []
    return [name for name in cast(list[object], raw) if isinstance(name, str) and name]


def _container_stacks(container: dict[str, object]) -> list[dict[str, object]]:
    """The item stacks held by a container row."""
    items = container.get("items_json")
    if not isinstance(items, list):
        return []
    return [cast(dict[str, object], item) for item in cast(list[object], items) if isinstance(item, dict)]


class InstanceContentService:
    """Populate a new instance from its rooms' declarations and clear it again before it is destroyed."""

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: one collaborator per kind of content (containers, items, NPCs)
        self,
        persistence: InstanceContentPersistence,
        registry: PrototypeRegistry,
        item_factory: ItemFactory,
        drops: RoomDropSink,
        npcs: InstanceNpcHost | None = None,
    ) -> None:
        """Wire the container store, item prototypes, floor-drop sink and (optionally) the NPC host."""
        self._persistence: InstanceContentPersistence = persistence
        self._registry: PrototypeRegistry = registry
        self._item_factory: ItemFactory = item_factory
        self._drops: RoomDropSink = drops
        self._npcs: InstanceNpcHost | None = npcs

    async def populate(self, instance: Instance) -> None:
        """Create the instance rooms' furniture containers, floor items and NPCs. Never raises over a fixture."""
        rooms = list(instance.rooms.values())
        try:
            _ = await sync_room_furniture(rooms, self._registry, self._persistence)
        except (DatabaseError, ValidationError, SQLAlchemyError) as e:
            logger.error(
                "Instance furniture failed; continuing without it", instance_id=instance.instance_id, error=str(e)
            )
        _ = seed_room_items(rooms, self._item_factory, self._drops)
        self._spawn_npcs(instance)

    def _spawn_npcs(self, instance: Instance) -> None:
        if self._npcs is None:
            return
        for room_id, room in instance.rooms.items():
            for name in _npc_names(room):
                if self._npcs.spawn(name, room_id) is None:
                    logger.warning(
                        "Instance NPC could not be spawned", instance_id=instance.instance_id, room_id=room_id, npc=name
                    )

    def _with_prototype_flags(self, stack: dict[str, object]) -> dict[str, object]:
        """The stack with its prototype's flags: container rows do not store them, and the flush needs INSTANCE_BOUND."""
        if stack.get("flags"):
            return stack
        prototype_id = stack.get("prototype_id") or stack.get("item_id")
        if not isinstance(prototype_id, str):
            return stack
        try:
            prototype = self._registry.get(prototype_id)
        except PrototypeRegistryError:
            return stack
        return {**stack, "flags": list(prototype.flags)} if prototype.flags else stack

    async def teardown(self, instance: Instance) -> list[dict[str, object]]:
        """Despawn the instance's NPCs and delete its containers; returns the stacks those containers held.

        Call before the instance is destroyed (NPC despawn resolves their rooms through it). A container
        whose delete fails keeps its contents out of the result, so nothing can be banked twice.
        """
        if self._npcs is not None:
            _ = self._npcs.despawn_in_rooms(f"{instance.instance_id}_")
        recovered: list[dict[str, object]] = []
        for room_id in instance.rooms:
            try:
                for container in await self._persistence.get_containers_by_room_id(room_id):
                    if await self._persistence.delete_container(UUID(str(container["container_id"]))):
                        recovered.extend(self._with_prototype_flags(stack) for stack in _container_stacks(container))
            except (DatabaseError, SQLAlchemyError, ValueError) as e:
                logger.error(
                    "Instance containers could not be cleared",
                    instance_id=instance.instance_id,
                    room_id=room_id,
                    error=str(e),
                )
        return recovered
