# pyright: reportPrivateUsage=false
# Tests import players.py helpers that are module-private by convention.
"""Unit tests for server.api.players helpers and core list/create paths."""

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import Request

from server.api.players import (
    _disconnect_other_characters,
    _get_connection_manager,
    _validate_character_access,
    _validate_character_id,
    _validate_player_for_grace_period,
    create_player,
    get_class_description,
    list_players,
)
from server.exceptions import LoggedHTTPException, ValidationError


def _user() -> MagicMock:
    u = MagicMock()
    u.id = uuid.uuid4()
    return u


def test_get_class_description_known_and_fallback() -> None:
    assert "researcher" in get_class_description("investigator").lower()
    assert "unknown" in get_class_description("custom_unknown").lower()


def test_validate_character_id_accepts_uuid_string() -> None:
    u = _user()
    cid = str(uuid.uuid4())
    assert _validate_character_id(cid, MagicMock(spec=Request), u) == uuid.UUID(cid)


def test_validate_character_id_rejects_bad_format() -> None:
    u = _user()
    with pytest.raises(LoggedHTTPException) as ei:
        _ = _validate_character_id("not-a-uuid", MagicMock(spec=Request), u)
    assert ei.value.status_code == 400


def test_get_connection_manager_from_app_state() -> None:
    cm: MagicMock = MagicMock()
    container: MagicMock = MagicMock()
    container.connection_manager = cm
    state: MagicMock = MagicMock()
    state.container = container
    app: MagicMock = MagicMock()
    app.state = state
    req: MagicMock = MagicMock(spec=Request)
    req.app = app
    assert _get_connection_manager(req) is cm


def test_get_connection_manager_none_without_container() -> None:
    state: MagicMock = MagicMock()
    state.container = None
    app: MagicMock = MagicMock()
    app.state = state
    req: MagicMock = MagicMock(spec=Request)
    req.app = app
    assert _get_connection_manager(req) is None


@pytest.mark.asyncio
async def test_validate_character_access_success() -> None:
    char: MagicMock = MagicMock()
    svc: MagicMock = MagicMock()
    validate_m: AsyncMock = AsyncMock(return_value=(True, char, ""))
    svc.validate_character_access = validate_m
    result: MagicMock = cast(
        MagicMock,
        await _validate_character_access(uuid.uuid4(), _user(), MagicMock(spec=Request), svc),
    )
    assert result is char


@pytest.mark.asyncio
async def test_validate_character_access_not_found() -> None:
    svc = MagicMock()
    svc.validate_character_access = AsyncMock(return_value=(False, None, "Player not found here"))
    with pytest.raises(LoggedHTTPException) as ei:
        await _validate_character_access(uuid.uuid4(), _user(), MagicMock(spec=Request), svc)
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_validate_character_access_wrong_owner() -> None:
    svc = MagicMock()
    svc.validate_character_access = AsyncMock(return_value=(False, None, "Character does not belong to user"))
    with pytest.raises(LoggedHTTPException) as ei:
        await _validate_character_access(uuid.uuid4(), _user(), MagicMock(spec=Request), svc)
    assert ei.value.status_code == 403


@pytest.mark.asyncio
async def test_validate_player_for_grace_period_deleted() -> None:
    svc = MagicMock()
    svc.validate_character_access = AsyncMock(return_value=(False, None, "Character deleted"))
    with pytest.raises(LoggedHTTPException) as ei:
        await _validate_player_for_grace_period(uuid.uuid4(), _user(), MagicMock(spec=Request), svc)
    assert ei.value.status_code == 404


@pytest.mark.asyncio
async def test_disconnect_other_characters_no_manager() -> None:
    await _disconnect_other_characters(uuid.uuid4(), _user(), None, MagicMock())
    # no exception


@pytest.mark.asyncio
async def test_disconnect_other_characters_disconnects_peer() -> None:
    selected = uuid.uuid4()
    other = uuid.uuid4()
    other_char = MagicMock()
    other_char.id = other
    cm: MagicMock = MagicMock()
    cm.player_websockets = {other: MagicMock()}
    disconnect_ws: AsyncMock = AsyncMock()
    cm.disconnect_websocket = disconnect_ws
    svc: MagicMock = MagicMock()
    get_chars: AsyncMock = AsyncMock(return_value=[other_char])
    svc.get_user_characters = get_chars
    await _disconnect_other_characters(selected, _user(), cm, svc)
    disconnect_ws.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_player_success() -> None:
    svc = MagicMock()
    created = MagicMock()
    svc.create_player = AsyncMock(return_value=created)
    out = await create_player("Hero", MagicMock(spec=Request), "room_1", _user(), svc)
    assert out is created


@pytest.mark.asyncio
async def test_create_player_validation_error_to_400() -> None:
    svc = MagicMock()
    svc.create_player = AsyncMock(side_effect=ValidationError("bad name"))
    with pytest.raises(LoggedHTTPException) as ei:
        _ = await create_player("x", MagicMock(spec=Request), "room_1", _user(), svc)
    assert ei.value.status_code == 400


@pytest.mark.asyncio
async def test_list_players_requires_auth() -> None:
    svc = MagicMock()
    with pytest.raises(LoggedHTTPException) as ei:
        _ = await list_players(MagicMock(spec=Request), None, svc)
    assert ei.value.status_code == 401


@pytest.mark.asyncio
async def test_list_players_returns_list() -> None:
    svc = MagicMock()
    svc.list_players = AsyncMock(return_value=[MagicMock()])
    out = await list_players(MagicMock(spec=Request), _user(), svc)
    assert len(out) == 1
