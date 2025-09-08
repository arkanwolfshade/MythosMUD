"""
Tests for Message Handler Factory.

This module tests the factory pattern implementation for WebSocket message
routing, ensuring it correctly handles all message types and maintains
backward compatibility with existing functionality.
"""

from unittest.mock import AsyncMock, patch

import pytest
from fastapi import WebSocket

from ..error_types import ErrorType
from ..realtime.message_handler_factory import (
    ChatMessageHandler,
    CommandMessageHandler,
    MessageHandler,
    MessageHandlerFactory,
    PingMessageHandler,
    message_handler_factory,
)


class TestMessageHandlerFactory:
    """Test suite for Message Handler Factory."""

    @pytest.fixture
    def factory(self):
        """Create a fresh factory instance for testing."""
        return MessageHandlerFactory()

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock(spec=WebSocket)
        websocket.send_json = AsyncMock()
        return websocket

    def test_factory_initialization(self, factory):
        """Test that factory initializes with default handlers."""
        assert "command" in factory._handlers
        assert "chat" in factory._handlers
        assert "ping" in factory._handlers
        assert isinstance(factory._handlers["command"], CommandMessageHandler)
        assert isinstance(factory._handlers["chat"], ChatMessageHandler)
        assert isinstance(factory._handlers["ping"], PingMessageHandler)

    def test_register_handler(self, factory):
        """Test registering a new message handler."""

        class TestHandler(MessageHandler):
            async def handle(self, websocket, player_id, data):
                pass

        handler = TestHandler()
        factory.register_handler("test", handler)

        assert factory.get_handler("test") == handler

    def test_get_handler_existing(self, factory):
        """Test getting an existing handler."""
        handler = factory.get_handler("command")
        assert isinstance(handler, CommandMessageHandler)

    def test_get_handler_nonexistent(self, factory):
        """Test getting a non-existent handler."""
        handler = factory.get_handler("nonexistent")
        assert handler is None

    def test_get_supported_message_types(self, factory):
        """Test getting list of supported message types."""
        types = factory.get_supported_message_types()
        assert "command" in types
        assert "game_command" in types
        assert "chat" in types
        assert "ping" in types
        assert len(types) == 4

    @pytest.mark.asyncio
    async def test_handle_command_message(self, factory, mock_websocket):
        """Test handling command message through factory."""
        message = {"type": "command", "data": {"command": "look", "args": []}}

        with patch("server.realtime.websocket_handler.handle_game_command") as mock_handler:
            await factory.handle_message(mock_websocket, "test_player", message)

            mock_handler.assert_called_once_with(mock_websocket, "test_player", "look", [])

    @pytest.mark.asyncio
    async def test_handle_game_command_message(self, factory, mock_websocket):
        """Test handling game_command message through factory."""
        message = {"type": "game_command", "data": {"command": "look", "args": []}}

        with patch("server.realtime.websocket_handler.handle_game_command") as mock_handler:
            await factory.handle_message(mock_websocket, "test_player", message)

            mock_handler.assert_called_once_with(mock_websocket, "test_player", "look", [])

    @pytest.mark.asyncio
    async def test_handle_chat_message(self, factory, mock_websocket):
        """Test handling chat message through factory."""
        message = {"type": "chat", "data": {"message": "Hello, world!"}}

        with patch("server.realtime.websocket_handler.handle_chat_message") as mock_handler:
            await factory.handle_message(mock_websocket, "test_player", message)

            mock_handler.assert_called_once_with(mock_websocket, "test_player", "Hello, world!")

    @pytest.mark.asyncio
    async def test_handle_ping_message(self, factory, mock_websocket):
        """Test handling ping message through factory."""
        message = {"type": "ping", "data": {}}

        await factory.handle_message(mock_websocket, "test_player", message)

        # Verify pong event was sent with new envelope format
        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["event_type"] == "pong"
        assert "timestamp" in call_args
        assert "sequence_number" in call_args
        assert call_args["data"] == {}
        assert call_args["player_id"] == "test_player"

    @pytest.mark.asyncio
    async def test_handle_unknown_message_type(self, factory, mock_websocket):
        """Test handling unknown message type through factory."""
        message = {"type": "unknown_type", "data": {}}

        await factory.handle_message(mock_websocket, "test_player", message)

        # Verify error response was sent
        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["error_type"] == ErrorType.INVALID_COMMAND.value
        assert "Unknown message type: unknown_type" in call_args["message"]

    @pytest.mark.asyncio
    async def test_handle_message_missing_type(self, factory, mock_websocket):
        """Test handling message with missing type."""
        message = {"data": {}}

        await factory.handle_message(mock_websocket, "test_player", message)

        # Should treat as unknown type
        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["error_type"] == ErrorType.INVALID_COMMAND.value
        assert "Unknown message type: unknown" in call_args["message"]

    @pytest.mark.asyncio
    async def test_handle_message_missing_data(self, factory, mock_websocket):
        """Test handling message with missing data."""
        message = {"type": "command"}

        with patch("server.realtime.websocket_handler.handle_game_command") as mock_handler:
            await factory.handle_message(mock_websocket, "test_player", message)

            # Should use empty dict as default data
            mock_handler.assert_called_once_with(mock_websocket, "test_player", "", [])


