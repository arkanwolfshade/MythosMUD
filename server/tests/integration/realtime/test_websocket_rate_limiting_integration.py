"""
Integration tests for WebSocket rate limiting enforcement.

This module tests end-to-end WebSocket flows with rate limiting,
ensuring that rate limits are properly enforced during real connections.
"""

import json
import time
from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.realtime.connection_manager import ConnectionManager

pytestmark = pytest.mark.integration


class TestWebSocketRateLimitingIntegration:
    """Test WebSocket rate limiting in integration scenarios."""

    @pytest.fixture
    def connection_manager(self):
        """Create a ConnectionManager instance for testing."""
        cm = ConnectionManager()
        cm.persistence = None
        return cm

    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock()
        websocket.send_json = AsyncMock()
        websocket.receive_text = AsyncMock()
        websocket.accept = AsyncMock()
        websocket.client_state.name = "CONNECTED"
        websocket.state = {}
        return websocket

    @pytest.fixture
    def mock_player(self):
        """Create a mock player for testing."""
        player = Mock()
        player.player_id = "test_player_123"
        player.name = "TestPlayer"
        player.current_room_id = "test_room_001"
        player.get_stats = Mock(return_value={"health": 100, "level": 1})
        return player

    @pytest.mark.asyncio
    async def test_message_rate_limit_enforced_during_connection(self, connection_manager, mock_websocket, mock_player):
        """Test that message rate limits are enforced during active WebSocket connection."""
        # Setup
        connection_manager._get_player = AsyncMock(return_value=mock_player)
        connection_manager.persistence = Mock()
        connection_manager.persistence.get_room = AsyncMock(return_value=None)

        # Connect WebSocket
        await connection_manager.connect_websocket(mock_websocket, mock_player.player_id)
        connection_id = connection_manager.get_connection_id_from_websocket(mock_websocket)

        # Send messages up to the limit
        for _ in range(100):
            result = connection_manager.rate_limiter.check_message_rate_limit(connection_id)
            assert result is True

        # Next message should be blocked
        result = connection_manager.rate_limiter.check_message_rate_limit(connection_id)
        assert result is False, "Message 101 should be blocked"

    @pytest.mark.asyncio
    async def test_rate_limit_reset_after_window(self, connection_manager, mock_websocket, mock_player):
        """Test that rate limit resets after time window expires."""
        # Setup
        connection_manager._get_player = AsyncMock(return_value=mock_player)
        await connection_manager.connect_websocket(mock_websocket, mock_player.player_id)
        connection_id = connection_manager.get_connection_id_from_websocket(mock_websocket)

        # Send messages up to limit
        for _ in range(100):
            connection_manager.rate_limiter.check_message_rate_limit(connection_id)

        # Should be blocked
        assert connection_manager.rate_limiter.check_message_rate_limit(connection_id) is False

        # Fast-forward time - need to ensure mock returns a numeric value
        future_time = time.time() + 61  # After 60-second window
        with patch("server.realtime.rate_limiter.time.time", return_value=future_time):
            # Should be allowed again (all old attempts are outside the window now)
            result = connection_manager.rate_limiter.check_message_rate_limit(connection_id)
            assert result is True

    @pytest.mark.asyncio
    async def test_multiple_connections_independent_limits(self, connection_manager, mock_player):
        """Test that different WebSocket connections have independent rate limits."""
        # Create two WebSocket connections
        websocket1 = AsyncMock()
        websocket1.accept = AsyncMock()
        websocket1.client_state.name = "CONNECTED"
        websocket1.state = {}

        websocket2 = AsyncMock()
        websocket2.accept = AsyncMock()
        websocket2.client_state.name = "CONNECTED"
        websocket2.state = {}

        connection_manager._get_player = AsyncMock(return_value=mock_player)

        # Connect both
        await connection_manager.connect_websocket(websocket1, mock_player.player_id)
        await connection_manager.connect_websocket(websocket2, mock_player.player_id)

        connection_id1 = connection_manager.get_connection_id_from_websocket(websocket1)
        connection_id2 = connection_manager.get_connection_id_from_websocket(websocket2)

        # Send messages up to limit for connection1
        for _ in range(100):
            connection_manager.rate_limiter.check_message_rate_limit(connection_id1)

        # Connection1 should be blocked
        assert connection_manager.rate_limiter.check_message_rate_limit(connection_id1) is False

        # Connection2 should still be allowed
        assert connection_manager.rate_limiter.check_message_rate_limit(connection_id2) is True

    @pytest.mark.asyncio
    async def test_rate_limit_cleanup_on_disconnect(self, connection_manager, mock_websocket, mock_player):
        """Test that rate limit data is cleaned up on disconnect."""
        # Setup
        connection_manager._get_player = AsyncMock(return_value=mock_player)
        await connection_manager.connect_websocket(mock_websocket, mock_player.player_id)
        connection_id = connection_manager.get_connection_id_from_websocket(mock_websocket)

        # Send some messages
        for _ in range(50):
            connection_manager.rate_limiter.check_message_rate_limit(connection_id)

        # Verify data exists
        info = connection_manager.rate_limiter.get_message_rate_limit_info(connection_id)
        assert info["attempts"] == 50

        # Disconnect
        await connection_manager.disconnect_websocket(mock_player.player_id)

        # Rate limit data should be cleaned up
        info = connection_manager.rate_limiter.get_message_rate_limit_info(connection_id)
        assert info["attempts"] == 0

    @pytest.mark.asyncio
    async def test_message_validation_with_rate_limiting(self, connection_manager, mock_websocket, mock_player):
        """Test that message validation and rate limiting work together."""
        from server.realtime.message_validator import get_message_validator

        validator = get_message_validator()
        connection_manager._get_player = AsyncMock(return_value=mock_player)
        await connection_manager.connect_websocket(mock_websocket, mock_player.player_id)
        connection_id = connection_manager.get_connection_id_from_websocket(mock_websocket)

        # Valid message should pass both validation and rate limiting
        valid_message = {
            "message": json.dumps({"type": "chat", "command": "say hello"}),
            "timestamp": int(time.time() * 1000),
        }
        data = json.dumps(valid_message)

        # Should pass validation
        parsed = validator.parse_and_validate(data, mock_player.player_id)
        assert parsed == {"type": "chat", "command": "say hello"}

        # Should pass rate limiting
        assert connection_manager.rate_limiter.check_message_rate_limit(connection_id) is True

    @pytest.mark.asyncio
    async def test_rate_limit_error_response_format(self, connection_manager, mock_websocket, mock_player):
        """Test that rate limit errors return proper error response format."""
        connection_manager._get_player = AsyncMock(return_value=mock_player)
        await connection_manager.connect_websocket(mock_websocket, mock_player.player_id)
        connection_id = connection_manager.get_connection_id_from_websocket(mock_websocket)

        # Exceed rate limit
        for _ in range(101):
            connection_manager.rate_limiter.check_message_rate_limit(connection_id)

        # Get rate limit info
        info = connection_manager.rate_limiter.get_message_rate_limit_info(connection_id)

        # Verify info structure
        assert "max_attempts" in info
        assert "attempts" in info
        assert "reset_time" in info
        assert info["max_attempts"] == 100
        assert info["attempts"] >= 100
