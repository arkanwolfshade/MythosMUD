"""
Tests for command rate limiter to improve coverage.

This module provides targeted tests for command_rate_limiter.py
to cover the uncovered utility and statistics functions.

As documented in the Pnakotic Manuscripts, proper rate limiting
is essential for preventing eldritch denial-of-service attacks.
"""

from datetime import UTC, datetime, timedelta

from server.middleware.command_rate_limiter import CommandRateLimiter


class TestCommandRateLimiterStats:
    """Test command rate limiter statistics functions."""

    def test_get_stats_no_activity(self) -> None:
        """Test get_stats with no player activity.

        AI: Tests get_stats function (lines 171-186) with empty state.
        """
        limiter = CommandRateLimiter(max_commands=5, window_seconds=1)

        stats = limiter.get_stats()

        assert stats["active_players"] == 0
        assert stats["rate_limited_players"] == 0
        assert stats["total_recent_commands"] == 0
        assert stats["max_commands_per_window"] == 5
        assert stats["window_seconds"] == 1.0

    def test_get_stats_with_active_players(self) -> None:
        """Test get_stats with active players.

        AI: Tests stats collection with players having issued commands.
        """
        limiter = CommandRateLimiter(max_commands=5, window_seconds=1)

        # Simulate player activity
        limiter.is_allowed("player1")
        limiter.is_allowed("player1")
        limiter.is_allowed("player2")

        stats = limiter.get_stats()

        assert stats["active_players"] == 2
        assert stats["total_recent_commands"] == 3

    def test_get_stats_with_rate_limited_players(self) -> None:
        """Test get_stats with rate-limited players.

        AI: Tests detection of rate-limited players in stats.
        """
        limiter = CommandRateLimiter(max_commands=3, window_seconds=10)

        # Exhaust rate limit for player1
        for _ in range(3):
            assert limiter.is_allowed("player1")

        # Player 2 is under limit
        limiter.is_allowed("player2")

        stats = limiter.get_stats()

        assert stats["active_players"] == 2
        assert stats["rate_limited_players"] == 1  # Only player1 is at limit
        assert stats["total_recent_commands"] == 4

    def test_cleanup_inactive_players_no_activity(self) -> None:
        """Test cleanup with no inactive players.

        AI: Tests cleanup_inactive_players function (lines 208-223) with no data.
        """
        limiter = CommandRateLimiter()

        cleaned = limiter.cleanup_inactive_players(inactive_threshold_hours=24)

        assert cleaned == 0

    def test_cleanup_inactive_players_with_active_players(self) -> None:
        """Test cleanup doesn't remove active players.

        AI: Tests that recent player activity prevents cleanup.
        """
        limiter = CommandRateLimiter()

        # Recent activity
        limiter.is_allowed("active_player")

        cleaned = limiter.cleanup_inactive_players(inactive_threshold_hours=1)

        assert cleaned == 0
        assert "active_player" in limiter.player_timestamps

    def test_cleanup_inactive_players_removes_old_data(self) -> None:
        """Test cleanup removes old player data.

        AI: Tests removal of truly inactive players.
        """
        limiter = CommandRateLimiter()

        # Manually add old timestamp
        old_time = datetime.now(UTC) - timedelta(hours=25)
        limiter.player_timestamps["old_player"] = [old_time]

        # Add recent player
        limiter.is_allowed("active_player")

        cleaned = limiter.cleanup_inactive_players(inactive_threshold_hours=24)

        assert cleaned == 1
        assert "old_player" not in limiter.player_timestamps
        assert "active_player" in limiter.player_timestamps

    def test_cleanup_inactive_players_with_empty_lists(self) -> None:
        """Test cleanup removes players with empty timestamp lists.

        AI: Tests cleanup of players with empty timestamp lists.
        """
        limiter = CommandRateLimiter()

        # Manually add player with empty list
        limiter.player_timestamps["empty_player"] = []

        cleaned = limiter.cleanup_inactive_players(inactive_threshold_hours=1)

        assert cleaned == 1
        assert "empty_player" not in limiter.player_timestamps

    def test_get_wait_time_no_timestamps(self) -> None:
        """Test get_wait_time with no timestamps.

        AI: Tests early return in get_wait_time (line 104).
        """
        limiter = CommandRateLimiter()

        wait_time = limiter.get_wait_time("new_player")

        assert wait_time == 0.0

    def test_get_wait_time_with_available_commands(self) -> None:
        """Test get_wait_time when commands are available.

        AI: Tests wait time calculation when player can issue commands.
        """
        limiter = CommandRateLimiter(max_commands=5, window_seconds=10)

        # Issue a command
        limiter.is_allowed("player1")

        # Still under limit, should have 0 wait
        wait_time = limiter.get_wait_time("player1")

        assert wait_time >= 0.0

    def test_get_stats_with_mixed_activity(self) -> None:
        """Test get_stats with varied player activity.

        AI: Tests comprehensive stats with diverse player states.
        """
        limiter = CommandRateLimiter(max_commands=2, window_seconds=10)

        # Player 1: At limit
        limiter.is_allowed("player1")
        limiter.is_allowed("player1")

        # Player 2: Under limit
        limiter.is_allowed("player2")

        # Player 3: No commands yet (shouldn't appear in stats)

        stats = limiter.get_stats()

        assert stats["active_players"] == 2
        assert stats["rate_limited_players"] == 1
        assert stats["total_recent_commands"] == 3

    def test_cleanup_inactive_players_custom_threshold(self) -> None:
        """Test cleanup with custom inactivity threshold.

        AI: Tests cleanup with different threshold values.
        """
        limiter = CommandRateLimiter()

        # Add player with 2-hour-old activity
        old_time = datetime.now(UTC) - timedelta(hours=2)
        limiter.player_timestamps["semi_old_player"] = [old_time]

        # Cleanup with 1-hour threshold (should remove)
        cleaned = limiter.cleanup_inactive_players(inactive_threshold_hours=1)
        assert cleaned == 1

        # Add another player with 2-hour-old activity
        limiter.player_timestamps["semi_old_player2"] = [old_time]

        # Cleanup with 3-hour threshold (should NOT remove)
        cleaned = limiter.cleanup_inactive_players(inactive_threshold_hours=3)
        assert cleaned == 0
