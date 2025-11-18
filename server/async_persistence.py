"""
Async persistence layer for MythosMUD.

This module provides an async version of the persistence layer using SQLAlchemy ORM
for true async PostgreSQL database operations without blocking the event loop.
"""

import json

from sqlalchemy import select

from .database import get_async_session
from .exceptions import DatabaseError
from .logging.enhanced_logging_config import get_logger
from .models.player import Player
from .models.profession import Profession
from .utils.error_logging import create_error_context, log_and_raise
from .utils.retry import retry_with_backoff

logger = get_logger(__name__)

# Player table columns for explicit SELECT queries (avoids SELECT * anti-pattern)
# Exported for security tests that verify compile-time constants
PLAYER_COLUMNS = (
    "player_id, user_id, name, current_room_id, profession_id, "
    "experience_points, level, stats, inventory, status_effects, "
    "created_at, last_active, is_admin"
)
# Convert tuple to string for compatibility with security tests
PLAYER_COLUMNS = "".join(PLAYER_COLUMNS)

# Profession table columns for explicit SELECT queries
PROFESSION_COLUMNS = "id, name, description, flavor_text, is_available"


class AsyncPersistenceLayer:
    """
    Async persistence layer using SQLAlchemy ORM for true async PostgreSQL operations.

    This provides async database operations that don't block the event loop.
    Uses SQLAlchemy ORM with async sessions for type-safe, maintainable queries.
    """

    def __init__(self, db_path: str | None = None, log_path: str | None = None, event_bus=None):
        """Initialize the async persistence layer."""
        # db_path parameter kept for backward compatibility but not used
        # Database connection is managed by SQLAlchemy via get_async_session()
        self.log_path = log_path
        self._event_bus = event_bus
        self._logger = get_logger(__name__)
        self._load_room_cache()

    def _load_room_cache(self) -> None:
        """Load room cache using environment-aware world loader."""
        try:
            # Prefer the unified world loader which respects LOGGING_ENVIRONMENT
            from .world_loader import ROOMS_BASE_PATH, load_hierarchical_world

            world_data = load_hierarchical_world()
            rooms = world_data.get("rooms", {})

            # Store raw room dicts keyed by id for quick existence checks
            self._room_cache = dict(rooms)

            self._logger.info(
                "Room cache loaded",
                room_count=len(self._room_cache),
                rooms_base_path=str(ROOMS_BASE_PATH),
            )
        except (OSError, json.JSONDecodeError) as e:
            self._logger.error("Error loading room cache", error=str(e), error_type=type(e).__name__)
            self._room_cache = {}
        except Exception as e:
            # Fallback to empty cache on unexpected errors to avoid startup failure
            self._logger.error("Unexpected error loading room cache", error=str(e))
            self._room_cache = {}

    async def close(self) -> None:
        """Close and cleanup resources.

        Note: SQLAlchemy async sessions are managed by the session context manager,
        so no explicit cleanup is needed here. This method is kept for backward compatibility.
        """
        self._logger.debug("AsyncPersistenceLayer.close() called - no cleanup needed (sessions managed by context)")

    @retry_with_backoff(max_attempts=3, initial_delay=1.0, max_delay=10.0)
    async def get_player_by_name(self, name: str) -> Player | None:
        """Get a player by name using SQLAlchemy ORM."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_player_by_name"
        context.metadata["player_name"] = name

        try:
            async for session in get_async_session():
                stmt = select(Player).where(Player.name == name)
                result = await session.execute(stmt)
                player = result.scalar_one_or_none()
                if player:
                    self.validate_and_fix_player_room(player)
                    return player
                return None
                # Explicit return after loop to satisfy mypy
            return None
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by name '{name}': {e}",
                context=context,
                details={"player_name": name, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )

    @retry_with_backoff(max_attempts=3, initial_delay=1.0, max_delay=10.0)
    async def get_player_by_id(self, player_id: str) -> Player | None:
        """Get a player by ID using SQLAlchemy ORM."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_player_by_id"
        player_id = str(player_id)
        context.metadata["player_id"] = player_id

        try:
            async for session in get_async_session():
                stmt = select(Player).where(Player.player_id == player_id)
                result = await session.execute(stmt)
                player = result.scalar_one_or_none()
                if player:
                    self.validate_and_fix_player_room(player)
                    return player
                return None
                # Explicit return after loop to satisfy mypy
            return None
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by ID '{player_id}': {e}",
                context=context,
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )

    async def get_player_by_user_id(self, user_id: str) -> Player | None:
        """Get a player by user ID using SQLAlchemy ORM."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_player_by_user_id"
        context.metadata["user_id"] = user_id

        try:
            async for session in get_async_session():
                stmt = select(Player).where(Player.user_id == user_id)
                result = await session.execute(stmt)
                player = result.scalar_one_or_none()
                if player:
                    self.validate_and_fix_player_room(player)
                    return player
                return None
                # Explicit return after loop to satisfy mypy
            return None
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by user ID '{user_id}': {e}",
                context=context,
                details={"user_id": user_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )

    @retry_with_backoff(max_attempts=3, initial_delay=1.0, max_delay=10.0)
    async def save_player(self, player: Player) -> None:
        """Save a player using SQLAlchemy ORM (upsert behavior via merge)."""
        context = create_error_context()
        context.metadata["operation"] = "async_save_player"
        context.metadata["player_name"] = player.name
        context.metadata["player_id"] = str(player.player_id)

        try:
            async for session in get_async_session():
                # SQLAlchemy ORM handles JSON serialization automatically via Column[Text] types
                # Player model's stats, inventory, and status_effects are Column[str] that store JSON
                # The ORM will persist the current Column values, which are already JSON strings
                # Use merge() for upsert behavior - inserts if new, updates if exists
                await session.merge(player)
                await session.commit()
                self._logger.debug("Player saved successfully", player_id=str(player.player_id))
                return
            # Explicit return after loop to satisfy mypy
            return
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error saving player: {e}",
                context=context,
                details={"player_name": player.name, "player_id": str(player.player_id), "error": str(e)},
                user_friendly="Failed to save player",
            )

    async def list_players(self) -> list[Player]:
        """List all players using SQLAlchemy ORM."""
        context = create_error_context()
        context.metadata["operation"] = "async_list_players"

        try:
            async for session in get_async_session():
                stmt = select(Player)
                result = await session.execute(stmt)
                players = list(result.scalars().all())
                # Validate and fix room for each player
                for player in players:
                    self.validate_and_fix_player_room(player)
                return players
                # Explicit return after loop to satisfy mypy
            return []
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error listing players: {e}",
                context=context,
                details={"error": str(e)},
                user_friendly="Failed to retrieve player list",
            )

    async def get_players_in_room(self, room_id: str) -> list[Player]:
        """Get all players in a specific room using SQLAlchemy ORM."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_players_in_room"
        context.metadata["room_id"] = room_id

        try:
            async for session in get_async_session():
                stmt = select(Player).where(Player.current_room_id == room_id)
                result = await session.execute(stmt)
                players = list(result.scalars().all())
                # Validate and fix room for each player
                for player in players:
                    self.validate_and_fix_player_room(player)
                return players
                # Explicit return after loop to satisfy mypy
            return []
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error getting players in room: {e}",
                context=context,
                details={"room_id": room_id, "error": str(e)},
                user_friendly="Failed to retrieve players in room",
            )

    async def save_players(self, players: list[Player]) -> None:
        """Save multiple players using SQLAlchemy ORM in a single transaction."""
        context = create_error_context()
        context.metadata["operation"] = "async_save_players"
        context.metadata["player_count"] = len(players)

        try:
            async for session in get_async_session():
                # Batch save in a single transaction for atomicity
                # SQLAlchemy ORM handles JSON serialization automatically via Column[Text] types
                for player in players:
                    try:
                        # Use merge() for upsert behavior
                        await session.merge(player)
                    except (ValueError, TypeError, KeyError) as e:
                        # Data validation errors: log and continue with other players
                        self._logger.warning(
                            "Error saving player (data validation error)",
                            error=str(e),
                            error_type=type(e).__name__,
                            player_id=str(player.player_id),
                        )
                        continue

                # Commit all players in a single transaction
                await session.commit()
                self._logger.debug("Players saved successfully", player_count=len(players))
                return
            # Explicit return after loop to satisfy mypy
            return
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error saving players: {e}",
                context=context,
                details={"player_count": len(players), "error": str(e)},
                user_friendly="Failed to save players",
            )

    async def delete_player(self, player_id: str) -> bool:
        """Delete a player using SQLAlchemy ORM."""
        context = create_error_context()
        context.metadata["operation"] = "async_delete_player"
        context.metadata["player_id"] = player_id

        try:
            async for session in get_async_session():
                # First check if player exists
                stmt = select(Player).where(Player.player_id == player_id)
                result = await session.execute(stmt)
                player = result.scalar_one_or_none()

                if not player:
                    self._logger.warning("Player not found for deletion", player_id=player_id)
                    return False

                player_name = player.name

                # Delete the player using ORM
                await session.delete(player)
                await session.commit()

                self._logger.info("Player deleted successfully", player_id=player_id, player_name=player_name)
                return True
                # Explicit return after loop to satisfy mypy
            return False
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error deleting player: {e}",
                context=context,
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to delete player",
            )

    async def get_professions(self) -> list[Profession]:
        """Get all available professions using SQLAlchemy ORM."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_professions"

        try:
            async for session in get_async_session():
                # SQLAlchemy Column supports == comparison even with type annotations
                # The type annotation is for runtime value access, not query construction
                # At runtime, Profession.is_available is a Column, not a bool
                stmt = select(Profession).where(Profession.is_available == True).order_by(Profession.id)  # type: ignore[arg-type]  # noqa: E712
                result = await session.execute(stmt)
                professions = list(result.scalars().all())
                return professions
                # Explicit return after loop to satisfy mypy
            return []
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving professions: {e}",
                context=context,
                details={"error": str(e)},
                user_friendly="Failed to retrieve professions",
            )

    async def get_profession_by_id(self, profession_id: int) -> Profession | None:
        """Get a profession by ID using SQLAlchemy ORM."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_profession_by_id"
        context.metadata["profession_id"] = profession_id

        try:
            async for session in get_async_session():
                stmt = select(Profession).where(Profession.id == profession_id)
                result = await session.execute(stmt)
                profession = result.scalar_one_or_none()
                return profession
                # Explicit return after loop to satisfy mypy
            return None
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving profession: {e}",
                context=context,
                details={"profession_id": profession_id, "error": str(e)},
                user_friendly="Failed to retrieve profession",
            )

    def validate_and_fix_player_room(self, player: Player) -> None:
        """Validate and fix player room if needed."""
        if not hasattr(player, "current_room_id") or not player.current_room_id:
            player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"  # type: ignore[assignment]
            self._logger.warning("Fixed player with missing room", player_id=str(player.player_id))

        # Check if room exists in cache
        if hasattr(self, "_room_cache") and player.current_room_id not in self._room_cache:
            self._logger.warning(
                "Player in unknown room", player_id=str(player.player_id), room_id=player.current_room_id
            )


# DEPRECATED: Module-level global singleton removed - use ApplicationContainer instead
# Keeping these functions for backward compatibility during migration
_async_persistence_instance: AsyncPersistenceLayer | None = None


def get_async_persistence() -> AsyncPersistenceLayer:
    """
    Get the global async persistence instance.

    DEPRECATED: Use ApplicationContainer.async_persistence instead.
    This function exists only for backward compatibility during migration.

    Returns:
        AsyncPersistenceLayer: The async persistence instance
    """
    global _async_persistence_instance
    if _async_persistence_instance is None:
        _async_persistence_instance = AsyncPersistenceLayer()
    return _async_persistence_instance


def reset_async_persistence() -> None:
    """
    Reset the global async persistence instance for testing.

    DEPRECATED: Use ApplicationContainer.reset_instance() instead.
    This function exists only for backward compatibility during migration.
    """
    global _async_persistence_instance
    _async_persistence_instance = None
