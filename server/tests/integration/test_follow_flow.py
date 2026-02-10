"""
Integration tests for follow feature.

Flow: Player A requests follow B; B accepts -> A follows B.
B moves -> A moves (same room transfer). B moves through restricted exit -> A's move fails,
A is auto-unfollowed and notified.
"""

# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures use same names as params

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.events.event_bus import EventBus
from server.events.event_types import PlayerEnteredRoom
from server.game.follow_service import FollowService


@pytest.fixture
def event_bus():
    """Real EventBus for integration."""
    return EventBus()


@pytest.fixture
def movement_service():
    """Mock MovementService; move_player returns True then we can set False for restricted exit."""
    m = MagicMock()
    m.move_player = AsyncMock(return_value=True)
    return m


@pytest.fixture
def user_manager():
    """Mock UserManager; not muted."""
    m = MagicMock()
    m.is_player_muted_async = AsyncMock(return_value=False)
    return m


@pytest.fixture
def connection_manager():
    """Mock ConnectionManager (optional for this flow)."""
    return MagicMock()


@pytest.fixture
def follow_service(event_bus, movement_service, user_manager, connection_manager):
    """FollowService wired to real EventBus and mock MovementService."""
    return FollowService(
        event_bus=event_bus,
        movement_service=movement_service,
        user_manager=user_manager,
        connection_manager=connection_manager,
    )


@pytest.mark.asyncio
async def test_follow_accept_then_move_propagates_then_restricted_exit_unfollows(
    follow_service, movement_service, user_manager
):
    """
    A requests follow B; B accepts. B moves room_a -> room_b: A moves too.
    B moves room_b -> room_c (restricted for A): A's move fails, A is auto-unfollowed.
    """
    player_a_id = str(uuid.uuid4())
    player_b_id = str(uuid.uuid4())
    room_a = "room_a"
    room_b = "room_b"
    room_c = "room_c"

    # A requests to follow B (player)
    user_manager.is_player_muted_async = AsyncMock(return_value=False)
    result = await follow_service.request_follow(player_a_id, player_b_id, "player", "Alice")
    assert result["success"] is True
    request_id = result.get("request_id")
    assert request_id is not None

    # B accepts
    accept_result = await follow_service.accept_follow(player_b_id, request_id)
    assert accept_result["success"] is True
    assert follow_service.get_following(player_a_id) == (player_b_id, "player")
    assert follow_service.get_followers(player_b_id) == [player_a_id]

    # B moves room_a -> room_b: FollowService should move A
    movement_service.move_player.reset_mock()
    movement_service.move_player = AsyncMock(return_value=True)
    event1 = PlayerEnteredRoom(
        player_id=player_b_id,
        room_id=room_b,
        from_room_id=room_a,
    )
    # Integration test must publish to bus to verify FollowService subscription and propagation
    follow_service._event_bus.publish(event1)  # pylint: disable=protected-access
    await asyncio.sleep(0.05)
    movement_service.move_player.assert_called_once_with(player_a_id, room_a, room_b)
    assert follow_service.get_following(player_a_id) == (player_b_id, "player")

    # B moves room_b -> room_c; A's move fails (restricted exit) -> A is unfollowed
    movement_service.move_player.reset_mock()
    movement_service.move_player = AsyncMock(return_value=False)
    event2 = PlayerEnteredRoom(
        player_id=player_b_id,
        room_id=room_c,
        from_room_id=room_b,
    )
    # Publish to bus to verify auto-unfollow on move failure
    follow_service._event_bus.publish(event2)  # pylint: disable=protected-access
    await asyncio.sleep(0.05)
    movement_service.move_player.assert_called_once_with(player_a_id, room_b, room_c)
    assert follow_service.get_following(player_a_id) is None
    assert follow_service.get_followers(player_b_id) == []
