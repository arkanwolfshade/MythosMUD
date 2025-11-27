"""
Tests for the rate limiter module.

This module tests the RateLimiter class which handles sliding window rate limiting
for chat channels to prevent spam and maintain chat quality.
"""

import time
from unittest.mock import Mock, patch

import pytest

from server.exceptions import RateLimitError
from server.services.rate_limiter import RateLimiter, rate_limiter
from server.utils.rate_limiter import (
    RateLimiter as UtilsRateLimiter,
)
from server.utils.rate_limiter import (
    character_creation_limiter,
    stats_roll_limiter,
)


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


# ============================================================================
# Tests merged from test_utils_rate_limiter_legacy.py
# ============================================================================


"""
Tests for utils.rate_limiter module.

This module tests the simple rate limiter used for API endpoints like
stats rolling and character creation.
"""


class TestRateLimiterInitialization:
    """Test rate limiter initialization."""

    def test_default_initialization(self):
        """Test rate limiter initializes with default values."""
        limiter = UtilsRateLimiter()

        assert limiter.max_requests == 10
        assert limiter.window_seconds == 60
        assert isinstance(limiter.requests, dict)

    def test_custom_initialization(self):
        """Test rate limiter initializes with custom values."""
        limiter = UtilsRateLimiter(max_requests=5, window_seconds=30)

        assert limiter.max_requests == 5
        assert limiter.window_seconds == 30


class TestRateLimitChecking:
    """Test rate limit checking functionality."""

    def test_check_rate_limit_first_request(self):
        """Test first request is always allowed."""
        limiter = UtilsRateLimiter(max_requests=5)

        result = limiter.check_rate_limit("user1")

        assert result is True
        assert len(limiter.requests["user1"]) == 1

    def test_check_rate_limit_within_limit(self):
        """Test requests within limit are allowed."""
        limiter = UtilsRateLimiter(max_requests=3)

        # Make 3 requests (all should succeed)
        assert limiter.check_rate_limit("user1") is True
        assert limiter.check_rate_limit("user1") is True
        assert limiter.check_rate_limit("user1") is True

        assert len(limiter.requests["user1"]) == 3

    def test_check_rate_limit_at_limit(self):
        """Test request at exactly the limit is denied."""
        limiter = UtilsRateLimiter(max_requests=3)

        # Make 3 requests (all should succeed)
        for _ in range(3):
            assert limiter.check_rate_limit("user1") is True

        # 4th request should fail
        assert limiter.check_rate_limit("user1") is False

    def test_check_rate_limit_old_requests_cleaned(self):
        """Test old requests are cleaned up from the window."""
        limiter = UtilsRateLimiter(max_requests=2, window_seconds=1)

        # Make 2 requests (fill the limit)
        limiter.check_rate_limit("user1")
        limiter.check_rate_limit("user1")

        # Wait for window to expire (use 1.2 seconds to account for timing imprecision)
        time.sleep(1.2)

        # New request should succeed (old ones cleaned up)
        # The cleanup happens inside check_rate_limit, so this should work
        assert limiter.check_rate_limit("user1") is True

    def test_check_rate_limit_multiple_users_independent(self):
        """Test rate limits are independent per user."""
        limiter = UtilsRateLimiter(max_requests=2)

        # Fill limit for user1
        limiter.check_rate_limit("user1")
        limiter.check_rate_limit("user1")

        # user1 should be limited
        assert limiter.check_rate_limit("user1") is False

        # user2 should not be affected
        assert limiter.check_rate_limit("user2") is True


class TestGetRateLimitInfo:
    """Test rate limit information retrieval."""

    def test_get_rate_limit_info_no_requests(self):
        """Test getting info when no requests made."""
        limiter = UtilsRateLimiter(max_requests=10, window_seconds=60)

        info = limiter.get_rate_limit_info("user1")

        assert info["attempts"] == 0
        assert info["max_attempts"] == 10
        assert info["window_seconds"] == 60
        assert info["attempts_remaining"] == 10
        assert info["reset_time"] == 0
        assert info["retry_after"] == 0

    def test_get_rate_limit_info_with_requests(self):
        """Test getting info with active requests."""
        limiter = UtilsRateLimiter(max_requests=10, window_seconds=60)

        # Make some requests
        limiter.check_rate_limit("user1")
        limiter.check_rate_limit("user1")
        limiter.check_rate_limit("user1")

        info = limiter.get_rate_limit_info("user1")

        assert info["attempts"] == 3
        assert info["max_attempts"] == 10
        assert info["attempts_remaining"] == 7
        assert info["reset_time"] > 0

    def test_get_rate_limit_info_retry_after(self):
        """Test retry_after calculation."""
        limiter = UtilsRateLimiter(max_requests=2, window_seconds=10)

        # Fill the limit
        limiter.check_rate_limit("user1")
        limiter.check_rate_limit("user1")

        info = limiter.get_rate_limit_info("user1")

        # retry_after should be positive and less than window_seconds
        assert 0 <= info["retry_after"] <= 10


class TestEnforceRateLimit:
    """Test rate limit enforcement."""

    def test_enforce_rate_limit_allows_request(self):
        """Test enforce allows request when within limit."""
        limiter = UtilsRateLimiter(max_requests=5)

        # Should not raise exception
        limiter.enforce_rate_limit("user1")

    def test_enforce_rate_limit_raises_on_exceed(self):
        """Test enforce raises RateLimitError when limit exceeded."""
        limiter = UtilsRateLimiter(max_requests=2)

        # Fill the limit
        limiter.enforce_rate_limit("user1")
        limiter.enforce_rate_limit("user1")

        # Next request should raise exception
        with pytest.raises(RateLimitError) as exc_info:
            limiter.enforce_rate_limit("user1")

        error = exc_info.value
        assert "Rate limit exceeded" in str(error)
        assert error.limit_type == "api_endpoint"
        assert error.retry_after >= 0


class TestGlobalLimiters:
    """Test global limiter instances."""

    def test_stats_roll_limiter_exists(self):
        """Test stats_roll_limiter is configured correctly."""
        assert stats_roll_limiter.max_requests == 10
        assert stats_roll_limiter.window_seconds == 60

    def test_character_creation_limiter_exists(self):
        """Test character_creation_limiter is configured correctly."""
        assert character_creation_limiter.max_requests == 5
        assert character_creation_limiter.window_seconds == 300
