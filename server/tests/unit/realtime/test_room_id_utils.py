"""
Unit tests for room ID utilities.

Tests the RoomIDUtils class for room ID normalization and comparison.
"""

from unittest.mock import MagicMock

from server.realtime.room_id_utils import RoomIDUtils


def test_room_id_utils_init() -> None:
    """Test RoomIDUtils initialization."""
    mock_manager = MagicMock()
    utils = RoomIDUtils(mock_manager)
    assert utils.connection_manager == mock_manager


def test_get_canonical_room_id() -> None:
    """Test get_canonical_room_id returns canonical ID."""
    mock_manager = MagicMock()
    mock_manager.canonical_room_id = MagicMock(return_value="canonical_room_001")
    utils = RoomIDUtils(mock_manager)
    result = utils.get_canonical_room_id("room_001")
    assert result == "canonical_room_001"


def test_get_canonical_room_id_no_manager() -> None:
    """Test get_canonical_room_id returns original when no manager."""
    utils = RoomIDUtils(None)
    result = utils.get_canonical_room_id("room_001")
    assert result == "room_001"


def test_normalize_room_id_for_comparison_none() -> None:
    """Test normalize_room_id_for_comparison with None."""
    result = RoomIDUtils.normalize_room_id_for_comparison(None)
    assert result is None


def test_normalize_room_id_for_comparison_string() -> None:
    """Test normalize_room_id_for_comparison with string."""
    result = RoomIDUtils.normalize_room_id_for_comparison("room_001")
    assert result == "room_001"


def test_normalize_room_id_for_comparison_whitespace() -> None:
    """Test normalize_room_id_for_comparison strips whitespace."""
    result = RoomIDUtils.normalize_room_id_for_comparison("  room_001  ")
    assert result == "room_001"


def test_normalize_room_id_for_comparison_empty() -> None:
    """Test normalize_room_id_for_comparison returns None for empty string."""
    result = RoomIDUtils.normalize_room_id_for_comparison("")
    assert result is None


def test_check_normalized_ids_match() -> None:
    """Test check_normalized_ids_match returns True for matching IDs."""
    assert RoomIDUtils.check_normalized_ids_match("room_001", "room_001") is True


def test_check_normalized_ids_match_none() -> None:
    """Test check_normalized_ids_match returns False when either ID is None."""
    assert RoomIDUtils.check_normalized_ids_match(None, "room_001") is False
    assert RoomIDUtils.check_normalized_ids_match("room_001", None) is False
    assert RoomIDUtils.check_normalized_ids_match(None, None) is False


def test_check_normalized_room_matches() -> None:
    """Test check_normalized_room_matches checks all combinations."""
    assert RoomIDUtils.check_normalized_room_matches("room_001", "canonical_001", "room_001", "canonical_002") is True


def test_check_fallback_room_matches() -> None:
    """Test check_fallback_room_matches checks fallback matches."""
    assert RoomIDUtils.check_fallback_room_matches("room_001", None, "room_001", "canonical_001") is True
    assert RoomIDUtils.check_fallback_room_matches("room_001", "canonical_001", "room_002", "canonical_001") is True


def test_check_npc_room_match() -> None:
    """Test check_npc_room_match checks NPC room match."""
    mock_manager = MagicMock()
    mock_manager.canonical_room_id = MagicMock(return_value="canonical_001")
    utils = RoomIDUtils(mock_manager)
    result = utils.check_npc_room_match("room_001", None, "room_001", "canonical_001")
    assert result is True
