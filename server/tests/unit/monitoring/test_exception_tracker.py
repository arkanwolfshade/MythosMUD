"""Unit tests for server.monitoring.exception_tracker."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

import server.monitoring.exception_tracker as exc_mod
from server.monitoring.exception_tracker import ExceptionTracker, get_exception_tracker, track_exception


@pytest.fixture(autouse=True)
def _reset_global_tracker() -> None:
    exc_mod._exception_tracker = None  # pylint: disable=protected-access


def test_track_exception_and_stats() -> None:
    tracker = ExceptionTracker(max_records=10)
    exc_id = tracker.track_exception(ValueError("bad"), {"user_id": "u1", "severity": "critical", "handled": False})
    record = tracker.get_exception_record(exc_id)
    assert record is not None
    stats = tracker.get_stats()
    assert stats.total_exceptions == 1
    assert stats.exceptions_by_type["ValueError"] == 1
    assert stats.unhandled_exceptions == 1
    assert stats.critical_exceptions == 1


def test_get_recent_exceptions_and_by_type() -> None:
    tracker = ExceptionTracker()
    tracker.track_exception(RuntimeError("r1"))
    tracker.track_exception(RuntimeError("r2"))
    recent = tracker.get_recent_exceptions(count=1)
    assert len(recent) == 1
    by_type = tracker.get_exceptions_by_type("RuntimeError")
    assert len(by_type) == 2


def test_exception_handlers_global_and_specific() -> None:
    tracker = ExceptionTracker()
    specific = MagicMock()
    global_handler = MagicMock()
    tracker.add_exception_handler(ValueError, specific)
    tracker.add_global_exception_handler(global_handler)
    tracker.track_exception(ValueError("x"))
    specific.assert_called_once()
    global_handler.assert_called_once()


def test_get_unhandled_and_critical_filters() -> None:
    tracker = ExceptionTracker()
    tracker.track_exception(OSError("disk"), {"handled": False, "severity": "critical"})
    tracker.track_exception(KeyError("k"), {"handled": True})
    assert len(tracker.get_unhandled_exceptions()) == 1
    assert len(tracker.get_critical_exceptions()) == 1


def test_reset_records_and_module_helper() -> None:
    tracker = ExceptionTracker()
    track_exception(OSError("disk"), {"tracker": tracker})
    tracker.reset_records()
    assert tracker.get_stats().total_exceptions == 0


def test_get_exception_tracker_singleton() -> None:
    first = get_exception_tracker()
    second = get_exception_tracker()
    assert first is second
