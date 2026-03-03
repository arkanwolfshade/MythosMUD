"""
PlayerSkill repository for async persistence.

Supports SkillService: delete_for_player, insert_many, get_by_player_id (with skill join).
Uses PostgreSQL stored procedures.
"""

from typing import Any
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.player_skill import PlayerSkill
from server.models.skill import Skill
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


def _row_to_player_skill_with_skill(row: Any) -> PlayerSkill:
    """Map procedure result row to PlayerSkill with skill attached."""
    skill = Skill(
        id=row.skill_id,
        key=row.skill_key or "",
        name=row.skill_name or "",
        description=row.skill_description,
        base_value=row.skill_base_value or 0,
        allow_at_creation=bool(row.skill_allow_at_creation) if row.skill_allow_at_creation is not None else True,
        category=row.skill_category,
    )
    ps = PlayerSkill(
        player_id=str(row.player_id) if row.player_id else "",
        skill_id=row.skill_id,
        value=row.value or 0,
    )
    ps.skill = skill
    return ps


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
                await session.execute(
                    text("SELECT delete_player_skills_for_player(:player_id)"),
                    {"player_id": str(player_id)},
                )
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
                skill_ids = [sv[0] for sv in skill_values]
                values = [sv[1] for sv in skill_values]
                await session.execute(
                    text("SELECT insert_player_skills_many(:player_id, :skill_ids, :values)"),
                    {
                        "player_id": str(player_id),
                        "skill_ids": skill_ids,
                        "values": values,
                    },
                )
                await session.commit()
                self._logger.debug(
                    "Inserted player_skills",
                    player_id=str(player_id),
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
                result = await session.execute(
                    text("SELECT * FROM get_player_skills_with_skill(:player_id)"),
                    {"player_id": str(player_id)},
                )
                rows = result.mappings().all()
                player_skills = [_row_to_player_skill_with_skill(row) for row in rows]
                self._logger.debug(
                    "Loaded player_skills for player",
                    player_id=str(player_id),
                    count=len(player_skills),
                )
                return player_skills
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
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                await session.execute(
                    text("SELECT update_player_skill_value(:player_id, :skill_id, :value)"),
                    {
                        "player_id": str(player_id),
                        "skill_id": skill_id,
                        "value": value,
                    },
                )
                await session.commit()
                self._logger.debug(
                    "Updated player_skill value",
                    player_id=str(player_id),
                    skill_id=skill_id,
                    value=value,
                )
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating player_skill: {e}",
                operation="update_value",
                details={"player_id": str(player_id), "skill_id": skill_id, "error": str(e)},
                user_friendly="Failed to update skill value",
            )
