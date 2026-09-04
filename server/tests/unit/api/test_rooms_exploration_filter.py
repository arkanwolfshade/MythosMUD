"""
Tests for room list exploration filtering vs admin bypass (server.api.rooms).

Non-admin users intersect filter_explored with exploration_service lookups; admins
receive the full room list when filter_explored is requested.
"""

# pyright: reportPrivateUsage=false
# Reason: Unit tests intentionally call rooms._apply_exploration_filter_if_needed.

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from server.api.rooms import _apply_exploration_filter_if_needed
from server.game.room_service import RoomService
from server.services.exploration_service import ExplorationService

# pylint: disable=redefined-outer-name  # pytest fixtures

# Room payloads in these tests only use str fields; object avoids reportAny on dict values.
RoomDictList = list[dict[str, object]]


@pytest.fixture
def sample_rooms() -> RoomDictList:
    """Two stable room dict rows (stable_id, name) for filter tests."""
    return [
        {"stable_id": "r1", "name": "One"},
        {"stable_id": "r2", "name": "Two"},
    ]


@pytest.mark.asyncio
async def test_apply_exploration_filter_superuser_bypasses_filter(sample_rooms: RoomDictList) -> None:
    """Superuser bypass matches admin: full room list without exploration intersection."""
    user = MagicMock()
    user.id = uuid.uuid4()
    user.is_admin = False
    user.is_superuser = True

    filter_mock: AsyncMock = AsyncMock()
    mock_room_service = MagicMock(spec=RoomService)
    mock_room_service.filter_rooms_by_exploration = filter_mock
    mock_persistence = AsyncMock()
    mock_session = AsyncMock(spec=AsyncSession)
    mock_exploration = MagicMock(spec=ExplorationService)

    out = await _apply_exploration_filter_if_needed(
        rooms=list(sample_rooms),
        filter_explored=True,
        current_user=user,
        room_service=mock_room_service,
        persistence=mock_persistence,
        exploration_service=mock_exploration,
        session=mock_session,
    )

    assert out == sample_rooms
    filter_mock.assert_not_called()


@pytest.mark.asyncio
async def test_apply_exploration_filter_admin_sees_all_rooms_when_filter_requested(
    sample_rooms: RoomDictList,
) -> None:
    """Admin / superuser bypasses exploration filter; room_service is not called."""
    user = MagicMock()
    user.id = uuid.uuid4()
    user.is_admin = True
    user.is_superuser = False

    filter_mock: AsyncMock = AsyncMock()
    mock_room_service = MagicMock(spec=RoomService)
    mock_room_service.filter_rooms_by_exploration = filter_mock

    get_player_mock: AsyncMock = AsyncMock()
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_user_id = get_player_mock
    mock_session = AsyncMock(spec=AsyncSession)
    mock_exploration = MagicMock(spec=ExplorationService)

    out = await _apply_exploration_filter_if_needed(
        rooms=list(sample_rooms),
        filter_explored=True,
        current_user=user,
        room_service=mock_room_service,
        persistence=mock_persistence,
        exploration_service=mock_exploration,
        session=mock_session,
    )

    assert out == sample_rooms
    filter_mock.assert_not_called()
    get_player_mock.assert_not_called()


@pytest.mark.asyncio
async def test_apply_exploration_filter_non_admin_uses_room_service_intersection(
    sample_rooms: RoomDictList,
) -> None:
    """Non-admin with player record gets filter_rooms_by_exploration(stable room rows)."""
    user = MagicMock()
    user.id = uuid.uuid4()
    user.is_admin = False
    user.is_superuser = False

    player_id = uuid.uuid4()
    player = MagicMock()
    player.player_id = str(player_id)

    filtered: RoomDictList = [sample_rooms[0]]
    filter_mock: AsyncMock = AsyncMock(return_value=filtered)
    mock_room_service = MagicMock(spec=RoomService)
    mock_room_service.filter_rooms_by_exploration = filter_mock

    get_player_mock: AsyncMock = AsyncMock(return_value=player)
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_user_id = get_player_mock
    mock_session = AsyncMock(spec=AsyncSession)
    mock_exploration = MagicMock(spec=ExplorationService)

    out = await _apply_exploration_filter_if_needed(
        rooms=list(sample_rooms),
        filter_explored=True,
        current_user=user,
        room_service=mock_room_service,
        persistence=mock_persistence,
        exploration_service=mock_exploration,
        session=mock_session,
    )

    assert out == filtered
    filter_mock.assert_awaited_once()
    call_args = filter_mock.await_args
    assert call_args is not None
    assert call_args[0][0] == sample_rooms
    assert call_args[0][1] == player_id


@pytest.mark.asyncio
async def test_apply_exploration_filter_no_player_returns_unfiltered(
    sample_rooms: RoomDictList,
) -> None:
    """If user has no linked player, exploration cannot run; unknown rooms list returned."""
    user = MagicMock()
    user.id = uuid.uuid4()
    user.is_admin = False
    user.is_superuser = False

    filter_mock: AsyncMock = AsyncMock()
    mock_room_service = MagicMock(spec=RoomService)
    mock_room_service.filter_rooms_by_exploration = filter_mock

    get_player_mock: AsyncMock = AsyncMock(return_value=None)
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_user_id = get_player_mock
    mock_session = AsyncMock(spec=AsyncSession)
    mock_exploration = MagicMock(spec=ExplorationService)

    out = await _apply_exploration_filter_if_needed(
        rooms=list(sample_rooms),
        filter_explored=True,
        current_user=user,
        room_service=mock_room_service,
        persistence=mock_persistence,
        exploration_service=mock_exploration,
        session=mock_session,
    )

    assert out == sample_rooms
    filter_mock.assert_not_called()
