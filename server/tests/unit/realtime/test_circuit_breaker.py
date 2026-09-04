"""
Unit tests for circuit breaker.

Tests the CircuitBreaker class and CircuitBreakerOpen exception.
"""

import asyncio
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock

import pytest

from server.realtime.circuit_breaker import CircuitBreaker, CircuitBreakerOpen, CircuitState

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


def test_circuit_breaker_init():
    """Test CircuitBreaker initialization."""
    cb = CircuitBreaker(failure_threshold=5, timeout=timedelta(seconds=60), success_threshold=2)
    assert cb.failure_threshold == 5
    assert cb.timeout == timedelta(seconds=60)
    assert cb.success_threshold == 2
    assert cb.state == CircuitState.CLOSED
    assert cb.failure_count == 0
    assert cb.success_count == 0
    assert cb.last_failure_time is None


def test_circuit_breaker_init_defaults():
    """Test CircuitBreaker initialization with defaults."""
    cb = CircuitBreaker()
    assert cb.failure_threshold == 5
    assert cb.timeout == timedelta(seconds=60)
    assert cb.success_threshold == 2


@pytest.mark.asyncio
async def test_call_success_closed_state():
    """Test call() executes successfully in CLOSED state."""
    cb = CircuitBreaker()
    mock_func = AsyncMock(return_value="success")
    result = await cb.call(mock_func, "arg1", kwarg1="value1")
    assert result == "success"
    mock_func.assert_awaited_once_with("arg1", kwarg1="value1")
    assert cb.failure_count == 0


@pytest.mark.asyncio
async def test_call_failure_closed_state():
    """Test call() handles failure in CLOSED state."""
    cb = CircuitBreaker(failure_threshold=2)
    mock_func = AsyncMock(side_effect=ValueError("Test error"))
    with pytest.raises(ValueError, match="Test error"):
        await cb.call(mock_func)
    assert cb.failure_count == 1
    assert cb.state == CircuitState.CLOSED


@pytest.mark.asyncio
async def test_call_opens_circuit_after_threshold():
    """Test call() opens circuit after failure threshold."""
    cb = CircuitBreaker(failure_threshold=2)
    mock_func = AsyncMock(side_effect=ValueError("Test error"))
    # First failure
    with pytest.raises(ValueError):
        await cb.call(mock_func)
    assert cb.failure_count == 1
    assert cb.state == CircuitState.CLOSED
    # Second failure - should open circuit
    with pytest.raises(ValueError):
        await cb.call(mock_func)
    assert cb.failure_count == 2
    # Reason: Testing enum comparison - valid at runtime but mypy sees as non-overlapping due to type narrowing
    assert cb.state == CircuitState.OPEN  # type: ignore[comparison-overlap]


@pytest.mark.asyncio
async def test_call_rejects_when_open():
    """Test call() raises CircuitBreakerOpen when circuit is OPEN."""
    cb = CircuitBreaker(failure_threshold=1, timeout=timedelta(seconds=60))
    mock_func = AsyncMock(side_effect=ValueError("Test error"))
    # Trigger open
    with pytest.raises(ValueError):
        await cb.call(mock_func)
    assert cb.state == CircuitState.OPEN
    # Should reject immediately
    with pytest.raises(CircuitBreakerOpen):
        await cb.call(mock_func)


@pytest.mark.asyncio
async def test_call_transitions_to_half_open_after_timeout():
    """Test call() transitions to HALF_OPEN after timeout."""
    cb = CircuitBreaker(failure_threshold=1, timeout=timedelta(seconds=0.1))
    mock_func = AsyncMock(side_effect=ValueError("Test error"))
    # Trigger open
    with pytest.raises(ValueError):
        await cb.call(mock_func)
    assert cb.state == CircuitState.OPEN
    # Wait for timeout
    await asyncio.sleep(0.15)
    # Should transition to HALF_OPEN and attempt call
    mock_func.side_effect = None
    mock_func.return_value = "success"
    result = await cb.call(mock_func)
    assert result == "success"
    # Reason: Testing enum comparison - valid at runtime but mypy sees as non-overlapping
    assert cb.state == CircuitState.HALF_OPEN  # type: ignore[comparison-overlap]


