"""
Player effect repository (ADR-019, ADR-029 steps 3b-i and 6d).

The player registry owns the ``player_effects`` rows: it loads them with a player and writes them inside its units of
work. What is left here is the one read made without opening a unit, the status-effect tick's candidates.
"""

from collections.abc import Sequence
from typing import cast
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


class PlayerEffectRepository:
    """Repository for the player_effects table: the tick's candidate query."""

    async def player_ids_with_active_effects(self, player_ids: Sequence[UUID]) -> list[UUID]:
        """Which of these players have an effect with time left (or no limit). Raises DatabaseError."""
        if not player_ids:
            return []
        operation = "player_ids_with_active_effects"
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT player_id FROM get_player_ids_with_active_effects(CAST(:player_ids AS uuid[]))"),
                    {"player_ids": list(player_ids)},
                )
                rows = cast(Sequence[UUID], result.scalars().all())
                await session.commit()
                return [UUID(str(player_id)) for player_id in rows]
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error in {operation}: {e}",
                operation=operation,
                details={"players": len(player_ids), "error": str(e)},
                user_friendly="Failed to read player effects",
            )
