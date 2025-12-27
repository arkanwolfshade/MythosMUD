"""
Unit tests for communication command factory methods.

Tests factory methods for creating communication-related command objects.
"""

import pytest

from server.exceptions import ValidationError as MythosValidationError
from server.models.command import (
    EmoteCommand,
    LocalCommand,
    MeCommand,
    PoseCommand,
    ReplyCommand,
    SayCommand,
    SystemCommand,
    WhisperCommand,
)
from server.utils.command_factories_communication import CommunicationCommandFactory


def test_create_say_command_no_args():
    """Test create_say_command raises error when no arguments."""
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_say_command([])
    
    assert "requires a message" in str(exc_info.value).lower()


def test_create_say_command_with_message():
    """Test create_say_command creates command with message."""
    result = CommunicationCommandFactory.create_say_command(["Hello", "world"])
    
    assert isinstance(result, SayCommand)
    assert result.message == "Hello world"


def test_create_local_command_no_args():
    """Test create_local_command raises error when no arguments."""
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_local_command([])
    
    assert "must provide a message" in str(exc_info.value).lower()


def test_create_local_command_with_message():
    """Test create_local_command creates command with message."""
    result = CommunicationCommandFactory.create_local_command(["Hello", "everyone"])
    
    assert isinstance(result, LocalCommand)
    assert result.message == "Hello everyone"


def test_create_local_command_message_too_long():
    """Test create_local_command raises error when message too long."""
    long_message = "a" * 501
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_local_command([long_message])
    
    assert "too long" in str(exc_info.value).lower()


def test_create_local_command_message_at_limit():
    """Test create_local_command accepts message at 500 character limit."""
    message = "a" * 500
    result = CommunicationCommandFactory.create_local_command([message])
    
    assert isinstance(result, LocalCommand)
    assert result.message == message


def test_create_system_command_no_args():
    """Test create_system_command raises error when no arguments."""
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_system_command([])
    
    assert "requires a message" in str(exc_info.value).lower()


def test_create_system_command_with_message():
    """Test create_system_command creates command with message."""
    result = CommunicationCommandFactory.create_system_command(["System", "message"])
    
    assert isinstance(result, SystemCommand)
    assert result.message == "System message"


def test_create_emote_command_no_args():
    """Test create_emote_command raises error when no arguments."""
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_emote_command([])
    
    assert "requires an action" in str(exc_info.value).lower()


def test_create_emote_command_with_action():
    """Test create_emote_command creates command with action."""
    result = CommunicationCommandFactory.create_emote_command(["waves", "hello"])
    
    assert isinstance(result, EmoteCommand)
    assert result.action == "waves hello"


def test_create_me_command_no_args():
    """Test create_me_command raises error when no arguments."""
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_me_command([])
    
    assert "requires an action" in str(exc_info.value).lower()


def test_create_me_command_with_action():
    """Test create_me_command creates command with action."""
    result = CommunicationCommandFactory.create_me_command(["sits", "down"])
    
    assert isinstance(result, MeCommand)
    assert result.action == "sits down"


def test_create_pose_command_no_args():
    """Test create_pose_command creates command with None pose."""
    result = CommunicationCommandFactory.create_pose_command([])
    
    assert isinstance(result, PoseCommand)
    assert result.pose is None


def test_create_pose_command_with_pose():
    """Test create_pose_command creates command with pose."""
    result = CommunicationCommandFactory.create_pose_command(["is", "standing", "tall"])
    
    assert isinstance(result, PoseCommand)
    assert result.pose == "is standing tall"


def test_create_whisper_command_no_args():
    """Test create_whisper_command raises error when no arguments."""
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_whisper_command([])
    
    assert "Usage: whisper" in str(exc_info.value)


def test_create_whisper_command_target_only():
    """Test create_whisper_command raises error when only target provided."""
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_whisper_command(["player"])
    
    assert "must provide a message" in str(exc_info.value).lower()


def test_create_whisper_command_empty_message():
    """Test create_whisper_command raises error when message is empty."""
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_whisper_command(["player", ""])
    
    assert "must provide a message" in str(exc_info.value).lower()


def test_create_whisper_command_whitespace_only_message():
    """Test create_whisper_command raises error when message is whitespace only."""
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_whisper_command(["player", "   "])
    
    assert "must provide a message" in str(exc_info.value).lower()


def test_create_whisper_command_with_target_and_message():
    """Test create_whisper_command creates command with target and message."""
    result = CommunicationCommandFactory.create_whisper_command(["player", "Hello", "there"])
    
    assert isinstance(result, WhisperCommand)
    assert result.target == "player"
    assert result.message == "Hello there"


def test_create_whisper_command_message_too_long():
    """Test create_whisper_command raises error when message too long."""
    long_message = "a" * 501
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_whisper_command(["player", long_message])
    
    assert "too long" in str(exc_info.value).lower()


def test_create_whisper_command_message_at_limit():
    """Test create_whisper_command accepts message at 500 character limit."""
    message = "a" * 500
    result = CommunicationCommandFactory.create_whisper_command(["player", message])
    
    assert isinstance(result, WhisperCommand)
    assert result.message == message


def test_create_reply_command_no_args():
    """Test create_reply_command raises error when no arguments."""
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_reply_command([])
    
    assert "Usage: reply" in str(exc_info.value)


def test_create_reply_command_empty_message():
    """Test create_reply_command raises error when message is empty."""
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_reply_command([""])
    
    assert "Usage: reply" in str(exc_info.value)


def test_create_reply_command_whitespace_only_message():
    """Test create_reply_command raises error when message is whitespace only."""
    with pytest.raises(MythosValidationError) as exc_info:
        CommunicationCommandFactory.create_reply_command(["   "])
    
    assert "Usage: reply" in str(exc_info.value)


def test_create_reply_command_with_message():
    """Test create_reply_command creates command with message."""
    result = CommunicationCommandFactory.create_reply_command(["Hello", "back"])
    
    assert isinstance(result, ReplyCommand)
    assert result.message == "Hello back"
