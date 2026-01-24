"""
Unit tests for WebSocket room updates.

Tests the websocket_room_updates module functions.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
from server.realtime.websocket_room_updates import (
    broadcast_room_update,
    build_room_update_event,
    get_npc_occupants_fallback,
    get_npc_occupants_from_lifecycle_manager,
    get_player_occupants,
    update_player_room_subscription,
)

# Test UUID constant for player IDs
TEST_PLAYER_ID = uuid.UUID("12345678-1234-5678-1234-567812345678")
TEST_PLAYER_ID_STR = str(TEST_PLAYER_ID)


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = AsyncMock()
    manager.get_room_occupants = AsyncMock(return_value=[])
    manager.convert_room_players_uuids_to_names = AsyncMock(side_effect=lambda x: x)
    manager.broadcast_to_room = AsyncMock()
    manager.subscribe_to_room = AsyncMock()
    manager.unsubscribe_from_room = AsyncMock()
    manager.get_player = AsyncMock()
    return manager


@pytest.fixture
def mock_room():
    """Create a mock room."""
    room = MagicMock()
    room.to_dict.return_value = {"id": "room_123", "name": "Test Room"}
    room.get_players.return_value = []
    room.get_objects.return_value = []
    room.get_npcs.return_value = []
    room.get_occupant_count.return_value = 0
    return room


@pytest.mark.asyncio
async def test_get_player_occupants_success(mock_connection_manager):
    """Test get_player_occupants() extracts player names."""
    room_id = "room_123"
    mock_connection_manager.get_room_occupants.return_value = [
        {"player_name": "Player1"},
        {"name": "Player2"},
    ]

    result = await get_player_occupants(mock_connection_manager, room_id)

    assert "Player1" in result
    assert "Player2" in result


@pytest.mark.asyncio
async def test_get_player_occupants_empty(mock_connection_manager):
    """Test get_player_occupants() returns empty list when no occupants."""
    room_id = "room_123"
    mock_connection_manager.get_room_occupants.return_value = []

    result = await get_player_occupants(mock_connection_manager, room_id)

    assert result == []


@pytest.mark.asyncio
async def test_get_player_occupants_handles_exception(mock_connection_manager):
    """Test get_player_occupants() handles exceptions."""
    room_id = "room_123"
    mock_connection_manager.get_room_occupants.side_effect = AttributeError("Error")

    result = await get_player_occupants(mock_connection_manager, room_id)

    assert result == []


@pytest.mark.asyncio
async def test_get_npc_occupants_from_lifecycle_manager_success():
    """Test get_npc_occupants_from_lifecycle_manager() returns NPC names."""
    room_id = "room_123"

    mock_npc1 = MagicMock()
    mock_npc1.name = "NPC1"
    mock_npc1.is_alive = True
    mock_npc1.current_room_id = "room_123"
    mock_npc1.current_room = None

    mock_npc2 = MagicMock()
    mock_npc2.name = "NPC2"
    mock_npc2.is_alive = True
    mock_npc2.current_room_id = "room_123"
    mock_npc2.current_room = None

    with (
        patch("server.realtime.websocket_room_updates.get_npc_instance_service") as mock_get_service,
        patch("server.realtime.websocket_room_updates.get_npc_name_from_instance") as mock_get_name,
    ):
        mock_service = MagicMock()
        mock_service.lifecycle_manager.active_npcs = {"npc_1": mock_npc1, "npc_2": mock_npc2}
        mock_get_service.return_value = mock_service
        mock_get_name.side_effect = {"npc_1": "NPC1", "npc_2": "NPC2"}.get

        result = await get_npc_occupants_from_lifecycle_manager(room_id)

        assert "NPC1" in result
        assert "NPC2" in result


@pytest.mark.asyncio
async def test_get_npc_occupants_from_lifecycle_manager_filters_dead():
    """Test get_npc_occupants_from_lifecycle_manager() filters dead NPCs."""
    room_id = "room_123"

    mock_npc_alive = MagicMock()
    mock_npc_alive.name = "AliveNPC"
    mock_npc_alive.is_alive = True
    mock_npc_alive.current_room_id = "room_123"
    mock_npc_alive.current_room = None

    mock_npc_dead = MagicMock()
    mock_npc_dead.name = "DeadNPC"
    mock_npc_dead.is_alive = False
    mock_npc_dead.current_room_id = "room_123"
    mock_npc_dead.current_room = None

    with (
        patch("server.realtime.websocket_room_updates.get_npc_instance_service") as mock_get_service,
        patch("server.realtime.websocket_room_updates.get_npc_name_from_instance") as mock_get_name,
    ):
        mock_service = MagicMock()
        mock_service.lifecycle_manager.active_npcs = {"npc_alive": mock_npc_alive, "npc_dead": mock_npc_dead}
        mock_get_service.return_value = mock_service
        mock_get_name.side_effect = {"npc_alive": "AliveNPC"}.get  # Dead NPC returns None

        result = await get_npc_occupants_from_lifecycle_manager(room_id)

        assert "AliveNPC" in result
        assert "DeadNPC" not in result


@pytest.mark.asyncio
async def test_get_npc_occupants_from_lifecycle_manager_wrong_room():
    """Test get_npc_occupants_from_lifecycle_manager() filters by room."""
    room_id = "room_123"

    mock_npc = MagicMock()
    mock_npc.name = "NPC1"
    mock_npc.is_alive = True
    mock_npc.current_room_id = "room_456"  # Different room

    with patch("server.realtime.websocket_room_updates.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_service.lifecycle_manager.active_npcs = {"npc_1": mock_npc}
        mock_get_service.return_value = mock_service

        result = await get_npc_occupants_from_lifecycle_manager(room_id)

        assert "NPC1" not in result


@pytest.mark.asyncio
async def test_get_npc_occupants_from_lifecycle_manager_no_service():
    """Test get_npc_occupants_from_lifecycle_manager() returns empty when no service."""
    room_id = "room_123"

    with patch("server.realtime.websocket_room_updates.get_npc_instance_service", return_value=None):
        result = await get_npc_occupants_from_lifecycle_manager(room_id)
        assert not result


@pytest.mark.asyncio
async def test_get_npc_occupants_from_lifecycle_manager_handles_exception():
    """Test get_npc_occupants_from_lifecycle_manager() handles exceptions."""
    room_id = "room_123"

    with patch("server.realtime.websocket_room_updates.get_npc_instance_service", side_effect=AttributeError("Error")):
        with pytest.raises(AttributeError):
            await get_npc_occupants_from_lifecycle_manager(room_id)


@pytest.mark.asyncio
async def test_get_npc_occupants_fallback_success(mock_room):
    """Test get_npc_occupants_fallback() returns NPC names."""
    room_id = "room_123"
    mock_room.get_npcs.return_value = ["npc_1", "npc_2"]

    mock_npc1 = MagicMock()
    mock_npc1.name = "NPC1"
    mock_npc1.is_alive = True

    mock_npc2 = MagicMock()
    mock_npc2.name = "NPC2"
    mock_npc2.is_alive = True

    with (
        patch("server.realtime.websocket_room_updates.get_npc_instance_service") as mock_get_service,
        patch("server.realtime.websocket_room_updates.get_npc_name_from_instance") as mock_get_name,
    ):
        mock_service = MagicMock()
        mock_service.lifecycle_manager.active_npcs = {"npc_1": mock_npc1, "npc_2": mock_npc2}
        mock_get_service.return_value = mock_service
        mock_get_name.side_effect = {"npc_1": "NPC1", "npc_2": "NPC2"}.get

        result = await get_npc_occupants_fallback(mock_room, room_id)

        assert "NPC1" in result
        assert "NPC2" in result


@pytest.mark.asyncio
async def test_get_npc_occupants_fallback_filters_dead(mock_room):
    """Test get_npc_occupants_fallback() filters dead NPCs."""
    room_id = "room_123"
    mock_room.get_npcs.return_value = ["npc_alive", "npc_dead"]

    mock_npc_alive = MagicMock()
    mock_npc_alive.name = "AliveNPC"
    mock_npc_alive.is_alive = True

    mock_npc_dead = MagicMock()
    mock_npc_dead.name = "DeadNPC"
    mock_npc_dead.is_alive = False

    with (
        patch("server.realtime.websocket_room_updates.get_npc_instance_service") as mock_get_service,
        patch("server.realtime.websocket_room_updates.get_npc_name_from_instance") as mock_get_name,
    ):
        mock_service = MagicMock()
        mock_service.lifecycle_manager.active_npcs = {"npc_alive": mock_npc_alive, "npc_dead": mock_npc_dead}
        mock_get_service.return_value = mock_service
        mock_get_name.side_effect = {"npc_alive": "AliveNPC"}.get  # Dead NPC returns None

        result = await get_npc_occupants_fallback(mock_room, room_id)

        assert "AliveNPC" in result
        assert "DeadNPC" not in result


@pytest.mark.asyncio
async def test_get_npc_occupants_fallback_no_service(mock_room):
    """Test get_npc_occupants_fallback() returns empty when no service."""
    room_id = "room_123"
    mock_room.get_npcs.return_value = ["npc_1"]

    with patch("server.realtime.websocket_room_updates.get_npc_instance_service", return_value=None):
        result = await get_npc_occupants_fallback(mock_room, room_id)
        assert result == []


@pytest.mark.asyncio
async def test_build_room_update_event(mock_connection_manager, mock_room):
    """Test build_room_update_event() builds room update event."""
    room_id = "room_123"
    player_id = TEST_PLAYER_ID_STR
    occupant_names = ["Player1", "NPC1"]

    mock_connection_manager.room_manager = MagicMock()
    mock_connection_manager.room_manager.list_room_drops.return_value = []

    result = await build_room_update_event(mock_room, room_id, player_id, occupant_names, mock_connection_manager)

    assert result["event_type"] == "room_update"
    assert result["data"]["room"] is not None
    assert result["data"]["occupants"] == occupant_names
    assert result["data"]["occupant_count"] == 2


@pytest.mark.asyncio
async def test_build_room_update_event_with_drops(mock_connection_manager, mock_room):
    """Test build_room_update_event() includes room drops."""
    room_id = "room_123"
    player_id = TEST_PLAYER_ID_STR
    occupant_names = ["Player1"]

    mock_drops = [{"item_id": "item_1", "name": "Test Item"}]
    mock_connection_manager.room_manager = MagicMock()
    mock_connection_manager.room_manager.list_room_drops.return_value = mock_drops

    result = await build_room_update_event(mock_room, room_id, player_id, occupant_names, mock_connection_manager)

    assert "room_drops" in result["data"]
    assert "drop_summary" in result["data"]


@pytest.mark.asyncio
async def test_update_player_room_subscription_success(mock_connection_manager):
    """Test update_player_room_subscription() updates subscription."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    mock_player = MagicMock()
    mock_player.current_room_id = "room_456"  # Different room
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

    await update_player_room_subscription(mock_connection_manager, player_id, room_id)

    mock_connection_manager.unsubscribe_from_room.assert_called_once_with(TEST_PLAYER_ID, "room_456")
    mock_connection_manager.subscribe_to_room.assert_called_once_with(TEST_PLAYER_ID, room_id)
    assert mock_player.current_room_id == room_id


