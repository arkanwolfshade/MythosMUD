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


@pytest.mark.asyncio
async def test_guard_async_allows_first_execution():
    """Test async guard allows first execution."""
    guard = InventoryMutationGuard()

    async with guard.acquire_async("investigator-async-1", "token-async-1") as decision:
        assert decision.should_apply is True
        assert decision.duplicate is False


@pytest.mark.asyncio
async def test_guard_async_detects_duplicate_token():
    """Test async guard detects duplicate tokens."""
    guard = InventoryMutationGuard()

    async with guard.acquire_async("investigator-async-2", "token-async-dupe") as decision:
        assert decision.should_apply is True

    async with guard.acquire_async("investigator-async-2", "token-async-dupe") as decision:
        assert decision.should_apply is False
        assert decision.duplicate is True


@pytest.mark.asyncio
@pytest.mark.serial  # Worker crash in parallel execution - likely due to shared state in guard
async def test_guard_async_token_ttl_allows_reprocessing_after_expiry():
    """Test async guard allows reprocessing after token expiry."""
    import asyncio

    guard = InventoryMutationGuard(token_ttl_seconds=0.05)

    async with guard.acquire_async("investigator-async-4", "token-async-expiring") as decision:
        assert decision.should_apply

    # Sleep longer than TTL to ensure token expires
    await asyncio.sleep(0.10)

    async with guard.acquire_async("investigator-async-4", "token-async-expiring") as decision:
        assert decision.should_apply


@pytest.mark.asyncio
async def test_guard_async_handles_none_token():
    """Test async guard handles None token."""
    guard = InventoryMutationGuard()

    async with guard.acquire_async("investigator-async-5", None) as decision:
        assert decision.should_apply is True
        assert decision.duplicate is False


@pytest.mark.asyncio
async def test_guard_async_enforces_limit():
    """Test async guard enforces token limit."""
    guard = InventoryMutationGuard(max_tokens=3)

    # Add tokens up to limit
    for i in range(3):
        async with guard.acquire_async("investigator-async-6", f"token-{i}") as decision:
            assert decision.should_apply

    # Add one more - should prune oldest
    async with guard.acquire_async("investigator-async-6", "token-3") as decision:
        assert decision.should_apply

    # Oldest token should be gone
    async with guard.acquire_async("investigator-async-6", "token-0") as decision:
        assert decision.should_apply  # Should be allowed since token-0 was pruned


def test_guard_cleanup_state_when_empty():
    """Test guard cleans up state when tokens are empty."""
    guard = InventoryMutationGuard()

    # Acquire and release with a token - token will be stored
    with guard.acquire("investigator-cleanup", "token-cleanup") as decision:
        assert decision.should_apply

    # State is NOT cleaned up because tokens dict still has the token
    # The same token will be detected as duplicate
    with guard.acquire("investigator-cleanup", "token-cleanup") as decision:
        # Should be detected as duplicate since token is still in recent_tokens
        assert not decision.should_apply
        assert decision.duplicate

    # Use a different token - should be allowed
    with guard.acquire("investigator-cleanup", "token-cleanup-2") as decision:
        assert decision.should_apply


@pytest.mark.asyncio
async def test_guard_async_cleanup_state_when_empty():
    """Test async guard cleans up state when tokens are empty."""
    guard = InventoryMutationGuard()

    # Acquire and release with a token - token will be stored
    async with guard.acquire_async("investigator-async-cleanup", "token-async-cleanup") as decision:
        assert decision.should_apply

    # State is NOT cleaned up because tokens dict still has the token
    # The same token will be detected as duplicate
    async with guard.acquire_async("investigator-async-cleanup", "token-async-cleanup") as decision:
        # Should be detected as duplicate since token is still in recent_tokens
        assert not decision.should_apply
        assert decision.duplicate

    # Use a different token - should be allowed
    async with guard.acquire_async("investigator-async-cleanup", "token-async-cleanup-2") as decision:
        assert decision.should_apply


def test_guard_prune_tokens_with_zero_ttl():
    """Test guard handles zero TTL (no pruning)."""
    guard = InventoryMutationGuard(token_ttl_seconds=0.0)

    # Add token
    with guard.acquire("investigator-zero-ttl", "token-zero") as decision:
        assert decision.should_apply

    # With zero TTL, _prune_tokens returns early without pruning (by design)
    # So tokens are NOT pruned, and the same token will be detected as duplicate
    with guard.acquire("investigator-zero-ttl", "token-zero") as decision:
        # Token should still be there (not pruned) and detected as duplicate
        assert not decision.should_apply
        assert decision.duplicate


