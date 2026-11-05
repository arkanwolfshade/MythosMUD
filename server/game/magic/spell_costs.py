"""
Spell cost application service.

This module handles applying spell costs (MP, lucidity, corruption) to players.
"""

import uuid
from typing import TYPE_CHECKING, Any, Protocol, cast

from sqlalchemy.exc import SQLAlchemyError

from server.game.player_registry import PlayerNotFoundError
from server.game.player_service import PlayerService
from server.models.player import Player
from server.models.spell import Spell
from server.services.corruption_service import CorruptionPersistence
from server.services.player_mp_service import PlayerMpService
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.game.player_registry import PlayerRegistry

logger = get_logger(__name__)


class LucidityPersistence(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """The slice of AsyncPersistenceLayer spell costs use to spend lucidity."""

    async def apply_lucidity_loss(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Lower the player's lucidity through LucidityService."""


class SpellCostsService:
    """
    Service for applying spell costs.

    Handles MP, lucidity, and corruption costs for spellcasting.
    """

    def __init__(self, player_service: PlayerService, player_registry: "PlayerRegistry | None" = None) -> None:
        """
        Initialize the spell costs service.

        Args:
            player_service: Player service for accessing player data
            player_registry: Holds the player's MP (ADR-029 step 6b)
        """
        self.player_service = player_service
        self._player_registry: "PlayerRegistry | None" = player_registry

    def _mp(self) -> PlayerMpService:
        if self._player_registry is None:  # never fall back to writing stats directly
            raise RuntimeError("Player registry not wired; cannot change MP")
        return PlayerMpService(self._player_registry)

    async def _spend_lucidity_if_required(self, player: Player, spell: Spell) -> None:
        """Spend the lucidity cost of a Mythos spell that requires it, through player_lucidity (ADR-029 step 3a)."""
        if not (spell.is_mythos() and spell.requires_lucidity()):
            return
        persistence = cast(LucidityPersistence, self.player_service.persistence)
        await persistence.apply_lucidity_loss(player, spell.lucidity_cost, f"spell_cast:{spell.spell_id}")
        logger.debug("Spent lucidity", spell_id=spell.spell_id, lucidity_cost=spell.lucidity_cost)

    async def _apply_corruption_if_mythos(self, player_id: uuid.UUID, spell: Spell) -> None:
        """Apply corruption via CorruptionService for Mythos spells that carry a corruption cost.

        #804: route through CorruptionService, not a direct stats["corruption"] mutation -- it
        clamps 0..100, logs the ledger row, and updates the tier cache.
        """
        if not (spell.is_mythos() and spell.corruption_on_cast > 0):
            return
        # `self.player_service.persistence` is typed Any (pre-existing); cast() avoids reportAny.
        persistence = cast(CorruptionPersistence, self.player_service.persistence)
        _ = await persistence.adjust_corruption(
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

        # Spend MP, then lucidity and corruption: each is its own registry unit.
        change = await self._mp().spend(player_id, spell.mp_cost)
        logger.debug("Spent MP", player_id=player_id, mp_cost=spell.mp_cost, remaining_mp=change.new_mp)

        await self._spend_lucidity_if_required(cast(Player, player), spell)
        await self._apply_corruption_if_mythos(player_id, spell)
        await self._notify_mp_update(player_id, spell, stats, change.old_mp, change.new_mp)

    async def restore_mp(self, player_id: uuid.UUID, amount: int) -> dict[str, Any]:
        """
        Restore magic points to a player.

        Args:
            player_id: Player ID
            amount: Amount of MP to restore

        Returns:
            dict: Result message
        """
        try:
            change = await self._mp().restore(player_id, amount)
        except PlayerNotFoundError:
            return {"success": False, "message": "Player not found"}

        return {
            "success": True,
            "message": f"Restored {change.gained} MP",
            "current_mp": change.new_mp,
            "max_mp": change.max_mp,
        }
