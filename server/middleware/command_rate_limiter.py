"""
Per-player command rate limiting.

Prevents command flooding and denial-of-service attacks by limiting
the rate at which players can execute commands.

AI: Uses sliding window algorithm for accurate rate limiting without fixed time buckets.
"""

from collections import defaultdict
from collections.abc import Callable
from datetime import UTC, datetime, timedelta

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class CommandRateLimiter:
    """
    Per-player command rate limiting using sliding window algorithm.

    Tracks command timestamps per player and enforces a maximum commands
    per time window limit. More accurate than fixed-bucket rate limiting
    as it prevents burst attacks at bucket boundaries.

    AI: Sliding window prevents "boundary gaming" where attackers send bursts
    at bucket transitions.
    """

    def __init__(
        self,
        max_commands: int = 10,
        window_seconds: int = 1,
        now_provider: Callable[[], datetime] | None = None,
    ):
        """
        Initialize command rate limiter.

        Args:
            max_commands: Maximum commands allowed in time window
            window_seconds: Size of sliding window in seconds

        AI: Default of 10 commands/second is generous for legitimate play
        while preventing flood attacks.
        """
        self.max_commands = max_commands
        self.window = timedelta(seconds=window_seconds)
        self.player_timestamps: dict[str, list[datetime]] = defaultdict(list)
        self._now_provider = now_provider or (lambda: datetime.now(UTC))

        logger.info("CommandRateLimiter initialized", max_commands=max_commands, window_seconds=window_seconds)

    def is_allowed(self, player_name: str) -> bool:
        """
        Check if player can execute a command now.

        Implements sliding window rate limiting:
        1. Remove timestamps outside the window
        2. Check if under limit
        3. Record new timestamp if allowed

        Args:
            player_name: Player attempting to execute command

        Returns:
            True if command is allowed, False if rate limited

        AI: This is the primary rate limit check - call before processing commands.
        """
        now = self._now_provider()
        cutoff = now - self.window

        # Remove old timestamps outside the sliding window
        self.player_timestamps[player_name] = [ts for ts in self.player_timestamps[player_name] if ts > cutoff]

        # Check if under limit
        current_count = len(self.player_timestamps[player_name])
        if current_count >= self.max_commands:
            logger.warning(
                "Command rate limit exceeded",
                player=player_name,
                current_count=current_count,
                max_commands=self.max_commands,
                window_seconds=self.window.total_seconds(),
            )
            return False

        # Record new command timestamp
        self.player_timestamps[player_name].append(now)

        logger.debug("Command allowed", player=player_name, count=current_count + 1, max=self.max_commands)

        return True

    def get_wait_time(self, player_name: str) -> float:
        """
        Get seconds until rate limit resets for this player.

        Calculates when the oldest timestamp will age out of the window,
        allowing a new command to be executed.

        Args:
            player_name: Player to check

        Returns:
            Seconds until rate limit resets (0 if not rate limited)

        AI: Provides actionable feedback to players about when they can retry.
        """
        if not self.player_timestamps[player_name]:
            return 0.0

        # Find oldest timestamp
        oldest = min(self.player_timestamps[player_name])
        reset_time = oldest + self.window
        now = self._now_provider()

        wait = (reset_time - now).total_seconds()
        return max(0.0, wait)

    def get_remaining_commands(self, player_name: str) -> int:
        """
        Get number of commands player can still execute.

        Args:
            player_name: Player to check

        Returns:
            Number of commands remaining in current window

        AI: Useful for UI/UX to show player their remaining quota.
        """
        now = self._now_provider()
        cutoff = now - self.window

        # Count recent commands
        recent_count = sum(1 for ts in self.player_timestamps[player_name] if ts > cutoff)

        remaining = max(0, self.max_commands - recent_count)
        return remaining

    def reset_player(self, player_name: str) -> None:
        """
        Reset rate limit for a specific player.

        Useful for admin commands or when granting temporary immunity.

        Args:
            player_name: Player whose rate limit to reset

        AI: Use sparingly - mainly for admin/debugging purposes.
        """
        if player_name in self.player_timestamps:
            del self.player_timestamps[player_name]
            logger.info("Rate limit reset for player", player=player_name)

    def reset_all(self) -> None:
        """
        Reset rate limit for all players.

        Clears all accumulated timestamp data. Primarily used for testing
        to ensure test isolation and prevent test pollution.

        AI: Should be called between tests to prevent state leakage.
        """
        self.player_timestamps.clear()
        logger.debug("Rate limiter reset for all players")

    def get_stats(self) -> dict:
        """
        Get system-wide rate limiting statistics.

        Returns:
            Dictionary containing rate limiter stats

        AI: Useful for monitoring and detecting coordinated attacks.
        """
        now = self._now_provider()
        cutoff = now - self.window

        active_players = 0
        rate_limited_players = 0
        total_recent_commands = 0

        for _player, timestamps in self.player_timestamps.items():
            recent = [ts for ts in timestamps if ts > cutoff]
            if recent:
                active_players += 1
                total_recent_commands += len(recent)
                if len(recent) >= self.max_commands:
                    rate_limited_players += 1

        return {
            "active_players": active_players,
            "rate_limited_players": rate_limited_players,
            "total_recent_commands": total_recent_commands,
            "max_commands_per_window": self.max_commands,
            "window_seconds": self.window.total_seconds(),
        }

    def cleanup_inactive_players(self, inactive_threshold_hours: int = 24) -> int:
        """
        Remove timestamp data for players who haven't been active recently.

        Prevents memory growth from tracking every player who ever connected.

        Args:
            inactive_threshold_hours: Hours of inactivity before cleanup

        Returns:
            Number of players cleaned up

        AI: Call periodically (e.g., hourly) to prevent unbounded memory growth.
        """
        now = datetime.now(UTC)
        threshold = now - timedelta(hours=inactive_threshold_hours)

        inactive_players = [
            player
            for player, timestamps in self.player_timestamps.items()
            if not timestamps or max(timestamps) < threshold
        ]

        for player in inactive_players:
            del self.player_timestamps[player]

        if inactive_players:
            logger.info("Cleaned up inactive player rate limit data", count=len(inactive_players))

        return len(inactive_players)


# Global command rate limiter instance
# AI: Singleton pattern - import and use this instance throughout the codebase
command_rate_limiter = CommandRateLimiter(max_commands=10, window_seconds=1)
