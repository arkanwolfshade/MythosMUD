"""
MP regeneration service for passive and active magic point recovery.

This module handles automatic MP regeneration over time and integration
with rest/meditation commands for accelerated recovery.
"""

import math
import uuid
from typing import Any, cast

from sqlalchemy.exc import SQLAlchemyError

from server.game.player_service import PlayerService
from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Default MP regeneration rates (per tick)
# NOTE: Server tick rate is 0.1 seconds, so 0.01 MP per tick = 0.1 MP per second = 6 MP per minute
DEFAULT_MP_REGEN_RATE = 0.01  # 0.01 MP per tick (tick = 0.1s, so ~6 MP per minute)
REST_MP_REGEN_MULTIPLIER = 3.0  # 3x faster when resting
MEDITATION_MP_REGEN_MULTIPLIER = 5.0  # 5x faster when meditating


class MPRegenerationService:
    """
    Service for managing MP regeneration.

    Handles passive regeneration over time and accelerated regeneration
    during rest/meditation.
    """

    def __init__(self, player_service: PlayerService, regen_rate: float = DEFAULT_MP_REGEN_RATE):
        """
        Initialize the MP regeneration service.

        Args:
            player_service: Player service for stat modifications
            regen_rate: Base MP regeneration rate per tick (default 0.1)
        """
        self.player_service = player_service
        self.regen_rate = regen_rate
        logger.info("MPRegenerationService initialized", regen_rate=regen_rate)

    async def process_tick_regeneration(self, player_id: uuid.UUID) -> dict[str, Any]:
        """
        Process MP regeneration for a player on a game tick.

        Args:
            player_id: Player ID

        Returns:
            dict: Result with MP restored and current/max MP
        """
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return {"mp_restored": 0, "current_mp": 0, "max_mp": 0}

        stats = player.get_stats()
        current_mp = stats.get("magic_points", 0)

        # Calculate max_mp from power if not present
        if "max_magic_points" not in stats:
            power = stats.get("power", 50)
            max_mp = math.ceil(power * 0.2)
        else:
            max_mp = stats.get("max_magic_points", 10)

        # Already at max, no regeneration needed
        if current_mp >= max_mp:
            return {"mp_restored": 0, "current_mp": current_mp, "max_mp": max_mp}

        # Calculate regeneration rate (base rate, modified by position/activity)
        regen_multiplier = self._get_regen_multiplier(stats)
        mp_to_restore = self.regen_rate * regen_multiplier

        # Get fractional MP from stats (stored as _mp_fractional for accumulation)
        # If not present, initialize from current_mp (which might be fractional)
        mp_fractional = stats.get("_mp_fractional", 0.0)
        if isinstance(current_mp, float):
            # If current_mp is already fractional, extract the fractional part
            mp_fractional = current_mp - int(current_mp)
            current_mp = int(current_mp)

        # Add regeneration to fractional accumulator
        mp_fractional += mp_to_restore

        # Calculate new MP: integer part + accumulated fractional part
        mp_to_add = int(mp_fractional)  # Whole MP to add
        mp_fractional = mp_fractional - mp_to_add  # Remaining fractional part

        new_mp = min(max_mp, current_mp + mp_to_add)

        # Store fractional part for next tick
        stats["_mp_fractional"] = mp_fractional

        # Only update if there's actual change (avoid unnecessary saves)
        if new_mp > current_mp or mp_fractional > 0:
            stats["magic_points"] = new_mp  # Store as integer (fractional part stored separately)
            await self.player_service.persistence.save_player(player)

            mp_restored = new_mp - current_mp
            logger.debug(
                "MP regenerated",
                player_id=player_id,
                mp_restored=mp_restored,
                current_mp=new_mp,
                max_mp=max_mp,
                multiplier=regen_multiplier,
                mp_fractional=mp_fractional,
            )

            # Send player_update event to notify client of MP change
            if new_mp > current_mp:
                try:
                    from server.realtime.connection_manager_api import send_game_event

                    await send_game_event(
                        player_id,
                        "player_update",
                        {
                            "stats": {
                                "magic_points": new_mp,
                                "max_magic_points": max_mp,
                            },
                        },
                    )
                except (ValueError, AttributeError, SQLAlchemyError, OSError, TypeError, RuntimeError) as e:
                    logger.warning("Failed to send MP regeneration update event", player_id=player_id, error=str(e))

            return {"mp_restored": mp_restored, "current_mp": new_mp, "max_mp": max_mp}

        return {"mp_restored": 0, "current_mp": current_mp, "max_mp": max_mp}

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

    async def restore_mp_from_rest(self, player_id: uuid.UUID, duration_seconds: int = 60) -> dict[str, Any]:
        """
        Restore MP from resting (accelerated regeneration).

        Args:
            player_id: Player ID
            duration_seconds: Duration of rest in seconds

        Returns:
            dict: Result with MP restored
        """
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return {"success": False, "message": "Player not found", "mp_restored": 0}

        stats = player.get_stats()
        current_mp = stats.get("magic_points", 0)

        # Calculate max_mp
        if "max_magic_points" not in stats:
            power = stats.get("power", 50)
            max_mp = math.ceil(power * 0.2)
        else:
            max_mp = stats.get("max_magic_points", 10)

        if current_mp >= max_mp:
            return {"success": True, "message": "Your magic points are already full.", "mp_restored": 0}

        # Calculate MP to restore (rest multiplier * duration)
        mp_to_restore = self.regen_rate * REST_MP_REGEN_MULTIPLIER * duration_seconds
        new_mp = min(max_mp, current_mp + mp_to_restore)
        mp_restored = new_mp - current_mp

        stats["magic_points"] = int(new_mp)
        await self.player_service.persistence.save_player(player)

        logger.info(
            "MP restored from rest",
            player_id=player_id,
            mp_restored=mp_restored,
            duration=duration_seconds,
        )

        return {
            "success": True,
            "message": f"You rest and recover {int(mp_restored)} magic points.",
            "mp_restored": int(mp_restored),
            "current_mp": int(new_mp),
            "max_mp": max_mp,
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
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return {"success": False, "message": "Player not found", "mp_restored": 0}

        stats = player.get_stats()
        current_mp = stats.get("magic_points", 0)

        # Calculate max_mp
        if "max_magic_points" not in stats:
            power = stats.get("power", 50)
            max_mp = math.ceil(power * 0.2)
        else:
            max_mp = stats.get("max_magic_points", 10)

        if current_mp >= max_mp:
            return {"success": True, "message": "Your magic points are already full.", "mp_restored": 0}

        # Calculate MP to restore (meditation multiplier * duration)
        mp_to_restore = self.regen_rate * MEDITATION_MP_REGEN_MULTIPLIER * duration_seconds
        new_mp = min(max_mp, current_mp + mp_to_restore)
        mp_restored = new_mp - current_mp

        stats["magic_points"] = int(new_mp)
        await self.player_service.persistence.save_player(player)

        logger.info(
            "MP restored from meditation",
            player_id=player_id,
            mp_restored=mp_restored,
            duration=duration_seconds,
        )

        return {
            "success": True,
            "message": f"Through meditation, you recover {int(mp_restored)} magic points.",
            "mp_restored": int(mp_restored),
            "current_mp": int(new_mp),
            "max_mp": max_mp,
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

        # Fallback: direct restoration
        player = await self.player_service.persistence.get_player_by_id(player_id)
        if not player:
            return {"success": False, "message": "Player not found", "mp_restored": 0}

        stats = player.get_stats()
        current_mp = stats.get("magic_points", 0)

        # Calculate max_mp
        if "max_magic_points" not in stats:
            power = stats.get("power", 50)
            max_mp = math.ceil(power * 0.2)
        else:
            max_mp = stats.get("max_magic_points", 10)

        new_mp = min(max_mp, current_mp + amount)
        mp_restored = new_mp - current_mp

        stats["magic_points"] = int(new_mp)
        await self.player_service.persistence.save_player(player)

        return {
            "success": True,
            "message": f"You restore {mp_restored} magic points.",
            "mp_restored": mp_restored,
            "current_mp": int(new_mp),
            "max_mp": max_mp,
        }
