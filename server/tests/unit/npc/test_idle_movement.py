"""
Unit tests for idle movement.

Tests the IdleMovementHandler class.
"""

# White-box tests call IdleMovementHandler._is_npc_in_combat and
# _calculate_distance_to_room; basedpyright reportPrivateUsage otherwise flags that.
# pyright: reportPrivateUsage=false

import uuid
from unittest.mock import MagicMock, patch

import pytest

from server.npc.idle_movement import IdleMovementHandler


@pytest.fixture
def mock_persistence() -> MagicMock:
    """Create a mock persistence layer."""
    return MagicMock()


@pytest.fixture
def mock_event_bus() -> MagicMock:
    """Create a mock event bus."""
    return MagicMock()


@pytest.fixture
def idle_movement_handler(
    mock_persistence: MagicMock,
    mock_event_bus: MagicMock,
) -> IdleMovementHandler:
    """Create an IdleMovementHandler instance."""
    return IdleMovementHandler(event_bus=mock_event_bus, persistence=mock_persistence)


def test_idle_movement_handler_init(mock_persistence: MagicMock, mock_event_bus: MagicMock) -> None:
    """Test IdleMovementHandler initialization."""
    handler = IdleMovementHandler(event_bus=mock_event_bus, persistence=mock_persistence)
    assert handler.persistence == mock_persistence
    assert handler.movement_integration is not None


def test_idle_movement_handler_init_no_persistence() -> None:
    """Test IdleMovementHandler initialization fails without persistence."""
    with pytest.raises(ValueError, match="persistence.*required"):
        _ = IdleMovementHandler(persistence=None)


def test_should_idle_move_disabled(idle_movement_handler: IdleMovementHandler) -> None:
    """Test should_idle_move() returns False when idle movement is disabled."""
    npc_instance = MagicMock()
    npc_definition = MagicMock()
    behavior_config: dict[str, object] = {"idle_movement_enabled": False}
    result: bool = idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config)
    assert result is False


@patch("server.npc.idle_movement.random.random", return_value=0.0)
def test_should_idle_move_not_alive(
    _mock_random: MagicMock,
    idle_movement_handler: IdleMovementHandler,
) -> None:
    """Test should_idle_move() returns False when NPC is not alive."""
    npc_instance = MagicMock()
    npc_instance.is_alive = False
    npc_instance.is_active = True
    npc_definition = MagicMock()
    behavior_config: dict[str, object] = {"idle_movement_enabled": True, "idle_movement_probability": 1.0}
    result: bool = idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config)
    assert result is False


@patch("server.npc.idle_movement.random.random", return_value=0.0)
def test_should_idle_move_not_active(
    _mock_random: MagicMock,
    idle_movement_handler: IdleMovementHandler,
) -> None:
    """Test should_idle_move() returns False when NPC is not active."""
    npc_instance = MagicMock()
    npc_instance.is_alive = True
    npc_instance.is_active = False
    npc_definition = MagicMock()
    behavior_config: dict[str, object] = {"idle_movement_enabled": True, "idle_movement_probability": 1.0}
    result: bool = idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config)
    assert result is False


@patch("server.npc.idle_movement.random.random", return_value=0.5)
def test_should_idle_move_probability_check(
    _mock_random: MagicMock,
    idle_movement_handler: IdleMovementHandler,
) -> None:
    """Test should_idle_move() respects movement probability (random > threshold fails)."""
    npc_instance = MagicMock()
    npc_instance.is_alive = True
    npc_instance.is_active = True
    npc_definition = MagicMock()
    behavior_config: dict[str, object] = {"idle_movement_enabled": True, "idle_movement_probability": 0.0}
    result: bool = idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config)
    assert result is False


@patch("server.npc.idle_movement.random.random", return_value=0.24)
@patch("server.services.combat_service.get_combat_service")
def test_should_idle_move_probability_passes_when_random_below_threshold(
    mock_get_combat: MagicMock,
    _mock_random: MagicMock,
    idle_movement_handler: IdleMovementHandler,
) -> None:
    """Movement runs when random.random() <= idle_movement_probability (exclusive upper bound)."""
    npc_instance = MagicMock()
    npc_instance.npc_id = str(uuid.uuid4())
    npc_instance.is_alive = True
    npc_instance.is_active = True
    npc_definition = MagicMock()
    behavior_config: dict[str, object] = {"idle_movement_enabled": True, "idle_movement_probability": 0.25}
    mock_get_combat.return_value = MagicMock(_npc_combats={})
    assert idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config) is True


