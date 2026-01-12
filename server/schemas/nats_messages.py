"""
Pydantic schemas for NATS message validation.

This module provides type-safe message schemas for all NATS message types,
ensuring message structure consistency and preventing invalid messages from
being published or processed.

AI: Schema validation prevents malformed messages and provides clear error messages.
"""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, field_validator


class BaseMessageSchema(BaseModel):
    """Base schema for all NATS messages."""

    message_id: str = Field(..., description="Unique message identifier")
    timestamp: str = Field(..., description="ISO format timestamp")
    sender_id: str | None = Field(None, description="Sender player ID")
    sender_name: str | None = Field(None, description="Sender player name")

    @field_validator("timestamp")
    @classmethod
    def validate_timestamp(cls, v: str) -> str:
        """Validate timestamp is valid ISO format."""
        try:
            datetime.fromisoformat(v.replace("Z", "+00:00"))
        except (ValueError, AttributeError) as err:
            raise ValueError("Timestamp must be valid ISO format") from err
        return v

    model_config = {"extra": "forbid", "strict": True}


class ChatMessageSchema(BaseMessageSchema):
    """Schema for chat messages."""

    channel: str = Field(..., description="Chat channel (say, local, global, whisper, etc.)")
    content: str = Field(..., description="Message content", min_length=1, max_length=10000)
    room_id: str | None = Field(None, description="Room ID for room-scoped messages")
    subzone: str | None = Field(None, description="Subzone for subzone-scoped messages")
    target_id: str | None = Field(None, description="Target player ID for whisper messages")
    target_name: str | None = Field(None, description="Target player name for whisper messages")

    @field_validator("channel")
    @classmethod
    def validate_channel(cls, v: str) -> str:
        """Validate channel is a known chat channel."""
        valid_channels = {"say", "local", "global", "whisper", "emote", "pose", "system", "admin", "party"}
        if v not in valid_channels:
            raise ValueError(f"Invalid channel: {v}. Must be one of {valid_channels}")
        return v


class EventMessageSchema(BaseMessageSchema):
    """Schema for event messages."""

    event_type: str = Field(..., description="Event type identifier")
    event_data: dict[str, Any] = Field(..., description="Event-specific data")
    room_id: str | None = Field(None, description="Room ID for room-scoped events")
    player_id: str | None = Field(None, description="Player ID for player-scoped events")

    @field_validator("event_type")
    @classmethod
    def validate_event_type(cls, v: str) -> str:
        """Validate event type is not empty."""
        if not v or not v.strip():
            raise ValueError("Event type cannot be empty")
        return v.strip()


def validate_chat_message(data: dict[str, Any]) -> ChatMessageSchema:
    """
    Validate a chat message against the schema.

    Args:
        data: Message data dictionary

    Returns:
        Validated ChatMessageSchema instance

    Raises:
        ValueError: If message validation fails
    """
    return ChatMessageSchema(**data)


def validate_event_message(data: dict[str, Any]) -> EventMessageSchema:
    """
    Validate an event message against the schema.

    Args:
        data: Message data dictionary

    Returns:
        Validated EventMessageSchema instance

    Raises:
        ValueError: If message validation fails
    """
    return EventMessageSchema(**data)


def validate_message(data: dict[str, Any], message_type: str = "chat") -> BaseMessageSchema:
    """
    Validate a message based on its type.

    Args:
        data: Message data dictionary
        message_type: Type of message ("chat" or "event")

    Returns:
        Validated message schema instance

    Raises:
        ValueError: If message validation fails or message type is unknown
    """
    if message_type == "chat":
        return validate_chat_message(data)
    if message_type == "event":
        return validate_event_message(data)
    raise ValueError(f"Unknown message type: {message_type}")
