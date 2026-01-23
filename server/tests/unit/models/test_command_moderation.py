"""
Unit tests for moderation command models.

Tests the moderation command models and their validators.
"""

from unittest.mock import patch

import pytest
from pydantic import ValidationError

from server.models.command_moderation import (
    AddAdminCommand,
    AdminCommand,
    MuteCommand,
    MuteGlobalCommand,
    MutesCommand,
    UnmuteCommand,
    UnmuteGlobalCommand,
)

# --- Tests for MuteCommand ---


def test_mute_command_required_fields():
    """Test MuteCommand requires player_name."""
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        command = MuteCommand(player_name="TestPlayer")

        assert command.command_type == "mute"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
        # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
        assert command.player_name == "TestPlayer"  # type: ignore[unreachable]
        assert command.duration_minutes is None
        assert command.reason is None


def test_mute_command_with_duration():
    """Test MuteCommand can have optional duration_minutes."""
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        command = MuteCommand(player_name="TestPlayer", duration_minutes=60)

        assert command.duration_minutes == 60


def test_mute_command_with_reason():
    """Test MuteCommand can have optional reason."""
    with (
        patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"),
        patch("server.models.command_moderation.validate_reason_content", return_value="Spam"),
    ):
        command = MuteCommand(player_name="TestPlayer", reason="Spam")

        assert command.reason == "Spam"


def test_mute_command_validate_player_name_calls_validator():
    """Test MuteCommand calls validate_player_name."""
    with patch("server.models.command_moderation.validate_player_name", return_value="validated") as mock_validator:
        command = MuteCommand(player_name="test")

        mock_validator.assert_called_once_with("test")
        assert command.player_name == "validated"


def test_mute_command_validate_reason_calls_validator():
    """Test MuteCommand calls validate_reason_content when reason provided."""
    with (
        patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"),
        patch("server.models.command_moderation.validate_reason_content", return_value="validated") as mock_validator,
    ):
        command = MuteCommand(player_name="TestPlayer", reason="test")

        mock_validator.assert_called_once_with("test")
        assert command.reason == "validated"


def test_mute_command_validate_reason_none():
    """Test MuteCommand accepts None for reason."""
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        command = MuteCommand(player_name="TestPlayer", reason=None)

        assert command.reason is None


def test_mute_command_duration_validation_min():
    """Test MuteCommand validates duration_minutes is >= 1."""
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        with pytest.raises(ValidationError):
            MuteCommand(player_name="TestPlayer", duration_minutes=0)


def test_mute_command_duration_validation_max():
    """Test MuteCommand validates duration_minutes is <= 10080 (1 week)."""
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        with pytest.raises(ValidationError):
            MuteCommand(player_name="TestPlayer", duration_minutes=10081)


def test_mute_command_reason_max_length():
    """Test MuteCommand validates reason max length."""
    long_reason = "a" * 201  # Exceeds max_length=200
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        with pytest.raises(ValidationError):
            MuteCommand(player_name="TestPlayer", reason=long_reason)


# --- Tests for UnmuteCommand ---


def test_unmute_command_required_fields():
    """Test UnmuteCommand requires player_name."""
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        command = UnmuteCommand(player_name="TestPlayer")

        assert command.command_type == "unmute"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
        # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
        assert command.player_name == "TestPlayer"  # type: ignore[unreachable]


def test_unmute_command_validate_player_name_calls_validator():
    """Test UnmuteCommand calls validate_player_name."""
    with patch("server.models.command_moderation.validate_player_name", return_value="validated") as mock_validator:
        command = UnmuteCommand(player_name="test")

        mock_validator.assert_called_once_with("test")
        assert command.player_name == "validated"


# --- Tests for MuteGlobalCommand ---


def test_mute_global_command_required_fields():
    """Test MuteGlobalCommand requires player_name."""
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        command = MuteGlobalCommand(player_name="TestPlayer")

        assert command.command_type == "mute_global"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
        # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
        assert command.player_name == "TestPlayer"  # type: ignore[unreachable]
        assert command.duration_minutes is None
        assert command.reason is None


def test_mute_global_command_with_duration():
    """Test MuteGlobalCommand can have optional duration_minutes."""
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        command = MuteGlobalCommand(player_name="TestPlayer", duration_minutes=120)

        assert command.duration_minutes == 120


def test_mute_global_command_validate_player_name_calls_validator():
    """Test MuteGlobalCommand calls validate_player_name."""
    with patch("server.models.command_moderation.validate_player_name", return_value="validated") as mock_validator:
        command = MuteGlobalCommand(player_name="test")

        mock_validator.assert_called_once_with("test")
        assert command.player_name == "validated"


