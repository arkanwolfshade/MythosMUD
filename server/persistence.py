import json
import logging
import os
import sqlite3
import threading
from collections.abc import Callable
from typing import Any

from server.models import Player  # Assume Room model exists or will be added


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


# --- PersistenceLayer Class ---
class PersistenceLayer:
    """
    Unified persistence layer for all game data (players, rooms, inventory, etc.).
    Thread-safe, supports hooks, context management, and batch operations.
    """

    _hooks: dict[str, list[Callable]] = {}

    def __init__(self, db_path: str | None = None, log_path: str | None = None):
        # Default to the main production database in the project root
        self.db_path = db_path or os.environ.get("MYTHOS_DB_PATH", "../data/players.db")
        self.log_path = log_path or os.environ.get(
            "MYTHOS_PERSIST_LOG", "server/persistence.log"
        )
        self._lock = threading.RLock()
        self._logger = self._setup_logger()
        # TODO: Load config for SQL logging verbosity
        self._load_room_cache()

    def _setup_logger(self):
        logger = logging.getLogger("PersistenceLayer")
        logger.setLevel(logging.INFO)

        # Create log directory if it doesn't exist
        log_dir = os.path.dirname(self.log_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        fh = logging.FileHandler(self.log_path)
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        fh.setFormatter(formatter)
        if not logger.handlers:
            logger.addHandler(fh)
        return logger

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
        self._room_cache = {}
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                rows = conn.execute("SELECT * FROM rooms").fetchall()
                for row in rows:
                    self._room_cache[row["id"]] = dict(row)
            self._log(f"Loaded {len(self._room_cache)} rooms into cache.")
        except Exception as e:
            self._log(f"Room cache load failed: {e}")

    # --- CRUD for Players ---
    def get_player_by_name(self, name: str) -> Player | None:
        """Get a player by name."""
        with self._lock, sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT * FROM players WHERE name = ?", (name,)
            ).fetchone()
            if row:
                return Player(**dict(row))
            return None

    def get_player(self, player_id: str) -> Player | None:
        """Get a player by ID."""
        with self._lock, sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT * FROM players WHERE id = ?", (player_id,)
            ).fetchone()
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
                        id, name, strength, dexterity, constitution, intelligence, wisdom, charisma,
                        sanity, occult_knowledge, fear, corruption, cult_affiliation,
                        current_room_id, created_at, last_active, experience_points, level
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        player.id,
                        player.name,
                        player.stats.strength,
                        player.stats.dexterity,
                        player.stats.constitution,
                        player.stats.intelligence,
                        player.stats.wisdom,
                        player.stats.charisma,
                        player.stats.sanity,
                        player.stats.occult_knowledge,
                        player.stats.fear,
                        player.stats.corruption,
                        player.stats.cult_affiliation,
                        player.current_room_id,
                        player.created_at.isoformat(),
                        player.last_active.isoformat(),
                        player.experience_points,
                        player.level,
                    ),
                )
                conn.commit()
                self._log(f"Saved player {player.name} ({player.id})")
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
                            id, name, strength, dexterity, constitution, intelligence, wisdom, charisma,
                            sanity, occult_knowledge, fear, corruption, cult_affiliation,
                            current_room_id, created_at, last_active, experience_points, level
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            player.id,
                            player.name,
                            player.stats.strength,
                            player.stats.dexterity,
                            player.stats.constitution,
                            player.stats.intelligence,
                            player.stats.wisdom,
                            player.stats.charisma,
                            player.stats.sanity,
                            player.stats.occult_knowledge,
                            player.stats.fear,
                            player.stats.corruption,
                            player.stats.cult_affiliation,
                            player.current_room_id,
                            player.created_at.isoformat(),
                            player.last_active.isoformat(),
                            player.experience_points,
                            player.level,
                        ),
                    )
                conn.commit()
                self._log(f"Batch saved {len(players)} players.")
                self._run_hooks("after_save_players", players)
            except sqlite3.IntegrityError as e:
                self._log(f"Batch unique constraint error: {e}")
                raise UniqueConstraintError(str(e)) from e

    # --- CRUD for Rooms ---
    def get_room(self, room_id: str) -> dict[str, Any] | None:
        """Get a room by ID from the cache."""
        return self._room_cache.get(room_id)

    def save_room(self, room: dict[str, Any]):
        """Save or update a room."""
        with self._lock, sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO rooms (
                    id, name, description, zone, exits
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    room["id"],
                    room["name"],
                    room["description"],
                    room["zone"],
                    json.dumps(room["exits"]),
                ),
            )
            conn.commit()
            self._room_cache[room["id"]] = room
            self._log(f"Saved room {room['id']}")
            self._run_hooks("after_save_room", room)

    def list_rooms(self) -> list[dict[str, Any]]:
        """List all rooms from the cache."""
        return list(self._room_cache.values())

    def save_rooms(self, rooms: list[dict[str, Any]]):
        """Batch save rooms atomically."""
        with self._lock, sqlite3.connect(self.db_path) as conn:
            try:
                for room in rooms:
                    conn.execute(
                        """
                        INSERT OR REPLACE INTO rooms (
                            id, name, description, zone, exits
                        ) VALUES (?, ?, ?, ?, ?)
                        """,
                        (
                            room["id"],
                            room["name"],
                            room["description"],
                            room["zone"],
                            json.dumps(room["exits"]),
                        ),
                    )
                conn.commit()
                for room in rooms:
                    self._room_cache[room["id"]] = room
                self._log(f"Batch saved {len(rooms)} rooms.")
                self._run_hooks("after_save_rooms", rooms)
            except sqlite3.IntegrityError as e:
                self._log(f"Batch unique constraint error (rooms): {e}")
                raise UniqueConstraintError(str(e)) from e

    # --- TODO: Inventory, status effects, etc. ---
    # def get_inventory(self, ...): ...
    # def save_inventory(self, ...): ...
    # def list_inventory(self, ...): ...

    # --- TODO: Add async support, other backends, migrations, etc. ---
