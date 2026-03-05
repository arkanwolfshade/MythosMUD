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


def _str_or_default(value: Any, default: str = "") -> str:
    """Return value as str or a default if falsy."""
    return str(value) if value else default


def _text_or_default(value: Any, default: str) -> str:
    """Return text value or default if falsy."""
    return value if value else default


def _bool_or_default(value: Any, default: bool = True) -> bool:
    """Return bool(value) when not None, otherwise default."""
    if value is None:
        return default
    return bool(value)


def _row_to_profession(row: Any) -> Profession:
    """Map procedure result row to Profession model."""
    return Profession(
        id=row.id,
        name=_text_or_default(row.name, ""),
        description=_text_or_default(row.description, ""),
        flavor_text=_text_or_default(row.flavor_text, ""),
        stat_requirements=_text_or_default(row.stat_requirements, "{}"),
        mechanical_effects=_text_or_default(row.mechanical_effects, "{}"),
        is_available=_bool_or_default(row.is_available, True),
        stat_modifiers=_text_or_default(row.stat_modifiers, "[]"),
        skill_modifiers=_text_or_default(row.skill_modifiers, "[]"),
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
                result = await session.execute(
                    text(
                        """
                        SELECT
                            id,
                            name,
                            description,
                            flavor_text,
                            stat_requirements,
                            mechanical_effects,
                            is_available,
                            stat_modifiers,
                            skill_modifiers
                        FROM get_all_professions()
                        """
                    )
                )
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
                    text(
                        """
                        SELECT
                            id,
                            name,
                            description,
                            flavor_text,
                            stat_requirements,
                            mechanical_effects,
                            is_available,
                            stat_modifiers,
                            skill_modifiers
                        FROM get_profession_by_id(:profession_id)
                        """
                    ),
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
