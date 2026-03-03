"""
Profession repository for async persistence operations.

This module provides async database operations for profession queries
using PostgreSQL stored procedures.
"""

from typing import Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.profession import Profession
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


def _row_to_profession(row: Any) -> Profession:
    """Map procedure result row to Profession model."""
    return Profession(
        id=row.id,
        name=row.name or "",
        description=row.description or "",
        flavor_text=row.flavor_text or "",
        stat_requirements=row.stat_requirements or "{}",
        mechanical_effects=row.mechanical_effects or "{}",
        is_available=bool(row.is_available) if row.is_available is not None else True,
        stat_modifiers=row.stat_modifiers or "[]",
        skill_modifiers=row.skill_modifiers or "[]",
    )


class ProfessionRepository:
    """
    Repository for profession persistence operations.

    Handles profession queries and data retrieval.
    """

    def __init__(self) -> None:
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
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(text("SELECT * FROM get_all_professions()"))
                rows = result.mappings().all()
                professions = [_row_to_profession(row) for row in rows]
                self._logger.debug("Loaded professions", profession_count=len(professions))
                return professions
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving professions: {e}",
                operation="get_all_professions",
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
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT * FROM get_profession_by_id(:profession_id)"),
                    {"profession_id": profession_id},
                )
                row = result.mappings().first()
                if not row:
                    return None
                return _row_to_profession(row)
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving profession by ID '{profession_id}': {e}",
                operation="get_profession_by_id",
                profession_id=profession_id,
                details={"profession_id": profession_id, "error": str(e)},
                user_friendly="Failed to retrieve profession",
            )
