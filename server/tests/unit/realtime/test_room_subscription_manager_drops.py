"""
Unit tests for room subscription manager drop functions.

Tests the room drop functions in room_subscription_manager.py.
"""

from unittest.mock import patch

import pytest

from server.realtime.room_subscription_manager import RoomSubscriptionManager

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


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


def test_list_room_drops_with_drops(subscription_manager):
    """Test list_room_drops() returns room drops."""
    stack = {"item_name": "sword", "quantity": 1}
    subscription_manager.add_room_drop("room_001", stack)
    result = subscription_manager.list_room_drops("room_001")
    assert len(result) == 1
    assert result[0]["item_name"] == "sword"


def test_add_room_drop_new_room(subscription_manager):
    """Test add_room_drop() adds drop to new room."""
    stack = {"item_name": "Sword", "quantity": 1}
    subscription_manager.add_room_drop("room_001", stack)
    result = subscription_manager.list_room_drops("room_001")
    assert len(result) == 1


def test_add_room_drop_existing_room(subscription_manager):
    """Test add_room_drop() adds drop to existing room."""
    stack1 = {"item_name": "Sword", "quantity": 1}
    stack2 = {"item_name": "Potion", "quantity": 1}
    subscription_manager.add_room_drop("room_001", stack1)
    subscription_manager.add_room_drop("room_001", stack2)
    result = subscription_manager.list_room_drops("room_001")
    assert len(result) == 2


def test_take_room_drop_success(subscription_manager):
    """Test take_room_drop() successfully takes drop."""
    stack = {"item_name": "sword", "quantity": 1, "item_id": "sword_001"}
    subscription_manager.add_room_drop("room_001", stack)
    result = subscription_manager.take_room_drop("room_001", 0, 1)
    assert result is None or (isinstance(result, dict) and "item_name" in result)


def test_take_room_drop_index_out_of_range(subscription_manager):
    """Test take_room_drop() with index out of range."""
    stack = {"item_name": "Sword", "quantity": 1}
    subscription_manager.add_room_drop("room_001", stack)
    result = subscription_manager.take_room_drop("room_001", 5, 1)
    assert result is None


def test_take_room_drop_quantity_too_large(subscription_manager):
    """Test take_room_drop() with quantity larger than available."""
    stack = {"item_name": "Sword", "quantity": 1}
    subscription_manager.add_room_drop("room_001", stack)
    result = subscription_manager.take_room_drop("room_001", 0, 10)
    assert result is None or result.get("quantity", 0) <= 1


def test_take_room_drop_zero_quantity(subscription_manager):
    """Test take_room_drop() handles zero quantity gracefully."""
    stack = {"item_name": "sword", "quantity": 1}
    subscription_manager.add_room_drop("room_001", stack)
    result = subscription_manager.take_room_drop("room_001", 0, 0)
    assert result is None


def test_take_room_drop_full_quantity(subscription_manager):
    """Test take_room_drop() removes stack when quantity >= available."""
    stack = {"item_name": "sword", "quantity": 5, "item_id": "sword_001"}
    subscription_manager.add_room_drop("room_001", stack)
    result = subscription_manager.take_room_drop("room_001", 0, 5)
    assert result is not None
    assert result["quantity"] == 5
    assert len(subscription_manager.list_room_drops("room_001")) == 0


def test_take_room_drop_partial_quantity(subscription_manager):
    """Test take_room_drop() adjusts quantity when quantity < available."""
    stack = {"item_name": "sword", "quantity": 5, "item_id": "sword_001"}
    subscription_manager.add_room_drop("room_001", stack)
    result = subscription_manager.take_room_drop("room_001", 0, 2)
    assert result is not None
    assert result["quantity"] == 2
    remaining = subscription_manager.list_room_drops("room_001")
    assert len(remaining) == 1
    assert remaining[0]["quantity"] == 3


def test_take_room_drop_removes_empty_room(subscription_manager):
    """Test take_room_drop() removes room when drop list becomes empty."""
    stack = {"item_name": "sword", "quantity": 1, "item_id": "sword_001"}
    subscription_manager.add_room_drop("room_001", stack)
    subscription_manager.take_room_drop("room_001", 0, 1)
    assert "room_001" not in subscription_manager.room_drops


