"""
Unit tests for game model enums.

Tests AttributeType, StatusEffectType, and PositionState enums.
"""

from server.models.game import AttributeType, PositionState, StatusEffectType

# --- Tests for AttributeType enum ---


def test_attribute_type_enum_values():
    """Test AttributeType enum contains expected values."""
    assert AttributeType.STR.value == "strength"
    assert AttributeType.DEX.value == "dexterity"
    assert AttributeType.CON.value == "constitution"
    assert AttributeType.SIZ.value == "size"
    assert AttributeType.INT.value == "intelligence"
    assert AttributeType.POW.value == "power"
    assert AttributeType.EDU.value == "education"
    assert AttributeType.CHA.value == "charisma"
    assert AttributeType.LUCK.value == "luck"
    assert AttributeType.LCD.value == "lucidity"
    assert AttributeType.OCC.value == "occult"
    assert AttributeType.CORR.value == "corruption"


def test_attribute_type_enum_all_types():
    """Test AttributeType enum contains all expected types."""
    expected_types = {
        "strength",
        "dexterity",
        "constitution",
        "size",
        "intelligence",
        "power",
        "education",
        "charisma",
        "luck",
        "lucidity",
        "occult",
        "corruption",
    }
    actual_types = {t.value for t in AttributeType}
    assert actual_types == expected_types


# --- Tests for StatusEffectType enum ---


def test_status_effect_type_enum_values():
    """Test StatusEffectType enum contains expected values."""
    assert StatusEffectType.STUNNED.value == "stunned"
    assert StatusEffectType.POISONED.value == "poisoned"
    assert StatusEffectType.HALLUCINATING.value == "hallucinating"
    assert StatusEffectType.PARANOID.value == "paranoid"
    assert StatusEffectType.TREMBLING.value == "trembling"
    assert StatusEffectType.CORRUPTED.value == "corrupted"
    assert StatusEffectType.DELIRIOUS.value == "delirious"
    assert StatusEffectType.BUFF.value == "buff"


def test_status_effect_type_enum_all_types():
    """Test StatusEffectType enum contains all expected types."""
    expected_types = {
        "stunned",
        "poisoned",
        "hallucinating",
        "paranoid",
        "trembling",
        "corrupted",
        "delirious",
        "buff",
        "login_warded",  # ADR-009 effects system
    }
    actual_types = {t.value for t in StatusEffectType}
    assert actual_types == expected_types


# --- Tests for PositionState enum ---


def test_position_state_enum_values():
    """Test PositionState enum contains expected values."""
    assert PositionState.STANDING.value == "standing"
    assert PositionState.SITTING.value == "sitting"
    assert PositionState.LYING.value == "lying"


def test_position_state_enum_all_states():
    """Test PositionState enum contains all expected states."""
    expected_states = {"standing", "sitting", "lying"}
    actual_states = {s.value for s in PositionState}
    assert actual_states == expected_states
