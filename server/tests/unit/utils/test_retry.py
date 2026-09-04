"""
Unit tests for retry utilities.

Tests the retry decorator and retry logic.
"""

import pytest

from server.utils.retry import is_transient_error, retry_with_backoff


def test_is_transient_error_transient():
    """Test is_transient_error() identifies transient errors."""

    class PoolAcquireTimeoutError(Exception):
        pass

    error = PoolAcquireTimeoutError("Timeout")
    assert is_transient_error(error) is True


def test_is_transient_error_non_transient():
    """Test is_transient_error() returns False for non-transient errors."""
    error = ValueError("Not transient")
    assert is_transient_error(error) is False


def test_is_transient_error_wrapped_connection_closed():
    """DatabaseError wrapping asyncpg closed-connection must still retry (e2e regression)."""

    class DatabaseError(Exception):
        pass

    err = DatabaseError(
        "Database error retrieving player by ID 'x': "
        "(sqlalchemy.dialects.postgresql.asyncpg.Error) "
        "<class 'asyncpg.exceptions.ConnectionDoesNotExistError'>: "
        "connection was closed in the middle of operation"
    )
    assert is_transient_error(err) is True


def test_is_transient_error_cause_chain_connection_closed():
    """__cause__ ConnectionDoesNotExistError makes the outer wrapper transient."""

    class ConnectionDoesNotExistError(Exception):
        pass

    class DatabaseError(Exception):
        pass

    cause = ConnectionDoesNotExistError("connection was closed in the middle of operation")
    outer = DatabaseError("wrapped")
    outer.__cause__ = cause
    assert is_transient_error(outer) is True


@pytest.mark.asyncio
async def test_retry_retries_wrapped_connection_closed_then_succeeds():
    """Retry decorator must not treat wrapped closed-connection as final on attempt 1."""
    call_count = 0

    class DatabaseError(Exception):
        pass

    @retry_with_backoff(max_attempts=3, initial_delay=0.01)
    async def get_player_by_id() -> str:
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise DatabaseError(
                "Database error retrieving player: ConnectionDoesNotExistError: "
                "connection was closed in the middle of operation"
            )
        return "ok"

    assert await get_player_by_id() == "ok"
    assert call_count == 2


def test_retry_with_backoff_success():
    """Test retry_with_backoff() succeeds on first attempt."""
    call_count = 0

    @retry_with_backoff(max_attempts=3, initial_delay=0.01)
    def test_func():
        nonlocal call_count
        call_count += 1
        return "success"

    result = test_func()
    assert result == "success"
    assert call_count == 1


def test_retry_with_backoff_failure_then_success():
    """Test retry_with_backoff() retries on failure then succeeds."""
    call_count = 0

    class TransientError(Exception):
        pass

    @retry_with_backoff(max_attempts=3, initial_delay=0.01, retry_on=(TransientError,))
    def test_func():
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise TransientError("Test error")
        return "success"

    result = test_func()
    assert result == "success"
    assert call_count == 2


@pytest.mark.asyncio
async def test_retry_with_backoff_async_success():
    """Test retry_with_backoff() with async function succeeds on first attempt."""
    call_count = 0

    @retry_with_backoff(max_attempts=3, initial_delay=0.01)
    async def test_func():
        nonlocal call_count
        call_count += 1
        return "success"

    result = await test_func()
    assert result == "success"
    assert call_count == 1


@pytest.mark.asyncio
async def test_retry_with_backoff_async_failure_then_success():
    """Test retry_with_backoff() with async function retries on failure then succeeds."""
    call_count = 0

    class TransientError(Exception):
        pass

    @retry_with_backoff(max_attempts=3, initial_delay=0.01, retry_on=(TransientError,))
    async def test_func():
        nonlocal call_count
        call_count += 1
        if call_count < 2:
            raise TransientError("Test error")
        return "success"

    result = await test_func()
    assert result == "success"
    assert call_count == 2
