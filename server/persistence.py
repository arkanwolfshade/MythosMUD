import os
import sqlite3
import threading
from collections.abc import Callable
from typing import TYPE_CHECKING
from uuid import UUID

from server.logging.enhanced_logging_config import get_logger

from .exceptions import DatabaseError, ValidationError
from .models.player import Player
from .models.room import Room
from .utils.error_logging import create_error_context, log_and_raise
from .world_loader import ROOMS_BASE_PATH

if TYPE_CHECKING:
    from .models.profession import Profession

logger = get_logger(__name__)


# --- Custom Exceptions ---
# Note: These are kept for backward compatibility
# New code should use the comprehensive exception system in exceptions.py
class PersistenceError(Exception):
    pass


class UniqueConstraintError(PersistenceError):
    pass


# --- Hook Decorator ---
def register_hook(event: str):
    """Decorator to register a hook for a given event."""

    def decorator(func):
        PersistenceLayer._register_hook(event, func)
        return func

    return decorator


# DEPRECATED: Module-level global singleton removed - use ApplicationContainer instead
# Keeping these functions for backward compatibility during migration
_persistence_instance = None
_persistence_lock = threading.Lock()


def get_persistence(event_bus=None) -> "PersistenceLayer":
    """
    Get persistence layer instance.

    DEPRECATED: Use ApplicationContainer.persistence instead.
    This function exists only for backward compatibility during migration.

    Args:
        event_bus: Optional EventBus instance

    Returns:
        PersistenceLayer: The persistence layer instance
    """
    global _persistence_instance
    with _persistence_lock:
        if _persistence_instance is None:
            _persistence_instance = PersistenceLayer(event_bus=event_bus)
        elif event_bus is not None and _persistence_instance._event_bus is None:  # type: ignore[unreachable]
            # Update the event bus if it's not set and we have one to set
            _persistence_instance._event_bus = event_bus
        return _persistence_instance


def reset_persistence():
    """
    Reset the persistence singleton instance.

    DEPRECATED: Use ApplicationContainer.reset_instance() instead.
    This function exists only for backward compatibility during migration.
    """
    global _persistence_instance
    with _persistence_lock:
        if _persistence_instance is not None:
            # Force immediate shutdown of EventBus to prevent async task interference
            if _persistence_instance._event_bus is not None:
                try:
                    # Force shutdown without waiting for async cleanup
                    _persistence_instance._event_bus._running = False
                    _persistence_instance._event_bus._shutdown_event.set()
                    # Clear active tasks immediately
                    _persistence_instance._event_bus._active_tasks.clear()
                except (AttributeError, RuntimeError) as e:
                    logger.warning("Error during event bus cleanup", error=str(e), error_type=type(e).__name__)
                    # Any error during cleanup - just proceed with reset
                    pass
        _persistence_instance = None


