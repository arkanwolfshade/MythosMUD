"""
Unit tests for NATS retry handler.

Tests the NATSRetryHandler class and related retry logic.
"""

from datetime import UTC, datetime
from unittest.mock import AsyncMock

import anyio
import pytest

from server.realtime.nats_retry_handler import NATSRetryHandler, RetryableMessage, RetryConfig


def test_retry_config_calculate_delay_base():
    """Test RetryConfig.calculate_delay() with base delay."""
    config = RetryConfig(base_delay=1.0, exponential_base=2.0, max_delay=30.0)
    assert config.calculate_delay(0) == 1.0
    assert config.calculate_delay(1) == 2.0
    assert config.calculate_delay(2) == 4.0
    assert config.calculate_delay(3) == 8.0


def test_retry_config_calculate_delay_capped():
    """Test RetryConfig.calculate_delay() respects max_delay."""
    config = RetryConfig(base_delay=1.0, exponential_base=2.0, max_delay=5.0)
    assert config.calculate_delay(0) == 1.0
    assert config.calculate_delay(1) == 2.0
    assert config.calculate_delay(2) == 4.0
    assert config.calculate_delay(3) == 5.0  # Capped at max_delay
    assert config.calculate_delay(10) == 5.0  # Still capped


def test_retry_config_defaults():
    """Test RetryConfig default values."""
    config = RetryConfig()
    assert config.max_attempts == 3
    assert config.base_delay == 1.0
    assert config.max_delay == 30.0
    assert config.exponential_base == 2.0


def test_retryable_message_init():
    """Test RetryableMessage initialization."""
    now = datetime.now(UTC)
    message = RetryableMessage(subject="test.subject", data={"key": "value"}, attempt=0, first_attempt_time=now)
    assert message.subject == "test.subject"
    assert message.data == {"key": "value"}
    assert message.attempt == 0
    assert message.first_attempt_time == now


def test_nats_retry_handler_init():
    """Test NATSRetryHandler initialization."""
    handler = NATSRetryHandler(max_retries=5, base_delay=2.0, max_delay=60.0)
    assert handler.max_retries == 5
    assert handler.base_delay == 2.0
    assert handler.max_delay == 60.0
    assert handler.total_retries == 0
    assert handler.config.max_attempts == 5
    assert handler.config.base_delay == 2.0
    assert handler.config.max_delay == 60.0


def test_nats_retry_handler_init_defaults():
    """Test NATSRetryHandler default values."""
    handler = NATSRetryHandler()
    assert handler.max_retries == 3
    assert handler.base_delay == 1.0
    assert handler.max_delay == 60.0


def test_calculate_backoff_base():
    """Test calculate_backoff() with base attempt."""
    handler = NATSRetryHandler(base_delay=1.0, max_delay=30.0)
    delay = handler.calculate_backoff(0)
    # Should be base_delay ± 25% jitter
    assert 0.75 <= delay <= 1.25


def test_calculate_backoff_exponential():
    """Test calculate_backoff() with exponential growth."""
    handler = NATSRetryHandler(base_delay=1.0, max_delay=30.0)
    delay1 = handler.calculate_backoff(1)
    delay2 = handler.calculate_backoff(2)
    # delay2 should be approximately 2x delay1 (with jitter)
    assert delay2 > delay1


def test_calculate_backoff_capped():
    """Test calculate_backoff() respects max_delay."""
    handler = NATSRetryHandler(base_delay=1.0, max_delay=5.0)
    delay = handler.calculate_backoff(10)  # Would be > max_delay without cap
    assert delay <= 5.0 * 1.25  # Max delay + jitter


def test_calculate_backoff_non_negative():
    """Test calculate_backoff() never returns negative."""
    handler = NATSRetryHandler(base_delay=0.1, max_delay=1.0)
    for attempt in range(10):
        delay = handler.calculate_backoff(attempt)
        assert delay >= 0


@pytest.mark.asyncio
async def test_should_retry_under_max():
    """Test should_retry() returns True when under max retries."""
    handler = NATSRetryHandler(max_retries=3)
    message = RetryableMessage(subject="test", data={}, attempt=0, first_attempt_time=datetime.now(UTC))
    result = await handler.should_retry(message, Exception("Error"))
    assert result is True


@pytest.mark.asyncio
async def test_should_retry_at_max():
    """Test should_retry() returns False when at max retries."""
    handler = NATSRetryHandler(max_retries=3)
    message = RetryableMessage(subject="test", data={}, attempt=3, first_attempt_time=datetime.now(UTC))
    result = await handler.should_retry(message, Exception("Error"))
    assert result is False


@pytest.mark.asyncio
async def test_should_retry_over_max():
    """Test should_retry() returns False when over max retries."""
    handler = NATSRetryHandler(max_retries=3)
    message = RetryableMessage(subject="test", data={}, attempt=5, first_attempt_time=datetime.now(UTC))
    result = await handler.should_retry(message, Exception("Error"))
    assert result is False


@pytest.mark.asyncio
async def test_retry_async_increments_attempt():
    """Test retry_async() increments attempt counter."""
    handler = NATSRetryHandler(base_delay=0.01, max_delay=1.0)
    message = RetryableMessage(subject="test", data={}, attempt=0, first_attempt_time=datetime.now(UTC))
    func = AsyncMock()
    await handler.retry_async(func, message)
    assert message.attempt == 1
    assert handler.total_retries == 1


@pytest.mark.asyncio
async def test_retry_async_calls_function():
    """Test retry_async() calls the provided function."""
    handler = NATSRetryHandler(base_delay=0.01, max_delay=1.0)
    message = RetryableMessage(subject="test", data={}, attempt=0, first_attempt_time=datetime.now(UTC))
    func = AsyncMock()
    await handler.retry_async(func, message)
    func.assert_awaited_once_with(message)