class TestMessageHandlers:
    """Test suite for individual message handlers."""

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock(spec=WebSocket)
        websocket.send_json = AsyncMock()
        return websocket

    @pytest.mark.asyncio
    async def test_command_message_handler(self, mock_websocket):
        """Test CommandMessageHandler."""
        handler = CommandMessageHandler()
        data = {"command": "look", "args": ["north"]}

        with patch("server.realtime.websocket_handler.handle_game_command") as mock_handler:
            await handler.handle(mock_websocket, "test_player", data)

            mock_handler.assert_called_once_with(mock_websocket, "test_player", "look", ["north"])

    @pytest.mark.asyncio
    async def test_command_message_handler_missing_data(self, mock_websocket):
        """Test CommandMessageHandler with missing data."""
        handler = CommandMessageHandler()
        data = {}

        with patch("server.realtime.websocket_handler.handle_game_command") as mock_handler:
            await handler.handle(mock_websocket, "test_player", data)

            mock_handler.assert_called_once_with(mock_websocket, "test_player", "", [])

    @pytest.mark.asyncio
    async def test_chat_message_handler(self, mock_websocket):
        """Test ChatMessageHandler."""
        handler = ChatMessageHandler()
        data = {"message": "Hello, world!"}

        with patch("server.realtime.websocket_handler.handle_chat_message") as mock_handler:
            await handler.handle(mock_websocket, "test_player", data)

            mock_handler.assert_called_once_with(mock_websocket, "test_player", "Hello, world!")

    @pytest.mark.asyncio
    async def test_chat_message_handler_missing_data(self, mock_websocket):
        """Test ChatMessageHandler with missing data."""
        handler = ChatMessageHandler()
        data = {}

        with patch("server.realtime.websocket_handler.handle_chat_message") as mock_handler:
            await handler.handle(mock_websocket, "test_player", data)

            mock_handler.assert_called_once_with(mock_websocket, "test_player", "")

    @pytest.mark.asyncio
    async def test_ping_message_handler(self, mock_websocket):
        """Test PingMessageHandler."""
        handler = PingMessageHandler()
        data = {}

        await handler.handle(mock_websocket, "test_player", data)

        # Verify pong event was sent with new envelope format
        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["event_type"] == "pong"
        assert "timestamp" in call_args
        assert "sequence_number" in call_args
        assert call_args["data"] == {}
        assert call_args["player_id"] == "test_player"


class TestGlobalFactory:
    """Test suite for the global factory instance."""

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock(spec=WebSocket)
        websocket.send_json = AsyncMock()
        return websocket

    def test_global_factory_instance(self):
        """Test that global factory is properly initialized."""
        assert isinstance(message_handler_factory, MessageHandlerFactory)
        assert "command" in message_handler_factory._handlers
        assert "chat" in message_handler_factory._handlers
        assert "ping" in message_handler_factory._handlers

    @pytest.mark.asyncio
    async def test_global_factory_handles_command(self, mock_websocket):
        """Test that global factory handles command messages."""
        message = {"type": "command", "data": {"command": "look", "args": []}}

        with patch("server.realtime.websocket_handler.handle_game_command") as mock_handler:
            await message_handler_factory.handle_message(mock_websocket, "test_player", message)

            mock_handler.assert_called_once_with(mock_websocket, "test_player", "look", [])

    @pytest.mark.asyncio
    async def test_global_factory_handles_unknown_type(self, mock_websocket):
        """Test that global factory handles unknown message types."""
        message = {"type": "unknown_type", "data": {}}

        await message_handler_factory.handle_message(mock_websocket, "test_player", message)

        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["error_type"] == ErrorType.INVALID_COMMAND.value


class TestFactoryExtensibility:
    """Test suite for factory extensibility features."""

    @pytest.fixture
    def factory(self):
        """Create a fresh factory instance for testing."""
        return MessageHandlerFactory()

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock(spec=WebSocket)
        websocket.send_json = AsyncMock()
        return websocket

    @pytest.mark.asyncio
    async def test_custom_handler_registration(self, factory, mock_websocket):
        """Test registering and using a custom handler."""

        class CustomHandler(MessageHandler):
            def __init__(self):
                self.called = False
                self.called_with = None

            async def handle(self, websocket, player_id, data):
                self.called = True
                self.called_with = (websocket, player_id, data)
                await websocket.send_json({"type": "custom_response"})

        handler = CustomHandler()
        factory.register_handler("custom", handler)

        message = {"type": "custom", "data": {"test": "data"}}

        await factory.handle_message(mock_websocket, "test_player", message)

        assert handler.called
        assert handler.called_with == (mock_websocket, "test_player", {"test": "data"})
        mock_websocket.send_json.assert_called_with({"type": "custom_response"})

    def test_handler_overwrite(self, factory):
        """Test that registering a handler overwrites existing ones."""

        class CustomHandler(MessageHandler):
            async def handle(self, websocket, player_id, data):
                pass

        original_handler = factory.get_handler("command")
        custom_handler = CustomHandler()

        factory.register_handler("command", custom_handler)

        assert factory.get_handler("command") == custom_handler
        assert factory.get_handler("command") != original_handler
