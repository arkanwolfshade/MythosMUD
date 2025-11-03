"""
NATS message retry handler with exponential backoff.

Implements resilient message delivery with configurable retry logic
and exponential backoff to handle transient failures.

AI: Exponential backoff prevents overwhelming a recovering service.
"""

import asyncio
import random
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class RetryableMessage:
    """
    Message that can be retried with tracking metadata.

    Stores message data along with retry tracking information.

    AI: Tracks retry attempts and timing for exponential backoff.
    """

    subject: str
    data: dict[str, Any]
    attempt: int
    first_attempt_time: datetime


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

    config: RetryConfig

    def __init__(self, max_retries: int = 3, base_delay: float = 1.0, max_delay: float = 60.0):
        """
        Initialize retry handler.

        Args:
            max_retries: Maximum number of retry attempts
            base_delay: Base delay in seconds for exponential backoff
            max_delay: Maximum delay in seconds

        AI: Allows per-handler configuration while providing sensible defaults.
        """
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.total_retries = 0

        # Create config object for get_config() and update_config() methods
        self.config = RetryConfig(max_attempts=max_retries, base_delay=base_delay, max_delay=max_delay)

        logger.info(
            "NATSRetryHandler initialized",
            max_retries=self.max_retries,
            base_delay=self.base_delay,
            max_delay=self.max_delay,
        )

    def calculate_backoff(self, attempt: int) -> float:
        """
        Calculate exponential backoff delay with jitter.

        Args:
            attempt: Current attempt number (0-indexed)

        Returns:
            Delay in seconds with jitter

        AI: Jitter prevents thundering herd problem.
        """
        delay = self.base_delay * (2**attempt)
        delay = min(delay, self.max_delay)

        # Add jitter (±25%)
        jitter = delay * 0.25
        delay = delay + random.uniform(-jitter, jitter)

        return max(0, delay)

    async def should_retry(self, message: RetryableMessage, error: Exception) -> bool:
        """
        Determine if a message should be retried.

        Args:
            message: Message that failed
            error: Exception that caused failure

        Returns:
            True if should retry, False otherwise

        AI: Check retry count against threshold.
        """
        return message.attempt < self.max_retries

    async def retry_async(self, func: Callable, message: RetryableMessage) -> None:
        """
        Retry a function with exponential backoff.

        Args:
            func: Async function to retry
            message: Retryable message to process

        AI: Increments attempt counter and waits for backoff delay.
        """
        # Calculate backoff delay
        delay = self.calculate_backoff(message.attempt)

        # Wait for backoff
        if delay > 0:
            await asyncio.sleep(delay)

        # Increment attempt counter
        message.attempt += 1
        self.total_retries += 1

        # Execute the function
        await func(message)

    def get_retry_stats(self) -> dict[str, Any]:
        """
        Get retry statistics.

        Returns:
            Dictionary with retry metrics

        AI: For monitoring and alerting on retry rates.
        """
        return {
            "total_retries": self.total_retries,
            "max_retries": self.max_retries,
            "base_delay": self.base_delay,
            "max_delay": self.max_delay,
        }

    async def retry_with_backoff(self, func: Callable, *args, **kwargs) -> tuple[bool, Any]:
        """
        Retry async function with exponential backoff.

        Attempts the function up to max_retries times, with increasing
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

        for attempt in range(self.max_retries):
            try:
                logger.debug("Attempting function call", attempt=attempt + 1, max_attempts=self.max_retries)

                result = await func(*args, **kwargs)

                if attempt > 0:
                    logger.info(
                        "Function succeeded after retries",
                        attempt=attempt + 1,
                        max_attempts=self.max_retries,
                    )

                return True, result

            except Exception as e:
                last_error = e

                # Don't sleep after last attempt
                if attempt < self.max_retries - 1:
                    delay = self.calculate_backoff(attempt)

                    logger.warning(
                        "Function failed, retrying with backoff",
                        attempt=attempt + 1,
                        max_attempts=self.max_retries,
                        delay=delay,
                        error=str(e),
                        error_type=type(e).__name__,
                    )

                    await asyncio.sleep(delay)
                else:
                    logger.error(
                        "Function failed after all retries",
                        attempts=self.max_retries,
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
