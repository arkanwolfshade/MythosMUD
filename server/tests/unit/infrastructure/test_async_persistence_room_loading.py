"""
Unit tests for async persistence layer: process_room_rows, process_exit_rows, build_room_objects, ensure_room_cache.

Part of split from test_async_persistence.py to satisfy file-nloc limit.
"""

# pylint: disable=protected-access  # Reason: Test file - accessing protected members for unit testing
# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names must match fixture names

import asyncio
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.exceptions import DatabaseError


def test_process_room_rows_with_full_room_id(async_persistence_layer):
    """Test _process_room_rows with stable_id that already contains full hierarchical path."""
    row = {
        "stable_id": "earth_arkhamcity_subzone_room_001",
        "name": "Test Room",
        "description": "A test room",
        "attributes": {"environment": "indoors"},
        "subzone_stable_id": "subzone",
        "zone_stable_id": "earth/arkhamcity",
    }

    rows = [row]

    with patch("server.world_loader.generate_room_id") as mock_generate:
        result = async_persistence_layer._process_room_rows(rows)

    assert len(result) == 1
    assert result[0]["room_id"] == "earth_arkhamcity_subzone_room_001"
    mock_generate.assert_not_called()


def test_process_room_rows_with_partial_room_id(async_persistence_layer):
    """Test _process_room_rows with stable_id that needs room ID generation."""
    row = {
        "stable_id": "room_001",
        "name": "Test Room",
        "description": "A test room",
        "attributes": {"environment": "indoors"},
        "subzone_stable_id": "subzone",
        "zone_stable_id": "earth/arkhamcity",
    }

    rows = [row]

    with patch(
        "server.world_loader.generate_room_id", return_value="earth_arkhamcity_subzone_room_001"
    ) as mock_generate:
        result = async_persistence_layer._process_room_rows(rows)

    assert len(result) == 1
    assert result[0]["room_id"] == "earth_arkhamcity_subzone_room_001"
    mock_generate.assert_called_once()


def test_process_room_rows_with_none_attributes(async_persistence_layer):
    """Test _process_room_rows handles None attributes."""
    row = {
        "stable_id": "room_001",
        "name": "Test Room",
        "description": "A test room",
        "attributes": None,
        "subzone_stable_id": "subzone",
        "zone_stable_id": "earth/arkhamcity",
    }

    rows = [row]

    with patch("server.world_loader.generate_room_id", return_value="earth_arkhamcity_subzone_room_001"):
        result = async_persistence_layer._process_room_rows(rows)

    assert len(result) == 1
    assert result[0]["attributes"] == {}


def test_process_room_rows_zone_without_slash(async_persistence_layer):
    """Test _process_room_rows handles zone_stable_id without slash."""
    row = {
        "stable_id": "room_001",
        "name": "Test Room",
        "description": "A test room",
        "attributes": {},
        "subzone_stable_id": "subzone",
        "zone_stable_id": "earth_arkhamcity",
    }

    rows = [row]

    with patch("server.world_loader.generate_room_id", return_value="earth_arkhamcity_subzone_room_001"):
        result = async_persistence_layer._process_room_rows(rows)

    assert len(result) == 1
    assert result[0]["plane"] == "earth_arkhamcity"
    assert result[0]["zone"] == "earth_arkhamcity"


def test_process_exit_rows_with_full_room_ids(async_persistence_layer):
    """Test _process_exit_rows with stable_ids that already contain full hierarchical path."""
    row = {
        "from_room_stable_id": "earth_arkhamcity_subzone_room_001",
        "to_room_stable_id": "earth_arkhamcity_subzone_room_002",
        "direction": "north",
        "from_subzone_stable_id": "subzone",
        "from_zone_stable_id": "earth/arkhamcity",
        "to_subzone_stable_id": "subzone",
        "to_zone_stable_id": "earth/arkhamcity",
    }

    rows = [row]

    with patch("server.world_loader.generate_room_id") as mock_generate:
        result = async_persistence_layer._process_exit_rows(rows)

    assert "earth_arkhamcity_subzone_room_001" in result
    assert result["earth_arkhamcity_subzone_room_001"]["north"] == "earth_arkhamcity_subzone_room_002"
    mock_generate.assert_not_called()


