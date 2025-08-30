"""
Comprehensive tests for ConnectionManager to achieve 80%+ coverage.

This module tests all critical codepaths in the connection manager,
including WebSocket connections, SSE connections, room subscriptions,
player tracking, rate limiting, and error handling.
"""

import time
import uuid
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi import WebSocket

from ..realtime.connection_manager import ConnectionManager, MemoryMonitor


class TestConnectionManagerComprehensive:
    """Comprehensive tests for ConnectionManager."""

    @pytest.fixture
    def connection_manager(self):
        """Create a ConnectionManager instance for testing."""
        return ConnectionManager()

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = Mock(spec=WebSocket)
        websocket.accept = AsyncMock()
        websocket.close = AsyncMock()
        websocket.send_json = AsyncMock()
        return websocket

    @pytest.fixture
    def mock_player(self):
        """Create a mock player for testing."""
        player = Mock()
        player.player_id = "test_player_123"
        player.name = "TestPlayer"
        player.level = 5
        player.current_room_id = "test_room_001"
        return player

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        persistence = Mock()
        persistence.get_player = Mock()
        persistence.get_player_by_name = Mock()
        persistence.get_room = Mock()
        return persistence

    @pytest.mark.asyncio
    async def test_connect_websocket_success(self, connection_manager, mock_websocket, mock_player, mock_persistence):
        """Test successful WebSocket connection."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        success = await connection_manager.connect_websocket(mock_websocket, "test_player")

        assert success is True
        assert "test_player" in connection_manager.player_websockets
        assert len(connection_manager.active_websockets) == 1
        mock_websocket.accept.assert_called_once()

    @pytest.mark.asyncio
    async def test_connect_websocket_with_existing_connection(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test WebSocket connection when player already has a connection."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Add existing connection
        existing_websocket = Mock(spec=WebSocket)
        existing_websocket.accept = AsyncMock()
        existing_websocket.close = AsyncMock()
        connection_id = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id] = existing_websocket
        connection_manager.player_websockets["test_player"] = connection_id

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        success = await connection_manager.connect_websocket(mock_websocket, "test_player")

        assert success is True
        # Should have closed old connection
        existing_websocket.close.assert_called_once()

    @pytest.mark.asyncio
    async def test_connect_websocket_failure(self, connection_manager, mock_websocket):
        """Test WebSocket connection failure."""
        mock_websocket.accept.side_effect = Exception("Connection failed")

        success = await connection_manager.connect_websocket(mock_websocket, "test_player")

        assert success is False
        assert "test_player" not in connection_manager.player_websockets

    @pytest.mark.asyncio
    async def test_connect_websocket_without_persistence(self, connection_manager, mock_websocket):
        """Test WebSocket connection when persistence is not set."""
        connection_manager.persistence = None

        success = await connection_manager.connect_websocket(mock_websocket, "test_player")

        assert success is True
        assert "test_player" in connection_manager.player_websockets

    @pytest.mark.asyncio
    async def test_disconnect_websocket_success(self, connection_manager, mock_websocket):
        """Test successful WebSocket disconnection."""
        # Setup connection
        connection_id = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id] = mock_websocket
        connection_manager.player_websockets["test_player"] = connection_id

        await connection_manager.disconnect_websocket("test_player")

        assert "test_player" not in connection_manager.player_websockets
        assert connection_id not in connection_manager.active_websockets

    @pytest.mark.asyncio
    async def test_disconnect_websocket_not_found(self, connection_manager):
        """Test WebSocket disconnection for non-existent player."""
        await connection_manager.disconnect_websocket("nonexistent_player")
        # Should not raise any exceptions

    @pytest.mark.asyncio
    async def test_disconnect_websocket_with_room_subscriptions(self, connection_manager, mock_websocket):
        """Test WebSocket disconnection with room subscriptions."""
        # Setup connection and room subscription
        connection_id = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id] = mock_websocket
        connection_manager.player_websockets["test_player"] = connection_id
        connection_manager.room_subscriptions["test_room"] = {"test_player", "other_player"}

        await connection_manager.disconnect_websocket("test_player")

        assert "test_player" not in connection_manager.room_subscriptions["test_room"]
        assert "other_player" in connection_manager.room_subscriptions["test_room"]

    @pytest.mark.asyncio
    async def test_force_disconnect_player(self, connection_manager, mock_websocket):
        """Test force disconnect player from all connections."""
        # Setup WebSocket connection
        connection_id = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id] = mock_websocket
        connection_manager.player_websockets["test_player"] = connection_id

        # Setup SSE connection
        connection_manager.active_sse_connections["test_player"] = "sse_conn_id"

        await connection_manager.force_disconnect_player("test_player")

        assert "test_player" not in connection_manager.player_websockets
        assert "test_player" not in connection_manager.active_sse_connections

    @pytest.mark.asyncio
    async def test_connect_sse_success(self, connection_manager):
        """Test successful SSE connection."""
        connection_id = await connection_manager.connect_sse("test_player")

        assert connection_id is not None
        assert "test_player" in connection_manager.active_sse_connections
        assert connection_manager.active_sse_connections["test_player"] == connection_id

    @pytest.mark.asyncio
    async def test_connect_sse_with_existing_websocket(self, connection_manager, mock_websocket):
        """Test SSE connection when player has existing WebSocket."""
        # Setup existing WebSocket
        connection_id = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id] = mock_websocket
        connection_manager.player_websockets["test_player"] = connection_id

        with patch.object(
            connection_manager, "force_disconnect_player", new_callable=AsyncMock
        ) as mock_force_disconnect:
            sse_connection_id = await connection_manager.connect_sse("test_player")

            assert sse_connection_id is not None
            mock_force_disconnect.assert_called_once_with("test_player")

    def test_disconnect_sse_success(self, connection_manager):
        """Test successful SSE disconnection."""
        # Setup SSE connection
        connection_manager.active_sse_connections["test_player"] = "sse_conn_id"
        connection_manager.connection_attempts["test_player"] = [time.time()]
        connection_manager.pending_messages["test_player"] = [{"test": "message"}]
        connection_manager.last_seen["test_player"] = time.time()

        connection_manager.disconnect_sse("test_player")

        assert "test_player" not in connection_manager.active_sse_connections
        assert "test_player" not in connection_manager.connection_attempts
        assert "test_player" not in connection_manager.pending_messages
        assert "test_player" not in connection_manager.last_seen

    def test_disconnect_sse_not_found(self, connection_manager):
        """Test SSE disconnection for non-existent player."""
        connection_manager.disconnect_sse("nonexistent_player")
        # Should not raise any exceptions

    def test_mark_player_seen(self, connection_manager):
        """Test marking player as seen."""
        connection_manager.mark_player_seen("test_player")

        assert "test_player" in connection_manager.last_seen
        assert isinstance(connection_manager.last_seen["test_player"], float)

    def test_mark_player_seen_exception(self, connection_manager):
        """Test marking player as seen with exception."""
        with patch.object(connection_manager, "last_seen", create=True) as mock_last_seen:
            mock_last_seen.__setitem__.side_effect = Exception("Test exception")
            connection_manager.mark_player_seen("test_player")
            # Should not raise exception

    def test_prune_stale_players(self, connection_manager):
        """Test pruning stale players."""
        # Add some players with different timestamps
        connection_manager.last_seen["recent_player"] = time.time()
        connection_manager.last_seen["stale_player"] = time.time() - 200  # 200 seconds ago
        connection_manager.online_players["recent_player"] = {"player_id": "recent_player"}
        connection_manager.online_players["stale_player"] = {"player_id": "stale_player"}
        connection_manager.room_occupants["test_room"] = {"recent_player", "stale_player"}

        connection_manager.prune_stale_players(max_age_seconds=90)

        assert "recent_player" in connection_manager.online_players
        assert "stale_player" not in connection_manager.online_players
        assert "stale_player" not in connection_manager.last_seen

    def test_prune_stale_players_exception(self, connection_manager):
        """Test pruning stale players with exception."""
        with patch.object(connection_manager, "last_seen", create=True) as mock_last_seen:
            mock_last_seen.items.side_effect = Exception("Test exception")
            connection_manager.prune_stale_players()
            # Should not raise exception

    @pytest.mark.asyncio
    async def test_cleanup_orphaned_data_exception(self, connection_manager):
        """Test cleanup orphaned data with exception."""
        with patch.object(connection_manager, "connection_attempts", create=True) as mock_attempts:
            mock_attempts.items.side_effect = Exception("Test exception")
            await connection_manager.cleanup_orphaned_data()
            # Should not raise exception

    def test_get_active_connection_count(self, connection_manager, mock_websocket):
        """Test getting active connection count."""
        # Add WebSocket connection
        connection_manager.active_websockets["ws_conn"] = mock_websocket

        # Add SSE connection
        connection_manager.active_sse_connections["sse_player"] = "sse_conn"

        count = connection_manager.get_active_connection_count()
        assert count == 2

    def test_check_rate_limit_first_attempt(self, connection_manager):
        """Test rate limit check for first attempt."""
        result = connection_manager.check_rate_limit("test_player")

        assert result is True
        assert "test_player" in connection_manager.connection_attempts
        assert len(connection_manager.connection_attempts["test_player"]) == 1

    def test_check_rate_limit_within_limit(self, connection_manager):
        """Test rate limit check within limit."""
        # Add some attempts
        current_time = time.time()
        connection_manager.connection_attempts["test_player"] = [
            current_time - 30,  # 30 seconds ago
            current_time - 20,  # 20 seconds ago
        ]

        result = connection_manager.check_rate_limit("test_player")

        assert result is True
        assert len(connection_manager.connection_attempts["test_player"]) == 3

    def test_check_rate_limit_exceeded(self, connection_manager):
        """Test rate limit check when limit exceeded."""
        # Add maximum attempts
        current_time = time.time()
        connection_manager.connection_attempts["test_player"] = [
            current_time - 30,
            current_time - 20,
            current_time - 10,
            current_time - 5,
            current_time - 2,
        ]

        result = connection_manager.check_rate_limit("test_player")

        assert result is False

    def test_check_rate_limit_old_attempts_removed(self, connection_manager):
        """Test that old rate limit attempts are removed."""
        # Add old attempts
        old_time = time.time() - 120  # 2 minutes ago
        connection_manager.connection_attempts["test_player"] = [old_time]

        result = connection_manager.check_rate_limit("test_player")

        assert result is True
        assert len(connection_manager.connection_attempts["test_player"]) == 1
        assert connection_manager.connection_attempts["test_player"][0] > old_time

    def test_get_rate_limit_info(self, connection_manager):
        """Test getting rate limit information."""
        # Add some attempts
        current_time = time.time()
        connection_manager.connection_attempts["test_player"] = [
            current_time - 30,
            current_time - 20,
        ]

        info = connection_manager.get_rate_limit_info("test_player")

        assert info["attempts"] == 2
        assert info["max_attempts"] == 5
        assert info["window_seconds"] == 60
        assert info["attempts_remaining"] == 3
        assert info["reset_time"] > current_time

    def test_get_rate_limit_info_no_attempts(self, connection_manager):
        """Test getting rate limit info for player with no attempts."""
        info = connection_manager.get_rate_limit_info("test_player")

        assert info["attempts"] == 0
        assert info["attempts_remaining"] == 5
        assert info["reset_time"] == 0

    @pytest.mark.asyncio
    async def test_subscribe_to_room(self, connection_manager):
        """Test subscribing to a room."""
        await connection_manager.subscribe_to_room("test_player", "test_room")

        assert "test_room" in connection_manager.room_subscriptions
        assert "test_player" in connection_manager.room_subscriptions["test_room"]

    @pytest.mark.asyncio
    async def test_subscribe_to_room_with_canonical_id(self, connection_manager, mock_persistence):
        """Test subscribing to room with canonical ID resolution."""
        connection_manager.persistence = mock_persistence

        # Mock room with canonical ID
        mock_room = Mock()
        mock_room.id = "canonical_room_id"
        mock_persistence.get_room.return_value = mock_room

        await connection_manager.subscribe_to_room("test_player", "original_room_id")

        assert "canonical_room_id" in connection_manager.room_subscriptions
        assert "test_player" in connection_manager.room_subscriptions["canonical_room_id"]

    @pytest.mark.asyncio
    async def test_unsubscribe_from_room(self, connection_manager):
        """Test unsubscribing from a room."""
        # Setup subscription
        connection_manager.room_subscriptions["test_room"] = {"test_player", "other_player"}

        await connection_manager.unsubscribe_from_room("test_player", "test_room")

        assert "test_player" not in connection_manager.room_subscriptions["test_room"]
        assert "other_player" in connection_manager.room_subscriptions["test_room"]

    @pytest.mark.asyncio
    async def test_unsubscribe_from_room_empty(self, connection_manager):
        """Test unsubscribing from room when it becomes empty."""
        # Setup subscription with only one player
        connection_manager.room_subscriptions["test_room"] = {"test_player"}

        await connection_manager.unsubscribe_from_room("test_player", "test_room")

        assert "test_room" not in connection_manager.room_subscriptions

    def test_get_next_sequence(self, connection_manager):
        """Test getting next sequence number."""
        initial_counter = connection_manager.sequence_counter

        sequence1 = connection_manager._get_next_sequence()
        sequence2 = connection_manager._get_next_sequence()

        assert sequence1 == initial_counter + 1
        assert sequence2 == initial_counter + 2

    def test_canonical_room_id_with_persistence(self, connection_manager, mock_persistence):
        """Test canonical room ID resolution with persistence."""
        connection_manager.persistence = mock_persistence

        # Mock room with canonical ID
        mock_room = Mock()
        mock_room.id = "canonical_id"
        mock_persistence.get_room.return_value = mock_room

        canonical_id = connection_manager._canonical_room_id("original_id")

        assert canonical_id == "canonical_id"

    def test_canonical_room_id_without_persistence(self, connection_manager):
        """Test canonical room ID resolution without persistence."""
        connection_manager.persistence = None

        canonical_id = connection_manager._canonical_room_id("original_id")

        assert canonical_id == "original_id"

    def test_canonical_room_id_none_input(self, connection_manager):
        """Test canonical room ID resolution with None input."""
        canonical_id = connection_manager._canonical_room_id(None)

        assert canonical_id is None

    def test_canonical_room_id_exception(self, connection_manager, mock_persistence):
        """Test canonical room ID resolution with exception."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_room.side_effect = Exception("Test exception")

        canonical_id = connection_manager._canonical_room_id("original_id")

        assert canonical_id == "original_id"

    @pytest.mark.asyncio
    async def test_send_personal_message_websocket_success(self, connection_manager, mock_websocket):
        """Test sending personal message via WebSocket."""
        # Setup WebSocket connection
        connection_id = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id] = mock_websocket
        connection_manager.player_websockets["test_player"] = connection_id

        event = {"type": "test_event", "data": "test_data"}
        result = await connection_manager.send_personal_message("test_player", event)

        assert result is True
        mock_websocket.send_json.assert_called_once_with(event)

    @pytest.mark.asyncio
    async def test_send_personal_message_fallback_to_pending(self, connection_manager):
        """Test sending personal message falls back to pending messages."""
        event = {"type": "test_event", "data": "test_data"}
        result = await connection_manager.send_personal_message("test_player", event)

        assert result is True
        assert "test_player" in connection_manager.pending_messages
        assert event in connection_manager.pending_messages["test_player"]

    @pytest.mark.asyncio
    async def test_send_personal_message_exception(self, connection_manager, mock_websocket):
        """Test sending personal message with exception."""
        # Setup WebSocket connection
        connection_id = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id] = mock_websocket
        connection_manager.player_websockets["test_player"] = connection_id
        mock_websocket.send_json.side_effect = Exception("Test exception")

        event = {"type": "test_event", "data": "test_data"}
        result = await connection_manager.send_personal_message("test_player", event)

        assert result is False

    @pytest.mark.asyncio
    async def test_broadcast_to_room(self, connection_manager, mock_websocket):
        """Test broadcasting to room."""
        # Setup room subscription
        connection_manager.room_subscriptions["test_room"] = {"player1", "player2"}

        # Setup WebSocket connections
        connection_id1 = str(uuid.uuid4())
        connection_id2 = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id1] = mock_websocket
        connection_manager.active_websockets[connection_id2] = mock_websocket
        connection_manager.player_websockets["player1"] = connection_id1
        connection_manager.player_websockets["player2"] = connection_id2

        event = {"type": "room_event", "data": "test_data"}
        await connection_manager.broadcast_to_room("test_room", event)

        # Should have sent to both players
        assert mock_websocket.send_json.call_count == 2

    @pytest.mark.asyncio
    async def test_broadcast_to_room_with_exclude(self, connection_manager, mock_websocket):
        """Test broadcasting to room with excluded player."""
        # Setup room subscription
        connection_manager.room_subscriptions["test_room"] = {"player1", "player2"}

        # Setup WebSocket connections
        connection_id1 = str(uuid.uuid4())
        connection_id2 = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id1] = mock_websocket
        connection_manager.active_websockets[connection_id2] = mock_websocket
        connection_manager.player_websockets["player1"] = connection_id1
        connection_manager.player_websockets["player2"] = connection_id2

        event = {"type": "room_event", "data": "test_data"}
        await connection_manager.broadcast_to_room("test_room", event, exclude_player="player1")

        # Should have sent to only player2
        assert mock_websocket.send_json.call_count == 1

    @pytest.mark.asyncio
    async def test_broadcast_global(self, connection_manager, mock_websocket):
        """Test global broadcast."""
        # Setup WebSocket connections
        connection_id1 = str(uuid.uuid4())
        connection_id2 = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id1] = mock_websocket
        connection_manager.active_websockets[connection_id2] = mock_websocket
        connection_manager.player_websockets["player1"] = connection_id1
        connection_manager.player_websockets["player2"] = connection_id2

        event = {"type": "global_event", "data": "test_data"}
        await connection_manager.broadcast_global(event)

        # Should have sent to both players
        assert mock_websocket.send_json.call_count == 2

    def test_get_pending_messages(self, connection_manager):
        """Test getting pending messages."""
        # Setup pending messages
        messages = [{"type": "msg1"}, {"type": "msg2"}]
        connection_manager.pending_messages["test_player"] = messages

        result = connection_manager.get_pending_messages("test_player")

        assert result == messages
        assert "test_player" not in connection_manager.pending_messages

    def test_get_pending_messages_empty(self, connection_manager):
        """Test getting pending messages for player with none."""
        result = connection_manager.get_pending_messages("test_player")

        assert result == []

    def test_get_player_with_persistence(self, connection_manager, mock_persistence, mock_player):
        """Test getting player with persistence."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        result = connection_manager._get_player("test_player")

        assert result == mock_player
        mock_persistence.get_player.assert_called_once_with("test_player")

    def test_get_player_fallback_to_name(self, connection_manager, mock_persistence, mock_player):
        """Test getting player falls back to name lookup."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = None
        mock_persistence.get_player_by_name.return_value = mock_player

        result = connection_manager._get_player("test_player")

        assert result == mock_player
        mock_persistence.get_player_by_name.assert_called_once_with("test_player")

    def test_get_player_not_found(self, connection_manager, mock_persistence):
        """Test getting player that doesn't exist."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = None
        mock_persistence.get_player_by_name.return_value = None

        result = connection_manager._get_player("test_player")

        assert result is None

    def test_get_player_no_persistence(self, connection_manager):
        """Test getting player without persistence layer."""
        connection_manager.persistence = None

        result = connection_manager._get_player("test_player")

        assert result is None

    @pytest.mark.asyncio
    async def test_track_player_connected(self, connection_manager, mock_player, mock_persistence):
        """Test tracking player connection."""
        connection_manager.persistence = mock_persistence

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        await connection_manager._track_player_connected("test_player", mock_player)

        assert "test_player" in connection_manager.online_players
        assert "test_room_001" in connection_manager.room_occupants
        assert "test_player" in connection_manager.room_occupants["test_room_001"]

    @pytest.mark.asyncio
    async def test_track_player_connected_exception(self, connection_manager, mock_player):
        """Test tracking player connection with exception."""
        with patch.object(connection_manager, "online_players", create=True) as mock_online:
            mock_online.__setitem__.side_effect = Exception("Test exception")
            await connection_manager._track_player_connected("test_player", mock_player)
            # Should not raise exception

    @pytest.mark.asyncio
    async def test_track_player_disconnected(self, connection_manager, mock_player, mock_persistence):
        """Test tracking player disconnection."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Setup player in online players and room
        connection_manager.online_players["test_player"] = {"player_id": "test_player"}
        connection_manager.room_occupants["test_room_001"] = {"test_player"}

        await connection_manager._track_player_disconnected("test_player")

        assert "test_player" not in connection_manager.online_players
        # The room might be removed entirely if it becomes empty
        if "test_room_001" in connection_manager.room_occupants:
            assert "test_player" not in connection_manager.room_occupants["test_room_001"]

    @pytest.mark.asyncio
    async def test_track_player_disconnected_exception(self, connection_manager):
        """Test tracking player disconnection with exception."""
        with patch.object(connection_manager, "online_players", create=True) as mock_online:
            mock_online.__delitem__.side_effect = Exception("Test exception")
            await connection_manager._track_player_disconnected("test_player")
            # Should not raise exception

    def test_get_online_players(self, connection_manager):
        """Test getting online players."""
        # Setup some online players
        connection_manager.online_players["player1"] = {"player_id": "player1"}
        connection_manager.online_players["player2"] = {"player_id": "player2"}

        result = connection_manager.get_online_players()

        assert len(result) == 2
        assert {"player_id": "player1"} in result
        assert {"player_id": "player2"} in result

    def test_get_room_occupants(self, connection_manager):
        """Test getting room occupants."""
        # Setup room occupants
        connection_manager.room_occupants["test_room"] = {"player1", "player2"}
        connection_manager.online_players["player1"] = {"player_id": "player1"}
        connection_manager.online_players["player2"] = {"player_id": "player2"}

        result = connection_manager.get_room_occupants("test_room")

        assert len(result) == 2
        assert {"player_id": "player1"} in result
        assert {"player_id": "player2"} in result

    def test_get_room_occupants_empty(self, connection_manager):
        """Test getting room occupants for empty room."""
        result = connection_manager.get_room_occupants("empty_room")

        assert result == []

    def test_get_room_occupants_offline_players_filtered(self, connection_manager):
        """Test that offline players are filtered from room occupants."""
        # Setup room occupants with offline player
        connection_manager.room_occupants["test_room"] = {"player1", "player2"}
        connection_manager.online_players["player1"] = {"player_id": "player1"}
        # player2 is not in online_players (offline)

        result = connection_manager.get_room_occupants("test_room")

        assert len(result) == 1
        assert {"player_id": "player1"} in result

    @pytest.mark.asyncio
    async def test_send_initial_game_state(self, connection_manager, mock_player, mock_persistence):
        """Test sending initial game state."""
        connection_manager.persistence = mock_persistence

        # Mock room
        mock_room = Mock()
        mock_room.to_dict.return_value = {"room_id": "test_room_001", "name": "Test Room"}
        mock_persistence.get_room.return_value = mock_room

        # Setup room occupants
        connection_manager.room_occupants["test_room_001"] = {"other_player"}
        connection_manager.online_players["other_player"] = {"player_id": "other_player", "name": "OtherPlayer"}

        with patch.object(connection_manager, "send_personal_message", new_callable=AsyncMock) as mock_send:
            await connection_manager._send_initial_game_state("test_player", mock_player, "test_room_001")

            mock_send.assert_called_once()
            call_args = mock_send.call_args[0]
            assert call_args[0] == "test_player"  # player_id
            assert call_args[1]["event_type"] == "game_state"  # event type

    @pytest.mark.asyncio
    async def test_send_initial_game_state_exception(self, connection_manager, mock_player):
        """Test sending initial game state with exception."""
        with patch.object(connection_manager, "send_personal_message", new_callable=AsyncMock) as mock_send:
            mock_send.side_effect = Exception("Test exception")
            await connection_manager._send_initial_game_state("test_player", mock_player, "test_room_001")
            # Should not raise exception

    def test_reconcile_room_presence(self, connection_manager):
        """Test reconciling room presence."""
        # Setup room with online and offline players
        connection_manager.room_occupants["test_room"] = {"online_player", "offline_player"}
        connection_manager.online_players["online_player"] = {"player_id": "online_player"}

        connection_manager._reconcile_room_presence("test_room")

        assert "online_player" in connection_manager.room_occupants["test_room"]
        assert "offline_player" not in connection_manager.room_occupants["test_room"]

    def test_reconcile_room_presence_exception(self, connection_manager):
        """Test reconciling room presence with exception."""
        with patch.object(connection_manager, "room_occupants", create=True) as mock_occupants:
            mock_occupants.__getitem__.side_effect = Exception("Test exception")
            connection_manager._reconcile_room_presence("test_room")
            # Should not raise exception

    @pytest.mark.asyncio
    async def test_check_and_cleanup_triggered(self, connection_manager):
        """Test check and cleanup when triggered."""
        with patch.object(connection_manager.memory_monitor, "should_cleanup", return_value=True):
            with patch.object(connection_manager, "cleanup_orphaned_data", new_callable=AsyncMock) as mock_cleanup:
                with patch.object(connection_manager, "prune_stale_players") as mock_prune:
                    await connection_manager._check_and_cleanup()

                    mock_cleanup.assert_called_once()
                    mock_prune.assert_called_once()

    @pytest.mark.asyncio
    async def test_check_and_cleanup_not_triggered(self, connection_manager):
        """Test check and cleanup when not triggered."""
        with patch.object(connection_manager.memory_monitor, "should_cleanup", return_value=False):
            with patch.object(connection_manager, "cleanup_orphaned_data", new_callable=AsyncMock) as mock_cleanup:
                with patch.object(connection_manager, "prune_stale_players") as mock_prune:
                    await connection_manager._check_and_cleanup()

                    mock_cleanup.assert_not_called()
                    mock_prune.assert_not_called()

    def test_get_memory_stats_exception(self, connection_manager):
        """Test getting memory stats with exception."""
        with patch.object(
            connection_manager.memory_monitor, "get_memory_stats", side_effect=Exception("Test exception")
        ):
            result = connection_manager.get_memory_stats()

            assert result == {}

    def test_get_memory_alerts_exception(self, connection_manager):
        """Test getting memory alerts with exception."""
        with patch.object(
            connection_manager.memory_monitor, "get_memory_usage", side_effect=Exception("Test exception")
        ):
            result = connection_manager.get_memory_alerts()

            assert len(result) == 1
            assert "ERROR: Failed to get memory alerts" in result[0]

    @pytest.mark.asyncio
    async def test_force_cleanup_exception(self, connection_manager):
        """Test force cleanup with exception."""
        with patch.object(connection_manager, "cleanup_orphaned_data", side_effect=Exception("Test exception")):
            await connection_manager.force_cleanup()
            # Should not raise exception

    def test_prune_player_from_all_rooms(self, connection_manager):
        """Test pruning player from all rooms."""
        # Setup player in multiple rooms
        connection_manager.room_occupants["room1"] = {"player1", "player2"}
        connection_manager.room_occupants["room2"] = {"player1", "player3"}
        connection_manager.room_occupants["room3"] = {"player2", "player3"}

        connection_manager._prune_player_from_all_rooms("player1")

        assert "player1" not in connection_manager.room_occupants["room1"]
        assert "player1" not in connection_manager.room_occupants["room2"]
        assert "player2" in connection_manager.room_occupants["room1"]
        assert "player3" in connection_manager.room_occupants["room2"]
        assert "player2" in connection_manager.room_occupants["room3"]

    def test_prune_player_from_all_rooms_exception(self, connection_manager):
        """Test pruning player from all rooms with exception."""
        with patch.object(connection_manager, "room_occupants", create=True) as mock_occupants:
            mock_occupants.keys.side_effect = Exception("Test exception")
            connection_manager._prune_player_from_all_rooms("player1")
            # Should not raise exception

    @pytest.mark.asyncio
    async def test_cleanup_orphaned_data_with_large_structures(self, connection_manager):
        """Test cleanup with large data structures that need trimming."""
        # Add large rate limit entries
        connection_manager.connection_attempts["player1"] = [time.time()] * 1500  # Over limit

        # Add large pending message queue
        connection_manager.pending_messages["player1"] = [{"timestamp": time.time()}] * 1500  # Over limit

        # Add stale connection
        connection_manager.active_websockets["stale_conn"] = Mock()
        connection_manager.connection_timestamps["stale_conn"] = time.time() - 4000  # Old

        await connection_manager.cleanup_orphaned_data()

        # Check that data was limited
        assert (
            len(connection_manager.connection_attempts["player1"])
            <= connection_manager.memory_monitor.max_rate_limit_entries
        )
        assert (
            len(connection_manager.pending_messages["player1"])
            <= connection_manager.memory_monitor.max_pending_messages
        )
        assert "stale_conn" not in connection_manager.active_websockets

    @pytest.mark.asyncio
    async def test_cleanup_orphaned_data_with_old_messages(self, connection_manager):
        """Test cleanup with old messages that should be removed."""
        # Add old messages
        old_time = time.time() - 4000  # 1+ hours ago
        connection_manager.pending_messages["player1"] = [{"timestamp": old_time}]
        connection_manager.connection_attempts["player1"] = [old_time]

        await connection_manager.cleanup_orphaned_data()

        # Check that old data was removed
        assert "player1" not in connection_manager.pending_messages
        assert "player1" not in connection_manager.connection_attempts

    @pytest.mark.asyncio
    async def test_cleanup_orphaned_data_with_empty_structures(self, connection_manager):
        """Test cleanup with empty data structures."""
        # Add empty structures
        connection_manager.pending_messages["player1"] = []
        connection_manager.connection_attempts["player1"] = []

        await connection_manager.cleanup_orphaned_data()

        # Check that empty structures were removed
        assert "player1" not in connection_manager.pending_messages
        assert "player1" not in connection_manager.connection_attempts

    @pytest.mark.asyncio
    async def test_cleanup_orphaned_data_with_stale_connection_exception(self, connection_manager, mock_websocket):
        """Test cleanup with stale connection that raises exception on close."""
        # Add stale connection
        connection_manager.active_websockets["stale_conn"] = mock_websocket
        connection_manager.connection_timestamps["stale_conn"] = time.time() - 4000  # Old
        mock_websocket.close.side_effect = Exception("Close failed")

        await connection_manager.cleanup_orphaned_data()

        # Should still remove the connection despite close failure
        assert "stale_conn" not in connection_manager.active_websockets
        assert "stale_conn" not in connection_manager.connection_timestamps

    @pytest.mark.asyncio
    async def test_connect_sse_with_existing_sse_connection(self, connection_manager):
        """Test SSE connection when player has existing SSE connection."""
        # Setup existing SSE connection
        connection_manager.active_sse_connections["test_player"] = "existing_sse_id"

        with patch.object(
            connection_manager, "force_disconnect_player", new_callable=AsyncMock
        ) as mock_force_disconnect:
            sse_connection_id = await connection_manager.connect_sse("test_player")

            assert sse_connection_id is not None
            mock_force_disconnect.assert_called_once_with("test_player")

    @pytest.mark.asyncio
    async def test_connect_sse_with_player_tracking(self, connection_manager, mock_player, mock_persistence):
        """Test SSE connection with player tracking."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        with patch.object(connection_manager, "subscribe_to_room", new_callable=AsyncMock) as mock_subscribe:
            with patch.object(connection_manager, "_track_player_connected", new_callable=AsyncMock) as mock_track:
                sse_connection_id = await connection_manager.connect_sse("test_player")

                assert sse_connection_id is not None
                mock_subscribe.assert_called_once_with("test_player", "test_room_001")
                mock_track.assert_called_once_with("test_player", mock_player)

    @pytest.mark.asyncio
    async def test_connect_sse_with_room_resolution_exception(self, connection_manager, mock_player, mock_persistence):
        """Test SSE connection with room resolution exception."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player
        mock_persistence.get_room.side_effect = Exception("Room resolution failed")

        sse_connection_id = await connection_manager.connect_sse("test_player")

        assert sse_connection_id is not None
        # Should not raise exception

    def test_disconnect_sse_with_async_tracking(self, connection_manager):
        """Test SSE disconnection with async tracking."""
        # Setup SSE connection
        connection_manager.active_sse_connections["test_player"] = "sse_conn_id"

        # Create a mock that returns a completed coroutine
        async def mock_track_async(player_id):
            return None

        with patch.object(connection_manager, "_track_player_disconnected", side_effect=mock_track_async) as mock_track:
            connection_manager.disconnect_sse("test_player")

            mock_track.assert_called_once_with("test_player")

    def test_disconnect_sse_with_sync_tracking(self, connection_manager):
        """Test SSE disconnection with sync tracking (no running loop)."""
        # Setup SSE connection
        connection_manager.active_sse_connections["test_player"] = "sse_conn_id"

        with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
            with patch("asyncio.run") as mock_run:
                connection_manager.disconnect_sse("test_player")

                mock_run.assert_called_once()

    @pytest.mark.filterwarnings("ignore:coroutine.*was never awaited:RuntimeWarning")
    def test_disconnect_sse_with_tracking_exception(self, connection_manager):
        """Test SSE disconnection with tracking exception."""
        # Setup SSE connection
        connection_manager.active_sse_connections["test_player"] = "sse_conn_id"

        # Mock the entire async context to avoid unawaited coroutine warnings
        with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
            # Mock asyncio.run to prevent the actual coroutine execution
            with patch("asyncio.run") as mock_run:
                mock_run.side_effect = Exception("Tracking failed")
                # Mock the method to prevent any coroutine creation
                with patch.object(connection_manager, "_check_and_process_disconnect") as mock_check:
                    # Set the mock to do nothing when called
                    mock_check.return_value = None
                    connection_manager.disconnect_sse("test_player")
                    # Should not raise exception


