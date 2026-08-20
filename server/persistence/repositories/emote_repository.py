"""
Emote repository for async persistence operations.

This module provides async database operations for loading predefined emotes and their aliases,
via the shared session maker rather than a hand-rolled asyncpg connection. See issue #624: the
prior EmoteService opened its own connection from a synchronous constructor as a workaround for a
sync/async boundary problem that this repository -- and EmoteService's new async load path --
removes instead of working around.

Query text is unchanged from the original inline queries (per the #618 allowlist: relocating raw
SQL is tracked here, not converted to a stored procedure yet -- #633 owns that).
"""

from typing import Any

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from server.database import get_session_maker
from server.exceptions import DatabaseError
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.error_logging import log_and_raise

logger = get_logger(__name__)


class EmoteRepository:
    """Repository for predefined emote and emote-alias persistence operations."""

    def __init__(self) -> None:
        """Initialize the emote repository."""
        self._logger = get_logger(__name__)

    async def get_emotes(self) -> list[dict[str, Any]]:
        """
        Get all predefined emotes from the database.

        Returns:
            list[dict]: Rows with stable_id, self_message, other_message.

        Raises:
            DatabaseError: If the database operation fails.
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        """
                        SELECT
                            stable_id,
                            self_message,
                            other_message
                        FROM emotes
                        ORDER BY stable_id
                        """
                    )
                )
                return [
                    {
                        "stable_id": row.stable_id,
                        "self_message": row.self_message,
                        "other_message": row.other_message,
                    }
                    for row in result
                ]
        except SQLAlchemyError as e:
            log_and_raise(
                DatabaseError,
                f"Database error loading emotes: {e}",
                operation="get_emotes",
                details={"error": str(e)},
                user_friendly="Failed to load emotes",
            )

    async def get_emote_aliases(self) -> list[dict[str, Any]]:
        """
        Get all emote aliases joined to their owning emote's stable_id.

        Returns:
            list[dict]: Rows with stable_id, alias.

        Raises:
            DatabaseError: If the database operation fails.
        """
        try:
            session_maker = get_session_maker()
            async with session_maker() as session:
                result = await session.execute(
                    text(
                        """
                        SELECT
                            e.stable_id,
                            ea.alias
                        FROM emote_aliases ea
                        JOIN emotes e ON ea.emote_id = e.id
                        ORDER BY e.stable_id, ea.alias
                        """
                    )
                )
                return [{"stable_id": row.stable_id, "alias": row.alias} for row in result]
        except SQLAlchemyError as e:
            log_and_raise(
                DatabaseError,
                f"Database error loading emote aliases: {e}",
                operation="get_emote_aliases",
                details={"error": str(e)},
                user_friendly="Failed to load emote aliases",
            )
