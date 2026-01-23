"""
Unit tests for NPC utility functions.

Tests the utility functions in npc_utils.py.
"""

from unittest.mock import MagicMock

from server.npc.npc_utils import (
    extract_definition_id_from_npc,
    extract_npc_metadata,
    extract_room_id_from_npc,
    get_zone_key_from_room_id,
)


def test_extract_room_id_from_npc_current_room() -> None:
    """Test extract_room_id_from_npc() extracts from current_room."""
    npc = MagicMock()
    npc.current_room = "room-123"
    result = extract_room_id_from_npc(npc)
    assert result == "room-123"


def test_extract_room_id_from_npc_current_room_id() -> None:
    """Test extract_room_id_from_npc() extracts from current_room_id."""
    npc = MagicMock()
    npc.current_room = None
    npc.current_room_id = "room-456"
    result = extract_room_id_from_npc(npc)
    assert result == "room-456"


def test_extract_room_id_from_npc_room_id() -> None:
    """Test extract_room_id_from_npc() extracts from room_id."""
    npc = MagicMock()
    npc.current_room = None
    npc.current_room_id = None
    npc.room_id = "room-789"
    result = extract_room_id_from_npc(npc)
    assert result == "room-789"


def test_extract_room_id_from_npc_not_found() -> None:
    """Test extract_room_id_from_npc() returns 'unknown' when not found."""
    npc = MagicMock()
    npc.current_room = None
    npc.current_room_id = None
    # No room_id attribute
    result = extract_room_id_from_npc(npc)
    assert result == "unknown"


def test_extract_room_id_from_npc_non_string() -> None:
    """Test extract_room_id_from_npc() returns 'unknown' for non-string value."""
    npc = MagicMock()
    npc.current_room = 123  # Not a string
    result = extract_room_id_from_npc(npc)
    assert result == "unknown"


def test_extract_npc_metadata_valid() -> None:
    """Test extract_npc_metadata() extracts valid metadata."""
    npc = MagicMock()
    npc.npc_type = "aggressive_mob"
    npc.is_required = True
    npc_type, is_required = extract_npc_metadata(npc)
    assert npc_type == "aggressive_mob"
    assert is_required is True


def test_extract_npc_metadata_defaults() -> None:
    """Test extract_npc_metadata() returns defaults when missing."""

    # Use a simple object without attributes instead of MagicMock
    class SimpleNPC:
        pass

    npc = SimpleNPC()
    npc_type, is_required = extract_npc_metadata(npc)
    assert npc_type == "unknown"
    assert is_required is False


def test_extract_npc_metadata_non_string_type() -> None:
    """Test extract_npc_metadata() handles non-string npc_type."""
    npc = MagicMock()
    npc.npc_type = 123  # Not a string
    npc.is_required = False
    npc_type, is_required = extract_npc_metadata(npc)
    assert npc_type == "unknown"
    assert is_required is False


def test_extract_npc_metadata_truthy_required() -> None:
    """Test extract_npc_metadata() converts truthy is_required."""
    npc = MagicMock()
    npc.npc_type = "passive_mob"
    npc.is_required = 1  # Truthy but not bool
    npc_type, is_required = extract_npc_metadata(npc)
    assert npc_type == "passive_mob"
    assert is_required is True


def test_extract_npc_metadata_none_required() -> None:
    """Test extract_npc_metadata() handles None is_required."""
    npc = MagicMock()
    npc.npc_type = "shopkeeper"
    npc.is_required = None
    npc_type, is_required = extract_npc_metadata(npc)
    assert npc_type == "shopkeeper"
    assert is_required is False


def test_extract_definition_id_from_npc_has_definition_id() -> None:
    """Test extract_definition_id_from_npc() extracts from NPC instance."""
    npc = MagicMock()
    npc.definition_id = 42
    result = extract_definition_id_from_npc(npc, "npc-123", None)
    assert result == 42


def test_extract_definition_id_from_npc_non_int() -> None:
    """Test extract_definition_id_from_npc() returns None for non-int."""
    npc = MagicMock()
    npc.definition_id = "not-an-int"
    result = extract_definition_id_from_npc(npc, "npc-123", None)
    assert result is None


