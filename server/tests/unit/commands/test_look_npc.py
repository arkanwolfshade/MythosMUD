"""
Unit tests for NPC look functionality.

Tests the helper functions for looking at NPCs in rooms.
"""

import json
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.look_npc import (
    _find_matching_npcs,
    _format_core_attributes,
    _format_lifecycle_info,
    _format_multiple_npcs_result,
    _format_npc_description,
    _format_npc_stats_for_admin,
    _format_other_stats,
    _format_single_npc_result,
    _get_lifecycle_manager,
    _get_npc_room_id,
    _parse_npc_stats_dict,
    _parse_stat_datetime,
    _should_include_npc,
    _try_lookup_npc_implicit,
)


@pytest.fixture
def mock_npc():
    """Create a mock NPC."""
    npc = MagicMock()
    npc.npc_id = "test_npc_001"
    npc.name = "Test NPC"
    npc.is_alive = True
    definition = MagicMock()
    definition.description = "A test NPC description."
    npc.definition = definition
    return npc


@pytest.fixture
def mock_lifecycle_manager(mock_npc):
    """Create a mock lifecycle manager."""
    manager = MagicMock()
    manager.active_npcs = {mock_npc.npc_id: mock_npc}
    return manager


def test_parse_npc_stats_dict_from_dict():
    """Test parsing NPC stats from dictionary."""
    stats = {"strength": 50, "dexterity": 40}
    result = _parse_npc_stats_dict(stats)
    assert result == stats


def test_parse_npc_stats_dict_from_json_string():
    """Test parsing NPC stats from JSON string."""
    stats_json = '{"strength": 50, "dexterity": 40}'
    result = _parse_npc_stats_dict(stats_json)
    assert result == {"strength": 50, "dexterity": 40}


def test_parse_npc_stats_dict_invalid_json():
    """Test parsing NPC stats from invalid JSON."""
    result = _parse_npc_stats_dict("not json")
    assert result == {}


def test_parse_npc_stats_dict_non_dict_non_string():
    """Test parsing NPC stats from non-dict, non-string."""
    result = _parse_npc_stats_dict(123)
    assert result == {}


def test_format_core_attributes_success():
    """Test formatting core attributes."""
    npc_stats = {"strength": 50, "dexterity": 40, "constitution": 45}
    result = _format_core_attributes(npc_stats)
    assert len(result) > 0
    assert "Core Attributes:" in result[0]
    assert "STR: 50" in "\n".join(result)
    assert "DEX: 40" in "\n".join(result)


def test_format_core_attributes_empty():
    """Test formatting core attributes when none present."""
    npc_stats = {}
    result = _format_core_attributes(npc_stats)
    assert result == []


def test_format_other_stats_success():
    """Test formatting other stats."""
    npc_stats = {"level": 5, "experience": 1000}
    result = _format_other_stats(npc_stats)
    assert len(result) > 0
    assert "Other Stats:" in result[0]
    assert "level: 5" in "\n".join(result)


def test_format_other_stats_empty():
    """Test formatting other stats when none present."""
    npc_stats = {"strength": 50}  # Only core attributes
    result = _format_other_stats(npc_stats)
    assert result == []


def test_parse_stat_datetime_from_timestamp():
    """Test parsing datetime from timestamp."""
    timestamp = 1609459200  # 2021-01-01 00:00:00 UTC (may vary by timezone)
    result = _parse_stat_datetime(timestamp)
    # datetime.fromtimestamp uses local time, so we just check it's a valid date format
    assert len(result) > 0
    assert ":" in result  # Should have time component
    # Should be in YYYY-MM-DD format
    assert "-" in result


def test_parse_stat_datetime_from_datetime():
    """Test parsing datetime from datetime object."""
    dt = datetime(2021, 1, 1, 12, 30, 45)
    result = _parse_stat_datetime(dt)
    assert "2021-01-01" in result
    assert "12:30:45" in result


