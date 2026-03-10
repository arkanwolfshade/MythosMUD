"""
Unit tests for AggressiveMobNPC.

Regression test: aggressive mobs must have player_in_range and enemy_nearby
populated in context so attack_on_sight and hunt_players rules can fire.
"""

from unittest.mock import MagicMock, patch

from server.npc.aggressive_mob_npc import AggressiveMobNPC


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

    mock_room = MagicMock()
    mock_room.get_players.return_value = ["player-uuid-1", "player-uuid-2"]

    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id.return_value = mock_room

    mock_lm = MagicMock()
    mock_lm.persistence = mock_persistence

    mock_service = MagicMock()
    mock_service.lifecycle_manager = mock_lm

    context: dict = {}

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

    mock_room = MagicMock()
    mock_room.get_players.return_value = []

    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id.return_value = mock_room

    mock_lm = MagicMock()
    mock_lm.persistence = mock_persistence

    mock_service = MagicMock()
    mock_service.lifecycle_manager = mock_lm

    context: dict = {}

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

    context: dict = {}

    npc._enrich_behavior_context(context)

    assert context["player_in_range"] is False
    assert context["enemy_nearby"] is False
