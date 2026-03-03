"""
Experience repository for async persistence operations.

This module provides async database operations for player XP and stat management
using PostgreSQL stored procedures.
"""

import uuid
from typing import Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.player import Player
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


class ExperienceRepository:
    """
    Repository for player experience and stats persistence operations.

    Handles XP awards, stat updates, and leveling with atomic database
    operations to prevent race conditions.
    """

    # Field name to JSONB path for update_player_stat_field
    FIELD_NAME_TO_PATH: dict[str, list[str]] = {
        "current_dp": ["current_dp"],
        "lucidity": ["lucidity"],
        "occult_knowledge": ["occult_knowledge"],
        "fear": ["fear"],
        "corruption": ["corruption"],
        "cult_affiliation": ["cult_affiliation"],
        "strength": ["strength"],
        "dexterity": ["dexterity"],
        "constitution": ["constitution"],
        "intelligence": ["intelligence"],
        "wisdom": ["wisdom"],
        "charisma": ["charisma"],
    }

    def __init__(self, event_bus: Any = None) -> None:
        """
        Initialize the experience repository.

        Args:
            event_bus: Optional EventBus for publishing XP/level events
        """
        self._event_bus = event_bus
        self._logger = get_logger(__name__)

    async def gain_experience(self, player: Player, amount: int, source: str = "unknown") -> None:
        """
        Award experience points to a player atomically.

        Args:
            player: Player to award XP to
            amount: XP amount (must be non-negative)
            source: Source of XP for logging

        Raises:
            ValueError: If XP amount is invalid
            DatabaseError: If database operation fails
        """
        if amount < 0:
            raise ValueError(f"XP amount must be non-negative, got {amount}")

        try:
            # Update in-memory player object
            player.experience_points += amount

            # Atomic database update
            await self.update_player_xp(player.player_id, amount, source)

            self._logger.info(
                "Player gained experience atomically",
                player_id=str(player.player_id),
                player_name=player.name,
                amount=amount,
                source=source,
                new_total=int(player.experience_points),
            )

            # Publish event if event bus available
            if self._event_bus:
                from server.services.player_combat_service import PlayerXPAwardEvent

                event = PlayerXPAwardEvent(
                    player_id=uuid.UUID(str(player.player_id)),
                    xp_amount=amount,
                    new_level=int(player.level),
                )
                self._event_bus.publish(event)

        except ValueError:
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to persist player XP",
                player_id=str(player.player_id),
                player_name=player.name,
                amount=amount,
                source=source,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise

    async def update_player_xp(self, player_id: uuid.UUID | str, delta: int, reason: str = "") -> None:
        """
        Update player experience points atomically.

        Args:
            player_id: Player UUID or string
            delta: XP change amount (must be non-negative)
            reason: Reason for XP change

        Raises:
            ValueError: If delta is negative or player not found
            DatabaseError: If database operation fails
        """
        if delta < 0:
            raise ValueError(f"XP delta must be non-negative, got {delta}")

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT update_player_xp(:player_id, :delta)"),
                    {"player_id": str(player_id), "delta": delta},
                )
                rows_updated = result.scalar()
                if not rows_updated:
                    raise ValueError(f"Player {player_id} not found")

                await session.commit()

                self._logger.info(
                    "Player XP updated atomically",
                    player_id=str(player_id),
                    delta=delta,
                    reason=reason,
                )
        except (SQLAlchemyError, OSError, ValueError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating XP for player '{player_id}': {e}",
                operation="update_player_xp",
                player_id=str(player_id),
                details={"player_id": str(player_id), "delta": delta, "reason": reason, "error": str(e)},
                user_friendly="Failed to update player experience",
            )

    async def update_player_stat_field(
        self, player_id: uuid.UUID | str, field_name: str, delta: int | float, reason: str = ""
    ) -> None:
        """
        Update a specific numeric field in player stats atomically.

        Args:
            player_id: Player UUID or string
            field_name: Stat field name (must be in FIELD_NAME_TO_PATH)
            delta: Amount to change field by
            reason: Reason for update

        Raises:
            ValueError: If field_name invalid or delta type wrong
            DatabaseError: If database operation fails
        """
        if not isinstance(delta, (int, float)):
            raise TypeError(f"delta must be int or float, got {type(delta).__name__}")

        if field_name not in self.FIELD_NAME_TO_PATH:
            allowed_fields = set(self.FIELD_NAME_TO_PATH.keys())
            raise ValueError(f"Invalid stat field name: {field_name}. Must be one of {allowed_fields}")

        try:
            path = self.FIELD_NAME_TO_PATH[field_name]

            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT update_player_stat_field(:player_id, :path, :delta)"),
                    {"player_id": str(player_id), "path": path, "delta": delta},
                )
                rows_updated = result.scalar()
                if not rows_updated:
                    raise ValueError(f"Player {player_id} not found")

                await session.commit()

                self._logger.info(
                    "Player stat field updated atomically",
                    player_id=str(player_id),
                    field_name=field_name,
                    delta=delta,
                    reason=reason,
                )
        except (SQLAlchemyError, OSError, TypeError, ValueError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating stat field: {e}",
                operation="update_player_stat_field",
                player_id=str(player_id),
                field_name=field_name,
                details={
                    "player_id": str(player_id),
                    "field_name": field_name,
                    "delta": delta,
                    "reason": reason,
                    "error": str(e),
                },
                user_friendly="Failed to update player stats",
            )
