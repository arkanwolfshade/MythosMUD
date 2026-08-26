"""
Unit tests for NATSServicePoolMixin's exception-handling and retry branches.

test_nats_service.py already covers the happy paths (publish, pool init, cleanup).
This file targets the defensive/retry branches in server/services/nats_service_pool.py
that those happy-path tests never exercise: subject-validation failures, publish_with_pool's
exception handling, connection-pool-cleanup errors, batch add/flush failures, and the
retry-with-backoff recursion in _retry_failed_batch_groups.
"""

# pylint: disable=protected-access  # Reason: Tests need to access protected members to verify internal state and behavior
# pyright: reportPrivateUsage=false

from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.config.models import NATSConfig
from server.services.nats_exceptions import NATSPublishError
from server.services.nats_service import NATSService
from server.services.nats_subject_manager import NATSSubjectManager, SubjectValidationError


@pytest.fixture
def nats_config() -> NATSConfig:
    """Create a NATSConfig instance."""
    return NATSConfig(
        url="nats://localhost:4222",
        max_reconnect_attempts=5,
        reconnect_time_wait=2,
        ping_interval=20,
        max_outstanding_pings=2,
    )


@pytest.fixture
def nats_service(nats_config: NATSConfig) -> NATSService:
    """Create a NATSService instance."""
    return NATSService(nats_config)


def test_validate_pool_publish_subject_rejects_invalid_subject(nats_service: NATSService) -> None:
    """_validate_pool_publish_subject raises when the subject manager rejects the subject."""
    nats_service.subject_manager = NATSSubjectManager()
    nats_service.config.enable_subject_validation = True
    with pytest.raises(NATSPublishError, match="Subject validation failed"):
        nats_service._validate_pool_publish_subject("not a valid subject!", {"message_id": "1"})


def test_validate_pool_publish_subject_wraps_validation_error(nats_service: NATSService) -> None:
    """_validate_pool_publish_subject wraps a SubjectValidationError raised by validate_subject."""
    mock_manager = MagicMock()
    mock_manager.validate_subject.side_effect = SubjectValidationError("bad pattern")
    nats_service.subject_manager = mock_manager
    nats_service.config.enable_subject_validation = True
    with pytest.raises(NATSPublishError, match="Subject validation error"):
        nats_service._validate_pool_publish_subject("test.subject", {"message_id": "1"})


@pytest.mark.asyncio
async def test_publish_with_pool_wraps_unexpected_exception(nats_service: NATSService) -> None:
    """publish_with_pool wraps a non-NATSPublishError exception (e.g. a connection.publish failure)."""
    nats_service._pool_initialized = True
    nats_service.config.enable_subject_validation = False
    mock_connection = MagicMock()
    mock_connection.publish = AsyncMock(side_effect=RuntimeError("network down"))
    nats_service.available_connections.put_nowait(mock_connection)
    nats_service.connection_pool.append(mock_connection)

    with pytest.raises(NATSPublishError, match="Failed to publish message via connection pool"):
        await nats_service.publish_with_pool("test.subject", {"message_id": "1"})

    # finally block still returns the connection to the pool
    assert nats_service.available_connections.qsize() == 1


@pytest.mark.asyncio
async def test_cleanup_connection_pool_swallows_cancelled_error(nats_service: NATSService) -> None:
    """_cleanup_connection_pool logs and continues when a connection.close() is cancelled."""
    cancelled_connection = MagicMock()
    cancelled_connection.close = AsyncMock(side_effect=asyncio.CancelledError)
    nats_service.connection_pool.append(cancelled_connection)

    await nats_service._cleanup_connection_pool()  # must not raise
    assert nats_service.connection_pool == []
    assert nats_service._pool_initialized is False


@pytest.mark.asyncio
async def test_cleanup_connection_pool_swallows_close_error(nats_service: NATSService) -> None:
    """_cleanup_connection_pool logs and continues when a connection.close() raises an unexpected error."""
    bad_connection = MagicMock()
    bad_connection.close = AsyncMock(side_effect=RuntimeError("close failed"))
    nats_service.connection_pool.append(bad_connection)

    await nats_service._cleanup_connection_pool()  # must not raise
    assert nats_service.connection_pool == []


