"""Unit tests for server.realtime.connection_manager_api."""

from __future__ import annotations

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime import connection_manager_api as cm_api


@pytest.fixture
def mock_manager() -> MagicMock:
    mgr = MagicMock()
    mgr.send_personal_message = AsyncMock(return_value={"ok": True})
    mgr.broadcast_global = AsyncMock(return_value={"ok": True})
    mgr.broadcast_to_room = AsyncMock(return_value={"ok": True})
    mgr.online_players = {}
    return mgr


@pytest.mark.asyncio
async def test_require_manager_raises_when_missing() -> None:
    with patch("server.realtime.connection_manager_api.resolve_connection_manager", return_value=None):
        with pytest.raises(RuntimeError, match="not available"):
            cm_api._require_manager()


def test_remove_online_player_pops_the_roster_entry(mock_manager: MagicMock) -> None:
    """#784 follow-up: deleting a connected character must drop it from the tick roster,
    or the game-tick loop keeps regenerating stats for it and the #777 soft-delete guard
    refuses every save -- one warning + full stack trace per tick, indefinitely."""
    player_id = uuid.uuid4()
    # mock_manager.online_players is a real dict (set by the fixture); the cast states that
    # honestly for basedpyright, which otherwise sees MagicMock attribute access as Any.
    online_players = cast("dict[uuid.UUID, dict[str, object]]", mock_manager.online_players)
    online_players[player_id] = {"name": "Doomed"}
    with patch("server.realtime.connection_manager_api.resolve_connection_manager", return_value=mock_manager):
        cm_api.remove_online_player(player_id)
    assert player_id not in online_players


def test_remove_online_player_is_a_noop_for_an_absent_player(mock_manager: MagicMock) -> None:
    with patch("server.realtime.connection_manager_api.resolve_connection_manager", return_value=mock_manager):
        cm_api.remove_online_player(uuid.uuid4())  # must not raise KeyError


def test_remove_online_player_is_a_noop_without_a_manager() -> None:
    """Unlike _require_manager(), a missing manager must not raise: deletion has to succeed
    in contexts with no live connection manager (unit tests, offline tooling, startup)."""
    with patch("server.realtime.connection_manager_api.resolve_connection_manager", return_value=None):
        cm_api.remove_online_player(uuid.uuid4())  # must not raise


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
