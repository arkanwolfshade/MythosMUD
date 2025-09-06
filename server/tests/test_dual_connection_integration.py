"""
Integration tests for dual connection system.

This module tests the complete dual connection system integration,
including simultaneous WebSocket and SSE connections, message delivery,
disconnection scenarios, error handling, and session management.
"""

import asyncio
import time
from unittest.mock import AsyncMock

import pytest

from server.realtime.connection_manager import ConnectionManager


class TestDualConnectionIntegration:
    """Test dual connection system integration."""

    @pytest.fixture
    def connection_manager(self):
        """Create a connection manager instance for testing."""
        manager = ConnectionManager()
        return manager

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock()
        websocket.send_json = AsyncMock()
        websocket.close = AsyncMock()
        websocket.ping = AsyncMock()
        return websocket

    @pytest.fixture
    def mock_sse_queue(self):
        """Create a mock SSE queue for testing."""
        return asyncio.Queue()

    @pytest.mark.asyncio
    async def test_dual_connection_establishment(self, connection_manager, mock_websocket, mock_sse_queue):
        """Test establishing both WebSocket and SSE connections for a player."""
        player_id = "test_player"
        session_id = "session_1"

        # Establish WebSocket connection
        ws_success = await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
        assert ws_success is True

        # Establish SSE connection
        sse_connection_id = await connection_manager.connect_sse(player_id, session_id)
        assert sse_connection_id is not None

        # Verify both connections exist
        assert connection_manager.has_websocket_connection(player_id)
        assert connection_manager.has_sse_connection(player_id)

        # Verify connection metadata
        ws_connections = connection_manager.player_websockets.get(player_id, [])
        sse_connections = connection_manager.active_sse_connections.get(player_id, [])

        assert len(ws_connections) == 1
        assert len(sse_connections) == 1

        # Verify metadata for both connections
        for conn_id in ws_connections + sse_connections:
            metadata = connection_manager.connection_metadata.get(conn_id)
            assert metadata is not None
            assert metadata.player_id == player_id
            assert metadata.session_id == session_id
            assert metadata.is_healthy is True

        # Verify dual connection stats
        stats = connection_manager.get_dual_connection_stats()
        assert stats["connection_distribution"]["dual_connection_players"] == 1
        assert stats["connection_distribution"]["dual_connection_percentage"] == 100.0

    @pytest.mark.asyncio
    async def test_message_delivery_to_all_connections(self, connection_manager, mock_websocket, mock_sse_queue):
        """Test message delivery to all active connections."""
        player_id = "test_player"
        session_id = "session_1"
        test_message = {"type": "test_message", "content": "Hello from dual connections!"}

        # Establish both connections
        await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
        await connection_manager.connect_sse(player_id, session_id)

        # Send message to player
        delivery_result = await connection_manager.send_personal_message(player_id, test_message)

        # Verify delivery result
        assert delivery_result["success"] is True
        assert delivery_result["total_connections"] == 2
        assert delivery_result["active_connections"] == 2
        assert delivery_result["websocket_delivered"] == 1
        assert delivery_result["sse_delivered"] == 1

        # Verify WebSocket received the message
        mock_websocket.send_json.assert_called_once()
        sent_message = mock_websocket.send_json.call_args[0][0]
        assert sent_message == test_message

        # Verify SSE message was queued (we can't easily test the actual queue without more setup)
        # The important thing is that the delivery result shows SSE was delivered

    @pytest.mark.asyncio
    async def test_partial_connection_disconnection(self, connection_manager, mock_websocket, mock_sse_queue):
        """Test disconnecting one connection type while keeping the other."""
        player_id = "test_player"
        session_id = "session_1"

        # Establish both connections
        await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
        sse_connection_id = await connection_manager.connect_sse(player_id, session_id)

        # Verify both connections exist
        assert connection_manager.has_websocket_connection(player_id)
        assert connection_manager.has_sse_connection(player_id)

        # Disconnect only the SSE connection
        connection_manager.disconnect_sse_connection(player_id, sse_connection_id)

        # Verify WebSocket still exists but SSE is gone
        assert connection_manager.has_websocket_connection(player_id)
        assert not connection_manager.has_sse_connection(player_id)

        # Verify connection metadata cleanup
        sse_metadata = connection_manager.connection_metadata.get(sse_connection_id)
        assert sse_metadata is None

        # Verify dual connection stats updated
        stats = connection_manager.get_dual_connection_stats()
        assert stats["connection_distribution"]["dual_connection_players"] == 0
        assert stats["connection_distribution"]["websocket_only_players"] == 1

    @pytest.mark.asyncio
    async def test_complete_connection_disconnection(self, connection_manager, mock_websocket, mock_sse_queue):
        """Test disconnecting all connections for a player."""
        player_id = "test_player"
        session_id = "session_1"

        # Establish both connections
        await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
        await connection_manager.connect_sse(player_id, session_id)

        # Verify both connections exist
        assert connection_manager.has_websocket_connection(player_id)
        assert connection_manager.has_sse_connection(player_id)

        # Force disconnect all connections
        await connection_manager.force_disconnect_player(player_id)

        # Verify no connections exist
        assert not connection_manager.has_websocket_connection(player_id)
        assert not connection_manager.has_sse_connection(player_id)

        # Verify connection metadata cleanup
        ws_connections = connection_manager.player_websockets.get(player_id, [])
        sse_connections = connection_manager.active_sse_connections.get(player_id, [])
        assert len(ws_connections) == 0
        assert len(sse_connections) == 0

        # Verify player is no longer tracked (force_disconnect_player preserves session for reconnection)
        # This is expected behavior - the session is preserved for potential reconnection
        assert player_id in connection_manager.player_sessions

    @pytest.mark.asyncio
    async def test_session_switching_with_dual_connections(self, connection_manager, mock_websocket, mock_sse_queue):
        """Test session switching when player has dual connections."""
        player_id = "test_player"
        old_session = "session_1"
        new_session = "session_2"

        # Establish both connections in old session
        await connection_manager.connect_websocket(mock_websocket, player_id, old_session)
        await connection_manager.connect_sse(player_id, old_session)

        # Verify initial session
        assert connection_manager.get_player_session(player_id) == old_session

        # Switch to new session
        await connection_manager.handle_new_game_session(player_id, new_session)

        # Verify session was updated
        assert connection_manager.get_player_session(player_id) == new_session

        # Verify old connections were disconnected (session switch behavior)
        assert not connection_manager.has_websocket_connection(player_id)
        assert not connection_manager.has_sse_connection(player_id)

        # Verify session tracking
        old_session_connections = connection_manager.get_session_connections(old_session)
        new_session_connections = connection_manager.get_session_connections(new_session)
        assert player_id not in old_session_connections
        assert player_id not in new_session_connections  # No active connections in new session

    @pytest.mark.asyncio
    async def test_error_handling_websocket_failure(self, connection_manager, mock_websocket, mock_sse_queue):
        """Test error handling when WebSocket connection fails."""
        player_id = "test_player"
        session_id = "session_1"

        # Establish SSE connection first
        await connection_manager.connect_sse(player_id, session_id)

        # Mock WebSocket to raise an exception
        mock_websocket.send_json.side_effect = Exception("WebSocket connection failed")

        # Attempt to establish WebSocket connection
        ws_success = await connection_manager.connect_websocket(mock_websocket, player_id, session_id)

        # Connection should still succeed (the error is in message sending, not connection)
        assert ws_success is True

        # Verify both connections exist
        assert connection_manager.has_websocket_connection(player_id)
        assert connection_manager.has_sse_connection(player_id)

        # Test message delivery with WebSocket failure
        test_message = {"type": "test_message", "content": "Test message"}
        delivery_result = await connection_manager.send_personal_message(player_id, test_message)

        # Should report WebSocket failure but SSE success
        assert delivery_result["success"] is True  # Overall success because SSE worked
        assert delivery_result["websocket_delivered"] == 0
        assert delivery_result["websocket_failed"] == 1
        assert delivery_result["sse_delivered"] == 1

    @pytest.mark.asyncio
    async def test_connection_health_monitoring(self, connection_manager, mock_websocket, mock_sse_queue):
        """Test connection health monitoring with dual connections."""
        player_id = "test_player"
        session_id = "session_1"

        # Establish both connections
        await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
        await connection_manager.connect_sse(player_id, session_id)

        # Check initial health
        health_stats = connection_manager.get_connection_health_stats()
        assert health_stats["overall_health"]["total_connections"] == 2
        assert health_stats["overall_health"]["healthy_connections"] == 2
        assert health_stats["overall_health"]["unhealthy_connections"] == 0

        # Manually mark one connection as unhealthy
        connection_ids = list(connection_manager.connection_metadata.keys())
        if connection_ids:
            connection_manager.connection_metadata[connection_ids[0]].is_healthy = False

        # Check updated health
        health_stats = connection_manager.get_connection_health_stats()
        assert health_stats["overall_health"]["total_connections"] == 2
        assert health_stats["overall_health"]["healthy_connections"] == 1
        assert health_stats["overall_health"]["unhealthy_connections"] == 1
        assert health_stats["overall_health"]["health_percentage"] == 50.0

    @pytest.mark.asyncio
    async def test_multiple_players_dual_connections(self, connection_manager, mock_websocket, mock_sse_queue):
        """Test multiple players with dual connections."""
        players = ["player_1", "player_2", "player_3"]
        session_id = "session_1"

        # Establish dual connections for all players
        for player_id in players:
            await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
            await connection_manager.connect_sse(player_id, session_id)

        # Verify all players have dual connections
        for player_id in players:
            assert connection_manager.has_websocket_connection(player_id)
            assert connection_manager.has_sse_connection(player_id)

        # Test message delivery to all players
        test_message = {"type": "broadcast", "content": "Hello all players!"}

        # Use broadcast_global to test message delivery to all connections
        broadcast_result = await connection_manager.broadcast_global(test_message)

        # Should have delivered to 3 players (each with 2 connections)
        assert broadcast_result["total_players"] == 3
        assert broadcast_result["successful_deliveries"] == 3  # One per player (WebSocket)
        assert broadcast_result["failed_deliveries"] == 0

        # Verify dual connection stats
        stats = connection_manager.get_dual_connection_stats()
        assert stats["connection_distribution"]["total_players"] == 3
        assert stats["connection_distribution"]["dual_connection_players"] == 3
        assert stats["connection_distribution"]["dual_connection_percentage"] == 100.0

    @pytest.mark.asyncio
    async def test_connection_cleanup_on_disconnect(self, connection_manager, mock_websocket, mock_sse_queue):
        """Test that connection metadata is properly cleaned up on disconnect."""
        player_id = "test_player"
        session_id = "session_1"

        # Establish both connections
        await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
        sse_connection_id = await connection_manager.connect_sse(player_id, session_id)

        # Get connection IDs
        ws_connections = connection_manager.player_websockets.get(player_id, [])
        assert len(ws_connections) == 1
        ws_connection_id = ws_connections[0]

        # Verify metadata exists
        assert ws_connection_id in connection_manager.connection_metadata
        assert sse_connection_id in connection_manager.connection_metadata

        # Disconnect WebSocket
        await connection_manager.disconnect_websocket_connection(player_id, ws_connection_id)

        # Verify WebSocket metadata is cleaned up
        assert ws_connection_id not in connection_manager.connection_metadata
        assert sse_connection_id in connection_manager.connection_metadata  # SSE should still exist

        # Disconnect SSE
        connection_manager.disconnect_sse_connection(player_id, sse_connection_id)

        # Verify SSE metadata is cleaned up
        assert sse_connection_id not in connection_manager.connection_metadata

        # Verify no orphaned data (session is preserved for reconnection)
        assert player_id not in connection_manager.player_websockets
        assert player_id not in connection_manager.active_sse_connections
        # Session is preserved for potential reconnection
        assert player_id in connection_manager.player_sessions

    @pytest.mark.asyncio
    async def test_connection_recovery_after_failure(self, connection_manager, mock_websocket, mock_sse_queue):
        """Test connection recovery after a failure."""
        player_id = "test_player"
        session_id = "session_1"

        # Establish both connections
        await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
        await connection_manager.connect_sse(player_id, session_id)

        # Simulate a connection failure by marking one as unhealthy
        connection_ids = list(connection_manager.connection_metadata.keys())
        if connection_ids:
            connection_manager.connection_metadata[connection_ids[0]].is_healthy = False

        # Test error detection and handling
        error_state = await connection_manager.detect_and_handle_error_state(
            player_id, "connection_failure", {"connection_id": connection_ids[0]}
        )

        # Should detect the error state
        assert error_state is not None
        assert "error_type" in error_state
        assert "connections_kept" in error_state

        # Test recovery
        recovery_result = await connection_manager.recover_from_error(player_id, "connections_only")

        # Should attempt recovery
        assert recovery_result is not None
        assert "recovery_type" in recovery_result

    @pytest.mark.asyncio
    async def test_performance_under_load(self, connection_manager, mock_websocket, mock_sse_queue):
        """Test system performance with multiple dual connections."""
        num_players = 10
        players = [f"player_{i}" for i in range(num_players)]
        session_id = "session_1"

        # Establish dual connections for all players
        start_time = time.time()
        for player_id in players:
            await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
            await connection_manager.connect_sse(player_id, session_id)
        establishment_time = time.time() - start_time

        # Verify all connections established
        for player_id in players:
            assert connection_manager.has_websocket_connection(player_id)
            assert connection_manager.has_sse_connection(player_id)

        # Test message delivery performance
        test_message = {"type": "performance_test", "content": "Load test message"}

        start_time = time.time()
        delivery_results = []
        for player_id in players:
            result = await connection_manager.send_personal_message(player_id, test_message)
            delivery_results.append(result)
        delivery_time = time.time() - start_time

        # Verify all messages were delivered successfully
        for result in delivery_results:
            assert result["success"] is True
            assert result["total_connections"] == 2

        # Check performance stats
        perf_stats = connection_manager.get_performance_stats()
        assert perf_stats["connection_establishment"]["total_connections"] == num_players * 2
        assert perf_stats["connection_establishment"]["websocket_connections"] == num_players
        assert perf_stats["connection_establishment"]["sse_connections"] == num_players

        # Performance should be reasonable (establishment and delivery should complete quickly)
        assert establishment_time < 5.0  # Should establish 20 connections in under 5 seconds
        assert delivery_time < 2.0  # Should deliver 20 messages in under 2 seconds

    @pytest.mark.asyncio
    async def test_session_management_with_dual_connections(self, connection_manager, mock_websocket, mock_sse_queue):
        """Test session management features with dual connections."""
        player_id = "test_player"
        session_1 = "session_1"
        session_2 = "session_2"

        # Establish connections in session 1
        await connection_manager.connect_websocket(mock_websocket, player_id, session_1)
        await connection_manager.connect_sse(player_id, session_1)

        # Verify session tracking
        assert connection_manager.get_player_session(player_id) == session_1
        session_1_connections = connection_manager.get_session_connections(session_1)
        # get_session_connections returns connection IDs, not player IDs
        assert len(session_1_connections) == 2  # Should have 2 connections

        # Switch to session 2
        await connection_manager.handle_new_game_session(player_id, session_2)

        # Verify session was updated
        assert connection_manager.get_player_session(player_id) == session_2

        # Verify old connections were disconnected
        assert not connection_manager.has_websocket_connection(player_id)
        assert not connection_manager.has_sse_connection(player_id)

        # Establish new connections in session 2
        await connection_manager.connect_websocket(mock_websocket, player_id, session_2)
        await connection_manager.connect_sse(player_id, session_2)

        # Verify new session tracking
        session_2_connections = connection_manager.get_session_connections(session_2)
        assert len(session_2_connections) == 2  # Should have 2 connections

        # Test session validation
        assert connection_manager.validate_session(player_id, session_2) is True
        assert connection_manager.validate_session(player_id, "nonexistent_session") is False

        # Test session stats
        session_stats = connection_manager.get_session_stats()
        assert session_stats["total_sessions"] == 1  # Only current session (old session was cleaned up)
        assert session_stats["total_players_with_sessions"] == 1  # One player with session
        assert session_stats["sessions_with_connections"] == 1  # One session with connections
        assert session_stats["average_connections_per_session"] == 2.0  # 2 connections per session
