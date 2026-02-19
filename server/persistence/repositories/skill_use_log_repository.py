"""
SkillUseLog repository: record and query successful skill uses (plan 4.5).
"""

import datetime
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.skill_use_log import SkillUseLog
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


class SkillUseLogRepository:
    """Repository for skill_use_log: insert, get distinct skills used at a level."""

    def __init__(self) -> None:
        self._logger = get_logger(__name__)

    async def record_use(
        self,
        player_id: UUID | str,
        skill_id: int,
        character_level_at_use: int,
    ) -> None:
        """Insert one skill_use_log row."""
        try:
            from datetime import UTC

            session_maker = get_session_maker()
            async with session_maker() as session:
                row = SkillUseLog(
                    player_id=str(player_id),
                    skill_id=skill_id,
                    character_level_at_use=character_level_at_use,
                    used_at=datetime.datetime.now(UTC).replace(tzinfo=None),
                )
                session.add(row)
                await session.commit()
                self._logger.debug(
                    "Recorded skill use",
                    player_id=str(player_id),
                    skill_id=skill_id,
                    level=character_level_at_use,
                )
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error recording skill use: {e}",
                operation="record_use",
                details={"player_id": str(player_id), "skill_id": skill_id, "error": str(e)},
                user_friendly="Failed to record skill use",
            )

    async def get_skill_ids_used_at_level(
        self,
        player_id: UUID | str,
        character_level: int,
    ) -> list[int]:
        """
        Return distinct skill_ids that the player used at the given character level.

        Used by run_improvement_rolls to determine which skills get a roll.
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = (
                    select(SkillUseLog.skill_id)
                    .where(
                        SkillUseLog.player_id == str(player_id),
                        SkillUseLog.character_level_at_use == character_level,
                    )
                    .distinct()
                )
                result = await session.execute(stmt)
                ids = list(result.scalars().all())
                self._logger.debug(
                    "Skills used at level",
                    player_id=str(player_id),
                    level=character_level,
                    count=len(ids),
                )
                return ids
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error loading skills used at level: {e}",
                operation="get_skill_ids_used_at_level",
                details={"player_id": str(player_id), "level": character_level, "error": str(e)},
                user_friendly="Failed to load skill use log",
            )
