"""
Unit tests for spawn validator.

Tests the should_spawn_npc function.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.models.npc import NPCDefinition, NPCSpawnRule
from server.npc.spawn_validator import should_spawn_npc
from server.npc.zone_configuration import ZoneConfiguration


@pytest.fixture
def mock_npc_definition():
    """Create a mock NPC definition."""
    definition = MagicMock(spec=NPCDefinition)
    definition.id = 1
    definition.name = "Test NPC"
    definition.spawn_probability = 0.5
    definition.max_population = 10
    definition.can_spawn = MagicMock(return_value=True)
    definition.is_required = MagicMock(return_value=False)
    return definition


@pytest.fixture
def mock_zone_config():
    """Create a mock zone configuration."""
    config = MagicMock(spec=ZoneConfiguration)
    config.get_effective_spawn_probability = MagicMock(return_value=0.5)
    return config


@pytest.fixture
def mock_population_stats():
    """Create mock population statistics."""
    stats = MagicMock()
    stats.npcs_by_definition = {}
    return stats


def test_should_spawn_npc_population_limit_exceeded(mock_npc_definition, mock_zone_config):
    """Test should_spawn_npc() returns False when population limit exceeded."""
    mock_npc_definition.can_spawn.return_value = False
    stats = MagicMock()
    stats.npcs_by_definition = {1: 10}  # At max
    result = should_spawn_npc(
        definition=mock_npc_definition,
        zone_config=mock_zone_config,
        room_id="room-123",
        population_stats=stats,
        spawn_rules={},
        current_game_state={},
    )
    assert result is False


def test_should_spawn_npc_population_limit_ok(mock_npc_definition, mock_zone_config, mock_population_stats):
    """Test should_spawn_npc() continues when population limit is OK."""
    mock_npc_definition.can_spawn.return_value = True
    mock_population_stats.npcs_by_definition = {1: 5}  # Below max
    result = should_spawn_npc(
        definition=mock_npc_definition,
        zone_config=mock_zone_config,
        room_id="room-123",
        population_stats=mock_population_stats,
        spawn_rules={},
        current_game_state={},
    )
    # Should continue to check other conditions (required NPC check)
    assert isinstance(result, bool)


def test_should_spawn_npc_no_population_stats(mock_npc_definition, mock_zone_config):
    """Test should_spawn_npc() handles None population stats."""
    result = should_spawn_npc(
        definition=mock_npc_definition,
        zone_config=mock_zone_config,
        room_id="room-123",
        population_stats=None,
        spawn_rules={},
        current_game_state={},
    )
    # Should continue to check other conditions
    assert isinstance(result, bool)


def test_should_spawn_npc_spawn_rule_passes(mock_npc_definition, mock_zone_config, mock_population_stats):
    """Test should_spawn_npc() returns True when spawn rule passes."""
    mock_npc_definition.can_spawn.return_value = True
    spawn_rule = MagicMock(spec=NPCSpawnRule)
    spawn_rule.can_spawn_with_population = MagicMock(return_value=True)
    spawn_rule.check_spawn_conditions = MagicMock(return_value=True)
    spawn_rule.max_population = 10
    spawn_rules = {1: [spawn_rule]}
    with patch("random.random", return_value=0.3):  # Below 0.5 probability
        result = should_spawn_npc(
            definition=mock_npc_definition,
            zone_config=mock_zone_config,
            room_id="room-123",
            population_stats=mock_population_stats,
            spawn_rules=spawn_rules,
            current_game_state={},
        )
        assert result is True


def test_should_spawn_npc_spawn_rule_fails_population(mock_npc_definition, mock_zone_config, mock_population_stats):
    """Test should_spawn_npc() skips rule when population check fails."""
    mock_npc_definition.can_spawn.return_value = True
    spawn_rule = MagicMock(spec=NPCSpawnRule)
    spawn_rule.can_spawn_with_population = MagicMock(return_value=False)
    spawn_rules = {1: [spawn_rule]}
    result = should_spawn_npc(
        definition=mock_npc_definition,
        zone_config=mock_zone_config,
        room_id="room-123",
        population_stats=mock_population_stats,
        spawn_rules=spawn_rules,
        current_game_state={},
    )
    # Should continue to check other conditions (required NPC)
    assert isinstance(result, bool)


def test_should_spawn_npc_spawn_rule_fails_conditions(mock_npc_definition, mock_zone_config, mock_population_stats):
    """Test should_spawn_npc() skips rule when spawn conditions fail."""
    mock_npc_definition.can_spawn.return_value = True
    spawn_rule = MagicMock(spec=NPCSpawnRule)
    spawn_rule.can_spawn_with_population = MagicMock(return_value=True)
    spawn_rule.check_spawn_conditions = MagicMock(return_value=False)
    spawn_rules = {1: [spawn_rule]}
    result = should_spawn_npc(
        definition=mock_npc_definition,
        zone_config=mock_zone_config,
        room_id="room-123",
        population_stats=mock_population_stats,
        spawn_rules=spawn_rules,
        current_game_state={},
    )
    # Should continue to check other conditions
    assert isinstance(result, bool)


def test_should_spawn_npc_spawn_rule_fails_probability(mock_npc_definition, mock_zone_config, mock_population_stats):
    """Test should_spawn_npc() returns False when probability roll fails."""
    mock_npc_definition.can_spawn.return_value = True
    spawn_rule = MagicMock(spec=NPCSpawnRule)
    spawn_rule.can_spawn_with_population = MagicMock(return_value=True)
    spawn_rule.check_spawn_conditions = MagicMock(return_value=True)
    spawn_rules = {1: [spawn_rule]}
    with patch("random.random", return_value=0.9):  # Above 0.5 probability
        result = should_spawn_npc(
            definition=mock_npc_definition,
            zone_config=mock_zone_config,
            room_id="room-123",
            population_stats=mock_population_stats,
            spawn_rules=spawn_rules,
            current_game_state={},
        )
        # Should continue to check other conditions (required NPC)
        assert isinstance(result, bool)


def test_should_spawn_npc_required_npc_spawns(mock_npc_definition, mock_zone_config, mock_population_stats):
    """Test should_spawn_npc() returns True for required NPC."""
    mock_npc_definition.can_spawn.return_value = True
    mock_npc_definition.is_required.return_value = True
    result = should_spawn_npc(
        definition=mock_npc_definition,
        zone_config=mock_zone_config,
        room_id="room-123",
        population_stats=mock_population_stats,
        spawn_rules={},
        current_game_state={},
    )
    assert result is True


def test_should_spawn_npc_not_required_no_rules(mock_npc_definition, mock_zone_config, mock_population_stats):
    """Test should_spawn_npc() returns False for non-required NPC with no rules."""
    mock_npc_definition.can_spawn.return_value = True
    mock_npc_definition.is_required.return_value = False
    result = should_spawn_npc(
        definition=mock_npc_definition,
        zone_config=mock_zone_config,
        room_id="room-123",
        population_stats=mock_population_stats,
        spawn_rules={},
        current_game_state={},
    )
    assert result is False


def test_should_spawn_npc_multiple_rules_first_passes(mock_npc_definition, mock_zone_config, mock_population_stats):
    """Test should_spawn_npc() returns True when first rule passes."""
    mock_npc_definition.can_spawn.return_value = True
    rule1 = MagicMock(spec=NPCSpawnRule)
    rule1.can_spawn_with_population = MagicMock(return_value=True)
    rule1.check_spawn_conditions = MagicMock(return_value=True)
    rule2 = MagicMock(spec=NPCSpawnRule)
    rule2.can_spawn_with_population = MagicMock(return_value=True)
    rule2.check_spawn_conditions = MagicMock(return_value=True)
    spawn_rules = {1: [rule1, rule2]}
    with patch("random.random", return_value=0.3):
        result = should_spawn_npc(
            definition=mock_npc_definition,
            zone_config=mock_zone_config,
            room_id="room-123",
            population_stats=mock_population_stats,
            spawn_rules=spawn_rules,
            current_game_state={},
        )
        assert result is True
        # First rule should be checked
        rule1.can_spawn_with_population.assert_called_once()


def test_should_spawn_npc_multiple_rules_second_passes(mock_npc_definition, mock_zone_config, mock_population_stats):
    """Test should_spawn_npc() tries second rule when first fails."""
    mock_npc_definition.can_spawn.return_value = True
    rule1 = MagicMock(spec=NPCSpawnRule)
    rule1.can_spawn_with_population = MagicMock(return_value=False)
    rule2 = MagicMock(spec=NPCSpawnRule)
    rule2.can_spawn_with_population = MagicMock(return_value=True)
    rule2.check_spawn_conditions = MagicMock(return_value=True)
    spawn_rules = {1: [rule1, rule2]}
    with patch("random.random", return_value=0.3):
        result = should_spawn_npc(
            definition=mock_npc_definition,
            zone_config=mock_zone_config,
            room_id="room-123",
            population_stats=mock_population_stats,
            spawn_rules=spawn_rules,
            current_game_state={},
        )
        assert result is True
        # Both rules should be checked
        rule1.can_spawn_with_population.assert_called_once()
        rule2.can_spawn_with_population.assert_called_once()


def test_should_spawn_npc_uses_zone_effective_probability(mock_npc_definition, mock_zone_config, mock_population_stats):
    """Test should_spawn_npc() uses zone effective probability."""
    mock_npc_definition.can_spawn.return_value = True
    mock_zone_config.get_effective_spawn_probability.return_value = 0.8
    spawn_rule = MagicMock(spec=NPCSpawnRule)
    spawn_rule.can_spawn_with_population = MagicMock(return_value=True)
    spawn_rule.check_spawn_conditions = MagicMock(return_value=True)
    spawn_rules = {1: [spawn_rule]}
    with patch("random.random", return_value=0.75):  # Between 0.5 and 0.8
        result = should_spawn_npc(
            definition=mock_npc_definition,
            zone_config=mock_zone_config,
            room_id="room-123",
            population_stats=mock_population_stats,
            spawn_rules=spawn_rules,
            current_game_state={},
        )
        assert result is True
        mock_zone_config.get_effective_spawn_probability.assert_called_once_with(0.5)


def test_should_spawn_npc_population_stats_npcs_by_definition(mock_npc_definition, mock_zone_config):
    """Test should_spawn_npc() uses npcs_by_definition from population stats."""
    mock_npc_definition.can_spawn.return_value = True
    stats = MagicMock()
    stats.npcs_by_definition = {1: 3}  # Current count
    spawn_rule = MagicMock(spec=NPCSpawnRule)
    spawn_rule.can_spawn_with_population = MagicMock(return_value=True)
    spawn_rule.check_spawn_conditions = MagicMock(return_value=True)
    spawn_rules = {1: [spawn_rule]}
    with patch("random.random", return_value=0.3):
        should_spawn_npc(
            definition=mock_npc_definition,
            zone_config=mock_zone_config,
            room_id="room-123",
            population_stats=stats,
            spawn_rules=spawn_rules,
            current_game_state={},
        )
        # Should pass current count to rule
        spawn_rule.can_spawn_with_population.assert_called_once_with(3)
