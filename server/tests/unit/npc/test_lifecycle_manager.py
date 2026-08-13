"""Unit tests for NPCLifecycleManager."""

from __future__ import annotations

import time
from unittest.mock import MagicMock, patch

from server.events import EventBus
from server.events.event_types import NPCDied, NPCEnteredRoom, NPCLeftRoom
from server.npc.lifecycle_manager import NPCLifecycleManager
from server.npc.lifecycle_types import NPCLifecycleState


def _make_manager(*, population_controller: MagicMock | None = None) -> NPCLifecycleManager:
    spawning = MagicMock()
    spawning.create_npc_instance = MagicMock(return_value=None)
    return NPCLifecycleManager(
        event_bus=EventBus(),
        population_controller=population_controller,
        spawning_service=spawning,
        persistence=MagicMock(),
        thread_manager=None,
    )


def test_record_and_check_death_suppression() -> None:
    manager = _make_manager()
    manager.death_suppression_duration = 30.0
    manager.record_npc_death("npc-1")
    assert manager.is_npc_death_suppressed("npc-1") is True
    manager.death_suppression["npc-1"] = time.monotonic() - 31.0
    assert manager.is_npc_death_suppressed("npc-1") is False


def test_apply_schedule_state() -> None:
    manager = _make_manager()
    entry = MagicMock(id="night")
    manager.apply_schedule_state([entry])
    assert manager.active_schedule_ids == ["night"]


def test_can_spawn_admin_bypass() -> None:
    manager = _make_manager(population_controller=MagicMock())
    definition = MagicMock()
    can_spawn, reason = manager.can_spawn_npc(definition, "room-1", reason="admin_spawn")
    assert can_spawn is True
    assert reason == ""


def test_can_spawn_population_limit() -> None:
    controller = MagicMock()
    controller.get_zone_key_from_room_id.return_value = "zone/a"
    stats = MagicMock()
    stats.npcs_by_definition = {5: 3}
    controller.get_population_stats.return_value = stats
    definition = MagicMock()
    definition.id = 5
    definition.max_population = 2
    definition.can_spawn.return_value = False
    manager = _make_manager(population_controller=controller)
    can_spawn, reason = manager.can_spawn_npc(definition, "room-1")
    assert can_spawn is False
    assert "population limit" in reason


def test_get_lifecycle_statistics_empty() -> None:
    manager = _make_manager()
    stats = manager.get_lifecycle_statistics()
    assert stats["total_npcs"] == 0
    assert stats["error_rate"] == 0


def test_respawn_nonexistent_npc() -> None:
    manager = _make_manager()
    assert manager.respawn_npc("missing") is False


def test_respawn_blocked_by_death_suppression() -> None:
    manager = _make_manager()
    record = MagicMock()
    manager.lifecycle_records["npc-1"] = record
    manager.record_npc_death("npc-1")
    assert manager.respawn_npc("npc-1") is False


def test_handle_npc_entered_room_transitions_spawning() -> None:
    manager = _make_manager()
    record = MagicMock(current_state=NPCLifecycleState.SPAWNING)
    manager.lifecycle_records["npc-1"] = record
    event = NPCEnteredRoom(npc_id="npc-1", room_id="room-a")
    manager._handle_npc_entered_room(event)
    record.change_state.assert_called_once()


def test_handle_npc_left_room_adds_event() -> None:
    manager = _make_manager()
    record = MagicMock()
    manager.lifecycle_records["npc-1"] = record
    event = NPCLeftRoom(npc_id="npc-1", room_id="room-a")
    manager._handle_npc_left_room(event)
    record.add_event.assert_called_once()


def test_handle_npc_died_delegates() -> None:
    manager = _make_manager()
    with patch("server.npc.lifecycle_manager.handle_npc_died_impl") as mock_impl:
        event = NPCDied(npc_id="npc-1", room_id="room-a", killer_id=None)
        manager._handle_npc_died(event)
        mock_impl.assert_called_once_with(manager, event)


def test_generate_npc_id_format() -> None:
    manager = _make_manager()
    definition = MagicMock()
    definition.name = "Deep One"
    npc_id = manager._generate_npc_id(definition, "room_001")
    assert npc_id.startswith("deep_one_room_001_")


def test_spawn_npc_population_rejected() -> None:
    controller = MagicMock()
    controller.get_zone_key_from_room_id.return_value = "z/a"
    stats = MagicMock()
    stats.npcs_by_definition = {1: 99}
    controller.get_population_stats.return_value = stats
    definition = MagicMock()
    definition.id = 1
    definition.name = "Mob"
    definition.can_spawn.return_value = False
    definition.max_population = 1
    manager = _make_manager(population_controller=controller)
    npc_id, failure = manager.spawn_npc(definition, "room-1")
    assert npc_id is None
    assert failure


def test_spawn_npc_success_path() -> None:
    manager = _make_manager()
    definition = MagicMock()
    definition.id = 1
    definition.name = "Mob"
    definition.can_spawn.return_value = True
    npc_instance = MagicMock()
    npc_instance.current_room = "room-1"
    manager.spawning_service.create_npc_instance.return_value = npc_instance
    room = MagicMock()
    manager.persistence.get_room_by_id.return_value = room
    npc_id, failure = manager.spawn_npc(definition, "room-1")
    assert npc_id is not None
    assert failure is None
    assert npc_id in manager.active_npcs


def test_respawn_npc_success() -> None:
    manager = _make_manager()
    record = MagicMock()
    record.definition = MagicMock(id=1)
    manager.lifecycle_records["npc-1"] = record
    manager.respawn_queue = {}
    assert manager.respawn_npc("npc-1", delay=1.0) is True
    assert "npc-1" in manager.respawn_queue


def test_get_npc_lifecycle_record_missing() -> None:
    manager = _make_manager()
    assert manager.get_npc_lifecycle_record("missing") is None
