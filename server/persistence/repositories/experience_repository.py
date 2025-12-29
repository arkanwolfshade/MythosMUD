"""
Experience repository for async persistence operations.

This module provides async database operations for player XP and stat management
using SQLAlchemy ORM with PostgreSQL.
"""

import uuid

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.player import Player
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


class ExperienceRepository:
    """
    Repository for player experience and stats persistence operations.

    Handles XP awards, stat updates, and leveling with atomic database
    operations to prevent race conditions.
    """

    # Field name to PostgreSQL array literal mapping for atomic updates
    FIELD_NAME_TO_ARRAY: dict[str, str] = {
        "current_dp": "ARRAY['current_dp']::text[]",
        "lucidity": "ARRAY['lucidity']::text[]",
        "occult_knowledge": "ARRAY['occult_knowledge']::text[]",
        "fear": "ARRAY['fear']::text[]",
        "corruption": "ARRAY['corruption']::text[]",
        "cult_affiliation": "ARRAY['cult_affiliation']::text[]",
        "strength": "ARRAY['strength']::text[]",
        "dexterity": "ARRAY['dexterity']::text[]",
        "constitution": "ARRAY['constitution']::text[]",
        "intelligence": "ARRAY['intelligence']::text[]",
        "wisdom": "ARRAY['wisdom']::text[]",
        "charisma": "ARRAY['charisma']::text[]",
    }

    def __init__(self, event_bus=None):
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

        context = create_error_context()
        context.metadata["operation"] = "update_player_xp"
        context.metadata["player_id"] = str(player_id)

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                update_query = text(
                    """
                    UPDATE players
                    SET experience_points = experience_points + :delta
                    WHERE player_id = :player_id
                    """
                )

                result = await session.execute(update_query, {"player_id": str(player_id), "delta": delta})

                if result.rowcount == 0:
                    raise ValueError(f"Player {player_id} not found")

                await session.commit()

                self._logger.info(
                    "Player XP updated atomically",
                    player_id=str(player_id),
                    delta=delta,
                    reason=reason,
                )
                return
        except (SQLAlchemyError, OSError, ValueError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating XP for player '{player_id}': {e}",
                context=context,
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
            field_name: Stat field name (must be in FIELD_NAME_TO_ARRAY)
            delta: Amount to change field by
            reason: Reason for update

        Raises:
            ValueError: If field_name invalid or delta type wrong
            DatabaseError: If database operation fails
        """
        # Validate delta type
        if not isinstance(delta, int | float):
            raise TypeError(f"delta must be int or float, got {type(delta).__name__}")

        # Validate field name (whitelist approach for security)
        if field_name not in self.FIELD_NAME_TO_ARRAY:
            allowed_fields = set(self.FIELD_NAME_TO_ARRAY.keys())
            raise ValueError(f"Invalid stat field name: {field_name}. Must be one of {allowed_fields}")

        context = create_error_context()
        context.metadata["operation"] = "update_player_stat_field"
        context.metadata["player_id"] = str(player_id)
        context.metadata["field_name"] = field_name

        try:
            # Get the PostgreSQL array literal from the mapping dictionary
            array_literal = self.FIELD_NAME_TO_ARRAY[field_name]

            session_maker = get_session_maker()
            async with session_maker() as session:
                # Use raw SQL for JSONB path updates (SQLAlchemy ORM doesn't support this easily)
                update_query = text(
                    f"""
                    UPDATE players
                    SET stats = jsonb_set(
                        COALESCE(stats, '{{}}'::jsonb),
                        {array_literal},
                        to_jsonb((COALESCE(stats->>:field_name, '0'))::numeric + :delta),
                        true
                    )
                    WHERE player_id = :player_id
                    """
                )

                result = await session.execute(
                    update_query, {"field_name": field_name, "delta": delta, "player_id": str(player_id)}
                )

                if result.rowcount == 0:
                    raise ValueError(f"Player {player_id} not found")

                await session.commit()

                self._logger.info(
                    "Player stat field updated atomically",
                    player_id=str(player_id),
                    field_name=field_name,
                    delta=delta,
                    reason=reason,
                )
                return
        except (SQLAlchemyError, OSError, TypeError, ValueError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating stat field: {e}",
                context=context,
                details={
                    "player_id": str(player_id),
                    "field_name": field_name,
                    "delta": delta,
                    "reason": reason,
                    "error": str(e),
                },
                user_friendly="Failed to update player stats",
            )
