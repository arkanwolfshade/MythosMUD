"""Unit tests for NPC lifecycle periodic maintenance helpers."""

import time
from unittest.mock import MagicMock, patch

from server.config.npc_config import NPCMaintenanceConfig
from server.npc.lifecycle_periodic import (
    _attempt_optional_npc_spawn,
    _check_spawn_conditions_for_optional_npc,
    _should_skip_optional_npc,
    check_optional_npc_spawns_impl,
    cleanup_old_records_impl,
    get_spawn_room_for_definition,
    get_zone_key_for_definition,
    run_periodic_maintenance_impl,
)
from server.npc.lifecycle_types import NPCLifecycleState


def _make_record(state: NPCLifecycleState, age_seconds: float) -> MagicMock:
    record = MagicMock()
    record.current_state = state
    record.created_at = time.time() - age_seconds
    return record


def test_cleanup_old_records_removes_stale_despawned() -> None:
    manager = MagicMock()
    manager.lifecycle_records = {
        "npc-old": _make_record(NPCLifecycleState.DESPAWNED, 90000),
        "npc-fresh": _make_record(NPCLifecycleState.DESPAWNED, 100),
        "npc-active": _make_record(NPCLifecycleState.ACTIVE, 90000),
    }
    removed = cleanup_old_records_impl(manager, max_age_seconds=86400)
    assert removed == 1
    assert "npc-old" not in manager.lifecycle_records
    assert "npc-fresh" in manager.lifecycle_records
    assert "npc-active" in manager.lifecycle_records


def test_cleanup_old_records_removes_stale_error() -> None:
    manager = MagicMock()
    manager.lifecycle_records = {"npc-err": _make_record(NPCLifecycleState.ERROR, 100000)}
    assert cleanup_old_records_impl(manager) == 1
    assert manager.lifecycle_records == {}


def test_run_periodic_maintenance_respawn_and_cleanup() -> None:
    manager = MagicMock()
    manager.process_respawn_queue.return_value = 2
    manager.population_controller = None
    manager.last_cleanup = 0.0
    manager.cleanup_interval = 1.0
    manager.lifecycle_records = {}

    with patch("server.npc.lifecycle_periodic.time.time", return_value=1000.0):
        results = run_periodic_maintenance_impl(manager)

    assert results["respawned_npcs"] == 2
    assert results["spawned_npcs"] == 0
    assert results["spawn_checks_performed"] == 0
    assert "cleaned_records" in results


def test_run_periodic_maintenance_spawn_check_exception() -> None:
    manager = MagicMock()
    manager.process_respawn_queue.return_value = 0
    manager.last_cleanup = time.time()
    manager.cleanup_interval = 999999.0

    with patch(
        "server.npc.lifecycle_periodic.check_optional_npc_spawns_impl",
        side_effect=RuntimeError("boom"),
    ):
        results = run_periodic_maintenance_impl(manager)

    assert results["spawned_npcs"] == 0
    assert results["spawn_checks_performed"] == 0


def test_check_optional_npc_spawns_no_population_controller() -> None:
    manager = MagicMock()
    manager.population_controller = None
    assert check_optional_npc_spawns_impl(manager) == {"spawned_count": 0, "checks_performed": 0}


def test_should_skip_required_npc() -> None:
    definition = MagicMock()
    definition.is_required.return_value = True
    skip, _ = _should_skip_optional_npc(MagicMock(), 1, definition, time.time())
    assert skip is True


def test_should_skip_npc_in_respawn_queue() -> None:
    definition = MagicMock()
    definition.is_required.return_value = False
    definition.id = 7
    definition.name = "Shoggoth"
    manager = MagicMock()
    manager.respawn_queue = {"q1": {"definition": MagicMock(id=7)}}
    skip, _ = _should_skip_optional_npc(manager, 7, definition, time.time())
    assert skip is True


def test_should_skip_recent_spawn_check() -> None:
    definition = MagicMock()
    definition.is_required.return_value = False
    manager = MagicMock()
    manager.respawn_queue = {}
    now = time.time()
    manager.last_spawn_check = {3: now - 1}
    skip, last = _should_skip_optional_npc(manager, 3, definition, now)
    assert skip is True
    assert last == manager.last_spawn_check[3]


