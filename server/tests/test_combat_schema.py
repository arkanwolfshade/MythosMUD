"""
Tests for Combat Schema Validation.

This module tests the JSON schema validation for combat data stored in
NPC definition JSON fields (base_stats and behavior_config).
"""

import pytest

from server.schemas.combat_schema import (
    DEFAULT_COMBAT_BEHAVIOR,
    DEFAULT_COMBAT_MESSAGES,
    DEFAULT_COMBAT_STATS,
    CombatSchemaValidationError,
    add_default_combat_data_to_config,
    add_default_combat_data_to_stats,
    get_combat_stats_summary,
    validate_base_stats_combat_data,
    validate_behavior_config_combat_data,
    validate_combat_messages,
    validate_message_template_variables,
    validate_npc_combat_data,
)


class TestCombatSchemaValidation:
    """Test cases for combat schema validation functions."""

    def test_validate_base_stats_combat_data_valid(self):
        """Test validation of valid base stats combat data."""
        valid_data = {
            "hp": 50,
            "max_hp": 100,
            "xp_value": 10,
            "dexterity": 12,
            "strength": 15,
            "constitution": 8,
        }

        # Should not raise any exception
        validate_base_stats_combat_data(valid_data)

    def test_validate_base_stats_combat_data_missing_required(self):
        """Test validation fails when required fields are missing."""
        invalid_data = {
            "hp": 50,
            # Missing max_hp and xp_value
        }

        with pytest.raises(CombatSchemaValidationError) as exc_info:
            validate_base_stats_combat_data(invalid_data)

        assert "Base stats combat data validation failed" in str(exc_info.value)

    def test_validate_base_stats_combat_data_invalid_hp(self):
        """Test validation fails with invalid HP values."""
        invalid_data = {
            "hp": -10,  # Negative HP
            "max_hp": 100,
            "xp_value": 10,
        }

        with pytest.raises(CombatSchemaValidationError):
            validate_base_stats_combat_data(invalid_data)

    def test_validate_base_stats_combat_data_invalid_max_hp(self):
        """Test validation fails with invalid max HP values."""
        invalid_data = {
            "hp": 50,
            "max_hp": 0,  # Zero max HP
            "xp_value": 10,
        }

        with pytest.raises(CombatSchemaValidationError):
            validate_base_stats_combat_data(invalid_data)

    def test_validate_base_stats_combat_data_invalid_xp_value(self):
        """Test validation fails with negative XP value."""
        invalid_data = {
            "hp": 50,
            "max_hp": 100,
            "xp_value": -5,  # Negative XP
        }

        with pytest.raises(CombatSchemaValidationError):
            validate_base_stats_combat_data(invalid_data)

    def test_validate_base_stats_combat_data_invalid_dexterity(self):
        """Test validation fails with invalid dexterity values."""
        invalid_data = {
            "hp": 50,
            "max_hp": 100,
            "xp_value": 10,
            "dexterity": 25,  # Too high
        }

        with pytest.raises(CombatSchemaValidationError):
            validate_base_stats_combat_data(invalid_data)

    def test_validate_base_stats_combat_data_invalid_strength(self):
        """Test validation fails with invalid strength values."""
        invalid_data = {
            "hp": 50,
            "max_hp": 100,
            "xp_value": 10,
            "strength": 0,  # Too low
        }

        with pytest.raises(CombatSchemaValidationError):
            validate_base_stats_combat_data(invalid_data)

    def test_validate_base_stats_combat_data_invalid_constitution(self):
        """Test validation fails with invalid constitution values."""
        invalid_data = {
            "hp": 50,
            "max_hp": 100,
            "xp_value": 10,
            "constitution": 21,  # Too high
        }

        with pytest.raises(CombatSchemaValidationError):
            validate_base_stats_combat_data(invalid_data)

    def test_validate_behavior_config_combat_data_valid(self):
        """Test validation of valid behavior config combat data."""
        valid_data = {
            "combat_messages": {
                "attack_attacker": "You attack {target_name} for {damage} damage",
                "attack_defender": "{attacker_name} attacks you for {damage} damage",
                "attack_other": "{attacker_name} attacks {target_name} for {damage} damage",
                "death_message": "The {npc_name} dies",
            },
            "combat_behavior": {
                "aggression_level": "aggressive",
                "retreat_threshold": 0.3,
                "combat_timeout": 300,
            },
        }

        # Should not raise any exception
        validate_behavior_config_combat_data(valid_data)

    def test_validate_behavior_config_combat_data_missing_combat_messages(self):
        """Test validation fails when combat messages are missing required fields."""
        invalid_data = {
            "combat_messages": {
                "attack_attacker": "You attack {target_name} for {damage} damage",
                # Missing other required messages
            },
        }

        with pytest.raises(CombatSchemaValidationError):
            validate_behavior_config_combat_data(invalid_data)

    def test_validate_behavior_config_combat_data_invalid_aggression_level(self):
        """Test validation fails with invalid aggression level."""
        invalid_data = {
            "combat_behavior": {
                "aggression_level": "hostile",  # Invalid value
                "retreat_threshold": 0.3,
                "combat_timeout": 300,
            },
        }

        with pytest.raises(CombatSchemaValidationError):
            validate_behavior_config_combat_data(invalid_data)

    def test_validate_behavior_config_combat_data_invalid_retreat_threshold(self):
        """Test validation fails with invalid retreat threshold."""
        invalid_data = {
            "combat_behavior": {
                "aggression_level": "passive",
                "retreat_threshold": 1.5,  # Too high
                "combat_timeout": 300,
            },
        }

        with pytest.raises(CombatSchemaValidationError):
            validate_behavior_config_combat_data(invalid_data)

    def test_validate_behavior_config_combat_data_invalid_combat_timeout(self):
        """Test validation fails with invalid combat timeout."""
        invalid_data = {
            "combat_behavior": {
                "aggression_level": "passive",
                "retreat_threshold": 0.3,
                "combat_timeout": 30,  # Too low
            },
        }

        with pytest.raises(CombatSchemaValidationError):
            validate_behavior_config_combat_data(invalid_data)

    def test_validate_combat_messages_valid(self):
        """Test validation of valid combat messages."""
        valid_messages = {
            "attack_attacker": "You attack {target_name} for {damage} damage",
            "attack_defender": "{attacker_name} attacks you for {damage} damage",
            "attack_other": "{attacker_name} attacks {target_name} for {damage} damage",
            "death_message": "The {npc_name} dies",
        }

        # Should not raise any exception
        validate_combat_messages(valid_messages)

    def test_validate_combat_messages_missing_required(self):
        """Test validation fails when required messages are missing."""
        invalid_messages = {
            "attack_attacker": "You attack {target_name} for {damage} damage",
            # Missing other required messages
        }

        with pytest.raises(CombatSchemaValidationError):
            validate_combat_messages(invalid_messages)

    def test_validate_combat_messages_empty_string(self):
        """Test validation fails with empty message strings."""
        invalid_messages = {
            "attack_attacker": "",  # Empty string
            "attack_defender": "{attacker_name} attacks you for {damage} damage",
            "attack_other": "{attacker_name} attacks {target_name} for {damage} damage",
            "death_message": "The {npc_name} dies",
        }

        with pytest.raises(CombatSchemaValidationError):
            validate_combat_messages(invalid_messages)

    def test_validate_message_template_variables_valid(self):
        """Test validation of message template variables."""
        valid_messages = {
            "attack_attacker": "You attack {target_name} for {damage} damage",
            "attack_defender": "{attacker_name} attacks you for {damage} damage",
            "attack_other": "{attacker_name} attacks {target_name} for {damage} damage",
            "death_message": "The {npc_name} dies",
        }

        # Should not raise any exception
        validate_message_template_variables(valid_messages)

    def test_validate_message_template_variables_missing_target_name(self):
        """Test validation fails when required variables are missing."""
        invalid_messages = {
            "attack_attacker": "You attack for {damage} damage",  # Missing {target_name}
            "attack_defender": "{attacker_name} attacks you for {damage} damage",
            "attack_other": "{attacker_name} attacks {target_name} for {damage} damage",
            "death_message": "The {npc_name} dies",
        }

        with pytest.raises(CombatSchemaValidationError) as exc_info:
            validate_message_template_variables(invalid_messages)

        assert "missing required variable '{target_name}'" in str(exc_info.value)

    def test_validate_message_template_variables_missing_damage(self):
        """Test validation fails when damage variable is missing."""
        invalid_messages = {
            "attack_attacker": "You attack {target_name}",  # Missing {damage}
            "attack_defender": "{attacker_name} attacks you for {damage} damage",
            "attack_other": "{attacker_name} attacks {target_name} for {damage} damage",
            "death_message": "The {npc_name} dies",
        }

        with pytest.raises(CombatSchemaValidationError) as exc_info:
            validate_message_template_variables(invalid_messages)

        assert "missing required variable '{damage}'" in str(exc_info.value)

    def test_validate_message_template_variables_missing_attacker_name(self):
        """Test validation fails when attacker_name variable is missing."""
        invalid_messages = {
            "attack_attacker": "You attack {target_name} for {damage} damage",
            "attack_defender": "attacks you for {damage} damage",  # Missing {attacker_name}
            "attack_other": "{attacker_name} attacks {target_name} for {damage} damage",
            "death_message": "The {npc_name} dies",
        }

        with pytest.raises(CombatSchemaValidationError) as exc_info:
            validate_message_template_variables(invalid_messages)

        assert "missing required variable '{attacker_name}'" in str(exc_info.value)

    def test_validate_message_template_variables_missing_npc_name(self):
        """Test validation fails when npc_name variable is missing."""
        invalid_messages = {
            "attack_attacker": "You attack {target_name} for {damage} damage",
            "attack_defender": "{attacker_name} attacks you for {damage} damage",
            "attack_other": "{attacker_name} attacks {target_name} for {damage} damage",
            "death_message": "The creature dies",  # Missing {npc_name}
        }

        with pytest.raises(CombatSchemaValidationError) as exc_info:
            validate_message_template_variables(invalid_messages)

        assert "missing required variable '{npc_name}'" in str(exc_info.value)

    def test_validate_message_template_variables_skips_missing_message_types(self):
        """Test validation skips missing message types."""
        partial_messages = {
            "attack_attacker": "You attack {target_name} for {damage} damage",
            # Missing other message types
        }

        # Should not raise any exception for missing message types
        validate_message_template_variables(partial_messages)