def test_parse_stat_datetime_from_iso_string():
    """Test parsing datetime from ISO string."""
    iso_string = "2021-01-01T12:30:45"
    result = _parse_stat_datetime(iso_string)
    assert "2021-01-01" in result


def test_parse_stat_datetime_invalid():
    """Test parsing datetime with invalid value."""
    result = _parse_stat_datetime("invalid")
    assert result == "invalid"


def test_parse_stat_datetime_none():
    """Test parsing datetime with None."""
    result = _parse_stat_datetime(None)
    assert result == "Unknown"


def test_format_lifecycle_info_success():
    """Test formatting lifecycle information."""
    stats = {
        "lifecycle_state": "active",
        "spawn_time": datetime(2021, 1, 1, 12, 0, 0),
        "last_activity": datetime(2021, 1, 1, 13, 0, 0),
        "spawn_count": 5,
        "despawn_count": 2,
    }
    result = _format_lifecycle_info(stats)
    assert len(result) > 0
    assert "Lifecycle:" in result[0]
    assert "State: active" in "\n".join(result)
    assert "Spawn Count: 5" in "\n".join(result)


def test_format_lifecycle_info_empty():
    """Test formatting lifecycle information when not present."""
    stats = {}
    result = _format_lifecycle_info(stats)
    assert result == []


def test_format_npc_description_success(mock_npc):
    """Test formatting NPC description successfully."""
    result = _format_npc_description(mock_npc)
    assert result == "A test NPC description."


def test_format_npc_description_fallback_long_description():
    """Test formatting NPC description with long_description fallback."""
    npc = MagicMock()
    definition = MagicMock()
    definition.description = None
    definition.long_description = "Long description."
    npc.definition = definition
    result = _format_npc_description(npc)
    assert result == "Long description."


def test_format_npc_description_fallback_short_description():
    """Test formatting NPC description with short_description fallback."""
    npc = MagicMock()
    definition = MagicMock()
    definition.description = None
    definition.long_description = None
    definition.short_description = "Short description."
    npc.definition = definition
    result = _format_npc_description(npc)
    assert result == "Short description."


def test_format_npc_description_fallback_desc():
    """Test formatting NPC description with desc fallback."""
    npc = MagicMock()
    definition = MagicMock()
    definition.description = None
    definition.long_description = None
    definition.short_description = None
    definition.desc = "Desc attribute."
    npc.definition = definition
    result = _format_npc_description(npc)
    assert result == "Desc attribute."


def test_format_npc_description_no_description():
    """Test formatting NPC description when no description available."""
    npc = MagicMock()
    definition = MagicMock()
    definition.description = None
    definition.long_description = None
    definition.short_description = None
    definition.desc = None
    npc.definition = definition
    result = _format_npc_description(npc)
    assert result == "You see nothing remarkable about them."


def test_format_npc_description_empty_string():
    """Test formatting NPC description when description is empty string."""
    npc = MagicMock()
    definition = MagicMock()
    definition.description = "   "
    npc.definition = definition
    result = _format_npc_description(npc)
    assert result == "You see nothing remarkable about them."


def test_should_include_npc_alive_with_name(mock_npc):
    """Test should_include_npc for alive NPC with name."""
    assert _should_include_npc(mock_npc) is True


def test_should_include_npc_dead():
    """Test should_include_npc for dead NPC."""
    npc = MagicMock()
    npc.name = "Dead NPC"
    npc.is_alive = False
    assert _should_include_npc(npc) is False


def test_should_include_npc_no_name():
    """Test should_include_npc for NPC without name."""
    npc = MagicMock()
    npc.name = None
    npc.is_alive = True
    assert _should_include_npc(npc) is False


def test_get_npc_room_id_from_current_room_id():
    """Test getting NPC room ID from current_room_id."""
    npc = MagicMock()
    npc.current_room_id = "room_001"
    npc.current_room = "room_002"
    result = _get_npc_room_id(npc)
    assert result == "room_001"


