"""Unit tests for player_respawn API endpoints."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.api.player_respawn import respawn_player, respawn_player_from_delirium
from server.exceptions import LoggedHTTPException, ValidationError


def _user():
    user = MagicMock()
    user.id = uuid.uuid4()
    user.username = "TestPlayer"
    return user


def _respawn_payload(room_id: str = "room_1") -> dict:
    return {
        "success": True,
        "player": {
            "id": str(uuid.uuid4()),
            "name": "TestPlayer",
            "dp": 100,
            "max_dp": 100,
            "current_room_id": room_id,
        },
        "room": {"id": room_id, "name": "Respawn Room", "description": "Safe"},
        "message": "Respawned",
    }


@pytest.mark.asyncio
async def test_respawn_player_success():
    user = _user()
    player_service = MagicMock()
    player_service.respawn_player_by_user_id = AsyncMock(return_value=_respawn_payload("r1"))
    respawn_service = MagicMock()
    persistence = MagicMock()

    async def _session_gen():
        session = AsyncMock()
        yield session

    with patch("server.database.get_async_session", return_value=_session_gen()):
        result = await respawn_player(
            MagicMock(),
            user,
            player_service,
            respawn_service,
            persistence,
        )
    assert result.success is True
    assert result.player.current_room_id == "r1"


@pytest.mark.asyncio
async def test_respawn_player_validation_error():
    user = _user()
    player_service = MagicMock()
    player_service.respawn_player_by_user_id = AsyncMock(side_effect=ValidationError("Player must be dead to respawn"))

    async def _session_gen():
        yield AsyncMock()

    with patch("server.database.get_async_session", return_value=_session_gen()):
        with pytest.raises(LoggedHTTPException) as exc:
            await respawn_player(MagicMock(), user, player_service, MagicMock(), MagicMock())
    assert exc.value.status_code == 403


@pytest.mark.asyncio
async def test_respawn_player_from_delirium_success():
    user = _user()
    player_service = MagicMock()
    player_service.respawn_player_from_delirium_by_user_id = AsyncMock(return_value=_respawn_payload("sanitarium"))

    async def _session_gen():
        yield AsyncMock()

    with patch("server.database.get_async_session", return_value=_session_gen()):
        result = await respawn_player_from_delirium(
            MagicMock(),
            user,
            player_service,
            MagicMock(),
            MagicMock(),
        )
    assert result.player.current_room_id == "sanitarium"


@pytest.mark.asyncio
async def test_respawn_player_from_delirium_not_found():
    user = _user()
    player_service = MagicMock()
    player_service.respawn_player_from_delirium_by_user_id = AsyncMock(side_effect=ValidationError("Player not found"))

    async def _session_gen():
        yield AsyncMock()

    with patch("server.database.get_async_session", return_value=_session_gen()):
        with pytest.raises(LoggedHTTPException) as exc:
            await respawn_player_from_delirium(MagicMock(), user, player_service, MagicMock(), MagicMock())
    assert exc.value.status_code == 404


@pytest.mark.asyncio
async def test_respawn_player_not_found():
    user = _user()
    player_service = MagicMock()
    player_service.respawn_player_by_user_id = AsyncMock(side_effect=ValidationError("Player not found"))

    async def _session_gen():
        yield AsyncMock()

    with patch("server.database.get_async_session", return_value=_session_gen()):
        with pytest.raises(LoggedHTTPException) as exc:
            await respawn_player(MagicMock(), user, player_service, MagicMock(), MagicMock())
    assert exc.value.status_code == 404


@pytest.mark.asyncio
async def test_respawn_player_unexpected_error():
    user = _user()
    player_service = MagicMock()
    player_service.respawn_player_by_user_id = AsyncMock(side_effect=RuntimeError("boom"))

    async def _session_gen():
        yield AsyncMock()

    with patch("server.database.get_async_session", return_value=_session_gen()):
        with pytest.raises(LoggedHTTPException) as exc:
            await respawn_player(MagicMock(), user, player_service, MagicMock(), MagicMock())
    assert exc.value.status_code == 500


@pytest.mark.asyncio
async def test_respawn_player_no_session():
    user = _user()
    player_service = MagicMock()

    async def _empty_gen():
        if False:
            yield AsyncMock()

    with patch("server.database.get_async_session", return_value=_empty_gen()):
        with pytest.raises(LoggedHTTPException) as exc:
            await respawn_player(MagicMock(), user, player_service, MagicMock(), MagicMock())
    assert exc.value.status_code == 500


@pytest.mark.asyncio
async def test_respawn_delirium_unexpected_error():
    user = _user()
    player_service = MagicMock()
    player_service.respawn_player_from_delirium_by_user_id = AsyncMock(side_effect=RuntimeError("boom"))

    async def _session_gen():
        yield AsyncMock()

    with patch("server.database.get_async_session", return_value=_session_gen()):
        with pytest.raises(LoggedHTTPException) as exc:
            await respawn_player_from_delirium(MagicMock(), user, player_service, MagicMock(), MagicMock())
    assert exc.value.status_code == 500
