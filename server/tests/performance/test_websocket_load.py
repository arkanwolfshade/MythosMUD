"""
Load tests for WebSocket connections and message handling.

This module tests the system under load with:
- 100+ concurrent connections
- Message flooding scenarios
- Memory leak detection
"""

import asyncio
import gc
import time
from unittest.mock import AsyncMock, Mock

import pytest

from server.realtime.connection_manager import ConnectionManager


class TestWebSocketLoad:
    """Load tests for WebSocket system."""

    @pytest.fixture
    def connection_manager(self):
        """Create a ConnectionManager instance for testing."""
        cm = ConnectionManager()
        cm.persistence = None
        return cm

    @pytest.mark.asyncio
    async def test_100_concurrent_connections(self, connection_manager):
        """Test system handles 100 concurrent WebSocket connections."""
        num_connections = 100
        mock_websockets = []
        player_ids = []

        # Create 100 mock WebSocket connections
        for i in range(num_connections):
            websocket = AsyncMock()
            websocket.accept = AsyncMock()
            websocket.send_json = AsyncMock()
            websocket.client_state.name = "CONNECTED"
            websocket.state = {}
            mock_websockets.append(websocket)

            player_id = f"load_test_player_{i}"
            player_ids.append(player_id)

            # Create mock player
            player = Mock()
            player.player_id = player_id
            player.name = f"LoadTestPlayer{i}"
            player.current_room_id = "test_room_001"
            player.get_stats = Mock(return_value={"health": 100, "level": 1})

            connection_manager._get_player = AsyncMock(return_value=player)

        # Connect all WebSockets concurrently
        tasks = [
            connection_manager.connect_websocket(ws, pid) for ws, pid in zip(mock_websockets, player_ids, strict=True)
        ]
        await asyncio.gather(*tasks)

        # Verify all connections are active
        assert len(connection_manager.active_websockets) == num_connections
        assert len(connection_manager.player_websockets) == num_connections

        # Verify no memory leaks (connection count should match)
        assert len(connection_manager.connection_metadata) == num_connections

    @pytest.mark.asyncio
    async def test_message_flooding_protection(self, connection_manager):
        """Test system protects against message flooding attacks."""
        # Create connection
        websocket = AsyncMock()
        websocket.accept = AsyncMock()
        websocket.send_json = AsyncMock()
        websocket.client_state.name = "CONNECTED"
        websocket.state = {}

        player_id = "flood_test_player"
        player = Mock()
        player.player_id = player_id
        player.name = "FloodTestPlayer"
        player.current_room_id = "test_room_001"
        player.get_stats = Mock(return_value={"health": 100, "level": 1})

        connection_manager._get_player = AsyncMock(return_value=player)
        await connection_manager.connect_websocket(websocket, player_id)

        connection_id = connection_manager.get_connection_id_from_websocket(websocket)

        # Attempt to flood with messages
        allowed_count = 0
        blocked_count = 0

        # Send messages rapidly (simulating flood)
        for _ in range(200):  # Try to send 200 messages (limit is 100/minute)
            if connection_manager.rate_limiter.check_message_rate_limit(connection_id):
                allowed_count += 1
            else:
                blocked_count += 1

        # Verify rate limiting worked
        assert allowed_count <= 100, "Rate limit should cap at 100 messages"
        assert blocked_count >= 100, "Rate limit should block excess messages"

    @pytest.mark.asyncio
    async def test_memory_leak_detection(self, connection_manager):
        """Test for memory leaks in connection management."""
        from unittest.mock import patch

        # Patch loggers to avoid file I/O blocking under high concurrency
        # The logging system uses threading locks which can block the async event loop
        with (
            patch("server.realtime.integration.game_state_provider.logger") as mock_game_state_logger,
            patch("server.realtime.connection_manager.logger") as mock_connection_logger,
            patch("server.realtime.websocket_handler.logger") as mock_websocket_logger,
        ):
            # Mock all logging methods for all loggers
            for mock_logger in [mock_game_state_logger, mock_connection_logger, mock_websocket_logger]:
                mock_logger.warning = Mock()
                mock_logger.info = Mock()
                mock_logger.debug = Mock()
                mock_logger.error = Mock()

            # Get initial memory usage (approximate)
            initial_connections = len(connection_manager.active_websockets)
            initial_metadata = len(connection_manager.connection_metadata)

            # Create and destroy many connections
            num_cycles = 50
            connections_per_cycle = 10

            for cycle in range(num_cycles):
                # Create connections
                for i in range(connections_per_cycle):
                    websocket = AsyncMock()
                    websocket.accept = AsyncMock()
                    websocket.send_json = AsyncMock()
                    websocket.client_state.name = "CONNECTED"
                    websocket.state = {}

                    player_id = f"leak_test_player_{cycle}_{i}"
                    player = Mock()
                    player.player_id = player_id
                    player.name = f"LeakTestPlayer{cycle}_{i}"
                    player.current_room_id = "test_room_001"
                    player.get_stats = Mock(return_value={"health": 100, "level": 1})

                    connection_manager._get_player = AsyncMock(return_value=player)
                    await connection_manager.connect_websocket(websocket, player_id)

                # Disconnect all connections
                for i in range(connections_per_cycle):
                    player_id = f"leak_test_player_{cycle}_{i}"
                    await connection_manager.disconnect_websocket(player_id)

                # Force garbage collection
                gc.collect()

                # Verify cleanup (allow some tolerance for async cleanup)
                await asyncio.sleep(0.1)

            # Final cleanup
            await asyncio.sleep(0.5)
            gc.collect()

            # Verify no memory leaks (connections should be cleaned up)
            # Note: Some connections may remain if cleanup is async, but should be minimal
            final_connections = len(connection_manager.active_websockets)
            final_metadata = len(connection_manager.connection_metadata)

            # Connections should be cleaned up (allow small tolerance)
            assert final_connections <= initial_connections + 5, "Memory leak detected: connections not cleaned up"
            assert final_metadata <= initial_metadata + 5, "Memory leak detected: metadata not cleaned up"

    @pytest.mark.asyncio
    async def test_concurrent_message_broadcasting(self, connection_manager):
        """Test concurrent message broadcasting to many recipients."""
        num_recipients = 50
        mock_websockets = []
        player_ids = []

        # Create recipients
        for i in range(num_recipients):
            websocket = AsyncMock()
            websocket.accept = AsyncMock()
            websocket.send_json = AsyncMock()
            websocket.client_state.name = "CONNECTED"
            websocket.state = {}
            mock_websockets.append(websocket)

            player_id = f"broadcast_test_player_{i}"
            player_ids.append(player_id)

            player = Mock()
            player.player_id = player_id
            player.name = f"BroadcastTestPlayer{i}"
            player.current_room_id = "test_room_001"
            player.get_stats = Mock(return_value={"health": 100, "level": 1})

            connection_manager._get_player = AsyncMock(return_value=player)
            await connection_manager.connect_websocket(websocket, player_id)

            # Subscribe to room
            await connection_manager.subscribe_to_room(player_id, "test_room_001")

        # Broadcast message to all recipients concurrently
        message = {"type": "test", "content": "Load test message"}
        start_time = time.time()

        await connection_manager.broadcast_to_room("test_room_001", message)

        end_time = time.time()
        duration = end_time - start_time

        # Verify all recipients received the message
        for websocket in mock_websockets:
            assert websocket.send_json.called, "All recipients should receive broadcast"

        # Verify performance (should complete in reasonable time)
        assert duration < 5.0, f"Broadcast took too long: {duration}s"

    @pytest.mark.asyncio
    async def test_rate_limiter_under_load(self, connection_manager):
        """Test rate limiter performance under load."""
        num_connections = 50
        connection_ids = []

        # Create connections
        for i in range(num_connections):
            websocket = AsyncMock()
            websocket.accept = AsyncMock()
            websocket.client_state.name = "CONNECTED"
            websocket.state = {}

            player_id = f"rate_limit_test_player_{i}"
            player = Mock()
            player.player_id = player_id
            player.name = f"RateLimitTestPlayer{i}"
            player.current_room_id = "test_room_001"
            player.get_stats = Mock(return_value={"health": 100, "level": 1})

            connection_manager._get_player = AsyncMock(return_value=player)
            await connection_manager.connect_websocket(websocket, player_id)

            connection_id = connection_manager.get_connection_id_from_websocket(websocket)
            connection_ids.append(connection_id)

        # Test rate limiting for all connections concurrently
        start_time = time.time()

        # Check rate limits for all connections
        tasks = [
            asyncio.create_task(asyncio.to_thread(connection_manager.rate_limiter.check_message_rate_limit, cid))
            for cid in connection_ids
        ]
        results = await asyncio.gather(*tasks)

        end_time = time.time()
        duration = end_time - start_time

        # All should pass (first check for each connection)
        assert all(results), "All connections should pass initial rate limit check"

        # Verify performance
        assert duration < 1.0, f"Rate limit checks took too long: {duration}s"
