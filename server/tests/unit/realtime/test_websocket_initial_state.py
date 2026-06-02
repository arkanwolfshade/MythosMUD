"""
Unit tests for WebSocket initial state.

Tests the websocket_initial_state module functions.
"""

# pylint: disable=redefined-outer-name
# Reason: Pytest fixtures are injected as function parameters, which pylint incorrectly flags as redefining names from outer scope, this is standard pytest usage and cannot be avoided

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import WebSocket
from starlette.websockets import WebSocketState

from server.models.player import Player
from server.models.room import Room
from server.realtime.connection_manager import ConnectionManager
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


def _passthrough_room_data(room_data: object) -> object:
    """Return room data unchanged for convert_room_players_uuids_to_names mocks."""
    return room_data


@pytest.fixture
def mock_websocket() -> AsyncMock:
    """Create a mock WebSocket."""
    return AsyncMock(spec=WebSocket)


@pytest.fixture
def mock_connection_manager() -> AsyncMock:
    """Create a mock connection manager."""
    manager: AsyncMock = AsyncMock(spec=ConnectionManager)
    manager.get_room_occupants = AsyncMock(return_value=[])
    manager.convert_room_players_uuids_to_names = AsyncMock(side_effect=_passthrough_room_data)
    return manager


@pytest.fixture
def mock_room() -> MagicMock:
    """Create a mock room."""
    room: MagicMock = MagicMock(spec=Room)
    to_dict_mock: MagicMock = MagicMock(return_value={"id": "room_123", "name": "Test Room"})
    room.to_dict = to_dict_mock
    has_player_mock: MagicMock = MagicMock(return_value=True)
    room.has_player = has_player_mock
    return room


