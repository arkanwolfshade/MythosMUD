"""
Unit tests for room subscription manager helper functions.

Tests the helper functions in room_subscription_manager.py.
"""

from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from server.realtime.room_subscription_manager import RoomSubscriptionManager


@pytest.fixture
def subscription_manager():
    """Create a RoomSubscriptionManager instance."""
    return RoomSubscriptionManager()


def test_remove_player_from_all_rooms(subscription_manager):
    """Test remove_player_from_all_rooms() removes player from all rooms."""
    subscription_manager.subscribe_to_room("player_001", "room_001")
    subscription_manager.subscribe_to_room("player_001", "room_002")
    subscription_manager.add_room_occupant("player_001", "room_001")
    result = subscription_manager.remove_player_from_all_rooms("player_001")
    assert result is True
    assert "player_001" not in subscription_manager.room_subscriptions.get("room_001", set())
    assert "player_001" not in subscription_manager.room_occupants.get("room_001", set())


def test_reconcile_room_presence(subscription_manager):
    """Test reconcile_room_presence() removes offline players."""
    subscription_manager.add_room_occupant("player_001", "room_001")
    subscription_manager.add_room_occupant("player_002", "room_001")
    online_players: dict[str, dict[str, Any]] = {"player_001": {}}
    result = subscription_manager.reconcile_room_presence("room_001", online_players)
    assert result is True
    assert "player_001" in subscription_manager.room_occupants["room_001"]
    assert "player_002" not in subscription_manager.room_occupants.get("room_001", set())


def test_canonical_room_id(subscription_manager):
    """Test _canonical_room_id() resolves canonical ID."""
    mock_persistence = MagicMock()
    mock_room = MagicMock()
    mock_room.id = "canonical_001"
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    subscription_manager.set_async_persistence(mock_persistence)
    result = subscription_manager._canonical_room_id("room_001")
    assert result == "canonical_001"


def test_canonical_room_id_no_persistence(subscription_manager):
    """Test _canonical_room_id() returns original when no persistence."""
    result = subscription_manager._canonical_room_id("room_001")
    assert result == "room_001"


def test_get_stats(subscription_manager):
    """Test get_stats() returns statistics."""
    subscription_manager.subscribe_to_room("player_001", "room_001")
    subscription_manager.add_room_occupant("player_001", "room_001")
    result = subscription_manager.get_stats()
    assert "total_rooms_with_subscriptions" in result
    assert "total_subscriptions" in result
    assert result["total_subscriptions"] == 1


def test_remove_player_from_all_rooms_no_subscriptions(subscription_manager):
    """Test remove_player_from_all_rooms() when player has no subscriptions."""
    result = subscription_manager.remove_player_from_all_rooms("player_001")
    assert result is True


def test_remove_player_from_all_rooms_with_subscriptions(subscription_manager):
    """Test remove_player_from_all_rooms() removes player from all rooms."""
    subscription_manager.subscribe_to_room("player_001", "room_001")
    subscription_manager.subscribe_to_room("player_001", "room_002")
    result = subscription_manager.remove_player_from_all_rooms("player_001")
    assert result is True
    assert "player_001" not in subscription_manager.room_subscriptions.get("room_001", set())
    assert "player_001" not in subscription_manager.room_subscriptions.get("room_002", set())


def test_remove_player_from_all_rooms_error(subscription_manager):
    """Test remove_player_from_all_rooms() handles errors gracefully."""
    subscription_manager.subscribe_to_room("player_001", "room_001")
    with patch("builtins.list", side_effect=Exception("List error")):
        result = subscription_manager.remove_player_from_all_rooms("player_001")
        assert result is False


def test_reconcile_room_presence_no_online_players(subscription_manager):
    """Test reconcile_room_presence() with no online players."""
    subscription_manager.add_room_occupant("player_001", "room_001")
    result = subscription_manager.reconcile_room_presence("room_001", {})
    assert result is True
    assert "player_001" not in subscription_manager.room_occupants.get("room_001", set())


def test_reconcile_room_presence_error(subscription_manager):
    """Test reconcile_room_presence() handles errors gracefully."""
    subscription_manager._canonical_room_id = MagicMock(side_effect=Exception("Test error"))
    result = subscription_manager.reconcile_room_presence("room_001", {})
    assert result is False


def test_canonical_room_id_none(subscription_manager):
    """Test _canonical_room_id() with None."""
    result = subscription_manager._canonical_room_id(None)
    assert result is None


def test_canonical_room_id_empty_string(subscription_manager):
    """Test _canonical_room_id() with empty string."""
    result = subscription_manager._canonical_room_id("")
    assert result == ""


def test_canonical_room_id_with_persistence(subscription_manager):
    """Test _canonical_room_id() resolves via persistence."""
    mock_persistence = MagicMock()
    mock_room = MagicMock()
    mock_room.id = "canonical_room_001"
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    subscription_manager.set_async_persistence(mock_persistence)
    result = subscription_manager._canonical_room_id("room_001")
    assert result == "canonical_room_001"


def test_canonical_room_id_no_room_id_attr(subscription_manager):
    """Test _canonical_room_id() returns original when room has no id."""
    mock_persistence = MagicMock()
    mock_room = MagicMock()
    del mock_room.id
    mock_persistence.get_room_by_id = MagicMock(return_value=mock_room)
    subscription_manager.set_async_persistence(mock_persistence)
    result = subscription_manager._canonical_room_id("room_001")
    assert result == "room_001"


def test_canonical_room_id_error(subscription_manager):
    """Test _canonical_room_id() handles errors gracefully."""
    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id = MagicMock(side_effect=Exception("Persistence error"))
    subscription_manager.set_async_persistence(mock_persistence)
    result = subscription_manager._canonical_room_id("room_001")
    assert result == "room_001"


def test_get_stats_empty(subscription_manager):
    """Test get_stats() returns stats for empty manager."""
    stats = subscription_manager.get_stats()
    assert isinstance(stats, dict)
    assert "total_rooms_with_subscriptions" in stats
    assert stats["total_rooms_with_subscriptions"] == 0


def test_get_stats_with_data(subscription_manager):
    """Test get_stats() returns stats with data."""
    subscription_manager.subscribe_to_room("player_001", "room_001")
    subscription_manager.add_room_occupant("player_001", "room_001")
    stats = subscription_manager.get_stats()
    assert isinstance(stats, dict)
    assert stats["total_rooms_with_subscriptions"] == 1
    assert stats["total_subscriptions"] == 1


def test_get_stats_error(subscription_manager):
    """Test get_stats() handles errors gracefully."""
    original_subscriptions = subscription_manager.room_subscriptions
    subscription_manager.room_subscriptions = MagicMock(side_effect=Exception("Access error"))
    try:
        result = subscription_manager.get_stats()
        assert isinstance(result, dict)
    finally:
        subscription_manager.room_subscriptions = original_subscriptions
