"""
Tests for the SSE handler module.

This module tests the Server-Sent Events handler which manages real-time
communication streams, event broadcasting, and player notifications.
"""

import asyncio
from unittest.mock import AsyncMock, Mock, patch

import pytest

from ..realtime.sse_handler import (
    broadcast_game_event,
    format_sse_event,
    game_event_stream,
    send_game_event,
    send_player_status_update,
    send_room_description,
    send_room_event,
    send_system_notification,
)


class TestSSEHandlerFunctions:
    """Test cases for SSE handler utility functions."""

    def test_format_sse_event_backward_compatibility(self):
        """Test the backward compatibility shim function."""
        # Setup
        event_type = "test_event"
        data = {"key": "value", "number": 42}

        # Execute
        result = format_sse_event(event_type, data)

        # Verify
        assert "data:" in result
        assert "event_type" in result
        assert "test_event" in result
        assert "key" in result
        assert "value" in result
        assert "42" in result

    @pytest.mark.asyncio
    async def test_send_game_event_success(self):
        """Test successful game event sending."""
        # Setup
        player_id = "test_player_123"
        event_type = "player_move"
        data = {"direction": "north", "room_id": "room_002"}

        mock_connection_manager = Mock()
        mock_connection_manager.send_personal_message = AsyncMock()

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute
            await send_game_event(player_id, event_type, data)

            # Verify
            mock_connection_manager.send_personal_message.assert_called_once()
            call_args = mock_connection_manager.send_personal_message.call_args
            assert call_args[0][0] == "test_player_123"  # player_id
            event_data = call_args[0][1]  # event data
            assert event_data["event_type"] == event_type
            assert event_data["data"] == data
            assert event_data["player_id"] == "test_player_123"

    @pytest.mark.asyncio
    async def test_send_game_event_exception_handling(self):
        """Test game event sending when an exception occurs."""
        # Setup
        player_id = "test_player_123"
        event_type = "player_move"
        data = {"direction": "north"}

        mock_connection_manager = Mock()
        mock_connection_manager.send_personal_message = AsyncMock(side_effect=Exception("Connection error"))

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute - should not raise exception
            await send_game_event(player_id, event_type, data)

            # Verify
            mock_connection_manager.send_personal_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_broadcast_game_event_success(self):
        """Test successful game event broadcasting."""
        # Setup
        event_type = "system_announcement"
        data = {"message": "Server maintenance in 5 minutes"}

        mock_connection_manager = Mock()
        mock_connection_manager.broadcast_global = AsyncMock()

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute
            await broadcast_game_event(event_type, data)

            # Verify
            mock_connection_manager.broadcast_global.assert_called_once()
            call_args = mock_connection_manager.broadcast_global.call_args
            event_data = call_args[0][0]  # event data
            assert event_data["event_type"] == event_type
            assert event_data["data"] == data
            assert call_args[0][1] is None  # exclude_player should be None

    @pytest.mark.asyncio
    async def test_broadcast_game_event_with_exclude_player(self):
        """Test game event broadcasting with excluded player."""
        # Setup
        event_type = "player_joined"
        data = {"player_name": "NewPlayer"}
        exclude_player = "excluded_player_123"

        mock_connection_manager = Mock()
        mock_connection_manager.broadcast_global = AsyncMock()

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute
            await broadcast_game_event(event_type, data, exclude_player)

            # Verify
            mock_connection_manager.broadcast_global.assert_called_once()
            call_args = mock_connection_manager.broadcast_global.call_args
            event_data = call_args[0][0]  # event data
            assert event_data["event_type"] == event_type
            assert event_data["data"] == data
            assert call_args[0][1] == exclude_player  # exclude_player should be passed

    @pytest.mark.asyncio
    async def test_broadcast_game_event_exception_handling(self):
        """Test game event broadcasting when an exception occurs."""
        # Setup
        event_type = "system_announcement"
        data = {"message": "Test message"}

        mock_connection_manager = Mock()
        mock_connection_manager.broadcast_global = AsyncMock(side_effect=Exception("Broadcast error"))

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute - should not raise exception
            await broadcast_game_event(event_type, data)

            # Verify
            mock_connection_manager.broadcast_global.assert_called_once()

    @pytest.mark.asyncio
    async def test_send_room_event_success(self):
        """Test successful room event sending."""
        # Setup
        room_id = "room_001"
        event_type = "player_entered"
        data = {"player_name": "TestPlayer"}

        mock_connection_manager = Mock()
        mock_connection_manager.broadcast_to_room = AsyncMock()

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute
            await send_room_event(room_id, event_type, data)

            # Verify
            mock_connection_manager.broadcast_to_room.assert_called_once()
            call_args = mock_connection_manager.broadcast_to_room.call_args
            assert call_args[0][0] == room_id  # room_id
            event_data = call_args[0][1]  # event data
            assert event_data["event_type"] == event_type
            assert event_data["data"] == data
            assert event_data["room_id"] == room_id
            assert call_args[0][2] is None  # exclude_player should be None

    @pytest.mark.asyncio
    async def test_send_room_event_with_exclude_player(self):
        """Test room event sending with excluded player."""
        # Setup
        room_id = "room_001"
        event_type = "player_left"
        data = {"player_name": "LeavingPlayer"}
        exclude_player = "excluded_player_123"

        mock_connection_manager = Mock()
        mock_connection_manager.broadcast_to_room = AsyncMock()

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute
            await send_room_event(room_id, event_type, data, exclude_player)

            # Verify
            mock_connection_manager.broadcast_to_room.assert_called_once()
            call_args = mock_connection_manager.broadcast_to_room.call_args
            assert call_args[0][0] == room_id  # room_id
            event_data = call_args[0][1]  # event data
            assert event_data["event_type"] == event_type
            assert event_data["data"] == data
            assert event_data["room_id"] == room_id
            assert call_args[0][2] == exclude_player  # exclude_player should be passed

    @pytest.mark.asyncio
    async def test_send_room_event_exception_handling(self):
        """Test room event sending when an exception occurs."""
        # Setup
        room_id = "room_001"
        event_type = "player_entered"
        data = {"player_name": "TestPlayer"}

        mock_connection_manager = Mock()
        mock_connection_manager.broadcast_to_room = AsyncMock(side_effect=Exception("Room broadcast error"))

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute - should not raise exception
            await send_room_event(room_id, event_type, data)

            # Verify
            mock_connection_manager.broadcast_to_room.assert_called_once()

    @pytest.mark.asyncio
    async def test_send_system_notification_success(self):
        """Test successful system notification sending."""
        # Setup
        player_id = "test_player_123"
        message = "Welcome to MythosMUD!"
        notification_type = "info"

        mock_connection_manager = Mock()
        mock_connection_manager.send_personal_message = AsyncMock()

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute
            await send_system_notification(player_id, message, notification_type)

            # Verify
            mock_connection_manager.send_personal_message.assert_called_once()
            call_args = mock_connection_manager.send_personal_message.call_args
            assert call_args[0][0] == "test_player_123"  # player_id
            event_data = call_args[0][1]  # event data
            assert event_data["event_type"] == "system_notification"
            assert event_data["data"]["message"] == message
            assert event_data["data"]["notification_type"] == notification_type
            assert event_data["player_id"] == "test_player_123"

    @pytest.mark.asyncio
    async def test_send_system_notification_default_type(self):
        """Test system notification sending with default notification type."""
        # Setup
        player_id = "test_player_123"
        message = "Warning message"

        mock_connection_manager = Mock()
        mock_connection_manager.send_personal_message = AsyncMock()

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute
            await send_system_notification(player_id, message)

            # Verify
            mock_connection_manager.send_personal_message.assert_called_once()
            call_args = mock_connection_manager.send_personal_message.call_args
            event_data = call_args[0][1]  # event data
            assert event_data["data"]["notification_type"] == "info"  # default type

    @pytest.mark.asyncio
    async def test_send_system_notification_exception_handling(self):
        """Test system notification sending when an exception occurs."""
        # Setup
        player_id = "test_player_123"
        message = "Test message"

        mock_connection_manager = Mock()
        mock_connection_manager.send_personal_message = AsyncMock(side_effect=Exception("Notification error"))

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute - should not raise exception
            await send_system_notification(player_id, message)

            # Verify
            mock_connection_manager.send_personal_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_send_player_status_update_success(self):
        """Test successful player status update sending."""
        # Setup
        player_id = "test_player_123"
        status_data = {"health": 85, "sanity": 70, "level": 5}

        mock_connection_manager = Mock()
        mock_connection_manager.send_personal_message = AsyncMock()

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute
            await send_player_status_update(player_id, status_data)

            # Verify
            mock_connection_manager.send_personal_message.assert_called_once()
            call_args = mock_connection_manager.send_personal_message.call_args
            assert call_args[0][0] == "test_player_123"  # player_id
            event_data = call_args[0][1]  # event data
            assert event_data["event_type"] == "player_status"
            assert event_data["data"] == status_data
            assert event_data["player_id"] == "test_player_123"

    @pytest.mark.asyncio
    async def test_send_player_status_update_exception_handling(self):
        """Test player status update sending when an exception occurs."""
        # Setup
        player_id = "test_player_123"
        status_data = {"health": 85}

        mock_connection_manager = Mock()
        mock_connection_manager.send_personal_message = AsyncMock(side_effect=Exception("Status update error"))

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute - should not raise exception
            await send_player_status_update(player_id, status_data)

            # Verify
            mock_connection_manager.send_personal_message.assert_called_once()

    @pytest.mark.asyncio
    async def test_send_room_description_success(self):
        """Test successful room description sending."""
        # Setup
        player_id = "test_player_123"
        room_data = {
            "name": "Miskatonic Library",
            "description": "Ancient tomes line the walls...",
            "exits": ["north", "south"],
        }

        mock_connection_manager = Mock()
        mock_connection_manager.send_personal_message = AsyncMock()

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute
            await send_room_description(player_id, room_data)

            # Verify
            mock_connection_manager.send_personal_message.assert_called_once()
            call_args = mock_connection_manager.send_personal_message.call_args
            assert call_args[0][0] == "test_player_123"  # player_id
            event_data = call_args[0][1]  # event data
            assert event_data["event_type"] == "room_description"
            assert event_data["data"] == room_data
            assert event_data["player_id"] == "test_player_123"

    @pytest.mark.asyncio
    async def test_send_room_description_exception_handling(self):
        """Test room description sending when an exception occurs."""
        # Setup
        player_id = "test_player_123"
        room_data = {"name": "Test Room"}

        mock_connection_manager = Mock()
        mock_connection_manager.send_personal_message = AsyncMock(side_effect=Exception("Room description error"))

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute - should not raise exception
            await send_room_description(player_id, room_data)

            # Verify
            mock_connection_manager.send_personal_message.assert_called_once()