def test_should_not_skip_when_interval_elapsed() -> None:
    definition = MagicMock()
    definition.is_required.return_value = False
    manager = MagicMock()
    manager.respawn_queue = {}
    now = time.time()
    manager.last_spawn_check = {3: now - NPCMaintenanceConfig.MIN_SPAWN_CHECK_INTERVAL - 1}
    skip, _ = _should_skip_optional_npc(manager, 3, definition, now)
    assert skip is False


def test_check_spawn_conditions_no_controller() -> None:
    can_spawn, count = _check_spawn_conditions_for_optional_npc(
        MagicMock(population_controller=None), 1, MagicMock(), "z"
    )
    assert can_spawn is False
    assert count == 0


def test_check_spawn_conditions_population_limit() -> None:
    definition = MagicMock()
    definition.can_spawn.return_value = False
    definition.name = "Deep One"
    definition.max_population = 1
    stats = MagicMock()
    stats.npcs_by_definition = {5: 1}
    controller = MagicMock()
    controller.get_zone_configuration.return_value = MagicMock()
    controller.get_population_stats.return_value = stats
    manager = MagicMock(population_controller=controller)
    can_spawn, count = _check_spawn_conditions_for_optional_npc(manager, 5, definition, "zone-a")
    assert can_spawn is False
    assert count == 1


def test_check_spawn_conditions_can_spawn() -> None:
    definition = MagicMock()
    definition.can_spawn.return_value = True
    stats = MagicMock()
    stats.npcs_by_definition = {5: 0}
    controller = MagicMock()
    controller.get_zone_configuration.return_value = MagicMock()
    controller.get_population_stats.return_value = stats
    manager = MagicMock(population_controller=controller)
    can_spawn, count = _check_spawn_conditions_for_optional_npc(manager, 5, definition, "zone-a")
    assert can_spawn is True
    assert count == 0


def test_get_zone_key_for_definition_no_sub_zone() -> None:
    definition = MagicMock(sub_zone_id=None)
    assert get_zone_key_for_definition(MagicMock(), definition) is None


def test_get_zone_key_for_definition_with_room() -> None:
    definition = MagicMock(sub_zone_id=1, id=10, room_id="room-arkham-001")
    controller = MagicMock()
    controller.spawn_rules = {10: MagicMock()}
    controller._get_zone_key_from_room_id.return_value = "arkham/downtown"
    manager = MagicMock(population_controller=controller)
    assert get_zone_key_for_definition(manager, definition) == "arkham/downtown"


def test_get_spawn_room_for_definition_with_room() -> None:
    definition = MagicMock(room_id="room-001", name="Mob", id=1)
    assert get_spawn_room_for_definition(MagicMock(), definition) == "room-001"


def test_get_spawn_room_for_definition_missing_room() -> None:
    definition = MagicMock(room_id=None, name="Mob", id=1)
    assert get_spawn_room_for_definition(MagicMock(), definition) is None


def test_check_optional_npc_spawns_successful_spawn() -> None:
    definition = MagicMock()
    definition.is_required.return_value = False
    definition.id = 42
    definition.name = "Optional Mob"
    definition.sub_zone_id = 1
    definition.room_id = "room-spawn"
    definition.can_spawn.return_value = True
    definition.spawn_probability = 1.0

    zone_config = MagicMock()
    zone_config.get_effective_spawn_probability.return_value = 1.0
    stats = MagicMock()
    stats.npcs_by_definition = {42: 0}
    controller = MagicMock()
    controller.npc_definitions = {42: definition}
    controller.spawn_rules = {42: MagicMock()}
    controller._get_zone_key_from_room_id.return_value = "zone-1"
    controller.get_zone_configuration.return_value = zone_config
    controller.get_population_stats.return_value = stats

    manager = MagicMock()
    manager.population_controller = controller
    manager.respawn_queue = {}
    manager.last_spawn_check = {}
    manager.spawn_npc.return_value = ("npc-new", None)

    with patch("server.npc.lifecycle_periodic.random.random", return_value=0.0):
        result = check_optional_npc_spawns_impl(manager)

    assert result["checks_performed"] == 1
    assert result["spawned_count"] == 1
    manager.spawn_npc.assert_called_once()


