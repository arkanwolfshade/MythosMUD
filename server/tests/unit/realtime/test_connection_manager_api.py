"""Unit tests for server.realtime.connection_manager_api."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime import connection_manager_api as cm_api


@pytest.fixture
def mock_manager() -> MagicMock:
    mgr = MagicMock()
    mgr.send_personal_message = AsyncMock(return_value={"ok": True})
    mgr.broadcast_global = AsyncMock(return_value={"ok": True})
    mgr.broadcast_to_room = AsyncMock(return_value={"ok": True})
    return mgr


@pytest.mark.asyncio
async def test_require_manager_raises_when_missing() -> None:
    with patch("server.realtime.connection_manager_api.resolve_connection_manager", return_value=None):
        with pytest.raises(RuntimeError, match="not available"):
            cm_api._require_manager()


@pytest.mark.asyncio
async def test_send_game_event_with_uuid(mock_manager: MagicMock) -> None:
    player_id = uuid.uuid4()
    with (
        patch("server.realtime.connection_manager_api.resolve_connection_manager", return_value=mock_manager),
        patch("server.realtime.envelope.build_event", return_value={"type": "x"}),
    ):
        await cm_api.send_game_event(player_id, "test_event", {"k": "v"})
    mock_manager.send_personal_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_game_event(mock_manager: MagicMock) -> None:
    with (
        patch("server.realtime.connection_manager_api.resolve_connection_manager", return_value=mock_manager),
        patch("server.realtime.envelope.build_event", return_value={"type": "x"}),
    ):
        await cm_api.broadcast_game_event("global", {"msg": "hi"}, exclude_player="p1")
    mock_manager.broadcast_global.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_room_event(mock_manager: MagicMock) -> None:
    with (
        patch("server.realtime.connection_manager_api.resolve_connection_manager", return_value=mock_manager),
        patch("server.realtime.envelope.build_event", return_value={"type": "x"}),
    ):
        await cm_api.send_room_event("room_1", "room_event", {"msg": "hi"})
    mock_manager.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_system_notification(mock_manager: MagicMock) -> None:
    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock) as sge:
        await cm_api.send_system_notification(uuid.uuid4(), "hello", "warning")
    sge.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_player_status_update(mock_manager: MagicMock) -> None:
    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock) as sge:
        await cm_api.send_player_status_update(uuid.uuid4(), {"hp": 10})
    sge.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_room_description(mock_manager: MagicMock) -> None:
    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock) as sge:
        await cm_api.send_room_description(uuid.uuid4(), {"name": "Foyer"})
    sge.assert_awaited_once()
