"""
Performance tests for dual connection system.

This module tests the performance characteristics of the dual connection system,
including message delivery performance, connection establishment performance,
memory usage, and system stability under load.
"""

import asyncio
import time
from unittest.mock import AsyncMock

import pytest

from server.realtime.connection_manager import ConnectionManager

# Mark entire module as slow for CI/CD-only execution
pytestmark = pytest.mark.slow


class TestDualConnectionPerformance:
    """Test dual connection system performance."""

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

    @pytest.mark.asyncio
    async def test_connection_establishment_performance(self, connection_manager, mock_websocket):
        """Test connection establishment performance with multiple players."""
        num_players = 50
        players = [f"player_{i}" for i in range(num_players)]
        session_id = "session_1"

        # Measure connection establishment time
        start_time = time.time()

        # Establish dual connections for all players
        for player_id in players:
            await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
            await connection_manager.connect_sse(player_id, session_id)

        establishment_time = time.time() - start_time
        total_connections = num_players * 2

        # Performance assertions
        assert establishment_time < 10.0  # Should establish 100 connections in under 10 seconds
        assert establishment_time / total_connections < 0.1  # Less than 100ms per connection

        # Verify all connections were established
        for player_id in players:
            assert connection_manager.has_websocket_connection(player_id)
            assert connection_manager.has_sse_connection(player_id)

        # Check performance stats
        perf_stats = connection_manager.get_performance_stats()
        assert perf_stats["connection_establishment"]["total_connections"] == total_connections
        assert perf_stats["connection_establishment"]["websocket_connections"] == num_players
        assert perf_stats["connection_establishment"]["sse_connections"] == num_players

        # Average establishment time should be reasonable
        avg_ws_time = perf_stats["connection_establishment"]["avg_websocket_establishment_ms"]
        avg_sse_time = perf_stats["connection_establishment"]["avg_sse_establishment_ms"]
        assert avg_ws_time < 100  # Less than 100ms average
        assert avg_sse_time < 100  # Less than 100ms average

    @pytest.mark.asyncio
    async def test_message_delivery_performance(self, connection_manager, mock_websocket):
        """Test message delivery performance with multiple connections."""
        num_players = 30
        players = [f"player_{i}" for i in range(num_players)]
        session_id = "session_1"
        test_message = {"type": "performance_test", "content": "Load test message"}

        # Establish dual connections for all players
        for player_id in players:
            await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
            await connection_manager.connect_sse(player_id, session_id)

        # Measure message delivery time
        start_time = time.time()

        # Send messages to all players
        delivery_results = []
        for player_id in players:
            result = await connection_manager.send_personal_message(player_id, test_message)
            delivery_results.append(result)

        delivery_time = time.time() - start_time
        total_messages = num_players

        # Performance assertions
        assert delivery_time < 5.0  # Should deliver 30 messages in under 5 seconds
        assert delivery_time / total_messages < 0.2  # Less than 200ms per message

        # Verify all messages were delivered successfully
        for result in delivery_results:
            assert result["success"] is True
            assert result["total_connections"] == 2
            assert result["websocket_delivered"] == 1
            assert result["sse_delivered"] == 1

        # Verify WebSocket received all messages
        assert mock_websocket.send_json.call_count == num_players

    @pytest.mark.asyncio
    async def test_broadcast_performance(self, connection_manager, mock_websocket):
        """Test broadcast performance with multiple players."""
        num_players = 25
        players = [f"player_{i}" for i in range(num_players)]
        session_id = "session_1"
        test_message = {"type": "broadcast_test", "content": "Broadcast performance test"}

        # Establish dual connections for all players
        for player_id in players:
            await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
            await connection_manager.connect_sse(player_id, session_id)

        # Measure broadcast time
        start_time = time.time()

        # Perform global broadcast
        broadcast_result = await connection_manager.broadcast_global(test_message)

        broadcast_time = time.time() - start_time

        # Performance assertions
        assert broadcast_time < 3.0  # Should broadcast to 25 players in under 3 seconds
        assert broadcast_time / num_players < 0.15  # Less than 150ms per player

        # Verify broadcast results
        assert broadcast_result["total_players"] == num_players
        assert broadcast_result["successful_deliveries"] == num_players
        assert broadcast_result["failed_deliveries"] == 0

        # Verify WebSocket received all messages
        assert mock_websocket.send_json.call_count == num_players

    @pytest.mark.asyncio
    async def test_memory_usage_with_multiple_connections(self, connection_manager, mock_websocket):
        """Test memory usage with multiple connections."""
        num_players = 100
        players = [f"player_{i}" for i in range(num_players)]
        session_id = "session_1"

        # Get initial memory stats
        connection_manager.get_memory_stats()

        # Establish dual connections for all players
        for player_id in players:
            await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
            await connection_manager.connect_sse(player_id, session_id)

        # Get memory stats after connections
        final_stats = connection_manager.get_memory_stats()

        # Verify memory usage is reasonable
        assert final_stats["connections"]["total_connections"] == num_players * 2

        # Each player has exactly 1 WebSocket and 1 SSE connection, so they all have dual connections
        assert final_stats["connections"]["players_with_dual_connections"] == num_players
        assert final_stats["connections"]["dual_connection_rate"] == 100.0

        # Check that memory usage is proportional to connections
        total_connections = final_stats["connections"]["total_connections"]
        assert total_connections == num_players * 2

        # Verify connection metadata is properly tracked
        assert len(connection_manager.connection_metadata) == num_players * 2

        # Check session tracking - each player gets their own session
        assert final_stats["sessions"]["total_sessions"] == num_players
        assert final_stats["sessions"]["total_session_connections"] == num_players * 2
        assert final_stats["sessions"]["avg_connections_per_session"] == 2.0

    @pytest.mark.asyncio
    async def test_system_stability_under_load(self, connection_manager, mock_websocket):
        """Test system stability under high load."""
        num_players = 75
        players = [f"player_{i}" for i in range(num_players)]
        session_id = "session_1"
        num_messages = 10

        # Establish dual connections for all players
        for player_id in players:
            await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
            await connection_manager.connect_sse(player_id, session_id)

        # Send multiple messages to all players (stress test)
        start_time = time.time()

        for message_num in range(num_messages):
            test_message = {"type": "stress_test", "content": f"Message {message_num}"}

            # Send to all players
            for player_id in players:
                result = await connection_manager.send_personal_message(player_id, test_message)
                assert result["success"] is True

        total_time = time.time() - start_time
        total_operations = num_players * num_messages

        # Performance assertions
        assert total_time < 30.0  # Should complete in under 30 seconds
        assert total_time / total_operations < 0.05  # Less than 50ms per operation

        # Verify system stability - all connections should still be healthy
        health_stats = connection_manager.get_connection_health_stats()
        assert health_stats["overall_health"]["total_connections"] == num_players * 2
        assert health_stats["overall_health"]["healthy_connections"] == num_players * 2
        assert health_stats["overall_health"]["unhealthy_connections"] == 0

        # Verify all players still have dual connections
        for player_id in players:
            assert connection_manager.has_websocket_connection(player_id)
            assert connection_manager.has_sse_connection(player_id)

    @pytest.mark.asyncio
    async def test_connection_cleanup_performance(self, connection_manager, mock_websocket):
        """Test connection cleanup performance."""
        num_players = 50
        players = [f"player_{i}" for i in range(num_players)]
        session_id = "session_1"

        # Establish dual connections for all players
        for player_id in players:
            await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
            await connection_manager.connect_sse(player_id, session_id)

        # Verify connections exist
        for player_id in players:
            assert connection_manager.has_websocket_connection(player_id)
            assert connection_manager.has_sse_connection(player_id)

        # Measure cleanup time
        start_time = time.time()

        # Disconnect all players
        for player_id in players:
            await connection_manager.force_disconnect_player(player_id)

        cleanup_time = time.time() - start_time

        # Performance assertions
        assert cleanup_time < 5.0  # Should cleanup 50 players in under 5 seconds
        assert cleanup_time / num_players < 0.1  # Less than 100ms per player

        # Verify all connections are cleaned up
        for player_id in players:
            assert not connection_manager.has_websocket_connection(player_id)
            assert not connection_manager.has_sse_connection(player_id)

        # Verify metadata cleanup
        assert len(connection_manager.connection_metadata) == 0

    @pytest.mark.asyncio
    async def test_session_switching_performance(self, connection_manager, mock_websocket):
        """Test session switching performance."""
        num_players = 30
        players = [f"player_{i}" for i in range(num_players)]
        session_1 = "session_1"
        session_2 = "session_2"

        # Establish connections in session 1
        for player_id in players:
            await connection_manager.connect_websocket(mock_websocket, player_id, session_1)
            await connection_manager.connect_sse(player_id, session_1)

        # Measure session switching time
        start_time = time.time()

        # Switch all players to session 2
        for player_id in players:
            await connection_manager.handle_new_game_session(player_id, session_2)

        switch_time = time.time() - start_time

        # Performance assertions
        assert switch_time < 5.0  # Should switch 30 players in under 5 seconds
        assert switch_time / num_players < 0.2  # Less than 200ms per player

        # Verify all players are in session 2
        for player_id in players:
            assert connection_manager.get_player_session(player_id) == session_2

        # Verify old connections were disconnected
        for player_id in players:
            assert not connection_manager.has_websocket_connection(player_id)
            assert not connection_manager.has_sse_connection(player_id)

    @pytest.mark.asyncio
    async def test_concurrent_connection_establishment(self, connection_manager, mock_websocket):
        """Test concurrent connection establishment performance."""
        num_players = 40
        players = [f"player_{i}" for i in range(num_players)]
        session_id = "session_1"

        async def establish_dual_connections(player_id):
            """Establish dual connections for a player."""
            await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
            await connection_manager.connect_sse(player_id, session_id)

        # Measure concurrent connection establishment time
        start_time = time.time()

        # Establish connections concurrently
        await asyncio.gather(*[establish_dual_connections(player_id) for player_id in players])

        establishment_time = time.time() - start_time
        total_connections = num_players * 2

        # Performance assertions (should be faster than sequential)
        assert establishment_time < 8.0  # Should establish 80 connections in under 8 seconds
        assert establishment_time / total_connections < 0.1  # Less than 100ms per connection

        # Verify all connections were established
        for player_id in players:
            assert connection_manager.has_websocket_connection(player_id)
            assert connection_manager.has_sse_connection(player_id)

    @pytest.mark.asyncio
    async def test_concurrent_message_delivery(self, connection_manager, mock_websocket):
        """Test concurrent message delivery performance."""
        num_players = 25
        players = [f"player_{i}" for i in range(num_players)]
        session_id = "session_1"
        test_message = {"type": "concurrent_test", "content": "Concurrent delivery test"}

        # Establish dual connections for all players
        for player_id in players:
            await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
            await connection_manager.connect_sse(player_id, session_id)

        async def send_message_to_player(player_id):
            """Send message to a specific player."""
            return await connection_manager.send_personal_message(player_id, test_message)

        # Measure concurrent message delivery time
        start_time = time.time()

        # Send messages concurrently
        delivery_results = await asyncio.gather(*[send_message_to_player(player_id) for player_id in players])

        delivery_time = time.time() - start_time

        # Performance assertions (should be faster than sequential)
        assert delivery_time < 2.0  # Should deliver 25 messages in under 2 seconds
        assert delivery_time / num_players < 0.1  # Less than 100ms per message

        # Verify all messages were delivered successfully
        for result in delivery_results:
            assert result["success"] is True
            assert result["total_connections"] == 2

    @pytest.mark.asyncio
    async def test_performance_stats_accuracy(self, connection_manager, mock_websocket):
        """Test that performance stats accurately reflect system performance."""
        num_players = 20
        players = [f"player_{i}" for i in range(num_players)]
        session_id = "session_1"

        # Get initial performance stats
        initial_stats = connection_manager.get_performance_stats()
        initial_connections = initial_stats["connection_establishment"]["total_connections"]

        # Establish dual connections for all players
        for player_id in players:
            await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
            await connection_manager.connect_sse(player_id, session_id)

        # Get final performance stats
        final_stats = connection_manager.get_performance_stats()
        final_connections = final_stats["connection_establishment"]["total_connections"]

        # Verify stats accuracy
        assert final_connections == initial_connections + (num_players * 2)
        assert final_stats["connection_establishment"]["websocket_connections"] == num_players
        assert final_stats["connection_establishment"]["sse_connections"] == num_players

        # Verify timing data is recorded
        assert final_stats["connection_establishment"]["avg_websocket_establishment_ms"] >= 0
        assert final_stats["connection_establishment"]["avg_sse_establishment_ms"] >= 0
        assert final_stats["connection_establishment"]["max_websocket_establishment_ms"] >= 0
        assert final_stats["connection_establishment"]["max_sse_establishment_ms"] >= 0

        # Verify memory management is working (lists should be capped)
        establishment_times = connection_manager.performance_stats["connection_establishment_times"]
        assert len(establishment_times) <= 1000  # Should be capped at 1000 entries

    @pytest.mark.asyncio
    async def test_health_monitoring_performance(self, connection_manager, mock_websocket):
        """Test health monitoring performance with many connections."""
        num_players = 60
        players = [f"player_{i}" for i in range(num_players)]
        session_id = "session_1"

        # Establish dual connections for all players
        for player_id in players:
            await connection_manager.connect_websocket(mock_websocket, player_id, session_id)
            await connection_manager.connect_sse(player_id, session_id)

        # Measure health check performance
        start_time = time.time()

        # Perform health checks
        health_stats = connection_manager.get_connection_health_stats()
        dual_stats = connection_manager.get_dual_connection_stats()
        perf_stats = connection_manager.get_performance_stats()

        health_check_time = time.time() - start_time

        # Performance assertions
        assert health_check_time < 1.0  # Should complete health checks in under 1 second

        # Verify health stats accuracy
        assert health_stats["overall_health"]["total_connections"] == num_players * 2
        assert health_stats["overall_health"]["healthy_connections"] == num_players * 2
        assert health_stats["overall_health"]["unhealthy_connections"] == 0

        # Verify dual connection stats accuracy
        assert dual_stats["connection_distribution"]["total_players"] == num_players
        assert dual_stats["connection_distribution"]["dual_connection_players"] == num_players
        assert dual_stats["connection_distribution"]["dual_connection_percentage"] == 100.0

        # Verify performance stats accuracy
        assert perf_stats["connection_establishment"]["total_connections"] == num_players * 2
