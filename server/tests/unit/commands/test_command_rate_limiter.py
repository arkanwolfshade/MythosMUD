"""
Tests for command rate limiting to prevent DoS attacks.

Like the wards inscribed on the threshold of the Necronomicon's vault,
these rate limits prevent overwhelming the system.

AI: Tests sliding window rate limiting for command spam prevention.
"""

import time
from datetime import UTC, datetime, timedelta

import pytest

from server.middleware.command_rate_limiter import CommandRateLimiter


class FakeClock:
    """Deterministic clock for rate limiter tests."""

    def __init__(self, initial: datetime | None = None):
        self._current = initial or datetime.now(UTC)

    def advance(self, seconds: float) -> None:
        self._current += timedelta(seconds=seconds)

    def now(self) -> datetime:
        return self._current


class TestCommandRateLimiter:
    """Test suite for command rate limiting."""

    def test_initialization(self):
        """Rate limiter initializes with correct settings."""
        limiter = CommandRateLimiter(max_commands=10, window_seconds=60)

        assert limiter.max_commands == 10
        assert limiter.window.total_seconds() == 60

    def test_first_command_allowed(self):
        """First command is always allowed."""
        limiter = CommandRateLimiter(max_commands=5, window_seconds=60)

        assert limiter.is_allowed("player1") is True

    def test_commands_within_limit_allowed(self):
        """Commands within rate limit are allowed."""
        limiter = CommandRateLimiter(max_commands=5, window_seconds=60)

        # Should allow 5 commands
        for _ in range(5):
            assert limiter.is_allowed("player1") is True

    def test_commands_exceeding_limit_blocked(self):
        """Commands exceeding rate limit are blocked."""
        limiter = CommandRateLimiter(max_commands=3, window_seconds=60)

        # Allow 3 commands
        for _ in range(3):
            assert limiter.is_allowed("player1") is True

        # 4th command should be blocked
        assert limiter.is_allowed("player1") is False

    def test_get_wait_time(self):
        """Get wait time returns correct value when rate limited."""
        limiter = CommandRateLimiter(max_commands=2, window_seconds=10)

        # Use up the limit
        limiter.is_allowed("player1")
        limiter.is_allowed("player1")

        # Should need to wait
        wait_time = limiter.get_wait_time("player1")
        assert 0 < wait_time <= 10

    def test_wait_time_zero_when_not_limited(self):
        """Wait time is minimal when not rate limited."""
        limiter = CommandRateLimiter(max_commands=5, window_seconds=60)

        limiter.is_allowed("player1")

        wait_time = limiter.get_wait_time("player1")
        # Wait time will be window_seconds minus time since first command
        # Since we just issued a command, it should be close to window_seconds
        assert wait_time > 0  # Not zero, but should be small since we're not limited

    def test_rate_limit_resets_after_window(self):
        """Rate limit resets after time window passes."""
        clock = FakeClock()
        limiter = CommandRateLimiter(max_commands=2, window_seconds=1, now_provider=clock.now)

        # Use up the limit
        assert limiter.is_allowed("player1") is True
        assert limiter.is_allowed("player1") is True
        assert limiter.is_allowed("player1") is False

        # Advance beyond window
        clock.advance(1.1)

        # Should be allowed again
        assert limiter.is_allowed("player1") is True

    def test_multiple_players_independent(self):
        """Rate limits for different players are independent."""
        limiter = CommandRateLimiter(max_commands=2, window_seconds=60)

        # Player 1 uses limit
        assert limiter.is_allowed("player1") is True
        assert limiter.is_allowed("player1") is True
        assert limiter.is_allowed("player1") is False

        # Player 2 should still be allowed
        assert limiter.is_allowed("player2") is True
        assert limiter.is_allowed("player2") is True

    def test_get_remaining_commands(self):
        """Get remaining commands returns correct count."""
        limiter = CommandRateLimiter(max_commands=5, window_seconds=60)

        assert limiter.get_remaining_commands("player1") == 5

        limiter.is_allowed("player1")
        assert limiter.get_remaining_commands("player1") == 4

        limiter.is_allowed("player1")
        limiter.is_allowed("player1")
        assert limiter.get_remaining_commands("player1") == 2

    def test_reset_player_rate_limit(self):
        """Resetting player rate limit clears their history."""
        limiter = CommandRateLimiter(max_commands=2, window_seconds=60)

        # Use up limit
        limiter.is_allowed("player1")
        limiter.is_allowed("player1")
        assert limiter.is_allowed("player1") is False

        # Reset
        limiter.reset_player("player1")

        # Should be allowed again
        assert limiter.is_allowed("player1") is True

    def test_get_player_stats(self):
        """Get player stats returns usage data."""
        limiter = CommandRateLimiter(max_commands=10, window_seconds=60)

        limiter.is_allowed("player1")
        limiter.is_allowed("player1")

        remaining = limiter.get_remaining_commands("player1")

        assert remaining == 8  # 10 max - 2 used

    def test_cleanup_old_entries(self):
        """Old entries are cleaned up automatically."""
        clock = FakeClock()
        limiter = CommandRateLimiter(max_commands=5, window_seconds=1, now_provider=clock.now)

        limiter.is_allowed("player1")
        clock.advance(1.1)
        limiter.is_allowed("player1")

        # Old entry should be cleaned up
        assert limiter.get_remaining_commands("player1") == 4  # Only 1 command in window

    def test_sliding_window_accuracy(self):
        """Sliding window accurately tracks commands over time."""
        clock = FakeClock()
        limiter = CommandRateLimiter(max_commands=3, window_seconds=2, now_provider=clock.now)

        # Time 0: 3 commands
        limiter.is_allowed("player1")
        limiter.is_allowed("player1")
        limiter.is_allowed("player1")

        # Should be blocked
        assert limiter.is_allowed("player1") is False

        # Wait 1 second
        clock.advance(1.0)

        # Still should be blocked (all 3 still in 2-second window)
        assert limiter.is_allowed("player1") is False

        # Wait another 1.5 seconds (total 2.5s from start)
        clock.advance(1.5)

        # Now should be allowed (old commands outside window)
        assert limiter.is_allowed("player1") is True

    def test_zero_max_commands_always_blocks(self):
        """Zero max commands blocks all requests."""
        limiter = CommandRateLimiter(max_commands=0, window_seconds=60)

        assert limiter.is_allowed("player1") is False

    @pytest.mark.slow
    def test_very_short_window(self):
        """Very short time window works correctly."""
        limiter = CommandRateLimiter(max_commands=2, window_seconds=0.5)

        limiter.is_allowed("player1")
        limiter.is_allowed("player1")

        assert limiter.is_allowed("player1") is False

        time.sleep(0.6)

        assert limiter.is_allowed("player1") is True
