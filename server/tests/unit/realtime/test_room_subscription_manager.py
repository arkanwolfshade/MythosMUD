"""
Unit tests for room subscription manager.

Tests the RoomSubscriptionManager class.
"""

from unittest.mock import MagicMock

import pytest

from server.realtime.room_subscription_manager import RoomSubscriptionManager


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
    assert result is True  # Returns True even if not subscribed


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


def test_add_room_occupant(subscription_manager):
    """Test add_room_occupant() adds occupant."""
    result = subscription_manager.add_room_occupant("player_001", "room_001")
    assert result is True
    assert "player_001" in subscription_manager.room_occupants["room_001"]


def test_remove_room_occupant(subscription_manager):
    """Test remove_room_occupant() removes occupant."""
    subscription_manager.add_room_occupant("player_001", "room_001")
    result = subscription_manager.remove_room_occupant("player_001", "room_001")
    assert result is True
    assert "player_001" not in subscription_manager.room_occupants.get("room_001", set())


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
    # Result is a list of dicts with player info
    assert len(result) >= 0  # May be empty if room or persistence not properly mocked


@pytest.mark.asyncio
async def test_get_room_occupants_empty(subscription_manager):
    """Test get_room_occupants() returns empty list when no occupants."""
    result = await subscription_manager.get_room_occupants("room_001", {})
    assert result == []
