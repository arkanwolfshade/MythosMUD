"""
Unit tests for /flee command (handle_flee_command).
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.combat import CombatCommandHandler, get_combat_command_handler
from server.models.combat import CombatInstance, CombatParticipant, CombatParticipantType
from server.models.game import PositionState

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


def _make_participant(participant_id: uuid.UUID, name: str = "Player", dp: int = 100) -> CombatParticipant:
    return CombatParticipant(
        participant_id=participant_id,
        participant_type=CombatParticipantType.PLAYER,
        name=name,
        current_dp=dp,
        max_dp=100,
        dexterity=10,
        is_active=True,
    )


@pytest.fixture
def flee_handler_deps():
    """CombatCommandHandler deps for flee: combat_service, movement_service, player_position_service, persistence."""
    combat_service = AsyncMock()
    movement_service = AsyncMock()
    player_position_service = AsyncMock()
    persistence = MagicMock()
    room_with_exits = MagicMock()
    room_with_exits.exits = {"north": "room_2", "south": "room_3"}
    persistence.get_room_by_id = MagicMock(return_value=room_with_exits)
    persistence.get_player_by_name = AsyncMock()
    return {
        "combat_service": combat_service,
        "movement_service": movement_service,
        "player_position_service": player_position_service,
        "async_persistence": persistence,
    }


@pytest.fixture
def handler(flee_handler_deps):
    """CombatCommandHandler with flee-related deps."""
    return CombatCommandHandler(
        combat_service=flee_handler_deps["combat_service"],
        movement_service=flee_handler_deps["movement_service"],
        player_position_service=flee_handler_deps["player_position_service"],
        async_persistence=flee_handler_deps["async_persistence"],
    )


@pytest.fixture
def standing_player():
    """Player that is standing and in a room."""
    player_id = uuid.uuid4()
    p = MagicMock()
    p.player_id = player_id
    p.current_room_id = "room_1"
    p.get_stats = MagicMock(return_value={"position": PositionState.STANDING})
    p.name = "TestPlayer"
    return p


def _request_with_persistence(persistence, player=None):
    """Build request.app so _get_player_and_room gets player and room from persistence."""
    request = MagicMock()
    app = MagicMock()
    app.state.persistence = persistence
    app.state.container = None  # Force use of state.persistence (container.async_persistence would be used otherwise)
    # _get_player_and_room awaits persistence.get_player_by_name - must be AsyncMock
    persistence.get_player_by_name = AsyncMock(return_value=player)
    request.app = app
    return request


@pytest.mark.asyncio
async def test_flee_not_in_combat_returns_message(handler, flee_handler_deps, standing_player):
    """When not in combat, flee returns 'You are not in combat.'"""
    flee_handler_deps["combat_service"].get_combat_by_participant = AsyncMock(return_value=None)
    flee_handler_deps["async_persistence"].get_player_by_name = AsyncMock(return_value=standing_player)
    request = _request_with_persistence(flee_handler_deps["async_persistence"], standing_player)
    result = await handler.handle_flee_command(
        {},
        {"username": "TestPlayer"},
        request,
        None,
        "TestPlayer",
    )
    assert "not in combat" in result.get("result", "").lower()


@pytest.mark.asyncio
async def test_flee_no_exits_returns_no_escape(handler, flee_handler_deps, standing_player):
    """When room has no exits, flee returns 'There is no escape!'"""
    player_id = standing_player.player_id
    combat = CombatInstance(
        combat_id=uuid.uuid4(), room_id="room_1", participants={player_id: _make_participant(player_id)}
    )
    flee_handler_deps["combat_service"].get_combat_by_participant = AsyncMock(return_value=combat)
    flee_handler_deps["async_persistence"].get_player_by_name = AsyncMock(return_value=standing_player)
    no_exits_room = MagicMock()
    no_exits_room.exits = {}
    flee_handler_deps["async_persistence"].get_room_by_id = MagicMock(return_value=no_exits_room)
    request = _request_with_persistence(flee_handler_deps["async_persistence"], standing_player)
    result = await handler.handle_flee_command(
        {},
        {"username": "TestPlayer"},
        request,
        None,
        "TestPlayer",
    )
    assert "no escape" in result.get("result", "").lower()


@pytest.mark.asyncio
async def test_flee_roll_fails_returns_failure_and_uses_action(handler, flee_handler_deps, standing_player):
    """When voluntary flee roll fails, failure message indicates the attack for this round is lost."""
    player_id = standing_player.player_id
    combat = CombatInstance(
        combat_id=uuid.uuid4(), room_id="room_1", participants={player_id: _make_participant(player_id)}
    )
    flee_handler_deps["combat_service"].get_combat_by_participant = AsyncMock(return_value=combat)
    flee_handler_deps["async_persistence"].get_player_by_name = AsyncMock(return_value=standing_player)
    with patch("server.commands.combat.execute_voluntary_flee", new_callable=AsyncMock, return_value=False):
        request = _request_with_persistence(flee_handler_deps["async_persistence"], standing_player)
        result = await handler.handle_flee_command(
            {},
            {"username": "TestPlayer"},
            request,
            None,
            "TestPlayer",
        )
    message = result.get("result", "").lower()
    assert "fail" in message
    assert "attack" in message or "chance" in message


@pytest.mark.asyncio
async def test_flee_roll_succeeds_returns_success(handler, flee_handler_deps, standing_player):
    """When voluntary flee succeeds, success message returned."""
    player_id = standing_player.player_id
    combat = CombatInstance(
        combat_id=uuid.uuid4(), room_id="room_1", participants={player_id: _make_participant(player_id)}
    )
    flee_handler_deps["combat_service"].get_combat_by_participant = AsyncMock(return_value=combat)
    flee_handler_deps["async_persistence"].get_player_by_name = AsyncMock(return_value=standing_player)
    with patch("server.commands.combat.execute_voluntary_flee", new_callable=AsyncMock, return_value=True):
        request = _request_with_persistence(flee_handler_deps["async_persistence"], standing_player)
        result = await handler.handle_flee_command(
            {},
            {"username": "TestPlayer"},
            request,
            None,
            "TestPlayer",
        )
    assert "safety" in result.get("result", "").lower() or "flee" in result.get("result", "").lower()


@pytest.mark.asyncio
async def test_flee_not_standing_forces_stand_and_returns_message(handler, flee_handler_deps, standing_player):
    """When not standing, change_position(standing) is called and scrabble message returned."""
    standing_player.get_stats = MagicMock(return_value={"position": "sitting"})
    flee_handler_deps["async_persistence"].get_player_by_name = AsyncMock(return_value=standing_player)
    flee_handler_deps["player_position_service"].change_position = AsyncMock()
    request = _request_with_persistence(flee_handler_deps["async_persistence"], standing_player)
    result = await handler.handle_flee_command(
        {},
        {"username": "TestPlayer"},
        request,
        None,
        "TestPlayer",
    )
    assert "scrabble" in result.get("result", "").lower() or "feet" in result.get("result", "").lower()
    flee_handler_deps["player_position_service"].change_position.assert_awaited_once_with("TestPlayer", "standing")


def test_get_combat_command_handler_includes_flee():
    """get_combat_command_handler returns a handler that has handle_flee_command when app is provided."""
    app = MagicMock()
    app.state.container = MagicMock()
    app.state.container.combat_service = None
    app.state.container.movement_service = None
    app.state.container.player_position_service = None
    app.state.container.async_persistence = MagicMock()  # Required by CombatCommandHandler __init__
    app.state.container.event_bus = None
    app.state.container.player_combat_service = None
    app.state.container.connection_manager = None
    app.state.container.item_prototype_registry = None
    app.state.container.party_service = None
    handler = get_combat_command_handler(app)
    assert hasattr(handler, "handle_flee_command")
    assert callable(handler.handle_flee_command)
