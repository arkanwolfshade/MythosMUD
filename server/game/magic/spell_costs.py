"""
Spell cost application service.

This module handles applying spell costs (MP, lucidity, corruption) to players.
"""

import uuid
from typing import Any, cast

from sqlalchemy.exc import SQLAlchemyError

from server.game.player_service import PlayerService
from server.models.spell import Spell
from server.services.corruption_service import CorruptionPersistenceProtocol, CorruptionService
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class SpellCostsService:
    """
    Service for applying spell costs.

    Handles MP, lucidity, and corruption costs for spellcasting.
    """

    def __init__(self, player_service: PlayerService) -> None:
        """
        Initialize the spell costs service.

        Args:
            player_service: Player service for accessing player data
        """
        self.player_service = player_service

    def _spend_lucidity_if_required(
        self,
        player_id: uuid.UUID,
        spell: Spell,
        # Reason: SERIALIZATION_BOUNDARY - stats is dict[str, Any] per player.get_stats()'s own
        # established, unsuppressed return type.
        # Appropriate because: same unsuppressed convention as this class's other stats-dict access.
        stats: dict[str, Any],  # pyright: ignore[reportExplicitAny]
    ) -> None:
        """Deduct lucidity cost in-place on stats, for Mythos spells that require it."""
        if not (spell.is_mythos() and spell.requires_lucidity()):
            return
        current_lucidity = cast(int, stats.get("lucidity", 100))
        new_lucidity = max(0, current_lucidity - spell.lucidity_cost)
        stats["lucidity"] = new_lucidity
        logger.debug(
            "Spent lucidity",
            player_id=player_id,
            lucidity_cost=spell.lucidity_cost,
            remaining_lucidity=new_lucidity,
        )

    async def _apply_corruption_if_mythos(self, player_id: uuid.UUID, spell: Spell) -> None:
        """Apply corruption via CorruptionService for Mythos spells that carry a corruption cost.

        #804: route through CorruptionService, not a direct stats["corruption"] mutation -- it
        clamps 0..100, logs the ledger row, and updates the tier cache.
        """
        if not (spell.is_mythos() and spell.corruption_on_cast > 0):
            return
        # `self.player_service.persistence` is typed Any (pre-existing); cast() avoids reportAny.
        persistence = cast(CorruptionPersistenceProtocol, self.player_service.persistence)
        _ = await CorruptionService(persistence).apply_corruption_adjustment(
            player_id,
            spell.corruption_on_cast,
            reason_code="spell_cast",
            metadata={"spell_id": spell.spell_id},
        )
        logger.debug("Applied corruption", player_id=player_id, corruption_gained=spell.corruption_on_cast)

    async def _notify_mp_update(
        self,
        player_id: uuid.UUID,
        spell: Spell,
        # Reason: SERIALIZATION_BOUNDARY - stats is dict[str, Any]; current_mp is Any from the
        # same stats.get() lookup in apply_costs, matching this class's established convention.
        # Appropriate because: same unsuppressed convention as _spend_lucidity_if_required above.
        stats: dict[str, Any],  # pyright: ignore[reportExplicitAny]
        current_mp: int,
        new_mp: int,
    ) -> None:
        """Send a player_update event so the client reflects the new MP (and current health)."""
        try:
            from server.realtime.connection_manager_api import send_game_event

            # Send full player stats update so client can update both MP and health
            await send_game_event(
                player_id,
                "player_update",
                {
                    "stats": {
                        "magic_points": new_mp,
                        "max_magic_points": stats.get("max_magic_points", 10),
                        "current_dp": stats.get("current_dp", 0),
                        "max_dp": stats.get("max_dp", 0),
                    },
                },
            )
            logger.debug(
                "Sent MP update event",
                player_id=player_id,
                old_mp=current_mp,
                new_mp=new_mp,
                mp_cost=spell.mp_cost,
            )
        except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError, RuntimeError) as e:
            # RuntimeError can occur when connection manager is not available (e.g., in tests)
            logger.warning("Failed to send MP update event", player_id=player_id, error=str(e))

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

        # Reason: SERIALIZATION_BOUNDARY - player is Any (self.player_service.persistence is Any,
        # pre-existing); get_stats() is called dynamically off it.
        # Appropriate because: same unsuppressed convention as this class's persistence casts.
        stats = cast(dict[str, Any], player.get_stats())  # pyright: ignore[reportAny, reportExplicitAny]

        # Spend MP
        current_mp = cast(int, stats.get("magic_points", 0))
        new_mp = max(0, current_mp - spell.mp_cost)
        stats["magic_points"] = new_mp
        logger.debug("Spent MP", player_id=player_id, mp_cost=spell.mp_cost, remaining_mp=new_mp)

        self._spend_lucidity_if_required(player_id, spell, stats)

        # Save player (MP and lucidity). Corruption is applied separately below, *after* this
        # save -- CorruptionService.apply_corruption_adjustment does its own read-modify-write
        # cycle on the persisted row, so applying it before this save would have this save's
        # stale local `stats` dict immediately overwrite the corruption change.
        await self.player_service.persistence.save_player(player)

        await self._apply_corruption_if_mythos(player_id, spell)
        await self._notify_mp_update(player_id, spell, stats, current_mp, new_mp)

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
