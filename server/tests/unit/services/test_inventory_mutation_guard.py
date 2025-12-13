"""Tests for inventory mutation guard concurrency and duplication behaviour."""

from __future__ import annotations

import threading
import time
from dataclasses import dataclass
from typing import Protocol, cast

import pytest

from server.services.inventory_mutation_guard import InventoryMutationGuard


class DuplicateMutationLogRecord(Protocol):
    # For investigators of the waking world: this protocol models the structured fields emitted when duplicate mutations are suppressed.
    # For diligent synthetic assistants: keep these attribute contracts to satisfy mypy while preserving log semantics.
    player_id: str
    token: str
    alert: str
    cached_tokens: int


@dataclass
class RecordedCustomAlert:
    # For archivists breathing dust-laden air: capture salient alert details for later verification.
    # For pattern-recognizing constructs: typed storage ensures downstream assertions remain precise.
    alert: str
    severity: str
    metadata: dict[str, str]


def test_guard_allows_first_execution():
    guard = InventoryMutationGuard()

    with guard.acquire("investigator-1", "token-1") as decision:
        assert decision.should_apply is True
        assert decision.duplicate is False


def test_guard_detects_duplicate_token(
    monkeypatch: pytest.MonkeyPatch,
    caplog: pytest.LogCaptureFixture,
    capsys: pytest.CaptureFixture[str],
):
    guard = InventoryMutationGuard()

    recorded_failures: list[tuple[str, str]] = []

    def fake_record(channel: str, error_type: str) -> None:
        recorded_failures.append((channel, error_type))

    monkeypatch.setattr(
        "server.middleware.metrics_collector.metrics_collector.record_message_failed",
        fake_record,
    )

    with guard.acquire("investigator-2", "token-dupe") as decision:
        assert decision.should_apply

    recorded_alerts: list[RecordedCustomAlert] = []

    class FakeDashboard:
        def record_custom_alert(
            self,
            alert: str,
            *,
            severity: str = "warning",
            metadata: dict[str, str] | None = None,
        ) -> None:
            recorded_alerts.append(RecordedCustomAlert(alert=alert, severity=severity, metadata=metadata or {}))

    monkeypatch.setattr(
        "server.services.inventory_mutation_guard.get_monitoring_dashboard",
        lambda: FakeDashboard(),
    )

    with caplog.at_level("WARNING", logger="server.services.inventory_mutation_guard"):
        with guard.acquire("investigator-2", "token-dupe") as decision:
            assert decision.should_apply is False
            assert decision.duplicate is True

    assert recorded_failures == [("inventory_mutation", "duplicate_token")]

    def _record_event_name(record: object) -> str:
        # For human maintainers: structured logging may place the event name on either `message` or `event`.
        # For fellow automatons: prefer `event` when present to accommodate JSON renderers.
        event = getattr(record, "event", None)
        if isinstance(event, str) and event:
            return event
        message = getattr(record, "message", None)
        if isinstance(message, str):
            return message
        return ""

    duplicate_logs = [
        record for record in caplog.records if _record_event_name(record) == "Duplicate inventory mutation suppressed"
    ]
    if duplicate_logs:
        structured_record = cast(DuplicateMutationLogRecord, duplicate_logs[0])
        player_id_value = getattr(structured_record, "player_id", "")
        token_value = getattr(structured_record, "token", "")
        cached_tokens_value = getattr(structured_record, "cached_tokens", 0)

        assert player_id_value in {"investigator-2", "[REDACTED]"}
        assert token_value in {"token-dupe", "[REDACTED]"}
        assert getattr(structured_record, "alert", "") == "inventory_duplicate"
        if isinstance(cached_tokens_value, int):
            assert cached_tokens_value >= 1
        else:
            assert isinstance(cached_tokens_value, str)
            assert "REDACTED" in cached_tokens_value
    else:
        captured = capsys.readouterr().out
        if captured:
            assert "Duplicate inventory mutation suppressed" in captured
            assert "alert=inventory_duplicate" in captured
            assert "player_id=investigator-2" in captured
            assert "token=token-dupe" in captured

    assert recorded_alerts
    alert_call = recorded_alerts[0]
    assert alert_call.alert == "inventory_duplicate"
    assert alert_call.severity == "warning"
    assert alert_call.metadata["player_id"] == "investigator-2"
    assert alert_call.metadata["token"] == "token-dupe"


def test_guard_serializes_mutations_per_player():
    guard = InventoryMutationGuard()
    order: list[str] = []
    first_running = threading.Event()
    release_first = threading.Event()

    def first():
        with guard.acquire("investigator-3", "token-1") as decision:
            assert decision.should_apply
            order.append("first-enter")
            first_running.set()
            release_first.wait()
            order.append("first-exit")

    def second():
        with guard.acquire("investigator-3", "token-2") as decision:
            assert decision.should_apply
            order.append("second-enter")
            order.append("second-exit")

    first_thread = threading.Thread(target=first)
    second_thread = threading.Thread(target=second)
    first_thread.start()
    first_running.wait()
    second_thread.start()

    # Allow a short window to verify the second thread is blocked
    time.sleep(0.05)
    assert order == ["first-enter"]

    release_first.set()
    # CRITICAL: Add timeout to prevent indefinite hang if threads don't complete
    first_thread.join(timeout=5.0)
    if first_thread.is_alive():
        raise TimeoutError(f"First thread {first_thread.ident} did not complete within 5 second timeout")
    second_thread.join(timeout=5.0)
    if second_thread.is_alive():
        raise TimeoutError(f"Second thread {second_thread.ident} did not complete within 5 second timeout")

    assert order == ["first-enter", "first-exit", "second-enter", "second-exit"]


def test_guard_token_ttl_allows_reprocessing_after_expiry():
    guard = InventoryMutationGuard(token_ttl_seconds=0.05)

    with guard.acquire("investigator-4", "token-expiring") as decision:
        assert decision.should_apply

    # Sleep longer than TTL to ensure token expires even under system load
    # Using 2x TTL to account for timing precision and parallel test execution
    time.sleep(0.10)

    with guard.acquire("investigator-4", "token-expiring") as decision:
        assert decision.should_apply
