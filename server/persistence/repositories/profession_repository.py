"""
Profession repository for async persistence operations.

This module provides async database operations for profession queries
using SQLAlchemy ORM with PostgreSQL.
"""

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.profession import Profession
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


class ProfessionRepository:
    """
    Repository for profession persistence operations.

    Handles profession queries and data retrieval.
    """

    def __init__(self):
        """Initialize the profession repository."""
        self._logger = get_logger(__name__)

    async def get_all_professions(self) -> list[Profession]:
        """
        Get all available professions.

        Returns:
            list[Profession]: List of all professions

        Raises:
            DatabaseError: If database operation fails
        """
        context = create_error_context()
        context.metadata["operation"] = "get_all_professions"

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = select(Profession)
                result = await session.execute(stmt)
                professions = list(result.scalars().all())
                self._logger.debug("Loaded professions", profession_count=len(professions))
                return professions
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving professions: {e}",
                context=context,
                details={"error": str(e)},
                user_friendly="Failed to retrieve profession list",
            )

    async def get_profession_by_id(self, profession_id: int) -> Profession | None:
        """
        Get a profession by ID.

        Args:
            profession_id: Profession ID

        Returns:
            Profession | None: Profession object or None if not found

        Raises:
            DatabaseError: If database operation fails
        """
        context = create_error_context()
        context.metadata["operation"] = "get_profession_by_id"
        context.metadata["profession_id"] = profession_id

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = select(Profession).where(Profession.id == profession_id)
                result = await session.execute(stmt)
                profession = result.scalar_one_or_none()
                return profession
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving profession by ID '{profession_id}': {e}",
                context=context,
                details={"profession_id": profession_id, "error": str(e)},
                user_friendly="Failed to retrieve profession",
            )
