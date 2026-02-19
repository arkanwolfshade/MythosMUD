"""
PlayerSkill repository for async persistence.

Supports SkillService: delete_for_player, insert_many, get_by_player_id (with skill join).
"""

from uuid import UUID

from sqlalchemy import delete, select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.player_skill import PlayerSkill
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


class PlayerSkillRepository:
    """
    Repository for player_skills table.

    Used by SkillService for set_player_skills and get_player_skills.
    """

    def __init__(self) -> None:
        self._logger = get_logger(__name__)

    async def delete_for_player(self, player_id: UUID | str) -> None:
        """Delete all player_skills for the given player_id."""
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = delete(PlayerSkill).where(PlayerSkill.player_id == str(player_id))
                await session.execute(stmt)
                await session.commit()
                self._logger.debug("Deleted player_skills for player", player_id=str(player_id))
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error deleting player_skills: {e}",
                operation="delete_for_player",
                details={"player_id": str(player_id), "error": str(e)},
                user_friendly="Failed to clear player skills",
            )

    async def insert_many(self, player_id: UUID | str, skill_values: list[tuple[int, int]]) -> None:
        """
        Insert multiple (skill_id, value) rows for one player.

        skill_values: list of (skill_id, value).
        """
        if not skill_values:
            return
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                pid = str(player_id)
                for skill_id, value in skill_values:
                    ps = PlayerSkill(player_id=pid, skill_id=skill_id, value=value)
                    session.add(ps)
                await session.commit()
                self._logger.debug(
                    "Inserted player_skills",
                    player_id=pid,
                    count=len(skill_values),
                )
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error inserting player_skills: {e}",
                operation="insert_many",
                details={"player_id": str(player_id), "error": str(e)},
                user_friendly="Failed to save player skills",
            )

    async def get_by_player_id(self, player_id: UUID | str) -> list[PlayerSkill]:
        """
        Get all PlayerSkill rows for the player with skill loaded (join).

        Returns list of PlayerSkill with .skill populated for name/key.
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = (
                    select(PlayerSkill)
                    .where(PlayerSkill.player_id == str(player_id))
                    .options(selectinload(PlayerSkill.skill))
                )
                result = await session.execute(stmt)
                rows = list(result.scalars().all())
                self._logger.debug(
                    "Loaded player_skills for player",
                    player_id=str(player_id),
                    count=len(rows),
                )
                return rows
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error loading player_skills: {e}",
                operation="get_by_player_id",
                details={"player_id": str(player_id), "error": str(e)},
                user_friendly="Failed to load player skills",
            )

    async def update_value(self, player_id: UUID | str, skill_id: int, value: int) -> None:
        """Update a single player_skill row (e.g. after improvement roll). Clamps value 0-99."""
        clamped = max(0, min(99, value))
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = (
                    update(PlayerSkill)
                    .where(
                        PlayerSkill.player_id == str(player_id),
                        PlayerSkill.skill_id == skill_id,
                    )
                    .values(value=clamped)
                )
                await session.execute(stmt)
                await session.commit()
                self._logger.debug(
                    "Updated player_skill value",
                    player_id=str(player_id),
                    skill_id=skill_id,
                    value=clamped,
                )
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating player_skill: {e}",
                operation="update_value",
                details={"player_id": str(player_id), "skill_id": skill_id, "error": str(e)},
                user_friendly="Failed to update skill value",
            )
