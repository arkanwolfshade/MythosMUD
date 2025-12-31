"""
Spell repository for async persistence operations.

This module provides async database operations for spell queries
using SQLAlchemy ORM with PostgreSQL.
"""

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.spell_db import SpellDB
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


class SpellRepository:
    """
    Repository for spell persistence operations.

    Handles spell queries and data retrieval from the database.
    """

    def __init__(self):
        """Initialize the spell repository."""
        self._logger = get_logger(__name__)

    async def get_all_spells(self) -> list[dict]:
        """
        Get all spells from the database.

        Returns:
            list[dict]: List of all spell dictionaries

        Raises:
            DatabaseError: If database operation fails
        """
        context = create_error_context()
        context.metadata["operation"] = "get_all_spells"

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = select(SpellDB)
                result = await session.execute(stmt)
                spell_objs = list(result.scalars().all())
                # Convert SQLAlchemy objects to dicts
                spells = []
                for spell_obj in spell_objs:
                    spell_dict = {
                        "spell_id": spell_obj.spell_id,
                        "name": spell_obj.name,
                        "description": spell_obj.description,
                        "school": spell_obj.school,
                        "mp_cost": spell_obj.mp_cost,
                        "lucidity_cost": spell_obj.lucidity_cost,
                        "corruption_on_learn": spell_obj.corruption_on_learn,
                        "corruption_on_cast": spell_obj.corruption_on_cast,
                        "casting_time_seconds": spell_obj.casting_time_seconds,
                        "target_type": spell_obj.target_type,
                        "range_type": spell_obj.range_type,
                        "effect_type": spell_obj.effect_type,
                        "effect_data": spell_obj.effect_data or {},
                        "materials": spell_obj.materials or [],
                    }
                    spells.append(spell_dict)
                self._logger.debug("Loaded spells", spell_count=len(spells))
                return spells
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving spells: {e}",
                context=context,
                details={"error": str(e)},
                user_friendly="Failed to retrieve spell list",
            )

    async def get_spell_by_id(self, spell_id: str) -> dict | None:
        """
        Get a spell by ID.

        Args:
            spell_id: Spell ID

        Returns:
            dict | None: Spell dictionary or None if not found

        Raises:
            DatabaseError: If database operation fails
        """
        context = create_error_context()
        context.metadata["operation"] = "get_spell_by_id"
        context.metadata["spell_id"] = spell_id

        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                stmt = select(SpellDB).where(SpellDB.spell_id == spell_id)
                result = await session.execute(stmt)
                spell_obj = result.scalar_one_or_none()
                if spell_obj:
                    return {
                        "spell_id": spell_obj.spell_id,
                        "name": spell_obj.name,
                        "description": spell_obj.description,
                        "school": spell_obj.school,
                        "mp_cost": spell_obj.mp_cost,
                        "lucidity_cost": spell_obj.lucidity_cost,
                        "corruption_on_learn": spell_obj.corruption_on_learn,
                        "corruption_on_cast": spell_obj.corruption_on_cast,
                        "casting_time_seconds": spell_obj.casting_time_seconds,
                        "target_type": spell_obj.target_type,
                        "range_type": spell_obj.range_type,
                        "effect_type": spell_obj.effect_type,
                        "effect_data": spell_obj.effect_data or {},
                        "materials": spell_obj.materials or [],
                    }
                return None
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving spell by ID '{spell_id}': {e}",
                context=context,
                details={"spell_id": spell_id, "error": str(e)},
                user_friendly="Failed to retrieve spell",
            )
