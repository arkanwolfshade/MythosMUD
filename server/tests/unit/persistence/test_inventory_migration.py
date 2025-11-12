"""Migration tests ensuring player_inventories bootstrap correctly."""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from server.scripts.player_inventory_migration import migrate_player_inventories

LEGACY_SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE users (
    id TEXT PRIMARY KEY NOT NULL,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    hashed_password TEXT NOT NULL
);

CREATE TABLE players (
    player_id TEXT PRIMARY KEY NOT NULL,
    user_id TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    stats TEXT NOT NULL DEFAULT '{"position": "standing"}',
    inventory TEXT NOT NULL DEFAULT '[]',
    status_effects TEXT NOT NULL DEFAULT '[]',
    current_room_id TEXT NOT NULL DEFAULT 'earth_arkhamcity_sanitarium_room_foyer_001',
    respawn_room_id TEXT DEFAULT 'earth_arkhamcity_sanitarium_room_foyer_001',
    experience_points INTEGER NOT NULL DEFAULT 0,
    level INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
"""

SAMPLE_USERS = [
    ("legacy-user-1", "legacy1@example.com", "legacy1", "hashed-password-1"),
    ("legacy-user-2", "legacy2@example.com", "legacy2", "hashed-password-2"),
]

SAMPLE_PLAYERS = [
    ("legacy-player-1", "legacy-user-1", "LegacyPlayerOne"),
    ("legacy-player-2", "legacy-user-2", "LegacyPlayerTwo"),
]


@pytest.fixture
def legacy_database(tmp_path: Path) -> Path:
    """Create a legacy database missing the player_inventories table."""
    db_path = tmp_path / "legacy_inventory.db"
    with sqlite3.connect(db_path) as conn:
        conn.executescript(LEGACY_SCHEMA)
        conn.executemany(
            "INSERT INTO users (id, email, username, hashed_password) VALUES (?, ?, ?, ?)",
            SAMPLE_USERS,
        )
        conn.executemany(
            "INSERT INTO players (player_id, user_id, name) VALUES (?, ?, ?)",
            SAMPLE_PLAYERS,
        )
        conn.commit()
    return db_path


def test_migration_creates_table_and_rows(legacy_database: Path):
    migrate_player_inventories(legacy_database)

    with sqlite3.connect(legacy_database) as conn:
        tables = {row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        assert "player_inventories" in tables

        columns = [row[1] for row in conn.execute("PRAGMA table_info(player_inventories)")]
        assert columns == ["player_id", "inventory_json", "equipped_json", "created_at"]

        player_count = conn.execute("SELECT COUNT(*) FROM players").fetchone()[0]
        inventory_count = conn.execute("SELECT COUNT(*) FROM player_inventories").fetchone()[0]
        assert inventory_count == player_count

        rows = conn.execute(
            "SELECT player_id, inventory_json, equipped_json FROM player_inventories ORDER BY player_id"
        ).fetchall()
        for player_id, inventory_json, equipped_json in rows:
            assert player_id in {"legacy-player-1", "legacy-player-2"}
            assert inventory_json == "[]"
            assert equipped_json == "{}"


def test_migration_is_idempotent(legacy_database: Path):
    migrate_player_inventories(legacy_database)

    with sqlite3.connect(legacy_database) as conn:
        conn.execute(
            "UPDATE player_inventories SET inventory_json = ? WHERE player_id = ?",
            ('[{"item_id": "elder_sign"}]', "legacy-player-1"),
        )
        conn.commit()

    migrate_player_inventories(legacy_database)

    with sqlite3.connect(legacy_database) as conn:
        inventory_count = conn.execute("SELECT COUNT(*) FROM player_inventories").fetchone()[0]
        player_count = conn.execute("SELECT COUNT(*) FROM players").fetchone()[0]
        assert inventory_count == player_count

        preserved = conn.execute(
            "SELECT inventory_json FROM player_inventories WHERE player_id = ?",
            ("legacy-player-1",),
        ).fetchone()[0]
        assert preserved == '[{"item_id": "elder_sign"}]'