def test_get_npc_room_id_from_current_room():
    """Test getting NPC room ID from current_room when current_room_id is None."""
    npc = MagicMock()
    npc.current_room_id = None
    npc.current_room = "room_002"
    result = _get_npc_room_id(npc)
    assert result == "room_002"


def test_get_npc_room_id_none():
    """Test getting NPC room ID when both are None."""
    npc = MagicMock()
    npc.current_room_id = None
    npc.current_room = None
    result = _get_npc_room_id(npc)
    assert result is None


def test_find_matching_npcs_success(mock_npc, mock_lifecycle_manager):
    """Test finding matching NPCs successfully."""
    with patch("server.commands.look_npc.get_npc_instance_service") as mock_service:
        service_instance = MagicMock()
        service_instance.lifecycle_manager = mock_lifecycle_manager
        mock_service.return_value = service_instance

        result = _find_matching_npcs("test", [mock_npc.npc_id])
        assert len(result) == 1
        assert result[0] == mock_npc


def test_find_matching_npcs_no_match(mock_lifecycle_manager):
    """Test finding matching NPCs when no match."""
    with patch("server.commands.look_npc.get_npc_instance_service") as mock_service:
        service_instance = MagicMock()
        service_instance.lifecycle_manager = mock_lifecycle_manager
        mock_service.return_value = service_instance

        npc = MagicMock()
        npc.npc_id = "other_npc"
        npc.name = "Other NPC"
        mock_lifecycle_manager.active_npcs = {npc.npc_id: npc}

        result = _find_matching_npcs("test", [npc.npc_id])
        assert len(result) == 0


def test_find_matching_npcs_no_lifecycle_manager():
    """Test finding matching NPCs when lifecycle manager not available."""
    with patch("server.commands.look_npc.get_npc_instance_service") as mock_service:
        service_instance = MagicMock()
        service_instance.lifecycle_manager = None
        mock_service.return_value = service_instance

        result = _find_matching_npcs("test", ["npc_001"])
        assert len(result) == 0


@pytest.mark.asyncio
async def test_format_npc_stats_for_admin_success(mock_npc):
    """Test formatting NPC stats for admin successfully."""
    mock_service = MagicMock()
    mock_service.get_npc_stats = AsyncMock(
        return_value={
            "npc_id": mock_npc.npc_id,
            "npc_type": "test_type",
            "current_room_id": "room_001",
            "is_alive": True,
            "stats": {"strength": 50, "dexterity": 40},
            "lifecycle_state": "active",
        }
    )

    with patch("server.commands.look_npc.get_npc_instance_service", return_value=mock_service):
        result = await _format_npc_stats_for_admin(mock_npc)
        assert "Admin Stats" in result
        assert "NPC ID:" in result
        assert "STR: 50" in result


@pytest.mark.asyncio
async def test_format_npc_stats_for_admin_no_npc_id():
    """Test formatting NPC stats for admin when NPC ID missing."""
    npc = MagicMock()
    npc.npc_id = None

    result = await _format_npc_stats_for_admin(npc)
    assert "Admin Stats" in result
    assert "Error: NPC ID not found" in result


@pytest.mark.asyncio
async def test_format_single_npc_result_success(mock_npc):
    """Test formatting single NPC result successfully."""
    player = MagicMock()
    player.is_admin = False

    result = await _format_single_npc_result(mock_npc, "TestPlayer", player)
    assert "result" in result
    assert "Test NPC" in result["result"]
    assert "A test NPC description." in result["result"]


