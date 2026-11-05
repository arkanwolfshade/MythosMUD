"""
MP regeneration service for passive and active magic point recovery.

This module handles automatic MP regeneration over time and integration
with rest/meditation commands for accelerated recovery. MP itself changes through the player registry
(PlayerMpService, ADR-029 step 6b). Regeneration runs on every tick, so it accrues the fraction here and only writes
when a whole MP has built up; a restart loses at most one MP's worth of progress.
"""

import uuid
from typing import TYPE_CHECKING, Any, Protocol, cast

from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.game.player_registry import PlayerNotFoundError
from server.game.player_service import PlayerService
from server.models.player import Player
from server.models.player_mp import MpChange, max_mp_of, mp_of
from server.services.player_mp_service import PlayerMpService, announce_mp
from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.game.player_registry import PlayerRegistry

logger = get_logger(__name__)

# Default MP regeneration rates (per tick)
# NOTE: Server tick rate is 0.1 seconds, so 0.01 MP per tick = 0.1 MP per second = 6 MP per minute
DEFAULT_MP_REGEN_RATE = 0.01  # 0.01 MP per tick (tick = 0.1s, so ~6 MP per minute)
REST_MP_REGEN_MULTIPLIER = 3.0  # 3x faster when resting
MEDITATION_MP_REGEN_MULTIPLIER = 5.0  # 5x faster when meditating


