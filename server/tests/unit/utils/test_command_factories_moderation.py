"""
Unit tests for moderation command factories.

Tests the ModerationCommandFactory class methods.
"""

import pytest

from server.exceptions import ValidationError
from server.utils.command_factories_moderation import ModerationCommandFactory


def test_create_mute_command():
    """Test create_mute_command() creates MuteCommand."""
    command = ModerationCommandFactory.create_mute_command(["target", "reason"])
    assert command.player_name == "target"
    assert command.reason == "reason"


def test_create_mute_command_no_args():
    """Test create_mute_command() raises error with no args."""
    with pytest.raises(ValidationError):
        ModerationCommandFactory.create_mute_command([])


def test_create_unmute_command():
    """Test create_unmute_command() creates UnmuteCommand."""
    command = ModerationCommandFactory.create_unmute_command(["target"])
    assert command.player_name == "target"


def test_create_unmute_command_no_args():
    """Test create_unmute_command() raises error with no args."""
    with pytest.raises(ValidationError):
        ModerationCommandFactory.create_unmute_command([])


def test_create_add_admin_command():
    """Test create_add_admin_command() creates AddAdminCommand."""
    command = ModerationCommandFactory.create_add_admin_command(["target"])
    assert command.player_name == "target"


def test_create_add_admin_command_no_args():
    """Test create_add_admin_command() raises error with no args."""
    with pytest.raises(ValidationError):
        ModerationCommandFactory.create_add_admin_command([])


def test_create_mute_command_with_duration():
    """Test create_mute_command() with duration."""
    command = ModerationCommandFactory.create_mute_command(["target", "60"])
    assert command.player_name == "target"
    assert command.duration_minutes == 60
    assert command.reason is None


def test_create_mute_command_with_duration_and_reason():
    """Test create_mute_command() with duration and reason."""
    command = ModerationCommandFactory.create_mute_command(["target", "60", "Spamming"])
    assert command.player_name == "target"
    assert command.duration_minutes == 60
    assert command.reason == "Spamming"


def test_create_mute_command_with_reason_no_duration():
    """Test create_mute_command() with reason but no duration."""
    command = ModerationCommandFactory.create_mute_command(["target", "Spamming"])
    assert command.player_name == "target"
    assert command.duration_minutes is None
    assert command.reason == "Spamming"


def test_create_unmute_command_with_multiple_args():
    """Test create_unmute_command() raises error with multiple args."""
    with pytest.raises(ValidationError, match="only one argument"):
        ModerationCommandFactory.create_unmute_command(["target", "extra"])


def test_create_mute_global_command():
    """Test create_mute_global_command() creates MuteGlobalCommand."""
    command = ModerationCommandFactory.create_mute_global_command(["target"])
    assert command.player_name == "target"
    assert command.duration_minutes is None
    assert command.reason is None


def test_create_mute_global_command_no_args():
    """Test create_mute_global_command() raises error with no args."""
    with pytest.raises(ValidationError):
        ModerationCommandFactory.create_mute_global_command([])


def test_create_mute_global_command_with_duration():
    """Test create_mute_global_command() with duration."""
    command = ModerationCommandFactory.create_mute_global_command(["target", "120"])
    assert command.player_name == "target"
    assert command.duration_minutes == 120
    assert command.reason is None


def test_create_mute_global_command_with_duration_and_reason():
    """Test create_mute_global_command() with duration and reason."""
    command = ModerationCommandFactory.create_mute_global_command(["target", "120", "Global", "spam"])
    assert command.player_name == "target"
    assert command.duration_minutes == 120
    assert command.reason == "Global spam"


def test_create_mute_global_command_with_reason_no_duration():
    """Test create_mute_global_command() with reason but no duration."""
    command = ModerationCommandFactory.create_mute_global_command(["target", "Global", "spam"])
    assert command.player_name == "target"
    assert command.duration_minutes is None
    assert command.reason == "Global spam"


def test_create_unmute_global_command():
    """Test create_unmute_global_command() creates UnmuteGlobalCommand."""
    command = ModerationCommandFactory.create_unmute_global_command(["target"])
    assert command.player_name == "target"


def test_create_unmute_global_command_no_args():
    """Test create_unmute_global_command() raises error with no args."""
    with pytest.raises(ValidationError):
        ModerationCommandFactory.create_unmute_global_command([])


def test_create_unmute_global_command_with_multiple_args():
    """Test create_unmute_global_command() raises error with multiple args."""
    with pytest.raises(ValidationError, match="only one argument"):
        ModerationCommandFactory.create_unmute_global_command(["target", "extra"])


def test_create_admin_command():
    """Test create_admin_command() creates AdminCommand."""
    command = ModerationCommandFactory.create_admin_command(["setlucidity", "player", "10"])
    assert command.subcommand == "setlucidity"
    assert command.args == ["player", "10"]


def test_create_admin_command_no_args():
    """Test create_admin_command() raises error with no args."""
    with pytest.raises(ValidationError):
        ModerationCommandFactory.create_admin_command([])


def test_create_admin_command_status_with_args():
    """Test create_admin_command() raises error when status command has args."""
    with pytest.raises(ValidationError, match="does not accept additional arguments"):
        ModerationCommandFactory.create_admin_command(["status", "extra"])


def test_create_mutes_command():
    """Test create_mutes_command() creates MutesCommand."""
    command = ModerationCommandFactory.create_mutes_command([])
    assert command is not None


def test_create_mutes_command_with_args():
    """Test create_mutes_command() raises error with args."""
    with pytest.raises(ValidationError, match="takes no arguments"):
        ModerationCommandFactory.create_mutes_command(["extra"])


def test_create_add_admin_command_with_multiple_args():
    """Test create_add_admin_command() raises error with multiple args."""
    with pytest.raises(ValidationError, match="only one argument"):
        ModerationCommandFactory.create_add_admin_command(["target", "extra"])
