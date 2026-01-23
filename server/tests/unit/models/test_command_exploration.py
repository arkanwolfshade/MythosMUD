"""
Unit tests for exploration command models.

Tests the LookCommand and GoCommand models and their validators.
"""

import pytest
from pydantic import ValidationError

from server.models.command_base import Direction
from server.models.command_exploration import GoCommand, LookCommand

# --- Tests for LookCommand ---


def test_look_command_default_values():
    """Test LookCommand has correct default values."""
    command = LookCommand()

    # Reason: Enum values (str enums) are comparable to strings at runtime
    assert command.command_type == "look"  # type: ignore[comparison-overlap]
    # Reason: Testing default value - mypy may see as unreachable but validates at runtime
    assert command.direction is None  # type: ignore[unreachable]
    assert command.target is None
    assert command.target_type is None
    assert command.look_in is False
    assert command.instance_number is None


def test_look_command_with_direction():
    """Test LookCommand can be created with a direction."""
    command = LookCommand(direction=Direction.NORTH)

    assert command.direction == Direction.NORTH


def test_look_command_validate_direction_valid():
    """Test LookCommand validates valid direction."""
    command = LookCommand(direction=Direction.SOUTH)

    assert command.direction == Direction.SOUTH


def test_look_command_validate_direction_invalid():
    """Test LookCommand rejects invalid direction."""
    with pytest.raises(ValidationError) as exc_info:
        LookCommand(direction="invalid_direction")

    error_str = str(exc_info.value).lower()
    assert "invalid direction" in error_str or "validation" in error_str


def test_look_command_validate_direction_none():
    """Test LookCommand accepts None for direction."""
    command = LookCommand(direction=None)

    assert command.direction is None


def test_look_command_with_target():
    """Test LookCommand can be created with a target."""
    command = LookCommand(target="test_npc")

    assert command.target == "test_npc"


def test_look_command_with_look_in():
    """Test LookCommand can be created with look_in flag."""
    command = LookCommand(look_in=True)

    assert command.look_in is True


def test_look_command_with_instance_number():
    """Test LookCommand can be created with instance_number."""
    command = LookCommand(instance_number=2)

    assert command.instance_number == 2


def test_look_command_instance_number_validation_min():
    """Test LookCommand validates instance_number is >= 1."""
    with pytest.raises(ValidationError):
        LookCommand(instance_number=0)  # Below minimum


# --- Tests for GoCommand ---


def test_go_command_required_direction():
    """Test GoCommand requires direction field."""
    command = GoCommand(direction=Direction.EAST)

    # Reason: Enum values (str enums) are comparable to strings at runtime
    # Reason: Testing str enum direct comparison - valid at runtime for str enums, but mypy sees as non-overlapping
    assert command.command_type == "go"  # type: ignore[comparison-overlap]
    # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
    assert command.direction == Direction.EAST  # type: ignore[unreachable]


def test_go_command_validate_direction_valid():
    """Test GoCommand validates valid direction."""
    command = GoCommand(direction=Direction.WEST)

    assert command.direction == Direction.WEST


def test_go_command_validate_direction_invalid():
    """Test GoCommand rejects invalid direction."""
    with pytest.raises(ValidationError) as exc_info:
        GoCommand(direction="invalid_direction")

    error_str = str(exc_info.value).lower()
    assert "invalid direction" in error_str or "validation" in error_str


def test_go_command_all_directions():
    """Test GoCommand accepts all valid directions."""
    for direction in Direction:
        command = GoCommand(direction=direction)
        assert command.direction == direction


def test_go_command_missing_direction():
    """Test GoCommand requires direction (cannot be None)."""
    with pytest.raises(ValidationError):
        # Reason: Intentionally testing Pydantic validation with missing required field
        GoCommand()  # type: ignore[call-arg]  # Missing required direction