@pytest.mark.asyncio
async def test_update_player_room_subscription_same_room(mock_connection_manager):
    """Test update_player_room_subscription() doesn't unsubscribe when same room."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    mock_player = MagicMock()
    mock_player.current_room_id = room_id  # Same room
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

    await update_player_room_subscription(mock_connection_manager, player_id, room_id)

    mock_connection_manager.unsubscribe_from_room.assert_not_called()
    mock_connection_manager.subscribe_to_room.assert_called_once_with(TEST_PLAYER_ID, room_id)


@pytest.mark.asyncio
async def test_update_player_room_subscription_no_player(mock_connection_manager):
    """Test update_player_room_subscription() does nothing when player not found."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    mock_connection_manager.get_player = AsyncMock(return_value=None)

    await update_player_room_subscription(mock_connection_manager, player_id, room_id)

    mock_connection_manager.subscribe_to_room.assert_not_called()


@pytest.mark.asyncio
async def test_broadcast_room_update_success(mock_connection_manager):
    """Test broadcast_room_update() successfully broadcasts update."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    mock_room = MagicMock()
    mock_room.to_dict.return_value = {"id": room_id, "name": "Test Room"}
    mock_room.get_players.return_value = []
    mock_room.get_objects.return_value = []
    mock_room.get_npcs.return_value = []

    mock_player = MagicMock()
    mock_player.current_room_id = room_id
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

    with (
        patch("server.realtime.websocket_room_updates.get_async_persistence") as mock_get_persistence,
        patch("server.realtime.websocket_room_updates.get_player_occupants") as mock_get_players,
        patch("server.realtime.websocket_room_updates.get_npc_occupants_from_lifecycle_manager") as mock_get_npcs,
        patch("server.realtime.websocket_room_updates.build_room_update_event") as mock_build_event,
        patch("server.realtime.websocket_room_updates.get_npc_instance_service") as mock_get_npc_service,
    ):
        # Mock NPC service to avoid initialization errors
        mock_npc_service = MagicMock()
        mock_get_npc_service.return_value = mock_npc_service

        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id.return_value = mock_room
        mock_get_persistence.return_value = mock_persistence

        mock_get_players.return_value = ["Player1"]
        mock_get_npcs.return_value = ["NPC1"]
        mock_build_event.return_value = {"event_type": "room_update", "data": {}}

        await broadcast_room_update(player_id, room_id, mock_connection_manager)

        mock_connection_manager.broadcast_to_room.assert_called_once()


@pytest.mark.asyncio
async def test_broadcast_room_update_no_connection_manager():
    """Test broadcast_room_update() resolves connection manager from app."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    mock_room = MagicMock()
    mock_room.to_dict.return_value = {"id": room_id, "name": "Test Room"}
    mock_room.get_players.return_value = []
    mock_room.get_objects.return_value = []
    mock_room.get_npcs.return_value = []

    mock_connection_manager = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = room_id
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)
    mock_connection_manager.get_room_occupants = AsyncMock(return_value=[])
    mock_connection_manager.broadcast_to_room = AsyncMock()
    mock_connection_manager.subscribe_to_room = AsyncMock()
    mock_connection_manager.room_manager = MagicMock()
    mock_connection_manager.room_manager.list_room_drops.return_value = []

    # Create a proper mock FastAPI app structure before patching
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_container = MagicMock()
    mock_container.connection_manager = mock_connection_manager
    mock_app.state.container = mock_container

    with (
        patch("server.main.app", mock_app),
        patch("server.realtime.websocket_room_updates.get_async_persistence") as mock_get_persistence,
        patch("server.realtime.websocket_room_updates.get_player_occupants") as mock_get_players,
        patch("server.realtime.websocket_room_updates.get_npc_occupants_fallback") as mock_get_npcs,
        patch("server.realtime.websocket_room_updates.build_room_update_event") as mock_build_event,
        patch("server.realtime.websocket_room_updates.get_npc_instance_service") as mock_get_npc_service,
    ):
        # Mock NPC service to avoid initialization errors
        mock_npc_service = MagicMock()
        mock_get_npc_service.return_value = mock_npc_service

        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id.return_value = mock_room
        mock_get_persistence.return_value = mock_persistence

        mock_get_players.return_value = []
        mock_get_npcs.return_value = []
        mock_build_event.return_value = {"event_type": "room_update", "data": {}}

        await broadcast_room_update(player_id, room_id)

        mock_connection_manager.broadcast_to_room.assert_called_once()


