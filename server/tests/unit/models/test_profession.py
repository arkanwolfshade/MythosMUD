"""
Unit tests for the Profession model.

Tests the Profession model methods including stat requirements, mechanical effects, and validation.
"""

import json
from typing import Any

from server.models.profession import Profession


def test_profession_repr() -> None:
    """Test __repr__ returns expected string format."""
    profession = Profession()
    profession.id = 1
    profession.name = "Investigator"
    profession.is_available = True

    repr_str = repr(profession)

    assert "Profession" in repr_str
    assert "1" in repr_str
    assert "Investigator" in repr_str
    assert "True" in repr_str or "is_available=True" in repr_str


def test_profession_get_stat_requirements_valid_json() -> None:
    """Test get_stat_requirements returns dict for valid JSON."""
    profession = Profession()
    requirements: dict[str, int] = {"strength": 10, "intelligence": 15}
    profession.stat_requirements = json.dumps(requirements)

    result = profession.get_stat_requirements()

    assert result == requirements
    assert isinstance(result, dict)


def test_profession_get_stat_requirements_invalid_json() -> None:
    """Test get_stat_requirements returns empty dict for invalid JSON."""
    profession = Profession()
    profession.stat_requirements = "invalid json"

    result = profession.get_stat_requirements()

    assert result == {}
    assert isinstance(result, dict)


def test_profession_get_stat_requirements_empty_string() -> None:
    """Test get_stat_requirements returns empty dict for empty string."""
    profession = Profession()
    profession.stat_requirements = ""

    result = profession.get_stat_requirements()

    assert result == {}


def test_profession_get_stat_requirements_none() -> None:
    """Test get_stat_requirements returns empty dict for invalid value."""
    profession = Profession()
    # Use empty string instead of None since field is non-nullable
    profession.stat_requirements = ""

    result = profession.get_stat_requirements()

    assert result == {}


def test_profession_set_stat_requirements() -> None:
    """Test set_stat_requirements stores dict as JSON string."""
    profession = Profession()
    requirements = {"strength": 10, "intelligence": 15}

    profession.set_stat_requirements(requirements)

    assert profession.stat_requirements == json.dumps(requirements)
    assert profession.get_stat_requirements() == requirements


def test_profession_set_stat_requirements_empty_dict() -> None:
    """Test set_stat_requirements handles empty dict."""
    profession = Profession()
    requirements: dict[str, int] = {}

    profession.set_stat_requirements(requirements)

    assert profession.stat_requirements == "{}"
    assert profession.get_stat_requirements() == {}


def test_profession_get_mechanical_effects_valid_json() -> None:
    """Test get_mechanical_effects returns dict for valid JSON."""
    profession = Profession()
    effects: dict[str, Any] = {"damage_bonus": 5, "health_bonus": 10}
    profession.mechanical_effects = json.dumps(effects)

    result = profession.get_mechanical_effects()

    assert result == effects
    assert isinstance(result, dict)


def test_profession_get_mechanical_effects_invalid_json() -> None:
    """Test get_mechanical_effects returns empty dict for invalid JSON."""
    profession = Profession()
    profession.mechanical_effects = "invalid json"

    result = profession.get_mechanical_effects()

    assert result == {}
    assert isinstance(result, dict)


def test_profession_get_mechanical_effects_empty_string() -> None:
    """Test get_mechanical_effects returns empty dict for empty string."""
    profession = Profession()
    profession.mechanical_effects = ""

    result = profession.get_mechanical_effects()

    assert result == {}


def test_profession_get_mechanical_effects_none() -> None:
    """Test get_mechanical_effects returns empty dict for invalid value."""
    profession = Profession()
    # Use empty string instead of None since field is non-nullable
    profession.mechanical_effects = ""

    result = profession.get_mechanical_effects()

    assert result == {}


def test_profession_set_mechanical_effects() -> None:
    """Test set_mechanical_effects stores dict as JSON string."""
    profession = Profession()
    effects: dict[str, Any] = {"damage_bonus": 5, "health_bonus": 10}

    profession.set_mechanical_effects(effects)

    assert profession.mechanical_effects == json.dumps(effects)
    assert profession.get_mechanical_effects() == effects


def test_profession_set_mechanical_effects_empty_dict() -> None:
    """Test set_mechanical_effects handles empty dict."""
    profession = Profession()
    effects: dict[str, Any] = {}

    profession.set_mechanical_effects(effects)

    assert profession.mechanical_effects == "{}"
    assert profession.get_mechanical_effects() == {}


def test_profession_meets_stat_requirements_all_met() -> None:
    """Test meets_stat_requirements returns True when all requirements are met."""
    profession = Profession()
    profession.stat_requirements = json.dumps({"strength": 10, "intelligence": 15})
    stats = {"strength": 12, "intelligence": 18}

    result = profession.meets_stat_requirements(stats)

    assert result is True


