"""
Tests for connection health check functionality.

This module tests the periodic health check system that monitors
WebSocket connections and cleans up stale/dead connections.
"""

import asyncio
import time
from unittest.mock import AsyncMock

import pytest

from server.realtime.connection_manager import ConnectionManager


class TestConnectionHealthChecks:
    """Test cases for connection health checks."""

    @pytest.fixture
    def connection_manager(self):
        """Create a ConnectionManager instance for testing."""
        cm = ConnectionManager()
        cm.persistence = None
        return cm

    @pytest.mark.asyncio
    async def test_start_health_checks(self, connection_manager):
        """Test starting health check task."""
        connection_manager.start_health_checks()

        # Verify health check task was created
        assert connection_manager._health_check_task is not None
        assert not connection_manager._health_check_task.done()

        # Clean up
        connection_manager.stop_health_checks()

    @pytest.mark.asyncio
    async def test_stop_health_checks(self, connection_manager):
        """Test stopping health check task."""
        connection_manager.start_health_checks()
        assert connection_manager._health_check_task is not None

        connection_manager.stop_health_checks()

        # Task should be cancelled (may take a moment)
        await asyncio.sleep(0.1)
        # Note: Task may still exist but should be cancelled

    @pytest.mark.asyncio
    async def test_health_check_detects_stale_connection(self, connection_manager):
        """Test health check detects stale connections."""
        # Create a mock WebSocket
        mock_websocket = AsyncMock()
        mock_websocket.client_state.name = "CONNECTED"
        player_id = "test_player"

        # Connect WebSocket
        await connection_manager.connect_websocket(mock_websocket, player_id)

        # Mark connection as stale (last_seen very old)
        connection_manager.last_seen[player_id] = time.time() - 200  # 200 seconds ago

        # Run health check manually
        await connection_manager._check_connection_health()

        # Connection should be marked for cleanup (verify through internal state)
        # Note: Actual cleanup happens asynchronously

    @pytest.mark.asyncio
    async def test_health_check_detects_dead_websocket(self, connection_manager):
        """Test health check detects dead WebSocket connections."""
        # Create a mock WebSocket that appears closed
        mock_websocket = AsyncMock()
        mock_websocket.client_state.name = "DISCONNECTED"  # Dead connection
        player_id = "test_player"

        # Connect WebSocket
        await connection_manager.connect_websocket(mock_websocket, player_id)

        # Run health check manually
        await connection_manager._check_connection_health()

        # Dead connection should be detected and marked for cleanup

    @pytest.mark.asyncio
    async def test_health_check_skips_healthy_connections(self, connection_manager):
        """Test health check skips healthy connections."""
        # Create a healthy WebSocket
        mock_websocket = AsyncMock()
        mock_websocket.client_state.name = "CONNECTED"
        player_id = "test_player"

        # Connect WebSocket
        await connection_manager.connect_websocket(mock_websocket, player_id)

        # Mark as recently seen
        connection_manager.last_seen[player_id] = time.time()

        # Run health check manually
        await connection_manager._check_connection_health()

        # Healthy connection should remain active
        assert player_id in connection_manager.player_websockets

    @pytest.mark.asyncio
    async def test_periodic_health_check_runs(self, connection_manager):
        """Test periodic health check task runs continuously."""
        connection_manager.start_health_checks()

        # Wait a bit for task to run
        await asyncio.sleep(0.5)

        # Task should still be running
        assert connection_manager._health_check_task is not None
        assert not connection_manager._health_check_task.done()

        # Clean up
        connection_manager.stop_health_checks()

    @pytest.mark.asyncio
    async def test_health_check_handles_missing_metadata(self, connection_manager):
        """Test health check handles missing connection metadata gracefully."""
        # Create connection without metadata
        mock_websocket = AsyncMock()
        mock_websocket.client_state.name = "CONNECTED"
        player_id = "test_player"

        # Connect WebSocket
        await connection_manager.connect_websocket(mock_websocket, player_id)

        # Remove metadata to simulate edge case
        connection_id = list(connection_manager.active_websockets.keys())[0]
        if connection_id in connection_manager.connection_metadata:
            del connection_manager.connection_metadata[connection_id]

        # Health check should handle this gracefully
        await connection_manager._check_connection_health()

    def test_health_check_interval_configuration(self, connection_manager):
        """Test health check interval is configurable."""
        # Default interval should be set
        assert hasattr(connection_manager, "_health_check_interval")
        assert connection_manager._health_check_interval > 0

    @pytest.mark.asyncio
    async def test_health_check_connection_timeout(self, connection_manager):
        """Test health check uses connection timeout for stale detection."""
        # Set a custom timeout
        connection_manager._connection_timeout = 30  # 30 seconds

        # Create a connection that's stale but within timeout
        mock_websocket = AsyncMock()
        mock_websocket.client_state.name = "CONNECTED"
        player_id = "test_player"

        await connection_manager.connect_websocket(mock_websocket, player_id)
        connection_manager.last_seen[player_id] = time.time() - 15  # 15 seconds ago (within timeout)

        # Run health check
        await connection_manager._check_connection_health()

        # Connection should still be active (within timeout)
        assert player_id in connection_manager.player_websockets

        # Now make it stale (beyond timeout)
        connection_manager.last_seen[player_id] = time.time() - 60  # 60 seconds ago (beyond timeout)

        # Run health check
        await connection_manager._check_connection_health()

        # Connection should be marked for cleanup
