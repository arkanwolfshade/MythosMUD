"""
Tests for message rate limiting functionality in RateLimiter.

This module tests the per-connection message rate limiting features
that prevent DoS attacks and resource exhaustion.
"""

import time
from unittest.mock import patch

from server.realtime.rate_limiter import RateLimiter


class TestMessageRateLimiting:
    """Test cases for message rate limiting."""

    def setup_method(self):
        """Set up test fixtures."""
        self.rate_limiter = RateLimiter()
        self.connection_id = "test_connection_123"

    def test_message_rate_limit_allows_under_limit(self):
        """Test message rate limit allows messages under the limit."""
        # Send messages up to the limit
        for _ in range(50):  # Well under 100 messages/minute limit
            result = self.rate_limiter.check_message_rate_limit(self.connection_id)
            assert result is True

    def test_message_rate_limit_blocks_over_limit(self):
        """Test message rate limit blocks messages over the limit."""
        # Send exactly the limit
        for _ in range(100):
            result = self.rate_limiter.check_message_rate_limit(self.connection_id)
            assert result is True

        # Next message should be blocked
        result = self.rate_limiter.check_message_rate_limit(self.connection_id)
        assert result is False

    def test_message_rate_limit_resets_after_window(self):
        """Test message rate limit resets after time window."""
        # Capture current time before patching
        base_time = time.time()

        # Send messages up to limit
        for _ in range(100):
            self.rate_limiter.check_message_rate_limit(self.connection_id)

        # Should be blocked
        assert self.rate_limiter.check_message_rate_limit(self.connection_id) is False

        # Fast-forward time (mock time.time)
        with patch("server.realtime.rate_limiter.time.time") as mock_time:
            # Set time to be after the window (61 seconds later)
            mock_time.return_value = base_time + 61

            # Should now be allowed again
            result = self.rate_limiter.check_message_rate_limit(self.connection_id)
            assert result is True

    def test_message_rate_limit_info(self):
        """Test getting message rate limit information."""
        # Send some messages
        for _ in range(50):
            self.rate_limiter.check_message_rate_limit(self.connection_id)

        info = self.rate_limiter.get_message_rate_limit_info(self.connection_id)

        assert "max_attempts" in info
        assert "current_attempts" in info
        assert "reset_time" in info
        assert info["max_attempts"] == 100
        assert info["current_attempts"] == 50

    def test_message_rate_limit_info_after_limit_exceeded(self):
        """Test rate limit info when limit is exceeded."""
        # Send messages up to and over limit
        for _ in range(101):
            self.rate_limiter.check_message_rate_limit(self.connection_id)

        info = self.rate_limiter.get_message_rate_limit_info(self.connection_id)

        assert info["current_attempts"] >= 100
        assert info["max_attempts"] == 100

    def test_remove_connection_message_data(self):
        """Test removing message rate limit data for a connection."""
        # Send some messages
        for _ in range(50):
            self.rate_limiter.check_message_rate_limit(self.connection_id)

        # Verify data exists
        info = self.rate_limiter.get_message_rate_limit_info(self.connection_id)
        assert info["current_attempts"] == 50

        # Remove data
        self.rate_limiter.remove_connection_message_data(self.connection_id)

        # Verify data is cleared
        info = self.rate_limiter.get_message_rate_limit_info(self.connection_id)
        assert info["current_attempts"] == 0

    def test_multiple_connections_independent_limits(self):
        """Test that different connections have independent rate limits."""
        connection1 = "connection_1"
        connection2 = "connection_2"

        # Send messages up to limit for connection1
        for _ in range(100):
            self.rate_limiter.check_message_rate_limit(connection1)

        # connection1 should be blocked
        assert self.rate_limiter.check_message_rate_limit(connection1) is False

        # connection2 should still be allowed
        assert self.rate_limiter.check_message_rate_limit(connection2) is True

    def test_cleanup_old_message_attempts(self):
        """Test cleanup of old message attempts."""
        # Capture current time before patching
        base_time = time.time()

        # Send messages
        for _ in range(50):
            self.rate_limiter.check_message_rate_limit(self.connection_id)

        # Fast-forward time to be after window
        with patch("server.realtime.rate_limiter.time.time") as mock_time:
            mock_time.return_value = base_time + 61

            # Cleanup old attempts
            self.rate_limiter.cleanup_old_message_attempts()

            # Verify attempts were cleaned up
            info = self.rate_limiter.get_message_rate_limit_info(self.connection_id)
            assert info["current_attempts"] == 0

    def test_message_rate_limit_with_custom_limits(self):
        """Test message rate limiting with custom limits."""
        rate_limiter = RateLimiter(max_messages_per_minute=10, message_window=60)

        # Send messages up to custom limit
        for _ in range(10):
            result = rate_limiter.check_message_rate_limit(self.connection_id)
            assert result is True

        # Next message should be blocked
        result = rate_limiter.check_message_rate_limit(self.connection_id)
        assert result is False