def test_extract_definition_id_from_npc_from_lifecycle_manager() -> None:
    """Test extract_definition_id_from_npc() extracts from lifecycle manager."""
    npc = MagicMock()
    # No definition_id on NPC
    lifecycle_manager = MagicMock()
    lifecycle_record = MagicMock()
    lifecycle_record.definition = MagicMock()
    lifecycle_record.definition.id = 99
    lifecycle_manager.lifecycle_records = {"npc-123": lifecycle_record}
    result = extract_definition_id_from_npc(npc, "npc-123", lifecycle_manager)
    assert result == 99


def test_extract_definition_id_from_npc_lifecycle_manager_no_record() -> None:
    """Test extract_definition_id_from_npc() returns None when no lifecycle record."""
    npc = MagicMock()
    lifecycle_manager = MagicMock()
    lifecycle_manager.lifecycle_records = {}
    result = extract_definition_id_from_npc(npc, "npc-123", lifecycle_manager)
    assert result is None


def test_extract_definition_id_from_npc_lifecycle_manager_no_definition() -> None:
    """Test extract_definition_id_from_npc() returns None when record has no definition."""
    npc = MagicMock()
    lifecycle_manager = MagicMock()

    # Use a simple object without definition attribute
    class SimpleRecord:
        pass

    lifecycle_record = SimpleRecord()
    lifecycle_manager.lifecycle_records = {"npc-123": lifecycle_record}
    result = extract_definition_id_from_npc(npc, "npc-123", lifecycle_manager)
    assert result is None


def test_extract_definition_id_from_npc_no_manager() -> None:
    """Test extract_definition_id_from_npc() returns None when no manager and no definition_id."""
    npc = MagicMock()
    # No definition_id attribute
    result = extract_definition_id_from_npc(npc, "npc-123", None)
    assert result is None


def test_get_zone_key_from_room_id_valid() -> None:
    """Test get_zone_key_from_room_id() extracts zone key from valid room ID."""
    room_id = "earth_arkhamcity_downtown_001"
    result = get_zone_key_from_room_id(room_id)
    assert result == "arkhamcity/downtown"


def test_get_zone_key_from_room_id_with_description() -> None:
    """Test get_zone_key_from_room_id() handles room ID with description."""
    room_id = "earth_arkhamcity_sanitarium_room_foyer_entrance_001"
    result = get_zone_key_from_room_id(room_id)
    assert result == "arkhamcity/sanitarium"


def test_get_zone_key_from_room_id_innsmouth() -> None:
    """Test get_zone_key_from_room_id() handles Innsmouth room ID."""
    room_id = "earth_innsmouth_waterfront_dock_002"
    result = get_zone_key_from_room_id(room_id)
    assert result == "innsmouth/waterfront"


def test_get_zone_key_from_room_id_short() -> None:
    """Test get_zone_key_from_room_id() returns 'unknown/unknown' for short room ID."""
    room_id = "earth_arkhamcity"
    result = get_zone_key_from_room_id(room_id)
    assert result == "unknown/unknown"


def test_get_zone_key_from_room_id_too_short() -> None:
    """Test get_zone_key_from_room_id() returns 'unknown/unknown' for too short room ID."""
    room_id = "earth"
    result = get_zone_key_from_room_id(room_id)
    assert result == "unknown/unknown"


def test_get_zone_key_from_room_id_exactly_four_parts() -> None:
    """Test get_zone_key_from_room_id() handles room ID with exactly 4 parts."""
    room_id = "earth_arkhamcity_downtown_001"
    result = get_zone_key_from_room_id(room_id)
    assert result == "arkhamcity/downtown"


def test_get_zone_key_from_room_id_many_parts() -> None:
    """Test get_zone_key_from_room_id() handles room ID with many parts."""
    room_id = "earth_arkhamcity_downtown_intersection_derby_garrison_001"
    result = get_zone_key_from_room_id(room_id)
    assert result == "arkhamcity/downtown"
