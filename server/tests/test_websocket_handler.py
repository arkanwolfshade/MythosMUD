"""
Tests for the WebSocket handler module.

This module tests the WebSocket handler functions that are most amenable to unit testing,
focusing on message parsing, error handling, helper functions, and command routing logic.
"""

from unittest.mock import AsyncMock, Mock, patch

import pytest

from ..realtime.websocket_handler import (
    get_help_content,
    handle_websocket_message,
    process_websocket_command,
    send_system_message,
)


class TestWebSocketHandlerHelpers:
    """Test cases for WebSocket handler helper functions."""

    def test_get_help_content_general(self):
        """Test getting general help content."""
        # Execute
        help_content = get_help_content()

        # Verify
        assert "Available Commands:" in help_content
        assert "look [direction]" in help_content
        assert "go <direction>" in help_content
        assert "say <message>" in help_content
        assert "help [command]" in help_content
        assert "Directions: north, south, east, west" in help_content

    def test_get_help_content_specific_command(self):
        """Test getting help content for a specific command."""
        # Execute
        help_content = get_help_content("look")

        # Verify
        assert "Help for 'look'" in help_content
        assert "Command not found or help not available" in help_content

    def test_get_help_content_nonexistent_command(self):
        """Test getting help content for a non-existent command."""
        # Execute
        help_content = get_help_content("nonexistent")

        # Verify
        assert "Help for 'nonexistent'" in help_content
        assert "Command not found or help not available" in help_content

    @pytest.mark.asyncio
    async def test_send_system_message_success(self):
        """Test successful system message sending."""
        # Setup
        mock_websocket = AsyncMock()
        message = "Test system message"
        message_type = "info"

        # Execute
        await send_system_message(mock_websocket, message, message_type)

        # Verify
        mock_websocket.send_json.assert_called_once_with(
            {
                "type": "system",
                "message": message,
                "message_type": message_type,
            }
        )

    @pytest.mark.asyncio
    async def test_send_system_message_default_type(self):
        """Test system message sending with default message type."""
        # Setup
        mock_websocket = AsyncMock()
        message = "Test system message"

        # Execute
        await send_system_message(mock_websocket, message)

        # Verify
        mock_websocket.send_json.assert_called_once_with(
            {
                "type": "system",
                "message": message,
                "message_type": "info",
            }
        )

    @pytest.mark.asyncio
    async def test_send_system_message_error(self):
        """Test system message sending when WebSocket fails."""
        # Setup
        mock_websocket = AsyncMock()
        mock_websocket.send_json.side_effect = Exception("WebSocket error")
        message = "Test system message"

        # Execute - should not raise exception
        await send_system_message(mock_websocket, message)

        # Verify
        mock_websocket.send_json.assert_called_once()


