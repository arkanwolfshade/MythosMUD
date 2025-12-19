"""
Tests for NATS message retry logic with exponential backoff.

Like the rituals described in the Necronomicon, sometimes invocations
must be repeated with increasing intervals until they succeed.

AI: Tests retry logic with exponential backoff for transient failures.
"""

import asyncio
from datetime import datetime
from unittest.mock import AsyncMock

import pytest

from server.realtime.nats_retry_handler import NATSRetryHandler, RetryableMessage


class TestNATSRetryHandler:
    """Test suite for NATS retry handler."""

    def test_initialization(self) -> None:
        """Retry handler initializes with correct settings."""
        handler = NATSRetryHandler(max_retries=5, base_delay=1.0, max_delay=60.0)

        assert handler.max_retries == 5
        assert handler.base_delay == 1.0
        assert handler.max_delay == 60.0

    def test_calculate_backoff_exponential(self) -> None:
        """Backoff delay increases exponentially (with jitter)."""
        handler = NATSRetryHandler(max_retries=5, base_delay=1.0, max_delay=60.0)

        # Attempt 0: ~1s (with ±25% jitter)
        delay0 = handler.calculate_backoff(0)
        assert 0.75 <= delay0 <= 1.25

        # Attempt 1: ~2s (with ±25% jitter)
        delay1 = handler.calculate_backoff(1)
        assert 1.5 <= delay1 <= 2.5

        # Attempt 2: ~4s (with ±25% jitter)
        delay2 = handler.calculate_backoff(2)
        assert 3.0 <= delay2 <= 5.0

        # Attempt 3: ~8s (with ±25% jitter)
        delay3 = handler.calculate_backoff(3)
        assert 6.0 <= delay3 <= 10.0

    def test_calculate_backoff_respects_max_delay(self) -> None:
        """Backoff delay does not exceed max_delay (with jitter)."""
        handler = NATSRetryHandler(max_retries=10, base_delay=1.0, max_delay=10.0)

        # High attempt number should cap at max_delay + jitter (25%)
        # max_delay=10, so with jitter: 10 ± 2.5 = 7.5 to 12.5
        delay = handler.calculate_backoff(20)
        assert delay <= 12.5  # max_delay + 25% jitter

    def test_calculate_backoff_with_jitter(self) -> None:
        """Backoff includes random jitter."""
        handler = NATSRetryHandler(max_retries=5, base_delay=1.0, max_delay=60.0)

        delays = [handler.calculate_backoff(2) for _ in range(10)]

        # All delays should be around 4.0 but with jitter
        assert all(3.0 <= d <= 5.0 for d in delays)

        # Should have variation (not all exactly the same)
        assert len(set(delays)) > 1

    @pytest.mark.asyncio
    async def test_should_retry_within_max_attempts(self) -> None:
        """Should retry when within max attempts."""
        handler = NATSRetryHandler(max_retries=3)

        message = RetryableMessage(
            subject="test.subject", data={"test": "data"}, attempt=0, first_attempt_time=datetime.now()
        )

        assert await handler.should_retry(message, Exception("test error")) is True

        message.attempt = 2
        assert await handler.should_retry(message, Exception("test error")) is True

    @pytest.mark.asyncio
    async def test_should_not_retry_after_max_attempts(self) -> None:
        """Should not retry after max attempts exceeded."""
        handler = NATSRetryHandler(max_retries=3)

        message = RetryableMessage(
            subject="test.subject",
            data={"test": "data"},
            attempt=3,  # Already at max
            first_attempt_time=datetime.now(),
        )

        assert await handler.should_retry(message, Exception("test error")) is False

    @pytest.mark.asyncio
    async def test_retry_async_increments_attempt(self) -> None:
        """Retry async increments attempt counter."""
        handler = NATSRetryHandler(max_retries=5, base_delay=0.01)

        mock_func = AsyncMock()
        message = RetryableMessage(
            subject="test.subject", data={"test": "data"}, attempt=0, first_attempt_time=datetime.now()
        )

        await handler.retry_async(mock_func, message)

        assert message.attempt == 1
        mock_func.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_retry_async_waits_for_backoff(self) -> None:
        """Retry async waits for backoff delay."""
        handler = NATSRetryHandler(max_retries=5, base_delay=0.1)

        mock_func = AsyncMock()
        message = RetryableMessage(
            subject="test.subject", data={"test": "data"}, attempt=1, first_attempt_time=datetime.now()
        )

        # Use get_running_loop() in async context instead of deprecated get_event_loop()
        loop = asyncio.get_running_loop()
        start_time = loop.time()
        await handler.retry_async(mock_func, message)
        elapsed = loop.time() - start_time

        # Should have waited at least base_delay * 2^1 = 0.2s (with some tolerance)
        assert elapsed >= 0.15

    @pytest.mark.asyncio
    async def test_get_retry_stats(self) -> None:
        """Get retry stats returns correct counts."""
        handler = NATSRetryHandler(max_retries=5, base_delay=0.01)

        mock_func = AsyncMock()

        message1 = RetryableMessage("test1", {}, 0, datetime.now())
        message2 = RetryableMessage("test2", {}, 0, datetime.now())

        await handler.retry_async(mock_func, message1)
        await handler.retry_async(mock_func, message2)

        stats = handler.get_retry_stats()

        assert stats["total_retries"] == 2

    def test_retryable_message_creation(self) -> None:
        """RetryableMessage initializes correctly."""
        now = datetime.now()
        message = RetryableMessage(subject="test.subject", data={"key": "value"}, attempt=0, first_attempt_time=now)

        assert message.subject == "test.subject"
        assert message.data == {"key": "value"}
        assert message.attempt == 0
        assert message.first_attempt_time == now

    @pytest.mark.asyncio
    async def test_retry_async_passes_message_data_to_func(self) -> None:
        """Retry async passes message data to function."""
        handler = NATSRetryHandler(max_retries=5, base_delay=0.01)

        mock_func = AsyncMock()
        test_data = {"player": "test_player", "action": "move"}
        message = RetryableMessage(subject="game.events", data=test_data, attempt=0, first_attempt_time=datetime.now())

        await handler.retry_async(mock_func, message)

        mock_func.assert_awaited_once_with(message)

    @pytest.mark.asyncio
    async def test_multiple_retries_track_attempts(self) -> None:
        """Multiple retries correctly track attempt count."""
        handler = NATSRetryHandler(max_retries=5, base_delay=0.01)

        mock_func = AsyncMock()
        message = RetryableMessage("test", {}, 0, datetime.now())

        await handler.retry_async(mock_func, message)
        assert message.attempt == 1

        await handler.retry_async(mock_func, message)
        assert message.attempt == 2

        await handler.retry_async(mock_func, message)
        assert message.attempt == 3

    def test_zero_max_retries_never_retries(self) -> None:
        """Zero max retries means no retries allowed."""
        handler = NATSRetryHandler(max_retries=0)

        message = RetryableMessage("test", {}, 0, datetime.now())

        # Even first attempt should not be retryable
        asyncio.run(handler.should_retry(message, Exception("test")))
        # Should return False immediately
