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
    _looks_like_player_uuid,
    broadcast_room_update,
    build_room_update_event,
    get_npc_occupants,
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
def mock_room() -> MagicMock:
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
async def test_get_player_occupants_includes_in_room_player_without_websocket(mock_connection_manager):
    """In-room players must appear in Occupants even with no live WS and no grace (look's rule)."""
    other_id = uuid.uuid4()
    mock_connection_manager.get_room_occupants.return_value = [
        {"player_name": "Ithaqua", "player_id": str(other_id)},
    ]
    mock_connection_manager.has_websocket_connection = MagicMock(return_value=False)

    with (
        patch("server.realtime.occupant_display.is_player_in_grace_period", return_value=False),
        patch("server.realtime.occupant_display.is_player_in_login_grace_period", return_value=False),
    ):
        result = await get_player_occupants(mock_connection_manager, "room_123")

    assert "Ithaqua" in result


@pytest.mark.asyncio
async def test_get_player_occupants_adds_grace_badges(mock_connection_manager):
    """Occupants panel uses the same grace badges as look."""
    other_id = uuid.uuid4()
    mock_connection_manager.get_room_occupants.return_value = [
        {"player_name": "Ithaqua", "player_id": str(other_id)},
    ]
    mock_connection_manager.has_websocket_connection = MagicMock(return_value=False)

    with (
        patch("server.realtime.occupant_display.is_player_in_grace_period", return_value=True),
        patch("server.realtime.occupant_display.is_player_in_login_grace_period", return_value=True),
    ):
        result = await get_player_occupants(mock_connection_manager, "room_123")

    assert result == ["Ithaqua (linkdead) (warded)"]


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
async def test_get_npc_occupants_success(mock_room: MagicMock):
    """get_npc_occupants() returns names for alive NPCs the room lists."""
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

        result = await get_npc_occupants(mock_room, room_id)

        assert "NPC1" in result
        assert "NPC2" in result


@pytest.mark.asyncio
async def test_get_npc_occupants_filters_dead(mock_room: MagicMock):
    """get_npc_occupants() filters dead NPCs using the single liveness rule."""
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

        result = await get_npc_occupants(mock_room, room_id)

        assert "AliveNPC" in result
        assert "DeadNPC" not in result


