"""
Experience repository for async persistence operations.

This module provides async database operations for player XP and stat management
using PostgreSQL stored procedures.
"""

import uuid
from typing import Protocol, cast

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from structlog.stdlib import BoundLogger

from server.database import get_session_maker
from server.events.event_types import BaseEvent, PlayerXPAwardEvent
from server.exceptions import DatabaseError
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger: BoundLogger = get_logger(__name__)


class _ExperienceEventBus(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Minimal event bus surface for XP award publishing."""

    def publish(self, event: BaseEvent) -> None: ...  # pylint: disable=missing-function-docstring  # Reason: Protocol stub


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

    def __init__(self, event_bus: _ExperienceEventBus | None = None) -> None:
        """
        Initialize the experience repository.

        Args:
            event_bus: Optional EventBus for publishing XP/level events
        """
        self._event_bus: _ExperienceEventBus | None = event_bus
        self._logger: BoundLogger = get_logger(__name__)

    async def award_player_xp(self, player_id: uuid.UUID | str, delta: int, reason: str = "") -> tuple[int, int, int]:
        """
        Award XP and recompute level atomically via the award_player_xp stored function.

        Args:
            player_id: Player UUID or string
            delta: XP amount (must be non-negative)
            reason: Source of XP, for logging

        Returns:
            (new_xp, old_level, new_level)

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
                    text("SELECT new_xp, old_level, new_level FROM award_player_xp(:player_id, :delta)"),
                    {"player_id": str(player_id), "delta": delta},
                )
                row = result.one_or_none()
                if row is None:
                    raise ValueError(f"Player {player_id} not found")

                await session.commit()

                # Raw text() query -> SQLAlchemy Row has no static column typing; cast (not int())
                # keeps the Any confined to a single, explicit conversion point.
                new_xp = cast(int, row.new_xp)
                old_level = cast(int, row.old_level)
                new_level = cast(int, row.new_level)

                self._logger.info(
                    "Player XP awarded atomically",
                    player_id=str(player_id),
                    delta=delta,
                    reason=reason,
                    new_xp=new_xp,
                    old_level=old_level,
                    new_level=new_level,
                )

                if self._event_bus:
                    event = PlayerXPAwardEvent(
                        player_id=uuid.UUID(str(player_id)),
                        xp_amount=delta,
                        new_level=new_level,
                    )
                    self._event_bus.publish(event)

                return new_xp, old_level, new_level
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error awarding XP for player '{player_id}': {e}",
                operation="award_player_xp",
                player_id=str(player_id),
                details={"player_id": str(player_id), "delta": delta, "reason": reason, "error": str(e)},
                user_friendly="Failed to update player experience",
            )

    async def _persist_stat_field_delta(
        self,
        player_id: uuid.UUID | str,
        path: list[str],
        delta: int | float,
        field_name: str,
        reason: str,
    ) -> None:
        """Run update_player_stat_field stored procedure and log success."""
        try:
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

    async def update_player_stat_field(
        self, player_id: uuid.UUID | str, field_name: str, delta: object, reason: str = ""
    ) -> None:
        """
        Update a specific numeric field in player stats atomically.

        Args:
            player_id: Player UUID or string
            field_name: Stat field name (must be in FIELD_NAME_TO_PATH)
            delta: Amount to change field by (int or float)
            reason: Reason for update

        Raises:
            TypeError: If delta is not int or float
            ValueError: If field_name invalid
            DatabaseError: If database operation fails
        """
        if not isinstance(delta, int | float):
            raise TypeError(f"delta must be int or float, got {type(delta).__name__}")

        if field_name not in self.FIELD_NAME_TO_PATH:
            allowed_fields = set(self.FIELD_NAME_TO_PATH.keys())
            raise ValueError(f"Invalid stat field name: {field_name}. Must be one of {allowed_fields}")

        await self._persist_stat_field_delta(player_id, self.FIELD_NAME_TO_PATH[field_name], delta, field_name, reason)
