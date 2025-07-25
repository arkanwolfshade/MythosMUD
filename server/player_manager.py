import sqlite3
import uuid
from datetime import datetime
from typing import Optional, Dict, Any, Callable
import os


class PlayerManager:
    def __init__(self, db_path: str = "data/players.db", db_connection_factory: Optional[Callable] = None):
        self.db_path = db_path
        self.db_connection_factory = db_connection_factory or (lambda path: sqlite3.connect(path))
        dir_name = os.path.dirname(self.db_path)
        if dir_name and self.db_path != ":memory:":
            os.makedirs(dir_name, exist_ok=True)
        self._init_db()

    def _get_conn(self):
        return self.db_connection_factory(self.db_path)

    def _init_db(self):
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS players (
                    id TEXT PRIMARY KEY,
                    name TEXT UNIQUE NOT NULL,
                    strength INTEGER,
                    dexterity INTEGER,
                    constitution INTEGER,
                    intelligence INTEGER,
                    wisdom INTEGER,
                    charisma INTEGER,
                    sanity INTEGER,
                    occult_knowledge INTEGER,
                    fear INTEGER,
                    corruption INTEGER,
                    cult_affiliation INTEGER,
                    current_room_id TEXT,
                    created_at TEXT,
                    last_active TEXT,
                    experience_points INTEGER,
                    level INTEGER
                )
            """)
            conn.commit()

    def create_player(self, name: str, starting_room_id: str = "arkham_001") -> Optional[Dict[str, Any]]:
        if self.get_player_by_name(name):
            return None  # Player with this name already exists
        player_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat() + "Z"
        stats = {
            "strength": 10, "dexterity": 10, "constitution": 10,
            "intelligence": 10, "wisdom": 10, "charisma": 10,
            "sanity": 100, "occult_knowledge": 0, "fear": 0,
            "corruption": 0, "cult_affiliation": 0
        }
        with self._get_conn() as conn:
            conn.execute("""
                INSERT INTO players (
                    id, name, strength, dexterity, constitution, intelligence, wisdom, charisma,
                    sanity, occult_knowledge, fear, corruption, cult_affiliation,
                    current_room_id, created_at, last_active, experience_points, level
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                player_id, name, stats["strength"], stats["dexterity"], stats["constitution"],
                stats["intelligence"], stats["wisdom"], stats["charisma"], stats["sanity"],
                stats["occult_knowledge"], stats["fear"], stats["corruption"], stats["cult_affiliation"],
                starting_room_id, now, now, 0, 1
            ))
            conn.commit()
        return self.get_player(player_id)

    def get_player(self, player_id: str) -> Optional[Dict[str, Any]]:
        with self._get_conn() as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute("SELECT * FROM players WHERE id = ?", (player_id,)).fetchone()
            return dict(row) if row else None

    def get_player_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        with self._get_conn() as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute("SELECT * FROM players WHERE name = ?", (name,)).fetchone()
            return dict(row) if row else None

    def list_players(self):
        with self._get_conn() as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute("SELECT * FROM players").fetchall()
            return [dict(row) for row in rows]

    def delete_player(self, player_id: str):
        with self._get_conn() as conn:
            conn.execute("DELETE FROM players WHERE id = ?", (player_id,))
            conn.commit()
