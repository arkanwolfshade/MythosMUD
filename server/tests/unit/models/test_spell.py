"""
Unit tests for spell models.

Tests the Spell, SpellMaterial models and related enums.
"""

import pytest
from pydantic import ValidationError

from server.models.spell import (
    Spell,
    SpellEffectType,
    SpellMaterial,
    SpellRangeType,
    SpellSchool,
    SpellTargetType,
)

# --- Tests for SpellSchool enum ---


def test_spell_school_enum_values():
    """Test SpellSchool enum contains expected values."""
    assert SpellSchool.MYTHOS.value == "mythos"
    assert SpellSchool.CLERICAL.value == "clerical"
    assert SpellSchool.ELEMENTAL.value == "elemental"
    assert SpellSchool.OTHER.value == "other"


def test_spell_school_enum_all_schools():
    """Test SpellSchool enum contains all expected schools."""
    expected_schools = {"mythos", "clerical", "elemental", "other"}
    actual_schools = {s.value for s in SpellSchool}
    assert actual_schools == expected_schools


# --- Tests for SpellTargetType enum ---


def test_spell_target_type_enum_values():
    """Test SpellTargetType enum contains expected values."""
    assert SpellTargetType.SELF.value == "self"
    assert SpellTargetType.ENTITY.value == "entity"
    assert SpellTargetType.LOCATION.value == "location"
    assert SpellTargetType.AREA.value == "area"
    assert SpellTargetType.ALL.value == "all"


def test_spell_target_type_enum_all_types():
    """Test SpellTargetType enum contains all expected types."""
    expected_types = {"self", "entity", "location", "area", "all"}
    actual_types = {t.value for t in SpellTargetType}
    assert actual_types == expected_types


# --- Tests for SpellRangeType enum ---


def test_spell_range_type_enum_values():
    """Test SpellRangeType enum contains expected values."""
    assert SpellRangeType.TOUCH.value == "touch"
    assert SpellRangeType.SAME_ROOM.value == "same_room"
    assert SpellRangeType.ADJACENT_ROOM.value == "adjacent_room"
    assert SpellRangeType.UNLIMITED.value == "unlimited"


def test_spell_range_type_enum_all_types():
    """Test SpellRangeType enum contains all expected types."""
    expected_types = {"touch", "same_room", "adjacent_room", "unlimited"}
    actual_types = {t.value for t in SpellRangeType}
    assert actual_types == expected_types


# --- Tests for SpellEffectType enum ---


def test_spell_effect_type_enum_values():
    """Test SpellEffectType enum contains expected values."""
    assert SpellEffectType.HEAL.value == "heal"
    assert SpellEffectType.DAMAGE.value == "damage"
    assert SpellEffectType.STATUS_EFFECT.value == "status_effect"
    assert SpellEffectType.STAT_MODIFY.value == "stat_modify"
    assert SpellEffectType.LUCIDITY_ADJUST.value == "lucidity_adjust"
    assert SpellEffectType.CORRUPTION_ADJUST.value == "corruption_adjust"
    assert SpellEffectType.TELEPORT.value == "teleport"
    assert SpellEffectType.CREATE_OBJECT.value == "create_object"


def test_spell_effect_type_enum_all_types():
    """Test SpellEffectType enum contains all expected types."""
    expected_types = {
        "heal",
        "damage",
        "status_effect",
        "stat_modify",
        "lucidity_adjust",
        "corruption_adjust",
        "teleport",
        "create_object",
    }
    actual_types = {t.value for t in SpellEffectType}
    assert actual_types == expected_types


# --- Tests for SpellMaterial model ---


def test_spell_material_creation():
    """Test SpellMaterial can be created with required fields."""
    material = SpellMaterial(item_id="test_item_123")

    assert material.item_id == "test_item_123"
    assert material.consumed is True  # Default value


def test_spell_material_consumed_default():
    """Test SpellMaterial defaults consumed to True."""
    material = SpellMaterial(item_id="test_item")

    assert material.consumed is True


def test_spell_material_consumed_false():
    """Test SpellMaterial can have consumed set to False."""
    material = SpellMaterial(item_id="test_item", consumed=False)

    assert material.consumed is False


def test_spell_material_consumed_true():
    """Test SpellMaterial can have consumed set to True explicitly."""
    material = SpellMaterial(item_id="test_item", consumed=True)

    assert material.consumed is True


# --- Tests for Spell model methods ---


def test_spell_is_mythos_true():
    """Test is_mythos returns True for Mythos spells."""
    spell = Spell(
        spell_id="test_spell",
        name="Test Spell",
        description="A test spell",
        school=SpellSchool.MYTHOS,
        mp_cost=10,
        target_type=SpellTargetType.SELF,
        range_type=SpellRangeType.TOUCH,
        effect_type=SpellEffectType.HEAL,
    )

    assert spell.is_mythos() is True


