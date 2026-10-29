"""
Spell material handling service.

This module handles checking and consuming spell materials from player inventory.
"""

import uuid
from typing import Any

from server.game.player_registry import PlayerNotFoundError, PlayerRegistry
from server.game.player_service import PlayerService
from server.models.spell import Spell
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class SpellMaterialsService:
    """
    Service for handling spell material requirements.

    Handles checking if players have required materials and consuming them.
    """

    def __init__(self, player_service: PlayerService, player_registry: PlayerRegistry | None = None) -> None:
        """
        Initialize the spell materials service.

        Args:
            player_service: Player service for accessing player data
            player_registry: Commits consumed materials (ADR-029); without it, nothing can be consumed
        """
        self.player_service = player_service
        self.player_registry: PlayerRegistry | None = player_registry

    async def check_materials(self, player_id: uuid.UUID, spell: Spell) -> list[str]:
        """
        Check if player has all required materials.

        Args:
            player_id: Player ID
            spell: Spell to check materials for

        Returns:
            list[str]: List of missing material item IDs (empty if all present)
        """
        if not spell.materials:
            return []

        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return [material.item_id for material in spell.materials]

        inventory = player.get_inventory()
        missing = []

        for material in spell.materials:
            # Check if player has this item in inventory
            found = False
            for item in inventory:
                # Match by item_id or prototype_id
                item_id = item.get("item_id") or item.get("prototype_id", "")
                if item_id == material.item_id:
                    found = True
                    break

            if not found:
                missing.append(material.item_id)

        return missing

    def _process_material_requirement(
        self, material: Any, inventory: list[dict[str, Any]], processed_materials: set[int]
    ) -> tuple[bool, int | None, bool]:
        """
        Process a single material requirement.

        Args:
            material: Material requirement
            inventory: Player inventory
            processed_materials: Set of already processed inventory indices

        Returns:
            Tuple of (found, inventory_index, should_consume)
        """
        material_id = material.item_id

        for i, item in enumerate(inventory):
            if i in processed_materials:
                continue

            item_id = item.get("item_id") or item.get("prototype_id", "")
            if item_id == material_id:
                return True, i, material.consumed

        return False, None, False

    def _consume_material_item(
        self, item: dict[str, Any], _material_id: str, consumed: bool
    ) -> tuple[dict[str, Any] | None, bool]:
        """
        Consume a material item.

        Args:
            item: Inventory item
            material_id: Material ID
            consumed: Whether material should be consumed

        Returns:
            Tuple of (updated_item_or_none, was_consumed)
        """
        if not consumed:
            return item, False

        quantity = item.get("quantity", 1)
        if quantity > 1:
            updated_item = item.copy()
            updated_item["quantity"] = quantity - 1
            return updated_item, True

        return None, True

    def _build_final_inventory(
        self, inventory: list[dict[str, Any]], processed_materials: set[int], final_inventory: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """
        Build final inventory with consumed materials removed.

        Args:
            inventory: Original inventory
            processed_materials: Set of processed material indices
            final_inventory: Inventory items already processed

        Returns:
            Final inventory list
        """
        for i, item in enumerate(inventory):
            if i not in processed_materials:
                final_inventory.append(item)

        return final_inventory

    def _plan_consumption(
        self, inventory: list[dict[str, object]], spell: Spell
    ) -> tuple[list[dict[str, object]] | None, list[str], str]:
        """The inventory once the spell's materials are taken and what was consumed, or (None, [], missing id)."""
        consumed_items: list[str] = []
        final_inventory: list[dict[str, object]] = []
        processed_materials: set[int] = set()

        for material in spell.materials:
            found, item_index, should_consume = self._process_material_requirement(
                material, inventory, processed_materials
            )
            if not found or item_index is None:
                return None, [], material.item_id

            processed_materials.add(item_index)
            updated_item, was_consumed = self._consume_material_item(
                inventory[item_index], material.item_id, should_consume
            )
            if updated_item is not None:
                final_inventory.append(updated_item)
            if was_consumed:
                consumed_items.append(material.item_id)

        return self._build_final_inventory(inventory, processed_materials, final_inventory), consumed_items, ""

    async def consume_materials(self, player_id: uuid.UUID, spell: Spell) -> dict[str, Any]:
        """
        Consume spell materials from player inventory.

        Args:
            player_id: Player ID
            spell: Spell being cast

        Returns:
            dict: Result with success status and message
        """
        if not spell.materials:
            return {"success": True, "message": ""}
        if self.player_registry is None:
            return {"success": False, "message": "Player not found."}

        try:
            # One registry unit (ADR-029 step 4c-i): the live stacks, committed before the spell goes on.
            async with self.player_registry.mutate(player_id) as player:
                final_inventory, consumed_items, missing = self._plan_consumption(
                    [dict(stack) for stack in player.inventory.carried], spell
                )
                if final_inventory is None:
                    return {"success": False, "message": f"Missing required material: {missing}."}
                player.inventory.set_carried(final_inventory)
        except PlayerNotFoundError:
            return {"success": False, "message": "Player not found."}

        if consumed_items:
            logger.info(
                "Consumed spell materials",
                player_id=player_id,
                spell_id=spell.spell_id,
                materials=consumed_items,
            )

        return {"success": True, "message": "", "consumed": consumed_items}
