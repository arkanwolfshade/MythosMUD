"""
Async persistence layer for MythosMUD.

This module provides an async version of the persistence layer using SQLAlchemy ORM
for true async PostgreSQL database operations without blocking the event loop.

This is now a facade that delegates to focused async repositories.
"""

import asyncio
import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from .database import get_async_session
from .exceptions import DatabaseError, ValidationError
from .structured_logging.enhanced_logging_config import get_logger
from .models.player import Player
from .models.profession import Profession
from .models.user import User
from .persistence.repositories import (
    ContainerRepository,
    ExperienceRepository,
    HealthRepository,
    ItemRepository,
    PlayerRepository,
    ProfessionRepository,
    RoomRepository,
)
from .persistence.repositories.container_repository import ContainerCreateParams
from .utils.error_logging import create_error_context, log_and_raise

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

    def __init__(
        self, _db_path: str | None = None, _log_path: str | None = None, event_bus=None, _skip_room_cache: bool = False
    ):
        """
        Initialize the async persistence layer.

        This facade delegates to focused async repositories for better maintainability.

        Args:
            _db_path: Deprecated - kept for backward compatibility only
            _log_path: Deprecated - kept for backward compatibility only
            event_bus: Optional event bus for publishing events
            _skip_room_cache: If True, skip loading room cache during initialization.
                             Used in tests to avoid thread-based initialization race conditions.
        """
        # Parameters prefixed with _ are kept for backward compatibility but not used
        # Database connection is managed by SQLAlchemy via get_async_session()
        # Logging is managed by enhanced_logging_config
        self._event_bus = event_bus
        self._logger = get_logger(__name__)
        self._room_cache: dict[str, Room] = {}
        self._room_mappings: dict[str, Any] = {}
        if not _skip_room_cache:
            self._load_room_cache()

        # Initialize repositories (facade pattern)
        self._room_repo = RoomRepository(self._room_cache)
        self._player_repo = PlayerRepository(self._room_cache, event_bus)
        self._profession_repo = ProfessionRepository()
        self._experience_repo = ExperienceRepository(event_bus=event_bus)
        self._health_repo = HealthRepository(event_bus=event_bus)
        self._container_repo = ContainerRepository()
        self._item_repo = ItemRepository(
            None
        )  # ItemRepository handles None persistence layer by using sync persistence internally if needed

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
        except (DatabaseError, OSError, RuntimeError) as e:
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
        database_url = self._get_database_url()
        conn = await self._connect_to_database(database_url)
        try:
            await self._load_rooms_data(conn, result_container)
        finally:
            await conn.close()

    def _get_database_url(self) -> str:
        """Get and normalize database URL from environment."""
        import os

        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise ValueError("DATABASE_URL environment variable not set")

        # Convert SQLAlchemy-style URL to asyncpg-compatible format
        # asyncpg expects postgresql:// not postgresql+asyncpg://
        if database_url.startswith("postgresql+asyncpg://"):
            database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

        return database_url

    async def _connect_to_database(self, database_url: str) -> Any:
        """Create asyncpg connection to database."""
        import asyncpg

        # Use asyncpg directly to avoid event loop conflicts
        # Create a new connection in this event loop
        return await asyncpg.connect(database_url)

    async def _load_rooms_data(self, conn: Any, result_container: dict[str, Any]) -> None:
        """Load and process room data from database."""
        rooms_rows = []
        try:
            # Query rooms and exits from database
            rooms_rows = await self._query_rooms_from_db(conn)
            exits_rows = await self._query_exits_from_db(conn)

            # Process database rows into structured data
            room_data_list = self._process_room_rows(rooms_rows)
            exits_by_room = self._process_exit_rows(exits_rows)

            # Convert to Room objects and store in result container
            self._build_room_objects(room_data_list, exits_by_room, result_container)
        except (DatabaseError, OSError, RuntimeError, ConnectionError, TimeoutError) as e:
            # Catch specific database and connection errors
            error_msg = str(e).lower()
            if "does not exist" in error_msg or "relation" in error_msg or len(rooms_rows) == 0:
                # Tables don't exist or are empty - initialize empty cache
                result_container["rooms"] = {}
                self._logger.warning(
                    "Room tables not found or empty, initializing with empty cache",
                    error=str(e),
                    rooms_count=len(rooms_rows),
                )
            else:
                # Other errors should be raised
                result_container["error"] = e
                raise
        except Exception as e:  # pylint: disable=broad-exception-caught
            # Catch any other unexpected exceptions (e.g., asyncpg exceptions, test mocks)
            # This is necessary for test compatibility where mocks may raise generic Exception
            # and to handle asyncpg-specific exceptions that don't inherit from standard types
            error_msg = str(e).lower()
            if "does not exist" in error_msg or "relation" in error_msg or len(rooms_rows) == 0:
                # Tables don't exist or are empty - initialize empty cache
                result_container["rooms"] = {}
                self._logger.warning(
                    "Room tables not found or empty, initializing with empty cache",
                    error=str(e),
                    rooms_count=len(rooms_rows),
                )
            else:
                # Other errors should be raised
                result_container["error"] = e
                raise

    async def _query_rooms_from_db(self, conn: Any) -> list[Any]:
        """Query rooms with zone/subzone hierarchy from database."""
        # Use LEFT JOIN to handle empty tables gracefully
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
            LEFT JOIN subzones sz ON r.subzone_id = sz.id
            LEFT JOIN zones z ON sz.zone_id = z.id
            ORDER BY z.stable_id, sz.stable_id, r.stable_id
        """
        try:
            return await conn.fetch(rooms_query)
        except Exception as e:
            # If query fails (e.g., tables don't exist), return empty list
            error_msg = str(e).lower()
            if "does not exist" in error_msg or "relation" in error_msg:
                self._logger.warning("Room tables not found, returning empty room list", error=str(e))
                return []
            raise

    async def _query_exits_from_db(self, conn: Any) -> list[Any]:
        """Query room links (exits) for all rooms from database."""
        # Use LEFT JOIN to handle empty tables gracefully
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
            LEFT JOIN rooms r ON rl.from_room_id = r.id
            LEFT JOIN rooms r2 ON rl.to_room_id = r2.id
            LEFT JOIN subzones sz ON r.subzone_id = sz.id
            LEFT JOIN zones z ON sz.zone_id = z.id
            LEFT JOIN subzones sz2 ON r2.subzone_id = sz2.id
            LEFT JOIN zones z2 ON sz2.zone_id = z2.id
        """
        try:
            return await conn.fetch(exits_query)
        except Exception as e:
            # If query fails (e.g., tables don't exist), return empty list
            error_msg = str(e).lower()
            if "does not exist" in error_msg or "relation" in error_msg:
                self._logger.warning("Room link tables not found, returning empty exit list", error=str(e))
                return []
            raise

    def _process_room_rows(self, rooms_rows: list[Any]) -> list[dict[str, Any]]:
        """Process room database rows into structured room data list."""
        from .world_loader import generate_room_id

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

        return room_data_list

    def _process_exit_rows(self, exits_rows: list[Any]) -> dict[str, dict[str, str]]:
        """Process exit database rows into exits dictionary keyed by room_id."""
        from .world_loader import generate_room_id

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

        return exits_by_room

    def _build_room_objects(
        self,
        room_data_list: list[dict[str, Any]],
        exits_by_room: dict[str, dict[str, str]],
        result_container: dict[str, Any],
    ) -> None:
        """Convert room data to Room objects and store in result container."""
        from .models.room import Room

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

    async def close(self) -> None:
        """Close and cleanup resources.

        Note: SQLAlchemy async sessions are managed by the session context manager,
        so no explicit cleanup is needed here. This method is kept for backward compatibility.
        """
        self._logger.debug("AsyncPersistenceLayer.close() called - no cleanup needed (sessions managed by context)")

    async def get_player_by_name(self, name: str) -> Player | None:
        """Get a player by name. Delegates to PlayerRepository."""
        return await self._player_repo.get_player_by_name(name)

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        """Get a player by ID. Delegates to PlayerRepository."""
        return await self._player_repo.get_player_by_id(player_id)

    async def get_players_by_user_id(self, user_id: str) -> list[Player]:
        """Get all players (including deleted) for a user ID. Delegates to PlayerRepository."""
        return await self._player_repo.get_players_by_user_id(user_id)

    async def get_active_players_by_user_id(self, user_id: str) -> list[Player]:
        """Get active (non-deleted) players for a user ID. Delegates to PlayerRepository."""
        return await self._player_repo.get_active_players_by_user_id(user_id)

    async def get_player_by_user_id(self, user_id: str) -> Player | None:
        """Get the first active player by user ID (backward compatibility). Delegates to PlayerRepository."""
        return await self._player_repo.get_player_by_user_id(user_id)

    async def soft_delete_player(self, player_id: uuid.UUID) -> bool:
        """Soft delete a player (sets is_deleted=True). Delegates to PlayerRepository."""
        return await self._player_repo.soft_delete_player(player_id)

    async def get_user_by_username_case_insensitive(self, username: str) -> User | None:
        """
        Get a user by username (case-insensitive).

        MULTI-CHARACTER: Usernames are stored case-sensitively but checked case-insensitively for uniqueness.

        Args:
            username: Username (case-insensitive matching)

        Returns:
            User | None: User object or None if not found

        Raises:
            DatabaseError: If database operation fails
        """
        from sqlalchemy import func

        context = create_error_context()
        context.metadata["operation"] = "get_user_by_username_case_insensitive"
        context.metadata["username"] = username

        try:
            async for session in get_async_session():
                # Use case-insensitive comparison
                stmt = select(User).where(func.lower(User.username) == func.lower(username))
                result = await session.execute(stmt)
                user = result.scalar_one_or_none()
                return user
            return None
        except (DatabaseError, ValidationError, SQLAlchemyError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving user by username '{username}': {e}",
                context=context,
                details={"username": username, "error": str(e)},
                user_friendly="Failed to retrieve user information",
            )

    async def save_player(self, player: Player) -> None:
        """Save a player. Delegates to PlayerRepository."""
        return await self._player_repo.save_player(player)

    async def list_players(self) -> list[Player]:
        """List all players. Delegates to PlayerRepository."""
        return await self._player_repo.list_players()

    def get_room_by_id(self, room_id: str) -> "Room | None":
        """Get a room by ID from the cache. Delegates to RoomRepository."""
        return self._room_repo.get_room_by_id(room_id)

    def list_rooms(self) -> list["Room"]:
        """
        List all rooms from the cache. Delegates to RoomRepository.

        Returns:
            list[Room]: List of all cached rooms
        """
        return self._room_repo.list_rooms()

    async def async_list_rooms(self) -> list["Room"]:
        """
        List all rooms from the cache. Delegates to RoomRepository.

        Returns:
            list[Room]: List of all cached rooms

        Note: This is async for API consistency, though the underlying
        operation is synchronous as rooms are cached in memory.
        """
        # RoomRepository.list_rooms() is synchronous but we expose it as async
        # for consistency with the async API surface
        return self._room_repo.list_rooms()

    async def get_players_in_room(self, room_id: str) -> list[Player]:
        """Get all players in a specific room. Delegates to PlayerRepository."""
        return await self._player_repo.get_players_in_room(room_id)

    async def save_players(self, players: list[Player]) -> None:
        """Save multiple players in a single transaction. Delegates to PlayerRepository."""
        return await self._player_repo.save_players(players)

    async def delete_player(self, player_id: uuid.UUID) -> bool:
        """Delete a player. Delegates to PlayerRepository."""
        return await self._player_repo.delete_player(player_id)

    async def update_player_last_active(self, player_id: uuid.UUID, last_active: datetime | None = None) -> None:
        """Update the last_active timestamp for a player. Delegates to PlayerRepository."""
        await self._player_repo.update_player_last_active(player_id, last_active)

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
        except (SQLAlchemyError, OSError) as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving professions: {e}",
                context=context,
                details={"error": str(e)},
                user_friendly="Failed to retrieve professions",
            )

    async def get_profession_by_id(self, profession_id: int) -> Profession | None:
        """Get a profession by ID. Delegates to ProfessionRepository."""
        return await self._profession_repo.get_profession_by_id(profession_id)

    def validate_and_fix_player_room(self, player: Player) -> bool:
        """Validate and fix player room if needed. Delegates to PlayerRepository."""
        return self._player_repo.validate_and_fix_player_room(player)

    async def apply_lucidity_loss(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Apply lucidity loss to a player. Delegates to ExperienceRepository."""
        player_id = uuid.UUID(str(player.player_id))  # Convert Column to UUID for type checking
        await self._experience_repo.update_player_stat_field(player_id, "lucidity", -amount, f"{source}: lucidity loss")

    async def apply_fear(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Apply fear to a player. Delegates to ExperienceRepository."""
        player_id = uuid.UUID(str(player.player_id))  # Convert Column to UUID for type checking
        await self._experience_repo.update_player_stat_field(player_id, "fear", amount, f"{source}: fear increase")

    async def apply_corruption(self, player: Player, amount: int, source: str = "unknown") -> None:
        """Apply corruption to a player. Delegates to ExperienceRepository."""
        player_id = uuid.UUID(str(player.player_id))  # Convert Column to UUID for type checking
        await self._experience_repo.update_player_stat_field(
            player_id, "corruption", amount, f"{source}: corruption increase"
        )

    async def heal_player(self, player: Player, amount: int) -> None:
        """Heal a player. Delegates to HealthRepository."""
        await self._health_repo.heal_player(player, amount)

    async def async_heal_player(self, player: Player, amount: int) -> None:
        """Async alias for heal_player. Delegates to HealthRepository."""
        await self._health_repo.heal_player(player, amount)

    async def damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
        """Damage a player. Delegates to HealthRepository."""
        await self._health_repo.damage_player(player, amount, damage_type)

    async def async_damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
        """Async alias for damage_player. Delegates to HealthRepository."""
        await self._health_repo.damage_player(player, amount, damage_type)

    # Container methods
    async def create_container(
        self,
        source_type: str,
        params: ContainerCreateParams | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create a new container.

        Args:
            source_type: Type of container source (required)
            params: ContainerCreateParams object with all optional parameters (preferred)
            **kwargs: Individual parameters for backward compatibility

        Returns:
            dict: Container data dictionary
        """
        # Use params object if provided, otherwise create from kwargs
        if params is None:
            params = ContainerCreateParams(
                owner_id=kwargs.get("owner_id"),
                room_id=kwargs.get("room_id"),
                entity_id=kwargs.get("entity_id"),
                lock_state=kwargs.get("lock_state", "unlocked"),
                capacity_slots=kwargs.get("capacity_slots", 20),
                weight_limit=kwargs.get("weight_limit"),
                decay_at=kwargs.get("decay_at"),
                allowed_roles=kwargs.get("allowed_roles"),
                items_json=kwargs.get("items_json"),
                metadata_json=kwargs.get("metadata_json"),
            )

        return await self._container_repo.create_container(
            source_type,
            params,
        )

    async def get_container(self, container_id: uuid.UUID) -> dict[str, Any] | None:
        """Get a container by ID."""
        return await self._container_repo.get_container(container_id)

    async def get_containers_by_room_id(self, room_id: str) -> list[dict[str, Any]]:
        """Get all containers in a room."""
        return await self._container_repo.get_containers_by_room_id(room_id)

    async def get_containers_by_entity_id(self, entity_id: uuid.UUID) -> list[dict[str, Any]]:
        """Get all containers owned by an entity."""
        return await self._container_repo.get_containers_by_entity_id(entity_id)

    async def update_container(
        self,
        container_id: uuid.UUID,
        items_json: list[dict[str, Any]] | None = None,
        lock_state: str | None = None,
        metadata_json: dict[str, Any] | None = None,
    ) -> dict[str, Any] | None:
        """Update a container."""
        return await self._container_repo.update_container(container_id, items_json, lock_state, metadata_json)

    async def get_decayed_containers(self, current_time: datetime | None = None) -> list[dict[str, Any]]:
        """Get decayed containers."""
        return await self._container_repo.get_decayed_containers(current_time)

    async def delete_container(self, container_id: uuid.UUID) -> bool:
        """Delete a container."""
        return await self._container_repo.delete_container(container_id)

    # Item methods
    async def create_item_instance(
        self,
        item_instance_id: str,
        prototype_id: str,
        owner_type: str = "room",
        owner_id: str | None = None,
        location_context: str | None = None,
        quantity: int = 1,
        condition: int | None = None,
        flags_override: list[str] | None = None,
        binding_state: str | None = None,
        attunement_state: dict[str, Any] | None = None,
        custom_name: str | None = None,
        metadata: dict[str, Any] | None = None,
        origin_source: str | None = None,
        origin_metadata: dict[str, Any] | None = None,
    ) -> None:
        """Create a new item instance. Delegates to ItemRepository."""
        return await self._item_repo.create_item_instance(
            item_instance_id,
            prototype_id,
            owner_type,
            owner_id,
            location_context,
            quantity,
            condition,
            flags_override,
            binding_state,
            attunement_state,
            custom_name,
            metadata,
            origin_source,
            origin_metadata,
        )

    async def ensure_item_instance(
        self,
        item_instance_id: str,
        prototype_id: str,
        owner_type: str = "room",
        owner_id: str | None = None,
        quantity: int = 1,
        metadata: dict[str, Any] | None = None,
        origin_source: str | None = None,
        origin_metadata: dict[str, Any] | None = None,
    ) -> None:
        """Ensure an item instance exists. Delegates to ItemRepository."""
        return await self._item_repo.ensure_item_instance(
            item_instance_id,
            prototype_id,
            owner_type,
            owner_id,
            quantity,
            metadata,
            origin_source,
            origin_metadata,
        )

    async def item_instance_exists(self, item_instance_id: str) -> bool:
        """Check if an item instance exists. Delegates to ItemRepository."""
        return await self._item_repo.item_instance_exists(item_instance_id)


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
    global _async_persistence_instance  # pylint: disable=global-statement
    if _async_persistence_instance is None:
        _async_persistence_instance = AsyncPersistenceLayer()
    return _async_persistence_instance


def reset_async_persistence() -> None:
    """
    Reset the global async persistence instance for testing.

    DEPRECATED: Use ApplicationContainer.reset_instance() instead.
    This function exists only for backward compatibility during migration.
    """
    global _async_persistence_instance  # pylint: disable=global-statement
    _async_persistence_instance = None
