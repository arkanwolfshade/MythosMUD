"""
Health repository for async persistence operations.

This module provides async database operations for player health management
including damage, healing, and DP updates using SQLAlchemy ORM with PostgreSQL.
"""

import uuid

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from structlog.stdlib import BoundLogger

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.player import Player
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger: BoundLogger = get_logger(__name__)


def _stats_int(stats: dict[str, object], key: str, default: int) -> int:
    """Convert stat values to int with a safe fallback."""
    value = stats.get(key, default)
    if not isinstance(value, int | float | str):
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


class HealthRepository:
    """
    Repository for player health persistence operations.

    Handles damage, healing, and DP updates with atomic database operations
    to prevent race conditions.
    """

    def __init__(self, event_bus: object | None = None) -> None:
        """
        Initialize the health repository.

        Args:
            event_bus: Optional EventBus for publishing DP change events
        """
        self._event_bus: object | None = event_bus
        self._logger: BoundLogger = get_logger(__name__)

    def _calculate_effective_damage(
        self,
        stats: dict[str, object],
        amount: int,
        damage_type: str,
    ) -> int:
        """
        Calculate effective damage after applying simple resistance rules.

        Currently supports cold-style resistance via stats["cold_resistance"].
        """
        if amount <= 0:
            return 0

        effective_damage = amount

        # Simple cold-damage resistance hook:
        # Treat "cold" and "water" damage types as cold for resistance purposes.
        # Spells like Resist Cold can set a "cold_resistance" stat (0-100) which
        # reduces incoming cold damage by that percentage.
        if damage_type in {"cold", "water"}:
            raw_resist: object = stats.get("cold_resistance", 0)
            if isinstance(raw_resist, int | float | str):
                try:
                    resist_value = int(raw_resist)
                except (TypeError, ValueError):
                    resist_value = 0
            else:
                resist_value = 0
            if resist_value > 0:
                resist_clamped = max(0, min(100, resist_value))
                reduction_factor = resist_clamped / 100.0
                reduced = int(round(amount * (1.0 - reduction_factor)))
                # Ensure at least 1 damage still gets through when original > 0
                effective_damage = max(1, reduced)

        return effective_damage

    async def _damage_player_inner(self, player: Player, amount: int, damage_type: str) -> None:
        """Core damage logic without error handling wrapper."""
        stats = player.get_stats()
        current_dp = _stats_int(stats, "current_dp", 20)
        effective_damage = self._calculate_effective_damage(stats, amount, damage_type)
        new_dp = max(0, current_dp - effective_damage)

        stats["current_dp"] = new_dp
        player.set_stats(stats)

        await self.update_player_health(player.player_id, -effective_damage, f"damage:{damage_type}")

        self._logger.info(
            "Player health reduced atomically",
            player_id=str(player.player_id),
            player_name=player.name,
            damage=effective_damage,
            original_damage=amount,
            old_dp=current_dp,
            new_dp=new_dp,
            damage_type=damage_type,
        )

    def _log_damage_error(self, player: Player, amount: int, damage_type: str, error: Exception) -> None:
        """Log critical damage persistence failure."""
        self._logger.critical(
            "CRITICAL: Failed to persist player damage",
            player_id=str(player.player_id),
            player_name=player.name,
            amount=amount,
            damage_type=damage_type,
            error=str(error),
            error_type=type(error).__name__,
            exc_info=True,
        )

    async def _update_player_health_inner(self, player_id: uuid.UUID | str, delta: int, reason: str) -> None:
        """Execute atomic health update via update_player_health procedure."""
        session_maker = get_session_maker()
        async with session_maker() as session:
            _ = await session.execute(
                text("SELECT update_player_health(:player_id, :delta)"),
                {"player_id": str(player_id), "delta": delta},
            )
            await session.commit()

        self._logger.debug(
            "Atomically updated player health",
            player_id=str(player_id),
            delta=delta,
            reason=reason,
        )

    async def damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
        """
        Damage a player and persist health changes atomically.

        Args:
            player: Player to damage
            amount: Damage amount (must be positive)
            damage_type: Type of damage

        Raises:
            ValueError: If damage amount is invalid
            DatabaseError: If database operation fails
        """
        if amount < 0:
            raise ValueError(f"Damage amount must be positive, got {amount}")

        try:
            await self._damage_player_inner(player, amount, damage_type)
        except ValueError:
            raise
        except Exception as e:
            self._log_damage_error(player, amount, damage_type, e)
            raise

    async def heal_player(self, player: Player, amount: int) -> None:
        """Heal a player and persist health changes atomically."""
        if amount < 0:
            raise ValueError(f"Healing amount must be positive, got {amount}")

        try:
            await self._heal_player_inner(player, amount)
        except ValueError:
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to persist player healing",
                player_id=str(player.player_id),
                player_name=player.name,
                amount=amount,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise

    async def _heal_player_inner(self, player: Player, amount: int) -> None:
        """Core heal logic without error handling wrapper."""
        stats = player.get_stats()
        current_dp = _stats_int(stats, "current_dp", 100)
        constitution = _stats_int(stats, "constitution", 50)
        size = _stats_int(stats, "size", 50)
        con_size_dp = (constitution + size) // 5  # DP max = (CON + SIZ) / 5
        max_dp = _stats_int(stats, "max_dp", con_size_dp)
        if not max_dp:
            max_dp = 20  # Prevent division by zero
        new_dp = min(max_dp, current_dp + amount)
        actual_heal_amount = new_dp - current_dp  # Calculate actual amount healed (capped)

        stats["current_dp"] = new_dp
        player.set_stats(stats)

        # Atomic database update - use actual heal amount to ensure consistency
        # The SQL query will also cap at max_dp, but using actual_heal_amount ensures
        # the database matches the in-memory state
        if actual_heal_amount > 0:
            await self.update_player_health(player.player_id, actual_heal_amount, "healing")

            self._logger.info(
                "Player health increased atomically",
                player_id=str(player.player_id),
                player_name=player.name,
                healing=actual_heal_amount,
                requested_healing=amount,
                old_dp=current_dp,
                new_dp=new_dp,
                max_dp=max_dp,
            )

    async def update_player_health(self, player_id: uuid.UUID | str, delta: int, reason: str = "") -> None:
        """
        Update player current_dp field atomically.

        Args:
            player_id: Player UUID or string representation
            delta: Health change amount (positive for heal, negative for damage)
            reason: Reason for health change (for logging)

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            await self._update_player_health_inner(player_id, delta, reason)
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating player health: {e}",
                operation="update_player_health",
                player_id=str(player_id),
                delta=delta,
                reason=reason,
                details={"player_id": str(player_id), "delta": delta, "reason": reason, "error": str(e)},
                user_friendly="Failed to update player health",
            )
