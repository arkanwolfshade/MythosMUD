"""
Unit tests for room subscription manager.

Tests the RoomSubscriptionManager class. Additional coverage:
- test_room_subscription_manager_drops.py: room drops
- test_room_subscription_manager_helpers.py: helpers, reconcile, remove_from_all, canonical_id, stats
- test_room_subscription_manager_npcs.py: NPC helpers and get_room_occupants with NPCs
"""

from unittest.mock import MagicMock

import pytest

from server.realtime.room_subscription_manager import RoomSubscriptionManager

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice
# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names must match fixture names


@pytest.fixture
def subscription_manager():
    """Create a RoomSubscriptionManager instance."""
    return RoomSubscriptionManager()


def test_room_subscription_manager_init(subscription_manager):
    """Test RoomSubscriptionManager initialization."""
    assert len(subscription_manager.room_subscriptions) == 0
    assert len(subscription_manager.room_occupants) == 0
    assert subscription_manager.async_persistence is None


def test_set_async_persistence(subscription_manager):
    """Test set_async_persistence() sets persistence layer."""
    mock_persistence = MagicMock()
    subscription_manager.set_async_persistence(mock_persistence)
    assert subscription_manager.async_persistence == mock_persistence


def test_subscribe_to_room(subscription_manager):
    """Test subscribe_to_room() subscribes player to room."""
    result = subscription_manager.subscribe_to_room("player_001", "room_001")
    assert result is True
    assert "player_001" in subscription_manager.room_subscriptions["room_001"]


def test_subscribe_to_room_multiple_players(subscription_manager):
    """Test subscribe_to_room() with multiple players."""
    subscription_manager.subscribe_to_room("player_001", "room_001")
    subscription_manager.subscribe_to_room("player_002", "room_001")
    assert len(subscription_manager.room_subscriptions["room_001"]) == 2


def test_unsubscribe_from_room(subscription_manager):
    """Test unsubscribe_from_room() unsubscribes player from room."""
    subscription_manager.subscribe_to_room("player_001", "room_001")
    result = subscription_manager.unsubscribe_from_room("player_001", "room_001")
    assert result is True
    assert "player_001" not in subscription_manager.room_subscriptions.get("room_001", set())


def test_unsubscribe_from_room_not_subscribed(subscription_manager):
    """Test unsubscribe_from_room() when player is not subscribed."""
    result = subscription_manager.unsubscribe_from_room("player_001", "room_001")
    assert result is True


def test_unsubscribe_from_room_removes_empty_room(subscription_manager):
    """Test unsubscribe_from_room() removes room when last subscriber leaves."""
    subscription_manager.subscribe_to_room("player_001", "room_001")
    subscription_manager.unsubscribe_from_room("player_001", "room_001")
    assert "room_001" not in subscription_manager.room_subscriptions


def test_subscribe_to_room_error(subscription_manager):
    """Test subscribe_to_room() handles errors gracefully."""
    subscription_manager._canonical_room_id = MagicMock(side_effect=TypeError("test error"))
    result = subscription_manager.subscribe_to_room("player_001", "room_001")
    assert result is False


def test_unsubscribe_from_room_error(subscription_manager):
    """Test unsubscribe_from_room() handles errors gracefully."""
    subscription_manager._canonical_room_id = MagicMock(side_effect=TypeError("test error"))
    result = subscription_manager.unsubscribe_from_room("player_001", "room_001")
    assert result is False


@pytest.mark.asyncio
async def test_get_room_subscribers(subscription_manager):
    """Test get_room_subscribers() returns subscribers."""
    subscription_manager.subscribe_to_room("player_001", "room_001")
    subscription_manager.subscribe_to_room("player_002", "room_001")
    result = await subscription_manager.get_room_subscribers("room_001")
    assert "player_001" in result
    assert "player_002" in result


@pytest.mark.asyncio
async def test_get_room_subscribers_empty(subscription_manager):
    """Test get_room_subscribers() returns empty set when no subscribers."""
    result = await subscription_manager.get_room_subscribers("room_001")
    assert result == set()