@pytest.mark.asyncio
async def test_get_npc_occupants_ignores_npc_not_tracked_by_lifecycle_manager(mock_room: MagicMock):
    """An id the room lists but the lifecycle manager doesn't track is simply skipped."""
    room_id = "room_123"
    mock_room.get_npcs = MagicMock(return_value=["npc_untracked"])

    with patch("server.realtime.websocket_room_updates.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        # room lists an id the manager has never heard of
        mock_service.lifecycle_manager = MagicMock(active_npcs={})
        mock_get_service.return_value = mock_service

        result = await get_npc_occupants(mock_room, room_id)

        assert result == []


@pytest.mark.asyncio
async def test_get_npc_occupants_no_service(mock_room: MagicMock):
    """get_npc_occupants() fails closed (empty list) when no NPC service is available."""
    room_id = "room_123"
    mock_room.get_npcs.return_value = ["npc_1"]

    with patch("server.realtime.websocket_room_updates.get_npc_instance_service", return_value=None):
        result = await get_npc_occupants(mock_room, room_id)
        assert result == []


@pytest.mark.asyncio
async def test_get_npc_occupants_fails_closed_on_lookup_error(mock_room: MagicMock):
    """
    A lifecycle-manager lookup error fails closed (empty list), not the old degrade-to-unfiltered.

    #757 PR3: the previous two-function split had one path that, on a filtering error, fell back
    to `filtered_npc_ids = room_npc_ids` — showing every room-listed NPC unfiltered, dead ones
    included. That branch was untested and is gone; the merged resolver logs and returns no NPCs
    instead, matching what "fail closed" should mean for an occupant list players see.
    """
    room_id = "room_123"
    mock_room.get_npcs = MagicMock(return_value=["npc_1"])

    with patch("server.realtime.websocket_room_updates.get_npc_instance_service", side_effect=AttributeError("Error")):
        result = await get_npc_occupants(mock_room, room_id)

        assert result == []


def test_looks_like_player_uuid_true_for_real_uuid_string():
    """A real player_id (UUID string) is recognized as such."""
    assert _looks_like_player_uuid(TEST_PLAYER_ID_STR) is True


def test_looks_like_player_uuid_false_for_room_id_string():
    """
    A room_id passed in the player_id slot (room-only refresh) is not mistaken for a player_id.

    This is the shape callers rely on: EventBus-triggered room-only refreshes pass room_id where
    player_id normally goes, and this predicate is how downstream code tells the two apart.
    """
    assert _looks_like_player_uuid("room_123") is False


def test_looks_like_player_uuid_false_for_non_string():
    """A non-string value (e.g. None) is never treated as a player_id."""
    assert _looks_like_player_uuid(None) is False


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
    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id.return_value = mock_room
    mock_connection_manager.async_persistence = mock_persistence

    with (
        patch("server.realtime.websocket_room_updates.get_player_occupants") as mock_get_players,
        patch("server.realtime.websocket_room_updates.get_npc_occupants") as mock_get_npcs,
        patch("server.realtime.websocket_room_updates.build_room_update_event") as mock_build_event,
        patch("server.realtime.websocket_room_updates.get_npc_instance_service") as mock_get_npc_service,
    ):
        # Mock NPC service to avoid initialization errors
        mock_npc_service = MagicMock()
        mock_get_npc_service.return_value = mock_npc_service

        mock_get_players.return_value = ["Player1"]
        mock_get_npcs.return_value = ["NPC1"]
        mock_build_event.return_value = {"event_type": "room_update", "data": {}}

        await broadcast_room_update(player_id, room_id, mock_connection_manager)

        # broadcast_room_update sends room_update then room_occupants
        assert mock_connection_manager.broadcast_to_room.call_count == 2


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
    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id.return_value = mock_room
    mock_connection_manager.async_persistence = mock_persistence

    # Create a proper mock FastAPI app structure before patching
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_container = MagicMock()
    mock_container.connection_manager = mock_connection_manager
    mock_app.state.container = mock_container

    with (
        patch("server.main.app", mock_app),
        patch("server.realtime.websocket_room_updates.get_player_occupants") as mock_get_players,
        patch("server.realtime.websocket_room_updates.get_npc_occupants") as mock_get_npcs,
        patch("server.realtime.websocket_room_updates.build_room_update_event") as mock_build_event,
        patch("server.realtime.websocket_room_updates.get_npc_instance_service") as mock_get_npc_service,
    ):
        # Mock NPC service to avoid initialization errors
        mock_npc_service = MagicMock()
        mock_get_npc_service.return_value = mock_npc_service

        mock_get_players.return_value = []
        mock_get_npcs.return_value = []
        mock_build_event.return_value = {"event_type": "room_update", "data": {}}

        await broadcast_room_update(player_id, room_id)

        # broadcast_room_update sends room_update then room_occupants
        assert mock_connection_manager.broadcast_to_room.call_count == 2


@pytest.mark.asyncio
async def test_broadcast_room_update_room_not_found(mock_connection_manager):
    """Test broadcast_room_update() sends room_occupants only (empty) when room not found."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id.return_value = None
    mock_connection_manager.async_persistence = mock_persistence

    async def resolve_none_room(*_args, **_kwargs):
        return (None, room_id, room_id)

    with patch(
        "server.realtime.websocket_room_updates._resolve_room_with_fallback",
        side_effect=resolve_none_room,
    ):
        # get_npc_occupants() is never called when room resolution fails — no room object means
        # no room.get_npcs() to query, so npc_occupants short-circuits to [] deterministically.
        await broadcast_room_update(player_id, room_id, mock_connection_manager)

        # When room not found, we still send one room_occupants event with empty data (no room_update)
        mock_connection_manager.broadcast_to_room.assert_called_once()
        call_args = mock_connection_manager.broadcast_to_room.call_args[0]
        assert call_args[0] == room_id
        event = call_args[1]
        assert event["event_type"] == "room_occupants"
        assert event["data"]["players"] == []
        assert event["data"]["npcs"] == []
        assert event["data"]["occupants"] == []
        assert event["data"]["count"] == 0


@pytest.mark.asyncio
async def test_broadcast_room_update_no_persistence(mock_connection_manager):
    """Test broadcast_room_update() does nothing when persistence unavailable."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    mock_connection_manager.async_persistence = None
    await broadcast_room_update(player_id, room_id, mock_connection_manager)

    mock_connection_manager.broadcast_to_room.assert_not_called()


@pytest.mark.asyncio
async def test_broadcast_room_update_propagates_subscription_error(mock_connection_manager: MagicMock):
    """
    A genuine failure in update_player_room_subscription is no longer silently swallowed.

    #757 PR3: the old guard wrapped both the UUID-shape check *and* the real subscription work
    in one `try/except (ValueError, TypeError, AttributeError): pass`, so a real bug in the
    subscription update looked identical to "player_id just wasn't a UUID". Now the shape check
    is a separate predicate and the real work's exceptions reach broadcast_room_update's own
    outer handler — visible as an error log and an early return, not silence.
    """
    player_id = TEST_PLAYER_ID_STR  # a real UUID, so the subscription-update path is taken
    room_id = "room_123"

    mock_room = MagicMock()
    mock_room.to_dict.return_value = {"id": room_id, "name": "Test Room"}
    mock_room.get_npcs.return_value = []

    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id.return_value = mock_room
    mock_connection_manager.async_persistence = mock_persistence

    with (
        patch("server.realtime.websocket_room_updates.get_player_occupants", return_value=[]),
        patch("server.realtime.websocket_room_updates.get_npc_occupants", return_value=[]),
        patch("server.realtime.websocket_room_updates.build_room_update_event", return_value={}),
        patch(
            "server.realtime.websocket_room_updates.update_player_room_subscription",
            side_effect=AttributeError("subscription state corrupted"),
        ),
    ):
        await broadcast_room_update(player_id, room_id, mock_connection_manager)

    # The outer except caught it and returned early: neither broadcast happened.
    mock_connection_manager.broadcast_to_room.assert_not_called()


@pytest.mark.asyncio
async def test_broadcast_room_update_handles_exception(mock_connection_manager):
    """Test broadcast_room_update() does not raise when persistence is unavailable."""
    player_id = TEST_PLAYER_ID_STR
    room_id = "room_123"

    mock_connection_manager.async_persistence = None
    # Should not raise; exits early when persistence unavailable
    await broadcast_room_update(player_id, room_id, mock_connection_manager)
