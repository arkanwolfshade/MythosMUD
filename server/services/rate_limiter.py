"""
Rate limiting service for MythosMUD chat system.

This module provides sliding window rate limiting for chat channels,
ensuring players cannot spam messages and maintaining chat quality.
"""

import time
from collections import defaultdict, deque
from typing import Any

from ..config import get_config
from ..structured_logging.enhanced_logging_config import get_logger
from .chat_logger import chat_logger

logger = get_logger("communications.rate_limiter")


class RateLimiter:
    """
    Sliding window rate limiter for chat channels.

    Implements per-user, per-channel rate limiting with configurable
    limits and sliding window tracking for accurate rate enforcement.
    """

    def __init__(self) -> None:
        """Initialize the rate limiter with configuration-based limits."""
        # Load rate limits from configuration
        config = get_config()

        # Handle both new Pydantic config and legacy dict format
        if hasattr(config, "chat"):
            # New Pydantic config system
            # pylint: disable=no-member  # Pydantic FieldInfo dynamic attributes
            self.limits = {
                "global": config.chat.rate_limit_global,
                "local": config.chat.rate_limit_local,
                "say": config.chat.rate_limit_say,
                "party": config.chat.rate_limit_party,
                "whisper": config.chat.rate_limit_whisper,
                "system": 100,  # System messages - not in config
                "admin": 50,  # Admin channel - not in config
            }
            self.enabled = True
        else:
            # Legacy dict format (for backward compatibility with tests)
            # This branch should never execute in production since get_config() always returns AppConfig
            # which has a "chat" attribute. Kept for test compatibility where config may be a dict.
            chat_config = config.get("chat", {})  # type: ignore[attr-defined,unused-ignore]  # Reason: Legacy dict format for test compatibility, config may be dict in tests but AppConfig in production, mypy cannot verify dict.get on AppConfig
            rate_limiting_config = chat_config.get("rate_limiting", {})
            default_limits = {
                "global": 10,
                "local": 20,
                "say": 15,
                "party": 30,
                "whisper": 5,
                "system": 100,
                "admin": 50,
            }
            self.limits = rate_limiting_config.get("limits", default_limits)
            self.enabled = rate_limiting_config.get("enabled", True)

        # Sliding window storage: {player_id: {channel: deque(timestamps)}}
        self.windows: defaultdict[str, defaultdict[str, deque[float]]] = defaultdict(lambda: defaultdict(deque))

        # Window size in seconds (1 minute)
        self.window_size = 60

        # Chat logger for AI processing
        self.chat_logger = chat_logger

        logger.info("RateLimiter initialized", limits=self.limits, enabled=self.enabled)

    def set_limit(self, channel: str, limit: int) -> None:
        """
        Set a custom rate limit for a channel.

        Args:
            channel: Channel name
            limit: Messages per minute
        """
        self.limits[channel] = limit
        logger.info("Rate limit updated", channel=channel, limit=limit)

    def get_limit(self, channel: str) -> int:
        """
        Get the current rate limit for a channel.

        Args:
            channel: Channel name

        Returns:
            Messages per minute limit
        """
        return self.limits.get(channel, 10)  # Default to 10 if not configured

    def _cleanup_old_entries(self, player_id: str, channel: str) -> None:
        """
        Remove timestamps older than the window size.

        Args:
            player_id: Player ID
            channel: Channel name
        """
        current_time = time.time()
        window = self.windows[player_id][channel]

        # Remove timestamps older than window_size seconds
        while window and current_time - window[0] > self.window_size:
            window.popleft()

    def check_rate_limit(self, player_id: str, channel: str, player_name: str | None = None) -> bool:
        """
        Check if a player is within rate limits for a channel.

        Args:
            player_id: Player ID
            channel: Channel name
            player_name: Player name for logging

        Returns:
            True if within limits, False if rate limited
        """
        try:
            # If rate limiting is disabled, always allow
            if not self.enabled:
                return True

            # Get the limit for this channel
            limit = self.get_limit(channel)

            # Clean up old entries
            self._cleanup_old_entries(player_id, channel)

            # Get current message count
            current_count = len(self.windows[player_id][channel])

            # Check if within limits
            within_limits = current_count < limit

            if not within_limits:
                # Log rate limit violation for AI processing
                self.chat_logger.log_rate_limit_violation(
                    player_id=player_id,
                    player_name=player_name or player_id,
                    channel=channel,
                    message_count=current_count,
                    limit=limit,
                )

                logger.warning(
                    "Rate limit exceeded",
                    player_id=player_id,
                    player_name=player_name,
                    channel=channel,
                    current_count=current_count,
                    limit=limit,
                )

            return within_limits

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Rate limit check errors unpredictable, fail open
            logger.error("Error checking rate limit", error=str(e), player_id=player_id, channel=channel)
            # On error, allow the message (fail open)
            return True

    def record_message(self, player_id: str, channel: str, player_name: str | None = None) -> None:
        """
        Record a message for rate limiting.

        Args:
            player_id: Player ID
            channel: Channel name
            player_name: Player name for logging
        """
        try:
            current_time = time.time()

            # Clean up old entries first
            self._cleanup_old_entries(player_id, channel)

            # Add current timestamp
            self.windows[player_id][channel].append(current_time)

            # Get updated count for logging
            current_count = len(self.windows[player_id][channel])
            limit = self.get_limit(channel)

            logger.debug(
                "Message recorded for rate limiting",
                player_id=player_id,
                player_name=player_name,
                channel=channel,
                current_count=current_count,
                limit=limit,
            )

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Rate limit recording errors unpredictable, must handle gracefully
            logger.error(
                "Error recording message for rate limiting", error=str(e), player_id=player_id, channel=channel
            )

    def get_player_stats(self, player_id: str) -> dict[str, Any]:
        """
        Get rate limiting statistics for a player.

        Args:
            player_id: Player ID

        Returns:
            Dictionary with channel statistics
        """
        stats = {}

        for channel in self.limits.keys():
            self._cleanup_old_entries(player_id, channel)
            current_count = len(self.windows[player_id][channel])
            limit = self.get_limit(channel)

            stats[channel] = {
                "current_count": current_count,
                "limit": limit,
                "remaining": max(0, limit - current_count),
                "percentage_used": (current_count / limit * 100) if limit > 0 else 0,
            }

        return stats

    def reset_player_limits(self, player_id: str, channel: str | None = None) -> None:
        """
        Reset rate limiting for a player.

        Args:
            player_id: Player ID
            channel: Specific channel to reset (None for all channels)
        """
        try:
            if channel:
                if player_id in self.windows and channel in self.windows[player_id]:
                    self.windows[player_id][channel].clear()
                    logger.info("Rate limits reset for player", player_id=player_id, channel=channel)
            else:
                if player_id in self.windows:
                    self.windows[player_id].clear()
                    logger.info("All rate limits reset for player", player_id=player_id)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Rate limit reset errors unpredictable, must handle gracefully
            logger.error("Error resetting rate limits", error=str(e), player_id=player_id, channel=channel)

    def get_system_stats(self) -> dict[str, Any]:
        """
        Get system-wide rate limiting statistics.

        Returns:
            Dictionary with system statistics
        """
        try:
            total_players = len(self.windows)
            total_channels = len(self.limits)

            # Count active rate limiters (players with recent activity)
            active_players = 0
            total_messages = 0

            current_time = time.time()
            for _player_id, channels in self.windows.items():
                player_active = False
                for _channel, window in channels.items():
                    # Clean up old entries
                    while window and current_time - window[0] > self.window_size:
                        window.popleft()

                    if len(window) > 0:
                        player_active = True
                        total_messages += len(window)

                if player_active:
                    active_players += 1

            return {
                "total_players": total_players,
                "active_players": active_players,
                "total_channels": total_channels,
                "total_messages_in_window": total_messages,
                "window_size_seconds": self.window_size,
                "limits": self.limits.copy(),
            }

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Stats retrieval errors unpredictable, must return empty dict
            logger.error("Error getting system stats", error=str(e))
            return {}

    def is_player_rate_limited(self, player_id: str, channel: str) -> bool:
        """
        Check if a player is currently rate limited on a channel.

        Args:
            player_id: Player ID
            channel: Channel name

        Returns:
            True if rate limited, False otherwise
        """
        return not self.check_rate_limit(player_id, channel)

    def get_remaining_messages(self, player_id: str, channel: str) -> int:
        """
        Get the number of remaining messages a player can send on a channel.

        Args:
            player_id: Player ID
            channel: Channel name

        Returns:
            Number of remaining messages
        """
        try:
            self._cleanup_old_entries(player_id, channel)
            current_count = len(self.windows[player_id][channel])
            limit = self.get_limit(channel)
            return max(0, limit - current_count)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Remaining messages calculation errors unpredictable, must return 0
            logger.error("Error getting remaining messages", error=str(e), player_id=player_id, channel=channel)
            return 0


# Global rate limiter instance
rate_limiter = RateLimiter()