@pytest.mark.asyncio
async def test_format_single_npc_result_with_admin_stats(mock_npc):
    """Test formatting single NPC result with admin stats."""
    player = MagicMock()
    player.is_admin = True

    mock_service = MagicMock()
    mock_service.get_npc_stats = AsyncMock(return_value={"npc_id": mock_npc.npc_id, "npc_type": "test"})

    with patch("server.commands.look_npc.get_npc_instance_service", return_value=mock_service):
        result = await _format_single_npc_result(mock_npc, "TestPlayer", player)
        assert "result" in result
        assert "Admin Stats" in result["result"]


def test_format_multiple_npcs_result(mock_npc):
    """Test formatting multiple NPCs result."""
    npc2 = MagicMock()
    npc2.name = "Test NPC 2"
    matching_npcs = [mock_npc, npc2]

    result = _format_multiple_npcs_result(matching_npcs, "test", "TestPlayer")
    assert "result" in result
    assert "multiple NPCs" in result["result"]
    assert "Test NPC" in result["result"]
    assert "Test NPC 2" in result["result"]


def test_get_lifecycle_manager_success(mock_lifecycle_manager):
    """Test getting lifecycle manager successfully."""
    with patch("server.commands.look_npc.get_npc_instance_service") as mock_service:
        service_instance = MagicMock()
        service_instance.lifecycle_manager = mock_lifecycle_manager
        mock_service.return_value = service_instance

        result = _get_lifecycle_manager()
        assert result == mock_lifecycle_manager


def test_get_lifecycle_manager_no_service():
    """Test getting lifecycle manager when service not available."""
    with patch("server.commands.look_npc.get_npc_instance_service", return_value=None):
        result = _get_lifecycle_manager()
        assert result is None


def test_get_lifecycle_manager_no_lifecycle_manager():
    """Test getting lifecycle manager when lifecycle_manager not available."""
    with patch("server.commands.look_npc.get_npc_instance_service") as mock_service:
        service_instance = MagicMock()
        service_instance.lifecycle_manager = None
        mock_service.return_value = service_instance

        result = _get_lifecycle_manager()
        assert result is None


@pytest.mark.asyncio
async def test_try_lookup_npc_implicit_success(mock_npc, mock_lifecycle_manager):
    """Test trying implicit NPC lookup successfully."""
    room = MagicMock()
    room.get_npcs.return_value = [mock_npc.npc_id]

    with patch("server.commands.look_npc.get_npc_instance_service") as mock_service:
        service_instance = MagicMock()
        service_instance.lifecycle_manager = mock_lifecycle_manager
        mock_service.return_value = service_instance

        result = await _try_lookup_npc_implicit("test", room, "TestPlayer", None)
        assert result is not None
        assert "Test NPC" in result["result"]


@pytest.mark.asyncio
async def test_try_lookup_npc_implicit_no_npcs():
    """Test trying implicit NPC lookup when no NPCs in room."""
    room = MagicMock()
    room.get_npcs.return_value = []

    result = await _try_lookup_npc_implicit("test", room, "TestPlayer", None)
    assert result is None


@pytest.mark.asyncio
async def test_try_lookup_npc_implicit_multiple_matches(mock_npc, mock_lifecycle_manager):
    """Test trying implicit NPC lookup with multiple matches."""
    npc2 = MagicMock()
    npc2.npc_id = "test_npc_002"
    npc2.name = "Test NPC 2"
    npc2.is_alive = True
    definition2 = MagicMock()
    definition2.description = "Another test NPC."
    npc2.definition = definition2

    mock_lifecycle_manager.active_npcs = {mock_npc.npc_id: mock_npc, npc2.npc_id: npc2}

    room = MagicMock()
    room.get_npcs.return_value = [mock_npc.npc_id, npc2.npc_id]

    with patch("server.commands.look_npc.get_npc_instance_service") as mock_service:
        service_instance = MagicMock()
        service_instance.lifecycle_manager = mock_lifecycle_manager
        mock_service.return_value = service_instance

        result = await _try_lookup_npc_implicit("test", room, "TestPlayer", None)
        assert result is not None
        assert "multiple NPCs" in result["result"]
