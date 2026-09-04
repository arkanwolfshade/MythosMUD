"""Unit tests for NPC lifecycle despawn helpers."""

from unittest.mock import MagicMock

from server.events.event_types import NPCLeftRoom
from server.npc.lifecycle_despawn import despawn_npc_impl
from server.npc.lifecycle_types import NPCLifecycleEvent, NPCLifecycleState


def _make_manager(*, with_active: bool = True, with_room: bool = True, with_persistence: bool = True) -> MagicMock:
    manager = MagicMock()
    record = MagicMock()
    manager.lifecycle_records = {"npc-1": record}
    manager.active_npcs = {}
    if with_active:
        # Real NPCs use current_room; avoid bare MagicMock (auto-creates current_room).
        npc = MagicMock(spec=["current_room", "current_room_id", "spawn_room_id", "room_id"])
        npc.current_room = "room-a"
        npc.current_room_id = None
        npc.spawn_room_id = None
        npc.room_id = None
        manager.active_npcs["npc-1"] = npc
    manager.population_controller = MagicMock()
    manager.persistence = MagicMock() if with_persistence else None
    manager.event_bus = MagicMock()
    if with_persistence and with_room:
        room = MagicMock()
        manager.persistence.get_room_by_id.return_value = room
    elif with_persistence:
        manager.persistence.get_room_by_id.return_value = None
    return manager


def test_despawn_nonexistent_npc_returns_false() -> None:
    manager = MagicMock(lifecycle_records={})
    assert despawn_npc_impl(manager, "missing") is False


def test_despawn_success_with_persistence_and_room() -> None:
    manager = _make_manager()
    assert despawn_npc_impl(manager, "npc-1", reason="test") is True
    manager.population_controller.despawn_npc.assert_called_once_with("npc-1")
    manager.persistence.get_room_by_id.return_value.npc_left.assert_called_once_with("npc-1")
    assert "npc-1" not in manager.active_npcs
    record = manager.lifecycle_records["npc-1"]
    record.change_state.assert_any_call(NPCLifecycleState.DESPAWNED, "test")
    record.add_event.assert_called_once_with(NPCLifecycleEvent.DESPAWNED, {"reason": "test"})


def test_despawn_stops_npc_thread_worker() -> None:
    """#768: despawn must release the NPCThreadManager worker task for this npc_id.

    Without this call, `_npc_thread_worker`'s loop guard (`npc_id in active_threads`) is never
    falsified, the task runs forever, and every subsequent spawn (a fresh npc_id) piles up a new
    one -- the ~25/hour idle leak this issue tracks.
    """
    manager = _make_manager()
    assert despawn_npc_impl(manager, "npc-1", reason="test") is True
    manager.queue_npc_thread_stop.assert_called_once_with("npc-1")


def test_despawn_stops_npc_thread_worker_even_without_active_instance() -> None:
    """A thread can outlive its `active_npcs` entry; despawn must still release it by npc_id."""
    manager = _make_manager(with_active=False)
    assert despawn_npc_impl(manager, "npc-1") is True
    manager.queue_npc_thread_stop.assert_called_once_with("npc-1")


def test_despawn_publishes_event_when_room_missing() -> None:
    manager = _make_manager(with_room=False)
    assert despawn_npc_impl(manager, "npc-1") is True
    published = manager.event_bus.publish.call_args[0][0]
    assert isinstance(published, NPCLeftRoom)
    assert published.npc_id == "npc-1"


def test_despawn_publishes_event_without_persistence() -> None:
    manager = _make_manager(with_persistence=False)
    assert despawn_npc_impl(manager, "npc-1") is True
    manager.event_bus.publish.assert_called_once()


def test_despawn_record_only_when_not_active() -> None:
    manager = _make_manager(with_active=False)
    assert despawn_npc_impl(manager, "npc-1") is True
    manager.population_controller.despawn_npc.assert_not_called()


def test_despawn_exception_sets_error_state() -> None:
    manager = _make_manager()
    record = manager.lifecycle_records["npc-1"]
    manager.population_controller.despawn_npc.side_effect = RuntimeError("boom")
    assert despawn_npc_impl(manager, "npc-1") is False
    record.change_state.assert_any_call(NPCLifecycleState.ERROR, "boom")
    record.add_event.assert_called_with(NPCLifecycleEvent.ERROR_OCCURRED, {"error": "boom"})


def test_despawn_without_population_controller() -> None:
    manager = _make_manager()
    manager.population_controller = None
    assert despawn_npc_impl(manager, "npc-1", reason="cleanup") is True
    assert "npc-1" not in manager.active_npcs


def test_despawn_skips_left_event_when_room_unknown() -> None:
    manager = _make_manager(with_persistence=False)
    npc = MagicMock(spec=[])
    manager.active_npcs["npc-1"] = npc
    assert despawn_npc_impl(manager, "npc-1") is True
    manager.event_bus.publish.assert_not_called()


def test_despawn_prefers_current_room_over_room_id() -> None:
    manager = _make_manager()
    npc = MagicMock(spec=["current_room", "current_room_id", "spawn_room_id", "room_id"])
    npc.current_room = "room-foyer"
    npc.current_room_id = None
    npc.spawn_room_id = None
    npc.room_id = "stale-alias"
    manager.active_npcs["npc-1"] = npc
    assert despawn_npc_impl(manager, "npc-1") is True
    manager.persistence.get_room_by_id.assert_called_with("room-foyer")


def test_despawn_uses_lifecycle_spawn_room_when_attrs_missing() -> None:
    manager = _make_manager()
    npc = MagicMock(spec=[])
    manager.active_npcs["npc-1"] = npc
    manager.lifecycle_records["npc-1"].events = [
        {"details": {"room_id": "earth_arkhamcity_sanitarium_room_foyer_001"}},
    ]
    assert despawn_npc_impl(manager, "npc-1") is True
    manager.persistence.get_room_by_id.assert_called_with("earth_arkhamcity_sanitarium_room_foyer_001")