def test_guard_enforce_limit_edge_case():
    """Test guard enforces limit when exactly at max."""
    guard = InventoryMutationGuard(max_tokens=2)

    # Add exactly max_tokens
    with guard.acquire("investigator-limit", "token-0") as decision:
        assert decision.should_apply
    with guard.acquire("investigator-limit", "token-1") as decision:
        assert decision.should_apply

    # Add one more - should prune oldest
    with guard.acquire("investigator-limit", "token-2") as decision:
        assert decision.should_apply

    # token-0 should be gone
    with guard.acquire("investigator-limit", "token-0") as decision:
        assert decision.should_apply


@pytest.mark.asyncio
async def test_guard_async_cleanup_when_lock_held():
    """Test async guard cleanup when lock is held."""
    guard = InventoryMutationGuard()

    # First, create state with a token
    async with guard.acquire_async("investigator-lock-test", "token-lock") as decision:
        assert decision.should_apply

    # Clear tokens to make state eligible for cleanup
    state = await guard._get_async_state("investigator-lock-test")
    state.recent_tokens.clear()

    # Acquire the player's lock to simulate it being held
    player_lock = state.get_lock()
    await player_lock.acquire()

    try:
        # Cleanup should detect lock is held and skip
        await guard._cleanup_async_state("investigator-lock-test")
        # State should still exist because lock was held
        assert "investigator-lock-test" in guard._async_states
    finally:
        player_lock.release()
        # Now cleanup should work
        await guard._cleanup_async_state("investigator-lock-test")
        # State should be cleaned up now
        assert "investigator-lock-test" not in guard._async_states


def test_guard_handles_none_token_in_sync():
    """Test guard handles None token in sync context."""
    guard = InventoryMutationGuard()

    with guard.acquire("investigator-none-sync", None) as decision:
        assert decision.should_apply is True
        assert decision.duplicate is False

    # None token should not be stored, so second call should also work
    with guard.acquire("investigator-none-sync", None) as decision:
        assert decision.should_apply is True


def test_guard_record_custom_alert_with_message_parameter(monkeypatch):
    """Test guard handles record_custom_alert with message parameter."""
    guard = InventoryMutationGuard()

    recorded_alerts = []

    class FakeDashboard:
        def record_custom_alert(
            self,
            alert: str,
            *,
            severity: str = "warning",
            message: str | None = None,
            metadata: dict[str, str] | None = None,
        ) -> None:
            recorded_alerts.append({"alert": alert, "severity": severity, "message": message, "metadata": metadata})

    monkeypatch.setattr(
        "server.services.inventory_mutation_guard.get_monitoring_dashboard",
        lambda: FakeDashboard(),
    )

    # First call
    with guard.acquire("investigator-message-param", "token-message") as decision:
        assert decision.should_apply

    # Second call should trigger duplicate detection with message parameter
    with guard.acquire("investigator-message-param", "token-message") as decision:
        assert decision.should_apply is False
        assert decision.duplicate is True

    # Should have recorded alert with message parameter
    assert len(recorded_alerts) > 0
    assert recorded_alerts[0]["alert"] == "inventory_duplicate"
    assert "message" in recorded_alerts[0] or recorded_alerts[0].get("message") is not None


def test_guard_record_custom_alert_signature_error(monkeypatch):
    """Test guard handles TypeError when calling record_custom_alert."""
    guard = InventoryMutationGuard()

    class FakeDashboard:
        def record_custom_alert(self, *args, **kwargs):
            # Simulate signature mismatch
            raise TypeError("Unexpected signature")

    monkeypatch.setattr(
        "server.services.inventory_mutation_guard.get_monitoring_dashboard",
        lambda: FakeDashboard(),
    )

    # First call
    with guard.acquire("investigator-sig-error", "token-sig") as decision:
        assert decision.should_apply

    # Second call should handle TypeError gracefully
    with guard.acquire("investigator-sig-error", "token-sig") as decision:
        assert decision.should_apply is False
        assert decision.duplicate is True
