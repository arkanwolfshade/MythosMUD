"""
Tests for the rate limiter module.

This module tests the RateLimiter class which handles sliding window rate limiting
for chat channels to prevent spam and maintain chat quality.
"""

import time
from unittest.mock import Mock, patch

from ..services.rate_limiter import RateLimiter, rate_limiter


class TestRateLimiter:
    """Test cases for RateLimiter class."""

    def setup_method(self):
        """Set up test fixtures."""
        # Mock the config loader to return test configuration
        self.mock_config = {
            "chat": {
                "rate_limiting": {
                    "enabled": True,
                    "limits": {
                        "global": 10,
                        "local": 20,
                        "say": 15,
                        "party": 30,
                        "whisper": 5,
                        "system": 100,
                        "admin": 50,
                    },
                }
            }
        }

        # Create the rate limiter instance
        with patch("server.services.rate_limiter.get_config", return_value=self.mock_config):
            self.rate_limiter = RateLimiter()

        # Mock the chat logger
        self.rate_limiter.chat_logger = Mock()

        # Test data
        self.player_id = "test_player_123"
        self.player_name = "TestPlayer"
        self.channel = "say"

    def test_rate_limiter_initialization(self):
        """Test RateLimiter initialization."""
        assert self.rate_limiter.enabled is True
        assert self.rate_limiter.window_size == 60
        assert self.rate_limiter.limits["global"] == 10
        assert self.rate_limiter.limits["local"] == 20
        assert self.rate_limiter.limits["say"] == 15
        assert self.rate_limiter.limits["party"] == 30
        assert self.rate_limiter.limits["whisper"] == 5
        assert self.rate_limiter.limits["system"] == 100
        assert self.rate_limiter.limits["admin"] == 50

    def test_rate_limiter_initialization_with_defaults(self):
        """Test RateLimiter initialization with default limits."""
        # Mock config without rate limiting section
        mock_config = {"chat": {}}

        with patch("server.services.rate_limiter.get_config", return_value=mock_config):
            rate_limiter = RateLimiter()

        # Should use default limits
        assert rate_limiter.limits["global"] == 10
        assert rate_limiter.limits["local"] == 20
        assert rate_limiter.limits["say"] == 15
        assert rate_limiter.limits["party"] == 30
        assert rate_limiter.limits["whisper"] == 5
        assert rate_limiter.limits["system"] == 100
        assert rate_limiter.limits["admin"] == 50

    def test_rate_limiter_initialization_disabled(self):
        """Test RateLimiter initialization when disabled."""
        mock_config = {"chat": {"rate_limiting": {"enabled": False, "limits": {"global": 10}}}}

        with patch("server.services.rate_limiter.get_config", return_value=mock_config):
            rate_limiter = RateLimiter()

        assert rate_limiter.enabled is False

    def test_set_limit(self):
        """Test setting a custom rate limit."""
        # Execute
        self.rate_limiter.set_limit("custom_channel", 25)

        # Verify
        assert self.rate_limiter.limits["custom_channel"] == 25

    def test_get_limit_existing(self):
        """Test getting an existing rate limit."""
        # Execute
        limit = self.rate_limiter.get_limit("say")

        # Verify
        assert limit == 15

    def test_get_limit_nonexistent(self):
        """Test getting a rate limit for a non-existent channel."""
        # Execute
        limit = self.rate_limiter.get_limit("nonexistent_channel")

        # Verify - should return default
        assert limit == 10

    def test_cleanup_old_entries(self):
        """Test cleanup of old entries."""
        # Setup with old timestamps
        old_time = time.time() - 120  # 2 minutes ago
        current_time = time.time()

        from collections import deque

        self.rate_limiter.windows[self.player_id][self.channel] = deque(
            [
                old_time,  # Should be removed
                current_time,  # Should remain
            ]
        )

        # Execute
        self.rate_limiter._cleanup_old_entries(self.player_id, self.channel)

        # Verify
        window = self.rate_limiter.windows[self.player_id][self.channel]
        assert len(window) == 1
        assert window[0] == current_time

    def test_check_rate_limit_disabled(self):
        """Test rate limit checking when disabled."""
        # Setup disabled rate limiter
        self.rate_limiter.enabled = False

        # Execute
        result = self.rate_limiter.check_rate_limit(self.player_id, self.channel, self.player_name)

        # Verify
        assert result is True

    def test_check_rate_limit_within_limits(self):
        """Test rate limit checking when within limits."""
        # Setup - no messages recorded yet
        assert len(self.rate_limiter.windows[self.player_id][self.channel]) == 0

        # Execute
        result = self.rate_limiter.check_rate_limit(self.player_id, self.channel, self.player_name)

        # Verify
        assert result is True

    def test_check_rate_limit_at_limit(self):
        """Test rate limit checking when at the limit."""
        # Setup - record messages up to the limit
        limit = self.rate_limiter.get_limit(self.channel)
        current_time = time.time()

        for _ in range(limit):
            self.rate_limiter.windows[self.player_id][self.channel].append(current_time)

        # Execute
        result = self.rate_limiter.check_rate_limit(self.player_id, self.channel, self.player_name)

        # Verify
        assert result is False

    def test_check_rate_limit_exceeded(self):
        """Test rate limit checking when exceeded."""
        # Setup - record more messages than the limit
        limit = self.rate_limiter.get_limit(self.channel)
        current_time = time.time()

        for _ in range(limit + 1):
            self.rate_limiter.windows[self.player_id][self.channel].append(current_time)

        # Execute
        result = self.rate_limiter.check_rate_limit(self.player_id, self.channel, self.player_name)

        # Verify
        assert result is False

        # Verify logging was called
        self.rate_limiter.chat_logger.log_rate_limit_violation.assert_called_once()

    def test_check_rate_limit_exception(self):
        """Test rate limit checking when an exception occurs."""
        # Setup - cause an exception by making windows access fail
        self.rate_limiter.windows = None

        # Execute - should not raise exception and should return True (fail open)
        result = self.rate_limiter.check_rate_limit(self.player_id, self.channel, self.player_name)

        # Verify
        assert result is True

    def test_record_message_success(self):
        """Test successful message recording."""
        # Setup
        initial_count = len(self.rate_limiter.windows[self.player_id][self.channel])

        # Execute
        self.rate_limiter.record_message(self.player_id, self.channel, self.player_name)

        # Verify
        final_count = len(self.rate_limiter.windows[self.player_id][self.channel])
        assert final_count == initial_count + 1

        # Verify the timestamp is recent
        timestamp = self.rate_limiter.windows[self.player_id][self.channel][-1]
        assert abs(timestamp - time.time()) < 1  # Within 1 second

    def test_record_message_exception(self):
        """Test message recording when an exception occurs."""
        # Setup - cause an exception
        self.rate_limiter.windows = None

        # Execute - should not raise exception
        self.rate_limiter.record_message(self.player_id, self.channel, self.player_name)

    def test_get_player_stats(self):
        """Test getting player statistics."""
        # Setup - record some messages
        self.rate_limiter.record_message(self.player_id, "say", self.player_name)
        self.rate_limiter.record_message(self.player_id, "say", self.player_name)
        self.rate_limiter.record_message(self.player_id, "global", self.player_name)

        # Execute
        stats = self.rate_limiter.get_player_stats(self.player_id)

        # Verify
        assert "say" in stats
        assert "global" in stats
        assert "local" in stats

        # Verify say channel stats
        say_stats = stats["say"]
        assert say_stats["current_count"] == 2
        assert say_stats["limit"] == 15
        assert say_stats["remaining"] == 13
        assert say_stats["percentage_used"] == (2 / 15 * 100)

        # Verify global channel stats
        global_stats = stats["global"]
        assert global_stats["current_count"] == 1
        assert global_stats["limit"] == 10
        assert global_stats["remaining"] == 9

    def test_get_player_stats_empty(self):
        """Test getting player statistics when no messages recorded."""
        # Execute
        stats = self.rate_limiter.get_player_stats(self.player_id)

        # Verify
        assert "say" in stats
        say_stats = stats["say"]
        assert say_stats["current_count"] == 0
        assert say_stats["limit"] == 15
        assert say_stats["remaining"] == 15
        assert say_stats["percentage_used"] == 0

    def test_reset_player_limits_specific_channel(self):
        """Test resetting player limits for a specific channel."""
        # Setup - record some messages
        self.rate_limiter.record_message(self.player_id, "say", self.player_name)
        self.rate_limiter.record_message(self.player_id, "global", self.player_name)

        # Execute
        self.rate_limiter.reset_player_limits(self.player_id, "say")

        # Verify
        assert len(self.rate_limiter.windows[self.player_id]["say"]) == 0
        assert len(self.rate_limiter.windows[self.player_id]["global"]) == 1

    def test_reset_player_limits_all_channels(self):
        """Test resetting player limits for all channels."""
        # Setup - record some messages
        self.rate_limiter.record_message(self.player_id, "say", self.player_name)
        self.rate_limiter.record_message(self.player_id, "global", self.player_name)

        # Execute
        self.rate_limiter.reset_player_limits(self.player_id)

        # Verify
        assert len(self.rate_limiter.windows[self.player_id]["say"]) == 0
        assert len(self.rate_limiter.windows[self.player_id]["global"]) == 0

    def test_reset_player_limits_nonexistent_player(self):
        """Test resetting limits for a non-existent player."""
        # Execute - should not raise exception
        self.rate_limiter.reset_player_limits("nonexistent_player")

    def test_reset_player_limits_exception(self):
        """Test resetting limits when an exception occurs."""
        # Setup - cause an exception
        self.rate_limiter.windows = None

        # Execute - should not raise exception
        self.rate_limiter.reset_player_limits(self.player_id, "say")

    def test_get_system_stats(self):
        """Test getting system statistics."""
        # Setup - record messages for multiple players
        self.rate_limiter.record_message("player1", "say", "Player1")
        self.rate_limiter.record_message("player1", "say", "Player1")
        self.rate_limiter.record_message("player2", "global", "Player2")

        # Execute
        stats = self.rate_limiter.get_system_stats()

        # Verify
        assert stats["total_players"] == 2
        assert stats["active_players"] == 2
        assert stats["total_channels"] == 7  # All configured channels
        assert stats["total_messages_in_window"] == 3
        assert stats["window_size_seconds"] == 60
        assert "limits" in stats

    def test_get_system_stats_empty(self):
        """Test getting system statistics when no activity."""
        # Execute
        stats = self.rate_limiter.get_system_stats()

        # Verify
        assert stats["total_players"] == 0
        assert stats["active_players"] == 0
        assert stats["total_channels"] == 7
        assert stats["total_messages_in_window"] == 0

    def test_get_system_stats_with_old_entries(self):
        """Test getting system statistics with old entries that should be cleaned up."""
        # Setup - add old timestamps
        old_time = time.time() - 120  # 2 minutes ago
        current_time = time.time()

        from collections import deque

        self.rate_limiter.windows["player1"]["say"] = deque([old_time, current_time])
        self.rate_limiter.windows["player2"]["global"] = deque([old_time])  # Only old entries

        # Execute
        stats = self.rate_limiter.get_system_stats()

        # Verify
        assert stats["total_players"] == 2
        assert stats["active_players"] == 1  # Only player1 has recent activity
        assert stats["total_messages_in_window"] == 1  # Only current_time entry

    def test_get_system_stats_exception(self):
        """Test getting system statistics when an exception occurs."""
        # Setup - cause an exception
        self.rate_limiter.windows = None

        # Execute
        stats = self.rate_limiter.get_system_stats()

        # Verify - should return empty dict
        assert stats == {}

    def test_is_player_rate_limited_true(self):
        """Test checking if player is rate limited (true case)."""
        # Setup - exceed the limit
        limit = self.rate_limiter.get_limit(self.channel)
        current_time = time.time()

        for _ in range(limit + 1):
            self.rate_limiter.windows[self.player_id][self.channel].append(current_time)

        # Execute
        result = self.rate_limiter.is_player_rate_limited(self.player_id, self.channel)

        # Verify
        assert result is True

    def test_is_player_rate_limited_false(self):
        """Test checking if player is rate limited (false case)."""
        # Setup - within limits
        self.rate_limiter.record_message(self.player_id, self.channel, self.player_name)

        # Execute
        result = self.rate_limiter.is_player_rate_limited(self.player_id, self.channel)

        # Verify
        assert result is False

    def test_get_remaining_messages(self):
        """Test getting remaining messages count."""
        # Setup - record some messages
        self.rate_limiter.record_message(self.player_id, self.channel, self.player_name)
        self.rate_limiter.record_message(self.player_id, self.channel, self.player_name)

        # Execute
        remaining = self.rate_limiter.get_remaining_messages(self.player_id, self.channel)

        # Verify
        limit = self.rate_limiter.get_limit(self.channel)
        assert remaining == limit - 2

    def test_get_remaining_messages_zero(self):
        """Test getting remaining messages when at limit."""
        # Setup - reach the limit
        limit = self.rate_limiter.get_limit(self.channel)
        current_time = time.time()

        for _ in range(limit):
            self.rate_limiter.windows[self.player_id][self.channel].append(current_time)

        # Execute
        remaining = self.rate_limiter.get_remaining_messages(self.player_id, self.channel)

        # Verify
        assert remaining == 0

    def test_get_remaining_messages_exception(self):
        """Test getting remaining messages when an exception occurs."""
        # Setup - cause an exception
        self.rate_limiter.windows = None

        # Execute
        remaining = self.rate_limiter.get_remaining_messages(self.player_id, self.channel)

        # Verify - should return 0 on error
        assert remaining == 0

    def test_sliding_window_behavior(self):
        """Test sliding window behavior over time."""
        # Setup - record messages at different times
        base_time = time.time()

        from collections import deque

        # Add messages at different times
        self.rate_limiter.windows[self.player_id][self.channel] = deque(
            [
                base_time - 30,  # 30 seconds ago
                base_time - 20,  # 20 seconds ago
                base_time - 10,  # 10 seconds ago
                base_time,  # Now
            ]
        )

        # Mock current time to be 70 seconds after base_time
        with patch("time.time", return_value=base_time + 70):
            # Execute
            result = self.rate_limiter.check_rate_limit(self.player_id, self.channel, self.player_name)

            # Verify - all messages should be cleaned up (older than 60 second window)
            assert result is True
            window = self.rate_limiter.windows[self.player_id][self.channel]
            assert len(window) == 0

    def test_multiple_channels_independence(self):
        """Test that rate limits are independent across channels."""
        # Setup - exceed limit on one channel
        limit = self.rate_limiter.get_limit("say")
        current_time = time.time()

        for _ in range(limit + 1):
            self.rate_limiter.windows[self.player_id]["say"].append(current_time)

        # Execute - check both channels
        say_limited = self.rate_limiter.check_rate_limit(self.player_id, "say", self.player_name)
        global_allowed = self.rate_limiter.check_rate_limit(self.player_id, "global", self.player_name)

        # Verify
        assert say_limited is False
        assert global_allowed is True

    def test_multiple_players_independence(self):
        """Test that rate limits are independent across players."""
        # Setup - exceed limit for one player
        limit = self.rate_limiter.get_limit(self.channel)
        current_time = time.time()

        for _ in range(limit + 1):
            self.rate_limiter.windows["player1"][self.channel].append(current_time)

        # Execute - check both players
        player1_limited = self.rate_limiter.check_rate_limit("player1", self.channel, "Player1")
        player2_allowed = self.rate_limiter.check_rate_limit("player2", self.channel, "Player2")

        # Verify
        assert player1_limited is False
        assert player2_allowed is True

    def test_edge_case_zero_limit(self):
        """Test behavior with zero limit."""
        # Setup - set limit to zero
        self.rate_limiter.set_limit("zero_channel", 0)

        # Execute
        result = self.rate_limiter.check_rate_limit(self.player_id, "zero_channel", self.player_name)

        # Verify - should be rate limited
        assert result is False

    def test_edge_case_negative_limit(self):
        """Test behavior with negative limit."""
        # Setup - set limit to negative
        self.rate_limiter.set_limit("negative_channel", -5)

        # Execute
        result = self.rate_limiter.check_rate_limit(self.player_id, "negative_channel", self.player_name)

        # Verify - should be rate limited
        assert result is False

    def test_percentage_used_calculation(self):
        """Test percentage used calculation in player stats."""
        # Setup - use exactly half the limit
        limit = self.rate_limiter.get_limit(self.channel)
        current_time = time.time()

        for _ in range(limit // 2):
            self.rate_limiter.windows[self.player_id][self.channel].append(current_time)

        # Execute
        stats = self.rate_limiter.get_player_stats(self.player_id)

        # Verify
        channel_stats = stats[self.channel]
        expected_percentage = (limit // 2) / limit * 100
        assert channel_stats["percentage_used"] == expected_percentage

    def test_percentage_used_zero_limit(self):
        """Test percentage used calculation with zero limit."""
        # Setup - set limit to zero
        self.rate_limiter.set_limit("zero_channel", 0)

        # Execute
        stats = self.rate_limiter.get_player_stats(self.player_id)

        # Verify
        channel_stats = stats["zero_channel"]
        assert channel_stats["percentage_used"] == 0


class TestGlobalRateLimiter:
    """Test cases for the global rate limiter instance."""

    def test_global_rate_limiter_instance(self):
        """Test that the global rate limiter instance exists."""
        assert isinstance(rate_limiter, RateLimiter)
        assert hasattr(rate_limiter, "enabled")
        assert hasattr(rate_limiter, "limits")
        assert hasattr(rate_limiter, "windows")
        assert hasattr(rate_limiter, "window_size")
