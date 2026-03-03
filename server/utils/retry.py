"""
Retry utilities for transient database errors.

This module provides retry decorators and helpers for handling transient
database errors with exponential backoff.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Retry utilities require many parameters for complete retry configuration and context

import asyncio
import time
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar, cast

from anyio import sleep

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)

# Transient database errors that should be retried
TRANSIENT_ERRORS = (
    "PoolAcquireTimeoutError",
    "PostgresConnectionError",
    "ConnectionDoesNotExistError",
    "InterfaceError",
    "OperationalError",
)

# Message substrings that indicate transient psycopg2 errors
PSYCOPG2_TRANSIENT_INDICATORS = ("connection", "timeout", "network", "temporary", "retry")


def _is_asyncpg_transient(error_type: str, error_module: str) -> bool:
    """Return True if error is an asyncpg transient error."""
    return "asyncpg" in error_module and (
        "PoolAcquireTimeoutError" in error_type or "PostgresConnectionError" in error_type
    )


def _is_psycopg2_transient(error: Exception, error_type: str, error_module: str) -> bool:
    """Return True if error is a psycopg2 transient error (OperationalError/InterfaceError with transient message)."""
    if "psycopg2" not in error_module:
        return False
    if "OperationalError" not in error_type and "InterfaceError" not in error_type:
        return False
    error_msg = str(error).lower()
    return any(ind in error_msg for ind in PSYCOPG2_TRANSIENT_INDICATORS)


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

    if error_type in TRANSIENT_ERRORS:
        return True
    if _is_asyncpg_transient(error_type, error_module):
        return True
    if _is_psycopg2_transient(error, error_type, error_module):
        return True
    return False


def _should_retry_error(
    error: Exception, retry_on: tuple[type[Exception], ...] | None, attempt: int, max_attempts: int
) -> bool:
    """Determine if an error should be retried."""
    if attempt >= max_attempts:
        return False

    if retry_on:
        return isinstance(error, retry_on)

    return is_transient_error(error)


def _calculate_retry_delay(attempt: int, initial_delay: float, max_delay: float, exponential_base: float) -> float:
    """Calculate delay for retry attempt with exponential backoff."""
    return min(initial_delay * (exponential_base ** (attempt - 1)), max_delay)


def _log_retry_failure(func_name: str, attempt: int, max_attempts: int, error: Exception, should_retry: bool) -> None:
    """Log retry failure."""
    logger.error(
        "Function failed after retries",
        function=func_name,
        attempt=attempt,
        max_attempts=max_attempts,
        error=str(error),
        error_type=type(error).__name__,
        should_retry=should_retry,
    )


def _log_retry_attempt(func_name: str, attempt: int, max_attempts: int, delay: float, error: Exception) -> None:
    """Log retry attempt."""
    logger.warning(
        "Transient error detected, retrying",
        function=func_name,
        attempt=attempt,
        max_attempts=max_attempts,
        delay=delay,
        error=str(error),
        error_type=type(error).__name__,
    )


# Type variables for generic function signatures
T = TypeVar("T")
F = TypeVar("F", bound=Callable[..., Any])


def _create_async_wrapper(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Retry wrapper creation requires many parameters for complete retry configuration
    func: Callable[..., Any],
    max_attempts: int,
    initial_delay: float,
    max_delay: float,
    exponential_base: float,
    retry_on: tuple[type[Exception], ...] | None,
) -> Callable[..., Any]:
    """Create async wrapper function with retry logic."""

    @wraps(func)
    async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
        last_error: Exception | None = None
        for attempt in range(1, max_attempts + 1):
            try:
                return await func(*args, **kwargs)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Retry mechanism must catch all exceptions to determine retry behavior
                last_error = e

                should_retry = _should_retry_error(e, retry_on, attempt, max_attempts)

                if not should_retry:
                    _log_retry_failure(func.__name__, attempt, max_attempts, e, should_retry)
                    raise

                delay = _calculate_retry_delay(attempt, initial_delay, max_delay, exponential_base)
                _log_retry_attempt(func.__name__, attempt, max_attempts, delay, e)
                await sleep(delay)

        if last_error:
            raise last_error
        raise RuntimeError("Retry logic failed unexpectedly")

    return async_wrapper


def _create_sync_wrapper(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Retry wrapper creation requires many parameters for complete retry configuration
    func: Callable[..., Any],
    max_attempts: int,
    initial_delay: float,
    max_delay: float,
    exponential_base: float,
    retry_on: tuple[type[Exception], ...] | None,
) -> Callable[..., Any]:
    """Create sync wrapper function with retry logic."""

    @wraps(func)
    def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
        last_error: Exception | None = None
        for attempt in range(1, max_attempts + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Retry mechanism must catch all exceptions to determine retry behavior
                last_error = e

                should_retry = _should_retry_error(e, retry_on, attempt, max_attempts)

                if not should_retry:
                    _log_retry_failure(func.__name__, attempt, max_attempts, e, should_retry)
                    raise

                delay = _calculate_retry_delay(attempt, initial_delay, max_delay, exponential_base)
                _log_retry_attempt(func.__name__, attempt, max_attempts, delay, e)
                # Sync-only: must not be called from async request handlers.
                time.sleep(delay)

        if last_error:
            raise last_error
        raise RuntimeError("Retry logic failed unexpectedly")

    return sync_wrapper


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
            return cast(
                F,
                _create_async_wrapper(func, max_attempts, initial_delay, max_delay, exponential_base, retry_on),
            )
        return cast(
            F,
            _create_sync_wrapper(func, max_attempts, initial_delay, max_delay, exponential_base, retry_on),
        )

    return decorator
