"""
Unit tests for AggressiveMobNPC.

Regression test: aggressive mobs must have player_in_range and enemy_nearby
populated in context so attack_on_sight and hunt_players rules can fire.
"""

# pyright: reportPrivateUsage=false
# Reason: Unit tests call AggressiveMobNPC protected helpers (_enrich_behavior_context, _get_attack_damage, _targets).

# pylint: disable=protected-access  # Reason: Tests call NPC internal helpers

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.npc.aggressive_mob_npc import AggressiveMobNPC

BehaviorContext = dict[str, object]


def test_enrich_behavior_context_sets_player_in_range_when_players_in_room() -> None:
    """_enrich_behavior_context sets player_in_range and enemy_nearby True when players in room."""
    definition = MagicMock()
    definition.npc_type = "aggressive_mob"
    definition.name = "Nightgaunt"
    definition.room_id = "room-123"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"

    npc = AggressiveMobNPC(definition, "npc-001")
    npc.current_room = "room-123"

    get_players_mock: MagicMock = MagicMock()
    get_players_mock.return_value = ["player-uuid-1", "player-uuid-2"]
    mock_room = MagicMock()
    mock_room.get_players = get_players_mock

    get_room_mock: MagicMock = MagicMock(return_value=mock_room)
    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id = get_room_mock

    mock_lm = MagicMock()
    mock_lm.persistence = mock_persistence

    mock_service = MagicMock()
    mock_service.lifecycle_manager = mock_lm

    context: BehaviorContext = {}

    with patch(
        "server.services.npc_instance_service.get_npc_instance_service",
        return_value=mock_service,
    ):
        npc._enrich_behavior_context(context)

    assert context["player_in_range"] is True
    assert context["enemy_nearby"] is True
    assert context["target_id"] == "player-uuid-1"


def test_enrich_behavior_context_sets_false_when_no_players_in_room() -> None:
    """_enrich_behavior_context sets player_in_range and enemy_nearby False when room empty."""
    definition = MagicMock()
    definition.npc_type = "aggressive_mob"
    definition.name = "Nightgaunt"
    definition.room_id = "room-123"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"

    npc = AggressiveMobNPC(definition, "npc-001")
    npc.current_room = "room-123"

    get_players_mock: MagicMock = MagicMock()
    get_players_mock.return_value = []
    mock_room = MagicMock()
    mock_room.get_players = get_players_mock

    get_room_mock: MagicMock = MagicMock(return_value=mock_room)
    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id = get_room_mock

    mock_lm = MagicMock()
    mock_lm.persistence = mock_persistence

    mock_service = MagicMock()
    mock_service.lifecycle_manager = mock_lm

    context: BehaviorContext = {}

    with patch(
        "server.services.npc_instance_service.get_npc_instance_service",
        return_value=mock_service,
    ):
        npc._enrich_behavior_context(context)

    assert context["player_in_range"] is False
    assert context["enemy_nearby"] is False
    assert "target_id" not in context


def test_enrich_behavior_context_handles_no_current_room() -> None:
    """_enrich_behavior_context sets False when current_room is None."""
    definition = MagicMock()
    definition.npc_type = "aggressive_mob"
    definition.name = "Nightgaunt"
    definition.room_id = None
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"

    npc = AggressiveMobNPC(definition, "npc-001")
    npc.current_room = None

    context: BehaviorContext = {}

    npc._enrich_behavior_context(context)

    assert context["player_in_range"] is False
    assert context["enemy_nearby"] is False


def test_get_attack_damage_from_behavior_config() -> None:
    """_get_attack_damage coerces behavior_config attack_damage robustly."""
    definition = MagicMock()
    definition.npc_type = "aggressive_mob"
    definition.name = "Ghoul"
    definition.room_id = "r1"
    definition.base_stats = "{}"
    definition.behavior_config = '{"attack_damage": 4}'
    definition.ai_integration_stub = "{}"

    npc = AggressiveMobNPC(definition, "npc-002")
    assert npc._get_attack_damage() == 4


def test_get_attack_damage_invalid_string_falls_back_to_one() -> None:
    """Non-digit attack_damage string in behavior_config falls back to 1."""
    definition = MagicMock()
    definition.npc_type = "aggressive_mob"
    definition.name = "Ghoul"
    definition.room_id = "r1"
    definition.base_stats = "{}"
    definition.behavior_config = '{"attack_damage": "x"}'
    definition.ai_integration_stub = "{}"

    npc = AggressiveMobNPC(definition, "npc-003")
    assert npc._get_attack_damage() == 1


def test_hunt_target_avoids_duplicate_ids() -> None:
    """hunt_target appends each id once; repeated calls keep a single _targets entry."""
    definition = MagicMock()
    definition.npc_type = "aggressive_mob"
    definition.name = "Hunter"
    definition.room_id = "r1"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"

    npc = AggressiveMobNPC(definition, "npc-004")
    assert npc.hunt_target("p1") is True
    assert npc.hunt_target("p1") is True
    assert npc._targets == ["p1"]


