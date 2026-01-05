"""
Chat message model for MythosMUD.

This module provides the ChatMessage class which represents a chat message
with metadata for serialization and logging.
"""

import uuid
from datetime import UTC, datetime
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger("communications.chat_message")


class ChatMessage:
    """Represents a chat message with metadata."""

    def __init__(
        self,
        sender_id: uuid.UUID | str,
        sender_name: str,
        channel: str,
        content: str,
        target_id: uuid.UUID | str | None = None,
        target_name: str | None = None,
    ):
        self.id = str(uuid.uuid4())
        # Convert UUID to string for JSON serialization
        self.sender_id = str(sender_id) if isinstance(sender_id, uuid.UUID) else sender_id
        self.sender_name = sender_name
        self.channel = channel
        self.content = content
        # Convert UUID to string for JSON serialization
        # Type annotation ensures mypy knows this is str | None after conversion
        if target_id is None:
            self.target_id: str | None = None
        elif isinstance(target_id, uuid.UUID):
            self.target_id = str(target_id)
        else:
            self.target_id = target_id
        self.target_name = target_name
        self.timestamp = datetime.now(UTC)
        self.echo_sent = False

    def to_dict(self) -> dict[str, Any]:
        """Convert message to dictionary for serialization."""
        result: dict[str, Any] = {
            "id": self.id,
            "sender_id": self.sender_id,
            "sender_name": self.sender_name,
            "channel": self.channel,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
        }

        # Add target information for whisper messages
        if self.target_id:
            result["target_id"] = self.target_id
        if self.target_name:
            result["target_name"] = self.target_name

        # Indicate metadata flags when present
        if getattr(self, "echo_sent", False):
            result["echo_sent"] = True

        return result

    def log_message(self) -> None:
        """Log this chat message to the communications log."""
        log_data = {
            "message_id": self.id,
            "sender_id": self.sender_id,
            "sender_name": self.sender_name,
            "channel": self.channel,
            "content": self.content,
            "timestamp": self.timestamp.isoformat(),
        }

        # Add target information for whisper messages
        if self.target_id:
            log_data["target_id"] = self.target_id
        if self.target_name:
            log_data["target_name"] = self.target_name

        logger.info("CHAT MESSAGE", **log_data)
