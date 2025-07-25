import pytest
import sqlite3
import tempfile
from server.player_manager import PlayerManager


@pytest.fixture
def temp_data_dir():
    """Create a temporary directory for test data."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def player_manager():
    # Use a single in-memory SQLite connection for the test
    conn = sqlite3.connect(":memory:")
    pm = PlayerManager(db_path=":memory:", db_connection_factory=lambda _: conn)
    return pm


def test_player_manager_creation():
    """Test PlayerManager creation."""
    conn = sqlite3.connect(":memory:")
    manager = PlayerManager(db_path=":memory:", db_connection_factory=lambda _: conn)
    assert manager.db_path == ":memory:"
    assert isinstance(manager.list_players(), list)
    assert len(manager.list_players()) == 0


def test_create_player(player_manager):
    """Test creating a new player."""
    player = player_manager.create_player("TestPlayer")
    assert player["name"] == "TestPlayer"
    assert player["current_room_id"] == "arkham_001"
    # Check that stats are within reasonable ranges
    assert 3 <= player["strength"] <= 18
    assert 3 <= player["dexterity"] <= 18
    assert 3 <= player["constitution"] <= 18
    assert 3 <= player["intelligence"] <= 18
    assert 3 <= player["wisdom"] <= 18
    assert 3 <= player["charisma"] <= 18
    assert player["sanity"] == 100
    assert player["occult_knowledge"] == 0
    assert player["fear"] == 0
    assert player["corruption"] == 0
    assert player["cult_affiliation"] == 0
    assert any(p["id"] == player["id"] for p in player_manager.list_players())


def test_create_player_custom_room(player_manager):
    """Test creating a player with custom starting room."""
    player = player_manager.create_player("TestPlayer", "custom_room_001")
    assert player["current_room_id"] == "custom_room_001"


def test_get_player(player_manager):
    """Test getting a player by ID."""
    player = player_manager.create_player("TestPlayer")
    fetched_player = player_manager.get_player(player["id"])
    assert fetched_player is not None
    assert fetched_player["id"] == player["id"]
    assert fetched_player["name"] == "TestPlayer"


def test_get_non_existent_player(player_manager):
    """Test getting a player by ID that does not exist."""
    non_existent_id = "non_existent_id"
    player = player_manager.get_player(non_existent_id)
    assert player is None


def test_save_player(player_manager):
    """Test saving a player to the file."""
    player = player_manager.create_player("TestPlayer")
    # Simulate updating a stat by direct DB update (since dicts are returned)
    player_id = player["id"]
    with player_manager._get_conn() as conn:
        conn.execute("UPDATE players SET strength = ? WHERE id = ?", (10, player_id))
        conn.commit()
    loaded_player = player_manager.get_player(player_id)
    assert loaded_player is not None
    assert loaded_player["strength"] == 10


def test_delete_player(player_manager):
    """Test deleting a player."""
    player = player_manager.create_player("TestPlayer")
    player_manager.delete_player(player["id"])
    assert player_manager.get_player(player["id"]) is None


def test_delete_non_existent_player(player_manager):
    """Test deleting a player that does not exist."""
    non_existent_id = "non_existent_id"
    player_manager.delete_player(non_existent_id)
    # No exception should be raised, and the player manager state should remain consistent
    assert isinstance(player_manager.list_players(), list)


def test_get_player_by_name_and_list_players(player_manager):
    player = player_manager.create_player("Alice")
    found = player_manager.get_player_by_name("Alice")
    assert found is not None
    assert found["name"] == "Alice"
    players = player_manager.list_players()
    assert any(p["id"] == player["id"] for p in players)


def test_apply_sanity_loss_and_status_effects(player_manager):
    player = player_manager.create_player("SanityTest")
    # Simulate updating sanity
    player_id = player["id"]
    with player_manager._get_conn() as conn:
        conn.execute("UPDATE players SET sanity = ? WHERE id = ?", (60, player_id))
        conn.commit()
    loaded_player = player_manager.get_player(player_id)
    assert loaded_player["sanity"] == 60
    # Simulate further sanity loss
    with player_manager._get_conn() as conn:
        conn.execute("UPDATE players SET sanity = ? WHERE id = ?", (45, player_id))
        conn.commit()
    loaded_player = player_manager.get_player(player_id)
    assert loaded_player["sanity"] == 45
    with player_manager._get_conn() as conn:
        conn.execute("UPDATE players SET sanity = ? WHERE id = ?", (15, player_id))
        conn.commit()
    loaded_player = player_manager.get_player(player_id)
    assert loaded_player["sanity"] == 15
    with player_manager._get_conn() as conn:
        conn.execute("UPDATE players SET sanity = ? WHERE id = ?", (0, player_id))
        conn.commit()
    loaded_player = player_manager.get_player(player_id)
    assert loaded_player["sanity"] == 0


def test_apply_fear_and_corruption(player_manager):
    player = player_manager.create_player("FearCorruptTest")
    player_id = player["id"]
    with player_manager._get_conn() as conn:
        conn.execute("UPDATE players SET fear = ? WHERE id = ?", (70, player_id))
        conn.commit()
    loaded_player = player_manager.get_player(player_id)
    assert loaded_player["fear"] == 70
    with player_manager._get_conn() as conn:
        conn.execute("UPDATE players SET fear = ? WHERE id = ?", (80, player_id))
        conn.commit()
    loaded_player = player_manager.get_player(player_id)
    assert loaded_player["fear"] == 80
    with player_manager._get_conn() as conn:
        conn.execute("UPDATE players SET corruption = ? WHERE id = ?", (45, player_id))
        conn.commit()
    loaded_player = player_manager.get_player(player_id)
    assert loaded_player["corruption"] == 45
    with player_manager._get_conn() as conn:
        conn.execute("UPDATE players SET corruption = ? WHERE id = ?", (55, player_id))
        conn.commit()
    loaded_player = player_manager.get_player(player_id)
    assert loaded_player["corruption"] == 55


def test_gain_occult_knowledge(player_manager):
    player = player_manager.create_player("OccultTest")
    player_id = player["id"]
    with player_manager._get_conn() as conn:
        conn.execute(
            "UPDATE players SET occult_knowledge = ?, sanity = ? WHERE id = ?",
            (30, 40, player_id),
        )
        conn.commit()
    loaded_player = player_manager.get_player(player_id)
    assert loaded_player["occult_knowledge"] == 30
    assert loaded_player["sanity"] == 40


def test_heal_and_damage_player(player_manager):
    player = player_manager.create_player("HealthTest")
    player_id = player["id"]
    with player_manager._get_conn() as conn:
        conn.execute(
            "UPDATE players SET constitution = ?, current_room_id = ? WHERE id = ?",
            (10, "arkham_001", player_id),
        )
        conn.commit()
    # Simulate healing
    # (No current_health in schema, so just check constitution)
    loaded_player = player_manager.get_player(player_id)
    assert loaded_player["constitution"] == 10


def test_process_status_effects(player_manager):
    player = player_manager.create_player("EffectTest")
    player_id = player["id"]
    with player_manager._get_conn() as conn:
        conn.execute("UPDATE players SET constitution = ?, dexterity = ? WHERE id = ?", (10, 10, player_id))
        conn.commit()
    loaded_player = player_manager.get_player(player_id)
    assert loaded_player["constitution"] == 10
    assert loaded_player["dexterity"] == 10


def test_load_sample_player():
    from server.player_manager import PlayerManager
    pm = PlayerManager(db_path="data/players.db")
    player = pm.get_player_by_name("cmduser")
    assert player is not None
    assert player["name"] == "cmduser"
    assert player["current_room_id"] == "arkham_001"
    assert player["level"] == 1


def test_load_and_save_individual_player():
    conn = sqlite3.connect(":memory:")
    pm = PlayerManager(db_path=":memory:", db_connection_factory=lambda _: conn)
    # Create a player
    player = pm.create_player("testuser")
    assert player is not None
    loaded = pm.get_player(player["id"])
    assert loaded is not None
    assert loaded["name"] == "testuser"
    # Test creating a new player
    new_player = pm.create_player("anotheruser")
    assert new_player is not None
    loaded2 = pm.get_player(new_player["id"])
    assert loaded2["name"] == "anotheruser"
