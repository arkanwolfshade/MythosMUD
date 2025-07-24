import pytest
import tempfile
import os
from player_manager import PlayerManager
from models import Stats, StatusEffect, StatusEffectType


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
    created_player = player_manager.create_player("TestPlayer")
    retrieved_player = player_manager.get_player(created_player.id)

    assert retrieved_player is not None
    assert retrieved_player.id == created_player.id
    assert retrieved_player.name == created_player.name


def test_get_player_nonexistent(player_manager):
    """Test getting a non-existent player."""
    player = player_manager.get_player("nonexistent_id")
    assert player is None


def test_get_player_by_name(player_manager):
    """Test getting a player by name."""
    created_player = player_manager.create_player("TestPlayer")
    retrieved_player = player_manager.get_player_by_name("TestPlayer")

    assert retrieved_player is not None
    assert retrieved_player.id == created_player.id
    assert retrieved_player.name == created_player.name


def test_get_player_by_name_case_insensitive(player_manager):
    """Test getting a player by name (case insensitive)."""
    created_player = player_manager.create_player("TestPlayer")
    retrieved_player = player_manager.get_player_by_name("testplayer")

    assert retrieved_player is not None
    assert retrieved_player.id == created_player.id


def test_get_player_by_name_nonexistent(player_manager):
    """Test getting a non-existent player by name."""
    player = player_manager.get_player_by_name("NonexistentPlayer")
    assert player is None


def test_list_players(player_manager):
    """Test listing all players."""
    player1 = player_manager.create_player("Player1")
    player2 = player_manager.create_player("Player2")

    players = player_manager.list_players()
    assert len(players) == 2
    player_ids = [p.id for p in players]
    assert player1.id in player_ids
    assert player2.id in player_ids


def test_delete_player(player_manager):
    """Test deleting a player."""
    player = player_manager.create_player("TestPlayer")
    assert player.id in player_manager.players

    success = player_manager.delete_player(player.id)
    assert success is True
    assert player.id not in player_manager.players


def test_delete_player_nonexistent(player_manager):
    """Test deleting a non-existent player."""
    success = player_manager.delete_player("nonexistent_id")
    assert success is False


def test_apply_sanity_loss(player_manager):
    """Test applying sanity loss to a player."""
    player = player_manager.create_player("TestPlayer")
    initial_sanity = player.stats.sanity

    player_manager.apply_sanity_loss(player, 25, "test source")

    assert player.stats.sanity == initial_sanity - 25
    # No status effects should be applied for moderate sanity loss
    assert len(player.status_effects) == 0


def test_apply_sanity_loss_severe(player_manager):
    """Test applying severe sanity loss that triggers hallucinations."""
    player = player_manager.create_player("TestPlayer")

    player_manager.apply_sanity_loss(player, 80, "severe trauma")

    assert player.stats.sanity == 20
    assert len(player.status_effects) == 1
    assert player.status_effects[0].effect_type == StatusEffectType.HALLUCINATING


def test_apply_sanity_loss_insane(player_manager):
    """Test applying sanity loss that drives player insane."""
    player = player_manager.create_player("TestPlayer")

    player_manager.apply_sanity_loss(player, 100, "complete horror")

    assert player.stats.sanity == 0
    assert len(player.status_effects) == 1
    assert player.status_effects[0].effect_type == StatusEffectType.INSANE


def test_apply_fear(player_manager):
    """Test applying fear to a player."""
    player = player_manager.create_player("TestPlayer")
    initial_fear = player.stats.fear

    player_manager.apply_fear(player, 30, "scary encounter")

    assert player.stats.fear == initial_fear + 30
    assert len(player.status_effects) == 0  # Not enough fear for trembling


def test_apply_fear_trembling(player_manager):
    """Test applying fear that triggers trembling."""
    player = player_manager.create_player("TestPlayer")

    player_manager.apply_fear(player, 80, "extreme terror")

    assert player.stats.fear == 80
    assert len(player.status_effects) == 1
    assert player.status_effects[0].effect_type == StatusEffectType.TREMBLING


def test_apply_corruption(player_manager):
    """Test applying corruption to a player."""
    player = player_manager.create_player("TestPlayer")
    initial_corruption = player.stats.corruption

    player_manager.apply_corruption(player, 20, "dark ritual")

    assert player.stats.corruption == initial_corruption + 20
    assert len(player.status_effects) == 0  # Not enough corruption for effect


def test_apply_corruption_significant(player_manager):
    """Test applying corruption that triggers status effect."""
    player = player_manager.create_player("TestPlayer")

    player_manager.apply_corruption(player, 60, "major corruption")

    assert player.stats.corruption == 60
    assert len(player.status_effects) == 1
    assert player.status_effects[0].effect_type == StatusEffectType.CORRUPTED


def test_gain_occult_knowledge(player_manager):
    """Test gaining occult knowledge."""
    player = player_manager.create_player("TestPlayer")
    initial_knowledge = player.stats.occult_knowledge
    initial_sanity = player.stats.sanity

    player_manager.gain_occult_knowledge(player, 10, "forbidden tome")

    assert player.stats.occult_knowledge == initial_knowledge + 10
    assert player.stats.sanity == initial_sanity - 5  # Half the knowledge gained


def test_heal_player(player_manager):
    """Test healing a player."""
    player = player_manager.create_player("TestPlayer")
    player.stats.current_health = 50  # Damage the player

    player_manager.heal_player(player, 30)

    # Should be healed from 50 to 80, but not exceed max_health
    expected_health = min(50 + 30, player.stats.max_health)
    assert player.stats.current_health == expected_health


def test_heal_player_max_health(player_manager):
    """Test healing a player beyond max health."""
    player = player_manager.create_player("TestPlayer")
    max_health = player.stats.max_health

    player_manager.heal_player(player, 1000)

    assert player.stats.current_health == max_health


def test_damage_player(player_manager):
    """Test damaging a player."""
    player = player_manager.create_player("TestPlayer")
    initial_health = player.stats.current_health

    player_manager.damage_player(player, 30, "physical")

    assert player.stats.current_health == initial_health - 30


def test_damage_player_poison(player_manager):
    """Test poisoning a player."""
    player = player_manager.create_player("TestPlayer")

    player_manager.damage_player(player, 20, "poison")

    assert len(player.status_effects) == 1
    assert player.status_effects[0].effect_type == StatusEffectType.POISONED
    assert player.status_effects[0].duration == 10


def test_process_status_effects(player_manager):
    """Test processing status effects."""
    player = player_manager.create_player("TestPlayer")

    # Add a poisoned effect
    effect = StatusEffect(
        effect_type=StatusEffectType.POISONED, duration=10, intensity=5, source="test"
    )
    player.add_status_effect(effect)

    initial_health = player.stats.current_health

    # Process effects
    player_manager.process_status_effects(5)  # Current tick

    # Should have taken poison damage
    assert player.stats.current_health < initial_health


def test_data_persistence(temp_data_dir):
    """Test that player data persists between manager instances."""
    # Create first manager and add a player
    manager1 = PlayerManager(data_dir=temp_data_dir)
    player = manager1.create_player("TestPlayer")

    # Create second manager and check if player exists
    manager2 = PlayerManager(data_dir=temp_data_dir)
    retrieved_player = manager2.get_player(player.id)

    assert retrieved_player is not None
    assert retrieved_player.name == "TestPlayer"
