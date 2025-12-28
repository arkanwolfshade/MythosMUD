"""
Unit tests for exploration command factories.

Tests the ExplorationCommandFactory class methods.
"""

import pytest

from server.exceptions import ValidationError
from server.models.command import Direction
from server.utils.command_factories_exploration import ExplorationCommandFactory


def test_create_go_command():
    """Test create_go_command() creates GoCommand."""
    command = ExplorationCommandFactory.create_go_command(["north"])
    assert command.direction == Direction.NORTH


def test_create_go_command_no_args():
    """Test create_go_command() raises error with no args."""
    with pytest.raises(ValidationError):
        ExplorationCommandFactory.create_go_command([])


def test_create_go_command_invalid_direction():
    """Test create_go_command() raises error with invalid direction."""
    from pydantic import ValidationError as PydanticValidationError
    # Pydantic raises its own ValidationError for enum validation
    with pytest.raises(PydanticValidationError):
        ExplorationCommandFactory.create_go_command(["invalid"])


def test_create_look_command():
    """Test create_look_command() creates LookCommand."""
    command = ExplorationCommandFactory.create_look_command([])
    assert command.target is None


def test_create_look_command_with_target():
    """Test create_look_command() creates LookCommand with target."""
    command = ExplorationCommandFactory.create_look_command(["target"])
    assert command.target == "target"
