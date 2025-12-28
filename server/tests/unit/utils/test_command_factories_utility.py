"""
Unit tests for utility command factories.

Tests the UtilityCommandFactory class methods.
"""

import pytest

from server.exceptions import ValidationError
from server.utils.command_factories_utility import UtilityCommandFactory


def test_create_alias_command():
    """Test create_alias_command() creates AliasCommand."""
    command = UtilityCommandFactory.create_alias_command(["test_alias", "go", "north"])
    assert command.alias_name == "test_alias"
    assert command.command == "go north"


def test_create_alias_command_no_args():
    """Test create_alias_command() raises error with no args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_alias_command([])


def test_create_aliases_command():
    """Test create_aliases_command() creates AliasesCommand."""
    command = UtilityCommandFactory.create_aliases_command([])
    assert command is not None


def test_create_aliases_command_with_args():
    """Test create_aliases_command() raises error with args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_aliases_command(["arg"])


def test_create_unalias_command():
    """Test create_unalias_command() creates UnaliasCommand."""
    command = UtilityCommandFactory.create_unalias_command(["test_alias"])
    assert command.alias_name == "test_alias"


def test_create_unalias_command_no_args():
    """Test create_unalias_command() raises error with no args."""
    with pytest.raises(ValidationError):
        UtilityCommandFactory.create_unalias_command([])


def test_create_help_command():
    """Test create_help_command() creates HelpCommand."""
    command = UtilityCommandFactory.create_help_command(["look"])
    assert command.topic == "look"


def test_create_help_command_no_args():
    """Test create_help_command() creates HelpCommand with no topic."""
    command = UtilityCommandFactory.create_help_command([])
    assert command.topic is None
