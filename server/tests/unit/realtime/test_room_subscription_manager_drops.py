"""
Unit tests for room subscription manager drop functions.

Tests the room drop functions in room_subscription_manager.py.
"""

import pytest

from server.realtime.room_subscription_manager import RoomSubscriptionManager


@pytest.fixture
def subscription_manager():
    """Create a RoomSubscriptionManager instance."""
    return RoomSubscriptionManager()


def test_list_room_drops(subscription_manager):
    """Test list_room_drops() returns defensive copy."""
    subscription_manager.room_drops["room_001"] = [{"item_id": "item_001", "quantity": 1}]
    result = subscription_manager.list_room_drops("room_001")
    assert len(result) == 1
    assert result[0]["item_id"] == "item_001"
    # Modify original to verify defensive copy
    subscription_manager.room_drops["room_001"][0]["quantity"] = 2
    assert result[0]["quantity"] == 1


def test_list_room_drops_empty(subscription_manager):
    """Test list_room_drops() returns empty list when no drops."""
    result = subscription_manager.list_room_drops("room_001")
    assert result == []


def test_add_room_drop(subscription_manager):
    """Test add_room_drop() adds drop to room."""
    stack = {"item_id": "item_001", "quantity": 1}
    subscription_manager.add_room_drop("room_001", stack)
    assert len(subscription_manager.room_drops["room_001"]) == 1
    assert subscription_manager.room_drops["room_001"][0]["item_id"] == "item_001"


def test_add_room_drop_invalid_quantity(subscription_manager):
    """Test add_room_drop() raises error for invalid quantity."""
    stack = {"item_id": "item_001", "quantity": 0}
    subscription_manager.add_room_drop("room_001", stack)
    # Should not add drop with invalid quantity
    assert (
        "room_001" not in subscription_manager.room_drops
        or len(subscription_manager.room_drops.get("room_001", [])) == 0
    )


def test_take_room_drop(subscription_manager):
    """Test take_room_drop() removes drop from room."""
    subscription_manager.room_drops["room_001"] = [{"item_id": "item_001", "quantity": 5}]
    result = subscription_manager.take_room_drop("room_001", 0, 3)
    assert result is not None
    assert result["quantity"] == 3
    assert subscription_manager.room_drops["room_001"][0]["quantity"] == 2


def test_take_room_drop_all(subscription_manager):
    """Test take_room_drop() removes entire stack when quantity >= available."""
    subscription_manager.room_drops["room_001"] = [{"item_id": "item_001", "quantity": 5}]
    result = subscription_manager.take_room_drop("room_001", 0, 5)
    assert result is not None
    assert result["quantity"] == 5
    assert "room_001" not in subscription_manager.room_drops


def test_take_room_drop_invalid_index(subscription_manager):
    """Test take_room_drop() returns None for invalid index."""
    subscription_manager.room_drops["room_001"] = [{"item_id": "item_001", "quantity": 5}]
    result = subscription_manager.take_room_drop("room_001", 10, 1)
    assert result is None


def test_adjust_room_drop(subscription_manager):
    """Test adjust_room_drop() adjusts quantity."""
    subscription_manager.room_drops["room_001"] = [{"item_id": "item_001", "quantity": 5}]
    result = subscription_manager.adjust_room_drop("room_001", 0, 3)
    assert result is True
    assert subscription_manager.room_drops["room_001"][0]["quantity"] == 3


def test_adjust_room_drop_remove(subscription_manager):
    """Test adjust_room_drop() removes stack when quantity is 0."""
    subscription_manager.room_drops["room_001"] = [{"item_id": "item_001", "quantity": 5}]
    result = subscription_manager.adjust_room_drop("room_001", 0, 0)
    assert result is True
    assert "room_001" not in subscription_manager.room_drops


def test_adjust_room_drop_invalid_index(subscription_manager):
    """Test adjust_room_drop() returns False for invalid index."""
    subscription_manager.room_drops["room_001"] = [{"item_id": "item_001", "quantity": 5}]
    result = subscription_manager.adjust_room_drop("room_001", 10, 3)
    assert result is False