def test_check_optional_npc_spawns_probability_miss() -> None:
    definition = MagicMock()
    definition.is_required.return_value = False
    definition.id = 42
    definition.name = "Optional Mob"
    definition.sub_zone_id = 1
    definition.room_id = "room-spawn"
    definition.can_spawn.return_value = True
    definition.spawn_probability = 0.5

    zone_config = MagicMock()
    zone_config.get_effective_spawn_probability.return_value = 0.0
    stats = MagicMock()
    stats.npcs_by_definition = {42: 0}
    controller = MagicMock()
    controller.npc_definitions = {42: definition}
    controller.spawn_rules = {42: MagicMock()}
    controller._get_zone_key_from_room_id.return_value = "zone-1"
    controller.get_zone_configuration.return_value = zone_config
    controller.get_population_stats.return_value = stats

    manager = MagicMock()
    manager.population_controller = controller
    manager.respawn_queue = {}
    manager.last_spawn_check = {}

    with patch("server.npc.lifecycle_periodic.random.random", return_value=0.5):
        result = check_optional_npc_spawns_impl(manager)

    assert result["checks_performed"] == 1
    assert result["spawned_count"] == 0
    manager.spawn_npc.assert_not_called()


def test_run_periodic_maintenance_skips_cleanup_when_recent() -> None:
    manager = MagicMock()
    manager.process_respawn_queue.return_value = 0
    manager.population_controller = None
    manager.last_cleanup = time.time()
    manager.cleanup_interval = 999999.0
    results = run_periodic_maintenance_impl(manager)
    assert "cleaned_records" not in results


def test_check_spawn_conditions_no_zone_config() -> None:
    controller = MagicMock()
    controller.get_zone_configuration.return_value = None
    manager = MagicMock(population_controller=controller)
    can_spawn, count = _check_spawn_conditions_for_optional_npc(manager, 1, MagicMock(), "zone-x")
    assert can_spawn is False
    assert count == 0


def test_get_zone_key_without_spawn_rules() -> None:
    definition = MagicMock(sub_zone_id=1, id=10, room_id="room-001")
    controller = MagicMock(spawn_rules={})
    manager = MagicMock(population_controller=controller)
    assert get_zone_key_for_definition(manager, definition) is None


def test_attempt_optional_npc_spawn_no_controller() -> None:
    assert _attempt_optional_npc_spawn(MagicMock(population_controller=None), MagicMock(), "zone") is None


def test_attempt_optional_npc_spawn_probability_miss() -> None:
    definition = MagicMock(spawn_probability=0.0, room_id="room-1", name="Mob")
    zone_config = MagicMock()
    zone_config.get_effective_spawn_probability.return_value = 0.0
    controller = MagicMock()
    controller.get_zone_configuration.return_value = zone_config
    manager = MagicMock(population_controller=controller, spawn_npc=MagicMock())
    with patch("server.npc.lifecycle_periodic.random.random", return_value=1.0):
        assert _attempt_optional_npc_spawn(manager, definition, "zone") is None
    manager.spawn_npc.assert_not_called()


def test_attempt_optional_npc_spawn_no_zone_config() -> None:
    controller = MagicMock()
    controller.get_zone_configuration.return_value = None
    manager = MagicMock(population_controller=controller)
    assert _attempt_optional_npc_spawn(manager, MagicMock(), "zone") is None


def test_check_optional_npc_spawns_skips_missing_zone_key() -> None:
    definition = MagicMock()
    definition.is_required.return_value = False
    definition.id = 9
    definition.sub_zone_id = None
    controller = MagicMock(npc_definitions={9: definition})
    manager = MagicMock(population_controller=controller, respawn_queue={}, last_spawn_check={})
    result = check_optional_npc_spawns_impl(manager)
    assert result["checks_performed"] == 1
    assert result["spawned_count"] == 0