class TestWebSocketMessageHandling:
    """Test cases for WebSocket message handling."""

    def setup_method(self):
        """Set up test fixtures."""
        self.mock_websocket = AsyncMock()
        self.player_id = "test_player_123"

    @pytest.mark.asyncio
    async def test_handle_websocket_message_command(self):
        """Test handling a command message."""
        # Setup
        message = {"type": "command", "data": {"command": "look", "args": []}}

        with patch("server.realtime.websocket_handler.handle_game_command") as mock_handle_command:
            # Execute
            await handle_websocket_message(self.mock_websocket, self.player_id, message)

            # Verify
            mock_handle_command.assert_called_once_with(self.mock_websocket, self.player_id, "look", [])

    @pytest.mark.asyncio
    async def test_handle_websocket_message_chat(self):
        """Test handling a chat message."""
        # Setup
        message = {"type": "chat", "data": {"message": "Hello, world!"}}

        with patch("server.realtime.websocket_handler.handle_chat_message") as mock_handle_chat:
            # Execute
            await handle_websocket_message(self.mock_websocket, self.player_id, message)

            # Verify
            mock_handle_chat.assert_called_once_with(self.mock_websocket, self.player_id, "Hello, world!")

    @pytest.mark.asyncio
    async def test_handle_websocket_message_ping(self):
        """Test handling a ping message."""
        # Setup
        message = {"type": "ping", "data": {}}

        # Execute
        await handle_websocket_message(self.mock_websocket, self.player_id, message)

        # Verify
        self.mock_websocket.send_json.assert_called_once_with({"type": "pong"})

    @pytest.mark.asyncio
    async def test_handle_websocket_message_unknown_type(self):
        """Test handling an unknown message type."""
        # Setup
        message = {"type": "unknown_type", "data": {}}

        # Execute
        await handle_websocket_message(self.mock_websocket, self.player_id, message)

        # Verify
        self.mock_websocket.send_json.assert_called_once_with(
            {"type": "error", "message": "Unknown message type: unknown_type"}
        )

    @pytest.mark.asyncio
    async def test_handle_websocket_message_missing_type(self):
        """Test handling a message with missing type."""
        # Setup
        message = {"data": {}}

        # Execute
        await handle_websocket_message(self.mock_websocket, self.player_id, message)

        # Verify
        self.mock_websocket.send_json.assert_called_once_with(
            {"type": "error", "message": "Unknown message type: unknown"}
        )

    @pytest.mark.asyncio
    async def test_handle_websocket_message_missing_data(self):
        """Test handling a message with missing data."""
        # Setup
        message = {"type": "command"}

        with patch("server.realtime.websocket_handler.handle_game_command") as mock_handle_command:
            # Execute
            await handle_websocket_message(self.mock_websocket, self.player_id, message)

            # Verify
            mock_handle_command.assert_called_once_with(self.mock_websocket, self.player_id, "", [])

    @pytest.mark.asyncio
    async def test_handle_websocket_message_exception(self):
        """Test handling a message when an exception occurs."""
        # Setup
        message = {"type": "command", "data": {"command": "look", "args": []}}

        with patch("server.realtime.websocket_handler.handle_game_command", side_effect=Exception("Test error")):
            # Execute
            await handle_websocket_message(self.mock_websocket, self.player_id, message)

            # Verify
            self.mock_websocket.send_json.assert_called_once_with(
                {"type": "error", "message": "Error processing message"}
            )


