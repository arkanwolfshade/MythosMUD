"""
Tests for Circuit Breaker pattern implementation.

Like the protective wards inscribed by the Cult of the Elder Sign,
these circuit breakers prevent cascading failures from overwhelming the system.

AI: Tests circuit breaker for preventing cascading failures in NATS.
"""

import asyncio
from datetime import timedelta
from typing import Any, cast

import pytest

from server.realtime.circuit_breaker import CircuitBreaker, CircuitBreakerOpen, CircuitState


class TestCircuitBreaker:
    """Test suite for Circuit Breaker pattern."""

    def test_initialization(self) -> None:
        """Circuit breaker initializes in CLOSED state."""
        cb = CircuitBreaker(failure_threshold=5, success_threshold=2, timeout=timedelta(seconds=60))

        assert cast(Any, cb.state) == CircuitState.CLOSED
        assert cb.failure_threshold == 5
        assert cb.success_threshold == 2
        assert cb.timeout == timedelta(seconds=60)

    @pytest.mark.asyncio
    async def test_closed_state_allows_calls(self) -> None:
        """CLOSED state allows calls through."""
        cb = CircuitBreaker(failure_threshold=5, success_threshold=2, timeout=timedelta(seconds=60))

        async def test_func():
            return "success"

        result = await cb.call(test_func)
        assert result == "success"
        assert cast(Any, cb.state) == CircuitState.CLOSED

    @pytest.mark.asyncio
    async def test_successful_call_resets_failure_count(self) -> None:
        """Successful call in CLOSED state resets failure count."""
        cb = CircuitBreaker(failure_threshold=5, success_threshold=2, timeout=timedelta(seconds=60))

        # Simulate some failures first
        async def failing_func():
            raise RuntimeError("Test error")

        try:
            await cb.call(failing_func)
        except Exception:  # pylint: disable=broad-exception-caught
            # JUSTIFICATION: This test intentionally triggers and catches a generic exception
            # to verify that the circuit breaker correctly records failures.
            pass

        assert cb.failure_count == 1

        # Now succeed
        async def success_func():
            return "ok"

        await cb.call(success_func)
        assert cb.failure_count == 0  # Reset

    @pytest.mark.asyncio
    async def test_failure_increments_count(self) -> None:
        """Failed call increments failure count."""
        cb = CircuitBreaker(failure_threshold=5, success_threshold=2, timeout=timedelta(seconds=60))

        async def failing_func():
            raise RuntimeError("Test error")

        with pytest.raises(RuntimeError, match="Test error"):
            # JUSTIFICATION: This test verifies that exceptions are propagated
            # through the circuit breaker correctly.
            await cb.call(failing_func)

        assert cb.failure_count == 1
        assert cast(Any, cb.state) == CircuitState.CLOSED  # Not yet at threshold

    @pytest.mark.asyncio
    async def test_opens_after_threshold_failures(self) -> None:
        """Circuit opens after failure threshold is reached."""
        cb = CircuitBreaker(failure_threshold=3, success_threshold=2, timeout=timedelta(seconds=60))

        async def failing_func():
            raise RuntimeError("Always fails")

        # Fail 3 times to hit threshold
        for _ in range(3):
            try:
                await cb.call(failing_func)
            except RuntimeError:  # pylint: disable=broad-exception-caught
                # JUSTIFICATION: This test intentionally triggers and catches a generic exception
                # to verify that the circuit breaker correctly records failures.
                pass

        assert cast(Any, cb.state) == CircuitState.OPEN

    @pytest.mark.asyncio
    async def test_open_state_blocks_calls(self) -> None:
        """OPEN state blocks calls."""
        cb = CircuitBreaker(failure_threshold=1, success_threshold=2, timeout=timedelta(seconds=60))

        # Open the circuit
        async def failing_func():
            raise RuntimeError("Fail")

        try:
            await cb.call(failing_func)
        except RuntimeError:  # pylint: disable=broad-exception-caught
            # JUSTIFICATION: This test intentionally triggers and catches a generic exception
            # to verify that the circuit breaker correctly records failures.
            pass

        assert cast(Any, cb.state) == CircuitState.OPEN

        # Next call should be blocked
        async def any_func():
            return "should not execute"

        with pytest.raises(CircuitBreakerOpen):
            await cb.call(any_func)

    @pytest.mark.asyncio
    async def test_transitions_to_half_open_after_timeout(self) -> None:
        """Circuit transitions to HALF_OPEN after timeout."""
        cb = CircuitBreaker(failure_threshold=1, success_threshold=2, timeout=timedelta(seconds=0.1))

        # Open the circuit
        async def failing_func():
            raise RuntimeError("Fail")

        try:
            await cb.call(failing_func)
        except RuntimeError:  # pylint: disable=broad-exception-caught
            # JUSTIFICATION: This test intentionally triggers and catches a generic exception
            # to verify that the circuit breaker correctly records failures.
            pass

        assert cast(Any, cb.state) == CircuitState.OPEN

        # Wait for timeout
        await asyncio.sleep(0.15)

        # Next call should transition to HALF_OPEN
        async def test_func():
            return "testing"

        result = await cb.call(test_func)
        assert result == "testing"
        assert cast(Any, cb.state) == CircuitState.HALF_OPEN

    @pytest.mark.asyncio
    async def test_half_open_closes_after_success_threshold(self) -> None:
        """HALF_OPEN closes after success threshold is reached."""
        cb = CircuitBreaker(failure_threshold=1, success_threshold=2, timeout=timedelta(seconds=0.1))

        # Open the circuit
        async def failing_func():
            raise RuntimeError("Fail")

        try:
            await cb.call(failing_func)
        except RuntimeError:  # pylint: disable=broad-exception-caught
            # JUSTIFICATION: This test intentionally triggers and catches a generic exception
            # to verify that the circuit breaker correctly records failures.
            pass

        # Wait and transition to HALF_OPEN
        await asyncio.sleep(0.15)

        async def success_func():
            return "ok"

        # Two successes to close circuit
        await cb.call(success_func)
        await cb.call(success_func)

        assert cast(Any, cb.state) == CircuitState.CLOSED
        assert cb.failure_count == 0

    @pytest.mark.asyncio
    async def test_half_open_reopens_on_failure(self) -> None:
        """HALF_OPEN reopens circuit on any failure."""
        cb = CircuitBreaker(failure_threshold=1, success_threshold=2, timeout=timedelta(seconds=0.1))

        # Open the circuit
        async def failing_func():
            raise RuntimeError("Fail")

        try:
            await cb.call(failing_func)
        except RuntimeError:
            pass

        # Wait and transition to HALF_OPEN
        await asyncio.sleep(0.15)

        async def test_func():
            return "ok"

        await cb.call(test_func)  # First success
        assert cast(Any, cb.state) == CircuitState.HALF_OPEN

        # Now fail
        try:
            await cb.call(failing_func)
        except RuntimeError:
            pass

        assert cast(Any, cb.state) == CircuitState.OPEN

    def test_reset_closes_circuit(self) -> None:
        """Reset closes circuit and clears counters."""
        cb = CircuitBreaker(failure_threshold=1, success_threshold=2, timeout=timedelta(seconds=60))

        # Open the circuit
        async def failing_func():
            raise RuntimeError("Fail")

        # Run the call properly
        async def open_circuit():
            try:
                await cb.call(failing_func)
            except Exception:  # pylint: disable=broad-exception-caught
                # JUSTIFICATION: This test intentionally triggers and catches a generic exception
                # to verify that the circuit breaker correctly records failures.
                pass

        asyncio.run(open_circuit())

        assert cast(Any, cb.state) == CircuitState.OPEN

        # Reset
        cb.reset()

        assert cast(Any, cb.state) == CircuitState.CLOSED
        assert cb.failure_count == 0
        assert cb.success_count == 0

    def test_get_stats(self) -> None:
        """Get stats returns correct circuit breaker state."""
        cb = CircuitBreaker(failure_threshold=5, success_threshold=2, timeout=timedelta(seconds=60))

        stats = cb.get_stats()

        assert stats["state"] == CircuitState.CLOSED.value
        assert stats["failure_count"] == 0
        assert stats["success_count"] == 0
        assert stats["failure_threshold"] == 5
        assert stats["success_threshold"] == 2
        assert stats["timeout_seconds"] == 60.0

    @pytest.mark.asyncio
    async def test_consecutive_failures_open_circuit(self) -> None:
        """Consecutive failures open the circuit."""
        cb = CircuitBreaker(failure_threshold=3, success_threshold=2, timeout=timedelta(seconds=60))

        async def failing_func():
            raise RuntimeError("Always fails")

        # Execute until circuit opens (3 failures)
        for _ in range(3):
            try:
                await cb.call(failing_func)
            except RuntimeError:
                pass

        assert cast(Any, cb.state) == CircuitState.OPEN

    @pytest.mark.asyncio
    async def test_mixed_success_failure_doesnt_open(self) -> None:
        """Mixed successes and failures don't open circuit if below threshold."""
        cb = CircuitBreaker(failure_threshold=5, success_threshold=2, timeout=timedelta(seconds=60))

        async def failing_func():
            raise RuntimeError("Fail")

        async def success_func():
            return "ok"

        # Alternate between success and failure
        try:
            await cb.call(failing_func)
        except RuntimeError:
            pass

        await cb.call(success_func)  # Success resets failure count

        try:
            await cb.call(failing_func)
        except RuntimeError:
            pass

        await cb.call(success_func)  # Success resets again

        assert cast(Any, cb.state) == CircuitState.CLOSED
        assert cb.failure_count == 0  # Reset by last success

    def test_get_state(self) -> None:
        """Get state returns current CircuitState."""
        cb = CircuitBreaker(failure_threshold=5, success_threshold=2, timeout=timedelta(seconds=60))

        assert cb.get_state() == CircuitState.CLOSED
