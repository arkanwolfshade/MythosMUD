"""
Unit tests for room subscription manager helper functions.

Tests the helper functions in room_subscription_manager.py.
"""

from unittest.mock import MagicMock

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
    online_players = {"player_001": {}}
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