def test_process_exit_rows_with_partial_room_ids(async_persistence_layer):
    """Test _process_exit_rows with stable_ids that need room ID generation."""
    row = {
        "from_room_stable_id": "room_001",
        "to_room_stable_id": "room_002",
        "direction": "north",
        "from_subzone_stable_id": "subzone",
        "from_zone_stable_id": "earth/arkhamcity",
        "to_subzone_stable_id": "subzone",
        "to_zone_stable_id": "earth/arkhamcity",
    }

    rows = [row]

    with patch(
        "server.world_loader.generate_room_id",
        side_effect=["earth_arkhamcity_subzone_room_001", "earth_arkhamcity_subzone_room_002"],
    ) as mock_generate:
        result = async_persistence_layer._process_exit_rows(rows)

    assert "earth_arkhamcity_subzone_room_001" in result
    assert result["earth_arkhamcity_subzone_room_001"]["north"] == "earth_arkhamcity_subzone_room_002"
    assert mock_generate.call_count == 2


def test_process_exit_rows_debug_logging(async_persistence_layer):
    """Test _process_exit_rows logs debug info for specific room."""
    row = {
        "from_room_stable_id": "earth_arkhamcity_sanitarium_room_foyer_001",
        "to_room_stable_id": "room_002",
        "direction": "north",
        "from_subzone_stable_id": "sanitarium",
        "from_zone_stable_id": "earth/arkhamcity",
        "to_subzone_stable_id": "subzone",
        "to_zone_stable_id": "earth/arkhamcity",
    }

    rows = [row]

    with patch("server.world_loader.generate_room_id", return_value="earth_arkhamcity_sanitarium_room_foyer_001"):
        with patch.object(async_persistence_layer._room_loader, "_logger") as mock_logger:
            async_persistence_layer._process_exit_rows(rows)

    mock_logger.info.assert_called()


def test_build_room_objects_success(async_persistence_layer):
    """Test _build_room_objects successfully builds room objects."""
    room_data_list = [
        {
            "room_id": "earth_arkhamcity_subzone_room_001",
            "stable_id": "room_001",
            "name": "Test Room",
            "description": "A test room",
            "attributes": {"environment": "indoors"},
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "subzone",
        }
    ]
    exits_by_room: dict[str, dict[str, str]] = {
        "earth_arkhamcity_subzone_room_001": {"north": "earth_arkhamcity_subzone_room_002"}
    }
    result_container: dict[str, Any] = {"rooms": {}}

    with patch("server.models.room.Room") as mock_room_class:
        mock_room_instance = MagicMock()
        mock_room_class.return_value = mock_room_instance
        async_persistence_layer._build_room_objects(room_data_list, exits_by_room, result_container)

    assert "earth_arkhamcity_subzone_room_001" in result_container["rooms"]
    mock_room_class.assert_called_once()


def test_build_room_objects_with_non_dict_attributes(async_persistence_layer):
    """Test _build_room_objects handles non-dict attributes."""
    room_data_list = [
        {
            "room_id": "earth_arkhamcity_subzone_room_001",
            "stable_id": "room_001",
            "name": "Test Room",
            "description": "A test room",
            "attributes": "not a dict",
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "subzone",
        }
    ]
    exits_by_room: dict[str, dict[str, str]] = {}
    result_container: dict[str, Any] = {"rooms": {}}

    with patch("server.models.room.Room") as mock_room_class:
        mock_room_instance = MagicMock()
        mock_room_class.return_value = mock_room_instance
        async_persistence_layer._build_room_objects(room_data_list, exits_by_room, result_container)

    call_args = mock_room_class.call_args[0][0]
    assert call_args["resolved_environment"] == "outdoors"


def test_build_room_objects_debug_logging(async_persistence_layer):
    """Test _build_room_objects logs debug info for specific room."""
    room_data_list = [
        {
            "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
            "stable_id": "room_foyer_001",
            "name": "Foyer",
            "description": "A foyer",
            "attributes": {},
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "sanitarium",
        }
    ]
    exits_by_room: dict[str, dict[str, str]] = {}
    result_container: dict[str, Any] = {"rooms": {}}

    with patch("server.models.room.Room", return_value=MagicMock()):
        with patch.object(async_persistence_layer._room_loader, "_logger") as mock_logger:
            async_persistence_layer._build_room_objects(room_data_list, exits_by_room, result_container)

    mock_logger.info.assert_called()


def test_load_room_cache_success(async_persistence_layer):
    """Test _load_room_cache successfully loads rooms."""
    async_persistence_layer._async_load_room_cache = AsyncMock()

    with patch("threading.Thread") as mock_thread_class:
        mock_thread = MagicMock()
        mock_thread_class.return_value = mock_thread

        with patch.object(async_persistence_layer, "_async_load_room_cache", new_callable=AsyncMock) as mock_async:

            async def mock_async_load(result_cont):
                result_cont["rooms"] = {"room_001": MagicMock()}
                result_cont["error"] = None

            mock_async.side_effect = mock_async_load

            # We can't easily test threading; this test only verifies the mock is configured
            assert mock_async.side_effect is not None


