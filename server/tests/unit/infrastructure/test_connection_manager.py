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

from server.realtime.connection_manager import ConnectionManager, ConnectionMetadata, MemoryMonitor


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
        # Mock client_state for connection health checks
        websocket.client_state = Mock()
        websocket.client_state.name = "CONNECTED"
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

    def _create_mock_websocket(self):
        """Create a properly configured mock WebSocket."""
        websocket = Mock(spec=WebSocket)
        websocket.accept = AsyncMock()
        websocket.close = AsyncMock()
        websocket.ping = AsyncMock()
        # Mock client_state for connection health checks
        websocket.client_state = Mock()
        websocket.client_state.name = "CONNECTED"
        return websocket

    def _setup_mock_room(self, mock_persistence, room_id="test_room_001"):
        """Set up a properly configured mock room."""
        mock_room = Mock()
        mock_room.id = room_id
        mock_room.get_npcs.return_value = []  # Return empty list for NPCs
        mock_room.get_occupant_count.return_value = 1  # Return occupant count
        mock_room.to_dict.return_value = {}  # Return empty dict for room data
        mock_persistence.get_room.return_value = mock_room
        return mock_room

    def test_connection_manager_initialization(self, connection_manager):
        """Test ConnectionManager initialization with new data structures."""
        # Test that new data structures are properly initialized
        assert isinstance(connection_manager.player_websockets, dict)
        assert isinstance(connection_manager.active_sse_connections, dict)
        assert isinstance(connection_manager.connection_metadata, dict)

        # Test that they are empty initially
        assert len(connection_manager.player_websockets) == 0
        assert len(connection_manager.active_sse_connections) == 0
        assert len(connection_manager.connection_metadata) == 0

    def test_connection_metadata_dataclass(self):
        """Test ConnectionMetadata dataclass creation and properties."""
        connection_id = "test_connection_123"
        player_id = "test_player_456"
        connection_type = "websocket"
        established_at = time.time()
        last_seen = time.time()
        is_healthy = True
        session_id = "test_session_789"

        metadata = ConnectionMetadata(
            connection_id=connection_id,
            player_id=player_id,
            connection_type=connection_type,
            established_at=established_at,
            last_seen=last_seen,
            is_healthy=is_healthy,
            session_id=session_id,
        )

        assert metadata.connection_id == connection_id
        assert metadata.player_id == player_id
        assert metadata.connection_type == connection_type
        assert metadata.established_at == established_at
        assert metadata.last_seen == last_seen
        assert metadata.is_healthy == is_healthy
        assert metadata.session_id == session_id

    def test_connection_metadata_optional_session_id(self):
        """Test ConnectionMetadata with optional session_id."""
        metadata = ConnectionMetadata(
            connection_id="test_connection_123",
            player_id="test_player_456",
            connection_type="sse",
            established_at=time.time(),
            last_seen=time.time(),
            is_healthy=True,
        )

        assert metadata.session_id is None

    def test_compatibility_methods(self, connection_manager):
        """Test backward compatibility methods for new data structures."""
        player_id = "test_player_123"

        # Test with no connections
        assert connection_manager.get_player_websocket_connection_id(player_id) is None
        assert connection_manager.get_player_sse_connection_id(player_id) is None
        assert connection_manager.has_websocket_connection(player_id) is False
        assert connection_manager.has_sse_connection(player_id) is False

        connection_counts = connection_manager.get_connection_count(player_id)
        assert connection_counts["websocket"] == 0
        assert connection_counts["sse"] == 0
        assert connection_counts["total"] == 0

        # Test with WebSocket connections
        connection_id_1 = "ws_conn_1"
        connection_id_2 = "ws_conn_2"
        connection_manager.player_websockets[player_id] = [connection_id_1, connection_id_2]

        assert connection_manager.get_player_websocket_connection_id(player_id) == connection_id_1
        assert connection_manager.has_websocket_connection(player_id) is True

        connection_counts = connection_manager.get_connection_count(player_id)
        assert connection_counts["websocket"] == 2
        assert connection_counts["sse"] == 0
        assert connection_counts["total"] == 2

        # Test with SSE connections
        sse_connection_id_1 = "sse_conn_1"
        sse_connection_id_2 = "sse_conn_2"
        connection_manager.active_sse_connections[player_id] = [sse_connection_id_1, sse_connection_id_2]

        assert connection_manager.get_player_sse_connection_id(player_id) == sse_connection_id_1
        assert connection_manager.has_sse_connection(player_id) is True

        connection_counts = connection_manager.get_connection_count(player_id)
        assert connection_counts["websocket"] == 2
        assert connection_counts["sse"] == 2
        assert connection_counts["total"] == 4

    def test_data_structure_backward_compatibility(self, connection_manager):
        """Test that new data structures maintain backward compatibility."""
        player_id = "test_player_123"

        # Test that we can still access the first connection ID for backward compatibility
        connection_id = "test_connection_456"
        connection_manager.player_websockets[player_id] = [connection_id]

        # This should work with existing code that expects a single connection ID
        first_connection_id = connection_manager.get_player_websocket_connection_id(player_id)
        assert first_connection_id == connection_id

        # Test with multiple connections - should return the first one
        connection_id_2 = "test_connection_789"
        connection_manager.player_websockets[player_id].append(connection_id_2)

        first_connection_id = connection_manager.get_player_websocket_connection_id(player_id)
        assert first_connection_id == connection_id  # Should still be the first one

    @pytest.mark.asyncio
    async def test_connect_websocket_with_session_tracking(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test WebSocket connection with session tracking."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        session_id = "test_session_123"
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", session_id)

        assert success is True
        assert "test_player" in connection_manager.player_websockets
        assert len(connection_manager.active_websockets) == 1

        # Check that connection metadata includes session_id
        connection_id = connection_manager.get_player_websocket_connection_id("test_player")
        assert connection_id in connection_manager.connection_metadata
        metadata = connection_manager.connection_metadata[connection_id]
        assert metadata.session_id == session_id
        assert metadata.connection_type == "websocket"
        assert metadata.player_id == "test_player"

    @pytest.mark.asyncio
    async def test_connect_sse_with_session_tracking(self, connection_manager):
        """Test SSE connection with session tracking."""
        session_id = "test_session_456"
        connection_id = await connection_manager.connect_sse("test_player", session_id)

        assert connection_id is not None
        assert "test_player" in connection_manager.active_sse_connections

        # Check that connection metadata includes session_id
        assert connection_id in connection_manager.connection_metadata
        metadata = connection_manager.connection_metadata[connection_id]
        assert metadata.session_id == session_id
        assert metadata.connection_type == "sse"
        assert metadata.player_id == "test_player"

    @pytest.mark.asyncio
    async def test_simultaneous_websocket_and_sse_connections(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test that a player can have both WebSocket and SSE connections simultaneously."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket
        websocket_success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        assert websocket_success is True

        # Connect SSE
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_2")
        assert sse_connection_id is not None

        # Verify both connections exist
        assert connection_manager.has_websocket_connection("test_player") is True
        assert connection_manager.has_sse_connection("test_player") is True

        connection_counts = connection_manager.get_connection_count("test_player")
        assert connection_counts["websocket"] == 1
        assert connection_counts["sse"] == 1
        assert connection_counts["total"] == 2

    @pytest.mark.asyncio
    async def test_multiple_websocket_connections(self, connection_manager, mock_player, mock_persistence):
        """Test that a player can have multiple WebSocket connections."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Set up mock room
        self._setup_mock_room(mock_persistence)

        # Create multiple mock websockets
        websocket1 = self._create_mock_websocket()
        websocket2 = self._create_mock_websocket()

        # Connect first WebSocket
        success1 = await connection_manager.connect_websocket(websocket1, "test_player", "session_1")
        assert success1 is True

        # Connect second WebSocket
        success2 = await connection_manager.connect_websocket(websocket2, "test_player", "session_2")
        assert success2 is True

        # Verify both connections exist
        connection_counts = connection_manager.get_connection_count("test_player")
        assert connection_counts["websocket"] == 2
        assert connection_counts["sse"] == 0
        assert connection_counts["total"] == 2

    @pytest.mark.asyncio
    async def test_multiple_sse_connections(self, connection_manager):
        """Test that a player can have multiple SSE connections."""
        # Connect first SSE
        connection_id1 = await connection_manager.connect_sse("test_player", "session_1")
        assert connection_id1 is not None

        # Connect second SSE
        connection_id2 = await connection_manager.connect_sse("test_player", "session_2")
        assert connection_id2 is not None
        assert connection_id1 != connection_id2

        # Verify both connections exist
        connection_counts = connection_manager.get_connection_count("test_player")
        assert connection_counts["websocket"] == 0
        assert connection_counts["sse"] == 2
        assert connection_counts["total"] == 2

    @pytest.mark.asyncio
    async def test_handle_new_game_session(self, connection_manager, mock_websocket, mock_player, mock_persistence):
        """Test handling of new game session disconnects existing connections."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Set up existing connections
        websocket1 = Mock(spec=WebSocket)
        websocket1.accept = AsyncMock()
        websocket1.close = AsyncMock()
        websocket1.ping = AsyncMock()

        # Connect WebSocket
        await connection_manager.connect_websocket(websocket1, "test_player", "old_session")

        # Connect SSE
        await connection_manager.connect_sse("test_player", "old_session")

        # Verify connections exist
        assert connection_manager.has_websocket_connection("test_player") is True
        assert connection_manager.has_sse_connection("test_player") is True

        # Handle new game session
        await connection_manager.handle_new_game_session("test_player", "new_session")

        # Verify all connections are disconnected
        assert connection_manager.has_websocket_connection("test_player") is False
        assert connection_manager.has_sse_connection("test_player") is False

        connection_counts = connection_manager.get_connection_count("test_player")
        assert connection_counts["total"] == 0

    @pytest.mark.asyncio
    async def test_disconnect_connection_by_id_websocket(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test disconnecting a specific WebSocket connection by ID."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        assert success is True

        # Get the connection ID
        connection_id = connection_manager.get_player_websocket_connection_id("test_player")
        assert connection_id is not None

        # Disconnect the specific connection
        result = await connection_manager.disconnect_connection_by_id(connection_id)
        assert result is True

        # Verify connection is disconnected
        assert connection_manager.has_websocket_connection("test_player") is False
        assert connection_id not in connection_manager.connection_metadata

    @pytest.mark.asyncio
    async def test_disconnect_connection_by_id_sse(self, connection_manager):
        """Test disconnecting a specific SSE connection by ID."""
        # Connect SSE
        connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert connection_id is not None

        # Disconnect the specific connection
        result = await connection_manager.disconnect_connection_by_id(connection_id)
        assert result is True

        # Verify connection is disconnected
        assert connection_manager.has_sse_connection("test_player") is False
        assert connection_id not in connection_manager.connection_metadata

    @pytest.mark.asyncio
    async def test_disconnect_websocket_connection(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test disconnecting a specific WebSocket connection for a player."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        assert success is True

        # Get the connection ID
        connection_id = connection_manager.get_player_websocket_connection_id("test_player")
        assert connection_id is not None

        # Disconnect the specific WebSocket connection
        result = await connection_manager.disconnect_websocket_connection("test_player", connection_id)
        assert result is True

        # Verify connection is disconnected
        assert connection_manager.has_websocket_connection("test_player") is False
        assert connection_id not in connection_manager.connection_metadata

    @pytest.mark.asyncio
    async def test_disconnect_sse_connection(self, connection_manager):
        """Test disconnecting a specific SSE connection for a player."""
        # Connect SSE
        connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert connection_id is not None

        # Disconnect the specific SSE connection
        result = connection_manager.disconnect_sse_connection("test_player", connection_id)
        assert result is True

        # Verify connection is disconnected
        assert connection_manager.has_sse_connection("test_player") is False
        assert connection_id not in connection_manager.connection_metadata

    @pytest.mark.asyncio
    async def test_partial_connection_disconnection(self, connection_manager, mock_player, mock_persistence):
        """Test partial disconnection - disconnect one of multiple connections."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Set up mock room
        self._setup_mock_room(mock_persistence)

        # Create multiple mock websockets
        websocket1 = self._create_mock_websocket()
        websocket2 = self._create_mock_websocket()

        # Connect two WebSockets
        success1 = await connection_manager.connect_websocket(websocket1, "test_player", "session_1")
        success2 = await connection_manager.connect_websocket(websocket2, "test_player", "session_2")
        assert success1 is True
        assert success2 is True

        # Verify both connections exist
        connection_counts = connection_manager.get_connection_count("test_player")
        assert connection_counts["websocket"] == 2

        # Get the first connection ID
        first_connection_id = connection_manager.get_player_websocket_connection_id("test_player")
        assert first_connection_id is not None

        # Disconnect only the first connection
        result = await connection_manager.disconnect_websocket_connection("test_player", first_connection_id)
        assert result is True

        # Verify only one connection remains
        connection_counts = connection_manager.get_connection_count("test_player")
        assert connection_counts["websocket"] == 1
        assert connection_manager.has_websocket_connection("test_player") is True

    @pytest.mark.asyncio
    async def test_complete_connection_disconnection(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test complete disconnection - disconnect all connections for a player."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket
        websocket_success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        assert websocket_success is True

        # Connect SSE
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_2")
        assert sse_connection_id is not None

        # Verify both connections exist
        connection_counts = connection_manager.get_connection_count("test_player")
        assert connection_counts["total"] == 2

        # Disconnect all connections
        await connection_manager.force_disconnect_player("test_player")

        # Verify all connections are disconnected
        connection_counts = connection_manager.get_connection_count("test_player")
        assert connection_counts["total"] == 0
        assert connection_manager.has_websocket_connection("test_player") is False
        assert connection_manager.has_sse_connection("test_player") is False

    @pytest.mark.asyncio
    async def test_connection_cleanup_after_disconnection(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test that connection cleanup is performed after disconnection."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        assert success is True

        # Get the connection ID
        connection_id = connection_manager.get_player_websocket_connection_id("test_player")
        assert connection_id is not None

        # Verify connection metadata exists
        assert connection_id in connection_manager.connection_metadata

        # Disconnect the connection
        result = await connection_manager.disconnect_connection_by_id(connection_id)
        assert result is True

        # Verify cleanup was performed
        assert connection_id not in connection_manager.connection_metadata
        assert connection_id not in connection_manager.active_websockets
        assert not connection_manager.has_websocket_connection("test_player")

    @pytest.mark.asyncio
    async def test_force_disconnect_with_multiple_connections(self, connection_manager, mock_player, mock_persistence):
        """Test force disconnect with multiple connections."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Set up mock room
        self._setup_mock_room(mock_persistence)

        # Create multiple mock websockets
        websocket1 = self._create_mock_websocket()
        websocket2 = self._create_mock_websocket()

        # Connect multiple WebSockets
        success1 = await connection_manager.connect_websocket(websocket1, "test_player", "session_1")
        success2 = await connection_manager.connect_websocket(websocket2, "test_player", "session_2")
        assert success1 is True
        assert success2 is True

        # Connect SSE
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_3")
        assert sse_connection_id is not None

        # Verify all connections exist
        connection_counts = connection_manager.get_connection_count("test_player")
        assert connection_counts["total"] == 3

        # Force disconnect all connections
        await connection_manager.force_disconnect_player("test_player")

        # Verify all connections are disconnected
        connection_counts = connection_manager.get_connection_count("test_player")
        assert connection_counts["total"] == 0
        assert connection_manager.has_websocket_connection("test_player") is False
        assert connection_manager.has_sse_connection("test_player") is False

    @pytest.mark.asyncio
    async def test_disconnect_nonexistent_connection(self, connection_manager):
        """Test disconnecting a connection that doesn't exist."""
        # Try to disconnect a nonexistent connection
        result = await connection_manager.disconnect_connection_by_id("nonexistent_connection_id")
        assert result is False

    @pytest.mark.asyncio
    async def test_disconnect_connection_wrong_player(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test disconnecting a connection with wrong player ID."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        assert success is True

        # Get the connection ID
        connection_id = connection_manager.get_player_websocket_connection_id("test_player")
        assert connection_id is not None

        # Try to disconnect with wrong player ID
        result = await connection_manager.disconnect_websocket_connection("wrong_player", connection_id)
        assert result is False

        # Verify connection still exists
        assert connection_manager.has_websocket_connection("test_player") is True

    @pytest.mark.asyncio
    async def test_send_personal_message_multiple_connections(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test sending personal message to multiple connections."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Set up mock room using helper method
        self._setup_mock_room(mock_persistence, "test_room_001")

        # Create multiple mock websockets using helper method
        websocket1 = self._create_mock_websocket()
        websocket2 = self._create_mock_websocket()

        # Connect two WebSockets
        success1 = await connection_manager.connect_websocket(websocket1, "test_player", "session_1")
        success2 = await connection_manager.connect_websocket(websocket2, "test_player", "session_2")
        assert success1 is True
        assert success2 is True

        # Connect SSE
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_3")
        assert sse_connection_id is not None

        # Send message
        test_event = {"type": "test_message", "content": "Hello World"}
        delivery_status = await connection_manager.send_personal_message("test_player", test_event)

        # Verify delivery status
        assert delivery_status["success"] is True
        assert delivery_status["websocket_delivered"] == 2
        assert delivery_status["websocket_failed"] == 0
        assert delivery_status["sse_delivered"] is True
        assert delivery_status["total_connections"] == 3
        assert delivery_status["active_connections"] == 3

        # Verify WebSocket messages were sent (at least once for our test message)
        assert websocket1.send_json.call_count >= 1
        assert websocket2.send_json.call_count >= 1

        # Verify our test message was sent to both WebSockets
        test_message_calls = [
            call for call in websocket1.send_json.call_args_list if call[0][0].get("type") == "test_message"
        ]
        assert len(test_message_calls) == 1

        test_message_calls = [
            call for call in websocket2.send_json.call_args_list if call[0][0].get("type") == "test_message"
        ]
        assert len(test_message_calls) == 1

    @pytest.mark.asyncio
    async def test_send_personal_message_websocket_only(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test sending personal message to WebSocket connections only."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        assert success is True

        # Send message
        test_event = {"type": "test_message", "content": "Hello World"}
        delivery_status = await connection_manager.send_personal_message("test_player", test_event)

        # Verify delivery status
        assert delivery_status["success"] is True
        assert delivery_status["websocket_delivered"] == 1
        assert delivery_status["websocket_failed"] == 0
        assert delivery_status["sse_delivered"] is False
        assert delivery_status["total_connections"] == 1
        assert delivery_status["active_connections"] == 1

    @pytest.mark.asyncio
    async def test_send_personal_message_sse_only(self, connection_manager):
        """Test sending personal message to SSE connections only."""
        # Connect SSE
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert sse_connection_id is not None

        # Send message
        test_event = {"type": "test_message", "content": "Hello World"}
        delivery_status = await connection_manager.send_personal_message("test_player", test_event)

        # Verify delivery status
        assert delivery_status["success"] is True
        assert delivery_status["websocket_delivered"] == 0
        assert delivery_status["websocket_failed"] == 0
        assert delivery_status["sse_delivered"] is True
        assert delivery_status["total_connections"] == 1
        assert delivery_status["active_connections"] == 1

    @pytest.mark.asyncio
    async def test_send_personal_message_mixed_connections(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test sending personal message to mixed WebSocket and SSE connections."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket
        websocket_success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        assert websocket_success is True

        # Connect SSE
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_2")
        assert sse_connection_id is not None

        # Send message
        test_event = {"type": "test_message", "content": "Hello World"}
        delivery_status = await connection_manager.send_personal_message("test_player", test_event)

        # Verify delivery status
        assert delivery_status["success"] is True
        assert delivery_status["websocket_delivered"] == 1
        assert delivery_status["websocket_failed"] == 0
        assert delivery_status["sse_delivered"] is True
        assert delivery_status["total_connections"] == 2
        assert delivery_status["active_connections"] == 2

    @pytest.mark.asyncio
    async def test_send_personal_message_failure_handling(self, connection_manager, mock_player, mock_persistence):
        """Test message delivery failure handling."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Set up mock room using helper method
        self._setup_mock_room(mock_persistence, "test_room_001")

        # Create a mock websocket that will fail using helper method
        websocket = self._create_mock_websocket()
        websocket.send_json = AsyncMock(side_effect=Exception("Connection closed"))

        # Connect WebSocket
        success = await connection_manager.connect_websocket(websocket, "test_player", "session_1")
        assert success is True

        # Send message
        test_event = {"type": "test_message", "content": "Hello World"}
        delivery_status = await connection_manager.send_personal_message("test_player", test_event)

        # Verify delivery status shows message was queued (connection was cleaned up during initial game state)
        assert delivery_status["success"] is True  # Message was queued for later delivery
        assert delivery_status["websocket_delivered"] == 0
        assert delivery_status["websocket_failed"] == 0  # Connection already cleaned up
        assert delivery_status["sse_delivered"] is True  # Message was queued
        assert delivery_status["total_connections"] == 0  # No connections left
        assert delivery_status["active_connections"] == 0

    @pytest.mark.asyncio
    async def test_send_personal_message_dead_connection_cleanup(
        self, connection_manager, mock_player, mock_persistence
    ):
        """Test dead connection cleanup during message delivery."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Set up mock room using helper method
        self._setup_mock_room(mock_persistence, "test_room_001")

        # Create a mock websocket that will fail using helper method
        websocket = self._create_mock_websocket()
        websocket.send_json = AsyncMock(side_effect=Exception("Connection closed"))

        # Connect WebSocket
        success = await connection_manager.connect_websocket(websocket, "test_player", "session_1")
        assert success is True

        # Connection was already cleaned up during initial game state message
        # Verify connection no longer exists
        assert connection_manager.has_websocket_connection("test_player") is False

        # Send message (no connections left to clean up)
        test_event = {"type": "test_message", "content": "Hello World"}
        delivery_status = await connection_manager.send_personal_message("test_player", test_event)

        # Verify no connections and no failures (already cleaned up)
        assert connection_manager.has_websocket_connection("test_player") is False
        assert delivery_status["websocket_failed"] == 0

    def test_get_message_delivery_stats(self, connection_manager):
        """Test getting message delivery statistics."""
        # Initially no connections
        stats = connection_manager.get_message_delivery_stats("test_player")
        assert stats["player_id"] == "test_player"
        assert stats["websocket_connections"] == 0
        assert stats["sse_connections"] == 0
        assert stats["total_connections"] == 0
        assert stats["pending_messages"] == 0
        assert stats["has_active_connections"] is False

        # Add some connections
        connection_manager.player_websockets["test_player"] = ["ws1", "ws2"]
        connection_manager.active_sse_connections["test_player"] = ["sse1"]
        connection_manager.message_queue.pending_messages["test_player"] = ["msg1", "msg2"]

        stats = connection_manager.get_message_delivery_stats("test_player")
        assert stats["websocket_connections"] == 2
        assert stats["sse_connections"] == 1
        assert stats["total_connections"] == 3
        assert stats["pending_messages"] == 2
        assert stats["has_active_connections"] is True

    @pytest.mark.asyncio
    async def test_check_connection_health_healthy(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test checking connection health for healthy connections."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        _mock_room = self._setup_mock_room(mock_persistence, "test_room_001")

        # Ensure mock WebSocket has a working ping method
        mock_websocket.ping = AsyncMock()

        # Connect WebSocket
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        assert success is True

        # Connect SSE
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_2")
        assert sse_connection_id is not None

        # Check health
        health_status = await connection_manager.check_connection_health("test_player")

        # Verify health status
        assert health_status["player_id"] == "test_player"
        assert health_status["websocket_healthy"] == 1
        assert health_status["websocket_unhealthy"] == 0
        assert health_status["sse_healthy"] == 1
        assert health_status["overall_health"] == "healthy"

    @pytest.mark.asyncio
    async def test_check_connection_health_unhealthy(self, connection_manager, mock_player, mock_persistence):
        """Test checking connection health for unhealthy connections."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Create a mock websocket that will fail ping
        websocket = Mock(spec=WebSocket)
        websocket.accept = AsyncMock()
        websocket.close = AsyncMock()
        websocket.ping = AsyncMock(side_effect=Exception("Connection closed"))

        # Connect WebSocket
        success = await connection_manager.connect_websocket(websocket, "test_player", "session_1")
        assert success is True

        # Check health (this should clean up the unhealthy connection)
        health_status = await connection_manager.check_connection_health("test_player")

        # Verify health status
        assert health_status["player_id"] == "test_player"
        assert health_status["websocket_healthy"] == 0
        assert health_status["websocket_unhealthy"] == 1
        assert health_status["sse_healthy"] == 0
        assert health_status["overall_health"] == "unhealthy"

        # Verify connection was cleaned up
        assert connection_manager.has_websocket_connection("test_player") is False

    @pytest.mark.asyncio
    async def test_cleanup_dead_connections_specific_player(self, connection_manager, mock_player, mock_persistence):
        """Test cleaning up dead connections for a specific player."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Create a mock websocket that will fail ping
        websocket = Mock(spec=WebSocket)
        websocket.accept = AsyncMock()
        websocket.close = AsyncMock()
        websocket.ping = AsyncMock(side_effect=Exception("Connection closed"))

        # Connect WebSocket
        success = await connection_manager.connect_websocket(websocket, "test_player", "session_1")
        assert success is True

        # Clean up dead connections
        cleanup_results = await connection_manager.cleanup_dead_connections("test_player")

        # Verify cleanup results
        assert cleanup_results["players_checked"] == 1
        assert cleanup_results["connections_cleaned"] == 1
        assert len(cleanup_results["errors"]) == 0

        # Verify connection was cleaned up
        assert connection_manager.has_websocket_connection("test_player") is False

    @pytest.mark.asyncio
    async def test_cleanup_dead_connections_all_players(self, connection_manager, mock_player, mock_persistence):
        """Test cleaning up dead connections for all players."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Create mock websockets that will fail ping
        websocket1 = Mock(spec=WebSocket)
        websocket1.accept = AsyncMock()
        websocket1.close = AsyncMock()
        websocket1.ping = AsyncMock(side_effect=Exception("Connection closed"))

        websocket2 = Mock(spec=WebSocket)
        websocket2.accept = AsyncMock()
        websocket2.close = AsyncMock()
        websocket2.ping = AsyncMock(side_effect=Exception("Connection closed"))

        # Connect WebSockets for two players
        success1 = await connection_manager.connect_websocket(websocket1, "player1", "session_1")
        success2 = await connection_manager.connect_websocket(websocket2, "player2", "session_2")
        assert success1 is True
        assert success2 is True

        # Clean up dead connections for all players
        cleanup_results = await connection_manager.cleanup_dead_connections()

        # Verify cleanup results
        assert cleanup_results["players_checked"] == 2
        assert cleanup_results["connections_cleaned"] == 2
        assert len(cleanup_results["errors"]) == 0

        # Verify connections were cleaned up
        assert connection_manager.has_websocket_connection("player1") is False
        assert connection_manager.has_websocket_connection("player2") is False

    @pytest.mark.asyncio
    async def test_handle_new_game_session_success(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test successful new game session handling."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        assert success is True

        # Connect SSE
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert sse_connection_id is not None

        # Verify initial session tracking
        assert connection_manager.get_player_session("test_player") == "session_1"
        assert len(connection_manager.get_session_connections("session_1")) == 2

        # Handle new game session
        session_results = await connection_manager.handle_new_game_session("test_player", "session_2")

        # Verify session results
        assert session_results["player_id"] == "test_player"
        assert session_results["new_session_id"] == "session_2"
        assert session_results["previous_session_id"] == "session_1"
        assert session_results["connections_disconnected"] == 2
        assert session_results["websocket_connections"] == 1
        assert session_results["sse_connections"] == 1
        assert session_results["success"] is True
        assert len(session_results["errors"]) == 0

        # Verify session tracking updated
        assert connection_manager.get_player_session("test_player") == "session_2"
        assert len(connection_manager.get_session_connections("session_2")) == 0
        assert "session_1" not in connection_manager.session_connections

        # Verify connections were disconnected
        assert connection_manager.has_websocket_connection("test_player") is False
        assert connection_manager.has_sse_connection("test_player") is False

    @pytest.mark.asyncio
    async def test_handle_new_game_session_no_existing_connections(self, connection_manager):
        """Test new game session handling when player has no existing connections."""
        # Handle new game session for player with no connections
        session_results = await connection_manager.handle_new_game_session("test_player", "session_1")

        # Verify session results
        assert session_results["player_id"] == "test_player"
        assert session_results["new_session_id"] == "session_1"
        assert session_results["previous_session_id"] is None
        assert session_results["connections_disconnected"] == 0
        assert session_results["websocket_connections"] == 0
        assert session_results["sse_connections"] == 0
        assert session_results["success"] is True
        assert len(session_results["errors"]) == 0

        # Verify session tracking
        assert connection_manager.get_player_session("test_player") == "session_1"
        assert len(connection_manager.get_session_connections("session_1")) == 0

    @pytest.mark.asyncio
    async def test_handle_new_game_session_with_errors(self, connection_manager, mock_player, mock_persistence):
        """Test new game session handling with connection errors."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Create a mock websocket that will fail to close
        websocket = Mock(spec=WebSocket)
        websocket.accept = AsyncMock()
        websocket.close = AsyncMock(side_effect=Exception("Connection close failed"))
        websocket.ping = AsyncMock()
        websocket.send_json = AsyncMock()

        # Mock the logger to avoid Unicode encoding issues on Windows during error logging
        with patch("server.realtime.connection_manager.logger"):
            # Connect WebSocket
            success = await connection_manager.connect_websocket(websocket, "test_player", "session_1")
            assert success is True

            # Handle new game session (should handle errors gracefully)
            session_results = await connection_manager.handle_new_game_session("test_player", "session_2")

            # Verify session results show error handling
            assert session_results["player_id"] == "test_player"
            assert session_results["new_session_id"] == "session_2"
            assert session_results["success"] is True  # Should still succeed despite connection errors
            # The connection close error is logged but handled gracefully, not reported in errors list
            assert len(session_results["errors"]) == 0  # Errors are handled internally

            # Verify session tracking still updated
            assert connection_manager.get_player_session("test_player") == "session_2"

    def test_get_player_session(self, connection_manager):
        """Test getting player session."""
        # Initially no session
        assert connection_manager.get_player_session("test_player") is None

        # Set session
        connection_manager.player_sessions["test_player"] = "session_1"
        assert connection_manager.get_player_session("test_player") == "session_1"

    def test_get_session_connections(self, connection_manager):
        """Test getting session connections."""
        # Initially no connections
        assert connection_manager.get_session_connections("session_1") == []

        # Add connections
        connection_manager.session_connections["session_1"] = ["conn1", "conn2", "conn3"]
        connections = connection_manager.get_session_connections("session_1")
        assert len(connections) == 3
        assert "conn1" in connections
        assert "conn2" in connections
        assert "conn3" in connections

    def test_validate_session(self, connection_manager):
        """Test session validation."""
        # Set up session
        connection_manager.player_sessions["test_player"] = "session_1"

        # Valid session
        assert connection_manager.validate_session("test_player", "session_1") is True

        # Invalid session
        assert connection_manager.validate_session("test_player", "session_2") is False

        # Player with no session
        assert connection_manager.validate_session("other_player", "session_1") is False

    def test_get_session_stats(self, connection_manager):
        """Test getting session statistics."""
        # Initially empty
        stats = connection_manager.get_session_stats()
        assert stats["total_sessions"] == 0
        assert stats["total_players_with_sessions"] == 0
        assert stats["sessions_with_connections"] == 0
        assert stats["average_connections_per_session"] == 0

        # Add some sessions and connections
        connection_manager.player_sessions["player1"] = "session_1"
        connection_manager.player_sessions["player2"] = "session_2"
        connection_manager.session_connections["session_1"] = ["conn1", "conn2"]
        connection_manager.session_connections["session_2"] = ["conn3"]
        connection_manager.session_connections["session_3"] = []  # Empty session

        stats = connection_manager.get_session_stats()
        assert stats["total_sessions"] == 3
        assert stats["total_players_with_sessions"] == 2
        assert stats["sessions_with_connections"] == 2
        assert stats["average_connections_per_session"] == 1.0  # (2+1+0)/3

    @pytest.mark.asyncio
    async def test_session_tracking_during_connection(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test that session tracking works during connection establishment."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket with session
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        assert success is True

        # Verify session tracking
        assert connection_manager.get_player_session("test_player") == "session_1"
        session_connections = connection_manager.get_session_connections("session_1")
        assert len(session_connections) == 1

        # Connect SSE with same session
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert sse_connection_id is not None

        # Verify session tracking updated
        assert connection_manager.get_player_session("test_player") == "session_1"
        session_connections = connection_manager.get_session_connections("session_1")
        assert len(session_connections) == 2

        # Connect another WebSocket with different session (should update session tracking)
        websocket2 = Mock(spec=WebSocket)
        websocket2.accept = AsyncMock()
        websocket2.close = AsyncMock()
        websocket2.ping = AsyncMock()
        websocket2.send_json = AsyncMock()

        success2 = await connection_manager.connect_websocket(websocket2, "test_player", "session_2")
        assert success2 is True

        # Verify session tracking remains with original session (not automatically updated)
        assert connection_manager.get_player_session("test_player") == "session_1"
        session_connections = connection_manager.get_session_connections("session_2")
        assert len(session_connections) == 1

        # Both sessions should exist (connections weren't disconnected)
        assert "session_1" in connection_manager.session_connections
        assert "session_2" in connection_manager.session_connections
        assert len(connection_manager.get_session_connections("session_1")) == 2

        # Now explicitly handle new game session to clean up old connections
        session_results = await connection_manager.handle_new_game_session("test_player", "session_2")
        assert session_results["success"] is True

        # Now old session should be cleaned up and player session updated
        assert "session_1" not in connection_manager.session_connections
        assert connection_manager.get_player_session("test_player") == "session_2"

    @pytest.mark.asyncio
    async def test_detect_and_handle_error_state_fatal_error(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test fatal error handling that terminates all connections."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket and SSE
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert success is True
        assert sse_connection_id is not None

        # Verify initial connections
        assert connection_manager.has_websocket_connection("test_player") is True
        assert connection_manager.has_sse_connection("test_player") is True

        # Handle fatal error
        error_results = await connection_manager.detect_and_handle_error_state(
            "test_player", "CRITICAL_WEBSOCKET_ERROR", "Connection lost unexpectedly"
        )

        # Verify error handling results
        assert error_results["player_id"] == "test_player"
        assert error_results["error_type"] == "CRITICAL_WEBSOCKET_ERROR"
        assert error_results["fatal_error"] is True
        assert error_results["success"] is True
        assert error_results["connections_terminated"] == 2
        assert error_results["connections_kept"] == 0
        assert len(error_results["errors"]) == 0

        # Verify connections were terminated
        assert connection_manager.has_websocket_connection("test_player") is False
        assert connection_manager.has_sse_connection("test_player") is False

    @pytest.mark.asyncio
    async def test_detect_and_handle_error_state_connection_specific(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test connection-specific error handling."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket and SSE
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert success is True
        assert sse_connection_id is not None

        # Get the WebSocket connection ID
        websocket_connection_id = connection_manager.get_player_websocket_connection_id("test_player")

        # Handle connection-specific error
        error_results = await connection_manager.detect_and_handle_error_state(
            "test_player", "WEBSOCKET_ERROR", "Invalid message format", websocket_connection_id
        )

        # Verify error handling results
        assert error_results["player_id"] == "test_player"
        assert error_results["error_type"] == "WEBSOCKET_ERROR"
        assert error_results["connection_id"] == websocket_connection_id
        assert error_results["fatal_error"] is False
        assert error_results["success"] is True
        assert error_results["connections_terminated"] == 1
        assert error_results["connections_kept"] == 1
        assert len(error_results["errors"]) == 0

        # Verify only WebSocket was terminated, SSE remains
        assert connection_manager.has_websocket_connection("test_player") is False
        assert connection_manager.has_sse_connection("test_player") is True

    @pytest.mark.asyncio
    async def test_detect_and_handle_error_state_non_critical(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test non-critical error handling that keeps connections alive."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket and SSE
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert success is True
        assert sse_connection_id is not None

        # Handle non-critical error
        error_results = await connection_manager.detect_and_handle_error_state(
            "test_player", "MESSAGE_RATE_LIMIT", "Too many messages per second"
        )

        # Verify error handling results
        assert error_results["player_id"] == "test_player"
        assert error_results["error_type"] == "MESSAGE_RATE_LIMIT"
        assert error_results["fatal_error"] is False
        assert error_results["success"] is True
        assert error_results["connections_terminated"] == 0
        assert error_results["connections_kept"] == 2
        assert len(error_results["errors"]) == 0

        # Verify connections remain active
        assert connection_manager.has_websocket_connection("test_player") is True
        assert connection_manager.has_sse_connection("test_player") is True

    @pytest.mark.asyncio
    async def test_handle_websocket_error_critical(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test critical WebSocket error handling."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket and SSE
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert success is True
        assert sse_connection_id is not None

        # Get the WebSocket connection ID
        websocket_connection_id = connection_manager.get_player_websocket_connection_id("test_player")

        # Handle critical WebSocket error
        error_results = await connection_manager.handle_websocket_error(
            "test_player", websocket_connection_id, "CONNECTION_CLOSED_UNEXPECTEDLY", "WebSocket connection lost"
        )

        # Verify error handling results
        assert error_results["player_id"] == "test_player"
        assert error_results["error_type"] == "CRITICAL_WEBSOCKET_ERROR"
        assert error_results["fatal_error"] is True
        assert error_results["success"] is True
        assert error_results["connections_terminated"] == 2  # All connections terminated for critical error
        assert error_results["connections_kept"] == 0

        # Verify all connections were terminated
        assert connection_manager.has_websocket_connection("test_player") is False
        assert connection_manager.has_sse_connection("test_player") is False

    @pytest.mark.asyncio
    async def test_handle_sse_error_critical(self, connection_manager, mock_websocket, mock_player, mock_persistence):
        """Test critical SSE error handling."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket and SSE
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert success is True
        assert sse_connection_id is not None

        # Handle critical SSE error
        error_results = await connection_manager.handle_sse_error(
            "test_player", sse_connection_id, "STREAM_INTERRUPTED", "SSE stream interrupted"
        )

        # Verify error handling results
        assert error_results["player_id"] == "test_player"
        assert error_results["error_type"] == "CRITICAL_SSE_ERROR"
        assert error_results["fatal_error"] is True
        assert error_results["success"] is True
        assert error_results["connections_terminated"] == 2  # All connections terminated for critical error
        assert error_results["connections_kept"] == 0

        # Verify all connections were terminated
        assert connection_manager.has_websocket_connection("test_player") is False
        assert connection_manager.has_sse_connection("test_player") is False

    @pytest.mark.asyncio
    async def test_handle_authentication_error(self, connection_manager, mock_websocket, mock_player, mock_persistence):
        """Test authentication error handling."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket and SSE
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert success is True
        assert sse_connection_id is not None

        # Handle authentication error
        error_results = await connection_manager.handle_authentication_error(
            "test_player", "INVALID_TOKEN", "Authentication token expired"
        )

        # Verify error handling results
        assert error_results["player_id"] == "test_player"
        assert error_results["error_type"] == "AUTHENTICATION_FAILURE"
        assert error_results["fatal_error"] is True
        assert error_results["success"] is True
        assert error_results["connections_terminated"] == 2
        assert error_results["connections_kept"] == 0

        # Verify all connections were terminated
        assert connection_manager.has_websocket_connection("test_player") is False
        assert connection_manager.has_sse_connection("test_player") is False

    @pytest.mark.asyncio
    async def test_handle_security_violation(self, connection_manager, mock_websocket, mock_player, mock_persistence):
        """Test security violation handling."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket and SSE
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert success is True
        assert sse_connection_id is not None

        # Handle security violation
        error_results = await connection_manager.handle_security_violation(
            "test_player", "UNAUTHORIZED_ACCESS", "Attempted to access restricted resource"
        )

        # Verify error handling results
        assert error_results["player_id"] == "test_player"
        assert error_results["error_type"] == "SECURITY_VIOLATION"
        assert error_results["fatal_error"] is True
        assert error_results["success"] is True
        assert error_results["connections_terminated"] == 2
        assert error_results["connections_kept"] == 0

        # Verify all connections were terminated
        assert connection_manager.has_websocket_connection("test_player") is False
        assert connection_manager.has_sse_connection("test_player") is False

    @pytest.mark.asyncio
    async def test_recover_from_error_full(self, connection_manager, mock_websocket, mock_player, mock_persistence):
        """Test full error recovery."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket and SSE
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert success is True
        assert sse_connection_id is not None

        # Attempt full recovery
        recovery_results = await connection_manager.recover_from_error("test_player", "FULL")

        # Verify recovery results
        assert recovery_results["player_id"] == "test_player"
        assert recovery_results["recovery_type"] == "FULL"
        assert recovery_results["success"] is True
        assert recovery_results["sessions_cleared"] == 1
        assert len(recovery_results["errors"]) == 0

        # Verify session was cleared
        assert connection_manager.get_player_session("test_player") is None

    @pytest.mark.asyncio
    async def test_recover_from_error_connections_only(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test connections-only error recovery."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect WebSocket and SSE
        success = await connection_manager.connect_websocket(mock_websocket, "test_player", "session_1")
        sse_connection_id = await connection_manager.connect_sse("test_player", "session_1")
        assert success is True
        assert sse_connection_id is not None

        # Attempt connections-only recovery
        recovery_results = await connection_manager.recover_from_error("test_player", "CONNECTIONS_ONLY")

        # Verify recovery results
        assert recovery_results["player_id"] == "test_player"
        assert recovery_results["recovery_type"] == "CONNECTIONS_ONLY"
        assert recovery_results["success"] is True
        assert recovery_results["sessions_cleared"] == 0  # Session should not be cleared
        assert len(recovery_results["errors"]) == 0

        # Verify session remains
        assert connection_manager.get_player_session("test_player") == "session_1"

    def test_get_error_statistics(self, connection_manager):
        """Test getting error statistics."""
        # Mock the config to avoid Pydantic validation errors
        from server.config.models import LoggingConfig

        mock_logging_config = LoggingConfig(
            environment="unit_test", log_base="logs", max_bytes=10485760, backup_count=3
        )

        with patch("server.config.get_config") as mock_get_config:
            mock_config = Mock()
            mock_config.logging = mock_logging_config
            mock_get_config.return_value = mock_config

            # Initially empty
            stats = connection_manager.get_error_statistics()
            assert stats["total_players"] == 0
            assert stats["total_connections"] == 0
            assert stats["active_sessions"] == 0
            assert stats["players_with_sessions"] == 0
            # The error log path should be resolved based on test configuration
            # Test config uses environment: unit_test and log_base: logs
            error_log_path = stats["error_log_path"]
            assert "logs" in error_log_path
            assert "unit_test" in error_log_path
            assert error_log_path.endswith("connection_errors.log")

            # Add some connections and sessions
            connection_manager.player_sessions["player1"] = "session_1"
            connection_manager.player_sessions["player2"] = "session_2"
            connection_manager.session_connections["session_1"] = ["conn1", "conn2"]
            connection_manager.session_connections["session_2"] = ["conn3"]
            connection_manager.player_websockets["player1"] = ["conn1", "conn2"]
            connection_manager.active_sse_connections["player2"] = ["conn3"]
            connection_manager.online_players["player1"] = True
            connection_manager.online_players["player2"] = True

            stats = connection_manager.get_error_statistics()
            assert stats["total_players"] == 2
            assert stats["total_connections"] == 3
            assert stats["active_sessions"] == 2
            assert stats["players_with_sessions"] == 2

    @pytest.mark.asyncio
    async def test_track_player_connected_new_connection(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test tracking a new player connection."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Track new connection
        await connection_manager._track_player_connected("test_player", mock_player, "websocket")

        # Verify player is tracked as online
        assert "test_player" in connection_manager.online_players
        player_info = connection_manager.online_players["test_player"]
        assert player_info["connection_types"] == {"websocket"}
        assert player_info["total_connections"] == 0  # No actual connections yet, just tracking

    @pytest.mark.asyncio
    async def test_track_player_connected_additional_connection(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test tracking an additional connection for an existing player."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # First connection
        await connection_manager._track_player_connected("test_player", mock_player, "websocket")

        # Add actual connections to simulate real connection
        connection_manager.player_websockets["test_player"] = ["conn1"]
        connection_manager.active_sse_connections["test_player"] = ["conn2"]

        # Second connection
        await connection_manager._track_player_connected("test_player", mock_player, "sse")

        # Verify player info is updated
        player_info = connection_manager.online_players["test_player"]
        assert player_info["connection_types"] == {"websocket", "sse"}
        assert player_info["total_connections"] == 2

    @pytest.mark.asyncio
    async def test_track_player_connected_broadcasts_player_entered_event(
        self, connection_manager, mock_player, mock_persistence
    ):
        """Ensure new connections broadcast a player_entered_game event to room occupants."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player
        mock_persistence.save_player = Mock()

        # Prepare mock room returned by the persistence layer
        mock_room = Mock()
        mock_room.id = mock_player.current_room_id
        mock_persistence.get_room.return_value = mock_room

        # Replace collaborators with lightweight mocks for this test
        connection_manager.room_manager = Mock()
        connection_manager.room_manager.add_room_occupant = Mock()
        connection_manager.room_manager.reconcile_room_presence = Mock()
        connection_manager.message_queue = Mock()
        connection_manager.message_queue.remove_player_messages = Mock()

        connection_manager._send_initial_game_state = AsyncMock()
        connection_manager.broadcast_to_room = AsyncMock()

        # Track the initial (new) connection
        await connection_manager._track_player_connected(mock_player.player_id, mock_player, "sse")

        # The room should receive a player_entered_game event excluding the connecting player
        connection_manager.broadcast_to_room.assert_awaited_once()
        broadcast_args = connection_manager.broadcast_to_room.await_args
        assert broadcast_args.args[0] == mock_room.id
        event_payload = broadcast_args.args[1]
        assert event_payload["event_type"] == "player_entered_game"
        assert event_payload["data"]["player_id"] == mock_player.player_id
        assert event_payload["data"]["player_name"] == mock_player.name
        assert broadcast_args.kwargs["exclude_player"] == mock_player.player_id
        mock_room.player_entered.assert_called_once_with(mock_player.player_id)

        # Additional connections should not re-broadcast the entry event
        connection_manager.broadcast_to_room.reset_mock()
        await connection_manager._track_player_connected(mock_player.player_id, mock_player, "websocket")
        connection_manager.broadcast_to_room.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_track_player_disconnected_with_remaining_connections(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test tracking disconnection when player has remaining connections."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Set up player with multiple connections
        connection_manager.player_websockets["test_player"] = ["conn1", "conn2"]
        connection_manager.active_sse_connections["test_player"] = ["conn3"]
        connection_manager.online_players["test_player"] = {
            "player_id": "test_player",
            "player_name": "Test Player",
            "connection_types": {"websocket", "sse"},
            "total_connections": 3,
        }

        # Disconnect one connection type
        await connection_manager._track_player_disconnected("test_player", "websocket")

        # Verify player is still online (not fully disconnected)
        assert "test_player" in connection_manager.online_players

    @pytest.mark.asyncio
    async def test_track_player_disconnected_no_remaining_connections(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test tracking disconnection when player has no remaining connections."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Set up player with one connection
        connection_manager.player_websockets["test_player"] = ["conn1"]
        connection_manager.online_players["test_player"] = {
            "player_id": "test_player",
            "player_name": "Test Player",
            "connection_types": {"websocket"},
            "total_connections": 1,
        }

        # Remove the connection
        del connection_manager.player_websockets["test_player"]

        # Disconnect
        await connection_manager._track_player_disconnected("test_player", "websocket")

        # Verify player is fully disconnected
        assert "test_player" not in connection_manager.online_players

    def test_get_player_presence_info_online(self, connection_manager):
        """Test getting presence info for an online player."""
        # Set up player with connections
        connection_manager.player_websockets["test_player"] = ["conn1", "conn2"]
        connection_manager.active_sse_connections["test_player"] = ["conn3"]
        connection_manager.online_players["test_player"] = {
            "player_id": "test_player",
            "player_name": "Test Player",
            "connection_types": {"websocket", "sse"},
            "total_connections": 3,
            "connected_at": 1234567890,
            "current_room_id": "room_001",
            "level": 5,
        }
        connection_manager.last_seen["test_player"] = 1234567891

        # Get presence info
        presence_info = connection_manager.get_player_presence_info("test_player")

        # Verify presence info
        assert presence_info["player_id"] == "test_player"
        assert presence_info["is_online"] is True
        assert set(presence_info["connection_types"]) == {"websocket", "sse"}
        assert presence_info["total_connections"] == 3
        assert presence_info["websocket_connections"] == 2
        assert presence_info["sse_connections"] == 1
        assert presence_info["connected_at"] == 1234567890
        assert presence_info["last_seen"] == 1234567891
        assert presence_info["player_name"] == "Test Player"
        assert presence_info["current_room_id"] == "room_001"
        assert presence_info["level"] == 5

    def test_get_player_presence_info_offline(self, connection_manager):
        """Test getting presence info for an offline player."""
        # Get presence info for non-existent player
        presence_info = connection_manager.get_player_presence_info("nonexistent_player")

        # Verify presence info
        assert presence_info["player_id"] == "nonexistent_player"
        assert presence_info["is_online"] is False
        assert presence_info["connection_types"] == []
        assert presence_info["total_connections"] == 0
        assert presence_info["websocket_connections"] == 0
        assert presence_info["sse_connections"] == 0
        assert presence_info["connected_at"] is None
        assert presence_info["last_seen"] is None

    def test_validate_player_presence_consistent(self, connection_manager):
        """Test presence validation for a consistent player."""
        # Set up consistent player
        connection_manager.player_websockets["test_player"] = ["conn1"]
        connection_manager.active_sse_connections["test_player"] = ["conn2"]
        connection_manager.online_players["test_player"] = {
            "player_id": "test_player",
            "connection_types": {"websocket", "sse"},
            "total_connections": 2,
        }

        # Validate presence
        validation_results = connection_manager.validate_player_presence("test_player")

        # Verify validation results
        assert validation_results["player_id"] == "test_player"
        assert validation_results["is_consistent"] is True
        assert len(validation_results["issues_found"]) == 0
        assert len(validation_results["actions_taken"]) == 0

    def test_validate_player_presence_inconsistent_online_no_connections(self, connection_manager):
        """Test presence validation for inconsistent player (online but no connections)."""
        # Set up inconsistent player
        connection_manager.online_players["test_player"] = {
            "player_id": "test_player",
            "connection_types": {"websocket"},
            "total_connections": 1,
        }

        # Validate presence
        validation_results = connection_manager.validate_player_presence("test_player")

        # Verify validation results
        assert validation_results["player_id"] == "test_player"
        assert validation_results["is_consistent"] is False
        assert "Player marked as online but has no connections" in validation_results["issues_found"]
        assert "Removed from online_players" in validation_results["actions_taken"]

        # Verify player was removed
        assert "test_player" not in connection_manager.online_players

    def test_validate_player_presence_connection_count_mismatch(self, connection_manager):
        """Test presence validation for connection count mismatch."""
        # Set up player with mismatched connection count
        connection_manager.player_websockets["test_player"] = ["conn1", "conn2"]
        connection_manager.active_sse_connections["test_player"] = ["conn3"]
        connection_manager.online_players["test_player"] = {
            "player_id": "test_player",
            "connection_types": {"websocket", "sse"},
            "total_connections": 1,  # Wrong count
        }

        # Validate presence
        validation_results = connection_manager.validate_player_presence("test_player")

        # Verify validation results
        assert validation_results["player_id"] == "test_player"
        assert validation_results["is_consistent"] is False
        assert "Connection count mismatch: recorded=1, actual=3" in validation_results["issues_found"]
        assert "Updated connection count" in validation_results["actions_taken"]

        # Verify connection count was updated
        assert connection_manager.online_players["test_player"]["total_connections"] == 3

    def test_get_presence_statistics(self, connection_manager):
        """Test getting presence statistics."""
        # Initially empty
        stats = connection_manager.get_presence_statistics()
        assert stats["total_online_players"] == 0
        assert stats["total_connections"] == 0
        assert stats["websocket_connections"] == 0
        assert stats["sse_connections"] == 0
        assert stats["connection_distribution"]["websocket_only"] == 0
        assert stats["connection_distribution"]["sse_only"] == 0
        assert stats["connection_distribution"]["dual_connection"] == 0
        assert stats["average_connections_per_player"] == 0

        # Add some players with different connection types
        # Player 1: WebSocket only
        connection_manager.player_websockets["player1"] = ["conn1"]
        connection_manager.online_players["player1"] = {"connection_types": {"websocket"}, "total_connections": 1}

        # Player 2: SSE only
        connection_manager.active_sse_connections["player2"] = ["conn2"]
        connection_manager.online_players["player2"] = {"connection_types": {"sse"}, "total_connections": 1}

        # Player 3: Dual connection
        connection_manager.player_websockets["player3"] = ["conn3"]
        connection_manager.active_sse_connections["player3"] = ["conn4"]
        connection_manager.online_players["player3"] = {
            "connection_types": {"websocket", "sse"},
            "total_connections": 2,
        }

        # Get statistics
        stats = connection_manager.get_presence_statistics()
        assert stats["total_online_players"] == 3
        assert stats["total_connections"] == 4
        assert stats["websocket_connections"] == 2
        assert stats["sse_connections"] == 2
        assert stats["connection_distribution"]["websocket_only"] == 1
        assert stats["connection_distribution"]["sse_only"] == 1
        assert stats["connection_distribution"]["dual_connection"] == 1
        assert stats["average_connections_per_player"] == 4 / 3

    @pytest.mark.asyncio
    async def test_broadcast_to_room_multiple_connections(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test room broadcasting with multiple connections per player."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        _mock_room = self._setup_mock_room(mock_persistence, "test_room_001")

        # Mock room manager to return subscribers and occupants
        connection_manager.room_manager = Mock()
        connection_manager.room_manager.get_room_subscribers.return_value = {"player1", "player2"}
        connection_manager.room_manager.get_room_occupants.return_value = []

        # Create multiple mock websockets for player1
        websocket1a = self._create_mock_websocket()
        websocket1b = self._create_mock_websocket()

        # Connect multiple WebSockets for player1
        success1a = await connection_manager.connect_websocket(websocket1a, "player1", "session_1a")
        success1b = await connection_manager.connect_websocket(websocket1b, "player1", "session_1b")
        assert success1a is True
        assert success1b is True

        # Connect SSE for player1
        sse_connection_id = await connection_manager.connect_sse("player1", "session_1c")
        assert sse_connection_id is not None

        # Connect single WebSocket for player2
        websocket2 = self._create_mock_websocket()

        success2 = await connection_manager.connect_websocket(websocket2, "player2", "session_2")
        assert success2 is True

        # Broadcast to room
        test_event = {"type": "room_broadcast", "content": "Hello Room"}
        broadcast_stats = await connection_manager.broadcast_to_room("test_room_001", test_event)

        # Verify broadcast statistics
        assert broadcast_stats["room_id"] == "test_room_001"
        assert broadcast_stats["total_targets"] == 2
        assert broadcast_stats["excluded_players"] == 0
        assert broadcast_stats["successful_deliveries"] == 2
        assert broadcast_stats["failed_deliveries"] == 0
        assert "player1" in broadcast_stats["delivery_details"]
        assert "player2" in broadcast_stats["delivery_details"]

        # Verify player1 received message on all connections
        player1_delivery = broadcast_stats["delivery_details"]["player1"]
        assert player1_delivery["websocket_delivered"] == 2  # Two WebSocket connections
        assert player1_delivery["sse_delivered"] is True
        assert player1_delivery["total_connections"] == 3

        # Verify player2 received message
        player2_delivery = broadcast_stats["delivery_details"]["player2"]
        assert player2_delivery["websocket_delivered"] == 1  # One WebSocket connection
        assert player2_delivery["sse_delivered"] is False
        assert player2_delivery["total_connections"] == 1

    @pytest.mark.asyncio
    async def test_broadcast_to_room_with_exclusion(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test room broadcasting with player exclusion."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Mock room manager to return subscribers
        connection_manager.room_manager = Mock()
        connection_manager.room_manager.get_room_subscribers.return_value = {"player1", "player2", "player3"}

        # Connect players
        success1 = await connection_manager.connect_websocket(mock_websocket, "player1", "session_1")
        success2 = await connection_manager.connect_websocket(mock_websocket, "player2", "session_2")
        success3 = await connection_manager.connect_websocket(mock_websocket, "player3", "session_3")
        assert success1 is True
        assert success2 is True
        assert success3 is True

        # Broadcast to room excluding player2
        test_event = {"type": "room_broadcast", "content": "Hello Room"}
        broadcast_stats = await connection_manager.broadcast_to_room(
            "test_room_001", test_event, exclude_player="player2"
        )

        # Verify broadcast statistics
        assert broadcast_stats["room_id"] == "test_room_001"
        assert broadcast_stats["total_targets"] == 3
        assert broadcast_stats["excluded_players"] == 1
        assert broadcast_stats["successful_deliveries"] == 2  # Only player1 and player3
        assert broadcast_stats["failed_deliveries"] == 0
        assert "player1" in broadcast_stats["delivery_details"]
        assert "player2" not in broadcast_stats["delivery_details"]  # Excluded
        assert "player3" in broadcast_stats["delivery_details"]

    @pytest.mark.asyncio
    async def test_broadcast_global_multiple_connections(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test global broadcasting with multiple connections per player."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        _mock_room = self._setup_mock_room(mock_persistence, "test_room_001")

        # Create multiple mock websockets for player1
        websocket1a = self._create_mock_websocket()
        websocket1b = self._create_mock_websocket()

        # Connect multiple WebSockets for player1
        success1a = await connection_manager.connect_websocket(websocket1a, "player1", "session_1a")
        success1b = await connection_manager.connect_websocket(websocket1b, "player1", "session_1b")
        assert success1a is True
        assert success1b is True

        # Connect SSE for player1
        sse_connection_id = await connection_manager.connect_sse("player1", "session_1c")
        assert sse_connection_id is not None

        # Connect only SSE for player2 (no WebSocket)
        sse_connection_id2 = await connection_manager.connect_sse("player2", "session_2")
        assert sse_connection_id2 is not None

        # Connect only WebSocket for player3 (no SSE)
        websocket3 = self._create_mock_websocket()

        success3 = await connection_manager.connect_websocket(websocket3, "player3", "session_3")
        assert success3 is True

        # Broadcast globally
        test_event = {"type": "global_broadcast", "content": "Hello World"}
        global_stats = await connection_manager.broadcast_global(test_event)

        # Verify global broadcast statistics
        assert global_stats["total_players"] == 3
        assert global_stats["excluded_players"] == 0
        assert global_stats["successful_deliveries"] == 3
        assert global_stats["failed_deliveries"] == 0
        assert "player1" in global_stats["delivery_details"]
        assert "player2" in global_stats["delivery_details"]
        assert "player3" in global_stats["delivery_details"]

        # Verify player1 received message on all connections
        player1_delivery = global_stats["delivery_details"]["player1"]
        assert player1_delivery["websocket_delivered"] == 2  # Two WebSocket connections
        assert player1_delivery["sse_delivered"] is True
        assert player1_delivery["total_connections"] == 3

        # Verify player2 received message via SSE only
        player2_delivery = global_stats["delivery_details"]["player2"]
        assert player2_delivery["websocket_delivered"] == 0
        assert player2_delivery["sse_delivered"] is True
        assert player2_delivery["total_connections"] == 1

        # Verify player3 received message via WebSocket only
        player3_delivery = global_stats["delivery_details"]["player3"]
        assert player3_delivery["websocket_delivered"] == 1
        assert player3_delivery["sse_delivered"] is False
        assert player3_delivery["total_connections"] == 1

    @pytest.mark.asyncio
    async def test_broadcast_global_with_exclusion(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test global broadcasting with player exclusion."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Connect players
        success1 = await connection_manager.connect_websocket(mock_websocket, "player1", "session_1")
        success2 = await connection_manager.connect_websocket(mock_websocket, "player2", "session_2")
        success3 = await connection_manager.connect_websocket(mock_websocket, "player3", "session_3")
        assert success1 is True
        assert success2 is True
        assert success3 is True

        # Broadcast globally excluding player2
        test_event = {"type": "global_broadcast", "content": "Hello World"}
        global_stats = await connection_manager.broadcast_global(test_event, exclude_player="player2")

        # Verify global broadcast statistics
        assert global_stats["total_players"] == 3
        assert global_stats["excluded_players"] == 1
        assert global_stats["successful_deliveries"] == 2  # Only player1 and player3
        assert global_stats["failed_deliveries"] == 0
        assert "player1" in global_stats["delivery_details"]
        assert "player2" not in global_stats["delivery_details"]  # Excluded
        assert "player3" in global_stats["delivery_details"]

    @pytest.mark.asyncio
    async def test_broadcast_to_room_mixed_connection_types(
        self, connection_manager, mock_websocket, mock_player, mock_persistence
    ):
        """Test room broadcasting with mixed connection types."""
        connection_manager.persistence = mock_persistence
        mock_persistence.get_player.return_value = mock_player

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        # Mock room manager to return subscribers
        connection_manager.room_manager = Mock()
        connection_manager.room_manager.get_room_subscribers.return_value = {"player1", "player2", "player3"}

        # Player1: WebSocket only
        success1 = await connection_manager.connect_websocket(mock_websocket, "player1", "session_1")
        assert success1 is True

        # Player2: SSE only
        sse_connection_id2 = await connection_manager.connect_sse("player2", "session_2")
        assert sse_connection_id2 is not None

        # Player3: Both WebSocket and SSE
        websocket3 = Mock(spec=WebSocket)
        websocket3.accept = AsyncMock()
        websocket3.close = AsyncMock()
        websocket3.ping = AsyncMock()
        websocket3.send_json = AsyncMock()

        success3 = await connection_manager.connect_websocket(websocket3, "player3", "session_3a")
        sse_connection_id3 = await connection_manager.connect_sse("player3", "session_3b")
        assert success3 is True
        assert sse_connection_id3 is not None

        # Broadcast to room
        test_event = {"type": "room_broadcast", "content": "Hello Room"}
        broadcast_stats = await connection_manager.broadcast_to_room("test_room_001", test_event)

        # Verify broadcast statistics
        assert broadcast_stats["room_id"] == "test_room_001"
        assert broadcast_stats["total_targets"] == 3
        assert broadcast_stats["successful_deliveries"] == 3
        assert broadcast_stats["failed_deliveries"] == 0

        # Verify delivery details for each player
        player1_delivery = broadcast_stats["delivery_details"]["player1"]
        assert player1_delivery["websocket_delivered"] == 1
        assert player1_delivery["sse_delivered"] is False
        assert player1_delivery["total_connections"] == 1

        player2_delivery = broadcast_stats["delivery_details"]["player2"]
        assert player2_delivery["websocket_delivered"] == 0
        assert player2_delivery["sse_delivered"] is True
        assert player2_delivery["total_connections"] == 1

        player3_delivery = broadcast_stats["delivery_details"]["player3"]
        assert player3_delivery["websocket_delivered"] == 1
        assert player3_delivery["sse_delivered"] is True
        assert player3_delivery["total_connections"] == 2

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
        existing_websocket = self._create_mock_websocket()
        connection_id = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id] = existing_websocket
        connection_manager.player_websockets["test_player"] = [connection_id]

        # Mock room
        mock_room = Mock()
        mock_room.id = "test_room_001"
        mock_persistence.get_room.return_value = mock_room

        success = await connection_manager.connect_websocket(mock_websocket, "test_player")

        assert success is True
        # In dual connection system, old connections are preserved
        # Should have 2 WebSocket connections now
        assert len(connection_manager.player_websockets["test_player"]) == 2

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
        connection_manager.player_websockets["test_player"] = [connection_id]

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
        connection_manager.player_websockets["test_player"] = [connection_id]
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
        connection_manager.player_websockets["test_player"] = [connection_id]

        # Setup SSE connection
        connection_manager.active_sse_connections["test_player"] = ["sse_conn_id"]

        await connection_manager.force_disconnect_player("test_player")

        assert "test_player" not in connection_manager.player_websockets
        assert "test_player" not in connection_manager.active_sse_connections

    @pytest.mark.asyncio
    async def test_connect_sse_success(self, connection_manager):
        """Test successful SSE connection."""
        connection_id = await connection_manager.connect_sse("test_player")

        assert connection_id is not None
        assert "test_player" in connection_manager.active_sse_connections
        assert connection_id in connection_manager.active_sse_connections["test_player"]

    @pytest.mark.asyncio
    async def test_connect_sse_with_existing_websocket(self, connection_manager, mock_websocket):
        """Test SSE connection when player has existing WebSocket."""
        # Setup existing WebSocket
        connection_id = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id] = mock_websocket
        connection_manager.player_websockets["test_player"] = [connection_id]

        with patch.object(
            connection_manager, "disconnect_websocket", new_callable=AsyncMock
        ) as mock_disconnect_websocket:
            sse_connection_id = await connection_manager.connect_sse("test_player")

            assert sse_connection_id is not None
            # The SSE connection should not trigger WebSocket disconnection
            # since SSE and WebSocket can coexist
            mock_disconnect_websocket.assert_not_called()

    def test_disconnect_sse_success(self, connection_manager):
        """Test successful SSE disconnection."""
        # Setup SSE connection
        connection_manager.active_sse_connections["test_player"] = ["sse_conn_id"]
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

    def test_mark_player_seen_updates_persistence_throttled(self, connection_manager):
        """Ensure mark_player_seen updates persistence on interval and throttles duplicate updates."""
        mock_persistence = Mock()
        connection_manager.persistence = mock_persistence
        mock_persistence.update_player_last_active = Mock()
        connection_manager.last_active_update_interval = 60.0

        with patch("server.realtime.connection_manager.time.time", side_effect=[1000.0, 1000.0, 1065.0]):
            connection_manager.mark_player_seen("test_player")
            connection_manager.mark_player_seen("test_player")
            connection_manager.mark_player_seen("test_player")

        assert mock_persistence.update_player_last_active.call_count == 2
        first_call, second_call = mock_persistence.update_player_last_active.call_args_list
        assert first_call.args[0] == "test_player"
        assert second_call.args[0] == "test_player"
        assert connection_manager.last_active_update_times["test_player"] == 1065.0

    def test_prune_stale_players(self, connection_manager):
        """Test pruning stale players."""
        # Add some players with different timestamps
        connection_manager.last_seen["recent_player"] = time.time()
        connection_manager.last_seen["stale_player"] = time.time() - 200  # 200 seconds ago
        connection_manager.online_players["recent_player"] = {"player_id": "recent_player"}
        connection_manager.online_players["stale_player"] = {"player_id": "stale_player"}
        connection_manager.room_occupants["test_room"] = {"recent_player", "stale_player"}
        connection_manager.last_active_update_times["stale_player"] = 0.0

        connection_manager.prune_stale_players(max_age_seconds=90)

        assert "recent_player" in connection_manager.online_players
        assert "stale_player" not in connection_manager.online_players
        assert "stale_player" not in connection_manager.last_seen
        assert "stale_player" not in connection_manager.last_active_update_times

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
        connection_manager.active_sse_connections["sse_player"] = ["sse_conn"]

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
        connection_manager.player_websockets["test_player"] = [connection_id]

        event = {"type": "test_event", "data": "test_data"}
        result = await connection_manager.send_personal_message("test_player", event)

        assert result["success"] is True
        assert result["websocket_delivered"] == 1
        mock_websocket.send_json.assert_called_once_with(event)

    @pytest.mark.asyncio
    async def test_send_personal_message_fallback_to_pending(self, connection_manager):
        """Test sending personal message falls back to pending messages."""
        event = {"type": "test_event", "data": "test_data"}
        result = await connection_manager.send_personal_message("test_player", event)

        assert result["success"] is True  # Message was queued for later delivery
        assert result["websocket_delivered"] == 0
        assert result["sse_delivered"] is True  # Message was queued
        # Note: messages are queued for later delivery when no connections exist

    @pytest.mark.asyncio
    async def test_send_personal_message_exception(self, connection_manager, mock_websocket):
        """Test sending personal message with exception."""
        # Setup WebSocket connection
        connection_id = str(uuid.uuid4())
        connection_manager.active_websockets[connection_id] = mock_websocket
        connection_manager.player_websockets["test_player"] = [connection_id]
        mock_websocket.send_json.side_effect = Exception("Test exception")

        event = {"type": "test_event", "data": "test_data"}
        result = await connection_manager.send_personal_message("test_player", event)

        assert result["success"] is False
        assert result["websocket_failed"] == 1

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
        connection_manager.player_websockets["player1"] = [connection_id1]
        connection_manager.player_websockets["player2"] = [connection_id2]

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
        connection_manager.player_websockets["player1"] = [connection_id1]
        connection_manager.player_websockets["player2"] = [connection_id2]

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
        connection_manager.player_websockets["player1"] = [connection_id1]
        connection_manager.player_websockets["player2"] = [connection_id2]

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
        mock_room = self._setup_mock_room(mock_persistence, "test_room_001")
        mock_room.to_dict.return_value = {"room_id": "test_room_001", "name": "Test Room"}

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
        connection_manager.active_sse_connections["test_player"] = ["existing_sse_id"]

        sse_connection_id = await connection_manager.connect_sse("test_player")

        assert sse_connection_id is not None
        # In dual connection system, multiple SSE connections are allowed
        # Should have 2 SSE connections now
        assert len(connection_manager.active_sse_connections["test_player"]) == 2

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
                mock_track.assert_called_once_with("test_player", mock_player, "sse")

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
        connection_manager.active_sse_connections["test_player"] = ["sse_conn_id"]

        # Create a mock that returns a completed coroutine
        async def mock_track_async(player_id):
            return None

        with patch.object(connection_manager, "_track_player_disconnected", side_effect=mock_track_async) as mock_track:
            connection_manager.disconnect_sse("test_player")

            mock_track.assert_called_once_with("test_player")

    def test_disconnect_sse_with_sync_tracking(self, connection_manager):
        """Test SSE disconnection with sync tracking (no running loop)."""
        # Setup SSE connection
        connection_manager.active_sse_connections["test_player"] = ["sse_conn_id"]

        with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
            with patch("asyncio.run") as mock_run:
                connection_manager.disconnect_sse("test_player")

                mock_run.assert_called_once()

    @pytest.mark.filterwarnings("ignore:coroutine.*was never awaited:RuntimeWarning")
    def test_disconnect_sse_with_tracking_exception(self, connection_manager):
        """Test SSE disconnection with tracking exception."""
        # Setup SSE connection
        connection_manager.active_sse_connections["test_player"] = ["sse_conn_id"]

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