class _PlayerReader(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """The slice of the persistence layer the regeneration tick reads."""

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        """The player's row, or None."""


class MPRegenerationService:
    """
    Service for managing MP regeneration.

    Handles passive regeneration over time and accelerated regeneration
    during rest/meditation.
    """

    def __init__(
        self,
        player_service: PlayerService,
        regen_rate: float = DEFAULT_MP_REGEN_RATE,
        player_registry: "PlayerRegistry | None" = None,
    ) -> None:
        """
        Initialize the MP regeneration service.

        Args:
            player_service: Player service for stat modifications
            regen_rate: Base MP regeneration rate per tick (default 0.1)
            player_registry: Holds the player's MP; without it nothing regenerates or is restored
        """
        self.player_service = player_service
        self.regen_rate = regen_rate
        self._mp: PlayerMpService | None = PlayerMpService(player_registry) if player_registry is not None else None
        self._accrued: dict[uuid.UUID, float] = {}
        logger.info("MPRegenerationService initialized", regen_rate=regen_rate)

    async def process_tick_regeneration(self, player_id: uuid.UUID) -> dict[str, Any]:
        """
        Process MP regeneration for a player on a game tick.

        The row read is what this tick has always cost; a registry unit (several reads and a commit) only opens when
        a whole MP has accrued.

        Args:
            player_id: Player ID

        Returns:
            dict: Result with MP restored and current/max MP
        """
        player = await cast(_PlayerReader, self.player_service.persistence).get_player_by_id(player_id)
        if not player:
            _ = self._accrued.pop(player_id, None)
            return {"mp_restored": 0, "current_mp": 0, "max_mp": 0}

        stats = player.get_stats()
        current_mp, max_mp = mp_of(stats), max_mp_of(stats)

        # Already at max, no regeneration needed
        if current_mp >= max_mp or self._mp is None:
            _ = self._accrued.pop(player_id, None)
            return {"mp_restored": 0, "current_mp": current_mp, "max_mp": max_mp}

        regen_multiplier = self._get_regen_multiplier(stats)
        accrued = self._accrued.get(player_id, 0.0) + self.regen_rate * regen_multiplier
        whole = int(accrued)
        self._accrued[player_id] = accrued - whole
        if whole < 1:
            return {"mp_restored": 0, "current_mp": current_mp, "max_mp": max_mp}

        try:
            change = await self._mp.restore(player_id, whole)
        except PlayerNotFoundError:
            _ = self._accrued.pop(player_id, None)
            return {"mp_restored": 0, "current_mp": 0, "max_mp": 0}
        except (DatabaseError, SQLAlchemyError) as e:
            self._accrued[player_id] += whole  # not written: the next tick tries again
            logger.warning("Failed to write MP regeneration", player_id=player_id, error=str(e))
            return {"mp_restored": 0, "current_mp": current_mp, "max_mp": max_mp}

        logger.debug(
            "MP regenerated",
            player_id=player_id,
            mp_restored=change.gained,
            current_mp=change.new_mp,
            max_mp=change.max_mp,
            multiplier=regen_multiplier,
        )

        if change.gained > 0:
            await announce_mp(player_id, change)

        return {"mp_restored": change.gained, "current_mp": change.new_mp, "max_mp": change.max_mp}

    def _get_regen_multiplier(self, stats: dict[str, Any]) -> float:
        """
        Get MP regeneration multiplier based on player state.

        Args:
            stats: Player stats dictionary

        Returns:
            float: Regeneration multiplier
        """
        position = stats.get("position", "standing")

        # Check for meditation (would be in status effects or a flag)
        # For now, check position - sitting/lying = rest, meditation would be a status effect
        if position == "sitting":
            return REST_MP_REGEN_MULTIPLIER
        if position == "lying":
            return REST_MP_REGEN_MULTIPLIER * 1.2  # Slightly better when lying

        # Check for meditation status effect
        # TODO: Check status effects for meditation when status effect system supports it  # pylint: disable=fixme  # Reason: Feature placeholder for status effect system integration
        # For now, base rate only

        return 1.0  # Base rate

    async def _restore(self, player_id: uuid.UUID, amount: float) -> MpChange | None:
        """Restore MP as one registry unit; None without a registry or with no such player."""
        if self._mp is None:
            logger.error("No player registry; cannot restore MP", player_id=player_id)
            return None
        try:
            return await self._mp.restore(player_id, amount)
        except PlayerNotFoundError:
            return None

    async def restore_mp_from_rest(self, player_id: uuid.UUID, duration_seconds: int = 60) -> dict[str, Any]:
        """
        Restore MP from resting (accelerated regeneration).

        Args:
            player_id: Player ID
            duration_seconds: Duration of rest in seconds

        Returns:
            dict: Result with MP restored
        """
        change = await self._restore(player_id, self.regen_rate * REST_MP_REGEN_MULTIPLIER * duration_seconds)
        if change is None:
            return {"success": False, "message": "Player not found", "mp_restored": 0}
        if change.old_mp >= change.max_mp:
            return {"success": True, "message": "Your magic points are already full.", "mp_restored": 0}

        logger.info(
            "MP restored from rest",
            player_id=player_id,
            mp_restored=change.gained,
            duration=duration_seconds,
        )

        return {
            "success": True,
            "message": f"You rest and recover {change.gained} magic points.",
            "mp_restored": change.gained,
            "current_mp": change.new_mp,
            "max_mp": change.max_mp,
        }

    async def restore_mp_from_meditation(self, player_id: uuid.UUID, duration_seconds: int = 180) -> dict[str, Any]:
        """
        Restore MP from meditation (highly accelerated regeneration).

        Args:
            player_id: Player ID
            duration_seconds: Duration of meditation in seconds

        Returns:
            dict: Result with MP restored
        """
        change = await self._restore(player_id, self.regen_rate * MEDITATION_MP_REGEN_MULTIPLIER * duration_seconds)
        if change is None:
            return {"success": False, "message": "Player not found", "mp_restored": 0}
        if change.old_mp >= change.max_mp:
            return {"success": True, "message": "Your magic points are already full.", "mp_restored": 0}

        logger.info(
            "MP restored from meditation",
            player_id=player_id,
            mp_restored=change.gained,
            duration=duration_seconds,
        )

        return {
            "success": True,
            "message": f"Through meditation, you recover {change.gained} magic points.",
            "mp_restored": change.gained,
            "current_mp": change.new_mp,
            "max_mp": change.max_mp,
        }

    async def restore_mp_from_item(self, player_id: uuid.UUID, amount: int) -> dict[str, Any]:
        """
        Restore MP from consuming an item.

        Args:
            player_id: Player ID
            amount: Amount of MP to restore

        Returns:
            dict: Result with MP restored
        """
        # Use MagicService.restore_mp if available, otherwise do it directly
        if hasattr(self.player_service, "magic_service") and self.player_service.magic_service:
            return cast(dict[str, Any], await self.player_service.magic_service.restore_mp(player_id, amount))

        change = await self._restore(player_id, amount)
        if change is None:
            return {"success": False, "message": "Player not found", "mp_restored": 0}

        return {
            "success": True,
            "message": f"You restore {change.gained} magic points.",
            "mp_restored": change.gained,
            "current_mp": change.new_mp,
            "max_mp": change.max_mp,
        }
