"""
Communication command models for MythosMUD.

This module provides command models for various communication channels.
"""

from typing import Literal

from pydantic import Field, field_validator

from ..validators.security_validator import (
    validate_action_content,
    validate_message_content,
    validate_pose_content,
    validate_target_player,
)
from .command_base import BaseCommand, CommandType


class SayCommand(BaseCommand):
    """Command for saying something to other players in the room."""

    command_type: Literal[CommandType.SAY] = CommandType.SAY
    message: str = Field(..., min_length=1, max_length=500, description="Message to say")

    @field_validator("message")
    @classmethod
    def validate_message(cls: type["SayCommand"], v: str) -> str:
        """Validate message content for security using centralized validation."""
        return validate_message_content(v)


class LocalCommand(BaseCommand):
    """Command for speaking in the local channel (sub-zone)."""

    command_type: Literal[CommandType.LOCAL] = CommandType.LOCAL
    message: str = Field(..., min_length=1, max_length=500, description="Message to send to local channel")

    @field_validator("message")
    @classmethod
    def validate_message(cls: type["LocalCommand"], v: str) -> str:
        """Validate message content for security using centralized validation."""
        return validate_message_content(v)


class SystemCommand(BaseCommand):
    """Command for sending system messages (admin only)."""

    command_type: Literal[CommandType.SYSTEM] = CommandType.SYSTEM
    message: str = Field(..., min_length=1, max_length=2000, description="System message to broadcast")

    @field_validator("message")
    @classmethod
    def validate_message(cls: type["SystemCommand"], v: str) -> str:
        """Validate system message content for security using centralized validation."""
        return validate_message_content(v)


class EmoteCommand(BaseCommand):
    """Command for performing an emote or action."""

    command_type: Literal[CommandType.EMOTE] = CommandType.EMOTE
    action: str = Field(..., min_length=1, max_length=200, description="Action to perform")

    @field_validator("action")
    @classmethod
    def validate_action(cls: type["EmoteCommand"], v: str) -> str:
        """Validate emote action for security using centralized validation."""
        return validate_action_content(v)


class MeCommand(BaseCommand):
    """Command for describing an action (alternative to emote)."""

    command_type: Literal[CommandType.ME] = CommandType.ME
    action: str = Field(..., min_length=1, max_length=200, description="Action to describe")

    @field_validator("action")
    @classmethod
    def validate_action(cls: type["MeCommand"], v: str) -> str:
        """Validate me action for security using centralized validation."""
        return validate_action_content(v)


class PoseCommand(BaseCommand):
    """Command for setting or displaying pose/status."""

    command_type: Literal[CommandType.POSE] = CommandType.POSE
    pose: str | None = Field(None, max_length=100, description="Pose description")

    @field_validator("pose")
    @classmethod
    def validate_pose(cls: type["PoseCommand"], v: str | None) -> str | None:
        """Validate pose description for security using centralized validation."""
        if v is None:
            return v
        return validate_pose_content(v)


class WhisperCommand(BaseCommand):
    """Command for whispering to a specific player."""

    command_type: Literal[CommandType.WHISPER] = CommandType.WHISPER
    target: str = Field(..., min_length=1, max_length=50, description="Target player name")
    message: str = Field(..., min_length=1, max_length=2000, description="Whisper message content")

    @field_validator("target")
    @classmethod
    def validate_target(cls: type["WhisperCommand"], v: str) -> str:
        """Validate target player name format using centralized validation."""
        return validate_target_player(v)

    @field_validator("message")
    @classmethod
    def validate_message(cls: type["WhisperCommand"], v: str) -> str:
        """Validate message content for security using centralized validation."""
        return validate_message_content(v)


class ReplyCommand(BaseCommand):
    """Command for replying to the last whisper received."""

    command_type: Literal[CommandType.REPLY] = CommandType.REPLY
    message: str = Field(..., min_length=1, max_length=2000, description="Reply message content")

    @field_validator("message")
    @classmethod
    def validate_message(cls: type["ReplyCommand"], v: str) -> str:
        """Validate message content for security using centralized validation."""
        return validate_message_content(v)