@pytest.mark.asyncio
async def test_call_closes_from_half_open_on_success():
    """Test call() closes circuit from HALF_OPEN after success threshold."""
    cb = CircuitBreaker(failure_threshold=1, success_threshold=2, timeout=timedelta(seconds=0.1))
    mock_func = AsyncMock(side_effect=ValueError("Test error"))
    # Trigger open
    with pytest.raises(ValueError):
        await cb.call(mock_func)
    # Reason: Testing enum comparison - valid at runtime but mypy sees as non-overlapping
    assert cb.state == CircuitState.OPEN
    # Wait for timeout
    await asyncio.sleep(0.15)
    # First success in HALF_OPEN
    mock_func.side_effect = None
    mock_func.return_value = "success"
    result = await cb.call(mock_func)
    assert result == "success"
    # Reason: Testing enum comparison - valid at runtime but mypy sees as non-overlapping
    assert cb.state == CircuitState.HALF_OPEN  # type: ignore[comparison-overlap]
    # Reason: Testing field value - mypy sees as unreachable but valid at runtime
    assert cb.success_count == 1  # type: ignore[unreachable]
    # Second success - should close
    result = await cb.call(mock_func)
    assert result == "success"
    assert cb.state == CircuitState.CLOSED
    assert cb.success_count == 0
    assert cb.failure_count == 0


@pytest.mark.asyncio
async def test_call_reopens_from_half_open_on_failure():
    """Test call() reopens circuit from HALF_OPEN on failure."""
    cb = CircuitBreaker(failure_threshold=1, success_threshold=2, timeout=timedelta(seconds=0.1))
    mock_func = AsyncMock(side_effect=ValueError("Test error"))
    # Trigger open
    with pytest.raises(ValueError):
        await cb.call(mock_func)
    assert cb.state == CircuitState.OPEN
    # Wait for timeout
    await asyncio.sleep(0.15)
    # Failure in HALF_OPEN - should reopen
    with pytest.raises(ValueError):
        await cb.call(mock_func)
    assert cb.state == CircuitState.OPEN
    assert cb.success_count == 0


def test_on_success_resets_failure_count_closed():
    """Test _on_success() resets failure count in CLOSED state."""
    cb = CircuitBreaker()
    cb.failure_count = 3
    cb._on_success()
    assert cb.failure_count == 0


def test_on_success_increments_success_count_half_open():
    """Test _on_success() increments success count in HALF_OPEN state."""
    cb = CircuitBreaker(success_threshold=2)
    cb.state = CircuitState.HALF_OPEN
    cb._on_success()
    assert cb.success_count == 1
    assert cb.state == CircuitState.HALF_OPEN
    # Second success should close
    cb._on_success()
    assert cb.success_count == 0
    # Reason: Testing enum comparison - valid at runtime but mypy sees as non-overlapping
    assert cb.state == CircuitState.CLOSED  # type: ignore[comparison-overlap]


def test_on_failure_increments_failure_count():
    """Test _on_failure() increments failure count."""
    cb = CircuitBreaker(failure_threshold=3)
    cb._on_failure()
    assert cb.failure_count == 1
    assert cb.last_failure_time is not None
    cb._on_failure()
    assert cb.failure_count == 2


def test_on_failure_opens_circuit_at_threshold():
    """Test _on_failure() opens circuit at threshold."""
    cb = CircuitBreaker(failure_threshold=2)
    cb._on_failure()
    assert cb.state == CircuitState.CLOSED
    cb._on_failure()
    # Reason: Testing enum comparison - valid at runtime but mypy sees as non-overlapping due to type narrowing
    assert cb.state == CircuitState.OPEN  # type: ignore[comparison-overlap]
    # Reason: Testing field value - mypy sees as unreachable but valid at runtime
    assert cb.failure_count == 2  # type: ignore[unreachable]


def test_on_failure_resets_success_count():
    """Test _on_failure() resets success count."""
    cb = CircuitBreaker()
    cb.state = CircuitState.HALF_OPEN
    cb.success_count = 1
    cb._on_failure()
    assert cb.success_count == 0