@pytest.mark.asyncio
async def test_retry_async_waits_for_backoff():
    """Test retry_async() waits for backoff delay."""
    handler = NATSRetryHandler(base_delay=0.1, max_delay=1.0)
    message = RetryableMessage(subject="test", data={}, attempt=0, first_attempt_time=datetime.now(UTC))
    func = AsyncMock()
    start_time = anyio.current_time()
    await handler.retry_async(func, message)
    elapsed = anyio.current_time() - start_time
    # Should have waited at least some time (with jitter, could be 0.075-0.125)
    assert elapsed >= 0.05  # Allow some margin for jitter


@pytest.mark.asyncio
async def test_retry_async_zero_delay():
    """Test retry_async() handles zero delay."""
    handler = NATSRetryHandler(base_delay=0.0, max_delay=1.0)
    message = RetryableMessage(subject="test", data={}, attempt=0, first_attempt_time=datetime.now(UTC))
    func = AsyncMock()
    await handler.retry_async(func, message)
    func.assert_awaited_once_with(message)


def test_get_retry_stats():
    """Test get_retry_stats() returns correct statistics."""
    handler = NATSRetryHandler(max_retries=5, base_delay=2.0, max_delay=60.0)
    handler.total_retries = 10
    stats = handler.get_retry_stats()
    assert stats["total_retries"] == 10
    assert stats["max_retries"] == 5
    assert stats["base_delay"] == 2.0
    assert stats["max_delay"] == 60.0


@pytest.mark.asyncio
async def test_retry_with_backoff_success_first_attempt():
    """Test retry_with_backoff() succeeds on first attempt."""
    handler = NATSRetryHandler(max_retries=3)
    func = AsyncMock(return_value="success")
    success, result = await handler.retry_with_backoff(func, "arg1", key="value")
    assert success is True
    assert result == "success"
    func.assert_awaited_once_with("arg1", key="value")


@pytest.mark.asyncio
async def test_retry_with_backoff_success_after_retries():
    """Test retry_with_backoff() succeeds after retries."""
    handler = NATSRetryHandler(max_retries=3, base_delay=0.01, max_delay=1.0)
    func = AsyncMock(side_effect=[Exception("Error1"), Exception("Error2"), "success"])
    success, result = await handler.retry_with_backoff(func)
    assert success is True
    assert result == "success"
    assert func.await_count == 3


@pytest.mark.asyncio
async def test_retry_with_backoff_all_retries_fail():
    """Test retry_with_backoff() returns False when all retries fail."""
    handler = NATSRetryHandler(max_retries=3, base_delay=0.01, max_delay=1.0)
    error = ValueError("Final error")
    func = AsyncMock(side_effect=error)
    success, result = await handler.retry_with_backoff(func)
    assert success is False
    assert result == error
    assert func.await_count == 3


@pytest.mark.asyncio
async def test_retry_with_backoff_no_sleep_after_last_attempt():
    """Test retry_with_backoff() doesn't sleep after last attempt."""
    handler = NATSRetryHandler(max_retries=2, base_delay=0.1, max_delay=1.0)
    func = AsyncMock(side_effect=Exception("Error"))
    start_time = anyio.current_time()
    await handler.retry_with_backoff(func)
    elapsed = anyio.current_time() - start_time
    # Should only sleep once (after first attempt), not after last
    # With base_delay=0.1 and jitter, should be ~0.075-0.125
    assert elapsed < 0.2  # Should not wait after last attempt


def test_get_config():
    """Test get_config() returns current RetryConfig."""
    handler = NATSRetryHandler(max_retries=5, base_delay=2.0, max_delay=60.0)
    config = handler.get_config()
    assert isinstance(config, RetryConfig)
    assert config.max_attempts == 5
    assert config.base_delay == 2.0
    assert config.max_delay == 60.0


def test_update_config_valid_field():
    """Test update_config() updates valid field."""
    handler = NATSRetryHandler()
    handler.update_config(max_attempts=10)
    assert handler.config.max_attempts == 10


def test_update_config_multiple_fields():
    """Test update_config() updates multiple fields."""
    handler = NATSRetryHandler()
    handler.update_config(base_delay=2.0, max_delay=120.0)
    assert handler.config.base_delay == 2.0
    assert handler.config.max_delay == 120.0


def test_update_config_invalid_field():
    """Test update_config() ignores invalid field."""
    handler = NATSRetryHandler()
    original_max_attempts = handler.config.max_attempts
    handler.update_config(invalid_field=123)
    # Should not change valid fields
    assert handler.config.max_attempts == original_max_attempts


@pytest.mark.asyncio
async def test_retry_with_backoff_preserves_exception_type():
    """Test retry_with_backoff() preserves exception type."""
    handler = NATSRetryHandler(max_retries=1, base_delay=0.01, max_delay=1.0)
    error = ValueError("Test error")
    func = AsyncMock(side_effect=error)
    success, result = await handler.retry_with_backoff(func)
    assert success is False
    assert isinstance(result, ValueError)
    assert str(result) == "Test error"


@pytest.mark.asyncio
async def test_retry_with_backoff_different_errors():
    """Test retry_with_backoff() handles different error types."""
    handler = NATSRetryHandler(max_retries=2, base_delay=0.01, max_delay=1.0)
    func = AsyncMock(side_effect=[ValueError("Error1"), TypeError("Error2")])
    success, result = await handler.retry_with_backoff(func)
    assert success is False
    assert isinstance(result, TypeError)  # Last error
    assert str(result) == "Error2"
