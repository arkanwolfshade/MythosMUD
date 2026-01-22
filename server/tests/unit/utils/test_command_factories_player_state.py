"""
Unit tests for player state command factories.

Tests the PlayerStateCommandFactory class methods.
"""

import pytest

from server.exceptions import ValidationError
from server.utils.command_factories_player_state import PlayerStateCommandFactory


def test_create_status_command():
    """Test create_status_command() creates StatusCommand."""
    command = PlayerStateCommandFactory.create_status_command([])
    assert command is not None


def test_create_status_command_with_args():
    """Test create_status_command() raises error with args."""
    with pytest.raises(ValidationError):
        PlayerStateCommandFactory.create_status_command(["arg"])


def test_create_whoami_command():
    """Test create_whoami_command() creates WhoamiCommand."""
    command = PlayerStateCommandFactory.create_whoami_command([])
    assert command is not None


def test_create_whoami_command_with_args():
    """Test create_whoami_command() raises error with args."""
    with pytest.raises(ValidationError):
        PlayerStateCommandFactory.create_whoami_command(["arg"])


def test_create_time_command():
    """Test create_time_command() creates TimeCommand."""
    command = PlayerStateCommandFactory.create_time_command([])
    assert command is not None


def test_create_time_command_with_args():
    """Test create_time_command() raises error with args."""
    with pytest.raises(ValidationError):
        PlayerStateCommandFactory.create_time_command(["arg"])


def test_create_who_command():
    """Test create_who_command() creates WhoCommand."""
    command = PlayerStateCommandFactory.create_who_command([])
    assert command.filter_name is None


def test_create_who_command_with_filter():
    """Test create_who_command() with filter name."""
    command = PlayerStateCommandFactory.create_who_command(["online"])
    assert command.filter_name == "online"


def test_create_quit_command():
    """Test create_quit_command() creates QuitCommand."""
    command = PlayerStateCommandFactory.create_quit_command([])
    assert command is not None


def test_create_quit_command_with_args():
    """Test create_quit_command() raises error with args."""
    with pytest.raises(ValidationError):
        PlayerStateCommandFactory.create_quit_command(["now"])


def test_create_logout_command():
    """Test create_logout_command() creates LogoutCommand."""
    command = PlayerStateCommandFactory.create_logout_command([])
    assert command is not None


def test_create_logout_command_with_args():
    """Test create_logout_command() ignores args."""
    command = PlayerStateCommandFactory.create_logout_command(["force"])
    assert command is not None


def test_create_rest_command():
    """Test create_rest_command() creates RestCommand."""
    command = PlayerStateCommandFactory.create_rest_command([])
    assert command is not None


def test_create_rest_command_with_args():
    """Test create_rest_command() raises error with args."""
    with pytest.raises(ValidationError):
        PlayerStateCommandFactory.create_rest_command(["quickly"])
