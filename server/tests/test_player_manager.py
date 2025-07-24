import pytest
import tempfile
import os
from player_manager import PlayerManager
from models import Stats


@pytest.fixture
def temp_data_dir():
    """Create a temporary directory for test data."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def player_manager(temp_data_dir):
    """Create a PlayerManager instance with temporary data directory."""
    return PlayerManager(data_dir=temp_data_dir)


def test_player_manager_creation(temp_data_dir):
    """Test PlayerManager creation."""
    manager = PlayerManager(data_dir=temp_data_dir)
    assert manager.data_dir == temp_data_dir
    assert manager.players_file == os.path.join(temp_data_dir, "players.json")
    assert isinstance(manager.players, dict)
    assert len(manager.players) == 0


def test_create_player(player_manager):
    """Test creating a new player."""
    player = player_manager.create_player("TestPlayer")
    assert player.name == "TestPlayer"
    assert isinstance(player.stats, Stats)
    assert player.current_room_id == "arkham_001"
    assert player.id in player_manager.players
    # Check that stats are within reasonable ranges
    assert 3 <= player.stats.strength <= 18
    assert 3 <= player.stats.dexterity <= 18
    assert 3 <= player.stats.constitution <= 18
    assert 3 <= player.stats.intelligence <= 18
    assert 3 <= player.stats.wisdom <= 18
    assert 3 <= player.stats.charisma <= 18
    assert player.stats.sanity == 100
    assert player.stats.occult_knowledge == 0
    assert player.stats.fear == 0
    assert player.stats.corruption == 0
    assert player.stats.cult_affiliation == 0


def test_create_player_custom_room(player_manager):
    """Test creating a player with custom starting room."""
    player = player_manager.create_player("TestPlayer", "custom_room_001")
    assert player.current_room_id == "custom_room_001"


def test_get_player(player_manager):
    """Test getting a player by ID."""
    player = player_manager.create_player("TestPlayer")
    fetched_player = player_manager.get_player(player.id)
    assert fetched_player is not None
    assert fetched_player.id == player.id
    assert fetched_player.name == "TestPlayer"


def test_get_non_existent_player(player_manager):
    """Test getting a player by ID that does not exist."""
    non_existent_id = "non_existent_id"
    player = player_manager.get_player(non_existent_id)
    assert player is None


def test_save_player(player_manager):
    """Test saving a player to the file."""
    player = player_manager.create_player("TestPlayer")
    player.stats.strength = 10  # Modify a stat
    player_manager.save_player(player)

    # Create a new manager instance to test loading
    new_manager = PlayerManager(data_dir=player_manager.data_dir)
    loaded_player = new_manager.get_player(player.id)
    assert loaded_player is not None
    assert loaded_player.stats.strength == 10


def test_delete_player(player_manager):
    """Test deleting a player."""
    player = player_manager.create_player("TestPlayer")
    player_manager.delete_player(player.id)
    assert player.id not in player_manager.players


def test_delete_non_existent_player(player_manager):
    """Test deleting a player that does not exist."""
    non_existent_id = "non_existent_id"
    player_manager.delete_player(non_existent_id)
    # No exception should be raised, and the player manager state should remain consistent
    assert len(player_manager.players) == 0
