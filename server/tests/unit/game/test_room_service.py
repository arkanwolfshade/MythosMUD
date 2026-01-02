"""
Unit tests for room service.

Tests the RoomService class for room-related operations.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.room_service import RoomService


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    persistence.get_room_by_id = MagicMock()
    persistence.async_list_rooms = AsyncMock(return_value=[])
    return persistence


@pytest.fixture
def mock_room_cache():
    """Create a mock room cache service."""
    cache = MagicMock()
    cache.get_room = AsyncMock()
    return cache


@pytest.fixture
def room_service(mock_persistence):  # pylint: disable=redefined-outer-name
    """Create a RoomService instance."""
    return RoomService(mock_persistence)


@pytest.fixture
def room_service_with_cache(mock_persistence, mock_room_cache):  # pylint: disable=redefined-outer-name
    """Create a RoomService instance with cache."""
    return RoomService(mock_persistence, room_cache_service=mock_room_cache)


@pytest.fixture
def sample_room_dict():
    """Create a sample room dictionary."""
    return {
        "id": "room_001",
        "name": "Test Room",
        "description": "A test room",
        "exits": {"north": "room_002", "south": "room_003"},
    }


@pytest.mark.asyncio
async def test_room_service_init(room_service):  # pylint: disable=redefined-outer-name
    """Test RoomService initialization."""
    assert room_service.persistence is not None
    assert room_service.room_cache is None
    # pylint: disable=protected-access
    # Accessing protected member for test verification of internal state
    assert room_service._environment_state["daypart"] == "day"
    assert room_service._environment_state["is_daytime"] is True


@pytest.mark.asyncio
async def test_room_service_init_with_cache(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test RoomService initialization with cache."""
    assert room_service_with_cache.room_cache is not None