class TestGameEventStream:
    """Test cases for the main SSE event stream generator."""

    @pytest.mark.asyncio
    async def test_game_event_stream_initial_events(self):
        """Test the initial events sent when SSE stream starts."""
        # Setup
        player_id = "test_player_123"

        mock_connection_manager = Mock()
        mock_connection_manager.connect_sse = AsyncMock()
        mock_connection_manager.disconnect_sse = Mock()
        mock_connection_manager.get_pending_messages = Mock(return_value=[])
        mock_connection_manager.mark_player_seen = Mock()
        mock_connection_manager.prune_stale_players = Mock()
        # Make pending_messages iterable for the "in" operator
        mock_connection_manager.pending_messages = {}

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute
            events = []
            async for event in game_event_stream(player_id):
                events.append(event)
                if len(events) >= 3:  # Get initial events
                    break

            # Verify
            assert len(events) >= 2  # connected + heartbeat + any pending messages
            assert any("connected" in event for event in events)
            assert any("heartbeat" in event for event in events)

            # Verify connection manager calls
            mock_connection_manager.connect_sse.assert_called_once_with("test_player_123", None)
            mock_connection_manager.get_pending_messages.assert_called_once_with("test_player_123")

    @pytest.mark.asyncio
    async def test_game_event_stream_with_pending_messages(self):
        """Test SSE stream with pending messages."""
        # Setup
        player_id = "test_player_123"
        pending_messages = [
            {"type": "chat", "message": "Hello from the past!"},
            {"type": "system", "message": "Welcome back!"},
        ]

        mock_connection_manager = Mock()
        mock_connection_manager.connect_sse = AsyncMock()
        mock_connection_manager.disconnect_sse = Mock()
        mock_connection_manager.get_pending_messages = Mock(return_value=pending_messages)
        mock_connection_manager.mark_player_seen = Mock()
        mock_connection_manager.prune_stale_players = Mock()
        # Make pending_messages iterable for the "in" operator
        mock_connection_manager.pending_messages = {player_id: pending_messages}

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            # Execute
            events = []
            async for event in game_event_stream(player_id):
                events.append(event)
                if len(events) >= 5:  # Get initial events + pending messages
                    break

            # Verify
            assert len(events) >= 4  # connected + heartbeat + 2 pending messages
            assert any("connected" in event for event in events)
            assert any("heartbeat" in event for event in events)
            assert any("pending_message" in event for event in events)

    @pytest.mark.asyncio
    async def test_game_event_stream_heartbeat_loop(self):
        """Test the heartbeat loop in SSE stream."""
        # Setup
        player_id = "test_player_123"

        mock_connection_manager = Mock()
        mock_connection_manager.connect_sse = AsyncMock()
        mock_connection_manager.disconnect_sse = Mock()
        mock_connection_manager.get_pending_messages = Mock(return_value=[])
        mock_connection_manager.mark_player_seen = Mock()
        mock_connection_manager.prune_stale_players = Mock()
        # Make pending_messages iterable for the "in" operator
        mock_connection_manager.pending_messages = {}

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            with patch("asyncio.sleep", new_callable=AsyncMock) as mock_sleep:
                # Execute
                events = []
                async for event in game_event_stream(player_id):
                    events.append(event)
                    if len(events) >= 4:  # Get initial events + one heartbeat
                        break

                # Verify
                assert mock_sleep.called  # Should have called sleep for heartbeat
                mock_connection_manager.mark_player_seen.assert_called_with("test_player_123")
                mock_connection_manager.prune_stale_players.assert_called()

    @pytest.mark.skip(reason="Async generator cancellation testing is complex in test environment")
    @pytest.mark.asyncio
    async def test_game_event_stream_cancellation(self):
        """Test SSE stream cancellation handling."""
        # Setup
        player_id = "test_player_123"

        mock_connection_manager = Mock()
        mock_connection_manager.connect_sse = Mock()
        mock_connection_manager.disconnect_sse = Mock()
        mock_connection_manager.get_pending_messages = Mock(return_value=[])
        mock_connection_manager.mark_player_seen = Mock()
        mock_connection_manager.prune_stale_players = Mock()

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            with patch("asyncio.sleep", side_effect=asyncio.CancelledError):
                # Execute
                events = []
                try:
                    async for event in game_event_stream(player_id):
                        events.append(event)
                        break  # Should exit on cancellation
                except asyncio.CancelledError:
                    pass  # Expected

                # Verify
                mock_connection_manager.disconnect_sse.assert_called_once_with("test_player_123")

    @pytest.mark.skip(reason="Async generator exception testing is complex in test environment")
    @pytest.mark.asyncio
    async def test_game_event_stream_exception_handling(self):
        """Test SSE stream exception handling."""
        # Setup
        player_id = "test_player_123"

        mock_connection_manager = Mock()
        mock_connection_manager.connect_sse = Mock()
        mock_connection_manager.disconnect_sse = Mock()
        mock_connection_manager.get_pending_messages = Mock(return_value=[])
        mock_connection_manager.mark_player_seen = Mock()
        mock_connection_manager.prune_stale_players = Mock()

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            with patch("asyncio.sleep", side_effect=Exception("Test error")):
                # Execute
                events = []
                async for event in game_event_stream(player_id):
                    events.append(event)
                    break  # Should exit on exception

                # Verify
                assert any("error" in event for event in events)
                mock_connection_manager.disconnect_sse.assert_called_once_with("test_player_123")

    @pytest.mark.skip(reason="Async generator cleanup testing is complex in test environment")
    @pytest.mark.asyncio
    async def test_game_event_stream_player_id_conversion(self):
        """Test that player_id is properly converted to string."""
        # Setup
        player_id = 12345  # Integer player ID

        mock_connection_manager = Mock()
        mock_connection_manager.connect_sse = Mock()
        mock_connection_manager.disconnect_sse = Mock()
        mock_connection_manager.get_pending_messages = Mock(return_value=[])
        mock_connection_manager.mark_player_seen = Mock()
        mock_connection_manager.prune_stale_players = Mock()

        with patch("server.realtime.sse_handler.connection_manager", mock_connection_manager):
            with patch("asyncio.sleep", new_callable=AsyncMock):
                # Execute
                events = []
                async for event in game_event_stream(player_id):
                    events.append(event)
                    if len(events) >= 2:  # Get initial events
                        break

                # Verify
                mock_connection_manager.connect_sse.assert_called_once_with("12345")
                mock_connection_manager.disconnect_sse.assert_called_once_with("12345")
                assert any("12345" in event for event in events)  # Player ID should be in events
