"""Unit tests for npc/lifecycle_death helpers."""

from __future__ import annotations

from unittest.mock import MagicMock

from server.events.event_types import NPCDied
from server.npc.lifecycle_death import (
    _mark_despawned_and_queue_respawn,
    _remove_active_npc_and_notify,
    handle_npc_died_impl,
)
from server.npc.lifecycle_types import NPCLifecycleRecord, NPCLifecycleState


def _manager_stub():
    manager = MagicMock()
    manager.lifecycle_records = {}
    manager.active_npcs = {}
    manager.population_controller = MagicMock()
    manager.persistence = MagicMock()
    manager.event_bus = MagicMock()
    manager.default_respawn_delay = 30.0
    manager.respawn_npc = MagicMock(return_value=True)
    return manager


def _record(npc_id: str = "npc_1") -> NPCLifecycleRecord:
    definition = MagicMock()
    definition.name = "Cultist"
    return NPCLifecycleRecord(npc_id, definition)


def test_handle_npc_died_impl_no_record():
    manager = _manager_stub()
    event = NPCDied(npc_id="missing", room_id="room_1", cause="combat")
    handle_npc_died_impl(manager, event)
    manager.respawn_npc.assert_not_called()


def test_handle_npc_died_impl_full_path():
    manager = _manager_stub()
    record = _record("npc_1")
    manager.lifecycle_records["npc_1"] = record
    npc_instance = MagicMock()
    npc_instance.room_id = "room_1"
    manager.active_npcs["npc_1"] = npc_instance
    room = MagicMock()
    manager.persistence.get_room_by_id = MagicMock(return_value=room)
    event = NPCDied(npc_id="npc_1", room_id="room_1", cause="combat")

    handle_npc_died_impl(manager, event)

    assert "npc_1" not in manager.active_npcs
    manager.population_controller.despawn_npc.assert_called_once_with("npc_1")
    room.npc_left.assert_called_once_with("npc_1")
    manager.event_bus.publish.assert_called_once()
    assert record.current_state == NPCLifecycleState.DESPAWNED
    manager.respawn_npc.assert_called_once()


def test_remove_active_npc_skips_when_not_active():
    manager = _manager_stub()
    event = NPCDied(npc_id="npc_1", room_id="room_1")
    _remove_active_npc_and_notify(manager, event)
    manager.event_bus.publish.assert_not_called()


def test_mark_despawned_logs_failure():
    manager = _manager_stub()
    manager.respawn_npc = MagicMock(return_value=False)
    record = _record("npc_1")
    event = NPCDied(npc_id="npc_1", room_id="room_1", cause="fire")
    _mark_despawned_and_queue_respawn(manager, event, record)
    assert record.current_state == NPCLifecycleState.DESPAWNED