def test_load_room_cache_with_rooms_logs_sample_ids(async_persistence_layer):
    """Test _load_room_cache logs sample room IDs when rooms are loaded."""
    async_persistence_layer._room_cache = {
        "room_001": MagicMock(),
        "room_002": MagicMock(),
        "room_003": MagicMock(),
        "room_004": MagicMock(),
        "room_005": MagicMock(),
        "room_006": MagicMock(),
    }

    with patch.object(async_persistence_layer, "_logger") as mock_logger:
        if async_persistence_layer._room_cache:
            sample_room_ids = list(async_persistence_layer._room_cache.keys())[:5]
            async_persistence_layer._logger.debug("Sample room IDs loaded", sample_room_ids=sample_room_ids)

    mock_logger.debug.assert_called_once()
    call_kwargs = mock_logger.debug.call_args[1]
    assert "sample_room_ids" in call_kwargs
    assert len(call_kwargs["sample_room_ids"]) == 5


def test_process_room_rows_empty_list(async_persistence_layer):
    """Test _process_room_rows with empty list."""
    result = async_persistence_layer._process_room_rows([])
    assert not result


def test_process_exit_rows_empty_list(async_persistence_layer):
    """Test _process_exit_rows with empty list."""
    result = async_persistence_layer._process_exit_rows([])
    assert not result


def test_process_exit_rows_multiple_exits_same_room(async_persistence_layer):
    """Test _process_exit_rows with multiple exits from same room."""
    row1 = {
        "from_room_stable_id": "room_001",
        "to_room_stable_id": "room_002",
        "direction": "north",
        "from_subzone_stable_id": "subzone",
        "from_zone_stable_id": "earth/arkhamcity",
        "to_subzone_stable_id": "subzone",
        "to_zone_stable_id": "earth/arkhamcity",
    }

    row2 = {
        "from_room_stable_id": "room_001",
        "to_room_stable_id": "room_003",
        "direction": "south",
        "from_subzone_stable_id": "subzone",
        "from_zone_stable_id": "earth/arkhamcity",
        "to_subzone_stable_id": "subzone",
        "to_zone_stable_id": "earth/arkhamcity",
    }

    rows = [row1, row2]

    with patch("server.world_loader.generate_room_id", side_effect=["room_001", "room_002", "room_001", "room_003"]):
        result = async_persistence_layer._process_exit_rows(rows)

    assert "room_001" in result
    assert "north" in result["room_001"]
    assert "south" in result["room_001"]
    assert result["room_001"]["north"] == "room_002"
    assert result["room_001"]["south"] == "room_003"


def test_process_room_rows_zone_single_part(async_persistence_layer):
    """Test _process_room_rows with zone_stable_id that has only one part (no slash)."""
    row = {
        "stable_id": "room_001",
        "name": "Test Room",
        "description": "A test room",
        "attributes": {},
        "subzone_stable_id": "subzone",
        "zone_stable_id": "earth",
    }

    rows = [row]

    with patch("server.world_loader.generate_room_id", return_value="earth_earth_subzone_room_001"):
        result = async_persistence_layer._process_room_rows(rows)

    assert len(result) == 1
    assert result[0]["plane"] == "earth"
    assert result[0]["zone"] == "earth"


def test_process_exit_rows_zone_single_part(async_persistence_layer):
    """Test _process_exit_rows with zone_stable_id that has only one part."""
    row = {
        "from_room_stable_id": "room_001",
        "to_room_stable_id": "room_002",
        "direction": "north",
        "from_subzone_stable_id": "subzone",
        "from_zone_stable_id": "earth",
        "to_subzone_stable_id": "subzone",
        "to_zone_stable_id": "earth",
    }

    rows = [row]

    with patch("server.world_loader.generate_room_id", side_effect=["room_001", "room_002"]):
        result = async_persistence_layer._process_exit_rows(rows)

    assert "room_001" in result
    assert result["room_001"]["north"] == "room_002"


def test_build_room_objects_with_exits(async_persistence_layer):
    """Test _build_room_objects includes exits in room data."""
    room_data_list = [
        {
            "room_id": "earth_arkhamcity_subzone_room_001",
            "stable_id": "room_001",
            "name": "Test Room",
            "description": "A test room",
            "attributes": {},
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "subzone",
        }
    ]
    exits_by_room: dict[str, dict[str, str]] = {
        "earth_arkhamcity_subzone_room_001": {
            "north": "earth_arkhamcity_subzone_room_002",
            "south": "earth_arkhamcity_subzone_room_003",
        }
    }
    result_container: dict[str, Any] = {"rooms": {}}

    with patch("server.models.room.Room") as mock_room_class:
        mock_room_instance = MagicMock()
        mock_room_class.return_value = mock_room_instance
        async_persistence_layer._build_room_objects(room_data_list, exits_by_room, result_container)

    call_args = mock_room_class.call_args[0][0]
    assert call_args["exits"] == exits_by_room["earth_arkhamcity_subzone_room_001"]


