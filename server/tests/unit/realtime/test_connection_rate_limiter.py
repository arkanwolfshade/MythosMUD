"""
Unit tests for rate limiter.

Tests the rate_limiter module classes and functions.
"""

import time
from unittest.mock import patch

import pytest

from server.realtime.rate_limiter import RateLimiter


def test_rate_limiter_init_defaults():
    """Test RateLimiter.__init__() with default values."""
    limiter = RateLimiter()

    assert limiter.max_connection_attempts == 5
    assert limiter.connection_window == 60
    assert limiter.max_messages_per_minute == 100
    assert limiter.message_window == 60
    assert limiter.connection_attempts == {}
    assert limiter.message_attempts == {}


def test_rate_limiter_init_custom():
    """Test RateLimiter.__init__() with custom values."""
    limiter = RateLimiter(
        max_connection_attempts=10, connection_window=120, max_messages_per_minute=200, message_window=30
    )

    assert limiter.max_connection_attempts == 10
    assert limiter.connection_window == 120
    assert limiter.max_messages_per_minute == 200
    assert limiter.message_window == 30


def test_rate_limiter_check_rate_limit_first_attempt():
    """Test RateLimiter.check_rate_limit() allows first attempt."""
    limiter = RateLimiter(max_connection_attempts=5, connection_window=60)
    player_id = "player_123"

    result = limiter.check_rate_limit(player_id)

    assert result is True
    assert len(limiter.connection_attempts[player_id]) == 1


def test_rate_limiter_check_rate_limit_within_limit():
    """Test RateLimiter.check_rate_limit() allows attempts within limit."""
    limiter = RateLimiter(max_connection_attempts=5, connection_window=60)
    player_id = "player_123"

    for i in range(4):
        result = limiter.check_rate_limit(player_id)
        assert result is True

    assert len(limiter.connection_attempts[player_id]) == 4


def test_rate_limiter_check_rate_limit_exceeded():
    """Test RateLimiter.check_rate_limit() blocks when limit exceeded."""
    limiter = RateLimiter(max_connection_attempts=5, connection_window=60)
    player_id = "player_123"

    # Make 5 attempts (the limit)
    for _ in range(5):
        limiter.check_rate_limit(player_id)

    # 6th attempt should be blocked
    with patch("server.realtime.rate_limiter.logger") as mock_logger:
        result = limiter.check_rate_limit(player_id)
        assert result is False
        mock_logger.warning.assert_called_once()


def test_rate_limiter_check_rate_limit_old_attempts_removed():
    """Test RateLimiter.check_rate_limit() removes old attempts outside window."""
    limiter = RateLimiter(max_connection_attempts=5, connection_window=60)
    player_id = "player_123"

    # Add old attempt (outside window)
    old_time = time.time() - 120  # 2 minutes ago
    limiter.connection_attempts[player_id] = [old_time]

    # New attempt should be allowed (old one removed)
    result = limiter.check_rate_limit(player_id)

    assert result is True
    assert len(limiter.connection_attempts[player_id]) == 1
    # The old attempt should be gone, only new one remains
    assert all(t > old_time for t in limiter.connection_attempts[player_id])


def test_rate_limiter_get_rate_limit_info():
    """Test RateLimiter.get_rate_limit_info() returns correct info."""
    limiter = RateLimiter(max_connection_attempts=5, connection_window=60)
    player_id = "player_123"

    # Make 2 attempts
    limiter.check_rate_limit(player_id)
    limiter.check_rate_limit(player_id)

    info = limiter.get_rate_limit_info(player_id)

    assert info["attempts"] == 2
    assert info["max_attempts"] == 5
    assert info["window_seconds"] == 60
    assert info["attempts_remaining"] == 3
    assert info["reset_time"] > time.time()


def test_rate_limiter_get_rate_limit_info_no_attempts():
    """Test RateLimiter.get_rate_limit_info() for player with no attempts."""
    limiter = RateLimiter(max_connection_attempts=5, connection_window=60)
    player_id = "player_123"

    info = limiter.get_rate_limit_info(player_id)

    assert info["attempts"] == 0
    assert info["max_attempts"] == 5
    assert info["attempts_remaining"] == 5
    assert info["reset_time"] == 0


def test_rate_limiter_cleanup_old_attempts():
    """Test RateLimiter.cleanup_old_attempts() removes old attempts."""
    limiter = RateLimiter()
    player_id = "player_123"

    # Add old and recent attempts
    old_time = time.time() - 7200  # 2 hours ago
    recent_time = time.time() - 30  # 30 seconds ago
    limiter.connection_attempts[player_id] = [old_time, recent_time]

    limiter.cleanup_old_attempts(max_age_seconds=3600)

    # Only recent attempt should remain
    assert len(limiter.connection_attempts[player_id]) == 1
    assert limiter.connection_attempts[player_id][0] == recent_time


def test_rate_limiter_cleanup_old_attempts_removes_empty():
    """Test RateLimiter.cleanup_old_attempts() removes empty entries."""
    limiter = RateLimiter()
    player_id = "player_123"

    # Add only old attempts
    old_time = time.time() - 7200
    limiter.connection_attempts[player_id] = [old_time]

    with patch("server.realtime.rate_limiter.logger") as mock_logger:
        limiter.cleanup_old_attempts(max_age_seconds=3600)

        # Player entry should be removed
        assert player_id not in limiter.connection_attempts
        mock_logger.debug.assert_called_once()