def test_mute_global_command_validate_reason_calls_validator():
    """Test MuteGlobalCommand calls validate_reason_content when reason provided."""
    with (
        patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"),
        patch("server.models.command_moderation.validate_reason_content", return_value="validated") as mock_validator,
    ):
        command = MuteGlobalCommand(player_name="TestPlayer", reason="test")

        mock_validator.assert_called_once_with("test")
        assert command.reason == "validated"


def test_mute_global_command_duration_validation_min():
    """Test MuteGlobalCommand validates duration_minutes is >= 1."""
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        with pytest.raises(ValidationError):
            MuteGlobalCommand(player_name="TestPlayer", duration_minutes=0)


def test_mute_global_command_duration_validation_max():
    """Test MuteGlobalCommand validates duration_minutes is <= 10080."""
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        with pytest.raises(ValidationError):
            MuteGlobalCommand(player_name="TestPlayer", duration_minutes=10081)


# --- Tests for UnmuteGlobalCommand ---


def test_unmute_global_command_required_fields():
    """Test UnmuteGlobalCommand requires player_name."""
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        command = UnmuteGlobalCommand(player_name="TestPlayer")

        assert command.command_type == "unmute_global"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
        # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
        assert command.player_name == "TestPlayer"  # type: ignore[unreachable]


def test_unmute_global_command_validate_player_name_calls_validator():
    """Test UnmuteGlobalCommand calls validate_player_name."""
    with patch("server.models.command_moderation.validate_player_name", return_value="validated") as mock_validator:
        command = UnmuteGlobalCommand(player_name="test")

        mock_validator.assert_called_once_with("test")
        assert command.player_name == "validated"


# --- Tests for AddAdminCommand ---


def test_add_admin_command_required_fields():
    """Test AddAdminCommand requires player_name."""
    with patch("server.models.command_moderation.validate_player_name", return_value="TestPlayer"):
        command = AddAdminCommand(player_name="TestPlayer")

        assert command.command_type == "add_admin"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
        # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
        assert command.player_name == "TestPlayer"  # type: ignore[unreachable]


def test_add_admin_command_validate_player_name_calls_validator():
    """Test AddAdminCommand calls validate_player_name."""
    with patch("server.models.command_moderation.validate_player_name", return_value="validated") as mock_validator:
        command = AddAdminCommand(player_name="test")

        mock_validator.assert_called_once_with("test")
        assert command.player_name == "validated"


# --- Tests for MutesCommand ---


def test_mutes_command_no_fields():
    """Test MutesCommand has no required fields."""
    command = MutesCommand()

    # Reason: Testing str enum direct comparison - valid at runtime for str enums, but mypy sees as non-overlapping
    assert command.command_type == "mutes"  # type: ignore[comparison-overlap]


# --- Tests for AdminCommand ---


def test_admin_command_required_fields():
    """Test AdminCommand requires subcommand."""
    command = AdminCommand(subcommand="status")

    assert command.command_type == "admin"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
    assert command.subcommand == "status"  # type: ignore[unreachable]
    assert command.args == []


def test_admin_command_with_args():
    """Test AdminCommand can have args."""
    command = AdminCommand(subcommand="status", args=["arg1", "arg2"])

    assert command.args == ["arg1", "arg2"]


def test_admin_command_validate_subcommand_valid():
    """Test AdminCommand validates valid subcommand."""
    command = AdminCommand(subcommand="status")

    assert command.subcommand == "status"


def test_admin_command_validate_subcommand_case_insensitive():
    """Test AdminCommand normalizes subcommand to lowercase."""
    command = AdminCommand(subcommand="STATUS")

    assert command.subcommand == "status"


def test_admin_command_validate_subcommand_invalid():
    """Test AdminCommand rejects invalid subcommand."""
    with pytest.raises(ValidationError) as exc_info:
        AdminCommand(subcommand="invalid")

    error_str = str(exc_info.value).lower()
    assert "invalid admin subcommand" in error_str or "validation" in error_str


def test_admin_command_subcommand_min_length():
    """Test AdminCommand validates subcommand min length."""
    with pytest.raises(ValidationError):
        AdminCommand(subcommand="")


def test_admin_command_subcommand_max_length():
    """Test AdminCommand validates subcommand max length."""
    long_subcommand = "a" * 31  # Exceeds max_length=30
    with pytest.raises(ValidationError):
        AdminCommand(subcommand=long_subcommand)
