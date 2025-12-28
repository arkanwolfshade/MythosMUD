"""
Retry utilities for transient database errors.

This module provides retry decorators and helpers for handling transient
database errors with exponential backoff.
"""

import asyncio
import time
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Type variables for generic function signatures
T = TypeVar("T")
F = TypeVar("F", bound=Callable[..., Any])


# Transient database errors that should be retried
TRANSIENT_ERRORS = (
    "PoolAcquireTimeoutError",
    "PostgresConnectionError",
    "ConnectionDoesNotExistError",
    "InterfaceError",
    "OperationalError",
)


def is_transient_error(error: Exception) -> bool:
    """
    Check if an error is a transient database error that should be retried.

    Args:
        error: The exception to check

    Returns:
        bool: True if the error is transient and should be retried
    """
    error_type = type(error).__name__
    error_module = type(error).__module__

    # Check error type name
    if error_type in TRANSIENT_ERRORS:
        return True

    # Check for asyncpg transient errors
    if "asyncpg" in error_module:
        if "PoolAcquireTimeoutError" in error_type or "PostgresConnectionError" in error_type:
            return True

    # Check for psycopg2 transient errors
    if "psycopg2" in error_module:
        if "OperationalError" in error_type or "InterfaceError" in error_type:
            # Check error message for transient indicators
            error_msg = str(error).lower()
            if any(indicator in error_msg for indicator in ["connection", "timeout", "network", "temporary", "retry"]):
                return True

    return False


def retry_with_backoff(
    max_attempts: int = 3,
    initial_delay: float = 1.0,
    max_delay: float = 10.0,
    exponential_base: float = 2.0,
    retry_on: tuple[type[Exception], ...] | None = None,
) -> Callable[[F], F]:
    """
    Decorator to retry a function with exponential backoff on transient errors.

    This decorator automatically detects whether the decorated function is async or sync
    and uses the appropriate sleep mechanism:
    - Async functions: Uses `asyncio.sleep()` (non-blocking)
    - Sync functions: Uses `time.sleep()` (blocking, but only called from sync contexts)

    USAGE GUIDELINES:
    - Async functions: Safe to use in async contexts, will not block the event loop
    - Sync functions: Should ONLY be called from sync contexts. If called from async,
      wrap with `asyncio.to_thread()` at the call site to avoid blocking.

    Args:
        max_attempts: Maximum number of retry attempts (default: 3)
        initial_delay: Initial delay in seconds (default: 1.0)
        max_delay: Maximum delay in seconds (default: 10.0)
        exponential_base: Base for exponential backoff (default: 2.0)
        retry_on: Specific exception types to retry on (default: None, uses is_transient_error)

    Returns:
        Decorated function with retry logic

    Example:
        @retry_with_backoff(max_attempts=3, initial_delay=1.0)
        async def get_player(player_id: str):
            # Function that may fail with transient errors
            ...
    """

    def decorator(func: F) -> F:
        if asyncio.iscoroutinefunction(func):

            @wraps(func)
            async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
                last_error: Exception | None = None
                for attempt in range(1, max_attempts + 1):
                    try:
                        return await func(*args, **kwargs)
                    except Exception as e:
                        last_error = e

                        # Check if we should retry this error
                        should_retry = False
                        if retry_on:
                            should_retry = isinstance(e, retry_on)
                        else:
                            should_retry = is_transient_error(e)

                        if not should_retry or attempt >= max_attempts:
                            # Don't retry or out of attempts
                            logger.error(
                                "Function failed after retries",
                                function=func.__name__,
                                attempt=attempt,
                                max_attempts=max_attempts,
                                error=str(e),
                                error_type=type(e).__name__,
                                should_retry=should_retry,
                            )
                            raise

                        # Calculate delay with exponential backoff
                        delay = min(initial_delay * (exponential_base ** (attempt - 1)), max_delay)

                        logger.warning(
                            "Transient error detected, retrying",
                            function=func.__name__,
                            attempt=attempt,
                            max_attempts=max_attempts,
                            delay=delay,
                            error=str(e),
                            error_type=type(e).__name__,
                        )

                        await asyncio.sleep(delay)

                # This should never be reached, but mypy needs it
                if last_error:
                    raise last_error
                raise RuntimeError("Retry logic failed unexpectedly")

            return async_wrapper  # type: ignore[return-value]
        else:

            @wraps(func)
            def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
                last_error: Exception | None = None
                for attempt in range(1, max_attempts + 1):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_error = e

                        # Check if we should retry this error
                        should_retry = False
                        if retry_on:
                            should_retry = isinstance(e, retry_on)
                        else:
                            should_retry = is_transient_error(e)

                        if not should_retry or attempt >= max_attempts:
                            # Don't retry or out of attempts
                            logger.error(
                                "Function failed after retries",
                                function=func.__name__,
                                attempt=attempt,
                                max_attempts=max_attempts,
                                error=str(e),
                                error_type=type(e).__name__,
                                should_retry=should_retry,
                            )
                            raise

                        # Calculate delay with exponential backoff
                        delay = min(initial_delay * (exponential_base ** (attempt - 1)), max_delay)

                        logger.warning(
                            "Transient error detected, retrying",
                            function=func.__name__,
                            attempt=attempt,
                            max_attempts=max_attempts,
                            delay=delay,
                            error=str(e),
                            error_type=type(e).__name__,
                        )

                        time.sleep(delay)

                # This should never be reached, but mypy needs it
                if last_error:
                    raise last_error
                raise RuntimeError("Retry logic failed unexpectedly")

            return sync_wrapper  # type: ignore[return-value]

    return decorator