# --- PersistenceLayer Class ---
class PersistenceLayer:
    """
    Unified persistence layer for all game data (players, rooms, inventory, etc.).
    Thread-safe, supports hooks, context management, and batch operations.
    """

    _hooks: dict[str, list[Callable]] = {}

    def __init__(self, db_path: str | None = None, log_path: str | None = None, event_bus=None):
        # Use environment variable for database path - require it to be set
        if db_path:
            self.db_path = db_path
        elif os.environ.get("DATABASE_URL"):
            # Derive database path from DATABASE_URL
            from .database import get_database_path

            self.db_path = str(get_database_path())
        else:
            context = create_error_context()
            context.metadata["operation"] = "persistence_init"
            log_and_raise(
                ValidationError,
                "DATABASE_URL environment variable must be set",
                context=context,
                details={"config_file": "server/env.example"},
                user_friendly="Database configuration is missing",
            )

        # Logging is now handled by the centralized logging system
        # The log_path parameter is kept for backward compatibility but not used
        self.log_path = None  # No longer needed with centralized logging

        self._lock = threading.RLock()
        self._logger = self._setup_logger()
        self._event_bus = event_bus
        # TODO: Load config for SQL logging verbosity
        self._load_room_cache()

    def _setup_logger(self):
        # Use centralized logging configuration
        from .logging.enhanced_logging_config import get_logger

        return get_logger("PersistenceLayer")

    def _log(self, msg: str):
        self._logger.info(msg)

    def _convert_row_to_player_data(self, row: sqlite3.Row) -> dict:
        """
        Convert SQLite row data to proper types for Player constructor.

        Args:
            row: SQLite Row object from query result

        Returns:
            dict: Data with proper types for Player constructor
        """
        data = dict(row)

        # Convert string UUIDs back to UUID objects
        if data.get("player_id"):
            try:
                data["player_id"] = str(data["player_id"])
            except (ValueError, TypeError):
                self._log(f"Invalid player_id format: {data['player_id']}")
                data["player_id"] = None

        if data.get("user_id"):
            try:
                data["user_id"] = str(data["user_id"])
            except (ValueError, TypeError):
                self._log(f"Invalid user_id format: {data['user_id']}")
                data["user_id"] = None

        # Convert is_admin from integer to boolean
        if "is_admin" in data:
            data["is_admin"] = bool(data["is_admin"])

        # Convert datetime strings back to datetime objects if needed
        # (Player model handles this internally, but we could add explicit conversion here)

        return data

    # --- Context Management ---
    def __enter__(self):
        self._lock.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lock.release()

    # --- Hook Registration ---
    @classmethod
    def _register_hook(cls, event: str, func: Callable):
        if event not in cls._hooks:
            cls._hooks[event] = []
        cls._hooks[event].append(func)

    def _run_hooks(self, event: str, *args, **kwargs):
        for func in self._hooks.get(event, []):
            func(*args, **kwargs)
        # TODO: Support async hooks in the future

    # --- Room Cache (Loaded at Startup) ---
    def _load_room_cache(self):
        """Load rooms from JSON files using world_loader and convert to Room objects."""
        self._room_cache = {}
        self._room_mappings = {}
        try:
            # Use the world_loader to load the full world data including room mappings
            from .world_loader import load_hierarchical_world

            world_data = load_hierarchical_world()
            room_data = world_data["rooms"]
            self._room_mappings = world_data["room_mappings"]

            # Convert dictionary data to Room objects
            for room_id, room_data_dict in room_data.items():
                self._room_cache[room_id] = Room(room_data_dict, self._event_bus)

            self._log(f"Loaded {len(self._room_cache)} rooms into cache from JSON files.")
            self._log(f"Loaded {len(self._room_mappings)} room mappings for backward compatibility.")
        except Exception as e:
            context = create_error_context()
            context.metadata["operation"] = "load_room_cache"
            context.metadata["rooms_base_path"] = ROOMS_BASE_PATH
            log_and_raise(
                DatabaseError,
                f"Room cache load failed: {e}",
                context=context,
                details={"rooms_base_path": ROOMS_BASE_PATH, "error": str(e)},
                user_friendly="Failed to load world data",
            )

    # --- CRUD for Players ---
    def get_player_by_name(self, name: str) -> Player | None:
        """Get a player by name."""
        context = create_error_context()
        context.metadata["operation"] = "get_player_by_name"
        context.metadata["player_name"] = name

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                row = conn.execute("SELECT * FROM players WHERE name = ?", (name,)).fetchone()
                if row:
                    player_data = self._convert_row_to_player_data(row)
                    player = Player(**player_data)
                    # Validate and fix room placement if needed
                    self.validate_and_fix_player_room(player)
                    return player
                return None
        except sqlite3.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by name '{name}': {e}",
                context=context,
                details={"player_name": name, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )
            return None  # type: ignore[unreachable]  # Defensive return after NoReturn

    def get_player(self, player_id: str) -> Player | None:
        """Get a player by ID."""
        context = create_error_context()
        context.metadata["operation"] = "get_player"
        context.metadata["player_id"] = player_id

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                # Convert player_id to string to ensure SQLite compatibility
                player_id_str = str(player_id) if player_id else None
                row = conn.execute("SELECT * FROM players WHERE player_id = ?", (player_id_str,)).fetchone()
                if row:
                    player_data = self._convert_row_to_player_data(row)
                    player = Player(**player_data)
                    # Validate and fix room placement if needed
                    self.validate_and_fix_player_room(player)
                    return player
                return None
        except sqlite3.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by ID '{player_id}': {e}",
                context=context,
                details={"player_id": player_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )
            return None  # type: ignore[unreachable]  # Defensive return after NoReturn

    def get_player_by_user_id(self, user_id: str) -> Player | None:
        """Get a player by the owning user's ID."""
        context = create_error_context()
        context.metadata["operation"] = "get_player_by_user_id"
        context.metadata["user_id"] = user_id

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                # Convert user_id to string to ensure SQLite compatibility
                user_id_str = str(user_id) if user_id else None
                row = conn.execute("SELECT * FROM players WHERE user_id = ?", (user_id_str,)).fetchone()
                if row:
                    player_data = self._convert_row_to_player_data(row)
                    player = Player(**player_data)
                    # Validate and fix room placement if needed
                    self.validate_and_fix_player_room(player)
                    return player
                return None
        except sqlite3.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving player by user ID '{user_id}': {e}",
                context=context,
                details={"user_id": user_id, "error": str(e)},
                user_friendly="Failed to retrieve player information",
            )
            return None  # type: ignore[unreachable]  # Defensive return after NoReturn

    def save_player(self, player: Player):
        """Save or update a player."""
        context = create_error_context()
        context.metadata["operation"] = "save_player"
        context.metadata["player_name"] = player.name
        context.metadata["player_id"] = str(player.player_id)

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                try:
                    # Handle datetime fields that might be strings
                    created_at = None
                    last_active = None

                    if player.created_at:
                        if isinstance(player.created_at, str):  # type: ignore[unreachable]
                            created_at = player.created_at  # type: ignore[unreachable]
                        else:
                            created_at = player.created_at.isoformat()

                    if player.last_active:
                        if isinstance(player.last_active, str):  # type: ignore[unreachable]
                            last_active = player.last_active  # type: ignore[unreachable]
                        else:
                            last_active = player.last_active.isoformat()

                    # Convert UUIDs to strings for SQLite compatibility
                    player_id_str = str(player.player_id) if player.player_id else None
                    user_id_str = str(player.user_id) if player.user_id else None

                    conn.execute(
                        """
                        INSERT OR REPLACE INTO players (
                            player_id, user_id, name, stats, inventory, status_effects,
                            current_room_id, experience_points, level, is_admin, profession_id, created_at, last_active
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            player_id_str,
                            user_id_str,
                            player.name,
                            player.stats,
                            player.inventory,
                            player.status_effects,
                            player.current_room_id,
                            player.experience_points,
                            player.level,
                            player.is_admin,
                            player.profession_id,
                            created_at,
                            last_active,
                        ),
                    )
                    conn.commit()
                    self._log(f"Saved player {player.name}")
                    self._run_hooks("after_save_player", player)
                except sqlite3.IntegrityError as e:
                    log_and_raise(
                        DatabaseError,
                        f"Unique constraint error saving player: {e}",
                        context=context,
                        details={"player_name": player.name, "player_id": str(player.player_id), "error": str(e)},
                        user_friendly="Player name already exists",
                    )
                except sqlite3.Error as e:
                    log_and_raise(
                        DatabaseError,
                        f"Database error saving player: {e}",
                        context=context,
                        details={"player_name": player.name, "player_id": str(player.player_id), "error": str(e)},
                        user_friendly="Failed to save player",
                    )
        except OSError as e:
            log_and_raise(
                DatabaseError,
                f"File system error saving player: {e}",
                context=context,
                details={"player_name": player.name, "player_id": str(player.player_id), "error": str(e)},
                user_friendly="Failed to save player - file system error",
            )
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Unexpected error saving player: {e}",
                context=context,
                details={"player_name": player.name, "player_id": str(player.player_id), "error": str(e)},
                user_friendly="Failed to save player",
            )

    def list_players(self) -> list[Player]:
        """List all players."""
        context = create_error_context()
        context.metadata["operation"] = "list_players"

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                rows = conn.execute("SELECT * FROM players").fetchall()
                players = []
                for row in rows:
                    player_data = self._convert_row_to_player_data(row)
                    player = Player(**player_data)
                    # Validate and fix room placement if needed
                    self.validate_and_fix_player_room(player)
                    players.append(player)
                return players
        except sqlite3.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error listing players: {e}",
                context=context,
                details={"error": str(e)},
                user_friendly="Failed to retrieve player list",
            )
            return []  # type: ignore[unreachable]  # Defensive return after NoReturn

    def get_players_in_room(self, room_id: str) -> list[Player]:
        """Get all players currently in a specific room."""
        context = create_error_context()
        context.metadata["operation"] = "get_players_in_room"
        context.metadata["room_id"] = room_id

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                rows = conn.execute("SELECT * FROM players WHERE current_room_id = ?", (room_id,)).fetchall()
                players = []
                for row in rows:
                    player_data = self._convert_row_to_player_data(row)
                    player = Player(**player_data)
                    # Validate and fix room placement if needed
                    self.validate_and_fix_player_room(player)
                    players.append(player)
                return players
        except sqlite3.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving players in room '{room_id}': {e}",
                context=context,
                details={"room_id": room_id, "error": str(e)},
                user_friendly="Failed to retrieve players in room",
            )
            return []  # type: ignore[unreachable]  # Defensive return after NoReturn

    def save_players(self, players: list[Player]):
        """Batch save players atomically."""
        context = create_error_context()
        context.metadata["operation"] = "save_players"
        context.metadata["player_count"] = len(players)

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                try:
                    for player in players:
                        # Handle datetime fields that might be strings
                        created_at = None
                        last_active = None

                        if player.created_at:
                            if isinstance(player.created_at, str):  # type: ignore[unreachable]
                                created_at = player.created_at  # type: ignore[unreachable]
                            else:
                                created_at = player.created_at.isoformat()

                        if player.last_active:
                            if isinstance(player.last_active, str):  # type: ignore[unreachable]
                                last_active = player.last_active  # type: ignore[unreachable]
                            else:
                                last_active = player.last_active.isoformat()

                        # Convert UUIDs to strings for SQLite compatibility
                        player_id_str = str(player.player_id) if player.player_id else None
                        user_id_str = str(player.user_id) if player.user_id else None

                        conn.execute(
                            """
                            INSERT OR REPLACE INTO players (
                                player_id, user_id, name, stats, inventory, status_effects,
                                current_room_id, experience_points, level, is_admin, profession_id, created_at, last_active
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (
                                player_id_str,
                                user_id_str,
                                player.name,
                                player.stats,
                                player.inventory,
                                player.status_effects,
                                player.current_room_id,
                                player.experience_points,
                                player.level,
                                player.is_admin,
                                player.profession_id,
                                created_at,
                                last_active,
                            ),
                        )
                    conn.commit()
                    self._log(f"Batch saved {len(players)} players.")
                    self._run_hooks("after_save_players", players)
                except sqlite3.IntegrityError as e:
                    log_and_raise(
                        DatabaseError,
                        f"Batch unique constraint error: {e}",
                        context=context,
                        details={"player_count": len(players), "error": str(e)},
                        user_friendly="Failed to save players - duplicate data",
                    )
                except sqlite3.Error as e:
                    log_and_raise(
                        DatabaseError,
                        f"Database error in batch save: {e}",
                        context=context,
                        details={"player_count": len(players), "error": str(e)},
                        user_friendly="Failed to save players",
                    )
        except Exception as e:
            log_and_raise(
                DatabaseError,
                f"Unexpected error in batch save: {e}",
                context=context,
                details={"player_count": len(players), "error": str(e)},
                user_friendly="Failed to save players",
            )

    def delete_player(self, player_id: str) -> bool:
        """
        Delete a player from the database.

        Args:
            player_id: The unique identifier of the player to delete

        Returns:
            bool: True if player was deleted, False if player didn't exist

        Raises:
            PersistenceError: If deletion fails due to database constraints or errors
        """
        with self._lock, sqlite3.connect(self.db_path) as conn:
            try:
                # First check if player exists
                cursor = conn.execute("SELECT player_id FROM players WHERE player_id = ?", (player_id,))
                if not cursor.fetchone():
                    self._log("Delete attempted for non-existent player")
                    return False

                # Delete the player (foreign key constraints will handle related data)
                cursor = conn.execute("DELETE FROM players WHERE player_id = ?", (player_id,))
                conn.commit()

                if cursor.rowcount > 0:
                    self._log("Successfully deleted player")
                    self._run_hooks("after_delete_player", player_id)
                    return True
                else:
                    self._log("No rows affected when deleting player")
                    return False

            except sqlite3.Error as e:
                context = create_error_context()
                context.metadata["operation"] = "delete_player"
                context.metadata["player_id"] = player_id
                log_and_raise(
                    DatabaseError,
                    f"Database error deleting player {player_id}: {e}",
                    context=context,
                    details={"player_id": player_id, "error": str(e)},
                    user_friendly="Failed to delete player",
                )
                return False  # type: ignore[unreachable]  # Defensive return after NoReturn

    # --- CRUD for Professions ---
    def get_all_professions(self) -> list:
        """Get all available professions."""
        context = create_error_context()
        context.metadata["operation"] = "get_all_professions"

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                rows = conn.execute("SELECT * FROM professions WHERE is_available = 1 ORDER BY id").fetchall()

                professions = []
                for row in rows:
                    profession_data = dict(row)
                    # Import here to avoid circular imports
                    from .models.profession import Profession

                    profession = Profession(**profession_data)
                    professions.append(profession)

                return professions
        except sqlite3.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving professions: {e}",
                context=context,
                details={"error": str(e)},
                user_friendly="Failed to retrieve professions",
            )
            return []  # type: ignore[unreachable]  # Defensive return after NoReturn

    def get_profession_by_id(self, profession_id: int) -> "Profession | None":
        """Get a profession by ID."""
        context = create_error_context()
        context.metadata["operation"] = "get_profession_by_id"
        context.metadata["profession_id"] = profession_id

        try:
            with self._lock, sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                row = conn.execute("SELECT * FROM professions WHERE id = ?", (profession_id,)).fetchone()

                if row:
                    profession_data = dict(row)
                    # Import here to avoid circular imports
                    from .models.profession import Profession

                    profession = Profession(**profession_data)
                    return profession
                return None
        except sqlite3.Error as e:
            log_and_raise(
                DatabaseError,
                f"Database error retrieving profession {profession_id}: {e}",
                context=context,
                details={"profession_id": profession_id, "error": str(e)},
                user_friendly="Failed to retrieve profession",
            )
            return None  # type: ignore[unreachable]  # Defensive return after NoReturn

    # --- CRUD for Rooms ---
    def get_room(self, room_id: str) -> Room | None:
        """Get a room by ID from the cache and sync with database state."""
        # First try direct lookup
        room = None
        if room_id in self._room_cache:
            room = self._room_cache[room_id]
        elif room_id in self._room_mappings:
            # If not found, check if it's an old ID that maps to a new one
            new_room_id = self._room_mappings[room_id]
            room = self._room_cache.get(new_room_id)

        if room:
            # Sync the room's player state with the database
            self._sync_room_players(room)
            return room

        return None

    def _sync_room_players(self, room: Room, _recursion_depth: int = 0) -> None:
        """
        Clear any ghost players from the room's in-memory state.

        Players should only be in rooms when they're actively connected to the game.
        The database current_room_id is just where the player was last located,
        not where they currently are. This method ensures rooms start clean.

        Args:
            room: The Room object to sync
            _recursion_depth: Internal parameter to prevent infinite recursion
        """
        # Prevent infinite recursion
        if _recursion_depth > 2:
            self._log(f"Preventing infinite recursion in _sync_room_players for room {room.id}")
            return

        try:
            # Get current in-memory player state
            memory_player_ids = set(room.get_players())

            # CRITICAL FIX: Only remove players that are no longer in the database
            # Players should only be added to rooms when they actually connect to the game
            # But we should not clear all players - only remove those that are truly ghost players
            if memory_player_ids:
                # Log player count without exposing GUIDs to prevent infinite loops with PlayerGuidFormatter
                self._log(f"Room {room.id} has {len(memory_player_ids)} players in memory")
                # Note: We don't clear the room's players here because they are added when players connect
                # The room's _players set should only be modified when players actually enter/leave

        except Exception as e:
            context = create_error_context()
            context.metadata["operation"] = "sync_room_players"
            context.metadata["room_id"] = room.id
            context.metadata["recursion_depth"] = _recursion_depth
            # Log as warning since this is a non-critical operation
            self._logger.warning(
                "Error syncing room players",
                context=context.to_dict(),
                error=str(e),
                error_type=type(e).__name__,
            )
            # Don't raise the exception - we want to continue even if sync fails

    def save_room(self, room: Room):
        """Save or update a room. Currently read-only - rooms are stored as JSON files."""
        # TODO: Implement JSON file saving for rooms
        # For now, just update the cache
        self._room_cache[room.id] = room
        self._log(f"Updated room {room.id} in cache (JSON file saving not implemented)")
        self._run_hooks("after_save_room", room)

    def list_rooms(self) -> list[Room]:
        """List all rooms from the cache."""
        return list(self._room_cache.values())

    def save_rooms(self, rooms: list[Room]):
        """Batch save rooms. Currently read-only - rooms are stored as JSON files."""
        # TODO: Implement JSON file saving for rooms
        # For now, just update the cache
        for room in rooms:
            self._room_cache[room.id] = room
        self._log(f"Updated {len(rooms)} rooms in cache (JSON file saving not implemented)")
        self._run_hooks("after_save_rooms", rooms)

    # --- Player Health Management Methods ---

    def damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
        """
        Damage a player and persist health changes to the database.

        PHASE 2A OPTIMIZATION: Uses atomic field update to prevent race conditions.

        Args:
            player: The player object to damage
            amount: Amount of damage to apply
            damage_type: Type of damage (for future extension)

        Raises:
            ValueError: If damage amount is invalid
            DatabaseError: If database save fails

        Note:
            Uses atomic database update for ONLY current_health field.
            This prevents race conditions where other systems (e.g., XP awards)
            overwrite health changes with stale cached player data.
        """
        try:
            if amount < 0:
                raise ValueError(f"Damage amount must be positive, got {amount}")

            # Get current stats from in-memory player object
            stats = player.get_stats()
            current_health = stats.get("current_health", 100)
            new_health = max(0, current_health - amount)

            # Update the in-memory player object (for immediate UI feedback)
            stats["current_health"] = new_health
            player.set_stats(stats)

            # CRITICAL: Use atomic field update instead of save_player()
            # This prevents race conditions with other systems updating the same player
            self.update_player_health(str(player.player_id), -amount, f"damage:{damage_type}")

            self._logger.info(
                "Player health reduced atomically",
                player_id=str(player.player_id),
                player_name=player.name,
                damage=amount,
                old_health=current_health,
                new_health=new_health,
                damage_type=damage_type,
            )
        except ValueError as e:
            self._logger.error(
                "Invalid damage amount",
                player_id=str(player.player_id),
                amount=amount,
                error=str(e),
                exc_info=True,
            )
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to persist player damage",
                player_id=str(player.player_id),
                player_name=player.name,
                amount=amount,
                damage_type=damage_type,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise

    def heal_player(self, player: Player, amount: int) -> None:
        """
        Heal a player and persist health changes to the database.

        PHASE 2A OPTIMIZATION: Uses atomic field update to prevent race conditions.

        Args:
            player: The player object to heal
            amount: Amount of healing to apply

        Raises:
            ValueError: If healing amount is invalid
            DatabaseError: If database save fails

        Note:
            Uses atomic database update for ONLY current_health field.
            This prevents race conditions with other systems updating the same player.
        """
        try:
            if amount < 0:
                raise ValueError(f"Healing amount must be positive, got {amount}")

            # Get current stats from in-memory player object
            stats = player.get_stats()
            current_health = stats.get("current_health", 100)
            max_health = 100  # TODO: Make this configurable or player-specific
            new_health = min(max_health, current_health + amount)

            # Update the in-memory player object (for immediate UI feedback)
            stats["current_health"] = new_health
            player.set_stats(stats)

            # CRITICAL: Use atomic field update instead of save_player()
            self.update_player_health(str(player.player_id), amount, "healing")

            self._logger.info(
                "Player health increased atomically",
                player_id=str(player.player_id),
                player_name=player.name,
                healing=amount,
                old_health=current_health,
                new_health=new_health,
            )
        except ValueError as e:
            self._logger.error(
                "Invalid healing amount",
                player_id=str(player.player_id),
                amount=amount,
                error=str(e),
                exc_info=True,
            )
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to persist player healing",
                player_id=str(player.player_id),
                player_name=player.name,
                amount=amount,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise

    async def async_damage_player(self, player: Player, amount: int, damage_type: str = "physical") -> None:
        """
        Async wrapper for damage_player to support async contexts.

        CRITICAL FIX: This method was missing, causing async damage calls to fail.

        Args:
            player: The player object to damage
            amount: Amount of damage to apply
            damage_type: Type of damage

        Note:
            Currently delegates to synchronous method since SQLite operations
            are blocking. Future enhancement: use asyncio.to_thread() for
            true async when migrating to PostgreSQL or other async databases.
        """
        # Since the underlying operations are synchronous (SQLite),
        # we call the sync version directly
        # Future: Could use asyncio.to_thread(self.damage_player, player, amount, damage_type)
        self.damage_player(player, amount, damage_type)

    async def async_heal_player(self, player: Player, amount: int) -> None:
        """
        Async wrapper for heal_player to support async contexts.

        CRITICAL FIX: This method was missing, causing async heal calls to fail.

        Args:
            player: The player object to heal
            amount: Amount of healing to apply

        Note:
            Currently delegates to synchronous method since SQLite operations
            are blocking. Future enhancement: use asyncio.to_thread() for
            true async when migrating to PostgreSQL or other async databases.
        """
        # Since the underlying operations are synchronous (SQLite),
        # we call the sync version directly
        # Future: Could use asyncio.to_thread(self.heal_player, player, amount)
        self.heal_player(player, amount)

    def gain_experience(self, player: Player, amount: int, source: str = "unknown") -> None:
        """
        Award experience points to a player and persist to database.

        PHASE 2A OPTIMIZATION: Uses atomic field update to prevent race conditions.

        Args:
            player: The player object to award XP to
            amount: Amount of XP to award (must be non-negative)
            source: Source of the XP for logging purposes

        Raises:
            ValueError: If amount is negative
            DatabaseError: If database operation fails

        Note:
            Uses atomic database update for ONLY experience_points field.
            This prevents race conditions where XP awards overwrite health changes
            by loading and saving stale cached player data.
        """
        try:
            if amount < 0:
                raise ValueError(f"Experience amount must be non-negative, got {amount}")

            # Get current stats from in-memory player object
            stats = player.get_stats()
            old_xp = stats.get("experience_points", 0)
            new_xp = old_xp + amount

            # Update the in-memory player object (for immediate UI feedback)
            stats["experience_points"] = new_xp
            player.set_stats(stats)

            # CRITICAL: Use atomic field update instead of save_player()
            # This prevents overwriting health or other fields with stale cached values
            self.update_player_xp(str(player.player_id), amount, source)

            self._logger.info(
                "Player experience increased atomically",
                player_id=str(player.player_id),
                player_name=player.name,
                xp_gained=amount,
                old_xp=old_xp,
                new_xp=new_xp,
                source=source,
            )

        except ValueError as e:
            self._logger.error(
                "Invalid experience amount",
                player_id=str(player.player_id),
                amount=amount,
                error=str(e),
                exc_info=True,
            )
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to persist player experience gain",
                player_id=str(player.player_id),
                player_name=player.name,
                amount=amount,
                source=source,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise

    async def async_gain_experience(self, player: Player, amount: int, source: str = "unknown") -> None:
        """
        Async wrapper for gain_experience to support async contexts.

        Args:
            player: The player object to award XP to
            amount: Amount of XP to award
            source: Source of the XP for logging purposes

        Note:
            Currently delegates to synchronous method since SQLite operations
            are blocking. Future enhancement: use asyncio.to_thread() for
            true async when migrating to PostgreSQL or other async databases.
        """
        # Since the underlying operations are synchronous (SQLite),
        # we call the sync version directly
        # Future: Could use asyncio.to_thread(self.gain_experience, player, amount, source)
        self.gain_experience(player, amount, source)

    def update_player_stat_field(
        self, player_id: str | UUID, field_name: str, delta: int | float, reason: str = ""
    ) -> None:
        """
        Update a specific numeric field in player stats using atomic database operation.

        CRITICAL FIX: This method prevents race conditions by updating only the specified
        field in the database without loading/saving the entire player object.

        This is the ONLY safe way to update stats when multiple systems may be modifying
        the same player simultaneously (e.g., combat damage + XP awards).

        Args:
            player_id: Player's unique ID (string or UUID)
            field_name: Name of the stat field to update (e.g., "current_health", "experience_points")
            delta: Amount to add (positive) or subtract (negative) from the field
            reason: Reason for the update (for logging)

        Raises:
            ValueError: If field_name is invalid or delta would result in negative values
            DatabaseError: If database operation fails

        Example:
            # Reduce health by 20 (combat damage)
            persistence.update_player_stat_field(player_id, "current_health", -20, "combat_damage")

            # Increase XP by 100
            persistence.update_player_stat_field(player_id, "experience_points", 100, "killed_npc")

        Note:
            Uses SQLite's json_set() function for atomic field updates.
            Invalidates player cache to ensure fresh data on next get_player().
        """
        try:
            # Convert UUID to string if needed
            player_id_str = str(player_id)

            # Validate field name (whitelist approach for security)
            allowed_fields = {
                "current_health",
                "experience_points",
                "sanity",
                "occult_knowledge",
                "fear",
                "corruption",
                "cult_affiliation",
                "strength",
                "dexterity",
                "constitution",
                "intelligence",
                "wisdom",
                "charisma",
            }
            if field_name not in allowed_fields:
                raise ValueError(f"Invalid stat field name: {field_name}. Must be one of {allowed_fields}")

            # Execute atomic field update using SQLite json_set()
            # AI Agent: This prevents race conditions by updating ONLY this field
            # without loading/saving the entire player object which might have stale data
            with self._lock, sqlite3.connect(self.db_path) as conn:
                cursor = conn.execute(
                    f"""
                    UPDATE players
                    SET stats = json_set(
                        stats,
                        '$.{field_name}',
                        CAST(json_extract(stats, '$.{field_name}') + ? AS INTEGER)
                    )
                    WHERE player_id = ?
                    """,
                    (delta, player_id_str),
                )

                if cursor.rowcount == 0:
                    raise ValueError(f"Player {player_id_str} not found")

                conn.commit()

            # AI Agent: No cache invalidation needed - atomic field updates bypass cache entirely
            # This prevents the race condition where XP awards overwrite combat damage

            self._logger.info(
                "Player stat field updated atomically",
                player_id=player_id_str,
                field_name=field_name,
                delta=delta,
                reason=reason,
            )

        except ValueError as e:
            self._logger.error(
                "Invalid stat field update",
                player_id=str(player_id),
                field_name=field_name,
                delta=delta,
                error=str(e),
                exc_info=True,
            )
            raise
        except Exception as e:
            self._logger.critical(
                "CRITICAL: Failed to update player stat field",
                player_id=str(player_id),
                field_name=field_name,
                delta=delta,
                reason=reason,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            raise

    def update_player_health(self, player_id: str | UUID, delta: int, reason: str = "") -> None:
        """
        Update player health using atomic database operation.

        CRITICAL FIX: Prevents race conditions where health changes are overwritten
        by other systems (e.g., XP awards) saving stale player data.

        Args:
            player_id: Player's unique ID
            delta: Amount to change health (negative for damage, positive for healing)
            reason: Reason for health change (for logging)

        Example:
            # Combat damage
            update_player_health(player_id, -20, "attacked_by_nightgaunt")

            # Healing
            update_player_health(player_id, 30, "health_potion")
        """
        self.update_player_stat_field(player_id, "current_health", delta, reason)

    def update_player_xp(self, player_id: str | UUID, delta: int, reason: str = "") -> None:
        """
        Update player experience points using atomic database operation.

        CRITICAL FIX: Prevents race conditions where XP awards overwrite health changes
        by loading stale player data from cache.

        Args:
            player_id: Player's unique ID
            delta: Amount of XP to award (must be positive)
            reason: Reason for XP award (for logging)

        Example:
            update_player_xp(player_id, 100, "killed_nightgaunt")
        """
        if delta < 0:
            raise ValueError(f"XP delta must be non-negative, got {delta}")
        self.update_player_stat_field(player_id, "experience_points", delta, reason)

    # --- TODO: Inventory, status effects, etc. ---
    # def get_inventory(self, ...): ...
    # def save_inventory(self, ...): ...
    # def list_inventory(self, ...): ...

    def validate_and_fix_player_room(self, player: Player) -> bool:
        """
        Validate that a player's current room exists, and fix if necessary.

        Args:
            player: The player to validate

        Returns:
            True if the room was valid or successfully fixed, False otherwise
        """
        # Check if the player's current room exists
        if self.get_room(str(player.current_room_id)) is not None:
            return True  # Room exists, no fix needed

        # Room doesn't exist, move player to default starting room from config
        old_room = player.current_room_id
        try:
            from .config import get_config

            config = get_config()
            default_room = config.game.default_player_room
        except Exception as e:
            # Fallback to hardcoded default if config loading fails
            context = create_error_context()
            context.metadata["operation"] = "validate_and_fix_player_room"
            context.metadata["player_name"] = player.name
            context.metadata["old_room_id"] = old_room
            self._logger.warning(
                "Config loading failed during room validation, using fallback",
                context=context.to_dict(),
                error=str(e),
                error_type=type(e).__name__,
            )
            default_room = "earth_arkhamcity_sanitarium_room_foyer_001"

        player.current_room_id = default_room  # type: ignore[assignment]

        self._log(f"Player {player.name} was in invalid room '{old_room}', moved to default room '{default_room}'")
        return True

    # --- Async Methods ---
    # These methods now delegate to the true async persistence layer
    # This provides real async database operations without blocking the event loop

    async def async_get_player_by_name(self, name: str) -> Player | None:
        """Get a player by name using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.get_player_by_name(name)

    async def async_get_player(self, player_id: str) -> Player | None:
        """Get a player by ID using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.get_player_by_id(player_id)

    async def async_get_player_by_user_id(self, user_id: str) -> Player | None:
        """Get a player by user ID using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.get_player_by_user_id(user_id)

    async def async_save_player(self, player: Player):
        """Save a player using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.save_player(player)

    async def async_list_players(self) -> list[Player]:
        """List all players using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.list_players()

    async def async_get_players_in_room(self, room_id: str) -> list[Player]:
        """Get all players in a room using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.get_players_in_room(room_id)

    async def async_save_players(self, players: list[Player]):
        """Save multiple players using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.save_players(players)

    async def async_delete_player(self, player_id: str) -> bool:
        """Delete a player using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.delete_player(player_id)

    async def async_get_all_professions(self) -> list:
        """Get all professions using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.get_professions()

    async def async_get_profession_by_id(self, profession_id: int) -> object | None:
        """Get a profession by ID using async database operations."""
        from .async_persistence import get_async_persistence

        async_persistence = get_async_persistence()
        return await async_persistence.get_profession_by_id(profession_id)

    async def async_get_room(self, room_id: str) -> Room | None:
        """Get a room by ID using async database operations."""
        # Rooms are still handled by the sync layer for now
        return self.get_room(room_id)

    async def async_save_room(self, room: Room):
        """Save a room using async database operations."""
        # Rooms are still handled by the sync layer for now
        return self.save_room(room)

    async def async_list_rooms(self) -> list[Room]:
        """List all rooms using async database operations."""
        # Rooms are still handled by the sync layer for now
        return self.list_rooms()

    async def async_save_rooms(self, rooms: list[Room]):
        """Save multiple rooms using async database operations."""
        # Rooms are still handled by the sync layer for now
        return self.save_rooms(rooms)

    def get_npc_lifecycle_manager(self):
        """
        Get the NPC lifecycle manager from app.state.

        Returns:
            NPCLifecycleManager: The NPC lifecycle manager instance, or None if not available
        """
        try:
            from server.main import app

            lifecycle_manager = getattr(app.state, "npc_lifecycle_manager", None)
            logger.debug(
                "get_npc_lifecycle_manager called",
                has_app=bool(app),
                has_state=bool(getattr(app, "state", None)),
                has_lifecycle_manager=bool(lifecycle_manager),
            )
            return lifecycle_manager
        except Exception as e:
            logger.debug("get_npc_lifecycle_manager failed", error=str(e))
            return None

    # --- TODO: Add async support, other backends, migrations, etc. ---
