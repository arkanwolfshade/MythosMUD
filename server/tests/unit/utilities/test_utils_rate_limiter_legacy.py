"""
Tests for utils.rate_limiter module.

This module tests the simple rate limiter used for API endpoints like
stats rolling and character creation.
"""

import time

import pytest

from server.exceptions import RateLimitError
from server.utils.rate_limiter import (
    RateLimiter,
    character_creation_limiter,
    stats_roll_limiter,
)


class TestRateLimiterInitialization:
    """Test rate limiter initialization."""

    def test_default_initialization(self):
        """Test rate limiter initializes with default values."""
        limiter = RateLimiter()

        assert limiter.max_requests == 10
        assert limiter.window_seconds == 60
        assert isinstance(limiter.requests, dict)

    def test_custom_initialization(self):
        """Test rate limiter initializes with custom values."""
        limiter = RateLimiter(max_requests=5, window_seconds=30)

        assert limiter.max_requests == 5
        assert limiter.window_seconds == 30


class TestRateLimitChecking:
    """Test rate limit checking functionality."""

    def test_check_rate_limit_first_request(self):
        """Test first request is always allowed."""
        limiter = RateLimiter(max_requests=5)

        result = limiter.check_rate_limit("user1")

        assert result is True
        assert len(limiter.requests["user1"]) == 1

    def test_check_rate_limit_within_limit(self):
        """Test requests within limit are allowed."""
        limiter = RateLimiter(max_requests=3)

        # Make 3 requests (all should succeed)
        assert limiter.check_rate_limit("user1") is True
        assert limiter.check_rate_limit("user1") is True
        assert limiter.check_rate_limit("user1") is True

        assert len(limiter.requests["user1"]) == 3

    def test_check_rate_limit_at_limit(self):
        """Test request at exactly the limit is denied."""
        limiter = RateLimiter(max_requests=3)

        # Make 3 requests (all should succeed)
        for _ in range(3):
            assert limiter.check_rate_limit("user1") is True

        # 4th request should fail
        assert limiter.check_rate_limit("user1") is False

    def test_check_rate_limit_old_requests_cleaned(self):
        """Test old requests are cleaned up from the window."""
        limiter = RateLimiter(max_requests=2, window_seconds=1)

        # Make 2 requests (fill the limit)
        limiter.check_rate_limit("user1")
        limiter.check_rate_limit("user1")

        # Wait for window to expire
        time.sleep(1.1)

        # New request should succeed (old ones cleaned up)
        assert limiter.check_rate_limit("user1") is True

    def test_check_rate_limit_multiple_users_independent(self):
        """Test rate limits are independent per user."""
        limiter = RateLimiter(max_requests=2)

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
        limiter = RateLimiter(max_requests=10, window_seconds=60)

        info = limiter.get_rate_limit_info("user1")

        assert info["attempts"] == 0
        assert info["max_attempts"] == 10
        assert info["window_seconds"] == 60
        assert info["attempts_remaining"] == 10
        assert info["reset_time"] == 0
        assert info["retry_after"] == 0

    def test_get_rate_limit_info_with_requests(self):
        """Test getting info with active requests."""
        limiter = RateLimiter(max_requests=10, window_seconds=60)

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
        limiter = RateLimiter(max_requests=2, window_seconds=10)

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
        limiter = RateLimiter(max_requests=5)

        # Should not raise exception
        limiter.enforce_rate_limit("user1")

    def test_enforce_rate_limit_raises_on_exceed(self):
        """Test enforce raises RateLimitError when limit exceeded."""
        limiter = RateLimiter(max_requests=2)

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
