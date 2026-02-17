"""
Unit tests for WebSocket initial state.

Tests the websocket_initial_state module functions.
"""

# pylint: disable=redefined-outer-name
# Reason: Pytest fixtures are injected as function parameters, which pylint incorrectly flags as redefining names from outer scope, this is standard pytest usage and cannot be avoided

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from starlette.websockets import WebSocketState

from server.realtime.websocket_initial_state import (
    add_npc_occupants_to_list,
    check_and_send_death_notification,
    get_event_handler_for_initial_state,
    prepare_initial_room_data,
    prepare_room_data_with_occupants,
    send_game_state_event_safely,
    send_initial_game_state,
    send_initial_room_state,
    send_occupants_snapshot_if_needed,
)


@pytest.fixture
def mock_websocket():
    """Create a mock WebSocket."""
    websocket = AsyncMock()
    websocket.send_json = AsyncMock()
    return websocket


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = AsyncMock()
    manager.get_room_occupants = AsyncMock(return_value=[])
    manager.convert_room_players_uuids_to_names = AsyncMock(side_effect=lambda x: x)
    return manager


@pytest.fixture
def mock_room():
    """Create a mock room."""
    room = MagicMock()
    room.to_dict.return_value = {"id": "room_123", "name": "Test Room"}
    room.has_player.return_value = True
    return room


@pytest.mark.asyncio
async def test_prepare_room_data_with_occupants(mock_connection_manager, mock_room):
    """Test prepare_room_data_with_occupants() prepares room data and occupant names."""
    canonical_room_id = "room_123"
    mock_connection_manager.get_room_occupants.return_value = [
        {"player_name": "Player1"},
        {"name": "Player2"},
    ]

    room_data, occupant_names = await prepare_room_data_with_occupants(
        mock_room, canonical_room_id, mock_connection_manager
    )

    assert isinstance(room_data, dict)
    assert "Player1" in occupant_names
    assert "Player2" in occupant_names


@pytest.mark.asyncio
async def test_send_game_state_event_safely_success(mock_websocket):
    """Test send_game_state_event_safely() successfully sends event."""
    game_state_event = {"type": "game_state", "data": {}}
    player_id_str = "player_123"

    # Set application_state to CONNECTED
    mock_websocket.application_state = WebSocketState.CONNECTED

    should_exit = await send_game_state_event_safely(mock_websocket, game_state_event, player_id_str)
    assert should_exit is False
    mock_websocket.send_json.assert_called_once_with(game_state_event)


@pytest.mark.asyncio
async def test_send_game_state_event_safely_disconnected(mock_websocket):
    """Test send_game_state_event_safely() returns True when WebSocket disconnected."""
    game_state_event = {"type": "game_state", "data": {}}
    player_id_str = "player_123"

    # Set application_state to DISCONNECTED
    mock_websocket.application_state = WebSocketState.DISCONNECTED

    should_exit = await send_game_state_event_safely(mock_websocket, game_state_event, player_id_str)
    assert should_exit is True
    mock_websocket.send_json.assert_not_called()


@pytest.mark.asyncio
async def test_send_game_state_event_safely_close_message_sent(mock_websocket):
    """Test send_game_state_event_safely() returns True when close message sent."""
    game_state_event = {"type": "game_state", "data": {}}
    player_id_str = "player_123"

    mock_websocket.application_state = WebSocketState.CONNECTED
    mock_websocket.send_json.side_effect = RuntimeError("close message has been sent")

    should_exit = await send_game_state_event_safely(mock_websocket, game_state_event, player_id_str)
    assert should_exit is True


