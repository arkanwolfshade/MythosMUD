import os
import sqlite3
import threading
from collections.abc import Callable

from .models.player import Player
from .models.room import Room


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


# --- PersistenceLayer Singleton ---
_persistence_instance = None
_persistence_lock = threading.Lock()


def get_persistence(event_bus=None) -> "PersistenceLayer":
    global _persistence_instance
    with _persistence_lock:
        if _persistence_instance is None:
            _persistence_instance = PersistenceLayer(event_bus=event_bus)
        elif event_bus is not None and _persistence_instance._event_bus is None:
            # Update the event bus if it's not set and we have one to set
            _persistence_instance._event_bus = event_bus
        return _persistence_instance


def reset_persistence():
    """Reset the persistence singleton instance."""
    global _persistence_instance
    with _persistence_lock:
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
            raise ValueError(
                "DATABASE_URL environment variable must be set. See server/env.example for configuration template."
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
        from .logging_config import get_logger

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
            self._log(f"Room cache load failed: {e}")

    # --- CRUD for Players ---
    def get_player_by_name(self, name: str) -> Player | None:
        """Get a player by name."""
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

    def get_player(self, player_id: str) -> Player | None:
        """Get a player by ID."""
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

    def get_player_by_user_id(self, user_id: str) -> Player | None:
        """Get a player by the owning user's ID."""
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

    def save_player(self, player: Player):
        """Save or update a player."""
        with self._lock, sqlite3.connect(self.db_path) as conn:
            try:
                # Handle datetime fields that might be strings
                created_at = None
                last_active = None

                if player.created_at:
                    if isinstance(player.created_at, str):
                        created_at = player.created_at
                    else:
                        created_at = player.created_at.isoformat()

                if player.last_active:
                    if isinstance(player.last_active, str):
                        last_active = player.last_active
                    else:
                        last_active = player.last_active.isoformat()

                # Convert UUIDs to strings for SQLite compatibility
                player_id_str = str(player.player_id) if player.player_id else None
                user_id_str = str(player.user_id) if player.user_id else None

                conn.execute(
                    """
                    INSERT OR REPLACE INTO players (
                        player_id, user_id, name, stats, inventory, status_effects,
                        current_room_id, experience_points, level, is_admin, created_at, last_active
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                        created_at,
                        last_active,
                    ),
                )
                conn.commit()
                self._log(f"Saved player {player.name} ({player.player_id})")
                self._run_hooks("after_save_player", player)
            except sqlite3.IntegrityError as e:
                self._log(f"Unique constraint error saving player: {e}")
                raise UniqueConstraintError(str(e)) from e

    def list_players(self) -> list[Player]:
        """List all players."""
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

    def get_players_in_room(self, room_id: str) -> list[Player]:
        """Get all players currently in a specific room."""
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

    def save_players(self, players: list[Player]):
        """Batch save players atomically."""
        with self._lock, sqlite3.connect(self.db_path) as conn:
            try:
                for player in players:
                    # Handle datetime fields that might be strings
                    created_at = None
                    last_active = None

                    if player.created_at:
                        if isinstance(player.created_at, str):
                            created_at = player.created_at
                        else:
                            created_at = player.created_at.isoformat()

                    if player.last_active:
                        if isinstance(player.last_active, str):
                            last_active = player.last_active
                        else:
                            last_active = player.last_active.isoformat()

                    # Convert UUIDs to strings for SQLite compatibility
                    player_id_str = str(player.player_id) if player.player_id else None
                    user_id_str = str(player.user_id) if player.user_id else None

                    conn.execute(
                        """
                        INSERT OR REPLACE INTO players (
                            player_id, user_id, name, stats, inventory, status_effects,
                            current_room_id, experience_points, level, created_at, last_active
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                            created_at,
                            last_active,
                        ),
                    )
                conn.commit()
                self._log(f"Batch saved {len(players)} players.")
                self._run_hooks("after_save_players", players)
            except sqlite3.IntegrityError as e:
                self._log(f"Batch unique constraint error: {e}")
                raise UniqueConstraintError(str(e)) from e

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
                    self._log(f"Delete attempted for non-existent player: {player_id}")
                    return False

                # Delete the player (foreign key constraints will handle related data)
                cursor = conn.execute("DELETE FROM players WHERE player_id = ?", (player_id,))
                conn.commit()

                if cursor.rowcount > 0:
                    self._log(f"Successfully deleted player {player_id}")
                    self._run_hooks("after_delete_player", player_id)
                    return True
                else:
                    self._log(f"No rows affected when deleting player {player_id}")
                    return False

            except sqlite3.Error as e:
                self._log(f"Database error deleting player {player_id}: {e}")
                raise PersistenceError(f"Failed to delete player {player_id}: {e}") from e

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
        Sync a room's in-memory player state with the database.

        This ensures that the Room object's _players set reflects the actual
        players currently in that room according to the database.

        Args:
            room: The Room object to sync
            _recursion_depth: Internal parameter to prevent infinite recursion
        """
        # Prevent infinite recursion
        if _recursion_depth > 2:
            self._log(f"Preventing infinite recursion in _sync_room_players for room {room.id}")
            return

        try:
            # Get all players currently in this room from the database
            with self._lock, sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                rows = conn.execute("SELECT player_id FROM players WHERE current_room_id = ?", (room.id,)).fetchall()
                db_player_ids = {row["player_id"] for row in rows}

            # Get current in-memory player state
            memory_player_ids = set(room.get_players())

            # Add players that are in DB but not in memory
            for player_id in db_player_ids - memory_player_ids:
                # Only add if the player actually exists and is valid
                # Use a direct database query to avoid recursion
                with self._lock, sqlite3.connect(self.db_path) as conn:
                    conn.row_factory = sqlite3.Row
                    row = conn.execute("SELECT * FROM players WHERE player_id = ?", (player_id,)).fetchone()
                    if row:
                        current_room_id = row["current_room_id"]
                        if current_room_id == room.id:
                            # Use direct room state update instead of player_entered() to avoid triggering events
                            # during initial sync - events should only be triggered for actual movement
                            room._players.add(player_id)
                            self._log(
                                f"Synced player {player_id} to room {room.id} from database (direct state update)"
                            )
                        else:
                            self._log(
                                f"Skipped syncing player {player_id} to room {room.id} (in room {current_room_id})"
                            )
                    else:
                        self._log(f"Skipped syncing invalid player {player_id} to room {room.id}")

            # Don't automatically remove players that are in memory but not in DB
            # This prevents race conditions where players are removed before they're saved
            # The movement system will handle removing players when they actually move
            removed_players = memory_player_ids - db_player_ids
            if removed_players:
                self._log(
                    f"Players in memory but not in DB for room {room.id}: {removed_players} (not removing to prevent race conditions)"
                )

        except Exception as e:
            self._log(f"Error syncing room {room.id} players: {e}")
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
        if self.get_room(player.current_room_id) is not None:
            return True  # Room exists, no fix needed

        # Room doesn't exist, move player to default starting room from config
        old_room = player.current_room_id
        try:
            from .config_loader import get_config

            config = get_config()
            default_room = config.get("default_player_room", "earth_arkham_city_northside_intersection_derby_high")
            if default_room is None:
                default_room = "earth_arkham_city_northside_intersection_derby_high"
        except Exception:
            # Fallback to hardcoded default if config loading fails
            default_room = "earth_arkham_city_northside_intersection_derby_high"

        player.current_room_id = default_room

        self._log(f"Player {player.name} was in invalid room '{old_room}', moved to default room '{default_room}'")
        return True

    # --- TODO: Add async support, other backends, migrations, etc. ---
