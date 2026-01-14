"""
Unit tests for websocket message schemas.

Tests the Pydantic schemas in websocket_messages.py.
"""

import pytest
from pydantic import ValidationError

from server.schemas.websocket_messages import (
    BaseWebSocketMessage,
    ChatMessage,
    ChatMessageData,
    CommandMessage,
    CommandMessageData,
    PingMessage,
    WrappedMessage,
)


def test_base_websocket_message():
    """Test BaseWebSocketMessage schema."""
    message = BaseWebSocketMessage(type="test")
    assert message.type == "test"
    assert message.csrfToken is None


def test_command_message():
    """Test CommandMessage schema."""
    data = CommandMessageData(command="look", args=[])
    message = CommandMessage(data=data)
    assert message.type == "command"
    # Access via getattr to avoid FieldInfo type inference issue
    message_data = getattr(message, "data")  # noqa: B009  # Reason: Using getattr to work around Pydantic Field typing limitation
    assert isinstance(message_data, CommandMessageData)
    assert message_data.command == "look"
    assert message_data.args == []


def test_command_message_data():
    """Test CommandMessageData schema."""
    data = CommandMessageData(command="look", args=["north"])
    assert data.command == "look"
    assert data.args == ["north"]


def test_chat_message():
    """Test ChatMessage schema."""
    data = ChatMessageData(message="Hello")
    message = ChatMessage(data=data)
    assert message.type == "chat"
    # Access via getattr to avoid FieldInfo type inference issue
    message_data = getattr(message, "data")  # noqa: B009  # Reason: Using getattr to work around Pydantic Field typing limitation
    assert isinstance(message_data, ChatMessageData)
    assert message_data.message == "Hello"


def test_chat_message_data():
    """Test ChatMessageData schema."""
    data = ChatMessageData(message="Hello")
    assert data.message == "Hello"


def test_ping_message():
    """Test PingMessage schema."""
    message = PingMessage()
    assert message.type == "ping"


def test_wrapped_message():
    """Test WrappedMessage schema."""
    message = WrappedMessage(message='{"type": "test"}')
    assert message.message == '{"type": "test"}'


def test_base_websocket_message_with_csrf_token():
    """Test BaseWebSocketMessage with CSRF token."""
    message = BaseWebSocketMessage(type="test", csrfToken="token123")
    assert message.type == "test"
    assert message.csrfToken == "token123"


def test_base_websocket_message_with_timestamp():
    """Test BaseWebSocketMessage with timestamp."""
    message = BaseWebSocketMessage(type="test", timestamp=1234567890)
    assert message.type == "test"
    assert message.timestamp == 1234567890


def test_command_message_with_csrf_token():
    """Test CommandMessage with CSRF token."""
    data = CommandMessageData(command="look")
    message = CommandMessage(data=data, csrfToken="token123")
    assert message.type == "command"
    assert message.csrfToken == "token123"
    # Access via getattr to avoid FieldInfo type inference issue
    message_data = getattr(message, "data")  # noqa: B009  # Reason: Using getattr to work around Pydantic Field typing limitation
    assert isinstance(message_data, CommandMessageData)
    assert message_data.command == "look"


def test_command_message_data_empty_args():
    """Test CommandMessageData with empty args."""
    data = CommandMessageData(command="look", args=[])
    assert data.command == "look"
    assert data.args == []


def test_command_message_data_multiple_args():
    """Test CommandMessageData with multiple args."""
    data = CommandMessageData(command="go", args=["north", "east"])
    assert data.command == "go"
    assert data.args == ["north", "east"]


def test_command_message_data_validation_error():
    """Test CommandMessageData validation with empty command."""
    with pytest.raises(ValidationError):
        CommandMessageData(command="", args=[])


def test_chat_message_with_channel():
    """Test ChatMessage with channel."""
    data = ChatMessageData(message="Hello", channel="say")
    message = ChatMessage(data=data)
    assert message.type == "chat"
    # Access via getattr to avoid FieldInfo type inference issue
    message_data = getattr(message, "data")  # noqa: B009  # Reason: Using getattr to work around Pydantic Field typing limitation
    assert isinstance(message_data, ChatMessageData)
    assert message_data.message == "Hello"
    assert message_data.channel == "say"


def test_chat_message_data_with_channel():
    """Test ChatMessageData with channel."""
    data = ChatMessageData(message="Hello", channel="say")
    assert data.message == "Hello"
    assert data.channel == "say"


def test_chat_message_data_no_channel():
    """Test ChatMessageData without channel."""
    data = ChatMessageData(message="Hello")
    assert data.message == "Hello"
    assert data.channel is None


def test_chat_message_data_validation_error():
    """Test ChatMessageData validation with empty message."""
    with pytest.raises(ValidationError):
        ChatMessageData(message="")


def test_ping_message_with_csrf_token():
    """Test PingMessage with CSRF token."""
    message = PingMessage(csrfToken="token123")
    assert message.type == "ping"
    assert message.csrfToken == "token123"


def test_ping_message_with_timestamp():
    """Test PingMessage with timestamp."""
    message = PingMessage(timestamp=1234567890)
    assert message.type == "ping"
    assert message.timestamp == 1234567890


def test_wrapped_message_with_csrf_token():
    """Test WrappedMessage with CSRF token."""
    message = WrappedMessage(message='{"type": "test"}', csrfToken="token123")
    assert message.message == '{"type": "test"}'
    assert message.csrfToken == "token123"


def test_wrapped_message_with_timestamp():
    """Test WrappedMessage with timestamp."""
    message = WrappedMessage(message='{"type": "test"}', timestamp=1234567890)
    assert message.message == '{"type": "test"}'
    assert message.timestamp == 1234567890


def test_command_message_rejects_extra_fields():
    """Test CommandMessage rejects extra fields (extra='forbid')."""
    data = CommandMessageData(command="look")
    with pytest.raises(ValidationError):
        CommandMessage(data=data, extra_field="should_fail")


def test_chat_message_rejects_extra_fields():
    """Test ChatMessage rejects extra fields (extra='forbid')."""
    data = ChatMessageData(message="Hello")
    with pytest.raises(ValidationError):
        ChatMessage(data=data, extra_field="should_fail")