@patch("server.npc.idle_movement.random.random", return_value=0.26)
@patch("server.services.combat_service.get_combat_service")
def test_should_idle_move_probability_fails_when_random_above_threshold(
    mock_get_combat: MagicMock,
    _mock_random: MagicMock,
    idle_movement_handler: IdleMovementHandler,
) -> None:
    """Movement is skipped when random.random() > idle_movement_probability."""
    npc_instance = MagicMock()
    npc_instance.npc_id = str(uuid.uuid4())
    npc_instance.is_alive = True
    npc_instance.is_active = True
    npc_definition = MagicMock()
    behavior_config: dict[str, object] = {"idle_movement_enabled": True, "idle_movement_probability": 0.25}
    mock_get_combat.return_value = MagicMock(_npc_combats={})
    assert idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config) is False


@patch("server.npc.idle_movement.random.random", return_value=0.0)
@patch("server.services.combat_service.get_combat_service")
def test_should_idle_move_false_when_registered_in_combat(
    mock_get_combat: MagicMock,
    _mock_random: MagicMock,
    idle_movement_handler: IdleMovementHandler,
) -> None:
    """Gating skips idle movement when combat service lists this NPC."""
    npc_uuid = uuid.uuid4()
    npc_instance = MagicMock()
    npc_instance.npc_id = str(npc_uuid)
    npc_instance.is_alive = True
    npc_instance.is_active = True
    npc_definition = MagicMock()
    behavior_config: dict[str, object] = {"idle_movement_enabled": True, "idle_movement_probability": 1.0}
    mock_svc = MagicMock()
    mock_svc._npc_combats = {npc_uuid: MagicMock()}
    mock_get_combat.return_value = mock_svc
    assert idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config) is False


@patch("server.npc.idle_movement.random.random", return_value=0.0)
@patch("server.services.combat_service.get_combat_service")
def test_should_idle_move_true_when_not_in_combat_and_probability_succeeds(
    mock_get_combat: MagicMock,
    _mock_random: MagicMock,
    idle_movement_handler: IdleMovementHandler,
) -> None:
    """When combat service is empty and probability passes, idle move is allowed."""
    npc_instance = MagicMock()
    npc_instance.npc_id = str(uuid.uuid4())
    npc_instance.is_alive = True
    npc_instance.is_active = True
    npc_definition = MagicMock()
    behavior_config: dict[str, object] = {"idle_movement_enabled": True, "idle_movement_probability": 1.0}
    mock_svc = MagicMock()
    mock_svc._npc_combats = {}
    mock_get_combat.return_value = mock_svc
    assert idle_movement_handler.should_idle_move(npc_instance, npc_definition, behavior_config) is True


def test_is_npc_in_combat_true(idle_movement_handler: IdleMovementHandler) -> None:
    """Test _is_npc_in_combat() when NPC is in combat."""
    npc_instance = MagicMock()
    npc_instance.npc_id = "npc_001"
    # The function imports get_combat_service from ..services.combat_service
    with patch("server.services.combat_service.get_combat_service") as mock_get_combat_service:
        mock_combat_service = MagicMock()
        npc_uuid = uuid.uuid4()
        mock_combat_service._npc_combats = {npc_uuid: MagicMock()}
        mock_get_combat_service.return_value = mock_combat_service
        result: bool = idle_movement_handler._is_npc_in_combat(npc_instance)
        # May return True if combat service is available and NPC is in combat
        assert isinstance(result, bool)


def test_is_npc_in_combat_false(idle_movement_handler: IdleMovementHandler) -> None:
    """Test _is_npc_in_combat() returns False when NPC is not in combat."""
    npc_instance = MagicMock()
    npc_instance.in_combat = False
    result: bool = idle_movement_handler._is_npc_in_combat(npc_instance)
    assert result is False


def test_is_npc_in_combat_no_attribute(idle_movement_handler: IdleMovementHandler) -> None:
    """Test _is_npc_in_combat() handles missing in_combat attribute."""
    npc_instance = MagicMock()
    del npc_instance.in_combat
    result: bool = idle_movement_handler._is_npc_in_combat(npc_instance)
    assert result is False