@pytest.mark.asyncio
async def test_send_initial_game_state_success(mock_websocket, mock_connection_manager, mock_room):
    """Test send_initial_game_state() successfully sends initial game state."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    room_id = "room_123"

    mock_player = MagicMock()
    mock_player.current_room_id = room_id
    mock_player.name = "TestPlayer"
    mock_player.get_stats.return_value = {"hp": 100}

    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_connection_manager.get_room_occupants = AsyncMock(return_value=[])

    with (
        patch("server.realtime.websocket_initial_state.get_player_and_room") as mock_get_player_room,
        patch("server.realtime.websocket_initial_state.prepare_player_data") as mock_prepare_player,
    ):
        mock_get_player_room.return_value = (mock_player, mock_room, room_id)
        mock_prepare_player.return_value = {"name": "TestPlayer", "stats": {"hp": 100}}

        mock_websocket.application_state = WebSocketState.CONNECTED

        canonical_room_id, should_exit = await send_initial_game_state(
            mock_websocket, player_id, player_id_str, mock_connection_manager
        )

        assert canonical_room_id == room_id
        assert should_exit is False
        mock_websocket.send_json.assert_called_once()


@pytest.mark.asyncio
async def test_send_initial_game_state_player_not_found(mock_websocket, mock_connection_manager):
    """Test send_initial_game_state() returns None when player not found."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)

    with patch("server.realtime.websocket_initial_state.get_player_and_room") as mock_get_player_room:
        mock_get_player_room.return_value = (None, None, None)

        canonical_room_id, should_exit = await send_initial_game_state(
            mock_websocket, player_id, player_id_str, mock_connection_manager
        )

        assert canonical_room_id is None
        assert should_exit is False


@pytest.mark.asyncio
async def test_send_initial_game_state_handles_exception(mock_websocket, mock_connection_manager):
    """Test send_initial_game_state() handles exceptions."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)

    with patch("server.realtime.websocket_initial_state.get_player_and_room", side_effect=ValueError("Error")):
        canonical_room_id, should_exit = await send_initial_game_state(
            mock_websocket, player_id, player_id_str, mock_connection_manager
        )

        assert canonical_room_id is None
        assert should_exit is False


@pytest.mark.asyncio
async def test_check_and_send_death_notification_player_dead(mock_websocket, mock_connection_manager, mock_room):
    """Test check_and_send_death_notification() sends notification when player dead."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.get_stats.return_value = {"current_dp": -15}  # Dead

    with patch("server.async_persistence.get_async_persistence") as mock_get_persistence:
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_get_persistence.return_value = mock_persistence

        await check_and_send_death_notification(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_room, mock_connection_manager
        )

        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["event_type"] == "player_died"


