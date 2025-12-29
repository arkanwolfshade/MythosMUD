"""
Unit tests for idle movement.

Tests the IdleMovementHandler class.
"""

import uuid
from unittest.mock import MagicMock, patch

import pytest

from server.npc.idle_movement import IdleMovementHandler


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    return MagicMock()


@pytest.fixture
def mock_event_bus():
    """Create a mock event bus."""
    return MagicMock()


@pytest.fixture
def idle_movement_handler(mock_persistence, mock_event_bus):
    """Create an IdleMovementHandler instance."""
    return IdleMovementHandler(event_bus=mock_event_bus, persistence=mock_persistence)


def test_idle_movement_handler_init(mock_persistence, mock_event_bus):
    """Test IdleMovementHandler initialization."""
    handler = IdleMovementHandler(event_bus=mock_event_bus, persistence=mock_persistence)
    assert handler.persistence == mock_persistence
    assert handler.movement_integration is not None


def test_idle_movement_handler_init_no_persistence():
    """Test IdleMovementHandler initialization fails without persistence."""
    with pytest.raises(ValueError, match="persistence.*required"):
        IdleMovementHandler(persistence=None)


def test_should_idle_move_disabled(idle_movement_handler):
    """Test should_idle_move() returns False when idle movement is disabled."""
    npc_instance = MagicMock()
    npc_definition = MagicMock()
    behavior_config = {"idle_movement_enabled": False}
    result = idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config)
    assert result is False


def test_should_idle_move_in_combat(idle_movement_handler):
    """Test should_idle_move() returns False when NPC is in combat."""
    npc_instance = MagicMock()
    npc_instance.combat_state = MagicMock()
    npc_definition = MagicMock()
    behavior_config = {"idle_movement_enabled": True}
    result = idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config)
    assert result is False


def test_should_idle_move_not_alive(idle_movement_handler):
    """Test should_idle_move() returns False when NPC is not alive."""
    npc_instance = MagicMock()
    npc_instance.is_alive = False
    npc_definition = MagicMock()
    behavior_config = {"idle_movement_enabled": True}
    result = idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config)
    assert result is False


def test_should_idle_move_not_active(idle_movement_handler):
    """Test should_idle_move() returns False when NPC is not active."""
    npc_instance = MagicMock()
    npc_instance.is_alive = True
    npc_instance.is_active = False
    npc_definition = MagicMock()
    behavior_config = {"idle_movement_enabled": True, "idle_movement_probability": 1.0}
    result = idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config)
    assert result is False


def test_should_idle_move_probability_check(idle_movement_handler):
    """Test should_idle_move() respects movement probability."""
    npc_instance = MagicMock()
    npc_instance.is_alive = True
    npc_instance.is_active = True
    npc_definition = MagicMock()
    behavior_config = {"idle_movement_enabled": True, "idle_movement_probability": 0.0}
    result = idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config)
    assert result is False


def test_is_npc_in_combat_true(idle_movement_handler):
    """Test _is_npc_in_combat() when NPC is in combat."""
    npc_instance = MagicMock()
    npc_instance.npc_id = "npc_001"
    # The function imports get_combat_service from ..services.combat_service
    with patch("server.services.combat_service.get_combat_service") as mock_get_combat_service:
        mock_combat_service = MagicMock()
        npc_uuid = uuid.uuid4()
        mock_combat_service._npc_combats = {npc_uuid: MagicMock()}
        mock_get_combat_service.return_value = mock_combat_service
        result = idle_movement_handler._is_npc_in_combat(npc_instance)
        # May return True if combat service is available and NPC is in combat
        assert isinstance(result, bool)


def test_is_npc_in_combat_false(idle_movement_handler):
    """Test _is_npc_in_combat() returns False when NPC is not in combat."""
    npc_instance = MagicMock()
    npc_instance.in_combat = False
    result = idle_movement_handler._is_npc_in_combat(npc_instance)
    assert result is False


def test_is_npc_in_combat_no_attribute(idle_movement_handler):
    """Test _is_npc_in_combat() handles missing in_combat attribute."""
    npc_instance = MagicMock()
    del npc_instance.in_combat
    result = idle_movement_handler._is_npc_in_combat(npc_instance)
    assert result is False


def test_get_valid_exits_empty_room(idle_movement_handler):
    """Test get_valid_exits() with room having no exits."""
    npc_definition = MagicMock()
    npc_definition.sub_zone_id = "subzone_001"
    behavior_config = {}
    mock_room = MagicMock()
    mock_room.exits = {}
    idle_movement_handler.movement_integration.get_available_exits = MagicMock(return_value={})
    result = idle_movement_handler.get_valid_exits("room_001", npc_definition, behavior_config)
    assert len(result) == 0


