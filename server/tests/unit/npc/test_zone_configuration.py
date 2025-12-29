"""
Unit tests for zone configuration.

Tests the ZoneConfiguration class.
"""


from server.npc.zone_configuration import ZoneConfiguration


def test_zone_configuration_init_minimal():
    """Test ZoneConfiguration initialization with minimal data."""
    config_data = {}
    config = ZoneConfiguration(config_data)
    assert config.zone_type is None
    assert config.environment == "outdoors"
    assert config.description == ""
    assert config.weather_patterns == []
    assert config.special_rules == {}
    assert config.npc_spawn_modifier == 1.0
    assert config.lucidity_drain_rate == 0.0
    assert config.combat_modifier == 1.0
    assert config.exploration_bonus == 0.0
    assert config.access_requirements == []


def test_zone_configuration_init_full():
    """Test ZoneConfiguration initialization with full data."""
    config_data = {
        "zone_type": "urban",
        "environment": "indoors",
        "description": "A dark alley",
        "weather_patterns": ["fog", "rain"],
        "special_rules": {
            "npc_spawn_modifier": 1.5,
            "lucidity_drain_rate": 0.1,
            "combat_modifier": 1.2,
            "exploration_bonus": 0.5,
            "access_requirements": ["key", "permission"],
        },
    }
    config = ZoneConfiguration(config_data)
    assert config.zone_type == "urban"
    assert config.environment == "indoors"
    assert config.description == "A dark alley"
    assert config.weather_patterns == ["fog", "rain"]
    assert config.npc_spawn_modifier == 1.5
    assert config.lucidity_drain_rate == 0.1
    assert config.combat_modifier == 1.2
    assert config.exploration_bonus == 0.5
    assert config.access_requirements == ["key", "permission"]


def test_zone_configuration_init_partial_special_rules():
    """Test ZoneConfiguration initialization with partial special_rules."""
    config_data = {
        "special_rules": {
            "npc_spawn_modifier": 0.8,
        },
    }
    config = ZoneConfiguration(config_data)
    assert config.npc_spawn_modifier == 0.8
    assert config.lucidity_drain_rate == 0.0  # Default
    assert config.combat_modifier == 1.0  # Default
    assert config.exploration_bonus == 0.0  # Default
    assert config.access_requirements == []  # Default


def test_get_effective_spawn_probability_no_modifier():
    """Test get_effective_spawn_probability() with no modifier."""
    config_data = {}
    config = ZoneConfiguration(config_data)
    result = config.get_effective_spawn_probability(0.5)
    assert result == 0.5


def test_get_effective_spawn_probability_with_modifier():
    """Test get_effective_spawn_probability() with modifier."""
    config_data = {"special_rules": {"npc_spawn_modifier": 1.5}}
    config = ZoneConfiguration(config_data)
    result = config.get_effective_spawn_probability(0.5)
    assert result == 0.75


def test_get_effective_spawn_probability_reduced_modifier():
    """Test get_effective_spawn_probability() with reduced modifier."""
    config_data = {"special_rules": {"npc_spawn_modifier": 0.5}}
    config = ZoneConfiguration(config_data)
    result = config.get_effective_spawn_probability(0.8)
    assert result == 0.4


def test_get_effective_spawn_probability_caps_at_one():
    """Test get_effective_spawn_probability() caps at 1.0."""
    config_data = {"special_rules": {"npc_spawn_modifier": 2.0}}
    config = ZoneConfiguration(config_data)
    result = config.get_effective_spawn_probability(0.8)
    assert result == 1.0


def test_get_effective_spawn_probability_already_one():
    """Test get_effective_spawn_probability() when already at 1.0."""
    config_data = {"special_rules": {"npc_spawn_modifier": 1.5}}
    config = ZoneConfiguration(config_data)
    result = config.get_effective_spawn_probability(1.0)
    assert result == 1.0


def test_can_access_no_requirements():
    """Test can_access() returns True when no requirements."""
    config_data = {}
    config = ZoneConfiguration(config_data)
    assert config.can_access([]) is True
    assert config.can_access(["key"]) is True


def test_can_access_with_requirements_met():
    """Test can_access() returns True when requirements are met."""
    config_data = {"special_rules": {"access_requirements": ["key", "permission"]}}
    config = ZoneConfiguration(config_data)
    player_requirements = ["key", "permission", "other"]
    assert config.can_access(player_requirements) is True


def test_can_access_with_requirements_partial():
    """Test can_access() returns True when at least one requirement is met."""
    config_data = {"special_rules": {"access_requirements": ["key", "permission"]}}
    config = ZoneConfiguration(config_data)
    player_requirements = ["key"]
    assert config.can_access(player_requirements) is True


def test_can_access_with_requirements_not_met():
    """Test can_access() returns False when requirements not met."""
    config_data = {"special_rules": {"access_requirements": ["key", "permission"]}}
    config = ZoneConfiguration(config_data)
    player_requirements = ["other"]
    assert config.can_access(player_requirements) is False


def test_can_access_empty_player_requirements():
    """Test can_access() returns False when player has no requirements."""
    config_data = {"special_rules": {"access_requirements": ["key"]}}
    config = ZoneConfiguration(config_data)
    assert config.can_access([]) is False


def test_can_access_multiple_requirements_any():
    """Test can_access() returns True if any requirement is met."""
    config_data = {"special_rules": {"access_requirements": ["key1", "key2", "key3"]}}
    config = ZoneConfiguration(config_data)
    player_requirements = ["key2"]
    assert config.can_access(player_requirements) is True


def test_zone_configuration_weather_patterns():
    """Test ZoneConfiguration handles weather_patterns correctly."""
    config_data = {"weather_patterns": ["fog", "rain", "snow"]}
    config = ZoneConfiguration(config_data)
    assert config.weather_patterns == ["fog", "rain", "snow"]


def test_zone_configuration_description():
    """Test ZoneConfiguration handles description correctly."""
    config_data = {"description": "A mysterious location"}
    config = ZoneConfiguration(config_data)
    assert config.description == "A mysterious location"


def test_zone_configuration_zone_type():
    """Test ZoneConfiguration handles zone_type correctly."""
    config_data = {"zone_type": "urban"}
    config = ZoneConfiguration(config_data)
    assert config.zone_type == "urban"


def test_zone_configuration_environment():
    """Test ZoneConfiguration handles environment correctly."""
    config_data = {"environment": "underground"}
    config = ZoneConfiguration(config_data)
    assert config.environment == "underground"


def test_get_effective_spawn_probability_zero_base():
    """Test get_effective_spawn_probability() with zero base probability."""
    config_data = {"special_rules": {"npc_spawn_modifier": 2.0}}
    config = ZoneConfiguration(config_data)
    result = config.get_effective_spawn_probability(0.0)
    assert result == 0.0


def test_get_effective_spawn_probability_very_high_modifier():
    """Test get_effective_spawn_probability() with very high modifier."""
    config_data = {"special_rules": {"npc_spawn_modifier": 10.0}}
    config = ZoneConfiguration(config_data)
    result = config.get_effective_spawn_probability(0.2)
    assert result == 1.0  # Capped at 1.0
