"""Unit tests for server.api.rooms write endpoints (#627): properties and exit CRUD."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import Request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from server.api.rooms import (
    ExitCreateRequest,
    ExitUpdateRequest,
    RoomUpdateRequest,
    _build_exit_attributes,
    _create_room_link_in_db,
    _delete_room_link_in_db,
    _update_room_link_in_db,
    _update_room_properties_in_db,
    create_room_exit,
    delete_room_exit,
    update_room,
    update_room_exit,
)
from server.exceptions import LoggedHTTPException
from server.game.room_service import RoomService
from server.models.command_base import Direction


def _admin_user() -> MagicMock:
    user = MagicMock()
    user.id = uuid.uuid4()
    return user


def _bypass_admin_auth():
    return patch("server.api.rooms.get_admin_auth_service", return_value=MagicMock())


# -- _build_exit_attributes -------------------------------------------------


def test_build_exit_attributes_empty_when_nothing_set() -> None:
    assert _build_exit_attributes(None, None) == "{}"


def test_build_exit_attributes_includes_flags_and_description() -> None:
    import json

    payload = json.loads(_build_exit_attributes(["one_way"], "A narrow gap."))
    assert payload == {"flags": ["one_way"], "description": "A narrow gap."}


# -- _update_room_properties_in_db -------------------------------------------


@pytest.mark.asyncio
async def test_update_room_properties_in_db_success() -> None:
    session = AsyncMock(spec=AsyncSession)
    result = MagicMock()
    result.scalar.return_value = True
    session.execute = AsyncMock(return_value=result)
    updated = await _update_room_properties_in_db(session, "room_1", "New Name", None, "arena", True)
    assert updated is True
    session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_room_properties_in_db_not_found_does_not_commit() -> None:
    session = AsyncMock(spec=AsyncSession)
    result = MagicMock()
    result.scalar.return_value = False
    session.execute = AsyncMock(return_value=result)
    updated = await _update_room_properties_in_db(session, "missing", None, None, None, False)
    assert updated is False
    session.commit.assert_not_awaited()


# -- _create_room_link_in_db / _update_room_link_in_db / _delete_room_link_in_db --


@pytest.mark.asyncio
async def test_create_room_link_in_db_success() -> None:
    session = AsyncMock(spec=AsyncSession)
    result = MagicMock()
    result.scalar.return_value = True
    session.execute = AsyncMock(return_value=result)
    created = await _create_room_link_in_db(session, "room_1", "north", "room_2", "{}")
    assert created is True
    session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_room_link_in_db_not_found_does_not_commit() -> None:
    session = AsyncMock(spec=AsyncSession)
    result = MagicMock()
    result.scalar.return_value = False
    session.execute = AsyncMock(return_value=result)
    updated = await _update_room_link_in_db(session, "room_1", "north", None, None)
    assert updated is False
    session.commit.assert_not_awaited()


@pytest.mark.asyncio
async def test_delete_room_link_in_db_success() -> None:
    session = AsyncMock(spec=AsyncSession)
    result = MagicMock()
    result.scalar.return_value = True
    session.execute = AsyncMock(return_value=result)
    deleted = await _delete_room_link_in_db(session, "room_1", "north")
    assert deleted is True
    session.commit.assert_awaited_once()


# -- update_room endpoint -----------------------------------------------------


@pytest.mark.asyncio
async def test_update_room_room_missing_404() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(return_value=None)
    with _bypass_admin_auth():
        with pytest.raises(LoggedHTTPException) as ei:
            await update_room(
                "missing",
                RoomUpdateRequest(name="x"),
                MagicMock(spec=Request),
                current_user=_admin_user(),
                session=AsyncMock(spec=AsyncSession),
                room_service=room_service,
            )
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_update_room_invalid_environment_422() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(return_value={"id": "room_1", "name": "Foyer"})
    with _bypass_admin_auth():
        with pytest.raises(LoggedHTTPException) as ei:
            await update_room(
                "room_1",
                RoomUpdateRequest(environment="not_a_real_environment"),
                MagicMock(spec=Request),
                current_user=_admin_user(),
                session=AsyncMock(spec=AsyncSession),
                room_service=room_service,
            )
    assert ei.value.status_code == 422


@pytest.mark.asyncio
async def test_update_room_empty_string_environment_clears_to_none() -> None:
    """RoomUpdateRequest(environment='') must translate to NULL, not the literal empty string."""
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(return_value={"id": "room_1", "name": "Foyer"})
    room_service.room_cache = None
    with (
        _bypass_admin_auth(),
        patch(
            "server.api.rooms._update_room_properties_in_db", new_callable=AsyncMock, return_value=True
        ) as mock_update,
    ):
        response = await update_room(
            "room_1",
            RoomUpdateRequest(environment=""),
            MagicMock(spec=Request),
            current_user=_admin_user(),
            session=AsyncMock(spec=AsyncSession),
            room_service=room_service,
        )
    _session, room_id, name, description, environment, set_environment = mock_update.call_args.args
    assert (room_id, name, description, environment, set_environment) == ("room_1", None, None, None, True)
    assert response.environment is None


@pytest.mark.asyncio
async def test_update_room_success_returns_updated_fields() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(return_value={"id": "room_1", "name": "Foyer"})
    room_service.room_cache = None
    with (
        _bypass_admin_auth(),
        patch("server.api.rooms._update_room_properties_in_db", new_callable=AsyncMock, return_value=True),
    ):
        response = await update_room(
            "room_1",
            RoomUpdateRequest(name="New Foyer", environment="arena"),
            MagicMock(spec=Request),
            current_user=_admin_user(),
            session=AsyncMock(spec=AsyncSession),
            room_service=room_service,
        )
    assert response.name == "New Foyer"
    assert response.environment == "arena"


# -- create_room_exit endpoint -------------------------------------------------


@pytest.mark.asyncio
async def test_create_room_exit_source_room_missing_404() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(return_value=None)
    with _bypass_admin_auth():
        with pytest.raises(LoggedHTTPException) as ei:
            await create_room_exit(
                "missing",
                ExitCreateRequest(direction=Direction.NORTH, target_room_id="room_2"),
                MagicMock(spec=Request),
                current_user=_admin_user(),
                session=AsyncMock(spec=AsyncSession),
                room_service=room_service,
            )
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_create_room_exit_target_room_missing_404() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(side_effect=[{"id": "room_1"}, None])
    with _bypass_admin_auth():
        with pytest.raises(LoggedHTTPException) as ei:
            await create_room_exit(
                "room_1",
                ExitCreateRequest(direction=Direction.NORTH, target_room_id="missing"),
                MagicMock(spec=Request),
                current_user=_admin_user(),
                session=AsyncMock(spec=AsyncSession),
                room_service=room_service,
            )
    assert ei.value.status_code == 404
    assert ei.value.detail == "Target room not found"


@pytest.mark.asyncio
async def test_create_room_exit_duplicate_direction_409() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(side_effect=[{"id": "room_1"}, {"id": "room_2"}])
    session = AsyncMock(spec=AsyncSession)
    with (
        _bypass_admin_auth(),
        patch(
            "server.api.rooms._create_room_link_in_db",
            new_callable=AsyncMock,
            side_effect=IntegrityError("stmt", {}, Exception("unique_violation")),
        ),
    ):
        with pytest.raises(LoggedHTTPException) as ei:
            await create_room_exit(
                "room_1",
                ExitCreateRequest(direction=Direction.NORTH, target_room_id="room_2"),
                MagicMock(spec=Request),
                current_user=_admin_user(),
                session=session,
                room_service=room_service,
            )
    assert ei.value.status_code == 409
    session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_room_exit_success() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(side_effect=[{"id": "room_1"}, {"id": "room_2"}])
    room_service.room_cache = None
    with (
        _bypass_admin_auth(),
        patch("server.api.rooms._create_room_link_in_db", new_callable=AsyncMock, return_value=True),
    ):
        response = await create_room_exit(
            "room_1",
            ExitCreateRequest(direction=Direction.NORTH, target_room_id="room_2"),
            MagicMock(spec=Request),
            current_user=_admin_user(),
            session=AsyncMock(spec=AsyncSession),
            room_service=room_service,
        )
    assert response.direction == "north"
    assert response.target_room_id == "room_2"


# -- update_room_exit endpoint --------------------------------------------------


@pytest.mark.asyncio
async def test_update_room_exit_not_found_404() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(return_value={"id": "room_1"})
    with (
        _bypass_admin_auth(),
        patch("server.api.rooms._update_room_link_in_db", new_callable=AsyncMock, return_value=False),
    ):
        with pytest.raises(LoggedHTTPException) as ei:
            await update_room_exit(
                "room_1",
                Direction.SOUTH,
                ExitUpdateRequest(description="A new description."),
                MagicMock(spec=Request),
                current_user=_admin_user(),
                session=AsyncMock(spec=AsyncSession),
                room_service=room_service,
            )
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_update_room_exit_success() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.get_room = AsyncMock(return_value={"id": "room_1"})
    room_service.room_cache = None
    with (
        _bypass_admin_auth(),
        patch("server.api.rooms._update_room_link_in_db", new_callable=AsyncMock, return_value=True),
    ):
        response = await update_room_exit(
            "room_1",
            Direction.NORTH,
            ExitUpdateRequest(target_room_id="room_3"),
            MagicMock(spec=Request),
            current_user=_admin_user(),
            session=AsyncMock(spec=AsyncSession),
            room_service=room_service,
        )
    assert response.target_room_id == "room_3"


# -- delete_room_exit endpoint --------------------------------------------------


@pytest.mark.asyncio
async def test_delete_room_exit_not_found_404() -> None:
    room_service = MagicMock(spec=RoomService)
    with (
        _bypass_admin_auth(),
        patch("server.api.rooms._delete_room_link_in_db", new_callable=AsyncMock, return_value=False),
    ):
        with pytest.raises(LoggedHTTPException) as ei:
            await delete_room_exit(
                "room_1",
                Direction.WEST,
                MagicMock(spec=Request),
                current_user=_admin_user(),
                session=AsyncMock(spec=AsyncSession),
                room_service=room_service,
            )
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_delete_room_exit_success() -> None:
    room_service = MagicMock(spec=RoomService)
    room_service.room_cache = None
    with (
        _bypass_admin_auth(),
        patch("server.api.rooms._delete_room_link_in_db", new_callable=AsyncMock, return_value=True),
    ):
        response = await delete_room_exit(
            "room_1",
            Direction.WEST,
            MagicMock(spec=Request),
            current_user=_admin_user(),
            session=AsyncMock(spec=AsyncSession),
            room_service=room_service,
        )
    assert response.message == "Exit deleted successfully"
    assert response.target_room_id is None