class TestCombatDataDefaults:
    """Test cases for default combat data functions."""

    def test_add_default_combat_data_to_stats_complete(self):
        """Test adding default combat data to complete stats."""
        stats = {
            "hp": 75,
            "max_hp": 100,
            "xp_value": 15,
            "dexterity": 12,
            "strength": 15,
            "constitution": 8,
            "custom_field": "custom_value",
        }

        result = add_default_combat_data_to_stats(stats)

        # Should not modify existing values
        assert result["hp"] == 75
        assert result["max_hp"] == 100
        assert result["xp_value"] == 15
        assert result["dexterity"] == 12
        assert result["strength"] == 15
        assert result["constitution"] == 8
        assert result["custom_field"] == "custom_value"

    def test_add_default_combat_data_to_stats_partial(self):
        """Test adding default combat data to partial stats."""
        stats = {
            "hp": 50,
            "custom_field": "custom_value",
        }

        result = add_default_combat_data_to_stats(stats)

        # Should add missing defaults
        assert result["hp"] == 50  # Existing value preserved
        assert result["max_hp"] == DEFAULT_COMBAT_STATS["max_hp"]
        assert result["xp_value"] == DEFAULT_COMBAT_STATS["xp_value"]
        assert result["dexterity"] == DEFAULT_COMBAT_STATS["dexterity"]
        assert result["strength"] == DEFAULT_COMBAT_STATS["strength"]
        assert result["constitution"] == DEFAULT_COMBAT_STATS["constitution"]
        assert result["custom_field"] == "custom_value"

    def test_add_default_combat_data_to_stats_empty(self):
        """Test adding default combat data to empty stats."""
        stats = {}

        result = add_default_combat_data_to_stats(stats)

        # Should add all defaults
        assert result == DEFAULT_COMBAT_STATS

    def test_add_default_combat_data_to_config_complete(self):
        """Test adding default combat data to complete config."""
        config = {
            "combat_messages": {
                "attack_attacker": "Custom attack message",
                "attack_defender": "Custom defender message",
                "attack_other": "Custom other message",
                "death_message": "Custom death message",
            },
            "combat_behavior": {
                "aggression_level": "aggressive",
                "retreat_threshold": 0.1,
                "combat_timeout": 600,
            },
            "custom_field": "custom_value",
        }

        result = add_default_combat_data_to_config(config)

        # Should not modify existing values
        assert result["combat_messages"]["attack_attacker"] == "Custom attack message"
        assert result["combat_behavior"]["aggression_level"] == "aggressive"
        assert result["custom_field"] == "custom_value"

    def test_add_default_combat_data_to_config_partial(self):
        """Test adding default combat data to partial config."""
        config = {
            "combat_messages": {
                "attack_attacker": "Custom attack message",
            },
            "custom_field": "custom_value",
        }

        result = add_default_combat_data_to_config(config)

        # Should preserve existing values and add missing sections
        assert result["combat_messages"]["attack_attacker"] == "Custom attack message"
        assert result["combat_behavior"] == DEFAULT_COMBAT_BEHAVIOR
        assert result["custom_field"] == "custom_value"

    def test_add_default_combat_data_to_config_empty(self):
        """Test adding default combat data to empty config."""
        config = {}

        result = add_default_combat_data_to_config(config)

        # Should add all defaults
        assert result["combat_messages"] == DEFAULT_COMBAT_MESSAGES
        assert result["combat_behavior"] == DEFAULT_COMBAT_BEHAVIOR