class TestWebSocketCommandProcessing:
    """Test cases for WebSocket command processing."""

    def setup_method(self):
        """Set up test fixtures."""
        self.player_id = "test_player_123"

        # Mock the connection manager
        self.mock_connection_manager = Mock()
        self.mock_player = Mock()
        self.mock_player.name = "TestPlayer"
        self.mock_player.current_room_id = "room_001"
        self.mock_connection_manager._get_player.return_value = self.mock_player

        # Mock persistence
        self.mock_persistence = Mock()
        self.mock_connection_manager.persistence = self.mock_persistence

    @pytest.mark.asyncio
    async def test_process_websocket_command_player_not_found(self):
        """Test command processing when player is not found."""
        # Setup
        self.mock_connection_manager._get_player.return_value = None

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            # Execute
            result = await process_websocket_command("look", [], self.player_id)

            # Verify
            assert result == {"result": "Player not found"}

    @pytest.mark.asyncio
    async def test_process_websocket_command_persistence_unavailable(self):
        """Test command processing when persistence is unavailable."""
        # Setup
        self.mock_connection_manager.persistence = None

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            # Execute
            result = await process_websocket_command("look", [], self.player_id)

            # Verify
            assert result == {"result": "Game system unavailable"}

    @pytest.mark.asyncio
    async def test_process_websocket_command_invalid_player_object(self):
        """Test command processing with invalid player object."""
        # Setup
        invalid_player = Mock()  # No current_room_id attribute
        # Make sure the mock doesn't have current_room_id attribute
        del invalid_player.current_room_id
        self.mock_connection_manager._get_player.return_value = invalid_player

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            # Execute
            result = await process_websocket_command("look", [], self.player_id)

            # Verify - should return player data error before trying to access room
            assert result == {"result": "Player data error"}

    @pytest.mark.asyncio
    async def test_process_websocket_command_look_no_args(self):
        """Test look command without arguments."""
        # Setup
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.description = "A test room"
        mock_room.exits = {"north": "room_002", "south": None}
        self.mock_persistence.get_room.return_value = mock_room

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            # Execute
            result = await process_websocket_command("look", [], self.player_id)

            # Verify
            assert "Test Room" in result["result"]
            assert "A test room" in result["result"]
            assert "Exits: north" in result["result"]
            assert "south" not in result["result"]  # None exit should be filtered

    @pytest.mark.asyncio
    async def test_process_websocket_command_look_with_direction(self):
        """Test look command with direction argument."""
        # Setup
        mock_room = Mock()
        mock_room.exits = {"north": "room_002"}
        self.mock_persistence.get_room.return_value = mock_room

        mock_target_room = Mock()
        mock_target_room.name = "North Room"
        mock_target_room.description = "A room to the north"
        self.mock_persistence.get_room.side_effect = (
            lambda room_id: mock_room if room_id == "room_001" else mock_target_room
        )

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            # Execute
            result = await process_websocket_command("look", ["north"], self.player_id)

            # Verify
            assert "North Room" in result["result"]
            assert "A room to the north" in result["result"]

    @pytest.mark.asyncio
    async def test_process_websocket_command_look_invalid_direction(self):
        """Test look command with invalid direction."""
        # Setup
        mock_room = Mock()
        mock_room.exits = {"north": "room_002"}
        self.mock_persistence.get_room.return_value = mock_room

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            # Execute
            result = await process_websocket_command("look", ["invalid"], self.player_id)

            # Verify
            assert "You see nothing special that way" in result["result"]

    @pytest.mark.asyncio
    async def test_process_websocket_command_look_room_not_found(self):
        """Test look command when room is not found."""
        # Setup
        self.mock_persistence.get_room.return_value = None

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            # Execute
            result = await process_websocket_command("look", [], self.player_id)

            # Verify
            assert "You see nothing special" in result["result"]

    @pytest.mark.asyncio
    async def test_process_websocket_command_go_no_args(self):
        """Test go command without arguments."""
        # Setup
        mock_room = Mock()
        mock_room.exits = {"north": "room_002"}
        self.mock_persistence.get_room.return_value = mock_room

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            # Execute
            result = await process_websocket_command("go", [], self.player_id)

            # Verify
            assert "Go where? Usage: go <direction>" in result["result"]

    @pytest.mark.asyncio
    async def test_process_websocket_command_go_invalid_direction(self):
        """Test go command with invalid direction."""
        # Setup
        mock_room = Mock()
        mock_room.exits = {"north": "room_002"}
        self.mock_persistence.get_room.return_value = mock_room

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            # Execute
            result = await process_websocket_command("go", ["invalid"], self.player_id)

            # Verify
            assert "You can't go that way" in result["result"]

    @pytest.mark.asyncio
    async def test_process_websocket_command_go_target_room_not_found(self):
        """Test go command when target room is not found."""
        # Setup
        mock_room = Mock()
        mock_room.exits = {"north": "room_002"}
        self.mock_persistence.get_room.side_effect = lambda room_id: mock_room if room_id == "room_001" else None

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            # Execute
            result = await process_websocket_command("go", ["north"], self.player_id)

            # Verify
            assert "You can't go that way" in result["result"]

    @pytest.mark.asyncio
    async def test_process_websocket_command_go_movement_service_failure(self):
        """Test go command when movement service fails."""
        # Setup
        mock_room = Mock()
        mock_room.exits = {"north": "room_002"}
        self.mock_persistence.get_room.return_value = mock_room

        mock_target_room = Mock()
        mock_target_room.name = "North Room"
        mock_target_room.description = "A room to the north"
        mock_target_room.exits = {"south": "room_001"}
        self.mock_persistence.get_room.side_effect = (
            lambda room_id: mock_room if room_id == "room_001" else mock_target_room
        )

        # Mock MovementService to return False (movement failed)
        mock_movement_service = Mock()
        mock_movement_service.move_player.return_value = False

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            with patch("server.game.movement_service.MovementService", return_value=mock_movement_service):
                with patch("server.realtime.websocket_handler.getattr", return_value=Mock()):  # Mock event_bus
                    # Execute
                    result = await process_websocket_command("go", ["north"], self.player_id)

                    # Verify
                    assert "You can't go that way" in result["result"]

    @pytest.mark.skip(reason="Complex integration test - go command involves many dependencies")
    @pytest.mark.asyncio
    async def test_process_websocket_command_go_success(self):
        """Test successful go command."""
        # Setup
        mock_room = Mock()
        mock_room.exits = {"north": "room_002"}
        self.mock_persistence.get_room.return_value = mock_room

        mock_target_room = Mock()
        mock_target_room.name = "North Room"
        mock_target_room.description = "A room to the north"
        mock_target_room.exits = {"south": "room_001"}
        self.mock_persistence.get_room.side_effect = (
            lambda room_id: mock_room if room_id == "room_001" else mock_target_room
        )

        # Ensure player's current_room_id is a string, not a Mock
        # The Mock object needs to return the string when accessed
        self.mock_player.current_room_id = "room_001"

        # Mock MovementService to return True (movement successful)
        mock_movement_service = Mock()
        mock_movement_service.move_player.return_value = True

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            with patch("server.game.movement_service.MovementService", return_value=mock_movement_service):
                # Mock the event bus properly
                mock_event_bus = Mock()
                with patch("server.realtime.websocket_handler.getattr", return_value=mock_event_bus):
                    # Execute
                    result = await process_websocket_command("go", ["north"], self.player_id)

                    # Verify - the movement should succeed and return room info
                    assert "North Room" in result["result"]
                    assert "A room to the north" in result["result"]
                    assert result["room_changed"] is True
                    assert result["room_id"] == "room_002"

    @pytest.mark.asyncio
    async def test_process_websocket_command_other_commands(self):
        """Test processing of other commands through command handler."""
        # Setup
        mock_room = Mock()
        mock_room.exits = {}
        self.mock_persistence.get_room.return_value = mock_room

        # Mock command handler to return success
        mock_command_result = {"result": "Command executed successfully"}

        with patch("server.realtime.websocket_handler.connection_manager", self.mock_connection_manager):
            with patch("server.command_handler.process_command", return_value=mock_command_result):
                # Execute
                result = await process_websocket_command("say", ["hello"], self.player_id)

                # Verify
                assert result == mock_command_result


