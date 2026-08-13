"""Unit tests for NPC spawning factory, request execution, and service."""

from __future__ import annotations

import uuid
from unittest.mock import MagicMock, patch

from server.events import EventBus
from server.npc.spawning_instance_factory import (
    create_npc_instance,
    generate_npc_id,
)
from server.npc.spawning_models import NPCSpawnRequest, NPCSpawnResult, SimpleNPCDefinition
from server.npc.spawning_request_execution import _spawn_success, spawn_npc_from_request
from server.npc.spawning_service import NPCSpawningService


def test_generate_npc_id_contains_room() -> None:
    definition = SimpleNPCDefinition(
        id=1,
        name="Shop Keeper",
        npc_type="shopkeeper",
        room_id="room-001",
        description=None,
        base_stats="{}",
        behavior_config="{}",
        ai_integration_stub="{}",
    )
    npc_id = generate_npc_id(definition, "room-001")
    assert "shop_keeper" in npc_id
    assert "room-001" in npc_id


def test_create_npc_instance_passive() -> None:
    definition = MagicMock()
    definition.id = 2
    definition.name = "Rat"
    definition.npc_type = "passive_mob"
    definition.room_id = "room-002"
    definition.description = None
    definition.base_stats = '{"determination_points": 10, "max_dp": 10, "dexterity": 5}'
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    npc = create_npc_instance(definition, "room-002", EventBus(), None, npc_id="rat-1")
    assert npc is not None
    assert npc.current_room == "room-002"


def test_create_npc_instance_unknown_type() -> None:
    definition = MagicMock()
    definition.id = 3
    definition.name = "Weird"
    definition.npc_type = "unknown_type"
    definition.room_id = "room-003"
    definition.description = None
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    assert create_npc_instance(definition, "room-003", EventBus(), None) is None


def test_spawn_success_result() -> None:
    request = MagicMock(spec=NPCSpawnRequest)
    request.definition = MagicMock(name="Mob")
    request.room_id = "room-1"
    npc = MagicMock()
    result = _spawn_success(request, "npc-9", npc)
    assert isinstance(result, NPCSpawnResult)
    assert result.success is True
    assert result.npc_id == "npc-9"


def test_spawn_npc_from_request_create_failure() -> None:
    request = MagicMock(spec=NPCSpawnRequest)
    request.definition = MagicMock()
    request.room_id = "room-x"
    result = spawn_npc_from_request(
        request,
        create_npc_instance=lambda *_a, **_k: None,
        generate_npc_id=lambda *_a, **_k: "id-1",
    )
    assert result.success is False


def test_spawn_npc_from_request_success() -> None:
    request = MagicMock(spec=NPCSpawnRequest)
    request.definition = MagicMock(name="Mob")
    request.room_id = "room-x"
    npc = MagicMock()
    room = MagicMock()
    with patch("server.npc.spawning_request_execution._room_from_persistence", return_value=room):
        result = spawn_npc_from_request(
            request,
            create_npc_instance=lambda *_a, **_k: npc,
            generate_npc_id=lambda *_a, **_k: "id-1",
        )
    assert result.success is True
    room.npc_entered.assert_called_once_with("id-1")


def test_spawn_npc_from_request_exception() -> None:
    request = MagicMock(spec=NPCSpawnRequest)
    request.definition = MagicMock()
    request.room_id = "room-x"

    def _boom(*_a, **_k):
        raise RuntimeError("boom")

    result = spawn_npc_from_request(
        request,
        create_npc_instance=_boom,
        generate_npc_id=lambda *_a, **_k: "id-1",
    )
    assert result.success is False


def test_spawn_npc_from_request_room_missing() -> None:
    request = MagicMock(spec=NPCSpawnRequest)
    request.definition = MagicMock(name="Mob")
    request.room_id = "room-x"
    npc = MagicMock()
    with patch("server.npc.spawning_request_execution._room_from_persistence", return_value=None):
        result = spawn_npc_from_request(
            request,
            create_npc_instance=lambda *_a, **_k: npc,
            generate_npc_id=lambda *_a, **_k: "id-1",
        )
    assert result.success is False
    assert result.error_message == "Room not found"


def test_spawning_service_queue_and_stats() -> None:
    service = NPCSpawningService(event_bus=EventBus(), population_controller=None)
    definition = MagicMock()
    definition.npc_type = "passive_mob"
    request = NPCSpawnRequest(definition=definition, room_id="room-1", spawn_rule=None, priority=10, reason="test")
    service._queue_spawn_request(request)
    stats = service.get_spawn_statistics()
    assert stats["queued_requests"] == 1
    assert stats["success_rate"] == 0.0


def test_spawning_service_despawn_returns_false() -> None:
    service = NPCSpawningService(event_bus=EventBus(), population_controller=None)
    assert service.despawn_npc("npc-1") is False


def test_spawning_service_calculate_priority_required() -> None:
    service = NPCSpawningService(event_bus=EventBus(), population_controller=MagicMock(current_game_state={}))
    definition = MagicMock()
    definition.npc_type = "shopkeeper"
    definition.is_required.return_value = True
    zone = MagicMock(npc_spawn_modifier=1.0)
    priority = service._calculate_spawn_priority(definition, MagicMock(), zone)
    assert priority >= 80


def test_spawning_service_process_spawn_queue_empty() -> None:
    service = NPCSpawningService(event_bus=EventBus(), population_controller=None)
    assert service.process_spawn_queue() == []


