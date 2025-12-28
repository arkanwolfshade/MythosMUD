"""
Rate limiting for MythosMUD connections.

This module provides rate limiting functionality for connection attempts,
message sending, and other operations that need throttling.
"""

import time
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class RateLimiter:
    """
    Rate limiter for connection attempts and other operations.

    This class provides rate limiting functionality with configurable
    windows and thresholds for different types of operations.
    """

    def __init__(
        self,
        max_connection_attempts: int = 5,
        connection_window: int = 60,
        max_messages_per_minute: int = 100,
        message_window: int = 60,
    ) -> None:
        """
        Initialize the rate limiter with configurable settings.

        Args:
            max_connection_attempts: Maximum connection attempts per window (default: 5)
            connection_window: Connection rate limit window in seconds (default: 60)
            max_messages_per_minute: Maximum messages per minute per connection (default: 100)
            message_window: Message rate limit window in seconds (default: 60)
        """
        # Connection rate limiting
        self.connection_attempts: dict[str, list[float]] = {}
        self.max_connection_attempts = max_connection_attempts
        self.connection_window = connection_window

        # Message rate limiting (per connection)
        self.message_attempts: dict[str, list[float]] = {}  # connection_id -> list of timestamps
        self.max_messages_per_minute = max_messages_per_minute
        self.message_window = message_window

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
            logger.warning("Rate limit exceeded", player_id=player_id)
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

    def cleanup_old_attempts(self, max_age_seconds: int = 3600) -> None:
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
                logger.debug("Cleaned up rate limit data", player_count=len(orphaned_players))

        except (OSError, ValueError, TypeError, KeyError) as e:
            logger.error(
                "Error cleaning up rate limit attempts",
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )

    def cleanup_large_structures(self, max_entries: int = 1000) -> None:
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
                        "Cleaned up large rate limit structure for player",
                        player_id=player_id,
                        kept_entries=max_entries,
                    )

        except (OSError, ValueError, TypeError, KeyError) as e:
            logger.error(
                "Error cleaning up large rate limit structures",
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )

    def remove_player_data(self, player_id: str) -> None:
        """
        Remove all rate limit data for a specific player.

        Args:
            player_id: The player's ID to remove data for
        """
        try:
            if player_id in self.connection_attempts:
                del self.connection_attempts[player_id]
                logger.debug("Removed rate limit data", player_id=player_id)
        except (OSError, ValueError, TypeError, KeyError) as e:
            logger.error(
                "Error removing rate limit data",
                player_id=player_id,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )

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
        except (OSError, ValueError, TypeError, KeyError) as e:
            logger.error(
                "Error getting rate limiter stats",
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
            return {}

    def check_message_rate_limit(self, connection_id: str) -> bool:
        """
        Check if a connection has exceeded message rate limits.

        Args:
            connection_id: The connection ID (not player_id, for per-connection tracking)

        Returns:
            bool: True if rate limit not exceeded, False if exceeded

        AI: Per-connection rate limiting prevents DoS attacks from individual connections.
        """
        current_time = time.time()
        if connection_id not in self.message_attempts:
            self.message_attempts[connection_id] = []

        # Remove old attempts outside the window
        self.message_attempts[connection_id] = [
            attempt_time
            for attempt_time in self.message_attempts[connection_id]
            if current_time - attempt_time < self.message_window
        ]

        # Check if limit exceeded
        if len(self.message_attempts[connection_id]) >= self.max_messages_per_minute:
            logger.warning(
                "Message rate limit exceeded",
                connection_id=connection_id,
                message_count=len(self.message_attempts[connection_id]),
                max_messages=self.max_messages_per_minute,
            )
            return False

        # Add current attempt
        self.message_attempts[connection_id].append(current_time)
        return True

    def get_message_rate_limit_info(self, connection_id: str) -> dict[str, Any]:
        """
        Get message rate limit information for a connection.

        Args:
            connection_id: The connection ID

        Returns:
            dict: Rate limit information including attempts, limits, and reset time
        """
        current_time = time.time()
        attempts = self.message_attempts.get(connection_id, [])

        # Filter recent attempts
        recent_attempts = [
            attempt_time for attempt_time in attempts if current_time - attempt_time < self.message_window
        ]

        return {
            "attempts": len(recent_attempts),
            "current_attempts": len(recent_attempts),  # Alias for test compatibility
            "max_attempts": self.max_messages_per_minute,
            "window_seconds": self.message_window,
            "attempts_remaining": max(0, self.max_messages_per_minute - len(recent_attempts)),
            "reset_time": current_time + self.message_window if recent_attempts else 0,
        }

    def remove_connection_message_data(self, connection_id: str) -> None:
        """
        Remove message rate limit data for a specific connection.

        Args:
            connection_id: The connection ID to remove data for
        """
        try:
            if connection_id in self.message_attempts:
                del self.message_attempts[connection_id]
                logger.debug("Removed message rate limit data", connection_id=connection_id)
        except (OSError, ValueError, TypeError, KeyError) as e:
            logger.error(
                "Error removing message rate limit data",
                connection_id=connection_id,
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )

    def cleanup_old_message_attempts(self, max_age_seconds: int = 3600) -> None:
        """
        Clean up old message rate limit attempts to prevent memory bloat.

        Args:
            max_age_seconds: Maximum age of attempts to keep (default: 1 hour)
        """
        try:
            current_time = time.time()
            orphaned_connections = []

            for connection_id, attempts in list(self.message_attempts.items()):
                # Remove attempts older than max_age_seconds
                self.message_attempts[connection_id] = [
                    attempt_time for attempt_time in attempts if current_time - attempt_time < max_age_seconds
                ]

                # Remove empty entries
                if not self.message_attempts[connection_id]:
                    orphaned_connections.append(connection_id)

            for connection_id in orphaned_connections:
                del self.message_attempts[connection_id]

            if orphaned_connections:
                logger.debug("Cleaned up message rate limit data", connection_count=len(orphaned_connections))

        except (OSError, ValueError, TypeError, KeyError) as e:
            logger.error(
                "Error cleaning up message rate limit attempts",
                error=str(e),
                error_type=type(e).__name__,
                exc_info=True,
            )
