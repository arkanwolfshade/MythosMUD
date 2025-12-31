"""
Unit tests for combat_schema validation functions.

Tests the validation functions in combat_schema.py module.
"""

from unittest.mock import MagicMock

import pytest

from server.schemas.combat_schema import (
    CombatSchemaValidationError,
    add_default_combat_data_to_config,
    add_default_combat_data_to_stats,
    get_combat_stats_summary,
    validate_base_stats_combat_data,
    validate_behavior_config_combat_data,
    validate_combat_messages,
    validate_npc_combat_data,
)


def test_validate_base_stats_combat_data_valid():
    """Test validate_base_stats_combat_data() accepts valid data."""
    data = {
        "determination_points": 20,
        "max_dp": 20,
        "xp_value": 10,
    }

    # Should not raise
    validate_base_stats_combat_data(data)


def test_validate_base_stats_combat_data_missing_required():
    """Test validate_base_stats_combat_data() raises error for missing required fields."""
    data = {
        "determination_points": 20,
        # Missing max_dp and xp_value
    }

    with pytest.raises(CombatSchemaValidationError):
        validate_base_stats_combat_data(data)


def test_validate_base_stats_combat_data_invalid_type():
    """Test validate_base_stats_combat_data() raises error for invalid type."""
    data = {
        "determination_points": "invalid",
        "max_dp": 20,
        "xp_value": 10,
    }

    with pytest.raises(CombatSchemaValidationError):
        validate_base_stats_combat_data(data)


def test_validate_behavior_config_combat_data_valid():
    """Test validate_behavior_config_combat_data() accepts valid data."""
    data = {
        "combat_messages": {
            "attack_attacker": "You attack {target_name} for {damage} damage",
            "attack_defender": "{attacker_name} attacks you for {damage} damage",
            "attack_other": "{attacker_name} attacks {target_name} for {damage} damage",
            "death_message": "The {npc_name} dies",
        },
    }

    # Should not raise
    validate_behavior_config_combat_data(data)


def test_validate_combat_messages_valid():
    """Test validate_combat_messages() accepts valid messages."""
    messages = {
        "attack_attacker": "You attack {target_name} for {damage} damage",
        "attack_defender": "{attacker_name} attacks you for {damage} damage",
        "attack_other": "{attacker_name} attacks {target_name} for {damage} damage",
        "death_message": "The {npc_name} dies",
    }

    # Should not raise
    validate_combat_messages(messages)


def test_validate_combat_messages_missing_required():
    """Test validate_combat_messages() raises error for missing required fields."""
    messages = {
        "attack_attacker": "You attack {target_name} for {damage} damage",
        # Missing attack_defender, attack_other, death_message
    }

    with pytest.raises(CombatSchemaValidationError):
        validate_combat_messages(messages)


def test_add_default_combat_data_to_stats():
    """Test add_default_combat_data_to_stats() adds defaults."""
    stats = {
        "strength": 50,
    }

    result = add_default_combat_data_to_stats(stats)

    assert "determination_points" in result
    assert "max_dp" in result
    assert "xp_value" in result


def test_add_default_combat_data_to_stats_preserves_existing():
    """Test add_default_combat_data_to_stats() preserves existing values."""
    stats = {
        "determination_points": 25,
        "max_dp": 30,
    }

    result = add_default_combat_data_to_stats(stats)

    assert result["determination_points"] == 25
    assert result["max_dp"] == 30


def test_add_default_combat_data_to_config():
    """Test add_default_combat_data_to_config() adds defaults."""
    config = {}

    result = add_default_combat_data_to_config(config)

    assert "combat_messages" in result
    assert "attack_attacker" in result["combat_messages"]
    assert "combat_behavior" in result


def test_validate_npc_combat_data():
    """Test validate_npc_combat_data() validates NPC definition."""
    npc_definition = MagicMock()
    npc_definition.name = "TestNPC"
    npc_definition.get_base_stats.return_value = {
        "determination_points": 20,
        "max_dp": 20,
        "xp_value": 10,
    }
    npc_definition.get_behavior_config.return_value = {
        "combat_messages": {
            "attack_attacker": "You attack {target_name} for {damage} damage",
            "attack_defender": "{attacker_name} attacks you for {damage} damage",
            "attack_other": "{attacker_name} attacks {target_name} for {damage} damage",
            "death_message": "The {npc_name} dies",
        },
    }

    # Should not raise
    validate_npc_combat_data(npc_definition)


def test_get_combat_stats_summary():
    """Test get_combat_stats_summary() returns summary."""
    npc_definition = MagicMock()
    npc_definition.name = "TestNPC"
    npc_definition.npc_type = "aggressive"
    npc_definition.get_base_stats.return_value = {
        "determination_points": 20,
        "max_dp": 20,
        "xp_value": 10,
        "strength": 50,
    }
    npc_definition.get_behavior_config.return_value = {}

    result = get_combat_stats_summary(npc_definition)

    assert "combat_stats" in result
    assert "determination_points" in result["combat_stats"]
    assert "max_dp" in result["combat_stats"]
    assert "xp_value" in result["combat_stats"]
    assert "strength" in result["combat_stats"]