class TestNPCCombatDataValidation:
    """Test cases for NPC combat data validation."""

    def test_validate_npc_combat_data_valid(self):
        """Test validation of valid NPC combat data."""
        # Mock NPC definition
        npc_definition = Mock()
        npc_definition.name = "Test NPC"
        npc_definition.get_base_stats = lambda: {
            "hp": 50,
            "max_hp": 100,
            "xp_value": 10,
            "dexterity": 12,
            "strength": 15,
            "constitution": 8,
        }
        npc_definition.get_behavior_config = lambda: {
            "combat_messages": {
                "attack_attacker": "You attack {target_name} for {damage} damage",
                "attack_defender": "{attacker_name} attacks you for {damage} damage",
                "attack_other": "{attacker_name} attacks {target_name} for {damage} damage",
                "death_message": "The {npc_name} dies",
            },
            "combat_behavior": {
                "aggression_level": "passive",
                "retreat_threshold": 0.2,
                "combat_timeout": 300,
            },
        }

        # Should not raise any exception
        validate_npc_combat_data(npc_definition)

    def test_validate_npc_combat_data_invalid_base_stats(self):
        """Test validation fails with invalid base stats."""
        # Mock NPC definition with invalid base stats
        npc_definition = Mock()
        npc_definition.name = "Test NPC"
        npc_definition.get_base_stats = lambda: {
            "hp": -10,  # Invalid HP
            "max_hp": 100,
            "xp_value": 10,
        }
        npc_definition.get_behavior_config = lambda: {}

        with pytest.raises(CombatSchemaValidationError) as exc_info:
            validate_npc_combat_data(npc_definition)

        assert "NPC Test NPC base stats validation failed" in str(exc_info.value)

    def test_validate_npc_combat_data_invalid_behavior_config(self):
        """Test validation fails with invalid behavior config."""
        # Mock NPC definition with invalid behavior config
        npc_definition = Mock()
        npc_definition.name = "Test NPC"
        npc_definition.get_base_stats = lambda: {
            "hp": 50,
            "max_hp": 100,
            "xp_value": 10,
        }
        npc_definition.get_behavior_config = lambda: {
            "combat_behavior": {
                "aggression_level": "invalid_level",  # Invalid aggression level
            },
        }

        with pytest.raises(CombatSchemaValidationError) as exc_info:
            validate_npc_combat_data(npc_definition)

        assert "NPC Test NPC behavior config validation failed" in str(exc_info.value)

    def test_validate_npc_combat_data_invalid_combat_messages(self):
        """Test validation fails with invalid combat messages."""
        # Mock NPC definition with invalid combat messages
        npc_definition = Mock()
        npc_definition.name = "Test NPC"
        npc_definition.get_base_stats = lambda: {
            "hp": 50,
            "max_hp": 100,
            "xp_value": 10,
        }
        npc_definition.get_behavior_config = lambda: {
            "combat_messages": {
                "attack_attacker": "You attack {target_name}",  # Missing {damage}
            },
        }

        with pytest.raises(CombatSchemaValidationError) as exc_info:
            validate_npc_combat_data(npc_definition)

        assert "NPC Test NPC behavior config validation failed" in str(exc_info.value)


