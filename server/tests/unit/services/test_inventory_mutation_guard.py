"""Tests for inventory mutation guard concurrency and duplication behaviour."""

from __future__ import annotations

import threading
import time
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

    with caplog.at_level("WARNING", logger="server.services.inventory_mutation_guard"):
        with guard.acquire("investigator-2", "token-dupe") as decision:
            assert decision.should_apply is False
            assert decision.duplicate is True

    assert recorded_failures == [("inventory_mutation", "duplicate_token")]

    duplicate_logs = [record for record in caplog.records if record.message == "Duplicate inventory mutation suppressed"]
    if duplicate_logs:
        structured_record = cast(DuplicateMutationLogRecord, duplicate_logs[0])
        assert structured_record.player_id == "investigator-2"
        assert structured_record.token == "token-dupe"
        assert structured_record.alert == "inventory_duplicate"
        assert structured_record.cached_tokens >= 1
    else:
        captured = capsys.readouterr().out
        assert "Duplicate inventory mutation suppressed" in captured
        assert "alert=inventory_duplicate" in captured
        assert "player_id=investigator-2" in captured
        assert "token=token-dupe" in captured


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
    first_thread.join()
    second_thread.join()

    assert order == ["first-enter", "first-exit", "second-enter", "second-exit"]


def test_guard_token_ttl_allows_reprocessing_after_expiry():
    guard = InventoryMutationGuard(token_ttl_seconds=0.05)

    with guard.acquire("investigator-4", "token-expiring") as decision:
        assert decision.should_apply

    time.sleep(0.06)

    with guard.acquire("investigator-4", "token-expiring") as decision:
        assert decision.should_apply
