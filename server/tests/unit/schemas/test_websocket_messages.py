"""
Unit tests for websocket message schemas.

Tests the Pydantic schemas in websocket_messages.py.
"""

import pytest

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
    message = CommandMessage(data={"command": "look", "args": []})
    assert message.type == "command"
    assert message.data == {"command": "look", "args": []}


def test_command_message_data():
    """Test CommandMessageData schema."""
    data = CommandMessageData(command="look", args=["north"])
    assert data.command == "look"
    assert data.args == ["north"]


def test_chat_message():
    """Test ChatMessage schema."""
    message = ChatMessage(data={"message": "Hello"})
    assert message.type == "chat"
    assert message.data == {"message": "Hello"}


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
