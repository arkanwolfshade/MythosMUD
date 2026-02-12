"""
Pydantic schemas for WebSocket messages.

These schemas define the structure and validation rules for all WebSocket
message types used in the MythosMUD real-time communication system.
"""

# pylint: disable=unused-import  # noqa: F401# JUSTIFICATION: ConfigDict is used in model_config attributes (lines 41, 57, 65).
# Pylint incorrectly flags it as unused because it doesn't recognize model_config as a Pydantic special attribute.
from pydantic import BaseModel, ConfigDict, Field


class BaseWebSocketMessage(BaseModel):
    """Base class for all WebSocket messages."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    type: str = Field(..., description="Message type identifier")
    csrfToken: str | None = Field(None, alias="csrfToken", description="CSRF token for security")
    timestamp: int | None = Field(None, description="Message timestamp")


class CommandMessageData(BaseModel):
    """Schema for command message data."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    command: str = Field(..., description="Command string", min_length=1, max_length=200)
    args: list[str] = Field(default_factory=list, description="Command arguments")


class ChatMessageData(BaseModel):
    """Schema for chat message data."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    message: str = Field(..., description="Chat message content", min_length=1, max_length=1000)
    channel: str | None = Field(None, description="Chat channel")


class CommandMessage(BaseWebSocketMessage):
    """Schema for command messages from client."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        populate_by_name=True,
    )

    type: str = Field(default="command", description="Message type")
    data: CommandMessageData = Field(..., description="Command data")


class ChatMessage(BaseWebSocketMessage):
    """Schema for chat messages from client."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        populate_by_name=True,
    )

    type: str = Field(default="chat", description="Message type")
    data: ChatMessageData = Field(..., description="Chat message data")


class PingMessage(BaseWebSocketMessage):
    """Schema for ping/heartbeat messages."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        populate_by_name=True,
    )

    type: str = Field(default="ping", description="Message type")


class WrappedMessage(BaseModel):
    """Schema for wrapped messages from useWebSocketConnection."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        populate_by_name=True,
    )

    message: str = Field(..., description="Inner message as JSON string")
    csrfToken: str | None = Field(None, alias="csrfToken", description="CSRF token")
    timestamp: int | None = Field(None, description="Message timestamp")