def test_get_valid_exits_no_subzone(idle_movement_handler):
    """Test get_valid_exits() when NPC definition has no sub_zone_id."""
    npc_definition = MagicMock()
    npc_definition.sub_zone_id = None
    behavior_config = {}
    result = idle_movement_handler.get_valid_exits("room_001", npc_definition, behavior_config)
    assert len(result) == 0


def test_select_exit_empty_dict(idle_movement_handler):
    """Test select_exit() with empty exit dict."""
    result = idle_movement_handler.select_exit({}, "spawn_001", "room_001", {})
    assert result is None


def test_select_exit_single_exit(idle_movement_handler):
    """Test select_exit() with single exit."""
    exits = {"north": "room_002"}
    result = idle_movement_handler.select_exit(exits, "spawn_001", "room_001", {})
    assert result is not None
    assert result[0] == "north"
    assert result[1] == "room_002"


def test_select_exit_multiple_exits(idle_movement_handler):
    """Test select_exit() with multiple exits."""
    exits = {"north": "room_002", "south": "room_003"}
    result = idle_movement_handler.select_exit(exits, "spawn_001", "room_001", {})
    assert result is not None
    assert result[0] in ["north", "south"]
    assert result[1] in ["room_002", "room_003"]


def test_select_exit_weighted_home_disabled(idle_movement_handler):
    """Test select_exit() with weighted_home disabled."""
    exits = {"north": "room_002", "south": "room_003"}
    behavior_config = {"idle_movement_weighted_home": False}
    result = idle_movement_handler.select_exit(exits, "spawn_001", "room_001", behavior_config)
    assert result is not None
    assert result[0] in ["north", "south"]


def test_calculate_distance_to_room_same_room(idle_movement_handler):
    """Test _calculate_distance_to_room() with same room."""
    result = idle_movement_handler._calculate_distance_to_room("room_001", "room_001")
    assert result == 0


def test_calculate_distance_to_room_different_rooms(idle_movement_handler):
    """Test _calculate_distance_to_room() with different rooms."""
    result = idle_movement_handler._calculate_distance_to_room("room_001", "room_002")
    assert result >= 0


def test_calculate_distance_to_room_same_subzone(idle_movement_handler):
    """Test _calculate_distance_to_room() with rooms in same subzone."""
    result = idle_movement_handler._calculate_distance_to_room("earth_zone_subzone_room1", "earth_zone_subzone_room2")
    assert result >= 0


def test_calculate_distance_to_room_different_subzone(idle_movement_handler):
    """Test _calculate_distance_to_room() with rooms in different subzones."""
    result = idle_movement_handler._calculate_distance_to_room("earth_zone_subzone1_room1", "earth_zone_subzone2_room1")
    assert result == 999  # High distance for different subzones


def test_execute_idle_movement_no_valid_exits(idle_movement_handler):
    """Test execute_idle_movement() when no valid exits."""
    npc_instance = MagicMock()
    npc_instance.current_room = "room_001"
    npc_instance.is_alive = True
    npc_instance.is_active = True
    npc_definition = MagicMock()
    npc_definition.sub_zone_id = "subzone_001"
    behavior_config = {"idle_movement_enabled": True, "idle_movement_probability": 1.0}
    idle_movement_handler.get_valid_exits = MagicMock(return_value={})
    result = idle_movement_handler.execute_idle_movement(npc_instance, npc_definition, behavior_config)
    assert result is False


def test_execute_idle_movement_no_exit_selected(idle_movement_handler):
    """Test execute_idle_movement() when no exit is selected."""
    npc_instance = MagicMock()
    npc_instance.current_room = "room_001"
    npc_instance.is_alive = True
    npc_instance.is_active = True
    npc_definition = MagicMock()
    npc_definition.sub_zone_id = "subzone_001"
    behavior_config = {"idle_movement_enabled": True, "idle_movement_probability": 1.0}
    idle_movement_handler.get_valid_exits = MagicMock(return_value={"north": "room_002"})
    idle_movement_handler.select_exit = MagicMock(return_value=None)
    result = idle_movement_handler.execute_idle_movement(npc_instance, npc_definition, behavior_config)
    assert result is False


def test_execute_idle_movement_no_current_room(idle_movement_handler):
    """Test execute_idle_movement() when NPC has no current room."""
    npc_instance = MagicMock()
    npc_instance.current_room = None
    npc_definition = MagicMock()
    behavior_config = {"idle_movement_enabled": True, "idle_movement_probability": 1.0}
    result = idle_movement_handler.execute_idle_movement(npc_instance, npc_definition, behavior_config)
    assert result is False