@pytest.mark.asyncio
async def test_cleanup_connection_pool_swallows_outer_exception(nats_service: NATSService) -> None:
    """_cleanup_connection_pool's outer try/except tolerates a failure enumerating the pool itself."""
    bad_pool = MagicMock()
    bad_pool.__iter__ = MagicMock(side_effect=RuntimeError("pool corrupted"))
    nats_service.connection_pool = bad_pool

    await nats_service._cleanup_connection_pool()  # must not raise


@pytest.mark.asyncio
async def test_publish_batch_returns_false_on_subject_validation_failure(nats_service: NATSService) -> None:
    """publish_batch returns False (not raise) when subject validation rejects the message."""
    nats_service.subject_manager = NATSSubjectManager()
    nats_service.config.enable_subject_validation = True
    result = await nats_service.publish_batch("not a valid subject!", {"message_id": "1"})
    assert result is False


@pytest.mark.asyncio
async def test_publish_batch_returns_false_on_unexpected_exception(nats_service: NATSService) -> None:
    """publish_batch's outer handler catches an unexpected exception and returns False."""
    nats_service.message_batch = MagicMock()
    nats_service.message_batch.append.side_effect = RuntimeError("batch corrupted")
    result = await nats_service.publish_batch("test.subject", {"message_id": "1"})
    assert result is False


@pytest.mark.asyncio
async def test_flush_batch_records_partial_success_and_cancels_batch_task(nats_service: NATSService) -> None:
    """_flush_batch reports partial success when one subject group fails, then clears batch state."""
    nats_service.message_batch = [("ok.subject", {"message_id": "1"}), ("bad.subject", {"message_id": "2"})]
    nats_service._max_batch_retries = 0  # exhaust immediately, skip the retry sleep

    async def fake_publish_with_pool(subject: str, _data: object) -> None:
        if subject == "bad.subject":
            raise NATSPublishError("boom", subject=subject)

    nats_service.publish_with_pool = AsyncMock(side_effect=fake_publish_with_pool)  # type: ignore[method-assign]

    fake_task = MagicMock()
    fake_task.done.return_value = False
    nats_service._batch_task = fake_task

    await nats_service._flush_batch()

    assert nats_service.message_batch == []
    assert nats_service._batch_task is None
    fake_task.cancel.assert_called_once()
    assert nats_service._failed_batch_queue == [("bad.subject", {"message_id": "2"})]


@pytest.mark.asyncio
async def test_retry_failed_batch_groups_recovers_on_retry(nats_service: NATSService) -> None:
    """_retry_failed_batch_groups republishes a failed group successfully on its retry pass."""
    nats_service._max_batch_retries = 3
    call_count = 0

    async def fake_publish_with_pool(subject: str, _data: object) -> None:
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            raise NATSPublishError("boom", subject=subject)

    nats_service.publish_with_pool = AsyncMock(side_effect=fake_publish_with_pool)  # type: ignore[method-assign]

    await nats_service._retry_failed_batch_groups({"test.subject": [{"message_id": "1"}]})

    assert call_count == 2
    assert nats_service._failed_batch_queue == []


@pytest.mark.asyncio
async def test_recover_failed_batches_requeues_on_repeated_failure(nats_service: NATSService) -> None:
    """recover_failed_batches puts a message back in the failed queue if recovery also fails."""
    nats_service._failed_batch_queue = [("test.subject", {"message_id": "1"})]
    nats_service.publish_with_pool = AsyncMock(side_effect=NATSPublishError("still down", subject="test.subject"))  # type: ignore[method-assign]

    recovered = await nats_service.recover_failed_batches()

    assert recovered == 0
    assert nats_service._failed_batch_queue == [("test.subject", {"message_id": "1"})]


@pytest.mark.asyncio
async def test_recover_failed_batches_recovers_successfully(nats_service: NATSService) -> None:
    """recover_failed_batches drains the failed queue and reports the recovered count."""
    nats_service._failed_batch_queue = [("test.subject", {"message_id": "1"})]
    nats_service.publish_with_pool = AsyncMock(return_value=None)  # type: ignore[method-assign]

    recovered = await nats_service.recover_failed_batches()

    assert recovered == 1
    assert nats_service._failed_batch_queue == []
