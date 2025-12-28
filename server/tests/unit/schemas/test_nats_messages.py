"""
Unit tests for nats_messages schemas.

Tests the Pydantic models and validation functions for NATS messages.
"""

from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from server.schemas.nats_messages import (
    BaseMessageSchema,
    ChatMessageSchema,
    EventMessageSchema,
    validate_chat_message,
    validate_event_message,
    validate_message,
)


def test_base_message_schema():
    """Test BaseMessageSchema can be instantiated."""
    timestamp = datetime.now(UTC).isoformat()
    message = BaseMessageSchema(message_id="msg_001", timestamp=timestamp)

    assert message.message_id == "msg_001"
    assert message.timestamp == timestamp
    assert message.sender_id is None
    assert message.sender_name is None


def test_base_message_schema_validate_timestamp():
    """Test BaseMessageSchema validates timestamp format."""
    timestamp = datetime.now(UTC).isoformat()

    message = BaseMessageSchema(message_id="msg_001", timestamp=timestamp)

    assert message.timestamp == timestamp


def test_base_message_schema_invalid_timestamp():
    """Test BaseMessageSchema raises error for invalid timestamp."""
    with pytest.raises(ValidationError):
        BaseMessageSchema(message_id="msg_001", timestamp="invalid")


def test_chat_message_schema():
    """Test ChatMessageSchema can be instantiated."""
    timestamp = datetime.now(UTC).isoformat()
    message = ChatMessageSchema(
        message_id="msg_001",
        timestamp=timestamp,
        channel="say",
        content="Hello",
    )

    assert message.channel == "say"
    assert message.content == "Hello"


def test_chat_message_schema_validate_channel():
    """Test ChatMessageSchema validates channel."""
    timestamp = datetime.now(UTC).isoformat()

    message = ChatMessageSchema(
        message_id="msg_001",
        timestamp=timestamp,
        channel="say",
        content="Hello",
    )

    assert message.channel == "say"


def test_chat_message_schema_invalid_channel():
    """Test ChatMessageSchema raises error for invalid channel."""
    timestamp = datetime.now(UTC).isoformat()

    with pytest.raises(ValidationError):
        ChatMessageSchema(
            message_id="msg_001",
            timestamp=timestamp,
            channel="invalid_channel",
            content="Hello",
        )


def test_chat_message_schema_content_validation():
    """Test ChatMessageSchema validates content length."""
    timestamp = datetime.now(UTC).isoformat()

    with pytest.raises(ValidationError):
        ChatMessageSchema(
            message_id="msg_001",
            timestamp=timestamp,
            channel="say",
            content="",
        )


def test_event_message_schema():
    """Test EventMessageSchema can be instantiated."""
    timestamp = datetime.now(UTC).isoformat()
    message = EventMessageSchema(
        message_id="msg_001",
        timestamp=timestamp,
        event_type="player_entered",
        event_data={},
    )

    assert message.event_type == "player_entered"
    assert message.event_data == {}


def test_event_message_schema_validate_event_type():
    """Test EventMessageSchema validates event_type."""
    timestamp = datetime.now(UTC).isoformat()

    message = EventMessageSchema(
        message_id="msg_001",
        timestamp=timestamp,
        event_type="player_entered",
        event_data={},
    )

    assert message.event_type == "player_entered"


def test_event_message_schema_empty_event_type():
    """Test EventMessageSchema raises error for empty event_type."""
    timestamp = datetime.now(UTC).isoformat()

    with pytest.raises(ValidationError):
        EventMessageSchema(
            message_id="msg_001",
            timestamp=timestamp,
            event_type="",
            event_data={},
        )


def test_validate_chat_message():
    """Test validate_chat_message() validates and returns schema."""
    timestamp = datetime.now(UTC).isoformat()
    data = {
        "message_id": "msg_001",
        "timestamp": timestamp,
        "channel": "say",
        "content": "Hello",
    }

    result = validate_chat_message(data)

    assert isinstance(result, ChatMessageSchema)
    assert result.channel == "say"
    assert result.content == "Hello"


def test_validate_event_message():
    """Test validate_event_message() validates and returns schema."""
    timestamp = datetime.now(UTC).isoformat()
    data = {
        "message_id": "msg_001",
        "timestamp": timestamp,
        "event_type": "player_entered",
        "event_data": {},
    }

    result = validate_event_message(data)

    assert isinstance(result, EventMessageSchema)
    assert result.event_type == "player_entered"


def test_validate_message_chat():
    """Test validate_message() with chat type."""
    timestamp = datetime.now(UTC).isoformat()
    data = {
        "message_id": "msg_001",
        "timestamp": timestamp,
        "channel": "say",
        "content": "Hello",
    }

    result = validate_message(data, message_type="chat")

    assert isinstance(result, ChatMessageSchema)


def test_validate_message_event():
    """Test validate_message() with event type."""
    timestamp = datetime.now(UTC).isoformat()
    data = {
        "message_id": "msg_001",
        "timestamp": timestamp,
        "event_type": "player_entered",
        "event_data": {},
    }

    result = validate_message(data, message_type="event")

    assert isinstance(result, EventMessageSchema)
