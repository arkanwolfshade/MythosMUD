"""
Unit tests for communication command models.

Tests the communication command models and their validators.
"""

from unittest.mock import patch

import pytest
from pydantic import ValidationError

from server.models.command_communication import (
    EmoteCommand,
    LocalCommand,
    MeCommand,
    PoseCommand,
    ReplyCommand,
    SayCommand,
    SystemCommand,
    WhisperCommand,
)

# --- Tests for SayCommand ---


def test_say_command_required_fields():
    """Test SayCommand requires message."""
    with patch("server.models.command_communication.validate_message_content", return_value="Hello"):
        command = SayCommand(message="Hello")

        assert command.command_type == "say"
        assert command.message == "Hello"


def test_say_command_validate_message_calls_validator():
    """Test SayCommand calls validate_message_content."""
    with patch(
        "server.models.command_communication.validate_message_content", return_value="validated"
    ) as mock_validator:
        command = SayCommand(message="test")

        mock_validator.assert_called_once_with("test")
        assert command.message == "validated"


def test_say_command_message_min_length():
    """Test SayCommand validates message min length."""
    with patch("server.models.command_communication.validate_message_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            SayCommand(message="")


def test_say_command_message_max_length():
    """Test SayCommand validates message max length."""
    long_message = "a" * 501  # Exceeds max_length=500
    with patch("server.models.command_communication.validate_message_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            SayCommand(message=long_message)


# --- Tests for LocalCommand ---


def test_local_command_required_fields():
    """Test LocalCommand requires message."""
    with patch("server.models.command_communication.validate_message_content", return_value="Hello"):
        command = LocalCommand(message="Hello")

        assert command.command_type == "local"
        assert command.message == "Hello"


def test_local_command_validate_message_calls_validator():
    """Test LocalCommand calls validate_message_content."""
    with patch(
        "server.models.command_communication.validate_message_content", return_value="validated"
    ) as mock_validator:
        command = LocalCommand(message="test")

        mock_validator.assert_called_once_with("test")
        assert command.message == "validated"


def test_local_command_message_min_length():
    """Test LocalCommand validates message min length."""
    with patch("server.models.command_communication.validate_message_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            LocalCommand(message="")


def test_local_command_message_max_length():
    """Test LocalCommand validates message max length."""
    long_message = "a" * 501  # Exceeds max_length=500
    with patch("server.models.command_communication.validate_message_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            LocalCommand(message=long_message)


# --- Tests for SystemCommand ---


def test_system_command_required_fields():
    """Test SystemCommand requires message."""
    with patch("server.models.command_communication.validate_message_content", return_value="System message"):
        command = SystemCommand(message="System message")

        assert command.command_type == "system"
        assert command.message == "System message"


def test_system_command_validate_message_calls_validator():
    """Test SystemCommand calls validate_message_content."""
    with patch(
        "server.models.command_communication.validate_message_content", return_value="validated"
    ) as mock_validator:
        command = SystemCommand(message="test")

        mock_validator.assert_called_once_with("test")
        assert command.message == "validated"


def test_system_command_message_min_length():
    """Test SystemCommand validates message min length."""
    with patch("server.models.command_communication.validate_message_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            SystemCommand(message="")


def test_system_command_message_max_length():
    """Test SystemCommand validates message max length."""
    long_message = "a" * 2001  # Exceeds max_length=2000
    with patch("server.models.command_communication.validate_message_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            SystemCommand(message=long_message)


# --- Tests for EmoteCommand ---


def test_emote_command_required_fields():
    """Test EmoteCommand requires action."""
    with patch("server.models.command_communication.validate_action_content", return_value="waves"):
        command = EmoteCommand(action="waves")

        assert command.command_type == "emote"
        assert command.action == "waves"


def test_emote_command_validate_action_calls_validator():
    """Test EmoteCommand calls validate_action_content."""
    with patch(
        "server.models.command_communication.validate_action_content", return_value="validated"
    ) as mock_validator:
        command = EmoteCommand(action="test")

        mock_validator.assert_called_once_with("test")
        assert command.action == "validated"


def test_emote_command_action_min_length():
    """Test EmoteCommand validates action min length."""
    with patch("server.models.command_communication.validate_action_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            EmoteCommand(action="")


def test_emote_command_action_max_length():
    """Test EmoteCommand validates action max length."""
    long_action = "a" * 201  # Exceeds max_length=200
    with patch("server.models.command_communication.validate_action_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            EmoteCommand(action=long_action)


# --- Tests for MeCommand ---


def test_me_command_required_fields():
    """Test MeCommand requires action."""
    with patch("server.models.command_communication.validate_action_content", return_value="waves"):
        command = MeCommand(action="waves")

        assert command.command_type == "me"
        assert command.action == "waves"


def test_me_command_validate_action_calls_validator():
    """Test MeCommand calls validate_action_content."""
    with patch(
        "server.models.command_communication.validate_action_content", return_value="validated"
    ) as mock_validator:
        command = MeCommand(action="test")

        mock_validator.assert_called_once_with("test")
        assert command.action == "validated"


def test_me_command_action_min_length():
    """Test MeCommand validates action min length."""
    with patch("server.models.command_communication.validate_action_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            MeCommand(action="")


def test_me_command_action_max_length():
    """Test MeCommand validates action max length."""
    long_action = "a" * 201  # Exceeds max_length=200
    with patch("server.models.command_communication.validate_action_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            MeCommand(action=long_action)


# --- Tests for PoseCommand ---


def test_pose_command_required_fields():
    """Test PoseCommand requires pose."""
    with patch("server.models.command_communication.validate_pose_content", return_value="stands tall"):
        command = PoseCommand(pose="stands tall")

        assert command.command_type == "pose"
        assert command.pose == "stands tall"


def test_pose_command_validate_pose_calls_validator():
    """Test PoseCommand calls validate_pose_content."""
    with patch("server.models.command_communication.validate_pose_content", return_value="validated") as mock_validator:
        command = PoseCommand(pose="test")

        mock_validator.assert_called_once_with("test")
        assert command.pose == "validated"


def test_pose_command_pose_none():
    """Test PoseCommand accepts None for pose."""
    command = PoseCommand(pose=None)

    assert command.pose is None


def test_pose_command_pose_empty_string():
    """Test PoseCommand validates empty pose string."""
    # Empty string gets passed to validate_pose_content which may reject it
    with patch("server.models.command_communication.validate_pose_content", side_effect=ValueError("Invalid pose")):
        with pytest.raises(ValidationError):
            PoseCommand(pose="")


def test_pose_command_pose_max_length():
    """Test PoseCommand validates pose max length."""
    long_pose = "a" * 201  # Exceeds max_length=200
    with patch("server.models.command_communication.validate_pose_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            PoseCommand(pose=long_pose)


# --- Tests for WhisperCommand ---


def test_whisper_command_required_fields():
    """Test WhisperCommand requires target and message."""
    with (
        patch("server.models.command_communication.validate_target_player", return_value="player1"),
        patch("server.models.command_communication.validate_message_content", return_value="secret"),
    ):
        command = WhisperCommand(target="player1", message="secret")

        assert command.command_type == "whisper"
        assert command.target == "player1"
        assert command.message == "secret"


def test_whisper_command_validate_target_calls_validator():
    """Test WhisperCommand calls validate_target_player."""
    with (
        patch("server.models.command_communication.validate_target_player", return_value="validated") as mock_validator,
        patch("server.models.command_communication.validate_message_content", return_value="message"),
    ):
        command = WhisperCommand(target="test", message="message")

        mock_validator.assert_called_once_with("test")
        assert command.target == "validated"


def test_whisper_command_validate_message_calls_validator():
    """Test WhisperCommand calls validate_message_content."""
    with (
        patch("server.models.command_communication.validate_target_player", return_value="target"),
        patch(
            "server.models.command_communication.validate_message_content", return_value="validated"
        ) as mock_validator,
    ):
        command = WhisperCommand(target="target", message="test")

        mock_validator.assert_called_once_with("test")
        assert command.message == "validated"


def test_whisper_command_target_min_length():
    """Test WhisperCommand validates target min length."""
    with patch("server.models.command_communication.validate_target_player", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            WhisperCommand(target="", message="message")


def test_whisper_command_message_min_length():
    """Test WhisperCommand validates message min length."""
    with patch("server.models.command_communication.validate_message_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            WhisperCommand(target="player1", message="")


def test_whisper_command_message_max_length():
    """Test WhisperCommand validates message max length."""
    long_message = "a" * 2001  # Exceeds max_length=2000
    with patch("server.models.command_communication.validate_message_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            WhisperCommand(target="player1", message=long_message)


# --- Tests for ReplyCommand ---


def test_reply_command_required_fields():
    """Test ReplyCommand requires message."""
    with patch("server.models.command_communication.validate_message_content", return_value="reply"):
        command = ReplyCommand(message="reply")

        assert command.command_type == "reply"
        assert command.message == "reply"


def test_reply_command_validate_message_calls_validator():
    """Test ReplyCommand calls validate_message_content."""
    with patch(
        "server.models.command_communication.validate_message_content", return_value="validated"
    ) as mock_validator:
        command = ReplyCommand(message="test")

        mock_validator.assert_called_once_with("test")
        assert command.message == "validated"


def test_reply_command_message_min_length():
    """Test ReplyCommand validates message min length."""
    with patch("server.models.command_communication.validate_message_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            ReplyCommand(message="")


def test_reply_command_message_max_length():
    """Test ReplyCommand validates message max length."""
    long_message = "a" * 2001  # Exceeds max_length=2000
    with patch("server.models.command_communication.validate_message_content", side_effect=ValidationError):
        with pytest.raises(ValidationError):
            ReplyCommand(message=long_message)
