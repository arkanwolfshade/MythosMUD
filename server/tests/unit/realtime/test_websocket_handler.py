"""
Tests for WebSocket handler functionality.

This module tests the WebSocket message handling, connection management,
and error handling for the MythosMUD real-time communication system.
As noted in the restricted archives, these tests ensure the stability
of our forbidden knowledge transmission protocols.
"""

import json
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import WebSocket, WebSocketDisconnect

from server.error_types import ErrorType
from server.realtime.websocket_handler import (
    broadcast_room_update,
    get_help_content,
    handle_chat_message,
    handle_game_command,
    handle_websocket_connection,
    handle_websocket_message,
    process_websocket_command,
    send_system_message,
)


class TestWebSocketConnection:
    """Test WebSocket connection handling."""

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock(spec=WebSocket)
        websocket.send_json = AsyncMock()
        websocket.receive_text = AsyncMock()
        return websocket

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock connection manager."""
        mock_cm = MagicMock()
        mock_cm.connect_websocket = AsyncMock(return_value=True)
        mock_cm.disconnect_websocket = AsyncMock()
        mock_cm._get_player = Mock()
        mock_cm.mark_player_seen = Mock()
        mock_cm.persistence = Mock()
        mock_cm.get_room_occupants = Mock(return_value=[])
        mock_cm.broadcast_to_room = AsyncMock()
        mock_cm.broadcast_global = AsyncMock()
        mock_cm.subscribe_to_room = AsyncMock()
        mock_cm.unsubscribe_from_room = AsyncMock()
        mock_cm.message_queue = MagicMock()
        return mock_cm

    @pytest.fixture
    def mock_user_manager(self):
        """Create a mock user manager."""
        with patch("server.services.user_manager.user_manager") as mock_um:
            mock_um.load_player_mutes = Mock()
            mock_um.cleanup_player_mutes = Mock()
            yield mock_um

    @pytest.mark.asyncio
    async def test_handle_websocket_connection_success(
        self, mock_websocket, mock_connection_manager, mock_user_manager
    ):
        """Test successful WebSocket connection handling."""
        # Setup
        player_id = "test_player_123"
        session_id = "session_456"

        # Mock app state to indicate no shutdown pending
        mock_app = Mock()
        mock_app.state.server_shutdown_pending = False
        mock_websocket.app = mock_app

        # Mock player and room data
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_player.level = 1
        mock_player.current_room_id = "room_1"
        mock_player.get_stats = Mock(return_value={"health": 100, "sanity": 80})

        mock_room = Mock()
        mock_room.id = "room_1"
        mock_room.name = "Test Room"
        mock_room.description = "A test room"
        mock_room.exits = {"north": "room_2"}
        mock_room.has_player = Mock(return_value=False)
        mock_room.player_entered = Mock()
        mock_room.get_players = Mock(return_value=[])
        mock_room.to_dict = Mock(return_value={"id": "room_1", "name": "Test Room"})

        mock_connection_manager._get_player.return_value = mock_player
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Mock the message loop to exit after first iteration
        mock_websocket.receive_text.side_effect = [json.dumps({"type": "ping", "data": {}}), WebSocketDisconnect()]

        # Execute
        await handle_websocket_connection(
            mock_websocket,
            player_id,
            session_id,
            connection_manager=mock_connection_manager,
        )

        # Verify
        mock_connection_manager.connect_websocket.assert_called_once_with(
            mock_websocket, player_id, session_id, token=None
        )
        mock_user_manager.load_player_mutes.assert_called_once_with(player_id)
        mock_websocket.send_json.assert_called()
        mock_connection_manager.disconnect_websocket.assert_called_once_with(player_id)
        mock_user_manager.cleanup_player_mutes.assert_called_once_with(player_id)

    @pytest.mark.asyncio
    async def test_handle_websocket_connection_connection_failure(self, mock_websocket, mock_connection_manager):
        """Test WebSocket connection handling when connection fails."""
        # Setup
        player_id = "test_player_123"

        # Mock app state to indicate no shutdown pending
        mock_app = Mock()
        mock_app.state.server_shutdown_pending = False
        mock_websocket.app = mock_app

        mock_connection_manager.connect_websocket.return_value = False

        # Execute
        await handle_websocket_connection(
            mock_websocket,
            player_id,
            connection_manager=mock_connection_manager,
        )

        # Verify
        mock_connection_manager.connect_websocket.assert_called_once_with(mock_websocket, player_id, None, token=None)
        mock_websocket.send_json.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_websocket_connection_json_decode_error(
        self, mock_websocket, mock_connection_manager, mock_user_manager
    ):
        """Test WebSocket connection handling with JSON decode error."""
        # Setup
        player_id = "test_player_123"

        # Mock app state to indicate no shutdown pending
        mock_app = Mock()
        mock_app.state.server_shutdown_pending = False
        mock_websocket.app = mock_app

        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "room_1"
        mock_player.get_stats = Mock(return_value={})

        mock_room = Mock()
        mock_room.id = "room_1"
        mock_room.name = "Test Room"
        mock_room.has_player = Mock(return_value=False)
        mock_room.player_entered = Mock()
        mock_room.get_players = Mock(return_value=[])
        mock_room.to_dict = Mock(return_value={"id": "room_1"})

        mock_connection_manager._get_player.return_value = mock_player
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Mock invalid JSON
        mock_websocket.receive_text.side_effect = ["invalid json", WebSocketDisconnect()]

        # Execute
        await handle_websocket_connection(
            mock_websocket,
            player_id,
            session_id=None,
            connection_manager=mock_connection_manager,
        )

        # Verify error response was sent
        error_calls = [call for call in mock_websocket.send_json.call_args_list if call[0][0].get("type") == "error"]
        assert len(error_calls) > 0
        assert error_calls[0][0][0]["error_type"] == ErrorType.INVALID_FORMAT.value


class TestWebSocketMessageHandling:
    """Test WebSocket message handling."""

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock(spec=WebSocket)
        websocket.send_json = AsyncMock()
        return websocket

    @pytest.mark.asyncio
    async def test_handle_websocket_message_success(self, mock_websocket):
        """Test successful WebSocket message handling."""
        # Setup
        player_id = "test_player_123"
        message = {"type": "command", "data": {"command": "look"}}

        with patch("server.realtime.message_handler_factory.message_handler_factory") as mock_factory:
            mock_factory.handle_message = AsyncMock()

            # Execute
            await handle_websocket_message(mock_websocket, player_id, message)

            # Verify
            mock_factory.handle_message.assert_called_once_with(mock_websocket, player_id, message)

    @pytest.mark.asyncio
    async def test_handle_websocket_message_none_message(self, mock_websocket):
        """Test WebSocket message handling with None message."""
        # Setup
        player_id = "test_player_123"
        message = None

        with patch("server.realtime.message_handler_factory.message_handler_factory") as mock_factory:
            mock_factory.handle_message = AsyncMock(
                side_effect=AttributeError("'NoneType' object has no attribute 'get'")
            )

            # Execute
            await handle_websocket_message(mock_websocket, player_id, message)

            # Verify error response was sent
            mock_websocket.send_json.assert_called_once()
            call_args = mock_websocket.send_json.call_args[0][0]
            assert call_args["type"] == "error"
            assert call_args["error_type"] == ErrorType.MESSAGE_PROCESSING_ERROR.value

    @pytest.mark.asyncio
    async def test_handle_websocket_message_exception(self, mock_websocket):
        """Test WebSocket message handling with exception."""
        # Setup
        player_id = "test_player_123"
        message = {"type": "command", "data": {"command": "look"}}

        with patch("server.realtime.message_handler_factory.message_handler_factory") as mock_factory:
            mock_factory.handle_message = AsyncMock(side_effect=Exception("Test error"))

            # Execute
            await handle_websocket_message(mock_websocket, player_id, message)

            # Verify error response was sent
            mock_websocket.send_json.assert_called_once()
            call_args = mock_websocket.send_json.call_args[0][0]
            assert call_args["type"] == "error"
            assert call_args["error_type"] == ErrorType.MESSAGE_PROCESSING_ERROR.value
            assert "Test error" in call_args["message"]


class TestGameCommandHandling:
    """Test game command handling."""

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock(spec=WebSocket)
        websocket.send_json = AsyncMock()
        return websocket

    @pytest.fixture(autouse=True)
    def configure_app_container(self):
        """Ensure the FastAPI app has a mock container with a connection manager."""
        from server.main import app as fastapi_app

        original_container = getattr(fastapi_app.state, "container", None)
        mock_container = MagicMock()
        mock_container.connection_manager = MagicMock()
        fastapi_app.state.container = mock_container
        try:
            yield mock_container.connection_manager
        finally:
            fastapi_app.state.container = original_container

    @pytest.mark.asyncio
    async def test_handle_game_command_success(self, mock_websocket):
        """Test successful game command handling."""
        # Setup
        player_id = "test_player_123"
        command = "look"
        args = []

        with patch("server.realtime.websocket_handler.process_websocket_command") as mock_process:
            mock_process.return_value = {"result": "You see a test room."}

            # Execute
            await handle_game_command(mock_websocket, player_id, command, args)

            # Verify
            # connection_manager is resolved from app.state.container.connection_manager
            from server.main import app

            expected_connection_manager = app.state.container.connection_manager
            mock_process.assert_called_once_with("look", [], player_id, connection_manager=expected_connection_manager)
            mock_websocket.send_json.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_game_command_empty_command(self, mock_websocket):
        """Test game command handling with empty command."""
        # Setup
        player_id = "test_player_123"
        command = ""
        args = None

        # Execute
        await handle_game_command(mock_websocket, player_id, command, args)

        # Verify error response was sent
        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["type"] == "error"
        assert call_args["error_type"] == ErrorType.INVALID_COMMAND.value

    @pytest.mark.asyncio
    async def test_handle_game_command_exception(self, mock_websocket):
        """Test game command handling with exception."""
        # Setup
        player_id = "test_player_123"
        command = "look"
        args = []

        with patch("server.realtime.websocket_handler.process_websocket_command") as mock_process:
            mock_process.side_effect = Exception("Test error")

            # Execute
            await handle_game_command(mock_websocket, player_id, command, args)

            # Verify error response was sent
            mock_websocket.send_json.assert_called_once()
            call_args = mock_websocket.send_json.call_args[0][0]
            assert call_args["type"] == "error"
            assert call_args["error_type"] == ErrorType.MESSAGE_PROCESSING_ERROR.value


class TestWebSocketCommandProcessing:
    """Test WebSocket command processing."""

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock connection manager and attach it to the FastAPI app state."""
        from server.main import app as fastapi_app

        original_container = getattr(fastapi_app.state, "container", None)
        mock_container = MagicMock()
        mock_cm = MagicMock()
        mock_cm._get_player = Mock()
        mock_cm.persistence = Mock()
        mock_cm.app = Mock()
        mock_container.connection_manager = mock_cm
        fastapi_app.state.container = mock_container

        try:
            yield mock_cm
        finally:
            fastapi_app.state.container = original_container

    @pytest.mark.asyncio
    async def test_process_websocket_command_look_success(self, mock_connection_manager):
        """Test successful look command processing."""
        # Setup
        player_id = "test_player_123"
        cmd = "look"
        args = []

        mock_player = Mock()
        mock_player.current_room_id = "room_1"
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player

        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.description = "A test room"
        mock_room.exits = {"north": "room_2"}
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Mock app state for the unified command handler
        mock_app = Mock()
        mock_app.state.persistence = mock_connection_manager.persistence
        mock_app.state.player_service = Mock()
        mock_app.state.user_manager = Mock()
        mock_connection_manager.app = mock_app

        # Execute
        result = await process_websocket_command(cmd, args, player_id)

        # Verify
        assert "result" in result
        assert "Test Room" in result["result"]
        assert "A test room" in result["result"]
        assert "Exits: north" in result["result"]

    @pytest.mark.asyncio
    async def test_process_websocket_command_look_direction(self, mock_connection_manager):
        """Test look command with direction."""
        # Setup
        player_id = "test_player_123"
        cmd = "look"
        args = ["north"]

        mock_player = Mock()
        mock_player.current_room_id = "room_1"
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player

        mock_room = Mock()
        mock_room.exits = {"north": "room_2"}
        mock_connection_manager.persistence.get_room.return_value = mock_room

        mock_target_room = Mock()
        mock_target_room.name = "North Room"
        mock_target_room.description = "A room to the north"
        mock_connection_manager.persistence.get_room.side_effect = [mock_room, mock_target_room]

        # Mock app state for the unified command handler
        mock_app = Mock()
        mock_app.state.persistence = mock_connection_manager.persistence
        mock_app.state.player_service = Mock()
        mock_app.state.user_manager = Mock()
        mock_connection_manager.app = mock_app

        # Execute
        result = await process_websocket_command(cmd, args, player_id)

        # Verify
        assert "result" in result
        assert "North Room" in result["result"]
        assert "A room to the north" in result["result"]

    @pytest.mark.asyncio
    async def test_process_websocket_command_go_success(self, mock_connection_manager):
        """Test successful go command processing."""
        # Setup
        player_id = "test_player_123"
        cmd = "go"
        args = ["north"]

        mock_player = Mock()
        mock_player.current_room_id = "room_1"
        mock_player.name = "test_player"  # Required for get_username_from_user
        # Mock get_stats to return standing position (required for movement)
        mock_player.get_stats = Mock(return_value={"position": "standing"})
        mock_connection_manager._get_player.return_value = mock_player
        # Mock persistence.get_player_by_name to return the same player (used by handle_go_command)
        mock_connection_manager.persistence.get_player_by_name.return_value = mock_player

        mock_room = Mock()
        mock_room.exits = {"north": "room_2"}
        mock_room.get_players = Mock(return_value=[player_id])

        mock_target_room = Mock()
        mock_target_room.name = "North Room"
        mock_target_room.description = "A room to the north"
        mock_target_room.exits = {"south": "room_1"}
        mock_target_room.get_players = Mock(return_value=[])

        # Mock get_room to return different rooms based on room_id
        def mock_get_room(room_id):
            if room_id == "room_1":
                return mock_room
            elif room_id == "room_2":
                return mock_target_room
            return None

        mock_connection_manager.persistence.get_room.side_effect = mock_get_room

        # Mock app state for the unified command handler
        mock_app = Mock()
        mock_app.state.persistence = mock_connection_manager.persistence
        mock_app.state.player_service = Mock()
        mock_app.state.user_manager = Mock()
        mock_connection_manager.app = mock_app

        with patch("server.game.movement_service.MovementService") as mock_movement_service:
            mock_service_instance = Mock()
            mock_service_instance.move_player = Mock(return_value=True)
            mock_movement_service.return_value = mock_service_instance

            # Mock event bus
            mock_connection_manager._event_bus = Mock()

            # Execute
            result = await process_websocket_command(cmd, args, player_id)

            # Verify
            assert "result" in result
            # The response may be "You move to the new location." without room description
            # Check that movement was successful
            assert "move" in result["result"].lower() or "location" in result["result"].lower()
            assert result["room_changed"] is True
            assert result["room_id"] == "room_2"

    @pytest.mark.asyncio
    async def test_process_websocket_command_player_not_found(self, mock_connection_manager):
        """Test command processing when player is not found."""
        # Setup
        player_id = "test_player_123"
        cmd = "look"
        args = []

        mock_connection_manager._get_player.return_value = None

        # Execute
        result = await process_websocket_command(cmd, args, player_id)

        # Verify
        assert result["result"] == "Player not found"

    @pytest.mark.asyncio
    async def test_process_websocket_command_no_persistence(self, mock_connection_manager):
        """Test command processing when persistence is not available."""
        # Setup
        player_id = "test_player_123"
        cmd = "look"
        args = []

        mock_player = Mock()
        mock_connection_manager._get_player.return_value = mock_player
        mock_connection_manager.persistence = None

        # Execute
        result = await process_websocket_command(cmd, args, player_id)

        # Verify
        assert result["result"] == "Game system unavailable"


