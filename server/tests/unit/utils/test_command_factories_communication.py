"""
Unit tests for communication command factories.

Tests the CommunicationCommandFactory class methods.
"""

import pytest

from server.exceptions import ValidationError
from server.utils.command_factories_communication import CommunicationCommandFactory


def test_create_say_command():
    """Test create_say_command() creates SayCommand."""
    command = CommunicationCommandFactory.create_say_command(["Hello", "world"])
    assert command.message == "Hello world"


def test_create_say_command_no_args():
    """Test create_say_command() raises error with no args."""
    with pytest.raises(ValidationError):
        CommunicationCommandFactory.create_say_command([])


def test_create_local_command():
    """Test create_local_command() creates LocalCommand."""
    command = CommunicationCommandFactory.create_local_command(["Hello", "world"])
    assert command.message == "Hello world"


def test_create_local_command_no_args():
    """Test create_local_command() raises error with no args."""
    with pytest.raises(ValidationError):
        CommunicationCommandFactory.create_local_command([])


def test_create_whisper_command():
    """Test create_whisper_command() creates WhisperCommand."""
    command = CommunicationCommandFactory.create_whisper_command(["target", "Hello"])
    assert command.target == "target"
    assert command.message == "Hello"


def test_create_whisper_command_no_args():
    """Test create_whisper_command() raises error with no args."""
    with pytest.raises(ValidationError):
        CommunicationCommandFactory.create_whisper_command([])


def test_create_whisper_command_no_message():
    """Test create_whisper_command() raises error with only target."""
    with pytest.raises(ValidationError):
        CommunicationCommandFactory.create_whisper_command(["target"])


def test_create_reply_command():
    """Test create_reply_command() creates ReplyCommand."""
    command = CommunicationCommandFactory.create_reply_command(["Hello"])
    assert command.message == "Hello"


def test_create_reply_command_no_args():
    """Test create_reply_command() raises error with no args."""
    with pytest.raises(ValidationError):
        CommunicationCommandFactory.create_reply_command([])
