"""
Async persistence layer for MythosMUD.

This module provides an async version of the persistence layer using SQLAlchemy ORM
for true async PostgreSQL database operations without blocking the event loop.
"""

import asyncio
import uuid
from typing import TYPE_CHECKING, Any

from sqlalchemy import select

from .database import get_async_session
from .exceptions import DatabaseError
from .logging.enhanced_logging_config import get_logger
from .models.player import Player
from .models.profession import Profession
from .utils.error_logging import create_error_context, log_and_raise
from .utils.retry import retry_with_backoff

if TYPE_CHECKING:
    from .models.room import Room

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
        self._room_cache: dict[str, Room] = {}
        self._room_mappings: dict[str, Any] = {}
        self._load_room_cache()

    def _load_room_cache(self) -> None:
        """Load rooms from PostgreSQL database and convert to Room objects."""
        try:
            # Always use a thread with a new event loop to avoid event loop conflicts
            # The database engine may be tied to a different event loop, so we need isolation
            import threading

            result_container: dict[str, Any] = {"rooms": {}, "error": None}

            def run_async():
                new_loop = asyncio.new_event_loop()
                asyncio.set_event_loop(new_loop)
                try:
                    new_loop.run_until_complete(self._async_load_room_cache(result_container))
                finally:
                    new_loop.close()

            # Use thread approach to ensure complete event loop isolation
            thread = threading.Thread(target=run_async)
            thread.start()
            thread.join()

            # Copy results from thread
            error = result_container.get("error")
            if error is not None:
                if isinstance(error, BaseException):
                    raise error
                raise RuntimeError(f"Unexpected error type: {type(error)}")
            rooms = result_container.get("rooms")
            if rooms is not None and isinstance(rooms, dict):
                self._room_cache = rooms
            else:
                self._room_cache = {}

            self._logger.info(
                "Loaded rooms into cache from PostgreSQL database",
                room_count=len(self._room_cache),
                mapping_count=len(self._room_mappings),
            )
            # Debug: Log sample room IDs for troubleshooting
            if self._room_cache:
                sample_room_ids = list(self._room_cache.keys())[:5]
                self._logger.debug("Sample room IDs loaded", sample_room_ids=sample_room_ids)
        except Exception as e:
            context = create_error_context()
            context.metadata["operation"] = "load_room_cache"
            self._logger.error(
                "Room cache load failed",
                error=str(e),
                error_type=type(e).__name__,
                operation="load_room_cache",
            )
            # Fallback to empty cache on error to avoid startup failure
            self._room_cache = {}

    async def _async_load_room_cache(self, result_container: dict[str, Any]) -> None:
        """Async helper to load rooms from PostgreSQL database."""
        import os

        import asyncpg

        from .models.room import Room
        from .world_loader import generate_room_id

        # Get database URL from environment
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise ValueError("DATABASE_URL environment variable not set")

        # Convert SQLAlchemy-style URL to asyncpg-compatible format
        # asyncpg expects postgresql:// not postgresql+asyncpg://
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

        try:
            # Use asyncpg directly to avoid event loop conflicts
            # Create a new connection in this event loop
            conn = await asyncpg.connect(database_url)
            try:
                # Query rooms with zone/subzone hierarchy
                rooms_query = """
                    SELECT
                        r.id as room_uuid,
                        r.stable_id,
                        r.name,
                        r.description,
                        r.attributes,
                        sz.stable_id as subzone_stable_id,
                        z.stable_id as zone_stable_id,
                        -- Extract plane from zone stable_id (format: 'plane/zone')
                        SPLIT_PART(z.stable_id, '/', 1) as plane,
                        SPLIT_PART(z.stable_id, '/', 2) as zone
                    FROM rooms r
                    JOIN subzones sz ON r.subzone_id = sz.id
                    JOIN zones z ON sz.zone_id = z.id
                    ORDER BY z.stable_id, sz.stable_id, r.stable_id
                """
                rooms_rows = await conn.fetch(rooms_query)

                # Query room links (exits) for all rooms
                exits_query = """
                    SELECT
                        r.stable_id as from_room_stable_id,
                        r2.stable_id as to_room_stable_id,
                        rl.direction,
                        sz.stable_id as from_subzone_stable_id,
                        z.stable_id as from_zone_stable_id,
                        sz2.stable_id as to_subzone_stable_id,
                        z2.stable_id as to_zone_stable_id
                    FROM room_links rl
                    JOIN rooms r ON rl.from_room_id = r.id
                    JOIN rooms r2 ON rl.to_room_id = r2.id
                    JOIN subzones sz ON r.subzone_id = sz.id
                    JOIN zones z ON sz.zone_id = z.id
                    JOIN subzones sz2 ON r2.subzone_id = sz2.id
                    JOIN zones z2 ON sz2.zone_id = z2.id
                """
                exits_rows = await conn.fetch(exits_query)

                # Process rooms and build room data list
                room_data_list = []

                for row in rooms_rows:
                    stable_id = row["stable_id"]
                    name = row["name"]
                    description = row["description"]
                    # asyncpg returns JSONB as dict, not string
                    attributes = row["attributes"] if row["attributes"] else {}
                    subzone_stable_id = row["subzone_stable_id"]
                    zone_stable_id = row["zone_stable_id"]

                    # Generate hierarchical room ID
                    zone_parts = zone_stable_id.split("/")
                    plane_name = zone_parts[0] if len(zone_parts) > 0 else ""
                    zone_name = zone_parts[1] if len(zone_parts) > 1 else zone_stable_id

                    # Check if stable_id already contains the full hierarchical path
                    # Expected format: plane_zone_subzone_room_xxx or plane_zone_subzone_intersection_xxx
                    # If stable_id already starts with plane_zone_subzone, it's a full room ID
                    expected_prefix = f"{plane_name}_{zone_name}_{subzone_stable_id}_"
                    if stable_id.startswith(expected_prefix):
                        # stable_id is already a full hierarchical room ID, use it directly
                        room_id = stable_id
                    else:
                        # stable_id is just the room identifier (e.g., "room_boundary_st_001"), generate full ID
                        room_id = generate_room_id(plane_name, zone_name, subzone_stable_id, stable_id)

                    # Store room data for processing
                    room_data_list.append(
                        {
                            "room_id": room_id,
                            "stable_id": stable_id,
                            "name": name,
                            "description": description,
                            "attributes": attributes,
                            "plane": plane_name,
                            "zone": zone_name,
                            "sub_zone": subzone_stable_id,
                        }
                    )

                # Build exits dictionary keyed by room_id (not stable_id)
                exits_by_room: dict[str, dict[str, str]] = {}
                for row in exits_rows:
                    from_stable_id = row["from_room_stable_id"]
                    to_stable_id = row["to_room_stable_id"]
                    direction = row["direction"]
                    from_subzone = row["from_subzone_stable_id"]
                    from_zone = row["from_zone_stable_id"]
                    to_subzone = row["to_subzone_stable_id"]
                    to_zone = row["to_zone_stable_id"]

                    # Generate hierarchical room IDs for both source and destination
                    from_zone_parts = from_zone.split("/")
                    from_plane = from_zone_parts[0] if len(from_zone_parts) > 0 else ""
                    from_zone_name = from_zone_parts[1] if len(from_zone_parts) > 1 else from_zone

                    to_zone_parts = to_zone.split("/")
                    to_plane = to_zone_parts[0] if len(to_zone_parts) > 0 else ""
                    to_zone_name = to_zone_parts[1] if len(to_zone_parts) > 1 else to_zone

                    # Check if stable_id already contains the full hierarchical path
                    # Expected format: plane_zone_subzone_room_xxx or plane_zone_subzone_intersection_xxx
                    # If stable_id already starts with plane_zone_subzone, it's a full room ID
                    from_expected_prefix = f"{from_plane}_{from_zone_name}_{from_subzone}_"
                    if from_stable_id.startswith(from_expected_prefix):
                        # stable_id is already a full hierarchical room ID, use it directly
                        from_room_id = from_stable_id
                    else:
                        # stable_id is just the room identifier, generate full ID
                        from_room_id = generate_room_id(from_plane, from_zone_name, from_subzone, from_stable_id)

                    to_expected_prefix = f"{to_plane}_{to_zone_name}_{to_subzone}_"
                    if to_stable_id.startswith(to_expected_prefix):
                        # stable_id is already a full hierarchical room ID, use it directly
                        to_room_id = to_stable_id
                    else:
                        # stable_id is just the room identifier, generate full ID
                        to_room_id = generate_room_id(to_plane, to_zone_name, to_subzone, to_stable_id)

                    if from_room_id not in exits_by_room:
                        exits_by_room[from_room_id] = {}

                    exits_by_room[from_room_id][direction] = to_room_id

                    # Debug logging for specific room
                    if from_stable_id == "earth_arkhamcity_sanitarium_room_foyer_001":
                        self._logger.info(
                            "Debugging exit processing",
                            from_stable_id=from_stable_id,
                            from_room_id=from_room_id,
                            from_expected_prefix=from_expected_prefix,
                            direction=direction,
                            to_room_id=to_room_id,
                        )

                # Convert database rows to Room objects
                for room_data_item in room_data_list:
                    room_id = room_data_item["room_id"]
                    name = room_data_item["name"]
                    description = room_data_item["description"]
                    attributes = room_data_item["attributes"]
                    plane_name = room_data_item["plane"]
                    zone_name = room_data_item["zone"]
                    subzone_stable_id = room_data_item["sub_zone"]

                    # Get exits for this room (already resolved to full room IDs)
                    exits = exits_by_room.get(room_id, {})

                    # Debug logging for exit matching
                    if room_id == "earth_arkhamcity_sanitarium_room_foyer_001":
                        self._logger.info(
                            "Debugging exit matching",
                            room_id=room_id,
                            exits_found=exits,
                            exits_by_room_keys=list(exits_by_room.keys())[:10],
                            exits_by_room_size=len(exits_by_room),
                        )

                    # Build room data dictionary matching Room class expectations
                    room_data = {
                        "id": room_id,
                        "name": name,
                        "description": description,
                        "plane": plane_name,
                        "zone": zone_name,
                        "sub_zone": subzone_stable_id,
                        "resolved_environment": attributes.get("environment", "outdoors")
                        if isinstance(attributes, dict)
                        else "outdoors",
                        "exits": exits,
                    }

                    result_container["rooms"][room_id] = Room(room_data, self._event_bus)
            finally:
                await conn.close()
        except Exception as e:
            result_container["error"] = e
            raise

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
    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        """Get a player by ID using SQLAlchemy ORM."""
        context = create_error_context()
        context.metadata["operation"] = "async_get_player_by_id"
        # Structlog handles UUID objects automatically, no need to convert to string
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
        # Structlog handles UUID objects automatically, no need to convert to string
        context.metadata["player_id"] = player.player_id

        try:
            # Ensure is_admin is an integer (PostgreSQL requires integer, not boolean)
            # Convert boolean to integer if needed (0 for False, 1 for True)
            # Note: is_admin is Integer column with nullable=False, so it can't be None
            if isinstance(getattr(player, "is_admin", None), bool):
                player.is_admin = 1 if player.is_admin else 0  # type: ignore[assignment]

            async for session in get_async_session():
                # SQLAlchemy ORM handles JSON serialization automatically via Column[Text] types
                # Player model's stats, inventory, and status_effects are Column[str] that store JSON
                # The ORM will persist the current Column values, which are already JSON strings
                # Use merge() for upsert behavior - inserts if new, updates if exists
                await session.merge(player)
                await session.commit()
                # Structlog handles UUID objects automatically, no need to convert to string
                self._logger.debug("Player saved successfully", player_id=player.player_id)
                return
            # Explicit return after loop to satisfy mypy
            return
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Database error saving player: {e}",
                context=context,
                # Structlog handles UUID objects automatically, no need to convert to string
                details={"player_name": player.name, "player_id": player.player_id, "error": str(e)},
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

    def get_room_by_id(self, room_id: str) -> "Room | None":
        """
        Get a room by ID from the cache (synchronous - rooms are cached at startup).

        Args:
            room_id: The room ID

        Returns:
            Room | None: The room object or None if not found
        """
        return self._room_cache.get(room_id)

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
            # Ensure is_admin is an integer for all players (PostgreSQL requires integer, not boolean)
            # Note: is_admin is Integer column with nullable=False, so it can't be None
            for player in players:
                if isinstance(getattr(player, "is_admin", None), bool):
                    player.is_admin = 1 if player.is_admin else 0  # type: ignore[assignment]

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
                            # Structlog handles UUID objects automatically, no need to convert to string
                            player_id=player.player_id,
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

    async def delete_player(self, player_id: uuid.UUID) -> bool:
        """Delete a player using SQLAlchemy ORM."""
        context = create_error_context()
        context.metadata["operation"] = "async_delete_player"
        # Structlog handles UUID objects automatically, no need to convert to string
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
            # Structlog handles UUID objects automatically, no need to convert to string
            self._logger.warning("Fixed player with missing room", player_id=player.player_id)

        # Check if room exists in cache
        if hasattr(self, "_room_cache") and player.current_room_id not in self._room_cache:
            self._logger.warning(
                # Structlog handles UUID objects automatically, no need to convert to string
                "Player in unknown room",
                player_id=player.player_id,
                room_id=player.current_room_id,
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