class TestChatMessageHandling:
    """Test chat message handling."""

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock(spec=WebSocket)
        websocket.send_json = AsyncMock()
        return websocket

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock connection manager."""
        from server.main import app as fastapi_app

        original_container = getattr(fastapi_app.state, "container", None)
        mock_container = MagicMock()
        mock_cm = MagicMock()
        mock_cm._get_player = Mock()
        mock_cm.broadcast_to_room = AsyncMock()
        mock_container.connection_manager = mock_cm
        fastapi_app.state.container = mock_container

        try:
            yield mock_cm
        finally:
            fastapi_app.state.container = original_container

    @pytest.mark.asyncio
    async def test_handle_chat_message_success(self, mock_websocket, mock_connection_manager):
        """Test successful chat message handling."""
        # Setup
        player_id = "test_player_123"
        message = "Hello, world!"

        mock_player = Mock()
        mock_player.current_room_id = "room_1"
        mock_connection_manager._get_player.return_value = mock_player

        # Execute
        await handle_chat_message(mock_websocket, player_id, message)

        # Verify
        mock_connection_manager.broadcast_to_room.assert_called_once()
        mock_websocket.send_json.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_chat_message_exception(self, mock_websocket, mock_connection_manager):
        """Test chat message handling with exception."""
        # Setup
        player_id = "test_player_123"
        message = "Hello, world!"

        mock_connection_manager._get_player.side_effect = Exception("Test error")

        # Execute
        await handle_chat_message(mock_websocket, player_id, message)

        # Verify error response was sent
        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["type"] == "error"
        assert call_args["error_type"] == ErrorType.MESSAGE_PROCESSING_ERROR.value


class TestRoomUpdateBroadcasting:
    """Test room update broadcasting."""

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock connection manager."""
        from server.main import app as fastapi_app

        original_container = getattr(fastapi_app.state, "container", None)
        mock_container = MagicMock()
        mock_cm = MagicMock()
        mock_cm._get_player = Mock()
        mock_cm.persistence = Mock()
        mock_cm.get_room_occupants = Mock(return_value=[])
        mock_cm.broadcast_to_room = AsyncMock()
        mock_cm.subscribe_to_room = AsyncMock()
        mock_cm.unsubscribe_from_room = AsyncMock()
        mock_cm.room_manager = MagicMock()
        mock_container.connection_manager = mock_cm
        fastapi_app.state.container = mock_container

        try:
            yield mock_cm
        finally:
            fastapi_app.state.container = original_container

    @pytest.mark.asyncio
    async def test_broadcast_room_update_success(self, mock_connection_manager):
        """Test successful room update broadcasting."""
        # Setup
        player_id = "test_player_123"
        room_id = "room_1"

        mock_player = Mock()
        mock_player.current_room_id = "room_1"
        mock_connection_manager._get_player.return_value = mock_player

        mock_room = Mock()
        mock_room.get_players = Mock(return_value=[])
        mock_room.get_objects = Mock(return_value=[])
        mock_room.get_npcs = Mock(return_value=[])
        mock_room.get_occupant_count = Mock(return_value=0)
        mock_room.to_dict = Mock(return_value={"id": "room_1", "name": "Test Room"})
        mock_connection_manager.persistence.get_room.return_value = mock_room
        drop_payload = [
            {
                "item_instance_id": "instance-obsidian_amulet",
                "prototype_id": "obsidian_amulet",
                "item_id": "obsidian_amulet",
                "item_name": "Obsidian Amulet",
                "slot_type": "neck",
                "quantity": 1,
            }
        ]
        mock_connection_manager.room_manager.list_room_drops.return_value = drop_payload

        # Execute
        await broadcast_room_update(player_id, room_id)

        # Verify
        mock_connection_manager.broadcast_to_room.assert_called_once()
        _, sent_event = mock_connection_manager.broadcast_to_room.call_args[0]
        assert sent_event["data"]["room_drops"] == drop_payload
        assert "Scattered upon the floor" in sent_event["data"]["drop_summary"]

    @pytest.mark.asyncio
    async def test_broadcast_room_update_no_persistence(self, mock_connection_manager):
        """Test room update broadcasting when persistence is not available."""
        # Setup
        player_id = "test_player_123"
        room_id = "room_1"

        mock_connection_manager.persistence = None

        # Execute
        await broadcast_room_update(player_id, room_id)

        # Verify
        mock_connection_manager.broadcast_to_room.assert_not_called()

    @pytest.mark.asyncio
    async def test_broadcast_room_update_room_not_found(self, mock_connection_manager):
        """Test room update broadcasting when room is not found."""
        # Setup
        player_id = "test_player_123"
        room_id = "room_1"

        mock_connection_manager.persistence.get_room.return_value = None

        # Execute
        await broadcast_room_update(player_id, room_id)

        # Verify
        mock_connection_manager.broadcast_to_room.assert_not_called()