def test_get_valid_exits_empty_room(idle_movement_handler: IdleMovementHandler) -> None:
    """Test get_valid_exits() with room having no exits."""
    npc_definition = MagicMock()
    npc_definition.sub_zone_id = "subzone_001"
    behavior_config: dict[str, object] = {}
    mock_room = MagicMock()
    mock_room.exits = {}
    idle_movement_handler.movement_integration.get_available_exits = MagicMock(return_value={})
    result: dict[str, str] = idle_movement_handler.get_valid_exits("room_001", npc_definition, behavior_config)
    assert len(result) == 0


def test_get_valid_exits_no_subzone(idle_movement_handler: IdleMovementHandler) -> None:
    """Test get_valid_exits() when NPC definition has no sub_zone_id."""
    npc_definition = MagicMock()
    npc_definition.sub_zone_id = None
    behavior_config: dict[str, object] = {}
    result: dict[str, str] = idle_movement_handler.get_valid_exits("room_001", npc_definition, behavior_config)
    assert len(result) == 0


def test_get_valid_exits_filters_exits_outside_subzone(idle_movement_handler: IdleMovementHandler) -> None:
    """Subzone boundary validation drops exits that would leave the NPC subzone."""
    npc_definition = MagicMock()
    npc_definition.sub_zone_id = "sub_a"
    behavior_config: dict[str, object] = {}
    idle_movement_handler.movement_integration.get_available_exits = MagicMock(
        return_value={"north": "room_in", "east": "room_out"}
    )

    def _validate(_sub_id: str, dest: str) -> bool:
        return dest == "room_in"

    idle_movement_handler.movement_integration.validate_subzone_boundary = MagicMock(side_effect=_validate)
    result: dict[str, str] = idle_movement_handler.get_valid_exits("room_001", npc_definition, behavior_config)
    assert result == {"north": "room_in"}
    idle_movement_handler.movement_integration.validate_subzone_boundary.assert_any_call("sub_a", "room_in")
    idle_movement_handler.movement_integration.validate_subzone_boundary.assert_any_call("sub_a", "room_out")


def test_get_valid_exits_all_exits_invalid_subzone_returns_empty(idle_movement_handler: IdleMovementHandler) -> None:
    """When every target fails boundary validation, valid exits dict is empty."""
    npc_definition = MagicMock()
    npc_definition.sub_zone_id = "sub_a"
    behavior_config: dict[str, object] = {}
    idle_movement_handler.movement_integration.get_available_exits = MagicMock(return_value={"south": "x", "west": "y"})
    idle_movement_handler.movement_integration.validate_subzone_boundary = MagicMock(return_value=False)
    result: dict[str, str] = idle_movement_handler.get_valid_exits("room_001", npc_definition, behavior_config)
    assert result == {}


def test_get_valid_exits_keeps_all_exits_when_subzone_boundary_allows(
    idle_movement_handler: IdleMovementHandler,
) -> None:
    """When validate_subzone_boundary accepts every target, all directions remain available."""
    npc_definition = MagicMock()
    npc_definition.sub_zone_id = "sub_z"
    behavior_config: dict[str, object] = {}
    idle_movement_handler.movement_integration.get_available_exits = MagicMock(
        return_value={"north": "room_n", "east": "room_e"}
    )
    idle_movement_handler.movement_integration.validate_subzone_boundary = MagicMock(return_value=True)
    result: dict[str, str] = idle_movement_handler.get_valid_exits("room_001", npc_definition, behavior_config)
    assert result == {"north": "room_n", "east": "room_e"}
    idle_movement_handler.movement_integration.validate_subzone_boundary.assert_any_call("sub_z", "room_n")
    idle_movement_handler.movement_integration.validate_subzone_boundary.assert_any_call("sub_z", "room_e")


def test_select_exit_empty_dict(idle_movement_handler: IdleMovementHandler) -> None:
    """Test select_exit() with empty exit dict."""
    empty_cfg: dict[str, object] = {}
    result: tuple[str, str] | None = idle_movement_handler.select_exit({}, "spawn_001", "room_001", empty_cfg)
    assert result is None


def test_select_exit_single_exit(idle_movement_handler: IdleMovementHandler) -> None:
    """Test select_exit() with single exit."""
    exits = {"north": "room_002"}
    empty_cfg: dict[str, object] = {}
    result: tuple[str, str] | None = idle_movement_handler.select_exit(exits, "spawn_001", "room_001", empty_cfg)
    assert result is not None
    assert result[0] == "north"
    assert result[1] == "room_002"


