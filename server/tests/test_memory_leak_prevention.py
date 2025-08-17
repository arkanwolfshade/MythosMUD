"""
Tests for memory leak prevention system.

This module tests the memory monitoring, cleanup mechanisms,
and alert generation for the connection manager.
"""

import time
from unittest.mock import AsyncMock, Mock, patch

import pytest

from ..realtime.connection_manager import ConnectionManager, MemoryMonitor


class TestMemoryMonitor:
    """Test the MemoryMonitor class."""

    def test_memory_monitor_initialization(self):
        """Test MemoryMonitor initialization."""
        monitor = MemoryMonitor()

        assert monitor.cleanup_interval == 300
        assert monitor.memory_threshold == 0.8
        assert monitor.max_connection_age == 3600
        assert monitor.max_pending_messages == 1000
        assert monitor.max_rate_limit_entries == 1000

    @patch("psutil.Process")
    def test_memory_usage_low(self, mock_process):
        """Test memory usage when it's below threshold."""
        monitor = MemoryMonitor()
        mock_process.return_value.memory_percent.return_value = 50.0

        memory_usage = monitor.get_memory_usage()
        assert memory_usage == 0.5

    @patch("psutil.Process")
    def test_memory_usage_high(self, mock_process):
        """Test memory usage when it's above threshold."""
        monitor = MemoryMonitor()
        mock_process.return_value.memory_percent.return_value = 85.0

        memory_usage = monitor.get_memory_usage()
        assert memory_usage == 0.85

    def test_should_cleanup_time_based(self):
        """Test time-based cleanup trigger."""
        monitor = MemoryMonitor()
        monitor.last_cleanup_time = time.time() - 400  # 6+ minutes ago

        assert monitor.should_cleanup() is True

    @patch("psutil.Process")
    def test_should_cleanup_memory_based(self, mock_process):
        """Test memory-based cleanup trigger."""
        monitor = MemoryMonitor()
        mock_process.return_value.memory_percent.return_value = 85.0

        assert monitor.should_cleanup() is True

    def test_should_cleanup_not_needed(self):
        """Test when cleanup is not needed."""
        monitor = MemoryMonitor()
        monitor.last_cleanup_time = time.time() - 100  # 1+ minutes ago

        assert monitor.should_cleanup() is False

    @patch("psutil.Process")
    def test_get_memory_stats(self, mock_process):
        """Test getting memory statistics."""
        monitor = MemoryMonitor()
        mock_process.return_value.memory_info.return_value.rss = 1024 * 1024 * 100  # 100MB
        mock_process.return_value.memory_info.return_value.vms = 1024 * 1024 * 200  # 200MB
        mock_process.return_value.memory_percent.return_value = 50.0

        with patch("psutil.virtual_memory") as mock_vm:
            mock_vm.return_value.available = 1024 * 1024 * 500  # 500MB
            mock_vm.return_value.total = 1024 * 1024 * 1000  # 1GB

            stats = monitor.get_memory_stats()

            assert "rss_mb" in stats
            assert "vms_mb" in stats
            assert "percent" in stats
            assert "available_mb" in stats
            assert "total_mb" in stats


