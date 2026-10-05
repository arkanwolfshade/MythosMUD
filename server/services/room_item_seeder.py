"""
Room item seeding: items declared on rooms are placed on the floor at startup (#870).

World data declares floor items per room:

    rooms.attributes.items = [{"prototype_id": "consumable.folk_tonic", "quantity": 1}]

Each entry is minted via ``ItemFactory`` and added to the room's drops. Drops live in memory, so
the world restocks on every server start. Template rooms are skipped -- instances need their own
seeding.

# ponytail: in-memory restock-on-restart only; persistent or respawn-timed world items need
# their own state (and a record of what players already took) when that design is wanted.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol, cast

from sqlalchemy.exc import SQLAlchemyError

from ..exceptions import DatabaseError, ValidationError
from ..game.instance_manager import is_template_room
from ..game.items.item_factory import ItemFactory, ItemFactoryError
from ..models.room import Room
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class RoomDropSink(Protocol):
    """The slice of the room manager the seeder needs."""

    def add_room_drop(self, room_id: str, stack: dict[str, object]) -> None:
        """Add a stack to a room's floor drops."""


class RoomListPersistence(Protocol):
    """The slice of AsyncPersistenceLayer the startup hook needs."""

    async def warmup_room_cache(self) -> None:
        """Load the room cache if it is not loaded yet."""

    def list_rooms(self) -> list[Room]:
        """All cached rooms."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body (not just a docstring) for a non-None Protocol return type


def _as_entry(item: object) -> dict[str, object]:
    # Narrowing happens here, not in the caller's loop, so `item` stays `object` there
    # (narrowed in place it became dict[Unknown, Unknown] for basedpyright).
    return cast(dict[str, object], item) if isinstance(item, dict) else {}


def _item_entries(room_id: str, attributes: dict[str, object]) -> list[tuple[str, int]]:
    """(prototype_id, quantity) pairs from room attributes["items"]; malformed entries are skipped."""
    raw = attributes.get("items")
    if raw is None:
        return []
    if not isinstance(raw, list):
        logger.warning("Room items must be a list; ignored", room_id=room_id)
        return []
    entries: list[tuple[str, int]] = []
    for item in cast(list[object], raw):
        entry = _as_entry(item)
        prototype_id = entry.get("prototype_id")
        quantity = entry.get("quantity", 1)
        if (
            not isinstance(prototype_id, str)
            or not prototype_id
            or not isinstance(quantity, int)
            or isinstance(quantity, bool)
            or quantity < 1
        ):
            logger.warning("Malformed room item entry ignored", room_id=room_id, entry=repr(item))
            continue
        entries.append((prototype_id, quantity))
    return entries


def seed_room_items(rooms: Iterable[Room], factory: ItemFactory, room_manager: RoomDropSink) -> int:
    """Add every room's declared items to its floor drops. Returns the number of stacks placed."""
    placed = 0
    for room in rooms:
        room_id = cast(str, room.id)
        entries = _item_entries(room_id, cast(dict[str, object], room.attributes))
        if not entries:
            continue
        if is_template_room(room):
            logger.warning("Items on an instance template room are not supported; ignored", room_id=room_id)
            continue
        for prototype_id, quantity in entries:
            try:
                instance = factory.create_instance(
                    prototype_id, quantity=quantity, origin={"source": "room_seed", "room_id": room_id}
                )
            except ItemFactoryError as e:
                logger.warning("Room item prototype unusable; skipped", room_id=room_id, error=str(e))
                continue
            stack = cast(dict[str, object], instance.to_inventory_stack())
            # Floor items are picked up into inventory, never worn, so they sit in the general slot.
            stack["slot_type"] = "inventory"
            room_manager.add_room_drop(room_id, stack)
            placed += 1
    logger.info("Room items seeded", stack_count=placed)
    return placed


async def initialize_room_items(
    persistence: RoomListPersistence | None, factory: object, room_manager: object | None
) -> None:
    """Startup hook: seed floor items for every cached room. Never fails startup over world data."""
    if persistence is None or not isinstance(factory, ItemFactory) or room_manager is None:
        logger.warning("Room item seeding skipped: persistence, item factory, or room manager unavailable")
        return
    try:
        await persistence.warmup_room_cache()
        _ = seed_room_items(persistence.list_rooms(), factory, cast(RoomDropSink, room_manager))
    except (DatabaseError, ValidationError, SQLAlchemyError) as e:
        logger.error("Room item seeding failed; continuing startup", error=str(e))
