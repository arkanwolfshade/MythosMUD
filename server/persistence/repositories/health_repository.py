"""
Health repository for async persistence operations.

This module provides async database operations for player health management
including damage, healing, and DP updates using SQLAlchemy ORM with PostgreSQL.
"""

import uuid

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_async_session
from server.exceptions import DatabaseError
from server.logging.enhanced_logging_config import get_logger
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
            current_db = stats.get("current_db", 100)
            new_health = max(0, current_db - amount)

            # Update the in-memory player object (for immediate UI feedback)
            stats["current_db"] = new_health
            player.set_stats(stats)

            # Atomic database update
            await self.update_player_health(player.player_id, -amount, f"damage:{damage_type}")  # type: ignore[arg-type]

            self._logger.info(
                "Player health reduced atomically",
                player_id=player.player_id,
                player_name=player.name,
                damage=amount,
                old_health=current_db,
                new_health=new_health,
                damage_type=damage_type,
            )
        except ValueError:
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to persist player damage",
                player_id=player.player_id,
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
            current_db = stats.get("current_db", 100)
            # NOTE: Max health is currently hardcoded; future enhancement will make it configurable
            max_health = 100
            new_health = min(max_health, current_db + amount)

            # Update the in-memory player object (for immediate UI feedback)
            stats["current_db"] = new_health
            player.set_stats(stats)

            # Atomic database update
            await self.update_player_health(player.player_id, amount, "healing")  # type: ignore[arg-type]

            self._logger.info(
                "Player health increased atomically",
                player_id=player.player_id,
                player_name=player.name,
                healing=amount,
                old_health=current_db,
                new_health=new_health,
            )
        except ValueError:
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to persist player healing",
                player_id=player.player_id,
                player_name=player.name,
                amount=amount,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise

    async def update_player_health(self, player_id: uuid.UUID, delta: int, reason: str = "") -> None:
        """
        Update player current_db field atomically.

        Args:
            player_id: Player UUID
            delta: Health change amount (positive for heal, negative for damage)
            reason: Reason for health change (for logging)

        Raises:
            DatabaseError: If database operation fails
        """
        context = create_error_context()
        context.metadata["operation"] = "update_player_health"
        context.metadata["player_id"] = player_id
        context.metadata["delta"] = delta
        context.metadata["reason"] = reason

        try:
            async for session in get_async_session():
                # Use JSON path update for atomic health modification
                # This prevents race conditions by updating only the current_db field
                update_query = text(
                    """
                    UPDATE players
                    SET stats = jsonb_set(
                        stats,
                        '{current_db}',
                        (GREATEST(0, LEAST(100, (stats->>'current_db')::int + :delta)))::text::jsonb
                    )
                    WHERE player_id = :player_id
                    """
                )

                await session.execute(update_query, {"player_id": player_id, "delta": delta})
                await session.commit()

                self._logger.debug(
                    "Atomically updated player health",
                    player_id=player_id,
                    delta=delta,
                    reason=reason,
                )
                return
            return
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating player health: {e}",
                context=context,
                details={"player_id": player_id, "delta": delta, "reason": reason, "error": str(e)},
                user_friendly="Failed to update player health",
            )
