"""
Spell material handling service.

This module handles checking and consuming spell materials from player inventory.
"""

import uuid
from typing import Any

from server.game.player_service import PlayerService
from server.structured_logging.enhanced_logging_config import get_logger
from server.models.spell import Spell

logger = get_logger(__name__)


class SpellMaterialsService:
    """
    Service for handling spell material requirements.

    Handles checking if players have required materials and consuming them.
    """

    def __init__(self, player_service: PlayerService):
        """
        Initialize the spell materials service.

        Args:
            player_service: Player service for accessing player data
        """
        self.player_service = player_service

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

        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return {"success": False, "message": "Player not found."}

        inventory = player.get_inventory()
        consumed_items = []
        final_inventory = []
        processed_materials = set()

        # Process each material requirement
        for material in spell.materials:
            material_id = material.item_id
            found = False

            # Find matching item in inventory
            for i, item in enumerate(inventory):
                if i in processed_materials:
                    continue

                item_id = item.get("item_id") or item.get("prototype_id", "")
                if item_id == material_id:
                    processed_materials.add(i)

                    if material.consumed:
                        # Consume the material
                        quantity = item.get("quantity", 1)
                        if quantity > 1:
                            # Reduce quantity
                            updated_item = item.copy()
                            updated_item["quantity"] = quantity - 1
                            final_inventory.append(updated_item)
                        # If quantity == 1, don't add to final_inventory (item is consumed)
                        consumed_items.append(material_id)
                    else:
                        # Reusable material - keep it in inventory
                        final_inventory.append(item)

                    found = True
                    break

            if not found:
                return {
                    "success": False,
                    "message": f"Missing required material: {material_id}.",
                }

        # Add all items that weren't materials
        for i, item in enumerate(inventory):
            if i not in processed_materials:
                final_inventory.append(item)

        # Update player inventory
        player.set_inventory(final_inventory)
        await self.player_service.persistence.save_player(player)

        if consumed_items:
            logger.info(
                "Consumed spell materials",
                player_id=player_id,
                spell_id=spell.spell_id,
                materials=consumed_items,
            )

        return {"success": True, "message": "", "consumed": consumed_items}
