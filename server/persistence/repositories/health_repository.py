"""
Health repository for async persistence operations.

This module provides async database operations for player health management
including damage, healing, and DP updates using SQLAlchemy ORM with PostgreSQL.
"""

import uuid

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.structured_logging.enhanced_logging_config import get_logger
from server.models.player import Player
from server.utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


class HealthRepository:
    """
    Repository for player health persistence operations.

    Handles damage, healing, and DP updates with atomic database operations
    to prevent race conditions.
    """

    def __init__(self, event_bus=None):
        """
        Initialize the health repository.

        Args:
            event_bus: Optional EventBus for publishing DP change events
        """
        self._event_bus = event_bus
        self._logger = get_logger(__name__)

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
            # Get current stats from in-memory player object
            stats = player.get_stats()
            current_dp = stats.get("current_dp", 100)
            new_dp = max(0, current_dp - amount)

            # Update the in-memory player object (for immediate UI feedback)
            stats["current_dp"] = new_dp
            player.set_stats(stats)

            # Atomic database update
            # player.player_id may be str or Column depending on mypy's view
            await self.update_player_health(player.player_id, -amount, f"damage:{damage_type}")

            self._logger.info(
                "Player health reduced atomically",
                player_id=str(player.player_id),
                player_name=player.name,
                damage=amount,
                old_dp=current_dp,
                new_dp=new_dp,
                damage_type=damage_type,
            )
        except ValueError:
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to persist player damage",
                player_id=str(player.player_id),
                player_name=player.name,
                amount=amount,
                damage_type=damage_type,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise

    async def heal_player(self, player: Player, amount: int) -> None:
        """
        Heal a player and persist health changes atomically.

        Args:
            player: Player to heal
            amount: Healing amount (must be positive)

        Raises:
            ValueError: If healing amount is invalid
            DatabaseError: If database operation fails
        """
        if amount < 0:
            raise ValueError(f"Healing amount must be positive, got {amount}")

        try:
            # Get current stats from in-memory player object
            stats = player.get_stats()
            current_dp = stats.get("current_dp", 100)
            # Calculate max DP from CON + SIZ if available, otherwise use default
            constitution = stats.get("constitution", 50)
            size = stats.get("size", 50)
            max_dp = stats.get("max_dp", (constitution + size) // 5)  # DP max = (CON + SIZ) / 5
            if max_dp == 0:
                max_dp = 20  # Prevent division by zero
            new_dp = min(max_dp, current_dp + amount)
            actual_heal_amount = new_dp - current_dp  # Calculate actual amount healed (capped)

            # Update the in-memory player object (for immediate UI feedback)
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
        context = create_error_context()
        context.metadata["operation"] = "update_player_health"
        context.metadata["player_id"] = str(player_id)
        context.metadata["delta"] = delta
        context.metadata["reason"] = reason

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                # Use JSON path update for atomic health modification
                # This prevents race conditions by updating only the current_dp field
                # Calculate max_dp: use stats->>'max_dp' if present, otherwise (CON + SIZ) / 5, with fallback to 20 if 0
                # Cap healing at max_dp to prevent exceeding maximum health
                update_query = text(
                    """
                    UPDATE players
                    SET stats = jsonb_set(
                        stats,
                        '{current_dp}',
                        (
                            GREATEST(
                                0,
                                LEAST(
                                    GREATEST(
                                        COALESCE(
                                            (stats->>'max_dp')::int,
                                            ((COALESCE((stats->>'constitution')::int, 50) + COALESCE((stats->>'size')::int, 50)) / 5)
                                        ),
                                        20
                                    ),
                                    (stats->>'current_dp')::int + :delta
                                )
                            )
                        )::text::jsonb
                    )
                    WHERE player_id = :player_id
                    """
                )

                await session.execute(update_query, {"player_id": str(player_id), "delta": delta})
                await session.commit()

                self._logger.debug(
                    "Atomically updated player health",
                    player_id=str(player_id),
                    delta=delta,
                    reason=reason,
                )
                return
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating player health: {e}",
                context=context,
                details={"player_id": str(player_id), "delta": delta, "reason": reason, "error": str(e)},
                user_friendly="Failed to update player health",
            )
