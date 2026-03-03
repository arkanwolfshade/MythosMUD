"""
Spell repository for async persistence operations.

This module provides async database operations for spell queries
using PostgreSQL stored procedures.
"""

from typing import Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


def _row_to_spell_dict(row: Any) -> dict[str, Any]:
    """Map procedure result row to spell dict."""
    return {
        "spell_id": row.spell_id,
        "name": row.name,
        "description": row.description,
        "school": row.school,
        "mp_cost": row.mp_cost,
        "lucidity_cost": row.lucidity_cost,
        "corruption_on_learn": row.corruption_on_learn,
        "corruption_on_cast": row.corruption_on_cast,
        "casting_time_seconds": row.casting_time_seconds,
        "target_type": row.target_type,
        "range_type": row.range_type,
        "effect_type": row.effect_type,
        "effect_data": dict(row.effect_data) if row.effect_data else {},
        "materials": list(row.materials) if row.materials else [],
    }


class SpellRepository:
    """
    Repository for spell persistence operations.

    Handles spell queries and data retrieval from the database.
    """

    def __init__(self) -> None:
        """Initialize the spell repository."""
        self._logger = get_logger(__name__)

    async def get_all_spells(self) -> list[dict[str, Any]]:
        """
        Get all spells from the database.

        Returns:
            list[dict]: List of all spell dictionaries

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(text("SELECT * FROM get_all_spells()"))
                rows = result.mappings().all()
                spells = [_row_to_spell_dict(row) for row in rows]
                self._logger.debug("Loaded spells", spell_count=len(spells))
                return spells
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving spells: {e}",
                operation="get_all_spells",
                details={"error": str(e)},
                user_friendly="Failed to retrieve spell list",
            )

    async def get_spell_by_id(self, spell_id: str) -> dict[str, Any] | None:
        """
        Get a spell by ID.

        Args:
            spell_id: Spell ID

        Returns:
            dict | None: Spell dictionary or None if not found

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT * FROM get_spell_by_id(:spell_id)"),
                    {"spell_id": spell_id},
                )
                row = result.mappings().first()
                if not row:
                    return None
                return _row_to_spell_dict(row)
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving spell by ID '{spell_id}': {e}",
                operation="get_spell_by_id",
                spell_id=spell_id,
                details={"spell_id": spell_id, "error": str(e)},
                user_friendly="Failed to retrieve spell",
            )
