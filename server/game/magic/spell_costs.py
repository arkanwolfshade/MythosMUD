"""
Spell cost application service.

This module handles applying spell costs (MP, lucidity, corruption) to players.
"""

import uuid
from typing import Any

from server.game.player_service import PlayerService
from server.logging.enhanced_logging_config import get_logger
from server.models.spell import Spell

logger = get_logger(__name__)


class SpellCostsService:
    """
    Service for applying spell costs.

    Handles MP, lucidity, and corruption costs for spellcasting.
    """

    def __init__(self, player_service: PlayerService):
        """
        Initialize the spell costs service.

        Args:
            player_service: Player service for accessing player data
        """
        self.player_service = player_service

    async def apply_costs(self, player_id: uuid.UUID, spell: Spell) -> None:
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
