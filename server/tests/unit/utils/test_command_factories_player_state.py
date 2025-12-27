"""
Unit tests for player state command factory methods.

Tests factory methods for creating player state and information command objects.
"""

import pytest

from server.exceptions import ValidationError as MythosValidationError
from server.models.command import (
    LogoutCommand,
    QuitCommand,
    StatusCommand,
    TimeCommand,
    WhoamiCommand,
    WhoCommand,
)
from server.utils.command_factories_player_state import PlayerStateCommandFactory


def test_create_status_command_no_args():
    """Test create_status_command creates command with no arguments."""
    result = PlayerStateCommandFactory.create_status_command([])
    
    assert isinstance(result, StatusCommand)


def test_create_status_command_with_args():
    """Test create_status_command raises error when arguments provided."""
    with pytest.raises(MythosValidationError) as exc_info:
        PlayerStateCommandFactory.create_status_command(["extra"])
    
    assert "no arguments" in str(exc_info.value).lower()


def test_create_time_command_no_args():
    """Test create_time_command creates command with no arguments."""
    result = PlayerStateCommandFactory.create_time_command([])
    
    assert isinstance(result, TimeCommand)


def test_create_time_command_with_args():
    """Test create_time_command raises error when arguments provided."""
    with pytest.raises(MythosValidationError) as exc_info:
        PlayerStateCommandFactory.create_time_command(["extra"])
    
    assert "no arguments" in str(exc_info.value).lower()


def test_create_whoami_command_no_args():
    """Test create_whoami_command creates command with no arguments."""
    result = PlayerStateCommandFactory.create_whoami_command([])
    
    assert isinstance(result, WhoamiCommand)


def test_create_whoami_command_with_args():
    """Test create_whoami_command raises error when arguments provided."""
    with pytest.raises(MythosValidationError) as exc_info:
        PlayerStateCommandFactory.create_whoami_command(["extra"])
    
    assert "no arguments" in str(exc_info.value).lower()


def test_create_who_command_no_args():
    """Test create_who_command creates command with no filter."""
    result = PlayerStateCommandFactory.create_who_command([])
    
    assert isinstance(result, WhoCommand)
    assert result.filter_name is None


def test_create_who_command_with_filter():
    """Test create_who_command creates command with filter name."""
    result = PlayerStateCommandFactory.create_who_command(["player"])
    
    assert isinstance(result, WhoCommand)
    assert result.filter_name == "player"


def test_create_who_command_with_multiple_args():
    """Test create_who_command uses first arg as filter."""
    result = PlayerStateCommandFactory.create_who_command(["player", "extra"])
    
    assert isinstance(result, WhoCommand)
    assert result.filter_name == "player"


def test_create_quit_command_no_args():
    """Test create_quit_command creates command with no arguments."""
    result = PlayerStateCommandFactory.create_quit_command([])
    
    assert isinstance(result, QuitCommand)


def test_create_quit_command_with_args():
    """Test create_quit_command raises error when arguments provided."""
    with pytest.raises(MythosValidationError) as exc_info:
        PlayerStateCommandFactory.create_quit_command(["extra"])
    
    assert "no arguments" in str(exc_info.value).lower()


def test_create_logout_command_no_args():
    """Test create_logout_command creates command ignoring arguments."""
    result = PlayerStateCommandFactory.create_logout_command([])
    
    assert isinstance(result, LogoutCommand)


def test_create_logout_command_with_args():
    """Test create_logout_command ignores arguments (unlike quit)."""
    # Logout command should accept arguments without error
    result = PlayerStateCommandFactory.create_logout_command(["force", "now"])
    
    assert isinstance(result, LogoutCommand)
