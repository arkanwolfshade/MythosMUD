"""
Unit tests for combat command models.

Tests the combat command models and their validators.
"""

from unittest.mock import patch

import pytest
from pydantic import ValidationError

from server.models.command_combat import AttackCommand, KickCommand, PunchCommand, StrikeCommand

# --- Tests for AttackCommand ---


def test_attack_command_default_values():
    """Test AttackCommand has correct default values."""
    command = AttackCommand()

    assert command.command_type == "attack"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing default value - mypy may see as unreachable but validates at runtime
    assert command.target is None  # type: ignore[unreachable]


def test_attack_command_with_target():
    """Test AttackCommand can have optional target."""
    with patch("server.models.command_combat.validate_combat_target", return_value="enemy"):
        command = AttackCommand(target="enemy")

        assert command.target == "enemy"


def test_attack_command_validate_target_calls_validator():
    """Test AttackCommand calls validate_combat_target when target provided."""
    with patch("server.models.command_combat.validate_combat_target", return_value="validated") as mock_validator:
        command = AttackCommand(target="test")

        mock_validator.assert_called_once_with("test")
        assert command.target == "validated"


def test_attack_command_validate_target_none():
    """Test AttackCommand accepts None for target."""
    command = AttackCommand(target=None)

    assert command.target is None


def test_attack_command_target_min_length():
    """Test AttackCommand validates target min length."""
    with patch("server.models.command_combat.validate_combat_target", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            AttackCommand(target="")


def test_attack_command_target_max_length():
    """Test AttackCommand validates target max length."""
    long_target = "a" * 51  # Exceeds max_length=50
    with patch("server.models.command_combat.validate_combat_target", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            AttackCommand(target=long_target)


# --- Tests for PunchCommand ---


def test_punch_command_default_values():
    """Test PunchCommand has correct default values."""
    command = PunchCommand()

    assert command.command_type == "punch"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing default value - mypy may see as unreachable but validates at runtime
    assert command.target is None  # type: ignore[unreachable]


def test_punch_command_with_target():
    """Test PunchCommand can have optional target."""
    with patch("server.models.command_combat.validate_combat_target", return_value="enemy"):
        command = PunchCommand(target="enemy")

        assert command.target == "enemy"


def test_punch_command_validate_target_calls_validator():
    """Test PunchCommand calls validate_combat_target when target provided."""
    with patch("server.models.command_combat.validate_combat_target", return_value="validated") as mock_validator:
        command = PunchCommand(target="test")

        mock_validator.assert_called_once_with("test")
        assert command.target == "validated"


def test_punch_command_validate_target_none():
    """Test PunchCommand accepts None for target."""
    command = PunchCommand(target=None)

    assert command.target is None


def test_punch_command_target_min_length():
    """Test PunchCommand validates target min length."""
    with patch("server.models.command_combat.validate_combat_target", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            PunchCommand(target="")


def test_punch_command_target_max_length():
    """Test PunchCommand validates target max length."""
    long_target = "a" * 51  # Exceeds max_length=50
    with patch("server.models.command_combat.validate_combat_target", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            PunchCommand(target=long_target)


# --- Tests for KickCommand ---


def test_kick_command_default_values():
    """Test KickCommand has correct default values."""
    command = KickCommand()

    assert command.command_type == "kick"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing default value - mypy may see as unreachable but validates at runtime
    assert command.target is None  # type: ignore[unreachable]


def test_kick_command_with_target():
    """Test KickCommand can have optional target."""
    with patch("server.models.command_combat.validate_combat_target", return_value="enemy"):
        command = KickCommand(target="enemy")

        assert command.target == "enemy"


def test_kick_command_validate_target_calls_validator():
    """Test KickCommand calls validate_combat_target when target provided."""
    with patch("server.models.command_combat.validate_combat_target", return_value="validated") as mock_validator:
        command = KickCommand(target="test")

        mock_validator.assert_called_once_with("test")
        assert command.target == "validated"


def test_kick_command_validate_target_none():
    """Test KickCommand accepts None for target."""
    command = KickCommand(target=None)

    assert command.target is None


def test_kick_command_target_min_length():
    """Test KickCommand validates target min length."""
    with patch("server.models.command_combat.validate_combat_target", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            KickCommand(target="")


def test_kick_command_target_max_length():
    """Test KickCommand validates target max length."""
    long_target = "a" * 51  # Exceeds max_length=50
    with patch("server.models.command_combat.validate_combat_target", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            KickCommand(target=long_target)


# --- Tests for StrikeCommand ---


def test_strike_command_default_values():
    """Test StrikeCommand has correct default values."""
    command = StrikeCommand()

    assert command.command_type == "strike"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing default value - mypy may see as unreachable but validates at runtime
    assert command.target is None  # type: ignore[unreachable]


def test_strike_command_with_target():
    """Test StrikeCommand can have optional target."""
    with patch("server.models.command_combat.validate_combat_target", return_value="enemy"):
        command = StrikeCommand(target="enemy")

        assert command.target == "enemy"


def test_strike_command_validate_target_calls_validator():
    """Test StrikeCommand calls validate_combat_target when target provided."""
    with patch("server.models.command_combat.validate_combat_target", return_value="validated") as mock_validator:
        command = StrikeCommand(target="test")

        mock_validator.assert_called_once_with("test")
        assert command.target == "validated"


def test_strike_command_validate_target_none():
    """Test StrikeCommand accepts None for target."""
    command = StrikeCommand(target=None)

    assert command.target is None


def test_strike_command_target_min_length():
    """Test StrikeCommand validates target min length."""
    with patch("server.models.command_combat.validate_combat_target", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            StrikeCommand(target="")


def test_strike_command_target_max_length():
    """Test StrikeCommand validates target max length."""
    long_target = "a" * 51  # Exceeds max_length=50
    with patch("server.models.command_combat.validate_combat_target", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            StrikeCommand(target=long_target)
