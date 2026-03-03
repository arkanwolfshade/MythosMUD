"""
Unit tests for async persistence layer: load_room_cache_async, query_rooms, warmup, generate_room_id, parse_exits.

Part of split from test_async_persistence.py to satisfy file-nloc limit.
"""

# pylint: disable=protected-access  # Reason: Test file - accessing protected members for unit testing
# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names must match fixture names
# pylint: disable=unused-argument  # Reason: Mock function signature must match original

import uuid
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.player import Player


@pytest.mark.asyncio
async def test_load_room_cache_async_rooms_none(async_persistence_layer):
    """Test _load_room_cache_async handles case when rooms is None."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = []
    mock_session.execute = AsyncMock(return_value=mock_result)

    async def mock_get_async_session():
        yield mock_session

    async_persistence_layer._query_rooms_with_exits_async = AsyncMock(return_value=[])
    async_persistence_layer._process_combined_rows = MagicMock(return_value=([], {}))
    original_build = async_persistence_layer._build_room_objects

    def mock_build(room_data, exits, container):
        original_build(room_data, exits, container)
        container["rooms"] = None

    async_persistence_layer._build_room_objects = MagicMock(side_effect=mock_build)

    with patch("server.async_persistence_room_loader.get_async_session", side_effect=mock_get_async_session):
        await async_persistence_layer._load_room_cache_async()

    assert not async_persistence_layer._room_cache


@pytest.mark.asyncio
async def test_load_room_cache_async_table_not_found(async_persistence_layer):
    """Test _load_room_cache_async handles table not found error."""
    from sqlalchemy.exc import SQLAlchemyError

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("relation 'rooms' does not exist", None, None))

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence_room_loader.get_async_session", side_effect=mock_get_async_session):
        await async_persistence_layer._load_room_cache_async()

    assert not async_persistence_layer._room_cache


@pytest.mark.asyncio
async def test_load_room_cache_async_other_error_raises(async_persistence_layer):
    """Test _load_room_cache_async raises other errors."""
    from sqlalchemy.exc import SQLAlchemyError

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("Other database error", None, None))

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence_room_loader.get_async_session", side_effect=mock_get_async_session):
        with pytest.raises(SQLAlchemyError):
            await async_persistence_layer._load_room_cache_async()


@pytest.mark.asyncio
async def test_query_rooms_with_exits_async_table_not_found(async_persistence_layer):
    """Test _query_rooms_with_exits_async handles table not found error."""
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=Exception("relation 'rooms' does not exist"))

    result = await async_persistence_layer._query_rooms_with_exits_async(mock_session)

    assert result == []


@pytest.mark.asyncio
async def test_query_rooms_with_exits_async_other_error_raises(async_persistence_layer):
    """Test _query_rooms_with_exits_async raises other errors."""
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=Exception("Other database error"))

    with pytest.raises(Exception, match="Other database error"):
        await async_persistence_layer._query_rooms_with_exits_async(mock_session)


@pytest.mark.asyncio
async def test_get_user_by_username_case_insensitive_no_session(async_persistence_layer):
    """Test get_user_by_username_case_insensitive when no session is yielded."""

    async def mock_get_async_session():
        if False:  # pylint: disable=using-constant-test  # Reason: Intentional - ensures generator doesn't yield
            yield  # type: ignore[unreachable]  # Reason: Intentional unreachable code to create empty generator

    with patch("server.async_persistence_direct_queries.get_async_session", side_effect=mock_get_async_session):
        result = await async_persistence_layer.get_user_by_username_case_insensitive("testuser")

    assert result is None


@pytest.mark.asyncio
async def test_get_professions_no_session(async_persistence_layer):
    """Test get_professions when no session is yielded."""

    async def mock_get_async_session():
        if False:  # pylint: disable=using-constant-test  # Reason: Intentional - ensures generator doesn't yield
            yield  # type: ignore[unreachable]  # Reason: Intentional unreachable code to create empty generator

    with patch("server.async_persistence_direct_queries.get_async_session", side_effect=mock_get_async_session):
        result = await async_persistence_layer.get_professions()

    assert result == []


@pytest.mark.asyncio
async def test_get_players_batch_empty_list(async_persistence_layer):
    """Test get_players_batch with empty list."""
    async_persistence_layer._ensure_room_cache_loaded = AsyncMock()

    result = await async_persistence_layer.get_players_batch([])

    assert result == {}


@pytest.mark.asyncio
async def test_get_players_batch_with_players(async_persistence_layer):
    """Test get_players_batch with actual players (UUID conversion)."""
    async_persistence_layer._ensure_room_cache_loaded = AsyncMock()

    player_id1 = uuid.uuid4()
    player_id2 = uuid.uuid4()
    mock_player1 = MagicMock(spec=Player)
    mock_player1.player_id = str(player_id1)
    mock_player2 = MagicMock(spec=Player)
    mock_player2.player_id = str(player_id2)

    async_persistence_layer._player_repo.get_players_batch = AsyncMock(return_value=[mock_player1, mock_player2])

    result = await async_persistence_layer.get_players_batch([player_id1, player_id2])

    assert len(result) == 2
    assert player_id1 in result
    assert player_id2 in result
    assert result[player_id1] == mock_player1
    assert result[player_id2] == mock_player2


def test_generate_room_id_from_zone_data_with_prefix(async_persistence_layer):
    """Test _generate_room_id_from_zone_data when stable_id already has full path."""
    zone_stable_id = "earth/arkhamcity"
    subzone_stable_id = "northside"
    stable_id = "earth_arkhamcity_northside_room_001"

    result = async_persistence_layer._generate_room_id_from_zone_data(zone_stable_id, subzone_stable_id, stable_id)

    assert result == stable_id


def test_generate_room_id_from_zone_data_needs_generation(async_persistence_layer):
    """Test _generate_room_id_from_zone_data when room ID needs generation."""
    with patch(
        "server.world_loader.generate_room_id", return_value="earth_arkhamcity_northside_room_002"
    ) as mock_generate:
        result = async_persistence_layer._generate_room_id_from_zone_data("earth/arkhamcity", "northside", "room_002")

        assert result == "earth_arkhamcity_northside_room_002"
        mock_generate.assert_called_once_with("earth", "arkhamcity", "northside", "room_002")


def test_generate_room_id_from_zone_data_none_values(async_persistence_layer):
    """Test _generate_room_id_from_zone_data with None values."""
    with patch("server.world_loader.generate_room_id", return_value="generated_id") as mock_generate:
        result = async_persistence_layer._generate_room_id_from_zone_data(None, None, None)

        assert result == "generated_id"
        mock_generate.assert_called_once_with("", "", "", "")


def test_parse_exits_json_string_valid(async_persistence_layer):
    """Test _parse_exits_json with valid JSON string."""
    exits_json = '[{"direction": "north", "to_room_stable_id": "room_002"}]'

    result = async_persistence_layer._parse_exits_json(exits_json)

    assert len(result) == 1
    assert result[0]["direction"] == "north"
    assert result[0]["to_room_stable_id"] == "room_002"


def test_parse_exits_json_string_invalid(async_persistence_layer):
    """Test _parse_exits_json with invalid JSON string."""
    exits_json = "invalid json"

    result = async_persistence_layer._parse_exits_json(exits_json)

    assert result == []


def test_parse_exits_json_list(async_persistence_layer):
    """Test _parse_exits_json with list."""
    exits_json = [{"direction": "south", "to_room_stable_id": "room_003"}]

    result = async_persistence_layer._parse_exits_json(exits_json)

    assert result == exits_json


def test_parse_exits_json_other_type(async_persistence_layer):
    """Test _parse_exits_json with non-string, non-list value."""
    result = async_persistence_layer._parse_exits_json({})

    assert result == []


def test_process_exits_for_room_with_direction(async_persistence_layer):
    """Test _process_exits_for_room processes exits with direction."""
    room_id = "room_001"
    exits_list = [
        {
            "direction": "north",
            "to_room_stable_id": "room_002",
            "to_subzone_stable_id": "subzone",
            "to_zone_stable_id": "earth/arkhamcity",
        }
    ]
    exits_by_room: dict[str, dict[str, str]] = {}

    with patch.object(
        async_persistence_layer._room_loader, "_generate_room_id_from_zone_data", return_value="room_002_full_id"
    ):
        async_persistence_layer._process_exits_for_room(room_id, exits_list, exits_by_room)

    assert room_id in exits_by_room
    assert exits_by_room[room_id]["north"] == "room_002_full_id"


def test_process_exits_for_room_no_direction(async_persistence_layer):
    """Test _process_exits_for_room skips exits without direction."""
    room_id = "room_001"
    exits_list = [{"to_room_stable_id": "room_002"}]
    exits_by_room: dict[str, dict[str, str]] = {}

    async_persistence_layer._process_exits_for_room(room_id, exits_list, exits_by_room)

    assert room_id not in exits_by_room or not exits_by_room[room_id]


def test_process_exits_for_room_multiple_exits(async_persistence_layer):
    """Test _process_exits_for_room handles multiple exits."""
    room_id = "room_001"
    exits_list = [
        {
            "direction": "north",
            "to_room_stable_id": "room_002",
            "to_subzone_stable_id": "sub",
            "to_zone_stable_id": "earth/zone",
        },
        {
            "direction": "south",
            "to_room_stable_id": "room_003",
            "to_subzone_stable_id": "sub",
            "to_zone_stable_id": "earth/zone",
        },
    ]
    exits_by_room: dict[str, dict[str, str]] = {}

    with patch.object(
        async_persistence_layer._room_loader,
        "_generate_room_id_from_zone_data",
        side_effect=["room_002_id", "room_003_id"],
    ):
        async_persistence_layer._process_exits_for_room(room_id, exits_list, exits_by_room)

    assert room_id in exits_by_room
    assert "north" in exits_by_room[room_id]
    assert "south" in exits_by_room[room_id]


def test_process_combined_rows_with_exits(async_persistence_layer):
    """Test _process_combined_rows processes rows with exits JSON."""
    combined_rows: list[dict[str, Any]] = [
        {
            "stable_id": "room_001",
            "name": "Test Room",
            "description": "A test room",
            "attributes": {},
            "subzone_stable_id": "subzone",
            "zone_stable_id": "earth/arkhamcity",
            "exits": '[{"direction": "north", "to_room_stable_id": "room_002", "to_subzone_stable_id": "sub", "to_zone_stable_id": "earth/zone"}]',
        }
    ]

    with patch.object(
        async_persistence_layer._room_loader,
        "_generate_room_id_from_zone_data",
        side_effect=["room_001_id", "room_002_id"],
    ):
        room_data_list, exits_by_room = async_persistence_layer._process_combined_rows(combined_rows)

    assert len(room_data_list) == 1
    assert room_data_list[0]["room_id"] == "room_001_id"
    assert "room_001_id" in exits_by_room
    assert "north" in exits_by_room["room_001_id"]


def test_process_combined_rows_no_exits(async_persistence_layer):
    """Test _process_combined_rows processes rows without exits."""
    combined_rows: list[dict[str, Any]] = [
        {
            "stable_id": "room_001",
            "name": "Test Room",
            "description": "A test room",
            "attributes": {},
            "subzone_stable_id": "subzone",
            "zone_stable_id": "earth/arkhamcity",
            "exits": None,
        }
    ]

    with patch.object(
        async_persistence_layer._room_loader, "_generate_room_id_from_zone_data", return_value="room_001_id"
    ):
        room_data_list, exits_by_room = async_persistence_layer._process_combined_rows(combined_rows)

    assert len(room_data_list) == 1
    assert not exits_by_room


def test_process_room_rows_with_none_zone_stable_id(async_persistence_layer):
    """Test _process_room_rows handles None zone_stable_id."""
    rooms_rows = [{"stable_id": "room_001", "zone_stable_id": None}]

    with patch.object(async_persistence_layer._room_loader, "_logger") as mock_logger:
        result = async_persistence_layer._process_room_rows(rooms_rows)

    assert not result
    mock_logger.warning.assert_called()


def test_process_room_rows_with_none_stable_id(async_persistence_layer):
    """Test _process_room_rows handles None stable_id."""
    rooms_rows = [{"stable_id": None, "zone_stable_id": "earth/arkhamcity"}]

    with patch.object(async_persistence_layer._room_loader, "_logger") as mock_logger:
        result = async_persistence_layer._process_room_rows(rooms_rows)

    assert not result
    mock_logger.warning.assert_called()


def test_process_exit_rows_missing_direction(async_persistence_layer):
    """Test _process_exit_rows handles missing direction."""
    exit_rows = [
        {
            "from_room_stable_id": "room_001",
            "to_room_stable_id": "room_002",
            "direction": None,
            "from_subzone_stable_id": "sub",
            "from_zone_stable_id": "earth/zone",
            "to_subzone_stable_id": "sub",
            "to_zone_stable_id": "earth/zone",
        }
    ]

    with patch.object(async_persistence_layer._room_loader, "_logger") as mock_logger:
        result = async_persistence_layer._process_exit_rows(exit_rows)

    assert not result
    mock_logger.warning.assert_called()


def test_process_exit_rows_missing_zone(async_persistence_layer):
    """Test _process_exit_rows handles missing zone data."""
    exit_rows = [
        {
            "from_room_stable_id": "room_001",
            "to_room_stable_id": "room_002",
            "direction": "north",
            "from_subzone_stable_id": "sub",
            "from_zone_stable_id": None,
            "to_subzone_stable_id": "sub",
            "to_zone_stable_id": "earth/zone",
        }
    ]

    with patch.object(async_persistence_layer._room_loader, "_logger") as mock_logger:
        result = async_persistence_layer._process_exit_rows(exit_rows)

    assert not result
    mock_logger.warning.assert_called()


def test_process_exit_rows_missing_stable_id(async_persistence_layer):
    """Test _process_exit_rows handles missing stable_id."""
    exit_rows = [
        {
            "from_room_stable_id": None,
            "to_room_stable_id": "room_002",
            "direction": "north",
            "from_subzone_stable_id": "sub",
            "from_zone_stable_id": "earth/zone",
            "to_subzone_stable_id": "sub",
            "to_zone_stable_id": "earth/zone",
        }
    ]

    with patch.object(async_persistence_layer._room_loader, "_logger") as mock_logger:
        result = async_persistence_layer._process_exit_rows(exit_rows)

    assert not result
    mock_logger.warning.assert_called()


@pytest.mark.asyncio
async def test_load_room_cache_async_warning_logging(async_persistence_layer):
    """Test _load_room_cache_async logs warning when table not found."""
    from sqlalchemy.exc import SQLAlchemyError

    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("relation 'rooms' does not exist", None, None))

    async def mock_get_async_session():
        yield mock_session

    with patch("server.async_persistence_room_loader.get_async_session", side_effect=mock_get_async_session):
        with patch.object(async_persistence_layer._room_loader, "_logger") as mock_logger:
            await async_persistence_layer._load_room_cache_async()

    mock_logger.warning.assert_called()


@pytest.mark.asyncio
async def test_warmup_room_cache(async_persistence_layer):
    """Test warmup_room_cache calls _ensure_room_cache_loaded."""
    async_persistence_layer._ensure_room_cache_loaded = AsyncMock()

    await async_persistence_layer.warmup_room_cache()

    async_persistence_layer._ensure_room_cache_loaded.assert_awaited_once()


@pytest.mark.asyncio
async def test_load_room_cache_async_success_with_rooms_logs_sample_ids(async_persistence_layer):
    """Test _load_room_cache_async logs sample room IDs when rooms are loaded successfully."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = []
    mock_session.execute = AsyncMock(return_value=mock_result)

    async def mock_get_async_session():
        yield mock_session

    mock_room1 = MagicMock()
    mock_room2 = MagicMock()
    mock_room3 = MagicMock()
    mock_room4 = MagicMock()
    mock_room5 = MagicMock()
    mock_room6 = MagicMock()

    loader = async_persistence_layer._room_loader
    loader._query_rooms_with_exits_async = AsyncMock(return_value=[])
    loader._process_combined_rows = MagicMock(return_value=([], {}))

    def mock_build_rooms(room_data, exits, container):
        container["rooms"] = {
            "room_001": mock_room1,
            "room_002": mock_room2,
            "room_003": mock_room3,
            "room_004": mock_room4,
            "room_005": mock_room5,
            "room_006": mock_room6,
        }

    loader._build_room_objects = MagicMock(side_effect=mock_build_rooms)

    with patch("server.async_persistence_room_loader.get_async_session", side_effect=mock_get_async_session):
        with patch.object(loader, "_logger") as mock_logger:
            await async_persistence_layer._load_room_cache_async()

    mock_logger.debug.assert_called_once()
    call_kwargs = mock_logger.debug.call_args[1]
    assert "sample_room_ids" in call_kwargs
    assert len(call_kwargs["sample_room_ids"]) == 5
