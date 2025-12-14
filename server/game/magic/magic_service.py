"""
Core magic service for spellcasting.

This module provides the main magic service that handles MP management,
spell validation, casting rolls, and cost application.
"""

import random
import uuid
from typing import Any

from server.game.magic.spell_effects import SpellEffects
from server.game.magic.spell_registry import SpellRegistry
from server.game.magic.spell_targeting import SpellTargetingService
from server.game.player_service import PlayerService
from server.logging.enhanced_logging_config import get_logger
from server.models.spell import Spell
from server.persistence.repositories.player_spell_repository import PlayerSpellRepository

logger = get_logger(__name__)


class MagicService:
    """
    Core magic service for spellcasting operations.

    Handles MP management, spell validation, casting mechanics,
    and coordinates with other services for spell effects.
    """

    def __init__(
        self,
        spell_registry: SpellRegistry,
        player_service: PlayerService,
        spell_targeting_service: SpellTargetingService,
        spell_effects: SpellEffects,
        player_spell_repository: PlayerSpellRepository | None = None,
        spell_learning_service=None,
    ):
        """
        Initialize the magic service.

        Args:
            spell_registry: Registry for spell lookups
            player_service: Player service for stat modifications
            spell_targeting_service: Service for target resolution
            spell_effects: Engine for processing spell effects
            player_spell_repository: Optional repository for mastery tracking
            spell_learning_service: Optional spell learning service for mastery progression
        """
        self.spell_registry = spell_registry
        self.player_service = player_service
        self.spell_targeting_service = spell_targeting_service
        self.spell_effects = spell_effects
        self.player_spell_repository = player_spell_repository or PlayerSpellRepository()
        self.spell_learning_service = spell_learning_service
        logger.info("MagicService initialized")

    async def can_cast_spell(self, player_id: uuid.UUID, spell: Spell) -> tuple[bool, str]:
        """
        Check if a player can cast a spell.

        Args:
            player_id: Player ID
            spell: Spell to check

        Returns:
            tuple[bool, str]: (can_cast, error_message)
        """
        # Get player
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return False, "You are not recognized by the cosmic forces."

        stats = player.get_stats()

        # Check MP cost
        current_mp = stats.get("magic_points", 0)
        if current_mp < spell.mp_cost:
            return False, f"Not enough magic points. You need {spell.mp_cost} MP, but only have {current_mp}."

        # Check lucidity cost for Mythos spells
        if spell.is_mythos() and spell.requires_lucidity():
            current_lucidity = stats.get("lucidity", 100)
            if current_lucidity < spell.lucidity_cost:
                return (
                    False,
                    f"Not enough lucidity. You need {spell.lucidity_cost} lucidity, but only have {current_lucidity}.",
                )

        # Check if player knows the spell
        player_spell = await self.player_spell_repository.get_player_spell(player_id, spell.spell_id)
        if not player_spell:
            return False, f"You have not learned {spell.name}."

        # Check materials
        if spell.materials:
            missing_materials = await self._check_materials(player_id, spell)
            if missing_materials:
                material_list = ", ".join(missing_materials)
                return False, f"You are missing required materials: {material_list}."

        return True, ""

    async def cast_spell(self, player_id: uuid.UUID, spell_id: str, target_name: str | None = None) -> dict[str, Any]:
        """
        Cast a spell.

        Args:
            player_id: Player ID
            spell_id: Spell ID to cast
            target_name: Optional target name

        Returns:
            dict: Result with success, messages, and effect details
        """
        logger.info("Casting spell", player_id=player_id, spell_id=spell_id, target_name=target_name)

        # Get spell from registry
        spell = self.spell_registry.get_spell(spell_id)
        if not spell:
            # Try by name
            spell = self.spell_registry.get_spell_by_name(spell_id)
            if not spell:
                return {"success": False, "message": f"Spell '{spell_id}' not found."}

        # Check if can cast
        can_cast, error_msg = await self.can_cast_spell(player_id, spell)
        if not can_cast:
            return {"success": False, "message": error_msg}

        # Resolve target
        target, target_error = await self.spell_targeting_service.resolve_spell_target(player_id, spell, target_name)
        if not target:
            return {"success": False, "message": target_error}

        # Get player spell for mastery
        player_spell = await self.player_spell_repository.get_player_spell(player_id, spell.spell_id)
        mastery = int(player_spell.mastery) if player_spell else 0

        # Consume materials (before casting roll, so materials are consumed even on failure)
        if spell.materials:
            material_result = await self._consume_materials(player_id, spell)
            if not material_result.get("success"):
                return {"success": False, "message": material_result.get("message", "Failed to consume materials.")}

        # Perform casting roll (simplified CoC mechanics)
        casting_success = await self._casting_roll(player_id, spell, mastery)
        if not casting_success:
            # Still pay costs on failure
            await self._apply_costs(player_id, spell)
            return {
                "success": False,
                "message": f"{spell.name} failed! The cosmic forces resist your incantation.",
                "costs_paid": True,
            }

        # Apply costs
        await self._apply_costs(player_id, spell)

        # Process effect
        effect_result = await self.spell_effects.process_effect(spell, target, player_id, mastery)

        # Record spell cast
        await self.player_spell_repository.record_spell_cast(player_id, spell.spell_id)

        # Increase mastery on successful cast
        if self.spell_learning_service:
            await self.spell_learning_service.increase_mastery_on_cast(player_id, spell.spell_id, casting_success)

        # Combine results
        return {
            "success": True,
            "message": effect_result.get("message", f"{spell.name} cast successfully."),
            "spell_name": spell.name,
            "target": target.target_name,
            "effect_result": effect_result,
            "mastery": mastery,
        }

    async def _casting_roll(self, player_id: uuid.UUID, spell: Spell, mastery: int) -> bool:
        """
        Perform a casting roll (simplified CoC mechanics).

        Args:
            player_id: Player ID
            spell: Spell being cast
            mastery: Mastery level (0-100)

        Returns:
            bool: True if casting succeeds
        """
        # Get player stats
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return False

        stats = player.get_stats()
        intelligence = stats.get("intelligence", 50)

        # Base success chance: Intelligence + mastery
        # Simplified: roll d100, succeed if roll <= (intelligence + mastery)
        base_chance = intelligence + mastery
        roll = random.randint(1, 100)

        success = roll <= base_chance
        logger.debug(
            "Casting roll",
            player_id=player_id,
            spell_id=spell.spell_id,
            intelligence=intelligence,
            mastery=mastery,
            base_chance=base_chance,
            roll=roll,
            success=success,
        )

        return success

    async def _apply_costs(self, player_id: uuid.UUID, spell: Spell) -> None:
        """
        Apply spell costs (MP and lucidity if Mythos).

        Args:
            player_id: Player ID
            spell: Spell being cast
        """
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return

        stats = player.get_stats()

        # Spend MP
        current_mp = stats.get("magic_points", 0)
        new_mp = max(0, current_mp - spell.mp_cost)
        stats["magic_points"] = new_mp
        logger.debug("Spent MP", player_id=player_id, mp_cost=spell.mp_cost, remaining_mp=new_mp)

        # Spend lucidity for Mythos spells
        if spell.is_mythos() and spell.requires_lucidity():
            current_lucidity = stats.get("lucidity", 100)
            new_lucidity = max(0, current_lucidity - spell.lucidity_cost)
            stats["lucidity"] = new_lucidity
            logger.debug(
                "Spent lucidity",
                player_id=player_id,
                lucidity_cost=spell.lucidity_cost,
                remaining_lucidity=new_lucidity,
            )

        # Apply corruption if Mythos spell
        if spell.is_mythos() and spell.corruption_on_cast > 0:
            current_corruption = stats.get("corruption", 0)
            stats["corruption"] = current_corruption + spell.corruption_on_cast
            logger.debug(
                "Applied corruption",
                player_id=player_id,
                corruption_gained=spell.corruption_on_cast,
                total_corruption=stats["corruption"],
            )

        # Save player
        await self.player_service.persistence.save_player(player)

    async def restore_mp(self, player_id: uuid.UUID, amount: int) -> dict[str, Any]:
        """
        Restore magic points to a player.

        Args:
            player_id: Player ID
            amount: Amount of MP to restore

        Returns:
            dict: Result message
        """
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return {"success": False, "message": "Player not found"}

        stats = player.get_stats()
        current_mp = stats.get("magic_points", 0)
        max_mp = stats.get("max_magic_points", 10)  # Fallback if not computed

        # Calculate max_mp from power if not present
        if "max_magic_points" not in stats:
            import math

            power = stats.get("power", 50)
            max_mp = math.ceil(power * 0.2)

        new_mp = min(max_mp, current_mp + amount)
        stats["magic_points"] = new_mp

        await self.player_service.persistence.save_player(player)

        return {
            "success": True,
            "message": f"Restored {new_mp - current_mp} MP",
            "current_mp": new_mp,
            "max_mp": max_mp,
        }

    async def _check_materials(self, player_id: uuid.UUID, spell: Spell) -> list[str]:
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

    async def _consume_materials(self, player_id: uuid.UUID, spell: Spell) -> dict[str, Any]:
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
