"""Tests for the sanity system database migration."""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from server.scripts.sanity_migration import migrate_sanity_system

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
    """Provision a legacy database missing sanity tables for migration tests."""
    db_path = tmp_path / "legacy_sanity.db"
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


def test_migration_creates_tables_and_backfills_defaults(legacy_database: Path) -> None:
    """Ensure new sanity tables exist and baseline data is backfilled."""
    migrate_sanity_system(legacy_database)

    with sqlite3.connect(legacy_database) as conn:
        tables = {row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        expected_tables = {
            "player_sanity",
            "sanity_adjustment_log",
            "sanity_exposure_state",
            "sanity_cooldowns",
        }
        assert expected_tables.issubset(tables)

        player_rows = conn.execute(
            """
            SELECT player_id, current_san, current_tier, liabilities, catatonia_entered_at
            FROM player_sanity
            ORDER BY player_id
            """
        ).fetchall()

        assert player_rows == [
            ("legacy-player-1", 100, "lucid", "[]", None),
            ("legacy-player-2", 100, "lucid", "[]", None),
        ]

        sanity_index_names = {row[1] for row in conn.execute("PRAGMA index_list('player_sanity')")}
        assert "idx_player_sanity_tier" in sanity_index_names

        adjustment_index_names = {row[1] for row in conn.execute("PRAGMA index_list('sanity_adjustment_log')")}
        assert "idx_sanity_adjustment_player_created" in adjustment_index_names


def test_migration_enforces_constraints_and_foreign_keys(legacy_database: Path) -> None:
    """Validate foreign keys, unique constraints, and value ranges."""
    migrate_sanity_system(legacy_database)

    with sqlite3.connect(legacy_database) as conn:
        conn.execute("PRAGMA foreign_keys = ON")

        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                "INSERT INTO player_sanity (player_id, current_san, current_tier, liabilities) VALUES (?, ?, ?, ?)",
                ("phantom-player", 100, "lucid", "[]"),
            )
            conn.commit()
        conn.rollback()

        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                "UPDATE player_sanity SET current_san = ? WHERE player_id = ?",
                (101, "legacy-player-1"),
            )
            conn.commit()
        conn.rollback()

        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                "UPDATE player_sanity SET current_tier = ? WHERE player_id = ?",
                ("eldritch", "legacy-player-1"),
            )
            conn.commit()
        conn.rollback()

        conn.execute(
            "INSERT INTO sanity_exposure_state (player_id, entity_archetype, encounter_count) VALUES (?, ?, ?)",
            ("legacy-player-1", "star_vampire", 1),
        )
        conn.commit()
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                "INSERT INTO sanity_exposure_state (player_id, entity_archetype, encounter_count) VALUES (?, ?, ?)",
                ("legacy-player-1", "star_vampire", 2),
            )
            conn.commit()
        conn.rollback()

        conn.execute(
            "INSERT INTO sanity_cooldowns (player_id, action_code, cooldown_expires_at) VALUES (?, ?, ?)",
            ("legacy-player-1", "pray", "2099-01-01T00:00:00Z"),
        )
        conn.commit()
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                "INSERT INTO sanity_cooldowns (player_id, action_code, cooldown_expires_at) VALUES (?, ?, ?)",
                ("legacy-player-1", "pray", "2099-01-02T00:00:00Z"),
            )
            conn.commit()
        conn.rollback()


def test_migration_is_idempotent_and_preserves_updates(legacy_database: Path) -> None:
    """Running the migration multiple times should not clobber existing data."""
    migrate_sanity_system(legacy_database)

    with sqlite3.connect(legacy_database) as conn:
        conn.execute("UPDATE player_sanity SET current_san = ? WHERE player_id = ?", (42, "legacy-player-1"))
        conn.commit()

    migrate_sanity_system(legacy_database)

    with sqlite3.connect(legacy_database) as conn:
        player_rows = conn.execute("SELECT player_id, current_san FROM player_sanity ORDER BY player_id").fetchall()
        assert player_rows == [
            ("legacy-player-1", 42),
            ("legacy-player-2", 100),
        ]

        sanity_row_count = conn.execute("SELECT COUNT(*) FROM player_sanity").fetchone()[0]
        assert sanity_row_count == 2
