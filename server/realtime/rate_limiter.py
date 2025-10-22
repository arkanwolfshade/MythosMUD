"""
Rate limiting for MythosMUD connections.

This module provides rate limiting functionality for connection attempts,
message sending, and other operations that need throttling.
"""

import time
from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class RateLimiter:
    """
    Rate limiter for connection attempts and other operations.

    This class provides rate limiting functionality with configurable
    windows and thresholds for different types of operations.
    """

    def __init__(self):
        """Initialize the rate limiter with default settings."""
        # Connection rate limiting
        self.connection_attempts: dict[str, list[float]] = {}
        self.max_connection_attempts = 5  # Max attempts per minute
        self.connection_window = 60  # Time window in seconds

    def check_rate_limit(self, player_id: str) -> bool:
        """
        Check if a player has exceeded rate limits.

        Args:
            player_id: The player's ID

        Returns:
            bool: True if rate limit not exceeded, False if exceeded
        """
        current_time = time.time()
        if player_id not in self.connection_attempts:
            self.connection_attempts[player_id] = []

        # Remove old attempts outside the window
        self.connection_attempts[player_id] = [
            attempt_time
            for attempt_time in self.connection_attempts[player_id]
            if current_time - attempt_time < self.connection_window
        ]

        # Check if limit exceeded
        if len(self.connection_attempts[player_id]) >= self.max_connection_attempts:
            logger.warning(f"Rate limit exceeded for player {player_id}")
            return False

        # Add current attempt
        self.connection_attempts[player_id].append(current_time)
        return True

    def get_rate_limit_info(self, player_id: str) -> dict[str, Any]:
        """
        Get rate limit information for a player.

        Args:
            player_id: The player's ID

        Returns:
            dict: Rate limit information including attempts, limits, and reset time
        """
        current_time = time.time()
        attempts = self.connection_attempts.get(player_id, [])

        # Filter recent attempts
        recent_attempts = [
            attempt_time for attempt_time in attempts if current_time - attempt_time < self.connection_window
        ]

        return {
            "attempts": len(recent_attempts),
            "max_attempts": self.max_connection_attempts,
            "window_seconds": self.connection_window,
            "attempts_remaining": max(0, self.max_connection_attempts - len(recent_attempts)),
            "reset_time": current_time + self.connection_window if recent_attempts else 0,
        }

    def cleanup_old_attempts(self, max_age_seconds: int = 3600):
        """
        Clean up old rate limit attempts to prevent memory bloat.

        Args:
            max_age_seconds: Maximum age of attempts to keep (default: 1 hour)
        """
        try:
            current_time = time.time()
            orphaned_players = []

            for player_id, attempts in list(self.connection_attempts.items()):
                # Remove attempts older than max_age_seconds
                self.connection_attempts[player_id] = [
                    attempt_time for attempt_time in attempts if current_time - attempt_time < max_age_seconds
                ]

                # Remove empty entries
                if not self.connection_attempts[player_id]:
                    orphaned_players.append(player_id)

            for player_id in orphaned_players:
                del self.connection_attempts[player_id]

            if orphaned_players:
                logger.debug(f"Cleaned up rate limit data for {len(orphaned_players)} players")

        except Exception as e:
            logger.error(f"Error cleaning up rate limit attempts: {e}")

    def cleanup_large_structures(self, max_entries: int = 1000):
        """
        Clean up large data structures to prevent memory bloat.

        Args:
            max_entries: Maximum number of entries per player to keep (default: 1000)
        """
        try:
            for player_id, attempts in list(self.connection_attempts.items()):
                if len(attempts) > max_entries:
                    # Keep only the most recent attempts
                    self.connection_attempts[player_id] = attempts[-max_entries:]
                    logger.debug(
                        f"Cleaned up large rate limit structure for player {player_id}: kept {max_entries} entries"
                    )

        except Exception as e:
            logger.error(f"Error cleaning up large rate limit structures: {e}")

    def remove_player_data(self, player_id: str):
        """
        Remove all rate limit data for a specific player.

        Args:
            player_id: The player's ID to remove data for
        """
        try:
            if player_id in self.connection_attempts:
                del self.connection_attempts[player_id]
                logger.debug(f"Removed rate limit data for player {player_id}")
        except Exception as e:
            logger.error(f"Error removing rate limit data for player {player_id}: {e}")

    def get_stats(self) -> dict[str, Any]:
        """
        Get rate limiter statistics.

        Returns:
            dict: Statistics about current rate limiting state
        """
        try:
            current_time = time.time()
            total_attempts = 0
            active_players = 0

            for _player_id, attempts in self.connection_attempts.items():
                recent_attempts = [
                    attempt_time for attempt_time in attempts if current_time - attempt_time < self.connection_window
                ]
                if recent_attempts:
                    active_players += 1
                    total_attempts += len(recent_attempts)

            return {
                "total_players": len(self.connection_attempts),
                "active_players": active_players,
                "total_attempts": total_attempts,
                "max_attempts_per_player": self.max_connection_attempts,
                "window_seconds": self.connection_window,
            }
        except Exception as e:
            logger.error(f"Error getting rate limiter stats: {e}")
            return {}
