"""
Unit tests for rate limiting utilities.

Tests the simple in-memory rate limiter for API endpoints.
"""

import time
from unittest.mock import patch

import pytest

from server.exceptions import RateLimitError
from server.utils.rate_limiter import RateLimiter, character_creation_limiter, stats_roll_limiter


@pytest.fixture
def rate_limiter():
    """Create a RateLimiter instance for testing."""
    return RateLimiter(max_requests=5, window_seconds=60)


def test_rate_limiter_initialization(rate_limiter):
    """Test RateLimiter initializes correctly."""
    assert rate_limiter.max_requests == 5
    assert rate_limiter.window_seconds == 60
    assert len(rate_limiter.requests) == 0


def test_check_rate_limit_first_request(rate_limiter):
    """Test check_rate_limit allows first request."""
    result = rate_limiter.check_rate_limit("user1")
    
    assert result is True
    assert len(rate_limiter.requests["user1"]) == 1


def test_check_rate_limit_multiple_requests(rate_limiter):
    """Test check_rate_limit allows multiple requests within limit."""
    for i in range(5):
        result = rate_limiter.check_rate_limit("user1")
        assert result is True
    
    assert len(rate_limiter.requests["user1"]) == 5


def test_check_rate_limit_exceeds_limit(rate_limiter):
    """Test check_rate_limit returns False when limit exceeded."""
    # Make 5 requests (at the limit)
    for _ in range(5):
        rate_limiter.check_rate_limit("user1")
    
    # 6th request should be denied and NOT added
    result = rate_limiter.check_rate_limit("user1")
    
    assert result is False
    assert len(rate_limiter.requests["user1"]) == 5  # Not added when limit exceeded


def test_check_rate_limit_different_users(rate_limiter):
    """Test check_rate_limit tracks different users separately."""
    rate_limiter.check_rate_limit("user1")
    rate_limiter.check_rate_limit("user2")
    
    assert len(rate_limiter.requests["user1"]) == 1
    assert len(rate_limiter.requests["user2"]) == 1


def test_check_rate_limit_removes_old_requests(rate_limiter):
    """Test check_rate_limit removes requests outside the window."""
    # Make requests at different times
    with patch("time.time", return_value=1000.0):
        rate_limiter.check_rate_limit("user1")
        rate_limiter.check_rate_limit("user1")
    
    # Advance time beyond window
    with patch("time.time", return_value=1070.0):  # 70 seconds later
        # Old requests should be removed
        result = rate_limiter.check_rate_limit("user1")
        assert result is True
        # Should only have the new request
        assert len(rate_limiter.requests["user1"]) == 1


def test_get_rate_limit_info_no_requests(rate_limiter):
    """Test get_rate_limit_info returns correct info for no requests."""
    info = rate_limiter.get_rate_limit_info("user1")
    
    assert info["attempts"] == 0
    assert info["max_attempts"] == 5
    assert info["window_seconds"] == 60
    assert info["attempts_remaining"] == 5
    assert info["reset_time"] == 0
    assert info["retry_after"] == 0


def test_get_rate_limit_info_with_requests(rate_limiter):
    """Test get_rate_limit_info returns correct info with requests."""
    with patch("time.time", return_value=1000.0):
        rate_limiter.check_rate_limit("user1")
        rate_limiter.check_rate_limit("user1")
    
    with patch("time.time", return_value=1001.0):
        info = rate_limiter.get_rate_limit_info("user1")
    
    assert info["attempts"] == 2
    assert info["max_attempts"] == 5
    assert info["window_seconds"] == 60
    assert info["attempts_remaining"] == 3
    assert info["reset_time"] > 0
    assert info["retry_after"] > 0


def test_get_rate_limit_info_calculates_reset_time(rate_limiter):
    """Test get_rate_limit_info calculates reset time correctly."""
    with patch("time.time", return_value=1000.0):
        rate_limiter.check_rate_limit("user1")
    
    with patch("time.time", return_value=1001.0):
        info = rate_limiter.get_rate_limit_info("user1")
    
    # Reset time should be oldest request + window_seconds
    expected_reset = 1000.0 + 60
    assert abs(info["reset_time"] - expected_reset) < 0.1


def test_get_rate_limit_info_calculates_retry_after(rate_limiter):
    """Test get_rate_limit_info calculates retry_after correctly."""
    with patch("time.time", return_value=1000.0):
        rate_limiter.check_rate_limit("user1")
    
    with patch("time.time", return_value=1010.0):  # 10 seconds later
        info = rate_limiter.get_rate_limit_info("user1")
    
    # Retry after should be reset_time - current_time
    expected_retry = (1000.0 + 60) - 1010.0
    assert abs(info["retry_after"] - expected_retry) < 1  # Allow 1 second tolerance


def test_get_rate_limit_info_filters_old_requests(rate_limiter):
    """Test get_rate_limit_info filters out old requests."""
    with patch("time.time", return_value=1000.0):
        rate_limiter.check_rate_limit("user1")
    
    with patch("time.time", return_value=1070.0):  # 70 seconds later, outside window
        info = rate_limiter.get_rate_limit_info("user1")
    
    assert info["attempts"] == 0
    assert info["attempts_remaining"] == 5


def test_enforce_rate_limit_allows_request(rate_limiter):
    """Test enforce_rate_limit allows request within limit."""
    # Should not raise
    rate_limiter.enforce_rate_limit("user1")


def test_enforce_rate_limit_raises_when_exceeded(rate_limiter):
    """Test enforce_rate_limit raises RateLimitError when limit exceeded."""
    # Make 5 requests (at the limit)
    for _ in range(5):
        rate_limiter.check_rate_limit("user1")
    
    # 6th request should raise
    with pytest.raises(RateLimitError) as exc_info:
        rate_limiter.enforce_rate_limit("user1")
    
    assert "Rate limit exceeded" in str(exc_info.value)
    assert exc_info.value.retry_after is not None


def test_enforce_rate_limit_includes_retry_after(rate_limiter):
    """Test enforce_rate_limit includes retry_after in error."""
    with patch("time.time", return_value=1000.0):
        for _ in range(5):
            rate_limiter.check_rate_limit("user1")
    
    with patch("time.time", return_value=1001.0):
        with pytest.raises(RateLimitError) as exc_info:
            rate_limiter.enforce_rate_limit("user1")
        
        assert exc_info.value.retry_after is not None
        assert exc_info.value.retry_after > 0


def test_stats_roll_limiter_initialized():
    """Test stats_roll_limiter is initialized with correct defaults."""
    assert stats_roll_limiter.max_requests == 10
    assert stats_roll_limiter.window_seconds == 60


def test_character_creation_limiter_initialized():
    """Test character_creation_limiter is initialized with correct defaults."""
    assert character_creation_limiter.max_requests == 5
    assert character_creation_limiter.window_seconds == 300