def test_spell_is_mythos_false():
    """Test is_mythos returns False for non-Mythos spells."""
    spell = Spell(
        spell_id="test_spell",
        name="Test Spell",
        description="A test spell",
        school=SpellSchool.CLERICAL,
        mp_cost=10,
        target_type=SpellTargetType.SELF,
        range_type=SpellRangeType.TOUCH,
        effect_type=SpellEffectType.HEAL,
    )

    assert spell.is_mythos() is False


def test_spell_requires_lucidity_true():
    """Test requires_lucidity returns True when lucidity_cost > 0."""
    spell = Spell(
        spell_id="test_spell",
        name="Test Spell",
        description="A test spell",
        school=SpellSchool.MYTHOS,
        mp_cost=10,
        lucidity_cost=5,
        target_type=SpellTargetType.SELF,
        range_type=SpellRangeType.TOUCH,
        effect_type=SpellEffectType.HEAL,
    )

    assert spell.requires_lucidity() is True


def test_spell_requires_lucidity_false_zero():
    """Test requires_lucidity returns False when lucidity_cost is 0."""
    spell = Spell(
        spell_id="test_spell",
        name="Test Spell",
        description="A test spell",
        school=SpellSchool.MYTHOS,
        mp_cost=10,
        lucidity_cost=0,
        target_type=SpellTargetType.SELF,
        range_type=SpellRangeType.TOUCH,
        effect_type=SpellEffectType.HEAL,
    )

    assert spell.requires_lucidity() is False


def test_spell_requires_lucidity_false_default():
    """Test requires_lucidity returns False when lucidity_cost uses default (0)."""
    spell = Spell(
        spell_id="test_spell",
        name="Test Spell",
        description="A test spell",
        school=SpellSchool.CLERICAL,
        mp_cost=10,
        # lucidity_cost defaults to 0
        target_type=SpellTargetType.SELF,
        range_type=SpellRangeType.TOUCH,
        effect_type=SpellEffectType.HEAL,
    )

    assert spell.requires_lucidity() is False


def test_spell_default_values():
    """Test Spell has correct default values."""
    spell = Spell(
        spell_id="test_spell",
        name="Test Spell",
        description="A test spell",
        school=SpellSchool.CLERICAL,
        mp_cost=10,
        target_type=SpellTargetType.SELF,
        range_type=SpellRangeType.TOUCH,
        effect_type=SpellEffectType.HEAL,
    )

    assert spell.lucidity_cost == 0
    assert spell.corruption_on_learn == 0
    assert spell.corruption_on_cast == 0
    assert spell.casting_time_seconds == 0
    assert spell.effect_data == {}
    assert spell.materials == []


def test_spell_mp_cost_validation_negative():
    """Test Spell validates mp_cost is non-negative."""
    with pytest.raises(ValidationError):
        Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.CLERICAL,
            mp_cost=-1,  # Invalid: negative
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
        )


def test_spell_lucidity_cost_validation_negative():
    """Test Spell validates lucidity_cost is non-negative."""
    with pytest.raises(ValidationError):
        Spell(
            spell_id="test_spell",
            name="Test Spell",
            description="A test spell",
            school=SpellSchool.MYTHOS,
            mp_cost=10,
            lucidity_cost=-1,  # Invalid: negative
            target_type=SpellTargetType.SELF,
            range_type=SpellRangeType.TOUCH,
            effect_type=SpellEffectType.HEAL,
        )


def test_spell_with_materials():
    """Test Spell can have material components."""
    material1 = SpellMaterial(item_id="item1", consumed=True)
    material2 = SpellMaterial(item_id="item2", consumed=False)

    spell = Spell(
        spell_id="test_spell",
        name="Test Spell",
        description="A test spell",
        school=SpellSchool.CLERICAL,
        mp_cost=10,
        target_type=SpellTargetType.SELF,
        range_type=SpellRangeType.TOUCH,
        effect_type=SpellEffectType.HEAL,
        materials=[material1, material2],
    )

    assert len(spell.materials) == 2
    assert spell.materials[0].item_id == "item1"
    assert spell.materials[1].item_id == "item2"


def test_spell_with_effect_data():
    """Test Spell can have effect_data dictionary."""
    spell = Spell(
        spell_id="test_spell",
        name="Test Spell",
        description="A test spell",
        school=SpellSchool.CLERICAL,
        mp_cost=10,
        target_type=SpellTargetType.SELF,
        range_type=SpellRangeType.TOUCH,
        effect_type=SpellEffectType.HEAL,
        effect_data={"amount": 50, "type": "hp"},
    )

    assert spell.effect_data == {"amount": 50, "type": "hp"}