def test_spawning_service_count_spawn_reasons() -> None:
    service = NPCSpawningService(event_bus=EventBus(), population_controller=None)
    result = MagicMock(
        success=True, spawn_request=MagicMock(reason="auto", definition=MagicMock(npc_type="passive_mob"))
    )
    counts = service._count_spawn_reasons([result])
    assert counts["auto"] == 1


def test_spawning_service_get_zone_key_no_controller() -> None:
    service = NPCSpawningService(event_bus=EventBus(), population_controller=None)
    assert service._get_zone_key_from_room_id("room-1") == "unknown/unknown"


def test_spawning_service_count_spawn_types() -> None:
    service = NPCSpawningService(event_bus=EventBus(), population_controller=None)
    result = MagicMock(
        success=True,
        spawn_request=MagicMock(reason="auto", definition=MagicMock(npc_type="passive_mob")),
    )
    counts = service._count_spawn_types([result])
    assert counts["passive_mob"] == 1


def test_spawning_service_cleanup_inactive_npcs() -> None:
    service = NPCSpawningService(event_bus=EventBus(), population_controller=None)
    assert service.cleanup_inactive_npcs(max_age_seconds=60) == 0


def test_spawning_service_handle_player_entered_room() -> None:
    from server.events.event_types import PlayerEnteredRoom

    controller = MagicMock()
    controller.get_zone_key_from_room_id.return_value = "zone/sub"
    controller.get_zone_configuration.return_value = None
    service = NPCSpawningService(event_bus=EventBus(), population_controller=controller)
    event = PlayerEnteredRoom(player_id=uuid.uuid4(), room_id="room-1")
    service._handle_player_entered_room(event)
    controller.get_zone_configuration.assert_called_once()


def test_spawning_service_process_spawn_queue_with_request() -> None:
    service = NPCSpawningService(event_bus=EventBus(), population_controller=None)
    request = NPCSpawnRequest(
        definition=MagicMock(name="Mob"),
        room_id="room-1",
        spawn_rule=None,
        priority=1,
        reason="test",
    )
    service.spawn_queue.append(request)
    with patch.object(service, "_spawn_npc_from_request", return_value=MagicMock(success=False)):
        results = service.process_spawn_queue()
    assert len(results) == 1
    assert service.spawn_queue == []


def test_spawning_service_generate_npc_id() -> None:
    service = NPCSpawningService(event_bus=EventBus(), population_controller=None)
    definition = MagicMock()
    definition.id = 1
    definition.name = "Mob"
    npc_id = service._generate_npc_id(definition, "room-1")
    assert isinstance(npc_id, str)
    assert npc_id


def test_spawning_service_npc_room_event_handlers() -> None:
    from server.events.event_types import NPCEnteredRoom, NPCLeftRoom

    service = NPCSpawningService(event_bus=EventBus(), population_controller=None)
    service._handle_npc_entered_room(NPCEnteredRoom(npc_id="n1", room_id="room-1"))
    service._handle_npc_left_room(NPCLeftRoom(npc_id="n1", room_id="room-1"))


def test_spawning_service_check_spawn_requirements_queues() -> None:
    controller = MagicMock()
    controller.get_zone_key_from_room_id.return_value = "earth/arkham"
    zone = MagicMock()
    controller.get_zone_configuration.return_value = zone
    definition = MagicMock()
    definition.sub_zone_id = "arkham"
    definition.id = 1
    controller.npc_definitions = {1: definition}
    service = NPCSpawningService(event_bus=EventBus(), population_controller=controller)
    with patch.object(service, "_evaluate_spawn_requirements", return_value=[]):
        service._check_spawn_requirements_for_room("earth_arkham_room_1")
    controller.get_zone_configuration.assert_called_once()


def test_spawning_service_evaluate_spawn_rules_success() -> None:
    controller = MagicMock()
    controller.current_game_state = {}
    rule = MagicMock()
    rule.can_spawn_with_population.return_value = True
    rule.check_spawn_conditions.return_value = True
    rule.max_population = 5
    controller.spawn_rules = {1: [rule]}
    zone = MagicMock()
    zone.get_effective_spawn_probability.return_value = 1.0
    zone.npc_spawn_modifier = 1.0
    definition = MagicMock()
    definition.id = 1
    definition.name = "Mob"
    definition.npc_type = "passive_mob"
    definition.spawn_probability = 1.0
    definition.is_required.return_value = False
    service = NPCSpawningService(event_bus=EventBus(), population_controller=controller)
    with patch("server.npc.spawning_service.random.random", return_value=0.0):
        requests = service._evaluate_spawn_rules(definition, zone, "room-1", 0)
    assert len(requests) == 1
    assert requests[0].reason == "automatic"


def test_spawning_service_maybe_add_required_npc_request() -> None:
    service = NPCSpawningService(event_bus=EventBus(), population_controller=MagicMock())
    definition = MagicMock()
    definition.id = 1
    definition.is_required.return_value = True
    stats = MagicMock()
    stats.npcs_by_definition = {}
    spawn_requests: list[NPCSpawnRequest] = []
    service._maybe_add_required_npc_request(definition, "room-1", stats, spawn_requests)
    assert len(spawn_requests) == 1
    assert spawn_requests[0].reason == "required"


def test_spawning_service_get_population_stats() -> None:
    controller = MagicMock()
    expected = MagicMock()
    controller.get_population_stats.return_value = expected
    service = NPCSpawningService(event_bus=EventBus(), population_controller=controller)
    assert service.get_population_stats("earth/arkham") is expected