def test_profession_meets_stat_requirements_exact_match() -> None:
    """Test meets_stat_requirements returns True when stats exactly match requirements."""
    profession = Profession()
    profession.stat_requirements = json.dumps({"strength": 10, "intelligence": 15})
    stats = {"strength": 10, "intelligence": 15}

    result = profession.meets_stat_requirements(stats)

    assert result is True


def test_profession_meets_stat_requirements_one_not_met() -> None:
    """Test meets_stat_requirements returns False when one requirement is not met."""
    profession = Profession()
    profession.stat_requirements = json.dumps({"strength": 10, "intelligence": 15})
    stats = {"strength": 12, "intelligence": 12}  # intelligence too low

    result = profession.meets_stat_requirements(stats)

    assert result is False


def test_profession_meets_stat_requirements_multiple_not_met() -> None:
    """Test meets_stat_requirements returns False when multiple requirements are not met."""
    profession = Profession()
    profession.stat_requirements = json.dumps({"strength": 10, "intelligence": 15, "wisdom": 12})
    stats = {"strength": 8, "intelligence": 12, "wisdom": 10}  # all too low

    result = profession.meets_stat_requirements(stats)

    assert result is False


def test_profession_meets_stat_requirements_missing_stat() -> None:
    """Test meets_stat_requirements returns False when required stat is missing."""
    profession = Profession()
    profession.stat_requirements = json.dumps({"strength": 10, "intelligence": 15})
    stats = {"strength": 12}  # missing intelligence

    result = profession.meets_stat_requirements(stats)

    assert result is False


def test_profession_meets_stat_requirements_empty_requirements() -> None:
    """Test meets_stat_requirements returns True when requirements are empty."""
    profession = Profession()
    profession.stat_requirements = json.dumps({})
    stats = {"strength": 5}

    result = profession.meets_stat_requirements(stats)

    assert result is True


def test_profession_meets_stat_requirements_invalid_json() -> None:
    """Test meets_stat_requirements returns True when stat_requirements is invalid JSON (treated as empty)."""
    profession = Profession()
    profession.stat_requirements = "invalid json"
    stats = {"strength": 10}

    result = profession.meets_stat_requirements(stats)

    # Invalid JSON is treated as empty requirements, so any stats meet the requirements
    assert result is True


def test_profession_meets_stat_requirements_extra_stats() -> None:
    """Test meets_stat_requirements returns True when stats exceed requirements."""
    profession = Profession()
    profession.stat_requirements = json.dumps({"strength": 10})
    stats = {"strength": 15, "intelligence": 20, "wisdom": 18}  # extra stats don't matter

    result = profession.meets_stat_requirements(stats)

    assert result is True


def test_profession_is_available_for_selection_true() -> None:
    """Test is_available_for_selection returns True when is_available is True."""
    profession = Profession()
    profession.is_available = True

    result = profession.is_available_for_selection()

    assert result is True


def test_profession_is_available_for_selection_false() -> None:
    """Test is_available_for_selection returns False when is_available is False."""
    profession = Profession()
    profession.is_available = False

    result = profession.is_available_for_selection()

    assert result is False


def test_profession_get_requirement_display_text_no_requirements() -> None:
    """Test get_requirement_display_text returns 'No requirements' when empty."""
    profession = Profession()
    profession.stat_requirements = json.dumps({})

    result = profession.get_requirement_display_text()

    assert result == "No requirements"


def test_profession_get_requirement_display_text_single_requirement() -> None:
    """Test get_requirement_display_text formats single requirement correctly."""
    profession = Profession()
    profession.stat_requirements = json.dumps({"strength": 10})

    result = profession.get_requirement_display_text()

    assert result == "Minimum: Strength 10"


def test_profession_get_requirement_display_text_multiple_requirements() -> None:
    """Test get_requirement_display_text formats multiple requirements correctly."""
    profession = Profession()
    profession.stat_requirements = json.dumps({"strength": 10, "intelligence": 15, "wisdom": 12})

    result = profession.get_requirement_display_text()

    assert "Minimum:" in result
    assert "Strength 10" in result
    assert "Intelligence 15" in result
    assert "Wisdom 12" in result
    # Check format: should have commas between requirements
    assert result.count(",") == 2


def test_profession_get_requirement_display_text_capitalizes_stat_names() -> None:
    """Test get_requirement_display_text capitalizes stat names."""
    profession = Profession()
    profession.stat_requirements = json.dumps({"strength": 10, "dexterity": 12})

    result = profession.get_requirement_display_text()

    assert "Strength" in result
    assert "Dexterity" in result
    assert "strength" not in result  # Should be capitalized
    assert "dexterity" not in result  # Should be capitalized