@pytest.mark.asyncio
async def test_get_room_subscribers_error(subscription_manager):
    """Test get_room_subscribers() handles errors gracefully."""
    subscription_manager._canonical_room_id = MagicMock(side_effect=Exception("Test error"))
    result = await subscription_manager.get_room_subscribers("room_001")
    assert result == set()


def test_add_room_occupant(subscription_manager):
    """Test add_room_occupant() adds occupant."""
    result = subscription_manager.add_room_occupant("player_001", "room_001")
    assert result is True
    assert "player_001" in subscription_manager.room_occupants["room_001"]


def test_add_room_occupant_multiple(subscription_manager):
    """Test add_room_occupant() with multiple occupants."""
    subscription_manager.add_room_occupant("player_001", "room_001")
    subscription_manager.add_room_occupant("player_002", "room_001")
    assert len(subscription_manager.room_occupants["room_001"]) == 2


def test_add_room_occupant_new_room(subscription_manager):
    """Test add_room_occupant() adds occupant to new room."""
    result = subscription_manager.add_room_occupant("player_001", "room_001")
    assert result is True
    assert "player_001" in subscription_manager.room_occupants.get("room_001", set())


def test_add_room_occupant_existing_room(subscription_manager):
    """Test add_room_occupant() adds occupant to existing room."""
    subscription_manager.add_room_occupant("player_001", "room_001")
    result = subscription_manager.add_room_occupant("player_002", "room_001")
    assert result is True
    assert len(subscription_manager.room_occupants.get("room_001", set())) == 2


def test_remove_room_occupant(subscription_manager):
    """Test remove_room_occupant() removes occupant."""
    subscription_manager.add_room_occupant("player_001", "room_001")
    result = subscription_manager.remove_room_occupant("player_001", "room_001")
    assert result is True
    assert "player_001" not in subscription_manager.room_occupants.get("room_001", set())


def test_remove_room_occupant_not_occupant(subscription_manager):
    """Test remove_room_occupant() when player is not an occupant."""
    result = subscription_manager.remove_room_occupant("player_001", "room_001")
    assert result is True


def test_remove_room_occupant_removes_empty_room(subscription_manager):
    """Test remove_room_occupant() removes room when last occupant leaves."""
    subscription_manager.add_room_occupant("player_001", "room_001")
    subscription_manager.remove_room_occupant("player_001", "room_001")
    assert "room_001" not in subscription_manager.room_occupants


def test_add_room_occupant_error_handling(subscription_manager):
    """Test add_room_occupant() handles errors gracefully."""
    subscription_manager._canonical_room_id = MagicMock(side_effect=TypeError("test error"))
    result = subscription_manager.add_room_occupant("player_001", "room_001")
    assert result is False


def test_remove_room_occupant_error_handling(subscription_manager):
    """Test remove_room_occupant() handles errors gracefully."""
    subscription_manager.add_room_occupant("player_001", "room_001")
    subscription_manager._canonical_room_id = MagicMock(side_effect=TypeError("test error"))
    result = subscription_manager.remove_room_occupant("player_001", "room_001")
    assert result is False


@pytest.mark.asyncio
async def test_get_room_occupants(subscription_manager):
    """Test get_room_occupants() returns occupants."""
    subscription_manager.add_room_occupant("player_001", "room_001")
    subscription_manager.add_room_occupant("player_002", "room_001")
    mock_player1 = MagicMock()
    mock_player1.player_id = "player_001"
    mock_player1.name = "Player1"
    mock_player2 = MagicMock()
    mock_player2.player_id = "player_002"
    mock_player2.name = "Player2"
    online_players = {"player_001": mock_player1, "player_002": mock_player2}
    result = await subscription_manager.get_room_occupants("room_001", online_players)
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_get_room_occupants_empty(subscription_manager):
    """Test get_room_occupants() returns empty list when no occupants."""
    result = await subscription_manager.get_room_occupants("room_001", {})
    assert result == []


@pytest.mark.asyncio
async def test_get_room_occupants_error(subscription_manager):
    """Test get_room_occupants() handles errors gracefully."""
    subscription_manager._canonical_room_id = MagicMock(side_effect=Exception("Test error"))
    result = await subscription_manager.get_room_occupants("room_001", {})
    assert result == []