def test_enrich_behavior_context_swallows_compute_errors() -> None:
    """Warnings path: failure in _compute_player_context must not raise."""
    definition = MagicMock()
    definition.npc_type = "aggressive_mob"
    definition.name = "Broken"
    definition.room_id = "r1"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"

    npc = AggressiveMobNPC(definition, "npc-005")
    npc.current_room = "room-x"
    context: BehaviorContext = {}

    with patch.object(npc, "_compute_player_context", side_effect=RuntimeError("boom")):
        npc._enrich_behavior_context(context)

    assert context["player_in_range"] is False
    assert context["enemy_nearby"] is False


def _make_aggro(behavior_config: str = "{}") -> AggressiveMobNPC:
    definition = MagicMock()
    definition.npc_type = "aggressive_mob"
    definition.name = "Ghoul"
    definition.room_id = "r1"
    definition.base_stats = "{}"
    definition.behavior_config = behavior_config
    definition.ai_integration_stub = "{}"
    return AggressiveMobNPC(definition, "npc-aggro")


def test_get_behavior_rules_returns_engine_rules() -> None:
    npc = _make_aggro()
    rules = npc.get_behavior_rules()
    assert isinstance(rules, list)
    assert any(r.get("action") == "attack_target" for r in rules)


def test_get_attack_damage_bool_and_float() -> None:
    npc_true = _make_aggro('{"attack_damage": true}')
    assert npc_true._get_attack_damage() == 1
    npc_false = _make_aggro('{"attack_damage": false}')
    assert npc_false._get_attack_damage() == 0
    npc_float = _make_aggro('{"attack_damage": 2.9}')
    assert npc_float._get_attack_damage() == 2


def test_compute_player_context_without_service() -> None:
    npc = _make_aggro()
    with patch("server.services.npc_instance_service.get_npc_instance_service", return_value=None):
        assert npc._compute_player_context("room-1") == (False, False, None)


def test_attack_via_combat_integration_none_when_missing() -> None:
    npc = _make_aggro()
    assert npc._attack_via_combat_integration("p1", 3) is None


def test_attack_via_event_bus_without_running_loop() -> None:
    npc = _make_aggro()
    bus = MagicMock()
    npc.event_bus = bus
    npc.combat_integration = MagicMock()
    with patch("asyncio.get_running_loop", side_effect=RuntimeError("no loop")):
        assert npc._attack_via_combat_integration("p1", 5) is True
    bus.publish.assert_called_once()


def test_attack_via_dropped_without_loop_or_bus() -> None:
    npc = _make_aggro()
    npc.event_bus = None
    npc.combat_integration = MagicMock()
    with patch("asyncio.get_running_loop", side_effect=RuntimeError("no loop")):
        assert npc._attack_via_combat_integration("p1", 5) is False


@pytest.mark.asyncio
async def test_attack_via_create_task_with_running_loop() -> None:
    npc = _make_aggro()
    ci = MagicMock()
    ci.handle_npc_attack = AsyncMock(return_value=True)
    npc.combat_integration = ci
    npc.current_room = "room-x"
    assert npc._attack_via_combat_integration("p1", 4) is True
    await asyncio.sleep(0)
    ci.handle_npc_attack.assert_awaited()


def test_attack_target_fallback_publishes_event() -> None:
    npc = _make_aggro('{"attack_damage": 3}')
    bus = MagicMock()
    npc.event_bus = bus
    npc.combat_integration = None
    assert npc.attack_target("p1") is True
    bus.publish.assert_called_once()


def test_attack_target_error_returns_false() -> None:
    npc = _make_aggro()
    with patch.object(npc, "_attack_target_impl", side_effect=TypeError("bad")):
        assert npc.attack_target("p1") is False


def test_flee_and_patrol_and_handlers() -> None:
    npc = _make_aggro()
    with patch.object(npc, "speak", return_value=True):
        assert npc.flee() is True
    assert npc.patrol_territory() is True
    assert npc._handle_hunt_target({"target_id": "p9"}) is True
    assert "p9" in npc._targets
    with patch.object(npc, "attack_target", return_value=True) as attack:
        assert npc._handle_attack_target({"target_id": "p2"}) is True
        attack.assert_called_once_with("p2")
    with patch.object(npc, "flee", return_value=True) as flee:
        assert npc._handle_flee({}) is True
        flee.assert_called_once()
    with patch.object(npc, "patrol_territory", return_value=True) as patrol:
        assert npc._handle_patrol_territory({}) is True
        patrol.assert_called_once()


def test_flee_error_returns_false() -> None:
    npc = _make_aggro()
    with patch.object(npc, "speak", side_effect=AttributeError("mute")):
        assert npc.flee() is False