class TestConnectionManagerMemoryLeakPrevention:
    """Test memory leak prevention in ConnectionManager."""

    @pytest.fixture
    def connection_manager(self):
        """Create a ConnectionManager instance for testing."""
        return ConnectionManager()

    def test_connection_manager_memory_monitor(self, connection_manager):
        """Test that ConnectionManager has memory monitoring."""
        assert hasattr(connection_manager, "memory_monitor")
        assert isinstance(connection_manager.memory_monitor, MemoryMonitor)
        assert hasattr(connection_manager, "connection_timestamps")
        assert hasattr(connection_manager, "cleanup_stats")

    @pytest.mark.asyncio
    async def test_cleanup_orphaned_data(self, connection_manager):
        """Test cleanup of orphaned data."""
        # Add some test data
        connection_manager.connection_attempts["player1"] = [time.time() - 4000]  # Old
        connection_manager.connection_attempts["player2"] = [time.time()]  # Recent
        connection_manager.pending_messages["player1"] = [{"timestamp": time.time() - 4000}]  # Old
        connection_manager.pending_messages["player2"] = [{"timestamp": time.time()}]  # Recent

        # Perform cleanup
        await connection_manager.cleanup_orphaned_data()

        # Check that old data was removed
        assert "player1" not in connection_manager.connection_attempts
        assert "player1" not in connection_manager.pending_messages
        assert "player2" in connection_manager.connection_attempts
        assert "player2" in connection_manager.pending_messages

    @pytest.mark.asyncio
    async def test_cleanup_large_data_structures(self, connection_manager):
        """Test cleanup of large data structures."""
        # Add large rate limit entries
        connection_manager.connection_attempts["player1"] = [time.time()] * 1500  # Over limit

        # Add large pending message queue
        connection_manager.pending_messages["player1"] = [{"timestamp": time.time()}] * 1500  # Over limit

        # Perform cleanup
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

    @pytest.mark.asyncio
    async def test_cleanup_stale_connections(self, connection_manager):
        """Test cleanup of stale connections."""
        # Add a stale connection
        connection_manager.active_websockets["stale_conn"] = Mock()
        connection_manager.connection_timestamps["stale_conn"] = time.time() - 4000  # Old

        # Add a recent connection
        connection_manager.active_websockets["recent_conn"] = Mock()
        connection_manager.connection_timestamps["recent_conn"] = time.time()

        # Perform cleanup
        await connection_manager.cleanup_orphaned_data()

        # Check that stale connection was removed
        assert "stale_conn" not in connection_manager.active_websockets
        assert "stale_conn" not in connection_manager.connection_timestamps
        assert "recent_conn" in connection_manager.active_websockets
        assert "recent_conn" in connection_manager.connection_timestamps

    def test_get_memory_stats(self, connection_manager):
        """Test getting memory statistics."""
        stats = connection_manager.get_memory_stats()

        assert "memory" in stats
        assert "connections" in stats
        assert "data_structures" in stats
        assert "cleanup_stats" in stats
        assert "memory_monitor" in stats

        # Check connection stats
        assert "active_websockets" in stats["connections"]
        assert "active_sse" in stats["connections"]
        assert "total_connections" in stats["connections"]

        # Check data structure stats
        assert "online_players" in stats["data_structures"]
        assert "room_occupants" in stats["data_structures"]
        assert "connection_attempts" in stats["data_structures"]
        assert "pending_messages" in stats["data_structures"]

    def test_get_memory_alerts(self, connection_manager):
        """Test memory alert generation."""
        with patch.object(connection_manager.memory_monitor, "get_memory_usage", return_value=0.85):
            alerts = connection_manager.get_memory_alerts()

            # Should have memory warning
            assert any("WARNING: Memory usage" in alert for alert in alerts)

    def test_get_memory_alerts_large_structures(self, connection_manager):
        """Test memory alerts for large data structures."""
        # Add large data structures - need to add multiple players to exceed 1000 total entries
        for i in range(1001):
            connection_manager.connection_attempts[f"player{i}"] = [time.time()]
        for i in range(1001):
            connection_manager.pending_messages[f"player{i}"] = [{"timestamp": time.time()}]

        alerts = connection_manager.get_memory_alerts()

        # Should have warnings for large structures
        assert any("Large number of rate limit entries" in alert for alert in alerts)
        assert any("Large number of pending message queues" in alert for alert in alerts)

    def test_get_memory_alerts_stale_connections(self, connection_manager):
        """Test memory alerts for stale connections."""
        # Add stale connections
        connection_manager.connection_timestamps["stale1"] = time.time() - 4000  # Old
        connection_manager.connection_timestamps["stale2"] = time.time() - 4000  # Old

        alerts = connection_manager.get_memory_alerts()

        # Should have warning for stale connections
        assert any("stale connections detected" in alert for alert in alerts)

    @pytest.mark.asyncio
    async def test_force_cleanup(self, connection_manager):
        """Test force cleanup functionality."""
        # Add some test data
        connection_manager.connection_attempts["player1"] = [time.time() - 4000]  # Old
        connection_manager.pending_messages["player1"] = [{"timestamp": time.time() - 4000}]  # Old

        # Perform force cleanup
        await connection_manager.force_cleanup()

        # Check that cleanup was performed
        assert connection_manager.cleanup_stats["cleanups_performed"] > 0
        assert connection_manager.memory_monitor.last_cleanup_time > 0

    @pytest.mark.asyncio
    async def test_check_and_cleanup_triggered(self, connection_manager):
        """Test automatic cleanup trigger."""
        # Mock memory monitor to trigger cleanup
        with patch.object(connection_manager.memory_monitor, "should_cleanup", return_value=True):
            # Add some test data
            connection_manager.connection_attempts["player1"] = [time.time() - 4000]  # Old

            # Trigger cleanup check
            await connection_manager._check_and_cleanup()

            # Check that cleanup was performed
            assert connection_manager.cleanup_stats["memory_cleanups"] > 0

    @pytest.mark.asyncio
    async def test_check_and_cleanup_not_triggered(self, connection_manager):
        """Test that cleanup is not triggered when not needed."""
        # Mock memory monitor to not trigger cleanup
        with patch.object(connection_manager.memory_monitor, "should_cleanup", return_value=False):
            initial_cleanups = connection_manager.cleanup_stats["cleanups_performed"]

            # Trigger cleanup check
            await connection_manager._check_and_cleanup()

            # Check that cleanup was not performed
            assert connection_manager.cleanup_stats["cleanups_performed"] == initial_cleanups