class TestSystemMessageHandling:
    """Test system message handling."""

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock(spec=WebSocket)
        websocket.send_json = AsyncMock()
        return websocket

    @pytest.mark.asyncio
    async def test_send_system_message_success(self, mock_websocket):
        """Test successful system message sending."""
        # Setup
        message = "System message"
        message_type = "info"

        # Execute
        await send_system_message(mock_websocket, message, message_type)

        # Verify
        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["event_type"] == "system"
        assert call_args["data"]["message"] == message
        assert call_args["data"]["message_type"] == message_type

    @pytest.mark.asyncio
    async def test_send_system_message_exception(self, mock_websocket):
        """Test system message sending with exception."""
        # Setup
        message = "System message"
        message_type = "info"
        mock_websocket.send_json.side_effect = Exception("Test error")

        # Execute
        await send_system_message(mock_websocket, message, message_type)

        # Verify - should not raise exception


class TestHelpContent:
    """Test help content functionality."""

    def test_get_help_content_specific_command(self):
        """Test getting help for a specific command."""
        # Execute
        result = get_help_content("look")

        # Verify
        assert "Help for 'look'" in result

    def test_get_help_content_general(self):
        """Test getting general help content."""
        # Execute
        result = get_help_content()

        # Verify
        assert "Available Commands" in result
        assert "look" in result
        assert "go" in result
        assert "say" in result
        assert "help" in result
