"""
Unit tests for look_npc helper functions.

Tests the helper functions in look_npc.py module.
"""

from datetime import datetime
from unittest.mock import MagicMock

from server.commands.look_npc import (
    _format_core_attributes,
    _format_lifecycle_info,
    _format_npc_description,
    _format_other_stats,
    _get_npc_room_id,
    _parse_npc_stats_dict,
    _parse_stat_datetime,
    _should_include_npc,
)


def test_parse_npc_stats_dict_from_dict():
    """Test _parse_npc_stats_dict() handles dict input."""
    npc_stats = {"strength": 50, "dexterity": 40}

    result = _parse_npc_stats_dict(npc_stats)

    assert result == {"strength": 50, "dexterity": 40}


def test_parse_npc_stats_dict_from_json_string():
    """Test _parse_npc_stats_dict() parses JSON string."""
    npc_stats = '{"strength": 50, "dexterity": 40}'

    result = _parse_npc_stats_dict(npc_stats)

    assert result == {"strength": 50, "dexterity": 40}


def test_parse_npc_stats_dict_invalid_json():
    """Test _parse_npc_stats_dict() returns empty dict for invalid JSON."""
    npc_stats = "invalid json"

    result = _parse_npc_stats_dict(npc_stats)

    assert result == {}


def test_parse_npc_stats_dict_other_type():
    """Test _parse_npc_stats_dict() returns empty dict for other types."""
    result = _parse_npc_stats_dict(123)

    assert result == {}


def test_format_core_attributes():
    """Test _format_core_attributes() formats core attributes."""
    npc_stats = {
        "strength": 50,
        "dexterity": 40,
        "constitution": 45,
        "intelligence": 60,
    }

    result = _format_core_attributes(npc_stats)

    result_str = "\n".join(result)
    assert "Core Attributes:" in result_str
    assert "STR: 50" in result_str
    assert "DEX: 40" in result_str
    assert "CON: 45" in result_str
    assert "INT: 60" in result_str


def test_format_core_attributes_empty():
    """Test _format_core_attributes() returns empty list when no core attributes."""
    npc_stats = {}

    result = _format_core_attributes(npc_stats)

    assert result == []


def test_format_other_stats():
    """Test _format_other_stats() formats non-core stats."""
    npc_stats = {
        "strength": 50,
        "current_dp": 20,
        "magic_points": 10,
    }

    result = _format_other_stats(npc_stats)

    result_str = "\n".join(result)
    assert "Other Stats:" in result_str
    assert "current_dp: 20" in result_str
    assert "magic_points: 10" in result_str
    assert "strength" not in result_str


def test_format_other_stats_empty():
    """Test _format_other_stats() returns empty list when no other stats."""
    npc_stats = {
        "strength": 50,
        "dexterity": 40,
    }

    result = _format_other_stats(npc_stats)

    assert result == []


def test_parse_stat_datetime_from_datetime():
    """Test _parse_stat_datetime() handles datetime object."""
    dt = datetime(2025, 1, 1, 12, 0, 0)

    result = _parse_stat_datetime(dt)

    assert "2025-01-01 12:00:00" in result


def test_parse_stat_datetime_from_timestamp():
    """Test _parse_stat_datetime() handles timestamp."""
    timestamp = 1735747200  # 2025-01-01 12:00:00 UTC

    result = _parse_stat_datetime(timestamp)

    assert "2025-01-01" in result


def test_parse_stat_datetime_from_iso_string():
    """Test _parse_stat_datetime() handles ISO string."""
    iso_string = "2025-01-01T12:00:00"

    result = _parse_stat_datetime(iso_string)

    assert "2025-01-01" in result


def test_parse_stat_datetime_none():
    """Test _parse_stat_datetime() returns 'Unknown' for None."""
    result = _parse_stat_datetime(None)

    assert result == "Unknown"


def test_parse_stat_datetime_invalid():
    """Test _parse_stat_datetime() returns string representation for invalid input."""
    result = _parse_stat_datetime("invalid")

    assert isinstance(result, str)


def test_format_lifecycle_info():
    """Test _format_lifecycle_info() formats lifecycle information."""
    stats = {
        "lifecycle_state": "active",
        "spawn_time": datetime(2025, 1, 1, 12, 0, 0),
        "last_activity": datetime(2025, 1, 1, 13, 0, 0),
        "spawn_count": 5,
        "despawn_count": 2,
    }

    result = _format_lifecycle_info(stats)

    result_str = "\n".join(result)
    assert "Lifecycle:" in result_str
    assert "State: active" in result_str
    assert "Spawn Time:" in result_str
    assert "Last Activity:" in result_str
    assert "Spawn Count: 5" in result_str
    assert "Despawn Count: 2" in result_str


def test_format_lifecycle_info_no_lifecycle_state():
    """Test _format_lifecycle_info() returns empty list when no lifecycle_state."""
    stats = {}

    result = _format_lifecycle_info(stats)

    assert result == []


def test_format_npc_description():
    """Test _format_npc_description() returns description from definition."""
    npc = MagicMock()
    npc.definition.description = "A test NPC."

    result = _format_npc_description(npc)

    assert result == "A test NPC."


def test_format_npc_description_fallback():
    """Test _format_npc_description() uses fallback when description is empty."""
    npc = MagicMock()
    definition = MagicMock()
    definition.description = ""
    definition.long_description = None
    definition.short_description = None
    definition.desc = None
    npc.definition = definition

    result = _format_npc_description(npc)

    assert result == "You see nothing remarkable about them."


def test_format_npc_description_no_description():
    """Test _format_npc_description() uses alternative attributes."""
    npc = MagicMock()
    npc.definition.description = None
    npc.definition.long_description = "A detailed description."

    result = _format_npc_description(npc)

    assert result == "A detailed description."


def test_get_npc_room_id_from_current_room_id():
    """Test _get_npc_room_id() returns current_room_id when available."""
    npc_instance = MagicMock()
    npc_instance.current_room_id = "room_001"
    npc_instance.current_room = "room_002"

    result = _get_npc_room_id(npc_instance)

    assert result == "room_001"


def test_get_npc_room_id_from_current_room():
    """Test _get_npc_room_id() returns current_room when current_room_id is None."""
    npc_instance = MagicMock()
    npc_instance.current_room_id = None
    npc_instance.current_room = "room_002"

    result = _get_npc_room_id(npc_instance)

    assert result == "room_002"


def test_get_npc_room_id_none():
    """Test _get_npc_room_id() returns None when both are None."""
    npc_instance = MagicMock()
    npc_instance.current_room_id = None
    npc_instance.current_room = None

    result = _get_npc_room_id(npc_instance)

    assert result is None


def test_should_include_npc():
    """Test _should_include_npc() returns True for valid NPC."""
    npc_instance = MagicMock()
    npc_instance.name = "Test NPC"
    npc_instance.is_alive = True

    result = _should_include_npc(npc_instance)

    assert result is True


def test_should_include_npc_no_name():
    """Test _should_include_npc() returns False when no name."""
    npc_instance = MagicMock()
    npc_instance.name = None
    npc_instance.is_alive = True

    result = _should_include_npc(npc_instance)

    assert result is False


def test_should_include_npc_not_alive():
    """Test _should_include_npc() returns False when not alive."""
    npc_instance = MagicMock()
    npc_instance.name = "Test NPC"
    npc_instance.is_alive = False

    result = _should_include_npc(npc_instance)

    assert result is False