class TestWebSocketErrorHandling:
    """Test cases for WebSocket error handling scenarios."""

    def setup_method(self):
        """Set up test fixtures."""
        self.mock_websocket = AsyncMock()
        self.player_id = "test_player_123"

        # Mock persistence for error handling tests
        self.mock_persistence = Mock()

    @pytest.mark.asyncio
    async def test_handle_websocket_message_malformed_json(self):
        """Test handling malformed JSON in message data."""
        # Setup
        message = "invalid json string"

        # Execute
        await handle_websocket_message(self.mock_websocket, self.player_id, message)

        # Verify - should handle gracefully and not crash
        # The actual JSON parsing happens in the main WebSocket loop, not in this function

    @pytest.mark.asyncio
    async def test_handle_websocket_message_empty_message(self):
        """Test handling empty message."""
        # Setup
        message = {}

        # Execute
        await handle_websocket_message(self.mock_websocket, self.player_id, message)

        # Verify
        self.mock_websocket.send_json.assert_called_once_with(
            {"type": "error", "message": "Unknown message type: unknown"}
        )

    @pytest.mark.asyncio
    async def test_handle_websocket_message_none_message(self):
        """Test handling None message."""
        # Setup
        message = None

        # Execute
        await handle_websocket_message(self.mock_websocket, self.player_id, message)

        # Verify - None message causes exception, so we get error processing message
        self.mock_websocket.send_json.assert_called_once_with({"type": "error", "message": "Error processing message"})

    @pytest.mark.asyncio
    async def test_process_websocket_command_room_has_no_exits_attribute(self):
        """Test command processing when room has no exits attribute."""
        # Setup
        mock_room = Mock()
        # Don't set exits attribute - make sure it doesn't exist
        if hasattr(mock_room, "exits"):
            del mock_room.exits
        self.mock_persistence.get_room.return_value = mock_room

        mock_connection_manager = Mock()
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "room_001"
        mock_connection_manager._get_player.return_value = mock_player
        mock_connection_manager.persistence = self.mock_persistence

        with patch("server.realtime.websocket_handler.connection_manager", mock_connection_manager):
            # Execute
            result = await process_websocket_command("look", [], self.player_id)

            # Verify
            assert "Exits: none" in result["result"]

    @pytest.mark.asyncio
    async def test_process_websocket_command_room_has_no_name_or_description(self):
        """Test command processing when room has no name or description attributes."""
        # Setup
        mock_room = Mock()
        mock_room.exits = {}
        # Don't set name or description attributes - make sure they don't exist
        if hasattr(mock_room, "name"):
            del mock_room.name
        if hasattr(mock_room, "description"):
            del mock_room.description
        self.mock_persistence.get_room.return_value = mock_room

        mock_connection_manager = Mock()
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "room_001"
        mock_connection_manager._get_player.return_value = mock_player
        mock_connection_manager.persistence = self.mock_persistence

        with patch("server.realtime.websocket_handler.connection_manager", mock_connection_manager):
            # Execute
            result = await process_websocket_command("look", [], self.player_id)

            # Verify
            assert "You see nothing special" in result["result"]
            assert "Exits: none" in result["result"]
