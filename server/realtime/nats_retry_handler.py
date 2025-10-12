"""
NATS message retry handler with exponential backoff.

Implements resilient message delivery with configurable retry logic
and exponential backoff to handle transient failures.

AI: Exponential backoff prevents overwhelming a recovering service.
"""

import asyncio
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from ..logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class RetryConfig:
    """
    Configuration for retry behavior.

    Defines retry parameters for handling transient failures.

    AI: Exponential backoff with max delay prevents retry storms.
    """

    max_attempts: int = 3
    base_delay: float = 1.0  # seconds
    max_delay: float = 30.0  # seconds
    exponential_base: float = 2.0  # Doubles delay each retry

    def calculate_delay(self, attempt: int) -> float:
        """
        Calculate delay for a given attempt number.

        Uses exponential backoff capped at max_delay.

        Args:
            attempt: Attempt number (0-indexed)

        Returns:
            Delay in seconds

        AI: Formula: min(base_delay * (base^attempt), max_delay)
        """
        delay = self.base_delay * (self.exponential_base**attempt)
        return min(delay, self.max_delay)


class NATSRetryHandler:
    """
    Handle NATS message retries with exponential backoff.

    Provides configurable retry logic for handling transient failures
    in NATS message delivery. Uses exponential backoff to avoid
    overwhelming recovering services.

    AI: Critical for handling network partitions and temporary outages.
    """

    def __init__(self, config: RetryConfig | None = None):
        """
        Initialize retry handler.

        Args:
            config: Retry configuration (uses defaults if None)

        AI: Allows per-handler configuration while providing sensible defaults.
        """
        self.config = config or RetryConfig()

        logger.info(
            "NATSRetryHandler initialized",
            max_attempts=self.config.max_attempts,
            base_delay=self.config.base_delay,
            max_delay=self.config.max_delay,
        )

    async def retry_with_backoff(self, func: Callable, *args, **kwargs) -> tuple[bool, Any]:
        """
        Retry async function with exponential backoff.

        Attempts the function up to max_attempts times, with increasing
        delays between attempts. Returns success status and result/error.

        Args:
            func: Async function to retry
            *args: Positional arguments for func
            **kwargs: Keyword arguments for func

        Returns:
            Tuple of (success: bool, result/error: Any)
            - If successful: (True, function_result)
            - If all retries fail: (False, last_exception)

        AI: Caller can decide whether to log error, add to DLQ, etc.
        """
        last_error = None

        for attempt in range(self.config.max_attempts):
            try:
                logger.debug("Attempting function call", attempt=attempt + 1, max_attempts=self.config.max_attempts)

                result = await func(*args, **kwargs)

                if attempt > 0:
                    logger.info(
                        "Function succeeded after retries",
                        attempt=attempt + 1,
                        max_attempts=self.config.max_attempts,
                    )

                return True, result

            except Exception as e:
                last_error = e

                # Don't sleep after last attempt
                if attempt < self.config.max_attempts - 1:
                    delay = self.config.calculate_delay(attempt)

                    logger.warning(
                        "Function failed, retrying with backoff",
                        attempt=attempt + 1,
                        max_attempts=self.config.max_attempts,
                        delay=delay,
                        error=str(e),
                        error_type=type(e).__name__,
                    )

                    await asyncio.sleep(delay)
                else:
                    logger.error(
                        "Function failed after all retries",
                        attempts=self.config.max_attempts,
                        error=str(e),
                        error_type=type(e).__name__,
                    )

        return False, last_error

    def get_config(self) -> RetryConfig:
        """
        Get current retry configuration.

        Returns:
            Current RetryConfig

        AI: Useful for debugging and monitoring.
        """
        return self.config

    def update_config(self, **kwargs) -> None:
        """
        Update retry configuration dynamically.

        Allows runtime adjustment of retry parameters.

        Args:
            **kwargs: RetryConfig fields to update

        AI: Use sparingly - mainly for testing or emergency tuning.
        """
        for key, value in kwargs.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)
                logger.info("Retry config updated", field=key, value=value)
            else:
                logger.warning("Unknown config field", field=key)