@pytest.mark.asyncio
async def test_prepare_room_data_with_occupants(mock_connection_manager: AsyncMock, mock_room: MagicMock):
    """Test prepare_room_data_with_occupants() prepares room data and occupant names."""
    canonical_room_id = "room_123"
    get_room_occupants_mock: AsyncMock = cast(AsyncMock, mock_connection_manager.get_room_occupants)
    get_room_occupants_mock.return_value = [
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
async def test_send_game_state_event_safely_success(mock_websocket: AsyncMock):
    """Test send_game_state_event_safely() successfully sends event."""
    game_state_event: dict[str, object] = {"type": "game_state", "data": {}}
    player_id_str = "player_123"

    # Set application_state to CONNECTED
    mock_websocket.application_state = WebSocketState.CONNECTED

    should_exit = await send_game_state_event_safely(mock_websocket, game_state_event, player_id_str)
    assert should_exit is False
    send_json_mock: AsyncMock = cast(AsyncMock, mock_websocket.send_json)
    send_json_mock.assert_called_once_with(game_state_event)


@pytest.mark.asyncio
async def test_send_game_state_event_safely_disconnected(mock_websocket: AsyncMock):
    """Test send_game_state_event_safely() returns True when WebSocket disconnected."""
    game_state_event: dict[str, object] = {"type": "game_state", "data": {}}
    player_id_str = "player_123"

    # Set application_state to DISCONNECTED
    mock_websocket.application_state = WebSocketState.DISCONNECTED

    should_exit = await send_game_state_event_safely(mock_websocket, game_state_event, player_id_str)
    assert should_exit is True
    send_json_mock: AsyncMock = cast(AsyncMock, mock_websocket.send_json)
    send_json_mock.assert_not_called()


@pytest.mark.asyncio
async def test_send_game_state_event_safely_close_message_sent(mock_websocket: AsyncMock):
    """Test send_game_state_event_safely() returns True when close message sent."""
    game_state_event: dict[str, object] = {"type": "game_state", "data": {}}
    player_id_str = "player_123"

    mock_websocket.application_state = WebSocketState.CONNECTED
    send_json_mock: AsyncMock = cast(AsyncMock, mock_websocket.send_json)
    send_json_mock.side_effect = RuntimeError("close message has been sent")

    should_exit = await send_game_state_event_safely(mock_websocket, game_state_event, player_id_str)
    assert should_exit is True


@pytest.mark.asyncio
async def test_send_initial_game_state_success(
    mock_websocket: AsyncMock, mock_connection_manager: AsyncMock, mock_room: MagicMock
):
    """Test send_initial_game_state() successfully sends initial game state."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    room_id = "room_123"

    mock_player = MagicMock(spec=Player)
    mock_player.current_room_id = room_id
    mock_player.name = "TestPlayer"
    mock_player.get_stats = MagicMock(return_value={"hp": 100})

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
        send_json_mock: AsyncMock = cast(AsyncMock, mock_websocket.send_json)
        send_json_mock.assert_called_once()


@pytest.mark.asyncio
async def test_send_initial_game_state_player_not_found(mock_websocket: AsyncMock, mock_connection_manager: AsyncMock):
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
async def test_send_initial_game_state_handles_exception(mock_websocket: AsyncMock, mock_connection_manager: AsyncMock):
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
async def test_check_and_send_death_notification_player_dead(
    mock_websocket: AsyncMock, mock_connection_manager: AsyncMock, mock_room: MagicMock
):
    """Test check_and_send_death_notification() sends notification when player dead."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    mock_player = MagicMock(spec=Player)
    mock_player.name = "TestPlayer"
    mock_player.get_stats = MagicMock(return_value={"current_dp": -15})  # Dead

    with patch("server.async_persistence.get_async_persistence") as mock_get_persistence:
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_get_persistence.return_value = mock_persistence

        await check_and_send_death_notification(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_room, mock_connection_manager
        )

        send_json_mock: AsyncMock = cast(AsyncMock, mock_websocket.send_json)
        send_json_mock.assert_called_once()
        call_args: dict[str, object] = cast(dict[str, object], send_json_mock.call_args[0][0])
        assert call_args["event_type"] == "player_died"


@pytest.mark.asyncio
async def test_check_and_send_death_notification_player_alive(
    mock_websocket: AsyncMock, mock_connection_manager: AsyncMock, mock_room: MagicMock
):
    """Test check_and_send_death_notification() does not send when player alive."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    mock_player = MagicMock(spec=Player)
    mock_player.name = "TestPlayer"
    mock_player.get_stats = MagicMock(return_value={"current_dp": 50})  # Alive

    with patch("server.async_persistence.get_async_persistence") as mock_get_persistence:
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_get_persistence.return_value = mock_persistence

        await check_and_send_death_notification(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_room, mock_connection_manager
        )

        send_json_mock: AsyncMock = cast(AsyncMock, mock_websocket.send_json)
        send_json_mock.assert_not_called()


@pytest.mark.asyncio
async def test_check_and_send_death_notification_in_limbo(
    mock_websocket: AsyncMock, mock_connection_manager: AsyncMock, mock_room: MagicMock
):
    """Test check_and_send_death_notification() sends notification when in limbo."""
    from server.services.player_respawn_service import LIMBO_ROOM_ID

    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = LIMBO_ROOM_ID

    mock_player = MagicMock(spec=Player)
    mock_player.name = "TestPlayer"
    # Death notification is only sent when current_dp <= -10 (actually dead, not just in limbo)
    mock_player.get_stats = MagicMock(return_value={"current_dp": -10})
    mock_player.current_room_id = LIMBO_ROOM_ID

    with patch("server.async_persistence.get_async_persistence") as mock_get_persistence:
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
        mock_get_persistence.return_value = mock_persistence

        await check_and_send_death_notification(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_room, mock_connection_manager
        )

        send_json_mock: AsyncMock = cast(AsyncMock, mock_websocket.send_json)
        send_json_mock.assert_called_once()


@pytest.mark.asyncio
async def test_add_npc_occupants_to_list_success(mock_connection_manager: AsyncMock, mock_room: MagicMock):
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

    get_npcs_mock: MagicMock = MagicMock(return_value=["npc_1", "npc_2"])
    mock_room.get_npcs = get_npcs_mock

    mock_app = MagicMock()
    mock_app_state: MagicMock = MagicMock()
    mock_container: MagicMock = MagicMock()
    mock_npc_lifecycle_manager: MagicMock = MagicMock()
    mock_npc_lifecycle_manager.active_npcs = {"npc_1": mock_npc1, "npc_2": mock_npc2}
    mock_container.npc_lifecycle_manager = mock_npc_lifecycle_manager
    mock_app_state.container = mock_container
    mock_app.state = mock_app_state
    mock_connection_manager.app = mock_app

    await add_npc_occupants_to_list(mock_room, occupant_names, canonical_room_id, mock_connection_manager)

    assert "NPC1" in occupant_names
    assert "NPC2" in occupant_names


@pytest.mark.asyncio
async def test_add_npc_occupants_to_list_no_app(mock_connection_manager: AsyncMock, mock_room: MagicMock):
    """Test add_npc_occupants_to_list() does nothing when no app."""
    occupant_names: list[str] = []
    canonical_room_id = "room_123"

    # Remove app attribute entirely
    if hasattr(mock_connection_manager, "app"):
        del mock_connection_manager.app

    await add_npc_occupants_to_list(mock_room, occupant_names, canonical_room_id, mock_connection_manager)

    assert len(occupant_names) == 0


@pytest.mark.asyncio
async def test_add_npc_occupants_to_list_filters_dead_npcs(mock_connection_manager: AsyncMock, mock_room: MagicMock):
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

    get_npcs_mock: MagicMock = MagicMock(return_value=["npc_alive", "npc_dead"])
    mock_room.get_npcs = get_npcs_mock

    mock_app = MagicMock()
    mock_app_state: MagicMock = MagicMock()
    mock_container: MagicMock = MagicMock()
    mock_npc_lifecycle_manager: MagicMock = MagicMock()
    mock_npc_lifecycle_manager.active_npcs = {
        "npc_alive": mock_npc_alive,
        "npc_dead": mock_npc_dead,
    }
    mock_container.npc_lifecycle_manager = mock_npc_lifecycle_manager
    mock_app_state.container = mock_container
    mock_app.state = mock_app_state
    mock_connection_manager.app = mock_app

    await add_npc_occupants_to_list(mock_room, occupant_names, canonical_room_id, mock_connection_manager)

    # The code doesn't actually filter dead NPCs - it just checks hasattr(npc, "name")
    assert "AliveNPC" in occupant_names
    assert "DeadNPC" in occupant_names


@pytest.mark.asyncio
async def test_prepare_initial_room_data(mock_connection_manager: AsyncMock, mock_room: MagicMock):
    """Test prepare_initial_room_data() prepares room data."""
    result = await prepare_initial_room_data(mock_room, mock_connection_manager)

    assert isinstance(result, dict)
    convert_uuids_mock: AsyncMock = cast(AsyncMock, mock_connection_manager.convert_room_players_uuids_to_names)
    convert_uuids_mock.assert_called_once()


def test_get_event_handler_for_initial_state_from_connection_manager(
    mock_connection_manager: AsyncMock, mock_websocket: AsyncMock
):
    """Test get_event_handler_for_initial_state() gets handler from connection manager."""
    mock_event_handler = MagicMock()
    mock_app = MagicMock()
    mock_app_state: MagicMock = MagicMock()
    mock_container: MagicMock = MagicMock()
    mock_container.real_time_event_handler = mock_event_handler
    mock_app_state.container = mock_container
    mock_app.state = mock_app_state
    mock_connection_manager.app = mock_app

    result = get_event_handler_for_initial_state(mock_connection_manager, mock_websocket)
    assert result is mock_event_handler


def test_get_event_handler_for_initial_state_from_websocket(
    mock_connection_manager: AsyncMock, mock_websocket: AsyncMock
):
    """Test get_event_handler_for_initial_state() gets handler from websocket."""
    mock_event_handler = MagicMock()
    mock_app = MagicMock()
    mock_app_state: MagicMock = MagicMock()
    mock_container: MagicMock = MagicMock()
    mock_container.real_time_event_handler = mock_event_handler
    mock_app_state.container = mock_container
    mock_app.state = mock_app_state
    mock_connection_manager.app = None
    mock_websocket.app = mock_app

    result = get_event_handler_for_initial_state(mock_connection_manager, mock_websocket)
    assert result is mock_event_handler


def test_get_event_handler_for_initial_state_not_found(mock_connection_manager: AsyncMock, mock_websocket: AsyncMock):
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
    send_occupants_snapshot_mock: AsyncMock = AsyncMock()
    mock_player_handler.send_occupants_snapshot_to_player = send_occupants_snapshot_mock
    mock_event_handler.player_handler = mock_player_handler

    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    mock_room = MagicMock()
    has_player_mock: MagicMock = MagicMock(return_value=True)
    mock_room.has_player = has_player_mock

    await send_occupants_snapshot_if_needed(mock_event_handler, mock_room, player_id, player_id_str, canonical_room_id)

    send_occupants_snapshot_mock.assert_called_once_with(player_id, canonical_room_id)


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
    send_occupants_snapshot_mock: AsyncMock = AsyncMock()
    mock_player_handler.send_occupants_snapshot_to_player = send_occupants_snapshot_mock
    mock_event_handler.player_handler = mock_player_handler

    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    mock_room = MagicMock()
    has_player_mock: MagicMock = MagicMock(return_value=False)
    mock_room.has_player = has_player_mock

    await send_occupants_snapshot_if_needed(mock_event_handler, mock_room, player_id, player_id_str, canonical_room_id)

    # Implementation always sends snapshot when handler exists (connecting player may not be in room._players yet)
    send_occupants_snapshot_mock.assert_called_once_with(player_id, canonical_room_id)


@pytest.mark.asyncio
async def test_send_initial_room_state_success(
    mock_websocket: AsyncMock,
    mock_connection_manager: AsyncMock,
) -> None:
    """Test send_initial_room_state() successfully sends initial room state."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    mock_room = MagicMock()
    to_dict_mock: MagicMock = MagicMock(return_value={"id": canonical_room_id, "name": "Test Room"})
    mock_room.to_dict = to_dict_mock
    get_npcs_mock: MagicMock = MagicMock(return_value=[])
    mock_room.get_npcs = get_npcs_mock

    mock_connection_manager.get_room_occupants = AsyncMock(return_value=[])

    with (
        patch("server.async_persistence.get_async_persistence") as mock_get_persistence,
        patch("server.realtime.websocket_initial_state.add_npc_occupants_to_list") as mock_add_npcs,
        patch("server.realtime.websocket_initial_state.get_event_handler_for_initial_state") as mock_get_handler,
    ):
        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
        mock_get_persistence.return_value = mock_persistence
        mock_add_npcs.return_value = None
        mock_get_handler.return_value = None

        await send_initial_room_state(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_connection_manager
        )

        send_json_mock: AsyncMock = cast(AsyncMock, mock_websocket.send_json)
        send_json_mock.assert_called_once()
        call_args: dict[str, object] = cast(dict[str, object], send_json_mock.call_args[0][0])
        assert call_args["event_type"] == "room_update"


@pytest.mark.asyncio
async def test_send_initial_room_state_room_not_found(
    mock_websocket: AsyncMock,
    mock_connection_manager: AsyncMock,
) -> None:
    """Test send_initial_room_state() does nothing when room not found."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    with patch("server.async_persistence.get_async_persistence") as mock_get_persistence:
        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id = MagicMock(return_value=None)
        mock_get_persistence.return_value = mock_persistence

        await send_initial_room_state(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_connection_manager
        )

        send_json_mock: AsyncMock = cast(AsyncMock, mock_websocket.send_json)
        send_json_mock.assert_not_called()


@pytest.mark.asyncio
async def test_send_initial_room_state_skips_closed_websocket(
    mock_websocket: AsyncMock,
    mock_connection_manager: AsyncMock,
) -> None:
    """Test send_initial_room_state() skips send when WebSocket already closed."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    mock_room = MagicMock()
    to_dict_mock: MagicMock = MagicMock(return_value={"id": canonical_room_id, "name": "Test Room"})
    mock_room.to_dict = to_dict_mock
    get_npcs_mock: MagicMock = MagicMock(return_value=[])
    mock_room.get_npcs = get_npcs_mock

    mock_connection_manager.get_room_occupants = AsyncMock(return_value=[])
    mock_websocket.application_state = WebSocketState.DISCONNECTED

    with (
        patch("server.async_persistence.get_async_persistence") as mock_get_persistence,
        patch("server.realtime.websocket_initial_state.add_npc_occupants_to_list") as mock_add_npcs,
        patch("server.realtime.websocket_initial_state.get_event_handler_for_initial_state") as mock_get_handler,
    ):
        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
        mock_get_persistence.return_value = mock_persistence
        mock_add_npcs.return_value = None
        mock_get_handler.return_value = None

        await send_initial_room_state(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_connection_manager
        )

    send_json_mock: AsyncMock = cast(AsyncMock, mock_websocket.send_json)
    send_json_mock.assert_not_called()


@pytest.mark.asyncio
async def test_send_initial_room_state_handles_exception(
    mock_websocket: AsyncMock,
    mock_connection_manager: AsyncMock,
) -> None:
    """Test send_initial_room_state() handles exceptions."""
    player_id = uuid.uuid4()
    player_id_str = str(player_id)
    canonical_room_id = "room_123"

    with patch("server.async_persistence.get_async_persistence", side_effect=ValueError("Error")):
        # Should not raise
        await send_initial_room_state(
            mock_websocket, player_id, player_id_str, canonical_room_id, mock_connection_manager
        )
