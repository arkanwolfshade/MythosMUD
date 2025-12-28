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
