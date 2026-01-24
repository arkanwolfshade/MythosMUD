"""
Unit tests for NPC models.

Tests the NPCDefinitionType enum and NPCDefinition, NPCSpawnRule, NPCRelationship SQLAlchemy models.
"""

from server.models.npc import (
    NPCDefinition,
    NPCDefinitionType,
    NPCRelationship,
    NPCSpawnRule,
)

# --- Tests for NPCDefinitionType enum ---


def test_npc_definition_type_enum_values() -> None:
    """Test NPCDefinitionType enum contains expected values."""
    assert NPCDefinitionType.SHOPKEEPER.value == "shopkeeper"
    assert NPCDefinitionType.QUEST_GIVER.value == "quest_giver"
    assert NPCDefinitionType.PASSIVE_MOB.value == "passive_mob"
    assert NPCDefinitionType.AGGRESSIVE_MOB.value == "aggressive_mob"


def test_npc_definition_type_enum_all_types() -> None:
    """Test NPCDefinitionType enum contains all expected types."""
    expected_types = {"shopkeeper", "quest_giver", "passive_mob", "aggressive_mob"}
    actual_types = {t.value for t in NPCDefinitionType}
    assert actual_types == expected_types


# --- Tests for NPCDefinition model ---


def test_npc_definition_creation() -> None:
    """Test NPCDefinition can be instantiated with required fields."""
    npc = NPCDefinition(
        name="Test NPC",
        npc_type="shopkeeper",
        sub_zone_id="subzone_001",
        base_stats="{}",
        behavior_config="{}",
        ai_integration_stub="{}",
    )

    assert npc.name == "Test NPC"
    assert npc.npc_type == "shopkeeper"
    assert npc.sub_zone_id == "subzone_001"
    assert npc.base_stats == "{}"
    assert npc.behavior_config == "{}"
    assert npc.ai_integration_stub == "{}"


def test_npc_definition_defaults() -> None:
    """Test NPCDefinition has correct default values."""
    npc = NPCDefinition(
        name="Test NPC",
        npc_type="passive_mob",
        sub_zone_id="subzone_001",
    )

    # SQLAlchemy defaults are applied on DB save, not object instantiation
    # With Mapped types, non-nullable fields have default values applied
    assert npc.required_npc is False
    assert npc.max_population == 1
    assert npc.spawn_probability == 1.0
    assert npc.base_stats == "{}"
    assert npc.behavior_config == "{}"
    assert npc.ai_integration_stub == "{}"


def test_npc_definition_get_base_stats() -> None:
    """Test NPCDefinition.get_base_stats() parses JSON."""
    npc = NPCDefinition(
        name="Test NPC",
        npc_type="aggressive_mob",
        sub_zone_id="subzone_001",
        base_stats='{"strength": 50, "dexterity": 40}',
    )

    stats = npc.get_base_stats()

    assert stats == {"strength": 50, "dexterity": 40}


def test_npc_definition_get_base_stats_empty() -> None:
    """Test NPCDefinition.get_base_stats() handles empty JSON."""
    npc = NPCDefinition(
        name="Test NPC",
        npc_type="passive_mob",
        sub_zone_id="subzone_001",
        base_stats="{}",
    )

    stats = npc.get_base_stats()

    assert stats == {}


def test_npc_definition_set_base_stats() -> None:
    """Test NPCDefinition.set_base_stats() serializes to JSON."""
    npc = NPCDefinition(
        name="Test NPC",
        npc_type="shopkeeper",
        sub_zone_id="subzone_001",
    )

    npc.set_base_stats({"strength": 60, "constitution": 50})

    assert npc.base_stats == '{"strength": 60, "constitution": 50}'


def test_npc_definition_get_behavior_config() -> None:
    """Test NPCDefinition.get_behavior_config() parses JSON."""
    npc = NPCDefinition(
        name="Test NPC",
        npc_type="aggressive_mob",
        sub_zone_id="subzone_001",
        behavior_config='{"aggression_level": 8, "wander_range": 3}',
    )

    config = npc.get_behavior_config()

    assert config == {"aggression_level": 8, "wander_range": 3}


