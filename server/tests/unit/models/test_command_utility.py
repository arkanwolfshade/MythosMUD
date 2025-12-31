"""
Unit tests for utility command models.

Tests the utility command models and their validators.
"""

from unittest.mock import patch

import pytest
from pydantic import ValidationError

from server.models.command_utility import (
    HelpCommand,
    StatusCommand,
    TimeCommand,
    WhoamiCommand,
    WhoCommand,
)

# --- Tests for HelpCommand ---


def test_help_command_default_values():
    """Test HelpCommand has correct default values."""
    command = HelpCommand()

    assert command.command_type == "help"
    assert command.topic is None


def test_help_command_with_topic():
    """Test HelpCommand can have optional topic."""
    with patch("server.models.command_utility.validate_help_topic", return_value="look"):
        command = HelpCommand(topic="look")

        assert command.topic == "look"


def test_help_command_validate_topic_calls_validator():
    """Test HelpCommand calls validate_help_topic when topic provided."""
    with patch("server.models.command_utility.validate_help_topic", return_value="validated") as mock_validator:
        command = HelpCommand(topic="test")

        mock_validator.assert_called_once_with("test")
        assert command.topic == "validated"


def test_help_command_validate_topic_none():
    """Test HelpCommand accepts None for topic."""
    command = HelpCommand(topic=None)

    assert command.topic is None


def test_help_command_topic_max_length():
    """Test HelpCommand validates topic max length."""
    long_topic = "a" * 51  # Exceeds max_length=50
    with patch("server.models.command_utility.validate_help_topic", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            HelpCommand(topic=long_topic)


# --- Tests for WhoCommand ---


def test_who_command_default_values():
    """Test WhoCommand has correct default values."""
    command = WhoCommand()

    assert command.command_type == "who"
    assert command.filter_name is None


def test_who_command_with_filter_name():
    """Test WhoCommand can have optional filter_name."""
    with patch("server.models.command_utility.validate_filter_name", return_value="player1"):
        command = WhoCommand(filter_name="player1")

        assert command.filter_name == "player1"


def test_who_command_validate_filter_name_calls_validator():
    """Test WhoCommand calls validate_filter_name when filter_name provided."""
    with patch("server.models.command_utility.validate_filter_name", return_value="validated") as mock_validator:
        command = WhoCommand(filter_name="test")

        mock_validator.assert_called_once_with("test")
        assert command.filter_name == "validated"


def test_who_command_validate_filter_name_none():
    """Test WhoCommand accepts None for filter_name."""
    command = WhoCommand(filter_name=None)

    assert command.filter_name is None


def test_who_command_filter_name_max_length():
    """Test WhoCommand validates filter_name max length."""
    long_filter = "a" * 51  # Exceeds max_length=50
    with patch("server.models.command_utility.validate_filter_name", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            WhoCommand(filter_name=long_filter)


# --- Tests for StatusCommand ---


def test_status_command_no_fields():
    """Test StatusCommand has no required fields."""
    command = StatusCommand()

    assert command.command_type == "status"


# --- Tests for TimeCommand ---


def test_time_command_no_fields():
    """Test TimeCommand has no required fields."""
    command = TimeCommand()

    assert command.command_type == "time"


# --- Tests for WhoamiCommand ---


def test_whoami_command_no_fields():
    """Test WhoamiCommand has no required fields."""
    command = WhoamiCommand()

    assert command.command_type == "whoami"
