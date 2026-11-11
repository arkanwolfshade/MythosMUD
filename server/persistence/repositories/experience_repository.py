"""
Experience repository for async persistence operations.

This module provides async database operations for player stat management using PostgreSQL stored procedures.
XP and level are awarded by the player registry (ADR-029 step 7b), not here.
"""

import uuid
from typing import cast

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from structlog.stdlib import BoundLogger

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger: BoundLogger = get_logger(__name__)


class ExperienceRepository:
    """
    Repository for player experience and stats persistence operations.

    Handles atomic stat-field updates (fear, occult knowledge, and the like).
    """

    # Field name to JSONB path for update_player_stat_field
    FIELD_NAME_TO_PATH: dict[str, list[str]] = {
        "current_dp": ["current_dp"],
        # No "lucidity": it lives in player_lucidity, written through LucidityService (ADR-029 step 3a).
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

    def __init__(self) -> None:
        """Initialize the experience repository."""
        self._logger: BoundLogger = get_logger(__name__)

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
                rows_updated = cast(object, result.scalar())
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
