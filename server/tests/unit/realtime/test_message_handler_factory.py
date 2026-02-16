"""
Unit tests for message handler factory.

Tests the message_handler_factory module classes and functions.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.message_handler_factory import (
    ChatMessageHandler,
    CommandMessageHandler,
    MessageHandlerFactory,
    PingMessageHandler,
    message_handler_factory,
)

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.mark.asyncio
async def test_command_message_handler_handle():
    """Test CommandMessageHandler.handle() calls handle_command_message."""
    mock_websocket = AsyncMock()
    player_id = "player_123"
    data = {"command": "look"}

    with patch("server.realtime.message_handlers.handle_command_message") as mock_handle:
        handler = CommandMessageHandler()
        await handler.handle(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, data)


@pytest.mark.asyncio
async def test_chat_message_handler_handle():
    """Test ChatMessageHandler.handle() calls handle_chat_message."""
    mock_websocket = AsyncMock()
    player_id = "player_123"
    data = {"message": "Hello"}

    with patch("server.realtime.message_handlers.handle_chat_message") as mock_handle:
        handler = ChatMessageHandler()
        await handler.handle(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, data)


@pytest.mark.asyncio
async def test_ping_message_handler_handle():
    """Test PingMessageHandler.handle() calls handle_ping_message."""
    mock_websocket = AsyncMock()
    player_id = "player_123"
    from typing import Any

    data: dict[str, Any] = {}

    with patch("server.realtime.message_handlers.handle_ping_message") as mock_handle:
        handler = PingMessageHandler()
        await handler.handle(mock_websocket, player_id, data)

        mock_handle.assert_called_once_with(mock_websocket, player_id, data)


def test_message_handler_factory_init():
    """Test MessageHandlerFactory.__init__() initializes with default handlers."""
    factory = MessageHandlerFactory()

    assert "command" in factory._handlers
    assert "game_command" in factory._handlers
    assert "chat" in factory._handlers
    assert "ping" in factory._handlers


def test_message_handler_factory_register_handler():
    """Test MessageHandlerFactory.register_handler() registers new handler."""
    factory = MessageHandlerFactory()
    mock_handler = MagicMock()

    factory.register_handler("custom", mock_handler)

    assert factory._handlers["custom"] == mock_handler


def test_message_handler_factory_get_handler_found():
    """Test MessageHandlerFactory.get_handler() returns handler when found."""
    factory = MessageHandlerFactory()

    handler = factory.get_handler("command")

    assert handler is not None
    assert isinstance(handler, CommandMessageHandler)


def test_message_handler_factory_get_handler_not_found():
    """Test MessageHandlerFactory.get_handler() returns None when not found."""
    factory = MessageHandlerFactory()

    handler = factory.get_handler("unknown")

    assert handler is None


@pytest.mark.asyncio
async def test_message_handler_factory_handle_message_success():
    """Test MessageHandlerFactory.handle_message() successfully handles message."""
    factory = MessageHandlerFactory()
    mock_websocket = AsyncMock()
    player_id = "player_123"
    message = {"type": "command", "data": {"command": "look"}}

    with patch("server.realtime.message_handlers.handle_command_message") as mock_handle:
        await factory.handle_message(mock_websocket, player_id, message)

        mock_handle.assert_called_once()


@pytest.mark.asyncio
async def test_message_handler_factory_handle_message_unknown_type():
    """Test MessageHandlerFactory.handle_message() sends error for unknown type."""
    factory = MessageHandlerFactory()
    mock_websocket = AsyncMock()
    player_id = "player_123"
    message = {"type": "unknown", "data": {}}

    await factory.handle_message(mock_websocket, player_id, message)

    mock_websocket.send_json.assert_called_once()
    call_args = mock_websocket.send_json.call_args[0][0]
    assert call_args["type"] == "error"


@pytest.mark.asyncio
async def test_message_handler_factory_handle_message_no_type():
    """Test MessageHandlerFactory.handle_message() handles message with no type."""
    factory = MessageHandlerFactory()
    mock_websocket = AsyncMock()
    player_id = "player_123"
    from typing import Any

    message: dict[str, Any] = {"data": {}}

    await factory.handle_message(mock_websocket, player_id, message)

    mock_websocket.send_json.assert_called_once()


def test_message_handler_factory_get_supported_message_types():
    """Test MessageHandlerFactory.get_supported_message_types() returns list of types."""
    factory = MessageHandlerFactory()

    types = factory.get_supported_message_types()

    assert isinstance(types, list)
    assert "command" in types
    assert "chat" in types
    assert "ping" in types
    assert "client_error_report" in types


def test_message_handler_factory_game_command_alias():
    """Test MessageHandlerFactory handles game_command as alias for command."""
    factory = MessageHandlerFactory()

    handler1 = factory.get_handler("command")
    handler2 = factory.get_handler("game_command")

    # Both should be CommandMessageHandler instances (may be different instances)
    assert isinstance(handler1, CommandMessageHandler)
    assert isinstance(handler2, CommandMessageHandler)
    # They should have the same type
    assert type(handler1) is type(handler2)


def test_global_message_handler_factory():
    """Test global message_handler_factory instance exists."""

    assert isinstance(message_handler_factory, MessageHandlerFactory)


@pytest.mark.asyncio
async def test_client_error_report_handler_logs():
    """Test ClientErrorReportMessageHandler logs via logger.error."""
    from server.realtime.message_handler_factory import ClientErrorReportMessageHandler

    mock_websocket = AsyncMock()
    player_id = "player_456"
    data = {
        "error_type": "occupants_panel_empty_players",
        "message": "Occupants panel players list is empty",
        "context": {"room_id": "room1", "player_name": "TestPlayer"},
    }

    with patch("server.realtime.message_handlers.logger") as mock_logger:
        handler = ClientErrorReportMessageHandler()
        await handler.handle(mock_websocket, player_id, data)

        mock_logger.error.assert_called_once()
        call_kwargs = mock_logger.error.call_args[1]
        assert call_kwargs["player_id"] == player_id
        assert call_kwargs["error_type"] == "occupants_panel_empty_players"
        assert "Occupants panel" in call_kwargs["message"]
        assert call_kwargs["context"]["room_id"] == "room1"
