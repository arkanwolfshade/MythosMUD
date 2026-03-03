"""
Player spell repository for async persistence operations.

This module provides async database operations for player spell learning
and mastery tracking using PostgreSQL stored procedures.
"""

import uuid
from typing import Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.models.player_spells import PlayerSpell
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


def _row_to_player_spell(row: Any) -> PlayerSpell:
    """Map procedure result row to PlayerSpell model."""
    return PlayerSpell(
        id=row.id,
        player_id=str(row.player_id) if row.player_id else "",
        spell_id=row.spell_id or "",
        mastery=row.mastery or 0,
        learned_at=row.learned_at,
        last_cast_at=row.last_cast_at,
        times_cast=row.times_cast or 0,
    )


class PlayerSpellRepository:
    """
    Repository for player spell persistence operations.

    Handles player spell learning, mastery tracking, and queries.
    """

    def __init__(self) -> None:
        """Initialize the player spell repository."""
        self._logger = get_logger(__name__)

    async def get_player_spells(self, player_id: uuid.UUID) -> list[PlayerSpell]:
        """
        Get all spells learned by a player.

        Args:
            player_id: Player ID

        Returns:
            list[PlayerSpell]: List of player spells

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT * FROM get_player_spells(:player_id)"),
                    {"player_id": str(player_id)},
                )
                rows = result.mappings().all()
                player_spells = [_row_to_player_spell(row) for row in rows]
                self._logger.debug(
                    "Loaded player spells",
                    player_id=str(player_id),
                    count=len(player_spells),
                )
                return player_spells
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player spells: {e}",
                operation="get_player_spells",
                player_id=str(player_id),
                details={"player_id": str(player_id), "error": str(e)},
                user_friendly="Failed to retrieve learned spells",
            )

    async def get_player_spell(self, player_id: uuid.UUID, spell_id: str) -> PlayerSpell | None:
        """
        Get a specific player spell.

        Args:
            player_id: Player ID
            spell_id: Spell ID

        Returns:
            PlayerSpell | None: Player spell or None if not found

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT * FROM get_player_spell(:player_id, :spell_id)"),
                    {"player_id": str(player_id), "spell_id": spell_id},
                )
                row = result.mappings().first()
                if not row:
                    return None
                return _row_to_player_spell(row)
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player spell: {e}",
                operation="get_player_spell",
                player_id=str(player_id),
                spell_id=spell_id,
                details={"player_id": str(player_id), "spell_id": spell_id, "error": str(e)},
                user_friendly="Failed to retrieve spell",
            )

    async def learn_spell(self, player_id: uuid.UUID, spell_id: str, initial_mastery: int = 0) -> PlayerSpell:
        """
        Learn a new spell for a player.

        Args:
            player_id: Player ID
            spell_id: Spell ID to learn
            initial_mastery: Initial mastery level (default 0)

        Returns:
            PlayerSpell: The created or existing player spell

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT * FROM learn_spell(:player_id, :spell_id, :initial_mastery)"),
                    {
                        "player_id": str(player_id),
                        "spell_id": spell_id,
                        "initial_mastery": initial_mastery,
                    },
                )
                row = result.mappings().first()
                if not row:
                    log_and_raise(
                        DatabaseError,
                        "learn_spell returned no row",
                        operation="learn_spell",
                        player_id=str(player_id),
                        spell_id=spell_id,
                        details={"player_id": str(player_id), "spell_id": spell_id},
                        user_friendly="Failed to learn spell",
                    )
                await session.commit()
                self._logger.info("Player learned spell", player_id=str(player_id), spell_id=spell_id)
                return _row_to_player_spell(row)
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error learning spell: {e}",
                operation="learn_spell",
                player_id=str(player_id),
                spell_id=spell_id,
                details={"player_id": str(player_id), "spell_id": spell_id, "error": str(e)},
                user_friendly="Failed to learn spell",
            )

    async def update_mastery(self, player_id: uuid.UUID, spell_id: str, new_mastery: int) -> PlayerSpell | None:
        """
        Update mastery level for a player spell.

        Args:
            player_id: Player ID
            spell_id: Spell ID
            new_mastery: New mastery level (0-100)

        Returns:
            PlayerSpell | None: Updated player spell or None if not found

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT * FROM update_player_spell_mastery(:player_id, :spell_id, :new_mastery)"),
                    {
                        "player_id": str(player_id),
                        "spell_id": spell_id,
                        "new_mastery": new_mastery,
                    },
                )
                row = result.mappings().first()
                if not row:
                    return None
                await session.commit()
                self._logger.debug(
                    "Updated spell mastery",
                    player_id=str(player_id),
                    spell_id=spell_id,
                    mastery=new_mastery,
                )
                return _row_to_player_spell(row)
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating mastery: {e}",
                operation="update_mastery",
                player_id=str(player_id),
                spell_id=spell_id,
                new_mastery=new_mastery,
                details={"player_id": str(player_id), "spell_id": spell_id, "error": str(e)},
                user_friendly="Failed to update spell mastery",
            )

    async def record_spell_cast(self, player_id: uuid.UUID, spell_id: str) -> PlayerSpell | None:
        """
        Record that a player cast a spell (increment times_cast, update last_cast_at).

        Args:
            player_id: Player ID
            spell_id: Spell ID

        Returns:
            PlayerSpell | None: Updated player spell or None if not found

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text("SELECT * FROM record_spell_cast(:player_id, :spell_id)"),
                    {"player_id": str(player_id), "spell_id": spell_id},
                )
                row = result.mappings().first()
                if not row:
                    return None
                await session.commit()
                self._logger.debug("Recorded spell cast", player_id=str(player_id), spell_id=spell_id)
                return _row_to_player_spell(row)
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error recording spell cast: {e}",
                operation="record_spell_cast",
                player_id=str(player_id),
                spell_id=spell_id,
                details={"player_id": str(player_id), "spell_id": spell_id, "error": str(e)},
                user_friendly="Failed to record spell cast",
            )