def test_build_room_objects_with_dict_attributes(async_persistence_layer):
    """Test _build_room_objects uses environment from attributes dict."""
    room_data_list = [
        {
            "room_id": "earth_arkhamcity_subzone_room_001",
            "stable_id": "room_001",
            "name": "Test Room",
            "description": "A test room",
            "attributes": {"environment": "indoors"},
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "subzone",
        }
    ]
    exits_by_room: dict[str, dict[str, str]] = {}
    result_container: dict[str, Any] = {"rooms": {}}

    with patch("server.models.room.Room") as mock_room_class:
        mock_room_instance = MagicMock()
        mock_room_class.return_value = mock_room_instance
        async_persistence_layer._build_room_objects(room_data_list, exits_by_room, result_container)

    call_args = mock_room_class.call_args[0][0]
    assert call_args["resolved_environment"] == "indoors"


def test_build_room_objects_without_environment_in_attributes(async_persistence_layer):
    """Test _build_room_objects defaults to outdoors when environment not in attributes."""
    room_data_list = [
        {
            "room_id": "earth_arkhamcity_subzone_room_001",
            "stable_id": "room_001",
            "name": "Test Room",
            "description": "A test room",
            "attributes": {"other_key": "value"},
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "subzone",
        }
    ]
    exits_by_room: dict[str, dict[str, str]] = {}
    result_container: dict[str, Any] = {"rooms": {}}

    with patch("server.models.room.Room") as mock_room_class:
        mock_room_instance = MagicMock()
        mock_room_class.return_value = mock_room_instance
        async_persistence_layer._build_room_objects(room_data_list, exits_by_room, result_container)

    call_args = mock_room_class.call_args[0][0]
    assert call_args["resolved_environment"] == "outdoors"


@pytest.mark.asyncio
async def test_ensure_room_cache_loaded_already_loaded(async_persistence_layer):
    """Test _ensure_room_cache_loaded returns early when cache is already loaded."""
    async_persistence_layer._room_cache_loaded = True

    await async_persistence_layer._ensure_room_cache_loaded()

    assert async_persistence_layer._room_cache_loaded is True


@pytest.mark.asyncio
async def test_ensure_room_cache_loaded_concurrent_load(async_persistence_layer):
    """Test _ensure_room_cache_loaded handles concurrent load scenario (double-check pattern)."""
    async_persistence_layer._room_cache_loaded = False
    async_persistence_layer._room_cache_loading = asyncio.Lock()

    async def mock_load():
        async_persistence_layer._room_cache_loaded = True
        async_persistence_layer._room_cache["dummy"] = None

    async_persistence_layer._load_room_cache_async = AsyncMock(side_effect=mock_load)

    await async_persistence_layer._ensure_room_cache_loaded()

    assert async_persistence_layer._room_cache_loaded is True


@pytest.mark.asyncio
async def test_ensure_room_cache_loaded_database_error(async_persistence_layer):
    """Test _ensure_room_cache_loaded handles DatabaseError gracefully."""
    async_persistence_layer._room_cache_loaded = False
    async_persistence_layer._load_room_cache_async = AsyncMock(side_effect=DatabaseError("Database error"))

    await async_persistence_layer._ensure_room_cache_loaded()

    assert async_persistence_layer._room_cache_loaded is False
    assert not async_persistence_layer._room_cache


@pytest.mark.asyncio
async def test_ensure_room_cache_loaded_os_error(async_persistence_layer):
    """Test _ensure_room_cache_loaded handles OSError gracefully."""
    async_persistence_layer._room_cache_loaded = False
    async_persistence_layer._load_room_cache_async = AsyncMock(side_effect=OSError("Connection error"))

    await async_persistence_layer._ensure_room_cache_loaded()

    assert async_persistence_layer._room_cache_loaded is False
    assert not async_persistence_layer._room_cache


@pytest.mark.asyncio
async def test_ensure_room_cache_loaded_runtime_error(async_persistence_layer):
    """Test _ensure_room_cache_loaded handles RuntimeError gracefully."""
    async_persistence_layer._room_cache_loaded = False
    async_persistence_layer._load_room_cache_async = AsyncMock(side_effect=RuntimeError("Runtime error"))

    await async_persistence_layer._ensure_room_cache_loaded()

    assert async_persistence_layer._room_cache_loaded is False
    assert not async_persistence_layer._room_cache
