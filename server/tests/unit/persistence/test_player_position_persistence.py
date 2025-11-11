"""Tests verifying player position persistence across login/logout cycles."""

from __future__ import annotations

import sqlite3
from datetime import UTC, datetime
from pathlib import Path

from server.models.player import Player
from server.persistence import PersistenceLayer


def initialize_database(db_path: Path, user_id: str = "test-user-position") -> None:
    """Create a fresh SQLite database with required schema and seed data."""
    schema_path = Path("server/sql/schema.sql")
    schema_sql = schema_path.read_text(encoding="utf-8")

    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.executescript(schema_sql)
        conn.execute(
            """
            INSERT OR REPLACE INTO users (
                id, email, username, hashed_password, is_active, is_superuser, is_verified
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                "position_test@example.com",
                "position_test_user",
                "hashed-password",
                1,
                0,
                1,
            ),
        )
        conn.commit()


def build_player(player_id: str, user_id: str) -> Player:
    """Create a Player instance with timestamps normalized for persistence tests."""
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="PositionTester",
        current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
    )
    now = datetime.now(UTC).replace(tzinfo=None)
    player.created_at = now  # type: ignore[assignment]
    player.last_active = now  # type: ignore[assignment]
    return player


def test_player_stats_include_position_by_default():
    """Ensure newly constructed Player stats include a standing position."""
    player = build_player("player-default-position", "user-default-position")
    stats = player.get_stats()

    assert "position" in stats, "position field should be present in default stats"
    assert stats["position"] == "standing", "default position should be standing"


def test_position_persists_across_logout_login_cycle(tmp_path: Path):
    """Verify that player position changes persist after saving and reloading."""
    db_path = tmp_path / "position_persistence.db"
    user_id = "position-user"
    initialize_database(db_path, user_id=user_id)

    persistence = PersistenceLayer(db_path=str(db_path))

    player_id = "position-player"
    player = build_player(player_id, user_id)

    # Initial save representing the player's first login.
    persistence.save_player(player)

    # Load the player (simulating a login) and confirm standing.
    loaded_player = persistence.get_player(player_id)
    assert loaded_player is not None, "player should load successfully after initial save"
    assert loaded_player.get_stats()["position"] == "standing"

    # Change position to sitting and persist (simulating logout).
    updated_stats = loaded_player.get_stats()
    updated_stats["position"] = "sitting"
    loaded_player.set_stats(updated_stats)
    persistence.save_player(loaded_player)

    # Reload and ensure the sitting posture persisted.
    reloaded_player = persistence.get_player(player_id)
    assert reloaded_player is not None, "player should load successfully after updating position"
    assert reloaded_player.get_stats()["position"] == "sitting"


def test_missing_position_defaults_to_standing_on_load(tmp_path: Path):
    """Players with legacy stats lacking position should default to standing."""
    db_path = tmp_path / "legacy_position.db"
    user_id = "legacy-position-user"
    initialize_database(db_path, user_id=user_id)

    # Insert legacy stats without a position field.
    legacy_stats = (
        '{"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, '
        '"wisdom": 10, "charisma": 10, "sanity": 100, "occult_knowledge": 0, '
        '"fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100}'
    )

    player_id = "legacy-player"
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute(
            """
            INSERT INTO players (
                player_id, user_id, name, stats, inventory, status_effects,
                current_room_id, experience_points, level, is_admin, profession_id
            ) VALUES (?, ?, ?, ?, '[]', '[]', ?, 0, 1, 0, 0)
            """,
            (
                player_id,
                user_id,
                "LegacyPlayer",
                legacy_stats,
                "earth_arkhamcity_sanitarium_room_foyer_001",
            ),
        )
        conn.commit()

    persistence = PersistenceLayer(db_path=str(db_path))
    rehydrated_player = persistence.get_player(player_id)

    assert rehydrated_player is not None, "legacy player should load successfully"
    assert rehydrated_player.get_stats()["position"] == "standing", "legacy player should default to standing position"
