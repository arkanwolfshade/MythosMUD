import pytest
import sqlite3
from server.persistence import PersistenceLayer
from server.models import Player, Stats


@pytest.fixture
def temp_db_path(tmp_path):
    db_path = tmp_path / "test_players.db"
    # Create the DB file and schema
    conn = sqlite3.connect(str(db_path))
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
    conn.close()
    return str(db_path)


@pytest.fixture
def persistence(temp_db_path):
    return PersistenceLayer(db_path=temp_db_path)


def test_persistence_creation(persistence):
    assert isinstance(persistence.list_players(), list)
    assert len(persistence.list_players()) == 0


def test_create_player(persistence):
    player = Player(
        id="testid",
        name="TestPlayer",
        stats=Stats(),
        current_room_id="arkham_001",
        experience_points=0,
        level=1,
    )
    persistence.save_player(player)
    loaded = persistence.get_player(player.id)
    assert loaded is not None
    assert loaded.name == "TestPlayer"
    assert loaded.current_room_id == "arkham_001"


def test_create_player_custom_room(persistence):
    player = Player(
        id="testid2",
        name="TestPlayer2",
        stats=Stats(),
        current_room_id="custom_room_001",
        experience_points=0,
        level=1,
    )
    persistence.save_player(player)
    loaded = persistence.get_player(player.id)
    assert loaded.current_room_id == "custom_room_001"


def test_get_player(persistence):
    player = Player(
        id="testid3",
        name="TestPlayer3",
        stats=Stats(),
        current_room_id="arkham_001",
        experience_points=0,
        level=1,
    )
    persistence.save_player(player)
    fetched = persistence.get_player(player.id)
    assert fetched is not None
    assert fetched.id == player.id
    assert fetched.name == "TestPlayer3"


def test_get_non_existent_player(persistence):
    player = persistence.get_player("non_existent_id")
    assert player is None


def test_save_player(persistence):
    player = Player(
        id="testid4",
        name="TestPlayer4",
        stats=Stats(strength=5),
        current_room_id="arkham_001",
        experience_points=0,
        level=1,
    )
    persistence.save_player(player)
    # Update stat
    player.stats.strength = 10
    persistence.save_player(player)
    loaded = persistence.get_player(player.id)
    assert loaded is not None
    assert loaded.stats.strength == 10


def test_list_players(persistence):
    player1 = Player(
        id="id1",
        name="Alice",
        stats=Stats(),
        current_room_id="r1",
        experience_points=0,
        level=1,
    )
    player2 = Player(
        id="id2",
        name="Bob",
        stats=Stats(),
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
        id="id3",
        name="Carol",
        stats=Stats(),
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
        id="id4",
        name="DeleteMe",
        stats=Stats(),
        current_room_id="r4",
        experience_points=0,
        level=1,
    )
    persistence.save_player(player)
    # Simulate delete (not yet implemented in PersistenceLayer)
    # persistence.delete_player(player.id)
    # assert persistence.get_player(player.id) is None
    # For now, just check player exists
    loaded = persistence.get_player(player.id)
    assert loaded is not None


def test_batch_save_players(persistence):
    players = [
        Player(
            id=f"id{i}",
            name=f"Player{i}",
            stats=Stats(),
            current_room_id=f"r{i}",
            experience_points=0,
            level=1,
        )
        for i in range(5)
    ]
    persistence.save_players(players)
    loaded = persistence.list_players()
    assert len(loaded) >= 5
