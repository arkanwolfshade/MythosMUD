"""
Unit tests for AggressiveMobNPC.

Regression test: aggressive mobs must have player_in_range and enemy_nearby
populated in context so attack_on_sight and hunt_players rules can fire.
"""

# pyright: reportPrivateUsage=false
# Reason: Unit tests call AggressiveMobNPC protected helpers (_enrich_behavior_context, _get_attack_damage, _targets).

# pylint: disable=protected-access  # Reason: Tests call NPC internal helpers

from unittest.mock import MagicMock, patch

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
