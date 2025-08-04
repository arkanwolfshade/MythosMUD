import os
import sqlite3
import threading
from collections.abc import Callable
from typing import Any

from .models import Player  # Assume Room model exists or will be added


# --- Custom Exceptions ---
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


def get_persistence() -> "PersistenceLayer":
    global _persistence_instance
    with _persistence_lock:
        if _persistence_instance is None:
            _persistence_instance = PersistenceLayer()
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

    def __init__(self, db_path: str | None = None, log_path: str | None = None):
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

        # Use environment variable for log path - require it to be set
        if log_path:
            self.log_path = log_path
        elif os.environ.get("PERSIST_LOG"):
            self.log_path = os.environ.get("PERSIST_LOG")
        else:
            raise ValueError(
                "PERSIST_LOG environment variable must be set. See server/env.example for configuration template."
            )

        self._lock = threading.RLock()
        self._logger = self._setup_logger()
        # TODO: Load config for SQL logging verbosity
        self._load_room_cache()

    def _setup_logger(self):
        # Use centralized logging configuration
        from .logging_config import get_logger

        return get_logger("PersistenceLayer")

    def _log(self, msg: str):
        self._logger.info(msg)

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
        """Load rooms from JSON files using world_loader instead of SQLite."""
        self._room_cache = {}
        self._room_mappings = {}
        try:
            # Use the world_loader to load the full world data including room mappings
            from .world_loader import load_hierarchical_world

            world_data = load_hierarchical_world()
            self._room_cache = world_data["rooms"]
            self._room_mappings = world_data["room_mappings"]
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
                return Player(**dict(row))
            return None

    def get_player(self, player_id: str) -> Player | None:
        """Get a player by ID."""
        with self._lock, sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute("SELECT * FROM players WHERE player_id = ?", (player_id,)).fetchone()
            if row:
                return Player(**dict(row))
            return None

    def save_player(self, player: Player):
        """Save or update a player."""
        with self._lock, sqlite3.connect(self.db_path) as conn:
            try:
                conn.execute(
                    """
                    INSERT OR REPLACE INTO players (
                        player_id, user_id, name, stats, inventory, status_effects,
                        current_room_id, experience_points, level, created_at, last_active
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        player.player_id,
                        player.user_id,
                        player.name,
                        player.stats,
                        player.inventory,
                        player.status_effects,
                        player.current_room_id,
                        player.experience_points,
                        player.level,
                        player.created_at.isoformat() if player.created_at else None,
                        player.last_active.isoformat() if player.last_active else None,
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
            return [Player(**dict(row)) for row in rows]

    def save_players(self, players: list[Player]):
        """Batch save players atomically."""
        with self._lock, sqlite3.connect(self.db_path) as conn:
            try:
                for player in players:
                    conn.execute(
                        """
                        INSERT OR REPLACE INTO players (
                            player_id, user_id, name, stats, inventory, status_effects,
                            current_room_id, experience_points, level, created_at, last_active
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            player.player_id,
                            player.user_id,
                            player.name,
                            player.stats,
                            player.inventory,
                            player.status_effects,
                            player.current_room_id,
                            player.experience_points,
                            player.level,
                            player.created_at.isoformat() if player.created_at else None,
                            player.last_active.isoformat() if player.last_active else None,
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
    def get_room(self, room_id: str) -> dict[str, Any] | None:
        """Get a room by ID from the cache."""
        # First try direct lookup
        if room_id in self._room_cache:
            return self._room_cache[room_id]

        # If not found, check if it's an old ID that maps to a new one
        if room_id in self._room_mappings:
            new_room_id = self._room_mappings[room_id]
            return self._room_cache.get(new_room_id)

        return None

    def save_room(self, room: dict[str, Any]):
        """Save or update a room. Currently read-only - rooms are stored as JSON files."""
        # TODO: Implement JSON file saving for rooms
        # For now, just update the cache
        self._room_cache[room["id"]] = room
        self._log(f"Updated room {room['id']} in cache (JSON file saving not implemented)")
        self._run_hooks("after_save_room", room)

    def list_rooms(self) -> list[dict[str, Any]]:
        """List all rooms from the cache."""
        return list(self._room_cache.values())

    def save_rooms(self, rooms: list[dict[str, Any]]):
        """Batch save rooms. Currently read-only - rooms are stored as JSON files."""
        # TODO: Implement JSON file saving for rooms
        # For now, just update the cache
        for room in rooms:
            self._room_cache[room["id"]] = room
        self._log(f"Updated {len(rooms)} rooms in cache (JSON file saving not implemented)")
        self._run_hooks("after_save_rooms", rooms)

    # --- TODO: Inventory, status effects, etc. ---
    # def get_inventory(self, ...): ...
    # def save_inventory(self, ...): ...
    # def list_inventory(self, ...): ...

    # --- TODO: Add async support, other backends, migrations, etc. ---