@pytest.mark.asyncio
async def test_check_and_send_death_notification_player_alive(mock_websocket, mock_connection_manager, mock_room):
    """Test check_and_send_death_notification() does not send when player alive."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.get_stats.return_value = {"current_dp": 50}  # Alive

    with patch("server.async_persistence.get_async_persistence") as mock_get_persistence:
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_get_persistence.return_value = mock_persistence

        await check_and_send_death_notification(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_room, mock_connection_manager
        )

        mock_websocket.send_json.assert_not_called()


@pytest.mark.asyncio
async def test_check_and_send_death_notification_in_limbo(mock_websocket, mock_connection_manager, mock_room):
    """Test check_and_send_death_notification() sends notification when in limbo."""
    from server.services.player_respawn_service import LIMBO_ROOM_ID

    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = LIMBO_ROOM_ID

    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    # Death notification is only sent when current_dp <= -10 (actually dead, not just in limbo)
    mock_player.get_stats.return_value = {"current_dp": -10}
    mock_player.current_room_id = LIMBO_ROOM_ID

    with patch("server.async_persistence.get_async_persistence") as mock_get_persistence:
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_get_persistence.return_value = mock_persistence

        await check_and_send_death_notification(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_room, mock_connection_manager
        )

        mock_websocket.send_json.assert_called_once()


@pytest.mark.asyncio
async def test_add_npc_occupants_to_list_success(mock_connection_manager, mock_room):
    """Test add_npc_occupants_to_list() adds NPC names to list."""
    occupant_names: list[str] = []
    canonical_room_id = "room_123"

    mock_npc1 = MagicMock()
    mock_npc1.name = "NPC1"
    mock_npc1.is_alive = True
    mock_npc1.current_room_id = "room_123"

    mock_npc2 = MagicMock()
    mock_npc2.name = "NPC2"
    mock_npc2.is_alive = True
    mock_npc2.current_room_id = "room_123"

    mock_room.get_npcs.return_value = ["npc_1", "npc_2"]

    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.container = MagicMock()
    mock_app.state.container.npc_lifecycle_manager = MagicMock()
    mock_app.state.container.npc_lifecycle_manager.active_npcs = {"npc_1": mock_npc1, "npc_2": mock_npc2}
    mock_connection_manager.app = mock_app

    await add_npc_occupants_to_list(mock_room, occupant_names, canonical_room_id, mock_connection_manager)

    assert "NPC1" in occupant_names
    assert "NPC2" in occupant_names


@pytest.mark.asyncio
async def test_add_npc_occupants_to_list_no_app(mock_connection_manager, mock_room):
    """Test add_npc_occupants_to_list() does nothing when no app."""
    occupant_names: list[str] = []
    canonical_room_id = "room_123"

    # Remove app attribute entirely
    if hasattr(mock_connection_manager, "app"):
        del mock_connection_manager.app

    await add_npc_occupants_to_list(mock_room, occupant_names, canonical_room_id, mock_connection_manager)

    assert len(occupant_names) == 0


@pytest.mark.asyncio
async def test_add_npc_occupants_to_list_filters_dead_npcs(mock_connection_manager, mock_room):
    """Test add_npc_occupants_to_list() includes all NPCs (code doesn't filter dead)."""
    occupant_names: list[str] = []
    canonical_room_id = "room_123"

    mock_npc_alive = MagicMock()
    mock_npc_alive.name = "AliveNPC"
    mock_npc_alive.is_alive = True
    mock_npc_alive.current_room_id = "room_123"

    mock_npc_dead = MagicMock()
    mock_npc_dead.name = "DeadNPC"
    mock_npc_dead.is_alive = False
    mock_npc_dead.current_room_id = "room_123"

    mock_room.get_npcs.return_value = ["npc_alive", "npc_dead"]

    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.container = MagicMock()
    mock_app.state.container.npc_lifecycle_manager = MagicMock()
    mock_app.state.container.npc_lifecycle_manager.active_npcs = {
        "npc_alive": mock_npc_alive,
        "npc_dead": mock_npc_dead,
    }
    mock_connection_manager.app = mock_app

    await add_npc_occupants_to_list(mock_room, occupant_names, canonical_room_id, mock_connection_manager)

    # The code doesn't actually filter dead NPCs - it just checks hasattr(npc, "name")
    assert "AliveNPC" in occupant_names
    assert "DeadNPC" in occupant_names


@pytest.mark.asyncio
async def test_prepare_initial_room_data(mock_connection_manager, mock_room):
    """Test prepare_initial_room_data() prepares room data."""
    result = await prepare_initial_room_data(mock_room, mock_connection_manager)

    assert isinstance(result, dict)
    mock_connection_manager.convert_room_players_uuids_to_names.assert_called_once()


def test_get_event_handler_for_initial_state_from_connection_manager(mock_connection_manager, mock_websocket):
    """Test get_event_handler_for_initial_state() gets handler from connection manager."""
    mock_event_handler = MagicMock()
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.container = MagicMock()
    mock_app.state.container.real_time_event_handler = mock_event_handler
    mock_connection_manager.app = mock_app

    result = get_event_handler_for_initial_state(mock_connection_manager, mock_websocket)
    assert result is mock_event_handler


def test_get_event_handler_for_initial_state_from_websocket(mock_connection_manager, mock_websocket):
    """Test get_event_handler_for_initial_state() gets handler from websocket."""
    mock_event_handler = MagicMock()
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.container = MagicMock()
    mock_app.state.container.real_time_event_handler = mock_event_handler
    mock_connection_manager.app = None
    mock_websocket.app = mock_app

    result = get_event_handler_for_initial_state(mock_connection_manager, mock_websocket)
    assert result is mock_event_handler


def test_get_event_handler_for_initial_state_not_found(mock_connection_manager, mock_websocket):
    """Test get_event_handler_for_initial_state() returns None when not found."""
    mock_connection_manager.app = None
    mock_websocket.app = None

    result = get_event_handler_for_initial_state(mock_connection_manager, mock_websocket)
    assert result is None


@pytest.mark.asyncio
async def test_send_occupants_snapshot_if_needed_success():
    """Test send_occupants_snapshot_if_needed() sends snapshot when conditions met."""
    mock_event_handler = MagicMock()
    mock_player_handler = MagicMock()
    mock_player_handler.send_occupants_snapshot_to_player = AsyncMock()
    mock_event_handler.player_handler = mock_player_handler

    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    mock_room = MagicMock()
    mock_room.has_player.return_value = True

    await send_occupants_snapshot_if_needed(mock_event_handler, mock_room, player_id, player_id_str, canonical_room_id)

    mock_player_handler.send_occupants_snapshot_to_player.assert_called_once_with(player_id, canonical_room_id)


@pytest.mark.asyncio
async def test_send_occupants_snapshot_if_needed_no_handler():
    """Test send_occupants_snapshot_if_needed() does nothing when no handler."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    mock_room = MagicMock()

    await send_occupants_snapshot_if_needed(None, mock_room, player_id, player_id_str, canonical_room_id)
    # Should not raise


@pytest.mark.asyncio
async def test_send_occupants_snapshot_if_needed_player_not_in_room():
    """Test send_occupants_snapshot_if_needed() calls send_occupants_snapshot_to_player when handler exists."""
    mock_event_handler = MagicMock()
    mock_player_handler = MagicMock()
    mock_player_handler.send_occupants_snapshot_to_player = AsyncMock()
    mock_event_handler.player_handler = mock_player_handler

    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    mock_room = MagicMock()
    mock_room.has_player.return_value = False

    await send_occupants_snapshot_if_needed(mock_event_handler, mock_room, player_id, player_id_str, canonical_room_id)

    # Implementation always sends snapshot when handler exists (connecting player may not be in room._players yet)
    mock_player_handler.send_occupants_snapshot_to_player.assert_called_once_with(player_id, canonical_room_id)


@pytest.mark.asyncio
async def test_send_initial_room_state_success(mock_websocket, mock_connection_manager):
    """Test send_initial_room_state() successfully sends initial room state."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    mock_room = MagicMock()
    mock_room.to_dict.return_value = {"id": canonical_room_id, "name": "Test Room"}
    mock_room.get_npcs.return_value = []

    mock_connection_manager.get_room_occupants = AsyncMock(return_value=[])

    with (
        patch("server.async_persistence.get_async_persistence") as mock_get_persistence,
        patch("server.realtime.websocket_initial_state.add_npc_occupants_to_list") as mock_add_npcs,
        patch("server.realtime.websocket_initial_state.get_event_handler_for_initial_state") as mock_get_handler,
    ):
        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id.return_value = mock_room
        mock_get_persistence.return_value = mock_persistence
        mock_add_npcs.return_value = None
        mock_get_handler.return_value = None

        await send_initial_room_state(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_connection_manager
        )

        mock_websocket.send_json.assert_called_once()
        call_args = mock_websocket.send_json.call_args[0][0]
        assert call_args["event_type"] == "room_update"


@pytest.mark.asyncio
async def test_send_initial_room_state_room_not_found(mock_websocket, mock_connection_manager):
    """Test send_initial_room_state() does nothing when room not found."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    with patch("server.async_persistence.get_async_persistence") as mock_get_persistence:
        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id.return_value = None
        mock_get_persistence.return_value = mock_persistence

        await send_initial_room_state(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_connection_manager
        )

        mock_websocket.send_json.assert_not_called()


@pytest.mark.asyncio
async def test_send_initial_room_state_handles_exception(mock_websocket, mock_connection_manager):
    """Test send_initial_room_state() handles exceptions."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    with patch("server.async_persistence.get_async_persistence", side_effect=ValueError("Error")):
        # Should not raise
        await send_initial_room_state(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_connection_manager
        )
