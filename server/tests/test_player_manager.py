import os
import tempfile

import pytest

from server.models import Player
from server.persistence import PersistenceLayer


@pytest.fixture
def temp_db_path(tmp_path):
    """Create a temporary database path."""
    db_path = tmp_path / "test_players.db"
    # Initialize the database with schema
    import sqlite3

    conn = sqlite3.connect(str(db_path))
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY NOT NULL,
            username TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            is_active BOOLEAN NOT NULL DEFAULT 1,
            is_superuser BOOLEAN NOT NULL DEFAULT 0,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS players (
            player_id TEXT PRIMARY KEY NOT NULL,
            user_id TEXT NOT NULL UNIQUE,
            name TEXT UNIQUE NOT NULL,
            stats TEXT NOT NULL DEFAULT '{"health": 100, "sanity": 100, "strength": 10}',
            inventory TEXT NOT NULL DEFAULT '[]',
            status_effects TEXT NOT NULL DEFAULT '[]',
            current_room_id TEXT NOT NULL DEFAULT 'arkham_001',
            experience_points INTEGER NOT NULL DEFAULT 0,
            level INTEGER NOT NULL DEFAULT 1,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            last_active DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        );
    """)
    conn.commit()
    conn.close()
    return str(db_path)


@pytest.fixture
def temp_log_file():
    """Create a temporary log file for the persistence layer."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as log_file:
        log_path = log_file.name

    yield log_path

    # Cleanup - don't try to remove if it's still in use
    try:
        if os.path.exists(log_path):
            os.remove(log_path)
    except PermissionError:
        pass  # File might still be in use by logger


@pytest.fixture
def persistence(temp_db_path, temp_log_file):
    return PersistenceLayer(db_path=temp_db_path, log_path=temp_log_file)


def test_persistence_creation(persistence):
    assert isinstance(persistence.list_players(), list)
    assert len(persistence.list_players()) == 0


def test_create_player(persistence):
    player = Player(
        player_id="testid",
        user_id="testuserid",
        name="TestPlayer",
        current_room_id="arkham_001",
        experience_points=0,
        level=1,
    )
    persistence.save_player(player)
    loaded = persistence.get_player(player.player_id)
    assert loaded is not None
    assert loaded.name == "TestPlayer"
    assert loaded.current_room_id == "arkham_001"


def test_create_player_custom_room(persistence):
    player = Player(
        player_id="testid2",
        user_id="testuserid2",
        name="TestPlayer2",
        current_room_id="custom_room_001",
        experience_points=0,
        level=1,
    )
    persistence.save_player(player)
    loaded = persistence.get_player(player.player_id)
    assert loaded.current_room_id == "custom_room_001"


def test_get_player(persistence):
    player = Player(
        player_id="testid3",
        user_id="testuserid3",
        name="TestPlayer3",
        current_room_id="arkham_001",
        experience_points=0,
        level=1,
    )
    persistence.save_player(player)
    fetched = persistence.get_player(player.player_id)
    assert fetched is not None
    assert fetched.player_id == player.player_id
    assert fetched.name == "TestPlayer3"


def test_get_non_existent_player(persistence):
    player = persistence.get_player("non_existent_id")
    assert player is None


def test_save_player(persistence):
    player = Player(
        player_id="testid4",
        user_id="testuserid4",
        name="TestPlayer4",
        current_room_id="arkham_001",
        experience_points=0,
        level=1,
    )
    persistence.save_player(player)
    # Update stats
    stats = player.get_stats()
    stats["strength"] = 10
    player.set_stats(stats)
    persistence.save_player(player)
    loaded = persistence.get_player(player.player_id)
    assert loaded is not None
    assert loaded.get_stats()["strength"] == 10


def test_list_players(persistence):
    player1 = Player(
        player_id="id1",
        user_id="userid1",
        name="Alice",
        current_room_id="r1",
        experience_points=0,
        level=1,
    )
    player2 = Player(
        player_id="id2",
        user_id="userid2",
        name="Bob",
        current_room_id="r2",
        experience_points=0,
        level=1,
    )
    persistence.save_players([player1, player2])
    players = persistence.list_players()
    names = [p.name for p in players]
    assert "Alice" in names and "Bob" in names


def test_get_player_by_name(persistence):
    player = Player(
        player_id="id3",
        user_id="userid3",
        name="Carol",
        current_room_id="r3",
        experience_points=0,
        level=1,
    )
    persistence.save_player(player)
    found = persistence.get_player_by_name("Carol")
    assert found is not None
    assert found.name == "Carol"


def test_delete_player(persistence):
    player = Player(
        player_id="id4",
        user_id="userid4",
        name="DeleteMe",
        current_room_id="r4",
        experience_points=0,
        level=1,
    )
    persistence.save_player(player)

    # Verify player exists before deletion
    loaded = persistence.get_player(player.player_id)
    assert loaded is not None
    assert loaded.name == "DeleteMe"

    # Delete the player
    result = persistence.delete_player(player.player_id)
    assert result is True

    # Verify player no longer exists
    deleted_player = persistence.get_player(player.player_id)
    assert deleted_player is None


def test_delete_non_existent_player(persistence):
    """Test deleting a player that doesn't exist."""
    result = persistence.delete_player("non_existent_id")
    assert result is False


def test_delete_player_twice(persistence):
    """Test that deleting a player twice returns False the second time."""
    player = Player(
        player_id="id5",
        user_id="userid5",
        name="DoubleDelete",
        current_room_id="r5",
        experience_points=0,
        level=1,
    )
    persistence.save_player(player)

    # First deletion should succeed
    result1 = persistence.delete_player(player.player_id)
    assert result1 is True

    # Second deletion should fail (player no longer exists)
    result2 = persistence.delete_player(player.player_id)
    assert result2 is False


def test_batch_save_players(persistence):
    players = [
        Player(
            player_id=f"id{i}",
            user_id=f"userid{i}",
            name=f"Player{i}",
            current_room_id=f"r{i}",
            experience_points=0,
            level=1,
        )
        for i in range(5)
    ]
    persistence.save_players(players)
    loaded = persistence.list_players()
    assert len(loaded) >= 5
