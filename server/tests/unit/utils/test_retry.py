"""
Unit tests for retry utilities.

Tests retry decorators and transient error detection.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.utils.retry import is_transient_error, retry_with_backoff


def test_is_transient_error_transient_error_names():
    """Test is_transient_error identifies transient error names."""
    class PoolAcquireTimeoutError(Exception):
        pass
    
    class PostgresConnectionError(Exception):
        pass
    
    class ConnectionDoesNotExistError(Exception):
        pass
    
    class InterfaceError(Exception):
        pass
    
    class OperationalError(Exception):
        pass
    
    assert is_transient_error(PoolAcquireTimeoutError()) is True
    assert is_transient_error(PostgresConnectionError()) is True
    assert is_transient_error(ConnectionDoesNotExistError()) is True
    assert is_transient_error(InterfaceError()) is True
    assert is_transient_error(OperationalError()) is True


def test_is_transient_error_asyncpg_errors():
    """Test is_transient_error identifies asyncpg errors."""
    class AsyncPGPoolAcquireTimeoutError(Exception):
        __module__ = "asyncpg.pool"
    
    class AsyncPGPostgresConnectionError(Exception):
        __module__ = "asyncpg.exceptions"
    
    assert is_transient_error(AsyncPGPoolAcquireTimeoutError()) is True
    assert is_transient_error(AsyncPGPostgresConnectionError()) is True


def test_is_transient_error_psycopg2_errors():
    """Test is_transient_error identifies psycopg2 transient errors."""
    class Psycopg2OperationalError(Exception):
        __module__ = "psycopg2"
    
    class Psycopg2InterfaceError(Exception):
        __module__ = "psycopg2"
    
    error1 = Psycopg2OperationalError("connection timeout")
    error2 = Psycopg2InterfaceError("network error")
    error3 = Psycopg2OperationalError("temporary failure")
    
    assert is_transient_error(error1) is True
    assert is_transient_error(error2) is True
    assert is_transient_error(error3) is True


def test_is_transient_error_non_transient():
    """Test is_transient_error returns False for non-transient errors."""
    assert is_transient_error(ValueError("Invalid input")) is False
    assert is_transient_error(KeyError("Missing key")) is False
    assert is_transient_error(RuntimeError("Runtime error")) is False


def test_retry_with_backoff_sync_success():
    """Test retry_with_backoff with sync function that succeeds."""
    @retry_with_backoff(max_attempts=3)
    def test_func():
        return "success"
    
    assert test_func() == "success"


def test_retry_with_backoff_sync_transient_error():
    """Test retry_with_backoff retries on transient errors."""
    attempt_count = 0
    
    class PoolAcquireTimeoutError(Exception):
        pass
    
    @retry_with_backoff(max_attempts=3, initial_delay=0.01)
    def test_func():
        nonlocal attempt_count
        attempt_count += 1
        if attempt_count < 2:
            raise PoolAcquireTimeoutError("Connection timeout")
        return "success"
    
    assert test_func() == "success"
    assert attempt_count == 2


def test_retry_with_backoff_sync_max_attempts():
    """Test retry_with_backoff stops after max attempts."""
    attempt_count = 0
    
    class PoolAcquireTimeoutError(Exception):
        pass
    
    @retry_with_backoff(max_attempts=3, initial_delay=0.01)
    def test_func():
        nonlocal attempt_count
        attempt_count += 1
        raise PoolAcquireTimeoutError("Connection timeout")
    
    with pytest.raises(PoolAcquireTimeoutError):
        test_func()
    
    assert attempt_count == 3


def test_retry_with_backoff_sync_non_transient_error():
    """Test retry_with_backoff does not retry non-transient errors."""
    attempt_count = 0
    
    @retry_with_backoff(max_attempts=3, initial_delay=0.01)
    def test_func():
        nonlocal attempt_count
        attempt_count += 1
        raise ValueError("Not transient")
    
    with pytest.raises(ValueError):
        test_func()
    
    assert attempt_count == 1


def test_retry_with_backoff_sync_custom_retry_on():
    """Test retry_with_backoff with custom retry_on exceptions."""
    attempt_count = 0
    
    @retry_with_backoff(max_attempts=3, initial_delay=0.01, retry_on=(ValueError,))
    def test_func():
        nonlocal attempt_count
        attempt_count += 1
        if attempt_count < 2:
            raise ValueError("Retry this")
        return "success"
    
    assert test_func() == "success"
    assert attempt_count == 2


@pytest.mark.asyncio
async def test_retry_with_backoff_async_success():
    """Test retry_with_backoff with async function that succeeds."""
    @retry_with_backoff(max_attempts=3)
    async def test_func():
        return "success"
    
    result = await test_func()
    assert result == "success"


@pytest.mark.asyncio
async def test_retry_with_backoff_async_transient_error():
    """Test retry_with_backoff retries async function on transient errors."""
    attempt_count = 0
    
    class PoolAcquireTimeoutError(Exception):
        pass
    
    @retry_with_backoff(max_attempts=3, initial_delay=0.01)
    async def test_func():
        nonlocal attempt_count
        attempt_count += 1
        if attempt_count < 2:
            raise PoolAcquireTimeoutError("Connection timeout")
        return "success"
    
    result = await test_func()
    assert result == "success"
    assert attempt_count == 2


@pytest.mark.asyncio
async def test_retry_with_backoff_async_max_attempts():
    """Test retry_with_backoff stops async function after max attempts."""
    attempt_count = 0
    
    class PoolAcquireTimeoutError(Exception):
        pass
    
    @retry_with_backoff(max_attempts=3, initial_delay=0.01)
    async def test_func():
        nonlocal attempt_count
        attempt_count += 1
        raise PoolAcquireTimeoutError("Connection timeout")
    
    with pytest.raises(PoolAcquireTimeoutError):
        await test_func()
    
    assert attempt_count == 3


@pytest.mark.asyncio
async def test_retry_with_backoff_async_exponential_backoff():
    """Test retry_with_backoff uses exponential backoff for async functions."""
    delays = []
    
    class PoolAcquireTimeoutError(Exception):
        pass
    
    @retry_with_backoff(max_attempts=3, initial_delay=0.01, exponential_base=2.0)
    async def test_func():
        raise PoolAcquireTimeoutError("Connection timeout")
    
    with patch("asyncio.sleep") as mock_sleep:
        async def sleep_side_effect(delay):
            delays.append(delay)
        
        mock_sleep.side_effect = sleep_side_effect
        
        with pytest.raises(PoolAcquireTimeoutError):
            await test_func()
        
        # Should have delays: 0.01, 0.02 (exponential backoff)
        assert len(delays) == 2
        assert delays[0] == 0.01
        assert delays[1] == 0.02


def test_retry_with_backoff_sync_exponential_backoff():
    """Test retry_with_backoff uses exponential backoff for sync functions."""
    delays = []
    
    class PoolAcquireTimeoutError(Exception):
        pass
    
    @retry_with_backoff(max_attempts=3, initial_delay=0.01, exponential_base=2.0)
    def test_func():
        raise PoolAcquireTimeoutError("Connection timeout")
    
    with patch("time.sleep") as mock_sleep:
        def sleep_side_effect(delay):
            delays.append(delay)
        
        mock_sleep.side_effect = sleep_side_effect
        
        with pytest.raises(PoolAcquireTimeoutError):
            test_func()
        
        # Should have delays: 0.01, 0.02 (exponential backoff)
        assert len(delays) == 2
        assert delays[0] == 0.01
        assert delays[1] == 0.02


def test_retry_with_backoff_max_delay_cap():
    """Test retry_with_backoff respects max_delay cap."""
    delays = []
    
    class PoolAcquireTimeoutError(Exception):
        pass
    
    @retry_with_backoff(max_attempts=5, initial_delay=1.0, max_delay=2.0, exponential_base=2.0)
    def test_func():
        raise PoolAcquireTimeoutError("Connection timeout")
    
    with patch("time.sleep") as mock_sleep:
        def sleep_side_effect(delay):
            delays.append(delay)
        
        mock_sleep.side_effect = sleep_side_effect
        
        with pytest.raises(PoolAcquireTimeoutError):
            test_func()
        
        # All delays should be capped at max_delay (2.0)
        assert all(d <= 2.0 for d in delays)