def test_rate_limiter_cleanup_old_attempts_error():
    """Test RateLimiter.cleanup_old_attempts() handles errors."""
    limiter = RateLimiter()
    player_id = "player_123"

    # Create a custom dict-like object that raises an error
    class ErrorDict(dict):
        def items(self):
            raise OSError("Test error")

    error_dict = ErrorDict()
    error_dict[player_id] = [time.time()]
    limiter.connection_attempts = error_dict

    with patch("server.realtime.rate_limiter.logger") as mock_logger:
        limiter.cleanup_old_attempts()

        mock_logger.error.assert_called_once()


def test_rate_limiter_cleanup_large_structures():
    """Test RateLimiter.cleanup_large_structures() trims large lists."""
    limiter = RateLimiter()
    player_id = "player_123"

    # Create a large list of attempts
    large_list = [time.time() - i for i in range(2000)]
    limiter.connection_attempts[player_id] = large_list

    with patch("server.realtime.rate_limiter.logger") as mock_logger:
        limiter.cleanup_large_structures(max_entries=1000)

        # Should be trimmed to 1000 most recent
        assert len(limiter.connection_attempts[player_id]) == 1000
        mock_logger.debug.assert_called_once()


def test_rate_limiter_cleanup_large_structures_error():
    """Test RateLimiter.cleanup_large_structures() handles errors."""
    limiter = RateLimiter()
    player_id = "player_123"

    # Create a custom dict-like object that raises an error
    class ErrorDict(dict):
        def items(self):
            raise ValueError("Test error")

    error_dict = ErrorDict()
    error_dict[player_id] = [time.time()]
    limiter.connection_attempts = error_dict

    with patch("server.realtime.rate_limiter.logger") as mock_logger:
        limiter.cleanup_large_structures()

        mock_logger.error.assert_called_once()


def test_rate_limiter_remove_player_data():
    """Test RateLimiter.remove_player_data() removes player data."""
    limiter = RateLimiter()
    player_id = "player_123"

    limiter.connection_attempts[player_id] = [time.time()]

    with patch("server.realtime.rate_limiter.logger") as mock_logger:
        limiter.remove_player_data(player_id)

        assert player_id not in limiter.connection_attempts
        mock_logger.debug.assert_called_once()


def test_rate_limiter_remove_player_data_not_present():
    """Test RateLimiter.remove_player_data() handles player not present."""
    limiter = RateLimiter()
    player_id = "player_123"

    # Should not raise error if player not in dict
    limiter.remove_player_data(player_id)

    assert player_id not in limiter.connection_attempts


def test_rate_limiter_remove_player_data_error():
    """Test RateLimiter.remove_player_data() handles errors."""
    limiter = RateLimiter()
    player_id = "player_123"

    # Create a custom dict-like object that raises an error on deletion
    class ErrorDict(dict):
        def __delitem__(self, key):
            raise KeyError("Test error")

    error_dict = ErrorDict()
    error_dict[player_id] = [time.time()]
    limiter.connection_attempts = error_dict

    with patch("server.realtime.rate_limiter.logger") as mock_logger:
        limiter.remove_player_data(player_id)

        mock_logger.error.assert_called_once()


def test_rate_limiter_get_stats():
    """Test RateLimiter.get_stats() returns statistics."""
    limiter = RateLimiter(max_connection_attempts=5, connection_window=60)
    player_id = "player_123"

    # Make some attempts
    limiter.check_rate_limit(player_id)
    limiter.check_rate_limit(player_id)

    stats = limiter.get_stats()

    assert stats["total_players"] == 1
    assert stats["active_players"] == 1
    assert stats["total_attempts"] == 2
    assert stats["max_attempts_per_player"] == 5
    assert stats["window_seconds"] == 60


def test_rate_limiter_get_stats_empty():
    """Test RateLimiter.get_stats() handles empty state."""
    limiter = RateLimiter()

    stats = limiter.get_stats()

    assert stats["total_players"] == 0
    assert stats["active_players"] == 0
    assert stats["total_attempts"] == 0


def test_rate_limiter_get_stats_error():
    """Test RateLimiter.get_stats() handles errors."""
    limiter = RateLimiter()
    player_id = "player_123"

    # Create a custom dict-like object that raises an error
    class ErrorDict(dict):
        def items(self):
            raise TypeError("Test error")

    error_dict = ErrorDict()
    error_dict[player_id] = [time.time()]
    limiter.connection_attempts = error_dict

    with patch("server.realtime.rate_limiter.logger") as mock_logger:
        stats = limiter.get_stats()

        assert stats == {}
        mock_logger.error.assert_called_once()


def test_rate_limiter_check_message_rate_limit_first():
    """Test RateLimiter.check_message_rate_limit() allows first message."""
    limiter = RateLimiter(max_messages_per_minute=100, message_window=60)
    connection_id = "conn_123"

    result = limiter.check_message_rate_limit(connection_id)

    assert result is True
    assert len(limiter.message_attempts[connection_id]) == 1


