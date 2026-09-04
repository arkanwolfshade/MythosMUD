"""
Unit tests for message handler factory.

Tests the message_handler_factory module classes and functions. `handle_message` and each
`MessageHandler.handle` dispatch validated, typed envelope messages (see
`server/schemas/realtime/websocket_messages.py`, `#765`), not raw dicts.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.message_handler_factory import (
    ChatMessageHandler,
    ClientErrorReportMessageHandler,
    CommandMessageHandler,
    MessageHandlerFactory,
    PingMessageHandler,
    message_handler_factory,
)
from server.schemas.realtime.websocket_messages import (
    ChatData,
    ChatMessage,
    ClientErrorReportData,
    ClientErrorReportMessage,
    CommandData,
    CommandMessage,
    PingMessage,
)

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.mark.asyncio
async def test_command_message_handler_handle():
    """Test CommandMessageHandler.handle() calls handle_command_message."""
    mock_websocket = AsyncMock()
    player_id = "player_123"
    message = CommandMessage(type="command", data=CommandData(command="look"))

    with patch("server.realtime.message_handlers.handle_command_message") as mock_handle:
        handler = CommandMessageHandler()
        await handler.handle(mock_websocket, player_id, message)

        mock_handle.assert_called_once_with(mock_websocket, player_id, message)


@pytest.mark.asyncio
async def test_command_message_handler_rejects_wrong_type():
    """Test CommandMessageHandler.handle() raises TypeError for a mismatched message."""
    mock_websocket = AsyncMock()
    handler = CommandMessageHandler()

    with pytest.raises(TypeError):
        await handler.handle(mock_websocket, "player_123", ChatMessage(type="chat"))


@pytest.mark.asyncio
async def test_chat_message_handler_handle():
    """Test ChatMessageHandler.handle() calls handle_chat_message."""
    mock_websocket = AsyncMock()
    player_id = "player_123"
    message = ChatMessage(type="chat", data=ChatData(message="Hello"))

    with patch("server.realtime.message_handlers.handle_chat_message") as mock_handle:
        handler = ChatMessageHandler()
        await handler.handle(mock_websocket, player_id, message)

        mock_handle.assert_called_once_with(mock_websocket, player_id, message)


@pytest.mark.asyncio
async def test_ping_message_handler_handle():
    """Test PingMessageHandler.handle() calls handle_ping_message."""
    mock_websocket = AsyncMock()
    player_id = "player_123"
    message = PingMessage(type="ping")

    with patch("server.realtime.message_handlers.handle_ping_message") as mock_handle:
        handler = PingMessageHandler()
        await handler.handle(mock_websocket, player_id, message)

        mock_handle.assert_called_once_with(mock_websocket, player_id, message)


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
    message = CommandMessage(type="command", data=CommandData(command="look"))

    with patch("server.realtime.message_handlers.handle_command_message") as mock_handle:
        await factory.handle_message(mock_websocket, player_id, message)

        mock_handle.assert_called_once()


@pytest.mark.asyncio
async def test_message_handler_factory_handle_message_unknown_type():
    """
    Test MessageHandlerFactory.handle_message() sends error for an unregistered type.

    `WebSocketInboundMessage`'s discriminator only admits registered types, so this branch is
    unreachable via a real validated message (see the drift guard test) — exercised here with a
    stand-in object to cover the defence-in-depth path for a caller that bypasses validation.
    """
    factory = MessageHandlerFactory()
    mock_websocket = AsyncMock()
    player_id = "player_123"
    message = MagicMock(type="unknown")

    await factory.handle_message(mock_websocket, player_id, message)

    mock_websocket.send_json.assert_called_once()
    call_args = mock_websocket.send_json.call_args[0][0]
    assert call_args["type"] == "error"


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
    mock_websocket = AsyncMock()
    player_id = "player_456"
    message = ClientErrorReportMessage(
        type="client_error_report",
        data=ClientErrorReportData(
            error_type="occupants_panel_empty_players",
            message="Occupants panel players list is empty",
            context={"room_id": "room1", "player_name": "TestPlayer"},
        ),
    )

    with patch("server.realtime.message_handlers.logger") as mock_logger:
        handler = ClientErrorReportMessageHandler()
        await handler.handle(mock_websocket, player_id, message)

        mock_logger.error.assert_called_once()
        call_kwargs = mock_logger.error.call_args[1]
        assert call_kwargs["player_id"] == player_id
        assert call_kwargs["error_type"] == "occupants_panel_empty_players"
        assert "Occupants panel" in call_kwargs["message"]
        assert call_kwargs["context"]["room_id"] == "room1"
