"""Unit tests for server.api.rooms helpers and endpoints."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from server.api.rooms import (
    RoomPositionUpdate,
    _invalidate_room_cache,
    _update_room_position_in_db,
    _validate_room_position_update,
    get_room,
    list_rooms,
    update_room_position,
)
from server.exceptions import LoggedHTTPException
from server.game.room_service import RoomService


@pytest.mark.asyncio
async def test_validate_room_position_update_requires_auth() -> None:
    with pytest.raises(LoggedHTTPException) as ei:
        _validate_room_position_update(None, "room_1", MagicMock(spec=Request))
    assert ei.value.status_code == 401


def test_validate_room_position_update_delegates_to_auth_service() -> None:
    user = MagicMock()
    req = MagicMock(spec=Request)
    auth = MagicMock()
    with patch("server.api.rooms.get_admin_auth_service", return_value=auth):
        _validate_room_position_update(user, "room_1", req)
    auth.validate_permission.assert_called_once()


@pytest.mark.asyncio
async def test_update_room_position_in_db_success() -> None:
    session = AsyncMock(spec=AsyncSession)
    result = MagicMock()
    result.rowcount = 1
    session.execute = AsyncMock(return_value=result)
    await _update_room_position_in_db(session, "room_1", 3, 4, MagicMock(spec=Request))
    session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_room_position_in_db_not_found() -> None:
    session = AsyncMock(spec=AsyncSession)
    result = MagicMock()
    result.rowcount = 0
    session.execute = AsyncMock(return_value=result)
    with pytest.raises(LoggedHTTPException) as ei:
        await _update_room_position_in_db(session, "missing", 1, 1, MagicMock(spec=Request))
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_invalidate_room_cache() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.room_cache = MagicMock()
    await _invalidate_room_cache(room_service, "room_1")
    room_service.room_cache.invalidate_room.assert_called_once_with("room_1")


@pytest.mark.asyncio
async def test_list_rooms_success() -> None:
    rooms = [{"id": "r1", "stable_id": "r1", "name": "One", "description": "A room"}]
    room_service = MagicMock(spec=RoomService)
    room_service.list_rooms = AsyncMock(return_value=rooms)
    with patch("server.api.rooms._apply_exploration_filter_if_needed", new_callable=AsyncMock, return_value=rooms):
        response = await list_rooms(
            MagicMock(spec=Request),
            plane="earth",
            zone="arkham",
            sub_zone=None,
            include_exits=True,
            filter_explored=False,
            current_user=None,
            session=AsyncMock(spec=AsyncSession),
            room_service=room_service,
            persistence=MagicMock(),
            exploration_service=MagicMock(),
        )
    assert response.total == 1
    assert response.plane == "earth"


@pytest.mark.asyncio
async def test_get_room_not_found() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(return_value=None)
    with pytest.raises(LoggedHTTPException) as ei:
        await get_room("missing", MagicMock(spec=Request), room_service=room_service)
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_get_room_success() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(
        return_value={"id": "r1", "stable_id": "r1", "name": "Foyer", "description": "Entry"}
    )
    response = await get_room("r1", MagicMock(spec=Request), room_service=room_service)
    assert response.name == "Foyer"


@pytest.mark.asyncio
async def test_update_room_position_room_missing() -> None:
    user = MagicMock()
    user.id = uuid.uuid4()
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(return_value=None)
    with (
        patch("server.api.rooms._validate_room_position_update"),
        patch("server.api.rooms.get_admin_auth_service", return_value=MagicMock(get_username=lambda _u: "admin")),
    ):
        with pytest.raises(LoggedHTTPException) as ei:
            await update_room_position(
                "missing",
                RoomPositionUpdate(map_x=1.0, map_y=2.0),
                MagicMock(spec=Request),
                current_user=user,
                session=AsyncMock(spec=AsyncSession),
                room_service=room_service,
            )
    assert ei.value.status_code == 404
