"""Unit tests for NPCBase combat stats and movement."""

from unittest.mock import MagicMock, patch

import pytest

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


def test_npc_base_inventory_operations() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-inv")
    item = {"id": "item-1", "name": "Shard"}
    assert npc.add_item_to_inventory(item) is True
    assert npc.get_item_from_inventory("item-1") == item
    assert npc.remove_item_from_inventory("item-1") is True
    assert npc.get_inventory() == []


def test_npc_base_take_damage_and_heal() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = '{"determination_points": 20, "max_dp": 20}'
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-hp")
    assert npc.take_damage(5) is True
    assert npc.get_combat_stats()["current_dp"] == 15
    assert npc.heal(3) is True
    assert npc.get_combat_stats()["current_dp"] == 18


def test_npc_base_move_simple() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-move")
    npc.current_room = "room_001"
    with patch.object(npc, "_is_npc_in_combat", return_value=False):
        assert npc.move_to_room("room_002", use_integration=False) is True
    assert npc.current_room == "room_002"


def test_npc_base_speak_and_listen() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-chat")
    npc.event_bus = MagicMock()
    assert npc.speak("Hello") is True
    assert npc.listen("Hi there", speaker_id="player-1") is True


def test_npc_base_to_dict_and_context() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-dict")
    data = npc.to_dict()
    assert data["npc_id"] == "test-npc-dict"
    context = npc.get_npc_context()
    assert context["npc_id"] == "test-npc-dict"


def test_npc_base_heal_when_dead_returns_false() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = '{"determination_points": 0, "max_dp": 20}'
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-dead")
    npc.is_alive = False
    assert npc.heal(5) is False


def test_npc_base_remove_missing_item() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-miss")
    assert npc.remove_item_from_inventory("missing") is False


def test_npc_base_take_damage_fatal() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = '{"determination_points": 5, "max_dp": 5}'
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-kill")
    npc.event_bus = MagicMock()
    with patch("server.npc.npc_base.schedule_end_combat_if_npc_died_best_effort"):
        assert npc.take_damage(10, source_id="player-1") is True
    assert npc.is_alive is False


def test_npc_base_take_damage_when_dead() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = '{"determination_points": 0, "max_dp": 5}'
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-no-dmg")
    npc.is_alive = False
    assert npc.take_damage(1) is False


@pytest.mark.asyncio
async def test_npc_base_execute_behavior() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-behave")
    npc._behavior_engine = MagicMock()
    npc._behavior_engine.execute_applicable_rules.return_value = True
    result = await npc.execute_behavior({})
    assert result is True


def test_npc_base_from_dict() -> None:
    from server.models.npc import NPCDefinition

    definition = MagicMock(spec=NPCDefinition)
    definition.room_id = "room_001"
    definition.id = 99
    data = {
        "npc_id": "restored-npc",
        "current_room": "room_002",
        "stats": {"determination_points": 10},
        "inventory": [],
        "is_alive": True,
        "is_active": True,
        "last_action_time": 100.0,
    }
    npc = PassiveMobNPC.from_dict(data, definition)
    assert npc.npc_id == "restored-npc"
    assert npc.current_room == "room_002"


def test_npc_base_ai_placeholders() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-ai")
    assert isinstance(npc.generate_ai_response("hello"), str)
    assert isinstance(npc.make_ai_decision({}), dict)
    assert npc.learn_from_interaction("player-1", "good") is False


def test_npc_base_get_behavior_and_ai_config() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = '{"flee_threshold": 10}'
    definition.ai_integration_stub = '{"model": "stub"}'
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-cfg")
    assert npc.get_behavior_config()["flee_threshold"] == 10
    assert npc.get_ai_config()["model"] == "stub"


def test_npc_base_move_with_event_reaction_system() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-ers")
    npc.event_reaction_system = MagicMock()
    npc.current_room = "room_001"
    with patch.object(npc, "_is_npc_in_combat", return_value=False):
        assert npc.move_to_room("room_002", use_integration=False) is True
    npc.event_reaction_system.set_npc_context.assert_called_once()


def test_npc_base_handle_die_and_idle() -> None:
    definition = MagicMock()
    definition.name = "TestMob"
    definition.room_id = "room_001"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.npc_type = "passive_mob"

    npc = PassiveMobNPC(definition=definition, npc_id="test-npc-actions")
    assert npc._handle_die({}) is True
    assert npc._handle_idle({}) is True