@pytest.mark.asyncio
async def test_get_room_with_cache(room_service_with_cache, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test get_room() uses cache when available."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=sample_room_dict)
    result = await room_service_with_cache.get_room("room_001")
    assert result == sample_room_dict
    room_service_with_cache.room_cache.get_room.assert_awaited_once_with("room_001")


@pytest.mark.asyncio
async def test_get_room_cache_not_found(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test get_room() returns None when room not in cache."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=None)
    result = await room_service_with_cache.get_room("room_001")
    assert result is None


@pytest.mark.asyncio
async def test_get_room_without_cache(room_service, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test get_room() falls back to persistence when cache unavailable."""
    mock_room = MagicMock()
    mock_room.name = "Test Room"
    mock_room.to_dict = MagicMock(return_value=sample_room_dict)
    room_service.persistence.get_room_by_id = MagicMock(return_value=mock_room)
    result = await room_service.get_room("room_001")
    assert result == sample_room_dict
    room_service.persistence.get_room_by_id.assert_called_once_with("room_001")


@pytest.mark.asyncio
async def test_get_room_persistence_not_found(room_service):  # pylint: disable=redefined-outer-name
    """Test get_room() returns None when room not found in persistence."""
    room_service.persistence.get_room_by_id = MagicMock(return_value=None)
    result = await room_service.get_room("room_001")
    assert result is None


@pytest.mark.asyncio
async def test_get_room_persistence_returns_dict(room_service, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test get_room() handles dict from persistence."""
    # When persistence returns a dict, we wrap it to simulate a Room object
    # The implementation expects a Room object with to_dict() method
    mock_room = MagicMock()
    mock_room.to_dict = MagicMock(return_value=sample_room_dict)
    room_service.persistence.get_room_by_id = MagicMock(return_value=mock_room)
    result = await room_service.get_room("room_001")
    assert result == sample_room_dict


def test_get_room_by_name(room_service):  # pylint: disable=redefined-outer-name
    """Test get_room_by_name() returns None (not implemented)."""
    result = room_service.get_room_by_name("Test Room")
    assert result is None


def test_list_rooms_in_zone(room_service):  # pylint: disable=redefined-outer-name
    """Test list_rooms_in_zone() returns empty list (not implemented)."""
    result = room_service.list_rooms_in_zone("zone_001")
    assert result == []


@pytest.mark.asyncio
async def test_get_adjacent_rooms_success(room_service_with_cache, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test get_adjacent_rooms() returns adjacent rooms."""
    room_002 = {"id": "room_002", "name": "Room 2"}
    room_003 = {"id": "room_003", "name": "Room 3"}
    room_service_with_cache.room_cache.get_room = AsyncMock(side_effect=[sample_room_dict, room_002, room_003])
    result = await room_service_with_cache.get_adjacent_rooms("room_001")
    assert len(result) == 2
    assert result[0]["direction"] == "north"
    assert result[0]["room_id"] == "room_002"
    assert result[1]["direction"] == "south"
    assert result[1]["room_id"] == "room_003"


@pytest.mark.asyncio
async def test_get_adjacent_rooms_source_not_found(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test get_adjacent_rooms() returns empty list when source room not found."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=None)
    result = await room_service_with_cache.get_adjacent_rooms("room_001")
    assert result == []


@pytest.mark.asyncio
async def test_get_adjacent_rooms_no_exits(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test get_adjacent_rooms() handles room with no exits."""
    room_no_exits = {"id": "room_001", "name": "Test Room", "exits": {}}
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=room_no_exits)
    result = await room_service_with_cache.get_adjacent_rooms("room_001")
    assert result == []


@pytest.mark.asyncio
async def test_get_adjacent_rooms_null_exit(room_service_with_cache, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test get_adjacent_rooms() skips null exits."""
    room_with_null = {
        **sample_room_dict,
        "exits": {"north": "room_002", "south": None, "east": "room_004"},
    }
    room_002 = {"id": "room_002", "name": "Room 2"}
    room_004 = {"id": "room_004", "name": "Room 4"}
    room_service_with_cache.room_cache.get_room = AsyncMock(side_effect=[room_with_null, room_002, room_004])
    result = await room_service_with_cache.get_adjacent_rooms("room_001")
    # Should only return 2 rooms (north and east, skipping null south)
    assert len(result) == 2
    assert "north" in [r["direction"] for r in result]
    assert "east" in [r["direction"] for r in result]


@pytest.mark.asyncio
async def test_get_adjacent_rooms_target_not_found(room_service_with_cache, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test get_adjacent_rooms() handles target room not found."""

    # get_room is called for source room, then for each exit (north and south)
    # First call returns source room, subsequent calls return None for targets
    def room_getter(room_id):
        if room_id == "room_001":
            return sample_room_dict
        return None

    room_service_with_cache.room_cache.get_room = AsyncMock(side_effect=room_getter)
    result = await room_service_with_cache.get_adjacent_rooms("room_001")
    # Should return empty list when target rooms not found
    assert result == []


@pytest.mark.asyncio
async def test_get_local_chat_scope(room_service_with_cache, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test get_local_chat_scope() returns current room and adjacent rooms."""
    room_002 = {"id": "room_002", "name": "Room 2"}
    room_003 = {"id": "room_003", "name": "Room 3"}

    # get_room is called: once for source in get_local_chat_scope,
    # then once for source in get_adjacent_rooms, then for each exit
    def room_getter(room_id):
        if room_id == "room_001":
            return sample_room_dict
        elif room_id == "room_002":
            return room_002
        elif room_id == "room_003":
            return room_003
        return None

    room_service_with_cache.room_cache.get_room = AsyncMock(side_effect=room_getter)
    result = await room_service_with_cache.get_local_chat_scope("room_001")
    assert "room_001" in result
    assert "room_002" in result
    assert "room_003" in result
    assert len(result) >= 3


@pytest.mark.asyncio
async def test_get_local_chat_scope_source_not_found(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test get_local_chat_scope() returns empty list when source room not found."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=None)
    result = await room_service_with_cache.get_local_chat_scope("room_001")
    assert result == []


@pytest.mark.asyncio
async def test_validate_room_exists_with_cache(room_service_with_cache, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test validate_room_exists() uses cache."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=sample_room_dict)
    result = await room_service_with_cache.validate_room_exists("room_001")
    assert result is True


@pytest.mark.asyncio
async def test_validate_room_exists_cache_not_found(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test validate_room_exists() returns False when room not in cache."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=None)
    result = await room_service_with_cache.validate_room_exists("room_001")
    assert result is False


@pytest.mark.asyncio
async def test_validate_room_exists_without_cache(room_service, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test validate_room_exists() falls back to persistence."""
    mock_room = MagicMock()
    mock_room.to_dict = MagicMock(return_value=sample_room_dict)
    room_service.persistence.get_room_by_id = MagicMock(return_value=mock_room)
    result = await room_service.validate_room_exists("room_001")
    assert result is True


@pytest.mark.asyncio
async def test_validate_exit_exists_success(room_service_with_cache, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test validate_exit_exists() returns True for valid exit."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=sample_room_dict)
    result = await room_service_with_cache.validate_exit_exists("room_001", "room_002")
    assert result is True


@pytest.mark.asyncio
async def test_validate_exit_exists_invalid(room_service_with_cache, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test validate_exit_exists() returns False for invalid exit."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=sample_room_dict)
    result = await room_service_with_cache.validate_exit_exists("room_001", "room_999")
    assert result is False


@pytest.mark.asyncio
async def test_validate_exit_exists_from_room_not_found(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test validate_exit_exists() returns False when from_room not found."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=None)
    result = await room_service_with_cache.validate_exit_exists("room_001", "room_002")
    assert result is False


@pytest.mark.asyncio
async def test_validate_exit_exists_no_exits(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test validate_exit_exists() returns False when room has no exits."""
    room_no_exits = {"id": "room_001", "name": "Test Room", "exits": {}}
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=room_no_exits)
    result = await room_service_with_cache.validate_exit_exists("room_001", "room_002")
    assert result is False


@pytest.mark.asyncio
async def test_get_room_occupants_with_cache_room_object(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test get_room_occupants() handles Room object with get_players/get_npcs."""
    mock_room = MagicMock()
    mock_room.get_players = MagicMock(return_value=["player1", "player2"])
    mock_room.get_npcs = MagicMock(return_value=["npc1"])
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=mock_room)
    result = await room_service_with_cache.get_room_occupants("room_001")
    assert len(result) == 3
    assert "player1" in result
    assert "player2" in result
    assert "npc1" in result


@pytest.mark.asyncio
async def test_get_room_occupants_with_cache_dict(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test get_room_occupants() handles room dict."""
    room_dict = {"id": "room_001", "occupants": ["player1", "player2"]}
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=room_dict)
    result = await room_service_with_cache.get_room_occupants("room_001")
    assert result == ["player1", "player2"]


@pytest.mark.asyncio
async def test_get_room_occupants_cache_not_found(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test get_room_occupants() returns empty list when room not found."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=None)
    result = await room_service_with_cache.get_room_occupants("room_001")
    assert result == []


@pytest.mark.asyncio
async def test_get_room_occupants_without_cache(room_service):  # pylint: disable=redefined-outer-name
    """Test get_room_occupants() falls back to persistence."""
    mock_room = MagicMock()
    mock_room.get_players = MagicMock(return_value=["player1"])
    mock_room.get_npcs = MagicMock(return_value=["npc1"])
    room_service.persistence.get_room_by_id = MagicMock(return_value=mock_room)
    result = await room_service.get_room_occupants("room_001")
    assert len(result) == 2
    assert "player1" in result
    assert "npc1" in result


@pytest.mark.asyncio
async def test_validate_player_in_room_with_cache_true(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test validate_player_in_room() returns True when player in room."""
    mock_room = MagicMock()
    mock_room.has_player = MagicMock(return_value=True)
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=mock_room)
    result = await room_service_with_cache.validate_player_in_room("player1", "room_001")
    assert result is True


@pytest.mark.asyncio
async def test_validate_player_in_room_with_cache_false(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test validate_player_in_room() returns False when player not in room."""
    mock_room = MagicMock()
    mock_room.has_player = MagicMock(return_value=False)
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=mock_room)
    result = await room_service_with_cache.validate_player_in_room("player1", "room_001")
    assert result is False


@pytest.mark.asyncio
async def test_validate_player_in_room_cache_dict(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test validate_player_in_room() handles room dict."""
    room_dict = {"id": "room_001", "occupants": ["player1", "player2"]}
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=room_dict)
    result = await room_service_with_cache.validate_player_in_room("player1", "room_001")
    assert result is True
    result = await room_service_with_cache.validate_player_in_room("player3", "room_001")
    assert result is False


@pytest.mark.asyncio
async def test_validate_player_in_room_cache_not_found(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test validate_player_in_room() returns False when room not found."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=None)
    result = await room_service_with_cache.validate_player_in_room("player1", "room_001")
    assert result is False


@pytest.mark.asyncio
async def test_get_room_exits_success(room_service_with_cache, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test get_room_exits() returns exits dictionary."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=sample_room_dict)
    result = await room_service_with_cache.get_room_exits("room_001")
    assert result == {"north": "room_002", "south": "room_003"}


@pytest.mark.asyncio
async def test_get_room_exits_room_not_found(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test get_room_exits() returns empty dict when room not found."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=None)
    result = await room_service_with_cache.get_room_exits("room_001")
    assert result == {}


@pytest.mark.asyncio
async def test_get_room_exits_no_exits(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test get_room_exits() returns empty dict when room has no exits."""
    room_no_exits = {"id": "room_001", "name": "Test Room"}
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=room_no_exits)
    result = await room_service_with_cache.get_room_exits("room_001")
    assert result == {}


@pytest.mark.asyncio
async def test_list_rooms_with_plane_zone(room_service):  # pylint: disable=redefined-outer-name
    """Test list_rooms() filters by plane and zone."""
    mock_room1 = MagicMock()
    mock_room1.to_dict = MagicMock(return_value={"id": "room_001", "plane": "earth", "zone": "arkhamcity"})
    mock_room2 = MagicMock()
    mock_room2.to_dict = MagicMock(return_value={"id": "room_002", "plane": "earth", "zone": "innsmouth"})
    room_service.persistence.async_list_rooms = AsyncMock(return_value=[mock_room1, mock_room2])
    result = await room_service.list_rooms("earth", "arkhamcity")
    assert len(result) == 1
    assert result[0]["id"] == "room_001"


@pytest.mark.asyncio
async def test_list_rooms_with_sub_zone(room_service):  # pylint: disable=redefined-outer-name
    """Test list_rooms() filters by sub_zone."""
    mock_room1 = MagicMock()
    mock_room1.to_dict = MagicMock(
        return_value={"id": "room_001", "plane": "earth", "zone": "arkhamcity", "sub_zone": "northside"}
    )
    mock_room2 = MagicMock()
    mock_room2.to_dict = MagicMock(
        return_value={"id": "room_002", "plane": "earth", "zone": "arkhamcity", "sub_zone": "downtown"}
    )
    room_service.persistence.async_list_rooms = AsyncMock(return_value=[mock_room1, mock_room2])
    result = await room_service.list_rooms("earth", "arkhamcity", sub_zone="northside")
    assert len(result) == 1
    assert result[0]["id"] == "room_001"


@pytest.mark.asyncio
async def test_list_rooms_exclude_exits(room_service):  # pylint: disable=redefined-outer-name
    """Test list_rooms() excludes exits when include_exits=False."""
    mock_room = MagicMock()
    mock_room.to_dict = MagicMock(
        return_value={"id": "room_001", "plane": "earth", "zone": "arkhamcity", "exits": {"north": "room_002"}}
    )
    room_service.persistence.async_list_rooms = AsyncMock(return_value=[mock_room])
    result = await room_service.list_rooms("earth", "arkhamcity", include_exits=False)
    assert len(result) == 1
    assert "exits" not in result[0]


@pytest.mark.asyncio
async def test_get_room_info_success(room_service_with_cache, sample_room_dict):  # pylint: disable=redefined-outer-name
    """Test get_room_info() returns comprehensive room information."""
    mock_room = MagicMock()
    mock_room.get_players = MagicMock(return_value=["player1"])
    mock_room.get_npcs = MagicMock(return_value=["npc1"])
    room_service_with_cache.room_cache.get_room = AsyncMock(
        side_effect=[sample_room_dict, sample_room_dict, sample_room_dict, sample_room_dict]
    )
    # Mock get_room_occupants and get_room_exits
    room_service_with_cache.get_room_occupants = AsyncMock(return_value=["player1", "npc1"])
    room_service_with_cache.get_room_exits = AsyncMock(return_value={"north": "room_002"})
    room_service_with_cache.get_adjacent_rooms = AsyncMock(return_value=[{"direction": "north", "room_id": "room_002"}])
    result = await room_service_with_cache.get_room_info("room_001")
    assert result is not None
    assert "occupants" in result
    assert "exits" in result
    assert "adjacent_rooms" in result
    assert result["occupant_count"] == 2


@pytest.mark.asyncio
async def test_get_room_info_not_found(room_service_with_cache):  # pylint: disable=redefined-outer-name
    """Test get_room_info() returns None when room not found."""
    room_service_with_cache.room_cache.get_room = AsyncMock(return_value=None)
    result = await room_service_with_cache.get_room_info("room_001")
    assert result is None


def test_update_environment_state(room_service):  # pylint: disable=redefined-outer-name
    """Test update_environment_state() updates environment state."""
    room_service.update_environment_state(daypart="night", is_daytime=False, active_holidays=["halloween"])
    state = room_service.get_environment_state()
    assert state["daypart"] == "night"
    assert state["is_daytime"] is False
    assert "halloween" in state["active_holidays"]


def test_get_environment_state(room_service):  # pylint: disable=redefined-outer-name
    """Test get_environment_state() returns current environment state."""
    state = room_service.get_environment_state()
    assert "daypart" in state
    assert "is_daytime" in state
    assert "active_holidays" in state


def test_describe_lighting_day(room_service):  # pylint: disable=redefined-outer-name
    """Test describe_lighting() returns description for day."""
    room_service.update_environment_state(daypart="day", is_daytime=True, active_holidays=[])
    description = room_service.describe_lighting()
    assert "sunlight" in description.lower() or "day" in description.lower()


def test_describe_lighting_night(room_service):  # pylint: disable=redefined-outer-name
    """Test describe_lighting() returns description for night."""
    room_service.update_environment_state(daypart="night", is_daytime=False, active_holidays=[])
    description = room_service.describe_lighting()
    assert "night" in description.lower() or "gaslights" in description.lower()


def test_describe_lighting_unknown_daypart(room_service):  # pylint: disable=redefined-outer-name
    """Test describe_lighting() returns default for unknown daypart."""
    room_service.update_environment_state(daypart="unknown", is_daytime=True, active_holidays=[])
    description = room_service.describe_lighting()
    assert "atmosphere" in description.lower() or "shifts" in description.lower()


def test_search_rooms_by_name_short_term(room_service):  # pylint: disable=redefined-outer-name
    """Test search_rooms_by_name() returns empty list for short search term."""
    result = room_service.search_rooms_by_name("a")
    assert result == []


def test_search_rooms_by_name_empty_term(room_service):  # pylint: disable=redefined-outer-name
    """Test search_rooms_by_name() returns empty list for empty term."""
    result = room_service.search_rooms_by_name("")
    assert result == []


def test_search_rooms_by_name_not_implemented(room_service):  # pylint: disable=redefined-outer-name
    """Test search_rooms_by_name() returns empty list (not implemented)."""
    result = room_service.search_rooms_by_name("test room")
    assert result == []


def test_get_rooms_in_zone(room_service):  # pylint: disable=redefined-outer-name
    """Test get_rooms_in_zone() returns empty list (not implemented)."""
    result = room_service.get_rooms_in_zone("zone_001")
    assert result == []