class TestCombatStatsSummary:
    """Test cases for combat stats summary function."""

    def test_get_combat_stats_summary_complete(self):
        """Test getting combat stats summary with complete data."""
        # Mock NPC definition
        npc_definition = Mock()
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "aggressive_mob"
        npc_definition.get_base_stats = lambda: {
            "hp": 75,
            "max_hp": 100,
            "xp_value": 15,
            "dexterity": 12,
            "strength": 15,
            "constitution": 8,
        }
        npc_definition.get_behavior_config = lambda: {
            "combat_messages": {"attack_attacker": "You attack {target_name} for {damage} damage"},
            "combat_behavior": {"aggression_level": "aggressive"},
        }

        result = get_combat_stats_summary(npc_definition)

        assert result["npc_name"] == "Test NPC"
        assert result["npc_type"] == "aggressive_mob"
        assert result["combat_stats"]["hp"] == 75
        assert result["combat_stats"]["max_hp"] == 100
        assert result["combat_stats"]["xp_value"] == 15
        assert result["combat_stats"]["dexterity"] == 12
        assert result["combat_stats"]["strength"] == 15
        assert result["combat_stats"]["constitution"] == 8
        assert result["has_combat_messages"] is True
        assert result["has_combat_behavior"] is True

    def test_get_combat_stats_summary_partial(self):
        """Test getting combat stats summary with partial data."""
        # Mock NPC definition with partial data
        npc_definition = Mock()
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "passive_mob"
        npc_definition.get_base_stats = lambda: {
            "hp": 50,
            "max_hp": 50,
            "xp_value": 5,
        }
        npc_definition.get_behavior_config = lambda: {}

        result = get_combat_stats_summary(npc_definition)

        assert result["npc_name"] == "Test NPC"
        assert result["npc_type"] == "passive_mob"
        assert result["combat_stats"]["hp"] == 50
        assert result["combat_stats"]["max_hp"] == 50
        assert result["combat_stats"]["xp_value"] == 5
        assert result["combat_stats"]["dexterity"] == 10  # Default value
        assert result["combat_stats"]["strength"] == 10  # Default value
        assert result["combat_stats"]["constitution"] == 8  # Default value
        assert result["has_combat_messages"] is False
        assert result["has_combat_behavior"] is False

    def test_get_combat_stats_summary_empty(self):
        """Test getting combat stats summary with empty data."""
        # Mock NPC definition with empty data
        npc_definition = Mock()
        npc_definition.name = "Test NPC"
        npc_definition.npc_type = "neutral_mob"
        npc_definition.get_base_stats = lambda: {}
        npc_definition.get_behavior_config = lambda: {}

        result = get_combat_stats_summary(npc_definition)

        assert result["npc_name"] == "Test NPC"
        assert result["npc_type"] == "neutral_mob"
        assert result["combat_stats"]["hp"] == 0  # Default value
        assert result["combat_stats"]["max_hp"] == 0  # Default value
        assert result["combat_stats"]["xp_value"] == 0  # Default value
        assert result["combat_stats"]["dexterity"] == 10  # Default value
        assert result["combat_stats"]["strength"] == 10  # Default value
        assert result["combat_stats"]["constitution"] == 8  # Default value
        assert result["has_combat_messages"] is False
        assert result["has_combat_behavior"] is False


# Mock class for testing
class Mock:
    """Simple mock class for testing."""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __call__(self, *args, **kwargs):
        return Mock()

    def __getattr__(self, name):
        return Mock()

    def __contains__(self, key):
        return hasattr(self, key) or key in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def get(self, key, default=None):
        return getattr(self, key, default)

    def __getitem__(self, key):
        return getattr(self, key, Mock())

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()
