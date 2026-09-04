"""
Unit tests for magic command models.

Tests the CastCommand, SpellCommand, SpellsCommand, and LearnCommand models and their validators.
"""

import pytest
from pydantic import ValidationError

from server.models.command_magic import CastCommand, LearnCommand, SpellCommand, SpellsCommand

# --- Tests for CastCommand ---


def test_cast_command_required_fields():
    """Test CastCommand requires spell_name."""
    command = CastCommand(spell_name="fireball")

    assert command.command_type == "cast"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
    assert command.spell_name == "fireball"  # type: ignore[unreachable]
    assert command.target is None


def test_cast_command_with_target():
    """Test CastCommand can have optional target."""
    command = CastCommand(spell_name="heal", target="player1")

    assert command.spell_name == "heal"
    assert command.target == "player1"


def test_cast_command_validate_spell_name_valid():
    """Test CastCommand validates and strips spell_name."""
    command = CastCommand(spell_name="  fireball  ")

    assert command.spell_name == "fireball"  # Should be stripped


def test_cast_command_validate_spell_name_empty():
    """Test CastCommand rejects empty spell_name."""
    with pytest.raises(ValidationError) as exc_info:
        CastCommand(spell_name="")

    error_str = str(exc_info.value).lower()
    assert "cannot be empty" in error_str or "validation" in error_str


def test_cast_command_validate_spell_name_whitespace_only():
    """Test CastCommand rejects whitespace-only spell_name."""
    with pytest.raises(ValidationError) as exc_info:
        CastCommand(spell_name="   ")

    error_str = str(exc_info.value).lower()
    assert "cannot be empty" in error_str or "validation" in error_str


def test_cast_command_validate_target_empty_string():
    """Test CastCommand converts empty target string to None."""
    command = CastCommand(spell_name="spell", target="")

    assert command.target is None


def test_cast_command_validate_target_whitespace():
    """Test CastCommand strips whitespace from target and converts empty to None."""
    command = CastCommand(spell_name="spell", target="   ")

    assert command.target is None


def test_cast_command_validate_target_strips():
    """Test CastCommand strips whitespace from target."""
    command = CastCommand(spell_name="spell", target="  target  ")

    assert command.target == "target"


def test_cast_command_spell_name_max_length():
    """Test CastCommand validates spell_name max length."""
    long_name = "a" * 101  # Exceeds max_length=100
    with pytest.raises(ValidationError):
        CastCommand(spell_name=long_name)


def test_cast_command_target_max_length():
    """Test CastCommand validates target max length."""
    long_target = "a" * 101  # Exceeds max_length=100
    with pytest.raises(ValidationError):
        CastCommand(spell_name="spell", target=long_target)


# --- Tests for SpellCommand ---


def test_spell_command_required_fields():
    """Test SpellCommand requires spell_name."""
    command = SpellCommand(spell_name="fireball")

    assert command.command_type == "spell"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
    assert command.spell_name == "fireball"  # type: ignore[unreachable]


def test_spell_command_validate_spell_name_valid():
    """Test SpellCommand validates and strips spell_name."""
    command = SpellCommand(spell_name="  fireball  ")

    assert command.spell_name == "fireball"  # Should be stripped


def test_spell_command_validate_spell_name_empty():
    """Test SpellCommand rejects empty spell_name."""
    with pytest.raises(ValidationError) as exc_info:
        SpellCommand(spell_name="")

    error_str = str(exc_info.value).lower()
    assert "cannot be empty" in error_str or "validation" in error_str


def test_spell_command_validate_spell_name_whitespace_only():
    """Test SpellCommand rejects whitespace-only spell_name."""
    with pytest.raises(ValidationError) as exc_info:
        SpellCommand(spell_name="   ")

    error_str = str(exc_info.value).lower()
    assert "cannot be empty" in error_str or "validation" in error_str


def test_spell_command_spell_name_max_length():
    """Test SpellCommand validates spell_name max length."""
    long_name = "a" * 101  # Exceeds max_length=100
    with pytest.raises(ValidationError):
        SpellCommand(spell_name=long_name)


# --- Tests for SpellsCommand ---


def test_spells_command_no_fields():
    """Test SpellsCommand has no required fields."""
    command = SpellsCommand()

    # Reason: Testing str enum direct comparison - valid at runtime for str enums, but mypy sees as non-overlapping
    assert command.command_type == "spells"  # type: ignore[comparison-overlap]


# --- Tests for LearnCommand ---


def test_learn_command_required_fields():
    """Test LearnCommand requires spell_name."""
    command = LearnCommand(spell_name="fireball")

    assert command.command_type == "learn"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
    assert command.spell_name == "fireball"  # type: ignore[unreachable]


def test_learn_command_validate_spell_name_valid():
    """Test LearnCommand validates and strips spell_name."""
    command = LearnCommand(spell_name="  fireball  ")

    assert command.spell_name == "fireball"  # Should be stripped


def test_learn_command_validate_spell_name_empty():
    """Test LearnCommand rejects empty spell_name."""
    with pytest.raises(ValidationError) as exc_info:
        LearnCommand(spell_name="")

    error_str = str(exc_info.value).lower()
    assert "cannot be empty" in error_str or "validation" in error_str


def test_learn_command_validate_spell_name_whitespace_only():
    """Test LearnCommand rejects whitespace-only spell_name."""
    with pytest.raises(ValidationError) as exc_info:
        LearnCommand(spell_name="   ")

    error_str = str(exc_info.value).lower()
    assert "cannot be empty" in error_str or "validation" in error_str


def test_learn_command_spell_name_max_length():
    """Test LearnCommand validates spell_name max length."""
    long_name = "a" * 101  # Exceeds max_length=100
    with pytest.raises(ValidationError):
        LearnCommand(spell_name=long_name)