@pytest.mark.asyncio
async def test_broadcast_room_update_room_not_found(mock_connection_manager):
    """Test broadcast_room_update() does nothing when room not found."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    with patch("server.realtime.websocket_room_updates.get_async_persistence") as mock_get_persistence:
        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id.return_value = None
        mock_get_persistence.return_value = mock_persistence

        await broadcast_room_update(player_id, room_id, mock_connection_manager)

        mock_connection_manager.broadcast_to_room.assert_not_called()


@pytest.mark.asyncio
async def test_broadcast_room_update_no_persistence(mock_connection_manager):
    """Test broadcast_room_update() does nothing when persistence unavailable."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    with patch("server.realtime.websocket_room_updates.get_async_persistence", return_value=None):
        await broadcast_room_update(player_id, room_id, mock_connection_manager)

        mock_connection_manager.broadcast_to_room.assert_not_called()


@pytest.mark.asyncio
async def test_broadcast_room_update_fallback_npc_method(mock_connection_manager):
    """Test broadcast_room_update() uses fallback when primary NPC method fails."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    mock_room = MagicMock()
    mock_room.to_dict.return_value = {"id": room_id, "name": "Test Room"}
    mock_room.get_players.return_value = []
    mock_room.get_objects.return_value = []
    mock_room.get_npcs.return_value = []

    mock_player = MagicMock()
    mock_player.current_room_id = room_id
    mock_connection_manager.get_player = AsyncMock(return_value=mock_player)

    with (
        patch("server.realtime.websocket_room_updates.get_async_persistence") as mock_get_persistence,
        patch("server.realtime.websocket_room_updates.get_player_occupants") as mock_get_players,
        patch("server.realtime.websocket_room_updates.get_npc_occupants_from_lifecycle_manager") as mock_get_npcs,
        patch("server.realtime.websocket_room_updates.get_npc_occupants_fallback") as mock_get_npcs_fallback,
        patch("server.realtime.websocket_room_updates.build_room_update_event") as mock_build_event,
        patch("server.realtime.websocket_room_updates.get_npc_instance_service") as mock_get_npc_service,
    ):
        # Mock NPC service to avoid initialization errors
        mock_npc_service = MagicMock()
        mock_get_npc_service.return_value = mock_npc_service

        mock_persistence = MagicMock()
        mock_persistence.get_room_by_id.return_value = mock_room
        mock_get_persistence.return_value = mock_persistence

        mock_get_players.return_value = []
        mock_get_npcs.side_effect = AttributeError("Error")  # Primary method fails
        mock_get_npcs_fallback.return_value = ["NPC1"]
        mock_build_event.return_value = {"event_type": "room_update", "data": {}}

        await broadcast_room_update(player_id, room_id, mock_connection_manager)

        mock_get_npcs_fallback.assert_called_once()
        mock_connection_manager.broadcast_to_room.assert_called_once()


@pytest.mark.asyncio
async def test_broadcast_room_update_handles_exception(mock_connection_manager):
    """Test broadcast_room_update() handles exceptions."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    with patch("server.realtime.websocket_room_updates.get_async_persistence", side_effect=ValueError("Error")):
        # Should not raise
        await broadcast_room_update(player_id, room_id, mock_connection_manager)
