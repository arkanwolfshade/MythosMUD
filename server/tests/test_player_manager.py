import pytest
from unittest.mock import patch
import tempfile
import os
from server.player_manager import PlayerManager
from server.models import Stats, StatusEffect, StatusEffectType


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
    assert manager.players_dir == os.path.join(temp_data_dir, "players")
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
    player_manager.update_player(player)  # Persist the change
    with patch.object(player_manager, "save_player") as mock_save:
        player_manager.save_player(player)
        mock_save.assert_called_once_with(player)

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


def test_get_player_by_name_and_list_players(player_manager):
    player = player_manager.create_player("Alice")
    found = player_manager.get_player_by_name("Alice")
    assert found is not None
    assert found.name == "Alice"
    players = player_manager.list_players()
    assert player in players


def test_apply_sanity_loss_and_status_effects(player_manager):
    player = player_manager.create_player("SanityTest")
    player.stats.sanity = 60
    player_manager.apply_sanity_loss(player, 15)
    assert player.stats.sanity == 45
    player_manager.apply_sanity_loss(player, 30)
    assert player.stats.sanity == 15
    # Should have paranoid and hallucinating effects
    effect_types = [e.effect_type for e in player.status_effects]
    assert StatusEffectType.PARANOID in effect_types
    assert StatusEffectType.HALLUCINATING in effect_types
    player_manager.apply_sanity_loss(player, 20)
    assert player.stats.sanity == 0
    effect_types = [e.effect_type for e in player.status_effects]
    assert StatusEffectType.INSANE in effect_types


def test_apply_fear_and_corruption(player_manager):
    player = player_manager.create_player("FearCorruptTest")
    player.stats.fear = 70
    player_manager.apply_fear(player, 10)
    assert player.stats.fear == 80
    effect_types = [e.effect_type for e in player.status_effects]
    assert StatusEffectType.TREMBLING in effect_types
    player.stats.corruption = 45
    player_manager.apply_corruption(player, 10)
    assert player.stats.corruption == 55
    effect_types = [e.effect_type for e in player.status_effects]
    assert StatusEffectType.CORRUPTED in effect_types


def test_gain_occult_knowledge(player_manager):
    player = player_manager.create_player("OccultTest")
    player.stats.occult_knowledge = 10
    player.stats.sanity = 50
    player_manager.gain_occult_knowledge(player, 20, source="tome")
    assert player.stats.occult_knowledge == 30
    assert player.stats.sanity == 40


def test_heal_and_damage_player(player_manager):
    player = player_manager.create_player("HealthTest")
    player.stats.constitution = 10  # Set predictable max_health
    player.stats.current_health = 50
    player_manager.heal_player(player, 30)
    assert player.stats.current_health == min(player.stats.max_health, 80)
    player_manager.damage_player(player, 20)
    assert player.stats.current_health == min(player.stats.max_health, 60)
    player_manager.damage_player(player, 10, damage_type="poison")
    effect_types = [e.effect_type for e in player.status_effects]
    assert StatusEffectType.POISONED in effect_types


def test_process_status_effects(player_manager):
    player = player_manager.create_player("EffectTest")
    player.stats.constitution = 10  # Set predictable max_health
    player.stats.current_health = 50
    player.stats.dexterity = 10
    # Add poison and trembling effects
    player.add_status_effect(
        StatusEffect(effect_type=StatusEffectType.POISONED, duration=2, intensity=2)
    )
    player.add_status_effect(
        StatusEffect(effect_type=StatusEffectType.TREMBLING, duration=2, intensity=2)
    )
    player_manager.process_status_effects(current_tick=1)
    # Poison should reduce health, trembling should reduce dexterity
    assert player.stats.current_health < 50
    assert player.stats.dexterity < 10


def test_load_sample_player():
    import json
    import os
    from server.models import Player

    # New path for the sample player file
    base = os.path.dirname(__file__)
    sample_path = os.path.abspath(
        os.path.join(base, "..", "..", "data", "players", "player_test-id-123.json")
    )
    with open(sample_path, "r", encoding="utf-8") as f:
        player_data = json.load(f)
    player = Player(**player_data)
    assert player.name == "SamplePlayer"
    assert player.current_room_id == "arkham_001"
    assert player.level == 2


def test_load_and_save_individual_player(tmp_path):
    from server.player_manager import PlayerManager
    import uuid
    import json

    # Setup test directory
    test_data_dir = tmp_path / "data"
    players_dir = test_data_dir / "players"
    players_dir.mkdir(parents=True)
    # Create a player file
    guid = str(uuid.uuid4())
    player_data = {
        "id": guid,
        "name": "testuser",
        "stats": {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10,
            "sanity": 100,
            "occult_knowledge": 0,
            "fear": 0,
            "corruption": 0,
            "cult_affiliation": 0,
            "current_health": 100,
            "max_health": 100,
            "max_sanity": 100,
        },
        "inventory": [],
        "status_effects": [],
        "current_room_id": "arkham_001",
        "created_at": "2025-07-24T00:00:00Z",
        "last_active": "2025-07-24T00:00:00Z",
        "experience_points": 0,
        "level": 1,
    }
    player_file = players_dir / f"player_{guid}.json"
    with open(player_file, "w", encoding="utf-8") as f:
        json.dump(player_data, f)
    # Test loading
    pm = PlayerManager(data_dir=str(test_data_dir))
    loaded = pm.get_player(guid)
    assert loaded is not None
    assert loaded.name == "testuser"
    # Test creating a new player
    new_player = pm.create_player("anotheruser")
    new_file = players_dir / f"player_{new_player.id}.json"
    assert new_file.exists()
    with open(new_file, "r", encoding="utf-8") as f:
        new_data = json.load(f)
    assert new_data["name"] == "anotheruser"
