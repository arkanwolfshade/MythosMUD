"""
Unit tests for map API orchestration (server.api.maps).

Verifies that get_ascii_map / _prepare_ascii_map_context correctly omit unexplored
rooms for non-admin users when the exploration service is used (Codacy PR#421 r2861147548).
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from server.api.map_helpers import MapZoneContext
from server.api.maps import _prepare_ascii_map_context

# pylint: disable=redefined-outer-name  # Reason: pytest fixture names


@pytest.fixture
def mock_request() -> MagicMock:
    """Minimal request mock for map context."""
    req = MagicMock(spec=Request)
    req.query_params = MagicMock()
    req.query_params.get = MagicMock(return_value=None)
    return req


@pytest.fixture
def zone_context() -> MapZoneContext:
    """Standard zone for tests."""
    return MapZoneContext(plane="material", zone="arkham", sub_zone=None)


@pytest.fixture
def two_rooms() -> list[dict]:
    """Two rooms as returned by load_rooms_with_coordinates; one will be 'explored'."""
    return [
        {"id": "material_arkham_room_1", "name": "Explored Room", "map_x": 0, "map_y": 0, "exits": {}},
        {"id": "material_arkham_room_2", "name": "Unexplored Room", "map_x": 1, "map_y": 0, "exits": {}},
    ]


@pytest.fixture
def mock_user_and_player():
    """Fake user and player for authenticated flow."""
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    user = MagicMock()
    user.id = user_id
    player = MagicMock()
    player.id = player_id
    return user, player, player_id


@pytest.mark.asyncio
async def test_prepare_ascii_map_context_filters_unexplored_rooms_for_authenticated_user(
    mock_request: MagicMock,
    zone_context: MapZoneContext,
    two_rooms: list[dict],
    mock_user_and_player: tuple,
) -> None:
    """
    For an authenticated non-admin user, rooms not present in exploration_service
    are omitted from the payload (Codacy PR#421 r2861147548).
    """
    user, player, player_id = mock_user_and_player
    explored_only = [two_rooms[0]]  # only first room "explored"

    mock_session = AsyncMock(spec=AsyncSession)
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_user_id = AsyncMock(return_value=player)

    mock_exploration_service = MagicMock()
    mock_room_service = MagicMock()
    mock_room_service.filter_rooms_by_exploration = AsyncMock(return_value=explored_only)

    with (
        patch("server.api.maps.load_rooms_with_coordinates", new_callable=AsyncMock, return_value=two_rooms),
        patch("server.api.maps._get_current_room_id", new_callable=AsyncMock, return_value=None),
        patch(
            "server.api.maps._get_player_and_exploration_service",
            new_callable=AsyncMock,
            return_value=(player, player_id, mock_exploration_service),
        ),
        patch("server.api.maps._filter_explored_rooms", new_callable=AsyncMock, return_value=explored_only),
        patch(
            "server.api.maps._ensure_coordinates_generated",
            new_callable=AsyncMock,
            side_effect=lambda _s, _zc, rooms, *_a, **_k: rooms,
        ),
    ):
        rooms, current_room_id = await _prepare_ascii_map_context(
            request=mock_request,
            zone_context=zone_context,
            current_user=user,
            session=mock_session,
            persistence=mock_persistence,
            exploration_service=mock_exploration_service,
            room_service=mock_room_service,
        )

    assert len(rooms) == 1
    assert rooms[0]["id"] == "material_arkham_room_1"
    assert rooms[0]["name"] == "Explored Room"
    assert current_room_id is None
