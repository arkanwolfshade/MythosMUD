"""
Rate limiting utilities for MythosMUD API endpoints.

This module provides rate limiting functionality for preventing abuse
of API endpoints, particularly for stats rolling and other sensitive operations.
"""

import time
from collections import defaultdict

from ..exceptions import RateLimitError


class RateLimiter:
    """
    Simple in-memory rate limiter for API endpoints.

    This rate limiter tracks requests per user and enforces limits
    based on a sliding window approach.
    """

    def __init__(self, max_requests: int = 10, window_seconds: int = 60):
        """
        Initialize the rate limiter.

        Args:
            max_requests: Maximum number of requests allowed in the window
            window_seconds: Time window in seconds for rate limiting
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests: dict[str, list[float]] = defaultdict(list)

    def check_rate_limit(self, user_id: str) -> bool:
        """
        Check if a user has exceeded the rate limit.

        Args:
            user_id: The user's ID

        Returns:
            bool: True if rate limit not exceeded, False if exceeded
        """
        current_time = time.time()

        # Remove old requests outside the window
        self.requests[user_id] = [
            request_time
            for request_time in self.requests[user_id]
            if current_time - request_time < self.window_seconds
        ]

        # Check if limit exceeded
        if len(self.requests[user_id]) >= self.max_requests:
            return False

        # Add current request
        self.requests[user_id].append(current_time)
        return True

    def get_rate_limit_info(self, user_id: str) -> dict:
        """
        Get rate limit information for a user.

        Args:
            user_id: The user's ID

        Returns:
            dict: Rate limit information including attempts, limits, and reset time
        """
        current_time = time.time()
        requests = self.requests[user_id]

        # Filter recent requests
        recent_requests = [
            request_time for request_time in requests
            if current_time - request_time < self.window_seconds
        ]

        # Calculate reset time (when the oldest request will expire)
        reset_time = 0
        if recent_requests:
            oldest_request = min(recent_requests)
            reset_time = oldest_request + self.window_seconds

        return {
            "attempts": len(recent_requests),
            "max_attempts": self.max_requests,
            "window_seconds": self.window_seconds,
            "attempts_remaining": max(0, self.max_requests - len(recent_requests)),
            "reset_time": reset_time,
            "retry_after": max(0, int(reset_time - current_time)) if reset_time > current_time else 0,
        }

    def enforce_rate_limit(self, user_id: str) -> None:
        """
        Enforce rate limiting for a user.

        Args:
            user_id: The user's ID

        Raises:
            RateLimitError: If rate limit is exceeded
        """
        if not self.check_rate_limit(user_id):
            info = self.get_rate_limit_info(user_id)
            raise RateLimitError(
                f"Rate limit exceeded. Maximum {self.max_requests} requests per {self.window_seconds} seconds.",
                limit_type="api_endpoint",
                retry_after=info["retry_after"]
            )


# Global rate limiters for different endpoints
stats_roll_limiter = RateLimiter(max_requests=10, window_seconds=60)  # 10 rolls per minute
character_creation_limiter = RateLimiter(max_requests=5, window_seconds=300)  # 5 creations per 5 minutes
