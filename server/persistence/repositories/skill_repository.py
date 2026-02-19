"""
Skill repository for async persistence operations.

Provides async database operations for the skills catalog.
"""

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.skill import Skill
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


class SkillRepository:
    """
    Repository for skills catalog persistence.

    Handles skill queries for character creation and skills API.
    """

    def __init__(self) -> None:
        """Initialize the skill repository."""
        self._logger = get_logger(__name__)

    async def get_all_skills(self) -> list[Skill]:
        """
        Get all skills in the catalog.

        Returns:
            list[Skill]: All skills (order not guaranteed; client can sort by name/key).

        Raises:
            DatabaseError: If database operation fails.
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = select(Skill).order_by(Skill.key)
                result = await session.execute(stmt)
                skills = list(result.scalars().all())
                self._logger.debug("Loaded skills catalog", skill_count=len(skills))
                return skills
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving skills: {e}",
                operation="get_all_skills",
                details={"error": str(e)},
                user_friendly="Failed to retrieve skills catalog",
            )

    async def get_skill_by_id(self, skill_id: int) -> Skill | None:
        """
        Get a skill by ID.

        Args:
            skill_id: Skill primary key.

        Returns:
            Skill | None: The skill or None if not found.
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = select(Skill).where(Skill.id == skill_id)
                result = await session.execute(stmt)
                return result.scalar_one_or_none()
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving skill by ID '{skill_id}': {e}",
                operation="get_skill_by_id",
                details={"skill_id": skill_id, "error": str(e)},
                user_friendly="Failed to retrieve skill",
            )

    async def get_skill_by_key(self, key: str) -> Skill | None:
        """
        Get a skill by key (e.g. accounting, cthulhu_mythos).

        Args:
            key: Skill key.

        Returns:
            Skill | None: The skill or None if not found.
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = select(Skill).where(Skill.key == key)
                result = await session.execute(stmt)
                return result.scalar_one_or_none()
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving skill by key '{key}': {e}",
                operation="get_skill_by_key",
                details={"key": key, "error": str(e)},
                user_friendly="Failed to retrieve skill",
            )
