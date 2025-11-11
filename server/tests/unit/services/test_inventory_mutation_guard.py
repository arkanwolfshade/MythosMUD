"""Tests for inventory mutation guard concurrency and duplication behaviour."""

from __future__ import annotations

import threading
import time

import pytest

from server.services.inventory_mutation_guard import InventoryMutationGuard


def test_guard_allows_first_execution():
    guard = InventoryMutationGuard()

    with guard.acquire("investigator-1", "token-1") as decision:
        assert decision.should_apply is True
        assert decision.duplicate is False


def test_guard_detects_duplicate_token(capsys: pytest.CaptureFixture[str]):
    guard = InventoryMutationGuard()

    with guard.acquire("investigator-2", "token-dupe") as decision:
        assert decision.should_apply

    with guard.acquire("investigator-2", "token-dupe") as decision:
        assert decision.should_apply is False
        assert decision.duplicate is True

    captured = capsys.readouterr()
    assert "Duplicate inventory mutation suppressed" in captured.out


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