class TestMemoryMonitorComprehensive:
    """Comprehensive tests for MemoryMonitor."""

    def test_memory_monitor_get_memory_usage_exception(self):
        """Test memory usage calculation with exception."""
        monitor = MemoryMonitor()

        with patch("psutil.Process", side_effect=Exception("Test exception")):
            result = monitor.get_memory_usage()

            assert result == 0.0

    @pytest.mark.filterwarnings("ignore:coroutine.*was never awaited:RuntimeWarning")
    def test_memory_monitor_get_memory_stats_exception(self):
        """Test memory stats calculation with exception."""
        monitor = MemoryMonitor()

        with patch("psutil.Process", side_effect=Exception("Test exception")):
            result = monitor.get_memory_stats()

            assert result == {}

    def test_memory_monitor_get_memory_stats_virtual_memory_exception(self):
        """Test memory stats calculation with virtual memory exception."""
        monitor = MemoryMonitor()

        with patch("psutil.Process") as mock_process:
            mock_process.return_value.memory_info.return_value.rss = 1024 * 1024 * 100
            mock_process.return_value.memory_info.return_value.vms = 1024 * 1024 * 200
            mock_process.return_value.memory_percent.return_value = 50.0

            with patch("psutil.virtual_memory", side_effect=Exception("Test exception")):
                result = monitor.get_memory_stats()

                assert result == {}