def test_rate_limiter_check_message_rate_limit_within_limit():
    """Test RateLimiter.check_message_rate_limit() allows messages within limit."""
    limiter = RateLimiter(max_messages_per_minute=100, message_window=60)
    connection_id = "conn_123"

    for _ in range(99):
        result = limiter.check_message_rate_limit(connection_id)
        assert result is True

    assert len(limiter.message_attempts[connection_id]) == 99


def test_rate_limiter_check_message_rate_limit_exceeded():
    """Test RateLimiter.check_message_rate_limit() blocks when limit exceeded."""
    limiter = RateLimiter(max_messages_per_minute=100, message_window=60)
    connection_id = "conn_123"

    # Make 100 attempts (the limit)
    for _ in range(100):
        limiter.check_message_rate_limit(connection_id)

    # 101st attempt should be blocked
    with patch("server.realtime.rate_limiter.logger") as mock_logger:
        result = limiter.check_message_rate_limit(connection_id)
        assert result is False
        mock_logger.warning.assert_called_once()


def test_rate_limiter_get_message_rate_limit_info():
    """Test RateLimiter.get_message_rate_limit_info() returns correct info."""
    limiter = RateLimiter(max_messages_per_minute=100, message_window=60)
    connection_id = "conn_123"

    # Make 3 attempts
    limiter.check_message_rate_limit(connection_id)
    limiter.check_message_rate_limit(connection_id)
    limiter.check_message_rate_limit(connection_id)

    info = limiter.get_message_rate_limit_info(connection_id)

    assert info["attempts"] == 3
    assert info["current_attempts"] == 3
    assert info["max_attempts"] == 100
    assert info["window_seconds"] == 60
    assert info["attempts_remaining"] == 97
    assert info["reset_time"] > time.time()


def test_rate_limiter_get_message_rate_limit_info_no_attempts():
    """Test RateLimiter.get_message_rate_limit_info() for connection with no attempts."""
    limiter = RateLimiter(max_messages_per_minute=100, message_window=60)
    connection_id = "conn_123"

    info = limiter.get_message_rate_limit_info(connection_id)

    assert info["attempts"] == 0
    assert info["current_attempts"] == 0
    assert info["max_attempts"] == 100
    assert info["attempts_remaining"] == 100
    assert info["reset_time"] == 0


def test_rate_limiter_remove_connection_message_data():
    """Test RateLimiter.remove_connection_message_data() removes connection data."""
    limiter = RateLimiter()
    connection_id = "conn_123"

    limiter.message_attempts[connection_id] = [time.time()]

    with patch("server.realtime.rate_limiter.logger") as mock_logger:
        limiter.remove_connection_message_data(connection_id)

        assert connection_id not in limiter.message_attempts
        mock_logger.debug.assert_called_once()


def test_rate_limiter_remove_connection_message_data_not_present():
    """Test RateLimiter.remove_connection_message_data() handles connection not present."""
    limiter = RateLimiter()
    connection_id = "conn_123"

    # Should not raise error if connection not in dict
    limiter.remove_connection_message_data(connection_id)

    assert connection_id not in limiter.message_attempts


def test_rate_limiter_cleanup_old_message_attempts():
    """Test RateLimiter.cleanup_old_message_attempts() removes old attempts."""
    limiter = RateLimiter()
    connection_id = "conn_123"

    # Add old and recent attempts
    old_time = time.time() - 7200  # 2 hours ago
    recent_time = time.time() - 30  # 30 seconds ago
    limiter.message_attempts[connection_id] = [old_time, recent_time]

    limiter.cleanup_old_message_attempts(max_age_seconds=3600)

    # Only recent attempt should remain
    assert len(limiter.message_attempts[connection_id]) == 1
    assert limiter.message_attempts[connection_id][0] == recent_time


def test_rate_limiter_cleanup_old_message_attempts_removes_empty():
    """Test RateLimiter.cleanup_old_message_attempts() removes empty entries."""
    limiter = RateLimiter()
    connection_id = "conn_123"

    # Add only old attempts
    old_time = time.time() - 7200
    limiter.message_attempts[connection_id] = [old_time]

    with patch("server.realtime.rate_limiter.logger") as mock_logger:
        limiter.cleanup_old_message_attempts(max_age_seconds=3600)

        # Connection entry should be removed
        assert connection_id not in limiter.message_attempts
        mock_logger.debug.assert_called_once()


def test_rate_limiter_cleanup_old_message_attempts_error():
    """Test RateLimiter.cleanup_old_message_attempts() handles errors."""
    limiter = RateLimiter()
    connection_id = "conn_123"

    # Create a custom dict-like object that raises an error
    class ErrorDict(dict):
        def items(self):
            raise OSError("Test error")

    error_dict = ErrorDict()
    error_dict[connection_id] = [time.time()]
    limiter.message_attempts = error_dict

    with patch("server.realtime.rate_limiter.logger") as mock_logger:
        limiter.cleanup_old_message_attempts()

        mock_logger.error.assert_called_once()
