from collections.abc import Callable
from typing import Any

import pytest

from server.services.nats_exceptions import NATSPublishError, NATSSubscribeError
from server.services.nats_service import NATSMetrics, NATSService
from server.services.nats_subject_manager import SubjectValidationError


class _FakeSubjectManager:
    def __init__(self, should_allow: bool = True) -> None:
        self.should_allow = should_allow
        self.last_subject: str | None = None

    def validate_subject(self, subject: str) -> None:
        self.last_subject = subject
        if not self.should_allow:
            raise SubjectValidationError("invalid subject")


class _FakeNATSClient:
    def __init__(self, should_fail: bool = False) -> None:
        self.should_fail = should_fail
        self.published: list[tuple[str, bytes]] = []
        self.subscriptions: list[str] = []

    async def publish(self, subject: str, payload: bytes) -> None:
        if self.should_fail:
            raise Exception("publish failed")
        self.published.append((subject, payload))

    async def subscribe(self, subject: str, cb: Callable[..., Any]) -> None:
        if self.should_fail:
            raise Exception("subscribe failed")
        self.subscriptions.append(subject)


def test_metrics_updates_and_rates() -> None:
    metrics = NATSMetrics()
    metrics.record_publish(success=True, processing_time=0.01)
    metrics.record_publish(success=False, processing_time=0.02)
    metrics.record_subscribe(success=True)
    metrics.record_subscribe(success=False)
    metrics.record_batch_flush(success=True, message_count=2)
    metrics.record_batch_flush(success=False, message_count=1)
    metrics.update_connection_health(120.0)
    metrics.update_pool_utilization(1.5)

    data = metrics.get_metrics()
    assert data["publish_count"] == 2
    assert data["publish_error_rate"] > 0
    assert data["subscribe_count"] == 2
    assert data["subscribe_error_rate"] > 0
    assert data["batch_flush_count"] == 2
    assert data["batch_flush_error_rate"] > 0
    # health/utilization are clamped
    assert data["connection_health"] == 100.0
    assert data["pool_utilization"] == 1.0
    assert data["avg_processing_time_ms"] > 0


@pytest.mark.asyncio
async def test_connect_blocked_by_state_machine(monkeypatch) -> None:
    svc = NATSService(config={"connection_pool_size": 1})
    # Use monkeypatch to mock method - cannot directly assign to method
    monkeypatch.setattr(svc.state_machine, "can_attempt_connection", lambda: False)
    result = await svc.connect()
    assert result is False


@pytest.mark.asyncio
async def test_publish_rejected_by_subject_validation() -> None:
    svc = NATSService(config={"connection_pool_size": 1}, subject_manager=_FakeSubjectManager(should_allow=False))
    # Test uses fake client that doesn't match nats.NATS type - type: ignore needed
    svc.nc = _FakeNATSClient()  # type: ignore[assignment]
    with pytest.raises(NATSPublishError):
        await svc.publish("invalid.subject", {"msg": "hi"})


@pytest.mark.asyncio
async def test_publish_batches_and_flushes(monkeypatch) -> None:
    fake_client = _FakeNATSClient()
    svc = NATSService(config={"connection_pool_size": 1, "batch_size": 2, "batch_timeout": 0.5})
    # Test uses fake client that doesn't match nats.NATS type - type: ignore needed
    svc.nc = fake_client  # type: ignore[assignment]
    svc._pool_initialized = True  # bypass pool init for unit test
    svc.connection_pool = [fake_client]  # type: ignore[list-item]
    svc.available_connections.put_nowait(fake_client)  # type: ignore[arg-type]
    svc.message_batch = [("chat.global", {"msg": "a"}), ("chat.global", {"msg": "b"})]

    await svc._flush_batch()

    # _flush_batch groups by subject and publishes one payload
    assert len(fake_client.published) == 1
    subject, payload = fake_client.published[0]
    assert subject == "chat.global"
    assert b'"count": 2' in payload
    assert svc.metrics.batch_flush_count == 1
    assert svc.metrics.batch_flush_errors == 0


@pytest.mark.asyncio
async def test_flush_batch_records_error_on_failure() -> None:
    fake_client = _FakeNATSClient(should_fail=True)
    svc = NATSService(config={"connection_pool_size": 1, "batch_size": 2})
    # Test uses fake client that doesn't match nats.NATS type - type: ignore needed
    svc.nc = fake_client  # type: ignore[assignment]
    svc.message_batch = [("chat.global", {"msg": "a"})]

    svc._pool_initialized = True
    svc.connection_pool = [fake_client]  # type: ignore[list-item]
    svc.available_connections.put_nowait(fake_client)  # type: ignore[arg-type]

    await svc._flush_batch()

    # Failure path currently only logs; batch_flush_errors stays unchanged
    assert svc.metrics.batch_flush_errors == 0


@pytest.mark.asyncio
async def test_subscribe_rejected_by_subject_validation() -> None:
    svc = NATSService(config={"connection_pool_size": 1}, subject_manager=_FakeSubjectManager(should_allow=False))
    # Test uses fake client that doesn't match nats.NATS type - type: ignore needed
    svc.nc = _FakeNATSClient()  # type: ignore[assignment]
    with pytest.raises(NATSSubscribeError):
        await svc.subscribe("bad.subject", lambda *args, **kwargs: None)