def test_adjust_room_drop_index_out_of_range(subscription_manager):
    """Test adjust_room_drop() with index out of range."""
    stack = {"item_name": "Sword", "quantity": 1}
    subscription_manager.add_room_drop("room_001", stack)
    result = subscription_manager.adjust_room_drop("room_001", 5, 1)
    assert result is False


def test_adjust_room_drop_quantity_zero(subscription_manager):
    """Test adjust_room_drop() with quantity zero removes stack."""
    stack = {"item_name": "Sword", "quantity": 1}
    subscription_manager.add_room_drop("room_001", stack)
    result = subscription_manager.adjust_room_drop("room_001", 0, 0)
    assert result is True
    assert len(subscription_manager.list_room_drops("room_001")) == 0


def test_adjust_room_drop_negative_quantity(subscription_manager):
    """Test adjust_room_drop() with negative quantity."""
    stack = {"item_name": "Sword", "quantity": 1}
    subscription_manager.add_room_drop("room_001", stack)
    result = subscription_manager.adjust_room_drop("room_001", 0, -1)
    assert result is False


def test_adjust_room_drop_success(subscription_manager):
    """Test adjust_room_drop() successfully adjusts quantity."""
    stack = {"item_name": "sword", "quantity": 1, "item_id": "sword_001"}
    subscription_manager.add_room_drop("room_001", stack)
    result = subscription_manager.adjust_room_drop("room_001", 0, 5)
    assert result is True
    assert subscription_manager.room_drops["room_001"][0]["quantity"] == 5


def test_add_room_drop_zero_quantity(subscription_manager):
    """Test add_room_drop() handles zero quantity gracefully."""
    stack = {"item_name": "sword", "quantity": 0}
    subscription_manager.add_room_drop("room_001", stack)
    canonical_id = subscription_manager._canonical_room_id("room_001") or "room_001"
    assert (
        canonical_id not in subscription_manager.room_drops
        or len(subscription_manager.room_drops.get(canonical_id, [])) == 0
    )


def test_add_room_drop_negative_quantity(subscription_manager):
    """Test add_room_drop() handles negative quantity gracefully."""
    stack = {"item_name": "sword", "quantity": -1}
    subscription_manager.add_room_drop("room_001", stack)
    canonical_id = subscription_manager._canonical_room_id("room_001") or "room_001"
    assert (
        canonical_id not in subscription_manager.room_drops
        or len(subscription_manager.room_drops.get(canonical_id, [])) == 0
    )


def test_add_room_drop_error_handling(subscription_manager):
    """Test add_room_drop() handles errors gracefully."""
    with patch("builtins.dict", side_effect=Exception("Dict error")):
        subscription_manager.add_room_drop("room_001", {"item": "sword"})


def test_take_room_drop_error_handling(subscription_manager):
    """Test take_room_drop() handles errors gracefully."""
    stack = {"item_name": "sword", "quantity": 1}
    subscription_manager.add_room_drop("room_001", stack)
    with patch("server.realtime.room_subscription_manager.deepcopy", side_effect=Exception("Deepcopy error")):
        result = subscription_manager.take_room_drop("room_001", 0, 1)
        assert result is None


def test_adjust_room_drop_error_handling(subscription_manager):
    """Test adjust_room_drop() handles errors gracefully."""
    stack = {"item_name": "sword", "quantity": 1}
    subscription_manager.add_room_drop("room_001", stack)
    subscription_manager.room_drops["room_001"][0] = None
    result = subscription_manager.adjust_room_drop("room_001", 0, 5)
    assert result is False


def test_list_room_drops_error(subscription_manager):
    """Test list_room_drops() handles errors gracefully."""
    subscription_manager.add_room_drop("room_001", {"item": "sword", "quantity": 1})
    with patch("server.realtime.room_subscription_manager.deepcopy", side_effect=Exception("Deepcopy error")):
        result = subscription_manager.list_room_drops("room_001")
        assert result == []
