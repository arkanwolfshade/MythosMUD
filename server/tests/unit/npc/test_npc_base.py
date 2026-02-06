"""
Unit tests for NPCBase combat stats and movement.

Tests get_combat_stats() which centralizes combat stat extraction for NPC combat,
and move_to_room() blocking when NPC is in combat.
"""

from unittest.mock import MagicMock, patch

from server.npc.passive_mob_npc import PassiveMobNPC


def test_npc_base_get_combat_stats() -> None:
    """Test NPCBase.get_combat_stats() returns combat-relevant stats."""
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = '{"determination_points": 30, "max_dp": 40, "dexterity": 12}'
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-001")

    combat_stats = npc.get_combat_stats()

    assert combat_stats["current_dp"] == 30
    assert combat_stats["max_dp"] == 40
    assert combat_stats["dexterity"] == 12


def test_npc_base_get_combat_stats_legacy_dp() -> None:
    """Test get_combat_stats() uses dp when determination_points absent."""
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = '{"dp": 25, "max_dp": 35, "dexterity": 8}'
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-002")

    combat_stats = npc.get_combat_stats()

    assert combat_stats["current_dp"] == 25
    assert combat_stats["max_dp"] == 35
    assert combat_stats["dexterity"] == 8


def test_npc_base_is_alive_property() -> None:
    """Test NPCBase.is_alive property returns and accepts bool."""
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-alive")
    assert npc.is_alive is True

    npc.is_alive = False
    assert npc.is_alive is False


def test_npc_base_get_combat_stats_defaults() -> None:
    """Test get_combat_stats() uses defaults when keys missing."""
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-003")

    combat_stats = npc.get_combat_stats()

    # NPCBase init adds determination_points=20 for empty stats; max_dp and dexterity from get_combat_stats defaults
    assert combat_stats["current_dp"] == 20
    assert combat_stats["max_dp"] == 100
    assert combat_stats["dexterity"] == 10


def test_npc_base_move_to_room_blocked_when_in_combat() -> None:
    """Test move_to_room() returns False and does not move when NPC is in combat."""
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-combat")
    npc.current_room = "room_001"

    with patch.object(npc, "_is_npc_in_combat", return_value=True):
        result = npc.move_to_room("room_002", use_integration=False)

    assert result is False
    assert npc.current_room == "room_001"
