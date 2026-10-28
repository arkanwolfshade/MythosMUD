"""Unit tests for server.api.rooms_helpers.fetch_room_list and its RoomListQuery grouping.

fetch_room_list used to take the five /list query parameters positionally-by-keyword; they are
now grouped into RoomListQuery. These tests pin the mapping: every field must reach the room
service (or the exploration filter) under the right name, so a swapped or dropped field fails.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from server.api import rooms_helpers
from server.api.rooms_helpers import RoomListQuery
from server.exceptions import LoggedHTTPException
from server.game.room_service import RoomService
from server.schemas.rooms import RoomListResponse
from server.services.exploration_service import ExplorationService

if TYPE_CHECKING:
    from server.async_persistence import AsyncPersistenceLayer

_ROOMS: list[dict[str, object]] = [{"id": "r1", "stable_id": "r1", "name": "One", "description": "A room"}]


class _RecordingRoomService:
    """Typed stand-in that records list_rooms keyword arguments."""

    def __init__(self, *, fail: bool = False) -> None:
        self.list_calls: list[dict[str, object]] = []
        self._fail: bool = fail

    async def list_rooms(
        self, *, plane: str, zone: str, sub_zone: str | None, include_exits: bool
    ) -> list[dict[str, object]]:
        """Record the call and return one room, or raise when configured to fail."""
        self.list_calls.append({"plane": plane, "zone": zone, "sub_zone": sub_zone, "include_exits": include_exits})
        if self._fail:
            raise RuntimeError("room service down")
        return list(_ROOMS)


async def _call(service: _RecordingRoomService, query: RoomListQuery) -> RoomListResponse:
    # The persistence/exploration/session collaborators are only reached when the exploration
    # filter runs for a real user; with current_user=None it returns early, so placeholders do.
    return await rooms_helpers.fetch_room_list(
        query=query,
        current_user=None,
        room_service=cast(RoomService, cast(object, service)),
        persistence=cast("AsyncPersistenceLayer", cast(object, None)),
        exploration_service=cast(ExplorationService, cast(object, None)),
        session=cast(AsyncSession, cast(object, None)),
    )


@pytest.mark.asyncio
async def test_fetch_room_list_forwards_every_query_field(monkeypatch: pytest.MonkeyPatch) -> None:
    """Non-default values for every field, so any swap or drop in the mapping is visible."""
    seen_filter_flags: list[bool] = []

    async def recording_filter(
        rooms: list[dict[str, object]], filter_explored: bool, *_collaborators: object
    ) -> list[dict[str, object]]:
        seen_filter_flags.append(filter_explored)
        return rooms

    monkeypatch.setattr(rooms_helpers, "apply_exploration_filter_if_needed", recording_filter)
    service = _RecordingRoomService()

    response = await _call(
        service,
        RoomListQuery(plane="earth", zone="arkham", sub_zone="campus", include_exits=False, filter_explored=True),
    )

    assert service.list_calls == [{"plane": "earth", "zone": "arkham", "sub_zone": "campus", "include_exits": False}]
    assert seen_filter_flags == [True]
    assert (response.plane, response.zone, response.sub_zone, response.total) == ("earth", "arkham", "campus", 1)


@pytest.mark.asyncio
async def test_fetch_room_list_wraps_service_errors_as_500() -> None:
    """A room-service failure surfaces as the route's 500, not a raw exception."""
    service = _RecordingRoomService(fail=True)

    with pytest.raises(LoggedHTTPException) as exc_info:
        _ = await _call(
            service,
            RoomListQuery(plane="earth", zone="arkham", sub_zone=None, include_exits=True, filter_explored=False),
        )

    assert exc_info.value.status_code == 500