def test_npc_definition_set_behavior_config() -> None:
    """Test NPCDefinition.set_behavior_config() serializes to JSON."""
    npc = NPCDefinition(
        name="Test NPC",
        npc_type="aggressive_mob",
        sub_zone_id="subzone_001",
    )

    npc.set_behavior_config({"aggression_level": 5})

    assert npc.behavior_config == '{"aggression_level": 5}'


def test_npc_definition_get_ai_integration_stub() -> None:
    """Test NPCDefinition.get_ai_integration_stub() parses JSON."""
    npc = NPCDefinition(
        name="Test NPC",
        npc_type="quest_giver",
        sub_zone_id="subzone_001",
        ai_integration_stub='{"model": "gpt-4", "temperature": 0.7}',
    )

    stub = npc.get_ai_integration_stub()

    assert stub == {"model": "gpt-4", "temperature": 0.7}


def test_npc_definition_set_ai_integration_stub() -> None:
    """Test NPCDefinition.set_ai_integration_stub() serializes to JSON."""
    npc = NPCDefinition(
        name="Test NPC",
        npc_type="quest_giver",
        sub_zone_id="subzone_001",
    )

    npc.set_ai_integration_stub({"model": "gpt-3.5"})

    assert npc.ai_integration_stub == '{"model": "gpt-3.5"}'


def test_npc_definition_is_required() -> None:
    """Test NPCDefinition.is_required() returns correct value."""
    npc1 = NPCDefinition(
        name="Required NPC",
        npc_type="shopkeeper",
        sub_zone_id="subzone_001",
        required_npc=True,
    )
    assert npc1.is_required() is True

    npc2 = NPCDefinition(
        name="Optional NPC",
        npc_type="passive_mob",
        sub_zone_id="subzone_001",
        required_npc=False,
    )
    assert npc2.is_required() is False


def test_npc_definition_can_spawn() -> None:
    """Test NPCDefinition.can_spawn() checks population limits."""
    npc = NPCDefinition(
        name="Test NPC",
        npc_type="passive_mob",
        sub_zone_id="subzone_001",
        max_population=3,
    )

    assert npc.can_spawn(current_population=0) is True
    assert npc.can_spawn(current_population=2) is True
    assert npc.can_spawn(current_population=3) is False
    assert npc.can_spawn(current_population=4) is False


def test_npc_definition_table_name() -> None:
    """Test NPCDefinition has correct table name."""
    assert NPCDefinition.__tablename__ == "npc_definitions"


def test_npc_definition_repr() -> None:
    """Test NPCDefinition __repr__ method."""
    npc = NPCDefinition(
        name="Test NPC",
        npc_type="shopkeeper",
        sub_zone_id="subzone_001",
    )

    repr_str = repr(npc)
    assert "NPCDefinition" in repr_str
    assert "Test NPC" in repr_str


# --- Tests for NPCSpawnRule model ---


def test_npc_spawn_rule_creation() -> None:
    """Test NPCSpawnRule can be instantiated with required fields."""
    rule = NPCSpawnRule(
        npc_definition_id=1,
        spawn_conditions='{"time_of_day": "night", "weather": "foggy"}',
        max_population=5,
    )

    assert rule.npc_definition_id == 1
    assert rule.spawn_conditions == '{"time_of_day": "night", "weather": "foggy"}'
    assert rule.max_population == 5


def test_npc_spawn_rule_get_spawn_conditions() -> None:
    """Test NPCSpawnRule.get_spawn_conditions() parses JSON."""
    rule = NPCSpawnRule(
        npc_definition_id=1,
        spawn_conditions='{"time_of_day": "night", "weather": "foggy"}',
        max_population=5,
    )

    conditions = rule.get_spawn_conditions()

    assert conditions == {"time_of_day": "night", "weather": "foggy"}


def test_npc_spawn_rule_set_spawn_conditions() -> None:
    """Test NPCSpawnRule.set_spawn_conditions() serializes to JSON."""
    rule = NPCSpawnRule(
        npc_definition_id=1,
        spawn_conditions="{}",
        max_population=5,
    )

    rule.set_spawn_conditions({"time_of_day": "day", "season": "winter"})

    assert rule.spawn_conditions == '{"time_of_day": "day", "season": "winter"}'


