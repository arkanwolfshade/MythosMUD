"""
Exploration service for MythosMUD.

This module provides the ExplorationService class that handles tracking
which rooms players have explored. This data is used to filter the map
viewer to show only explored rooms to players.

As documented in the Pnakotic Manuscripts, proper tracking of spatial
exploration is essential for maintaining awareness of dimensional
territories that have been traversed.
"""

# pylint: disable=too-many-return-statements  # Reason: Exploration service methods require multiple return statements for early validation returns (permission checks, validation, error handling)

import asyncio
from datetime import UTC, datetime
from typing import Any
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class ExplorationService:
    """
    Service for tracking player room exploration.

    This service manages the player_exploration junction table to track
    which rooms each player has explored. The data is used to filter
    the map viewer to show only explored rooms to players.
    """

    def __init__(self, database_manager: Any = None):
        """
        Initialize the exploration service.

        Args:
            database_manager: Database manager instance for database operations.
                             If not provided, uses DatabaseManager.get_instance().
        """
        from ..database import DatabaseManager

        self._database_manager = database_manager or DatabaseManager.get_instance()
        logger.info("ExplorationService initialized")

    async def mark_room_as_explored(self, player_id: UUID, room_id: str, session: AsyncSession | None = None) -> bool:
        """
        Mark a room as explored by a player.

        This method inserts a record into the player_exploration table
        if it doesn't already exist. The operation is idempotent.

        Args:
            player_id: UUID of the player
            room_id: Room ID (string hierarchical ID like "earth_arkhamcity_northside_...")
            session: Optional database session. If not provided, a new session will be created.

        Returns:
            True if the room was marked as explored (or already was), False on error

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            # Look up the room UUID by stable_id (hierarchical room ID)
            # Rooms table uses UUID as primary key, but game code uses hierarchical string IDs
            room_uuid = await self._get_room_uuid_by_stable_id(room_id, session)

            if not room_uuid:
                logger.warning("Room not found in database", player_id=player_id, room_id=room_id)
                return False

            # Use provided session or create a new one
            if session:
                # Use provided session
                return await self._mark_explored_in_session(session, player_id, room_uuid)
            # Create a new session
            async_session_maker = self._database_manager.get_session_maker()
            async with async_session_maker() as new_session:
                result = await self._mark_explored_in_session(new_session, player_id, room_uuid)
                await new_session.commit()
                return result

        except SQLAlchemyError as e:
            logger.error(
                "Database error marking room as explored",
                player_id=player_id,
                room_id=room_id,
                error=str(e),
                error_type=type(e).__name__,
            )
            raise DatabaseError(f"Failed to mark room as explored: {e}") from e
        except Exception as e:  # pylint: disable=broad-except
            # Unforeseen dimensional ripples must be logged before being
            # allowed to propagate further into the local reality.
            logger.error(
                "Unexpected error marking room as explored",
                player_id=player_id,
                room_id=room_id,
                error=str(e),
                error_type=type(e).__name__,
            )
            raise

    async def _get_room_uuid_by_stable_id(self, stable_id: str, session: AsyncSession | None = None) -> UUID | None:
        """
        Get room UUID by stable_id (hierarchical room ID).

        Args:
            stable_id: Hierarchical room ID (e.g., "earth_arkhamcity_northside_...")
            session: Optional database session. If not provided, a new session will be created.

        Returns:
            Room UUID if found, None otherwise
        """
        try:
            # Use provided session or create a new one
            if session:
                query = text("SELECT id FROM rooms WHERE stable_id = :stable_id")
                result = await session.execute(query, {"stable_id": stable_id})
                room_uuid_result = result.scalar_one_or_none()
                if room_uuid_result:
                    # CRITICAL FIX: asyncpg returns pgproto.UUID objects, not standard UUID objects
                    # Convert to string first, then to UUID to handle both string and UUID-like objects
                    # This prevents "'asyncpg.pgproto.pgproto.UUID' object has no attribute 'replace'" error
                    if isinstance(room_uuid_result, UUID):
                        # Already a standard UUID, return it directly
                        return room_uuid_result
                    # Handle string UUIDs (from tests or database)
                    if isinstance(room_uuid_result, str):
                        # Already a string, convert directly to UUID
                        return UUID(room_uuid_result)
                    # Convert to string first (handles asyncpg UUID objects), then to UUID
                    return UUID(str(room_uuid_result))
                return None
            # Create a new session
            async_session_maker = self._database_manager.get_session_maker()
            async with async_session_maker() as new_session:
                query = text("SELECT id FROM rooms WHERE stable_id = :stable_id")
                result = await new_session.execute(query, {"stable_id": stable_id})
                room_uuid_result = result.scalar_one_or_none()
                if room_uuid_result:
                    # CRITICAL FIX: asyncpg returns pgproto.UUID objects, not standard UUID objects
                    # Convert to string first, then to UUID to handle both string and UUID-like objects
                    # This prevents "'asyncpg.pgproto.pgproto.UUID' object has no attribute 'replace'" error
                    if isinstance(room_uuid_result, UUID):
                        # Already a standard UUID, return it directly
                        return room_uuid_result
                    # Handle string UUIDs (from tests or database)
                    if isinstance(room_uuid_result, str):
                        # Already a string, convert directly to UUID
                        return UUID(room_uuid_result)
                    # Convert to string first (handles asyncpg UUID objects), then to UUID
                    return UUID(str(room_uuid_result))
                return None

        except SQLAlchemyError as e:
            logger.error(
                "Database error looking up room UUID",
                stable_id=stable_id,
                error=str(e),
                error_type=type(e).__name__,
            )
            raise DatabaseError(f"Failed to look up room UUID: {e}") from e
        except Exception as e:  # pylint: disable=broad-except
            # Dimensional instability during room lookup must be recorded.
            logger.error(
                "Unexpected error looking up room UUID",
                stable_id=stable_id,
                error=str(e),
                error_type=type(e).__name__,
            )
            raise

    async def _mark_explored_in_session(self, session: AsyncSession, player_id: UUID, room_uuid: UUID) -> bool:
        """
        Mark room as explored using the provided session.

        Args:
            session: Database session
            player_id: UUID of the player
            room_uuid: UUID of the room

        Returns:
            True if successful, False otherwise
        """
        try:
            # Check if exploration record already exists
            check_query = text(
                """
                SELECT id FROM player_exploration
                WHERE player_id = :player_id AND room_id = :room_id
                """
            )
            result = await session.execute(check_query, {"player_id": str(player_id), "room_id": str(room_uuid)})
            existing = result.scalar_one_or_none()

            if existing:
                # Room already marked as explored
                logger.debug("Room already marked as explored", player_id=player_id, room_id=room_uuid)
                return True

            # Insert new exploration record
            insert_query = text(
                """
                INSERT INTO player_exploration (player_id, room_id, explored_at)
                VALUES (:player_id, :room_id, :explored_at)
                ON CONFLICT (player_id, room_id) DO NOTHING
                """
            )
            await session.execute(
                insert_query,
                {
                    "player_id": str(player_id),
                    "room_id": str(room_uuid),
                    "explored_at": datetime.now(UTC),
                },
            )

            logger.info("Room marked as explored", player_id=player_id, room_id=room_uuid)
            return True

        except SQLAlchemyError as e:
            logger.error(
                "Database error in _mark_explored_in_session",
                player_id=player_id,
                room_id=room_uuid,
                error=str(e),
            )
            raise

    async def get_explored_rooms(self, player_id: UUID, session: AsyncSession) -> list[str]:
        """
        Get list of room IDs that a player has explored.

        Args:
            player_id: UUID of the player
            session: Database session

        Returns:
            List of room IDs (as strings) that the player has explored

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            query = text(
                """
                SELECT room_id FROM player_exploration
                WHERE player_id = :player_id
                ORDER BY explored_at ASC
                """
            )
            result = await session.execute(query, {"player_id": str(player_id)})
            # fetchall() is synchronous, but handle both sync and async mocks in tests
            rows = result.fetchall()
            # Handle case where fetchall might return a coroutine (async mock in tests)
            if hasattr(rows, "__await__"):
                rows = await rows
            room_ids = [str(row[0]) for row in rows]

            logger.debug("Retrieved explored rooms", player_id=player_id, count=len(room_ids))
            return room_ids

        except SQLAlchemyError as e:
            logger.error(
                "Database error retrieving explored rooms",
                player_id=player_id,
                error=str(e),
                error_type=type(e).__name__,
            )
            raise DatabaseError(f"Failed to retrieve explored rooms: {e}") from e
        except Exception as e:  # pylint: disable=broad-except
            # Unforeseen disruptions in the retrieval of spatial memories.
            logger.error(
                "Unexpected error retrieving explored rooms",
                player_id=player_id,
                error=str(e),
                error_type=type(e).__name__,
            )
            raise

    async def is_room_explored(self, player_id: UUID, room_id: str, session: AsyncSession) -> bool:
        """
        Check if a player has explored a specific room.

        Args:
            player_id: UUID of the player
            room_id: Hierarchical room ID (string) to check
            session: Database session

        Returns:
            True if the room has been explored, False otherwise

        Raises:
            DatabaseError: If database operation fails
        """
        try:
            # Look up the room UUID by stable_id
            room_uuid = await self._get_room_uuid_by_stable_id(room_id, session)
            if not room_uuid:
                return False

            query = text(
                """
                SELECT EXISTS(
                    SELECT 1 FROM player_exploration
                    WHERE player_id = :player_id AND room_id = :room_id
                )
                """
            )
            result = await session.execute(query, {"player_id": str(player_id), "room_id": str(room_uuid)})
            exists = result.scalar_one()

            return bool(exists)

        except SQLAlchemyError as e:
            logger.error(
                "Database error checking room exploration",
                player_id=player_id,
                room_id=room_id,
                error=str(e),
                error_type=type(e).__name__,
            )
            raise DatabaseError(f"Failed to check room exploration: {e}") from e
        except Exception as e:  # pylint: disable=broad-except
            # Dimensional resonance failures during exploration verification.
            logger.error(
                "Unexpected error checking room exploration",
                player_id=player_id,
                room_id=room_id,
                error=str(e),
                error_type=type(e).__name__,
            )
            raise

    def mark_room_as_explored_sync(self, player_id: UUID, room_id: str, error_handler: Any = None) -> None:
        """
        Synchronous wrapper for mark_room_as_explored.

        This method is designed to be called from synchronous code (like MovementService).
        It fires off the async operation in the background and handles errors gracefully
        so that exploration failures don't block movement.

        Args:
            player_id: UUID of the player
            room_id: Room ID that was explored
            error_handler: Optional error handler function. If provided, errors will be
                passed to this handler instead of being logged.

        Note:
            This method is fire-and-forget. Errors are logged but don't raise exceptions.
            This ensures exploration failures don't block movement operations.
        """

        async def _mark_explored_async():
            """Inner async function to mark room as explored."""
            try:
                await self.mark_room_as_explored(player_id, room_id)
            except (DatabaseError, SQLAlchemyError) as e:
                # Log specific database/exploration errors from the service
                if error_handler:
                    error_handler(e)
                else:
                    logger.warning(
                        "Error marking room as explored (non-blocking database error)",
                        player_id=player_id,
                        room_id=room_id,
                        error=str(e),
                        error_type=type(e).__name__,
                    )
            except Exception as e:  # pylint: disable=broad-except
                # As documented in the Great Library of Celephaïs, unforeseen dimensional
                # ripples (unexpected exceptions) must be contained to prevent them from
                # disrupting the primary thread of reality (the player's movement).
                # We catch all exceptions here because this is a fire-and-forget background
                # task that must never block core game mechanics.
                if error_handler:
                    error_handler(e)
                else:
                    logger.error(
                        "Unexpected error in exploration background task",
                        player_id=player_id,
                        room_id=room_id,
                        error=str(e),
                        error_type=type(e).__name__,
                    )

        try:
            # Try to get the current event loop
            try:
                loop = asyncio.get_running_loop()
                # If we have a running loop, schedule the coroutine as a task
                # This is fire-and-forget - we don't await it
                loop.create_task(_mark_explored_async())
            except RuntimeError:
                # CRITICAL FIX: No running loop - log and skip instead of asyncio.run()
                # asyncio.run() can cause RuntimeError if called from event loop context
                # and creates unnecessary overhead. Since this is fire-and-forget,
                # it's safe to skip if no loop is available.
                # AI Agent: This should rarely happen as server runs in async context
                logger.warning(
                    "No event loop available for exploration tracking (skipped)",
                    player_id=player_id,
                    room_id=room_id,
                    reason="no_running_loop",
                )
                # Alternative: Could use threading to run in background, but adds complexity
                # Since exploration is non-critical, skipping is acceptable

        except Exception as e:  # pylint: disable=broad-except
            # As recorded in the Elder Signs, even the most basic attempts to manifest
            # intention (scheduling the task) can be thwarted by the Outer Gods.
            # We catch all exceptions here to ensure that scheduling failures do not
            # disrupt the player's immediate experience.
            # Log error but don't raise - exploration failures shouldn't block movement
            if error_handler:
                error_handler(e)
            else:
                logger.warning(
                    "Error scheduling exploration tracking (non-blocking)",
                    player_id=player_id,
                    room_id=room_id,
                    error=str(e),
                    error_type=type(e).__name__,
                )
