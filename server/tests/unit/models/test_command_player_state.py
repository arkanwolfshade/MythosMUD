"""
Unit tests for player state command models.

Tests the player state command models and their validators.
"""

from unittest.mock import patch

import pytest
from pydantic import ValidationError

from server.models.command_player_state import (
    GroundCommand,
    LieCommand,
    LogoutCommand,
    QuitCommand,
    SitCommand,
    StandCommand,
)

# --- Tests for QuitCommand ---


def test_quit_command_no_fields():
    """Test QuitCommand has no required fields."""
    command = QuitCommand()

    # Reason: Enum values (str enums) are comparable to strings at runtime
    assert command.command_type == "quit"  # type: ignore[comparison-overlap]


# --- Tests for LogoutCommand ---


def test_logout_command_no_fields():
    """Test LogoutCommand has no required fields."""
    command = LogoutCommand()

    # Reason: Enum values (str enums) are comparable to strings at runtime
    assert command.command_type == "logout"  # type: ignore[comparison-overlap]


# --- Tests for SitCommand ---


def test_sit_command_no_fields():
    """Test SitCommand has no required fields."""
    command = SitCommand()

    assert command.command_type == "sit"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime


# --- Tests for StandCommand ---


def test_stand_command_no_fields():
    """Test StandCommand has no required fields."""
    command = StandCommand()

    # Reason: Enum values (str enums) are comparable to strings at runtime
    assert command.command_type == "stand"  # type: ignore[comparison-overlap]


# --- Tests for LieCommand ---


def test_lie_command_default_values():
    """Test LieCommand has correct default values."""
    command = LieCommand()

    assert command.command_type == "lie"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing default value - mypy may see as unreachable but validates at runtime
    assert command.modifier is None  # type: ignore[unreachable]


def test_lie_command_with_modifier_down():
    """Test LieCommand accepts 'down' modifier."""
    command = LieCommand(modifier="down")

    assert command.modifier == "down"


def test_lie_command_validate_modifier_strips_and_lowercases():
    """Test LieCommand strips and lowercases modifier."""
    command = LieCommand(modifier="  DOWN  ")

    assert command.modifier == "down"


def test_lie_command_validate_modifier_case_insensitive():
    """Test LieCommand modifier validation is case insensitive."""
    command1 = LieCommand(modifier="DOWN")
    assert command1.modifier == "down"

    command2 = LieCommand(modifier="Down")
    assert command2.modifier == "down"

    command3 = LieCommand(modifier="down")
    assert command3.modifier == "down"


def test_lie_command_validate_modifier_invalid():
    """Test LieCommand rejects invalid modifier."""
    with pytest.raises(ValidationError) as exc_info:
        LieCommand(modifier="up")

    error_str = str(exc_info.value).lower()
    assert "invalid modifier" in error_str or "validation" in error_str


def test_lie_command_validate_modifier_none():
    """Test LieCommand accepts None for modifier."""
    command = LieCommand(modifier=None)

    assert command.modifier is None


def test_lie_command_validate_modifier_empty_string():
    """Test LieCommand rejects empty modifier after stripping."""
    # Empty string after stripping should fail validation
    with pytest.raises(ValidationError) as exc_info:
        LieCommand(modifier="   ")

    error_str = str(exc_info.value).lower()
    assert "invalid modifier" in error_str or "validation" in error_str


# --- Tests for GroundCommand ---


def test_ground_command_required_fields():
    """Test GroundCommand requires target_player."""
    with patch("server.models.command_player_state.validate_player_name", return_value="TestPlayer"):
        command = GroundCommand(target_player="TestPlayer")

        # Reason: Enum values (str enums) are comparable to strings at runtime
        assert command.command_type == "ground"  # type: ignore[comparison-overlap]
        # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
        assert command.target_player == "TestPlayer"  # type: ignore[unreachable]


def test_ground_command_validate_target_player_calls_validator():
    """Test GroundCommand calls validate_player_name."""
    with patch("server.models.command_player_state.validate_player_name", return_value="validated") as mock_validator:
        command = GroundCommand(target_player="test")

        mock_validator.assert_called_once_with("test")
        assert command.target_player == "validated"


def test_ground_command_target_player_min_length():
    """Test GroundCommand validates target_player min length."""
    with patch("server.models.command_player_state.validate_player_name", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            GroundCommand(target_player="")


def test_ground_command_target_player_max_length():
    """Test GroundCommand validates target_player max length."""
    long_name = "a" * 51  # Exceeds max_length=50
    with patch("server.models.command_player_state.validate_player_name", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            GroundCommand(target_player=long_name)
