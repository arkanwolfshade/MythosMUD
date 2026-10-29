"""
Giving a player a new item, through the player registry (ADR-029 step 4c-i).

``ItemGranter.grant`` turns "give this player n of prototype P" into a real stack, built by the ItemFactory
(instance id, name, metadata, origin), carried in general inventory like a floor pickup, and committed in one
registry unit before it returns. Spells that create objects and quest "item" rewards use it, so any future content
that hands out items gets the same, validated path.
"""

from __future__ import annotations

import uuid
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import TYPE_CHECKING

from ...constants.inventory import CARRIED_SLOT_TYPE
from ..player_registry import PlayerRegistry
from .item_factory import ItemFactory, ItemFactoryError

if TYPE_CHECKING:
    from ...services.inventory_service import InventoryService


@dataclass
class ItemGranter:
    """Creates items in players' inventories (an ItemGiver). ``item_factory`` is a provider: the factory loads after the registry."""

    registry: PlayerRegistry
    item_factory: Callable[[], ItemFactory | None]
    inventory_service: InventoryService

    async def has_free_slot(self, player_id: uuid.UUID) -> bool:
        """True if the player could take one more stack (False for no such player)."""
        view = await self.registry.get(player_id)
        return view is not None and len(view.inventory.carried) < self.inventory_service.max_slots

    async def grant(
        self, player_id: uuid.UUID, prototype_id: str, quantity: int = 1, *, origin: Mapping[str, object]
    ) -> None:
        """Add ``quantity`` of a new ``prototype_id`` item to the player's carried stacks, committed.

        Raises ItemFactoryError (no factory, unknown prototype, bad quantity), InventoryCapacityError (no free slot)
        and PlayerNotFoundError; nothing is written in any of those cases.
        """
        factory = self.item_factory()
        if factory is None:
            raise ItemFactoryError("The item system is not available.")
        instance = factory.create_instance(
            prototype_id, quantity=quantity, origin=dict(origin), slot_type=CARRIED_SLOT_TYPE
        )
        stack = instance.to_inventory_stack()
        async with self.registry.mutate(player_id) as player:
            carried = self.inventory_service.add_stack(player.inventory.carried, stack)
            player.inventory.set_carried([dict(item) for item in carried])
