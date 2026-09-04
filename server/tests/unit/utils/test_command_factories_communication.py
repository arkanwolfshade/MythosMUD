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


def test_create_local_command_too_long():
    """Test create_local_command() raises error when message exceeds 500 characters."""
    long_message = "a" * 501
    with pytest.raises(ValidationError, match="too long"):
        CommunicationCommandFactory.create_local_command([long_message])


def test_create_system_command():
    """Test create_system_command() creates SystemCommand."""
    command = CommunicationCommandFactory.create_system_command(["System", "message"])
    assert command.message == "System message"


def test_create_system_command_no_args():
    """Test create_system_command() raises error with no args."""
    with pytest.raises(ValidationError):
        CommunicationCommandFactory.create_system_command([])


def test_create_emote_command():
    """Test create_emote_command() creates EmoteCommand."""
    command = CommunicationCommandFactory.create_emote_command(["smiles", "widely"])
    assert command.action == "smiles widely"


def test_create_emote_command_no_args():
    """Test create_emote_command() raises error with no args."""
    with pytest.raises(ValidationError):
        CommunicationCommandFactory.create_emote_command([])


def test_create_me_command():
    """Test create_me_command() creates MeCommand."""
    command = CommunicationCommandFactory.create_me_command(["does", "something"])
    assert command.action == "does something"


def test_create_me_command_no_args():
    """Test create_me_command() raises error with no args."""
    with pytest.raises(ValidationError):
        CommunicationCommandFactory.create_me_command([])


def test_create_pose_command():
    """Test create_pose_command() creates PoseCommand."""
    command = CommunicationCommandFactory.create_pose_command(["stands", "tall"])
    assert command.pose == "stands tall"


def test_create_pose_command_no_args():
    """Test create_pose_command() allows no args (sets pose to None)."""
    command = CommunicationCommandFactory.create_pose_command([])
    assert command.pose is None


def test_create_channel_command():
    """Test create_channel_command() creates ChannelCommand."""
    command = CommunicationCommandFactory.create_channel_command(["ooc"])
    assert command.channel == "ooc"
    assert command.action is None


def test_create_channel_command_with_default():
    """Test create_channel_command() handles 'default' action."""
    command = CommunicationCommandFactory.create_channel_command(["default", "ooc"])
    assert command.channel == "default"
    assert command.action == "ooc"


def test_create_channel_command_no_args():
    """Test create_channel_command() raises error with no args."""
    with pytest.raises(ValidationError):
        CommunicationCommandFactory.create_channel_command([])


def test_create_channel_command_default_no_channel():
    """Test create_channel_command() raises error with 'default' but no channel."""
    with pytest.raises(ValidationError):
        CommunicationCommandFactory.create_channel_command(["default"])


def test_create_reply_command_empty_message():
    """Test create_reply_command() raises error with whitespace-only message."""
    with pytest.raises(ValidationError):
        CommunicationCommandFactory.create_reply_command(["   "])


def test_create_whisper_command_too_long():
    """Test create_whisper_command() raises error when message exceeds 500 characters."""
    long_message = "a" * 501
    with pytest.raises(ValidationError, match="too long"):
        CommunicationCommandFactory.create_whisper_command(["target", long_message])