class TestMemoryLeakPreventionIntegration:
    """Integration tests for memory leak prevention."""

    @pytest.mark.asyncio
    async def test_websocket_connection_cleanup(self):
        """Test that WebSocket connections are properly cleaned up."""

        # This test would require a more complex setup with actual WebSocket connections
        # For now, we'll test the connection manager directly
        connection_manager = ConnectionManager()

        # Simulate connection and disconnection
        mock_websocket = Mock()
        # Make the mock websocket awaitable
        mock_websocket.accept = AsyncMock()
        player_id = "test_player"

        # Connect
        success = await connection_manager.connect_websocket(mock_websocket, player_id)
        assert success is True
        assert player_id in connection_manager.player_websockets

        # Disconnect
        await connection_manager.disconnect_websocket(player_id)
        assert player_id not in connection_manager.player_websockets
        assert len(connection_manager.active_websockets) == 0

    @pytest.mark.asyncio
    async def test_memory_monitoring_end_to_end(self):
        """Test end-to-end memory monitoring."""
        connection_manager = ConnectionManager()

        # Get initial stats
        initial_stats = connection_manager.get_memory_stats()
        initial_alerts = connection_manager.get_memory_alerts()

        # Add some data to trigger alerts - need multiple players to exceed thresholds
        for i in range(1001):
            connection_manager.connection_attempts[f"player{i}"] = [time.time()]
        for i in range(1001):
            connection_manager.pending_messages[f"player{i}"] = [{"timestamp": time.time()}]

        # Get updated stats and alerts
        updated_stats = connection_manager.get_memory_stats()
        updated_alerts = connection_manager.get_memory_alerts()

        # Check that data structures grew
        assert (
            updated_stats["data_structures"]["connection_attempts"]
            > initial_stats["data_structures"]["connection_attempts"]
        )
        assert (
            updated_stats["data_structures"]["pending_messages"] > initial_stats["data_structures"]["pending_messages"]
        )

        # Check that alerts were generated
        assert len(updated_alerts) > len(initial_alerts)

        # Add some old data that should be cleaned up
        connection_manager.connection_attempts["old_player"] = [time.time() - 4000]  # Old
        connection_manager.pending_messages["old_player"] = [{"timestamp": time.time() - 4000}]  # Old

        # Perform cleanup
        await connection_manager.force_cleanup()

        # Check that old data was cleaned up
        assert "old_player" not in connection_manager.connection_attempts
        assert "old_player" not in connection_manager.pending_messages
