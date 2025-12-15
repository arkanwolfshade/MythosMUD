"""
Player spell repository for async persistence operations.

This module provides async database operations for player spell learning
and mastery tracking using SQLAlchemy ORM with PostgreSQL.
"""

import uuid
from datetime import UTC, datetime

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_async_session
from server.exceptions import DatabaseError
from server.logging.enhanced_logging_config import get_logger
from server.models.player_spells import PlayerSpell
from server.utils.error_logging import create_error_context, log_and_raise

logger = get_logger(__name__)


class PlayerSpellRepository:
    """
    Repository for player spell persistence operations.

    Handles player spell learning, mastery tracking, and queries.
    """

    def __init__(self):
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
        context = create_error_context()
        context.metadata["operation"] = "get_player_spells"
        context.metadata["player_id"] = str(player_id)

        try:
            async for session in get_async_session():
                stmt = select(PlayerSpell).where(PlayerSpell.player_id == str(player_id))
                result = await session.execute(stmt)
                player_spells = list(result.scalars().all())
                self._logger.debug("Loaded player spells", player_id=str(player_id), count=len(player_spells))
                return player_spells
            return []
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player spells: {e}",
                context=context,
                details={"player_id": str(player_id), "error": str(e)},
                user_friendly="Failed to retrieve learned spells",
            )

    async def get_player_spell(self, player_id: uuid.UUID, spell_id: str) -> PlayerSpell | None:  # type: ignore[return]
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
        context = create_error_context()
        context.metadata["operation"] = "get_player_spell"
        context.metadata["player_id"] = str(player_id)
        context.metadata["spell_id"] = spell_id

        try:
            async for session in get_async_session():
                stmt = select(PlayerSpell).where(
                    PlayerSpell.player_id == str(player_id), PlayerSpell.spell_id == spell_id
                )
                result = await session.execute(stmt)
                return result.scalar_one_or_none()
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player spell: {e}",
                context=context,
                details={"player_id": str(player_id), "spell_id": spell_id, "error": str(e)},
                user_friendly="Failed to retrieve spell",
            )

    async def learn_spell(self, player_id: uuid.UUID, spell_id: str, initial_mastery: int = 0) -> PlayerSpell:  # type: ignore[return]
        """
        Learn a new spell for a player.

        Args:
            player_id: Player ID
            spell_id: Spell ID to learn
            initial_mastery: Initial mastery level (default 0)

        Returns:
            PlayerSpell: The created player spell

        Raises:
            DatabaseError: If database operation fails
        """
        context = create_error_context()
        context.metadata["operation"] = "learn_spell"
        context.metadata["player_id"] = str(player_id)
        context.metadata["spell_id"] = spell_id

        try:
            async for session in get_async_session():
                # Check if already learned
                existing = await self.get_player_spell(player_id, spell_id)
                if existing:
                    self._logger.warning("Player already knows spell", player_id=str(player_id), spell_id=spell_id)
                    return existing

                # Create new player spell
                player_spell = PlayerSpell(
                    player_id=str(player_id),
                    spell_id=spell_id,
                    mastery=initial_mastery,
                    learned_at=datetime.now(UTC).replace(tzinfo=None),
                    times_cast=0,
                )
                session.add(player_spell)
                await session.commit()
                await session.refresh(player_spell)
                self._logger.info("Player learned spell", player_id=str(player_id), spell_id=spell_id)
                return player_spell
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error learning spell: {e}",
                context=context,
                details={"player_id": str(player_id), "spell_id": spell_id, "error": str(e)},
                user_friendly="Failed to learn spell",
            )

    async def update_mastery(self, player_id: uuid.UUID, spell_id: str, new_mastery: int) -> PlayerSpell | None:  # type: ignore[return]
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
        context = create_error_context()
        context.metadata["operation"] = "update_mastery"
        context.metadata["player_id"] = str(player_id)
        context.metadata["spell_id"] = spell_id
        context.metadata["new_mastery"] = new_mastery

        try:
            async for session in get_async_session():
                # Load PlayerSpell within the same session context to avoid session management errors
                stmt = select(PlayerSpell).where(
                    PlayerSpell.player_id == str(player_id), PlayerSpell.spell_id == spell_id
                )
                result = await session.execute(stmt)
                player_spell = result.scalar_one_or_none()
                if not player_spell:
                    return None

                # SQLAlchemy allows assigning Python values to Column attributes
                # Clamp mastery to 0-100 range
                clamped_mastery = min(100, max(0, new_mastery))
                player_spell.mastery = clamped_mastery  # type: ignore[assignment]
                await session.commit()
                await session.refresh(player_spell)
                self._logger.debug(
                    "Updated spell mastery", player_id=str(player_id), spell_id=spell_id, mastery=new_mastery
                )
                return player_spell
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error updating mastery: {e}",
                context=context,
                details={"player_id": str(player_id), "spell_id": spell_id, "error": str(e)},
                user_friendly="Failed to update spell mastery",
            )

    async def record_spell_cast(self, player_id: uuid.UUID, spell_id: str) -> PlayerSpell | None:  # type: ignore[return]
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
        context = create_error_context()
        context.metadata["operation"] = "record_spell_cast"
        context.metadata["player_id"] = str(player_id)
        context.metadata["spell_id"] = spell_id

        try:
            async for session in get_async_session():
                # Load PlayerSpell within the same session context to avoid session management errors
                stmt = select(PlayerSpell).where(
                    PlayerSpell.player_id == str(player_id), PlayerSpell.spell_id == spell_id
                )
                result = await session.execute(stmt)
                player_spell = result.scalar_one_or_none()
                if not player_spell:
                    return None

                # SQLAlchemy allows assigning Python values to Column attributes
                player_spell.times_cast += 1  # type: ignore[assignment]
                player_spell.last_cast_at = datetime.now(UTC).replace(tzinfo=None)  # type: ignore[assignment]
                await session.commit()
                await session.refresh(player_spell)
                self._logger.debug("Recorded spell cast", player_id=str(player_id), spell_id=spell_id)
                return player_spell
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error recording spell cast: {e}",
                context=context,
                details={"player_id": str(player_id), "spell_id": spell_id, "error": str(e)},
                user_friendly="Failed to record spell cast",
            )