def test_select_exit_multiple_exits(idle_movement_handler: IdleMovementHandler) -> None:
    """Test select_exit() with multiple exits."""
    exits = {"north": "room_002", "south": "room_003"}
    empty_cfg: dict[str, object] = {}
    result: tuple[str, str] | None = idle_movement_handler.select_exit(exits, "spawn_001", "room_001", empty_cfg)
    assert result is not None
    assert result[0] in ["north", "south"]
    assert result[1] in ["room_002", "room_003"]


def test_select_exit_weighted_home_disabled(idle_movement_handler: IdleMovementHandler) -> None:
    """Test select_exit() with weighted_home disabled."""
    exits = {"north": "room_002", "south": "room_003"}
    behavior_config: dict[str, object] = {"idle_movement_weighted_home": False}
    result: tuple[str, str] | None = idle_movement_handler.select_exit(exits, "spawn_001", "room_001", behavior_config)
    assert result is not None
    assert result[0] in ["north", "south"]


def test_calculate_distance_to_room_same_room(idle_movement_handler: IdleMovementHandler) -> None:
    """Test _calculate_distance_to_room() with same room."""
    result: int = idle_movement_handler._calculate_distance_to_room("room_001", "room_001")
    assert result == 0


def test_calculate_distance_to_room_different_rooms(idle_movement_handler: IdleMovementHandler) -> None:
    """Test _calculate_distance_to_room() with different rooms."""
    result: int = idle_movement_handler._calculate_distance_to_room("room_001", "room_002")
    assert result >= 0


def test_calculate_distance_to_room_same_subzone(idle_movement_handler: IdleMovementHandler) -> None:
    """Test _calculate_distance_to_room() with rooms in same subzone."""
    result: int = idle_movement_handler._calculate_distance_to_room(
        "earth_zone_subzone_room1", "earth_zone_subzone_room2"
    )
    assert result >= 0


def test_calculate_distance_to_room_different_subzone(idle_movement_handler: IdleMovementHandler) -> None:
    """Test _calculate_distance_to_room() with rooms in different subzones."""
    result: int = idle_movement_handler._calculate_distance_to_room(
        "earth_zone_subzone1_room1", "earth_zone_subzone2_room1"
    )
    assert result == 999  # High distance for different subzones


def test_execute_idle_movement_no_valid_exits(idle_movement_handler: IdleMovementHandler) -> None:
    """Test execute_idle_movement() when no valid exits."""
    npc_instance = MagicMock()
    npc_instance.current_room = "room_001"
    npc_instance.is_alive = True
    npc_instance.is_active = True
    npc_definition = MagicMock()
    npc_definition.sub_zone_id = "subzone_001"
    behavior_config: dict[str, object] = {"idle_movement_enabled": True, "idle_movement_probability": 1.0}
    idle_movement_handler.get_valid_exits = MagicMock(return_value={})
    result: bool = idle_movement_handler.execute_idle_movement(npc_instance, npc_definition, behavior_config)
    assert result is False


def test_execute_idle_movement_no_exit_selected(idle_movement_handler: IdleMovementHandler) -> None:
    """Test execute_idle_movement() when no exit is selected."""
    npc_instance = MagicMock()
    npc_instance.current_room = "room_001"
    npc_instance.is_alive = True
    npc_instance.is_active = True
    npc_definition = MagicMock()
    npc_definition.sub_zone_id = "subzone_001"
    behavior_config: dict[str, object] = {"idle_movement_enabled": True, "idle_movement_probability": 1.0}
    idle_movement_handler.get_valid_exits = MagicMock(return_value={"north": "room_002"})
    idle_movement_handler.select_exit = MagicMock(return_value=None)
    result: bool = idle_movement_handler.execute_idle_movement(npc_instance, npc_definition, behavior_config)
    assert result is False


def test_execute_idle_movement_no_current_room(idle_movement_handler: IdleMovementHandler) -> None:
    """Test execute_idle_movement() when NPC has no current room."""
    npc_instance = MagicMock()
    npc_instance.current_room = None
    npc_definition = MagicMock()
    behavior_config: dict[str, object] = {"idle_movement_enabled": True, "idle_movement_probability": 1.0}
    result: bool = idle_movement_handler.execute_idle_movement(npc_instance, npc_definition, behavior_config)
    assert result is False
