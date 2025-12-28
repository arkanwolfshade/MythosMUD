"""
Unit tests for alias command models.

Tests the alias command models and their validators.
"""

from unittest.mock import patch

import pytest
from pydantic import ValidationError

from server.models.command_alias import AliasCommand, AliasesCommand, UnaliasCommand

# --- Tests for AliasCommand ---


def test_alias_command_required_fields():
    """Test AliasCommand requires alias_name."""
    with patch("server.models.command_alias.validate_alias_name", return_value="testalias"):
        command = AliasCommand(alias_name="testalias")

        assert command.command_type == "alias"
        assert command.alias_name == "testalias"
        assert command.command is None


def test_alias_command_with_command():
    """Test AliasCommand can have optional command."""
    with (
        patch("server.models.command_alias.validate_alias_name", return_value="testalias"),
        patch("server.models.command_alias.validate_command_content", return_value="look north"),
    ):
        command = AliasCommand(alias_name="testalias", command="look north")

        assert command.command == "look north"


def test_alias_command_validate_alias_name_calls_validator():
    """Test AliasCommand calls validate_alias_name."""
    with patch("server.models.command_alias.validate_alias_name", return_value="validated") as mock_validator:
        command = AliasCommand(alias_name="test")

        mock_validator.assert_called_once_with("test")
        assert command.alias_name == "validated"


def test_alias_command_validate_command_calls_validator():
    """Test AliasCommand calls validate_command_content when command provided."""
    with (
        patch("server.models.command_alias.validate_alias_name", return_value="testalias"),
        patch("server.models.command_alias.validate_command_content", return_value="validated") as mock_validator,
    ):
        command = AliasCommand(alias_name="testalias", command="test")

        mock_validator.assert_called_once_with("test")
        assert command.command == "validated"


def test_alias_command_validate_command_none():
    """Test AliasCommand accepts None for command."""
    with patch("server.models.command_alias.validate_alias_name", return_value="testalias"):
        command = AliasCommand(alias_name="testalias", command=None)

        assert command.command is None


def test_alias_command_alias_name_min_length():
    """Test AliasCommand validates alias_name min length."""
    with patch("server.models.command_alias.validate_alias_name", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            AliasCommand(alias_name="")


def test_alias_command_alias_name_max_length():
    """Test AliasCommand validates alias_name max length."""
    long_name = "a" * 21  # Exceeds max_length=20
    with patch("server.models.command_alias.validate_alias_name", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            AliasCommand(alias_name=long_name)


def test_alias_command_command_max_length():
    """Test AliasCommand validates command max length."""
    long_command = "a" * 201  # Exceeds max_length=200
    with (
        patch("server.models.command_alias.validate_alias_name", return_value="testalias"),
        patch("server.models.command_alias.validate_command_content", side_effect=ValidationError),
    ):
        with pytest.raises(ValidationError):
            AliasCommand(alias_name="testalias", command=long_command)


# --- Tests for AliasesCommand ---


def test_aliases_command_no_fields():
    """Test AliasesCommand has no required fields."""
    command = AliasesCommand()

    assert command.command_type == "aliases"


# --- Tests for UnaliasCommand ---


def test_unalias_command_required_fields():
    """Test UnaliasCommand requires alias_name."""
    with patch("server.models.command_alias.validate_alias_name", return_value="testalias"):
        command = UnaliasCommand(alias_name="testalias")

        assert command.command_type == "unalias"
        assert command.alias_name == "testalias"


def test_unalias_command_validate_alias_name_calls_validator():
    """Test UnaliasCommand calls validate_alias_name."""
    with patch("server.models.command_alias.validate_alias_name", return_value="validated") as mock_validator:
        command = UnaliasCommand(alias_name="test")

        mock_validator.assert_called_once_with("test")
        assert command.alias_name == "validated"


def test_unalias_command_alias_name_min_length():
    """Test UnaliasCommand validates alias_name min length."""
    with patch("server.models.command_alias.validate_alias_name", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            UnaliasCommand(alias_name="")


def test_unalias_command_alias_name_max_length():
    """Test UnaliasCommand validates alias_name max length."""
    long_name = "a" * 21  # Exceeds max_length=20
    with patch("server.models.command_alias.validate_alias_name", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            UnaliasCommand(alias_name=long_name)
