"""Unit tests for NPC lifecycle respawn queue helpers."""

import time
from unittest.mock import MagicMock

from server.npc.lifecycle_respawn import (
    _attempt_respawn_impl,
    _cleanup_respawn_queue,
    _process_respawn_queue_entry,
    process_respawn_queue_impl,
)


def _respawn_data(*, scheduled_offset: float = -1.0, attempts: int = 0) -> dict:
    return {
        "scheduled_time": time.time() + scheduled_offset,
        "definition": MagicMock(id=1),
        "room_id": "room-spawn",
        "reason": "death",
        "attempts": attempts,
    }


def _make_manager(*, max_attempts: int = 3) -> MagicMock:
    """A manager with a population_controller configured, matching production wiring.

    #768: respawn spawns route through `population_controller.spawn_npc` (which registers the
    new NPC in `population_stats`), not `manager.spawn_npc` directly -- so the mocked return
    value belongs on `manager.population_controller.spawn_npc`, and `manager.spawn_npc` is left
    unconfigured (default MagicMock) so a test that accidentally exercises the old path fails
    loudly on an unpack error instead of silently passing.
    """
    manager = MagicMock()
    manager.respawn_queue = {}
    manager.max_respawn_attempts = max_attempts
    manager.can_spawn_npc.return_value = (True, None)
    manager.population_controller.spawn_npc.return_value = ("npc-new", None)
    manager.lifecycle_records = {}
    return manager


def test_process_respawn_queue_not_ready() -> None:
    manager = _make_manager()
    manager.respawn_queue = {"npc-old": _respawn_data(scheduled_offset=60.0)}
    assert process_respawn_queue_impl(manager) == 0
    assert "npc-old" in manager.respawn_queue


def test_process_respawn_queue_success() -> None:
    manager = _make_manager()
    manager.respawn_queue = {"npc-old": _respawn_data()}
    assert process_respawn_queue_impl(manager) == 1
    assert manager.respawn_queue == {}


def test_process_respawn_queue_failed_retry() -> None:
    manager = _make_manager()
    manager.population_controller.spawn_npc.return_value = (None, None)
    manager.respawn_queue = {"npc-old": _respawn_data()}
    assert process_respawn_queue_impl(manager) == 0
    assert manager.respawn_queue["npc-old"]["attempts"] == 1


def test_process_respawn_queue_max_attempts_removes_entry() -> None:
    manager = _make_manager(max_attempts=1)
    manager.population_controller.spawn_npc.return_value = (None, None)
    data = _respawn_data(attempts=0)
    manager.respawn_queue = {"npc-old": data}
    assert process_respawn_queue_impl(manager) == 0
    assert manager.respawn_queue == {}


def test_attempt_respawn_can_spawn_false() -> None:
    manager = _make_manager()
    manager.can_spawn_npc.return_value = (False, "limit")
    assert _attempt_respawn_impl(manager, "npc-1", _respawn_data()) is False


def test_attempt_respawn_migrates_lifecycle_record() -> None:
    manager = _make_manager()
    manager.population_controller.spawn_npc.return_value = ("npc-new", None)
    manager.lifecycle_records = {"npc-old": MagicMock()}
    assert _attempt_respawn_impl(manager, "npc-old", _respawn_data()) is True
    assert "npc-new" in manager.lifecycle_records
    assert "npc-old" not in manager.lifecycle_records


def test_attempt_respawn_exception_returns_false() -> None:
    manager = _make_manager()
    manager.can_spawn_npc.side_effect = RuntimeError("fail")
    assert _attempt_respawn_impl(manager, "npc-1", _respawn_data()) is False


def test_process_entry_not_ready() -> None:
    manager = _make_manager()
    should_remove, was_respawned = _process_respawn_queue_entry(
        manager, "npc-1", _respawn_data(scheduled_offset=30.0), time.time()
    )
    assert should_remove is False
    assert was_respawned is False


def test_cleanup_respawn_queue() -> None:
    manager = MagicMock()
    manager.respawn_queue = {"a": {}, "b": {}}
    _cleanup_respawn_queue(manager, ["a"])
    assert manager.respawn_queue == {"b": {}}


def test_attempt_respawn_same_npc_id_no_migration() -> None:
    manager = _make_manager()
    manager.population_controller.spawn_npc.return_value = ("npc-1", None)
    manager.lifecycle_records = {"npc-1": MagicMock()}
    assert _attempt_respawn_impl(manager, "npc-1", _respawn_data()) is True
    assert "npc-1" in manager.lifecycle_records


def test_process_respawn_queue_multiple_entries() -> None:
    manager = _make_manager()
    manager.respawn_queue = {
        "ready": _respawn_data(),
        "waiting": _respawn_data(scheduled_offset=120.0),
    }
    assert process_respawn_queue_impl(manager) == 1
    assert "waiting" in manager.respawn_queue
    assert "ready" not in manager.respawn_queue


def test_process_entry_success_removes_entry() -> None:
    manager = _make_manager()
    data = _respawn_data()
    should_remove, was_respawned = _process_respawn_queue_entry(manager, "npc-old", data, time.time())
    assert should_remove is True
    assert was_respawned is True


def test_attempt_respawn_routes_through_population_controller() -> None:
    """#768: respawn's spawn call must go through population_controller.spawn_npc, not
    manager.spawn_npc directly -- otherwise the respawned NPC never registers in
    population_stats and the population cap never engages for it.
    """
    manager = _make_manager()
    data = _respawn_data()
    assert _attempt_respawn_impl(manager, "npc-1", data) is True
    manager.population_controller.spawn_npc.assert_called_once_with(data["definition"], "room-spawn", "respawn: death")
    manager.spawn_npc.assert_not_called()
