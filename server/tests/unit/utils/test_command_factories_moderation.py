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