def test_npc_spawn_rule_can_spawn_with_population() -> None:
    """Test NPCSpawnRule.can_spawn_with_population() checks population limits."""
    rule = NPCSpawnRule(
        npc_definition_id=1,
        spawn_conditions="{}",
        max_population=3,
    )

    assert rule.can_spawn_with_population(current_population=0) is True
    assert rule.can_spawn_with_population(current_population=2) is True
    assert rule.can_spawn_with_population(current_population=3) is False
    assert rule.can_spawn_with_population(current_population=4) is False


def test_npc_spawn_rule_check_spawn_conditions() -> None:
    """Test NPCSpawnRule.check_spawn_conditions() validates game state."""
    rule = NPCSpawnRule(
        npc_definition_id=1,
        spawn_conditions='{"time_of_day": "night"}',
        max_population=5,
    )

    game_state1 = {"time_of_day": "night", "weather": "clear"}
    assert rule.check_spawn_conditions(game_state1) is True

    game_state2 = {"time_of_day": "day", "weather": "clear"}
    assert rule.check_spawn_conditions(game_state2) is False


def test_npc_spawn_rule_check_spawn_conditions_multiple() -> None:
    """Test NPCSpawnRule.check_spawn_conditions() validates multiple conditions."""
    rule = NPCSpawnRule(
        npc_definition_id=1,
        spawn_conditions='{"time_of_day": "night", "weather": "foggy"}',
        max_population=5,
    )

    game_state1 = {"time_of_day": "night", "weather": "foggy"}
    assert rule.check_spawn_conditions(game_state1) is True

    game_state2 = {"time_of_day": "night", "weather": "clear"}
    assert rule.check_spawn_conditions(game_state2) is False

    game_state3 = {"time_of_day": "day", "weather": "foggy"}
    assert rule.check_spawn_conditions(game_state3) is False


def test_npc_spawn_rule_table_name() -> None:
    """Test NPCSpawnRule has correct table name."""
    assert NPCSpawnRule.__tablename__ == "npc_spawn_rules"


def test_npc_spawn_rule_repr() -> None:
    """Test NPCSpawnRule __repr__ method."""
    rule = NPCSpawnRule(
        npc_definition_id=1,
        spawn_conditions="{}",
        max_population=5,
    )

    repr_str = repr(rule)
    assert "NPCSpawnRule" in repr_str


# --- Tests for NPCRelationship model ---


def test_npc_relationship_creation() -> None:
    """Test NPCRelationship can be instantiated with required fields."""
    relationship = NPCRelationship(
        npc_id_1=1,
        npc_id_2=2,
        relationship_type="ally",
        relationship_strength=0.5,
    )

    assert relationship.npc_id_1 == 1
    assert relationship.npc_id_2 == 2
    assert relationship.relationship_type == "ally"
    assert relationship.relationship_strength == 0.5


def test_npc_relationship_table_name() -> None:
    """Test NPCRelationship has correct table name."""
    assert NPCRelationship.__tablename__ == "npc_relationships"


def test_npc_relationship_repr() -> None:
    """Test NPCRelationship __repr__ method."""
    relationship = NPCRelationship(
        npc_id_1=1,
        npc_id_2=2,
        relationship_type="enemy",
        relationship_strength=0.3,
    )

    repr_str = repr(relationship)
    assert "NPCRelationship" in repr_str


def test_npc_relationship_different_types() -> None:
    """Test NPCRelationship can have different relationship types."""
    relationship1 = NPCRelationship(
        npc_id_1=1,
        npc_id_2=2,
        relationship_type="ally",
        relationship_strength=0.8,
    )
    relationship2 = NPCRelationship(
        npc_id_1=1,
        npc_id_2=3,
        relationship_type="enemy",
        relationship_strength=0.2,
    )

    assert relationship1.relationship_type != relationship2.relationship_type
    assert relationship1.relationship_strength != relationship2.relationship_strength