def test_should_attempt_reset_returns_false_before_timeout():
    """Test _should_attempt_reset() returns False before timeout."""
    cb = CircuitBreaker(timeout=timedelta(seconds=60))
    cb.state = CircuitState.OPEN
    cb.last_state_change = datetime.now(UTC)
    assert cb._should_attempt_reset() is False


def test_should_attempt_reset_returns_true_after_timeout():
    """Test _should_attempt_reset() returns True after timeout."""
    cb = CircuitBreaker(timeout=timedelta(seconds=0.1))
    cb.state = CircuitState.OPEN
    cb.last_state_change = datetime.now(UTC) - timedelta(seconds=0.2)
    assert cb._should_attempt_reset() is True


def test_should_attempt_reset_returns_false_when_not_open():
    """Test _should_attempt_reset() returns False when not OPEN."""
    cb = CircuitBreaker()
    cb.state = CircuitState.CLOSED
    cb.last_failure_time = datetime.now(UTC) - timedelta(seconds=30)
    # When not OPEN, it checks last_failure_time, but should return False if time hasn't passed
    cb.timeout = timedelta(seconds=60)
    assert cb._should_attempt_reset() is False


def test_time_until_retry_returns_zero_when_not_open():
    """Test _time_until_retry() returns 0 when not OPEN."""
    cb = CircuitBreaker()
    cb.state = CircuitState.CLOSED
    assert cb._time_until_retry() == 0.0


def test_time_until_retry_returns_remaining_time():
    """Test _time_until_retry() returns remaining time."""
    cb = CircuitBreaker(timeout=timedelta(seconds=60))
    cb.state = CircuitState.OPEN
    cb.last_state_change = datetime.now(UTC) - timedelta(seconds=30)
    time_until = cb._time_until_retry()
    assert 25.0 < time_until < 35.0  # Allow some variance


def test_time_until_retry_returns_zero_after_timeout():
    """Test _time_until_retry() returns 0 after timeout."""
    cb = CircuitBreaker(timeout=timedelta(seconds=60))
    cb.state = CircuitState.OPEN
    cb.last_state_change = datetime.now(UTC) - timedelta(seconds=120)
    assert cb._time_until_retry() == 0.0


def test_transition_to_updates_state():
    """Test _transition_to() updates state."""
    cb = CircuitBreaker()
    old_time = cb.last_state_change
    cb._transition_to(CircuitState.OPEN)
    assert cb.state == CircuitState.OPEN
    assert cb.last_state_change is not None
    assert cb.last_state_change >= old_time  # Should be updated


def test_get_state():
    """Test get_state() returns current state."""
    cb = CircuitBreaker()
    assert cb.get_state() == CircuitState.CLOSED
    cb.state = CircuitState.OPEN
    assert cb.get_state() == CircuitState.OPEN


def test_get_stats():
    """Test get_stats() returns comprehensive statistics."""
    cb = CircuitBreaker(failure_threshold=5, timeout=timedelta(seconds=60), success_threshold=2)
    cb.failure_count = 3
    cb.success_count = 1
    stats = cb.get_stats()
    assert stats["state"] == "closed"
    assert stats["failure_count"] == 3
    assert stats["success_count"] == 1
    assert stats["failure_threshold"] == 5
    assert stats["success_threshold"] == 2
    assert stats["timeout_seconds"] == 60.0
    assert "last_failure_time" in stats
    assert "last_state_change" in stats
    assert "time_until_retry" in stats


def test_get_stats_with_failure_time():
    """Test get_stats() includes failure time when set."""
    cb = CircuitBreaker()
    cb._on_failure()
    stats = cb.get_stats()
    assert stats["last_failure_time"] is not None


def test_reset():
    """Test reset() manually resets circuit breaker."""
    cb = CircuitBreaker()
    cb.state = CircuitState.OPEN
    cb.failure_count = 5
    cb.success_count = 2
    cb.last_failure_time = datetime.now(UTC)
    cb.reset()
    assert cb.state == CircuitState.CLOSED
    assert cb.failure_count == 0
    assert cb.success_count == 0
    assert cb.last_failure_time is None


def test_circuit_breaker_open_exception():
    """Test CircuitBreakerOpen exception."""
    error = CircuitBreakerOpen("Circuit is open")
    assert str(error) == "Circuit is open"
    assert isinstance(error, Exception)
