"""Unit tests for websocket_handler_commands (parse tokens, validate player, resolve CM)."""

# pyright: reportAny=false, reportUnknownMemberType=false
# WebSocket tests build nested MagicMock app/state graphs and inspect dynamic JSON dicts.

from __future__ import annotations

import uuid
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.websocket_handler_commands import (
    handle_game_command,
    parse_game_command_tokens,
    process_websocket_command,
    resolve_websocket_connection_manager,
    validate_player_and_persistence,
)

TEST_PLAYER_ID = uuid.UUID("12345678-1234-5678-1234-567812345678")
TEST_PLAYER_ID_STR = str(TEST_PLAYER_ID)


def test_parse_game_command_tokens_splits_string() -> None:
    assert parse_game_command_tokens("  look  north  ", None) == ("look", ["north"])


def test_parse_game_command_tokens_empty_returns_none() -> None:
    assert parse_game_command_tokens("   ", None) is None


def test_parse_game_command_tokens_explicit_args() -> None:
    assert parse_game_command_tokens("GET", ["1", "box"]) == ("get", ["1", "box"])


def test_resolve_websocket_connection_manager_uses_passed() -> None:
    cm = MagicMock()
    assert resolve_websocket_connection_manager(cm) is cm


def test_resolve_websocket_connection_manager_fallback_app_state() -> None:
    inner_cm = MagicMock()
    container = MagicMock()
    container.connection_manager = inner_cm
    state = MagicMock()
    state.container = container
    mock_app = MagicMock()
    mock_app.state = state
    with patch("server.main.app", mock_app):
        out = resolve_websocket_connection_manager(None)
    assert out is inner_cm


@pytest.mark.asyncio
async def test_validate_player_and_persistence_not_found() -> None:
    cm = MagicMock()
    cm.get_player = AsyncMock(return_value=None)
    pid = str(uuid.uuid4())
    player, err = await validate_player_and_persistence(cm, pid)
    assert player is None
    assert err == "Player not found"


@pytest.mark.asyncio
async def test_validate_player_and_persistence_missing_room_attr() -> None:
    cm = MagicMock()
    cm.get_player = AsyncMock(return_value=object())
    cm.async_persistence = MagicMock()
    pid = str(uuid.uuid4())
    player, err = await validate_player_and_persistence(cm, pid)
    assert player is None
    assert err == "Player data error"


@pytest.mark.asyncio
async def test_validate_player_and_persistence_no_persistence() -> None:
    cm = MagicMock()
    pl = MagicMock()
    pl.current_room_id = "r1"
    cm.get_player = AsyncMock(return_value=pl)
    cm.async_persistence = None
    pid = str(uuid.uuid4())
    player, err = await validate_player_and_persistence(cm, pid)
    assert player is None
    assert err == "Game system unavailable"


@pytest.mark.asyncio
async def test_validate_player_and_persistence_ok() -> None:
    cm = MagicMock()
    pl = MagicMock()
    pl.current_room_id = "r1"
    cm.get_player = AsyncMock(return_value=pl)
    cm.async_persistence = MagicMock()
    pid = str(uuid.uuid4())
    player, err = await validate_player_and_persistence(cm, pid)
    assert player is pl
    assert err is None


def _cm_with_player_and_app(pl: MagicMock) -> MagicMock:
    cm = MagicMock()
    cm.get_player = AsyncMock(return_value=pl)
    cm.async_persistence = MagicMock()
    mock_app_state = MagicMock()
    cm.app = MagicMock()
    cm.app.state = mock_app_state
    return cm


@pytest.mark.asyncio
async def test_process_websocket_command_attaches_room_state(tmp_path: Path) -> None:
    """Unified result with room_changed + room_id gets room_state from get_room_state_event."""
    pl = MagicMock()
    pl.current_room_id = "room_001"
    pl.name = "TestPlayer"
    cm = _cm_with_player_and_app(pl)
    get_room = AsyncMock(return_value={"display": "new_room"})
    player_handler = MagicMock()
    player_handler.get_room_state_event = get_room
    event_handler = MagicMock()
    event_handler.player_handler = player_handler
    cm.app.state.event_handler = event_handler

    aliases_dir = str(tmp_path / "aliases")
    with patch("server.config.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_config.game.aliases_dir = aliases_dir
        mock_get_config.return_value = mock_config
        with patch(
            "server.command_handler_unified.process_command_unified",
            new_callable=AsyncMock,
            return_value={
                "result": "You leave.",
                "room_changed": True,
                "room_id": "room-north-1",
            },
        ):
            with patch(
                "server.realtime.websocket_handler_app_state.resolve_and_setup_app_state_services",
                MagicMock(),
            ):
                result = await process_websocket_command("go", ["north"], TEST_PLAYER_ID_STR, cm)

    assert result.get("room_state") == {"display": "new_room"}
    get_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_websocket_command_room_state_get_room_fails_softly(tmp_path: Path) -> None:
    """TypeError from get_room_state_event leaves result without room_state."""
    pl = MagicMock()
    pl.current_room_id = "room_001"
    pl.name = "TestPlayer"
    cm = _cm_with_player_and_app(pl)
    get_room = AsyncMock(side_effect=TypeError("bad shape"))
    player_handler = MagicMock()
    player_handler.get_room_state_event = get_room
    cm.app.state.event_handler = MagicMock(player_handler=player_handler)

    aliases_dir = str(tmp_path / "aliases")
    with patch("server.config.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_config.game.aliases_dir = aliases_dir
        mock_get_config.return_value = mock_config
        with patch(
            "server.command_handler_unified.process_command_unified",
            new_callable=AsyncMock,
            return_value={"result": "moved", "room_changed": True, "room_id": "r2"},
        ):
            with patch(
                "server.realtime.websocket_handler_app_state.resolve_and_setup_app_state_services",
                MagicMock(),
            ):
                result = await process_websocket_command("go", ["e"], TEST_PLAYER_ID_STR, cm)

    assert "room_state" not in result


@pytest.mark.asyncio
async def test_process_websocket_command_room_changed_no_player_handler_skips_room_state(
    tmp_path: Path,
) -> None:
    pl = MagicMock()
    pl.current_room_id = "room_001"
    pl.name = "TestPlayer"
    cm = _cm_with_player_and_app(pl)
    cm.app.state.event_handler = None

    aliases_dir = str(tmp_path / "aliases")
    with patch("server.config.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_config.game.aliases_dir = aliases_dir
        mock_get_config.return_value = mock_config
        with patch(
            "server.command_handler_unified.process_command_unified",
            new_callable=AsyncMock,
            return_value={"result": "moved", "room_changed": True, "room_id": "r9"},
        ):
            with patch(
                "server.realtime.websocket_handler_app_state.resolve_and_setup_app_state_services",
                MagicMock(),
            ):
                result = await process_websocket_command("go", ["w"], TEST_PLAYER_ID_STR, cm)

    assert "room_state" not in result


@pytest.mark.asyncio
async def test_handle_game_command_empty_sends_invalid_error(mock_websocket: MagicMock) -> None:
    cm = MagicMock()
    await handle_game_command(mock_websocket, TEST_PLAYER_ID_STR, "   ", connection_manager=cm)
    mock_websocket.send_json.assert_awaited_once()
    sent = mock_websocket.send_json.await_args[0][0]
    assert isinstance(sent, dict)
    assert sent.get("error_type") is not None or sent.get("type") is not None


@pytest.mark.asyncio
async def test_handle_game_command_broadcasts_when_result_requests(
    mock_websocket: MagicMock,
    mock_ws_connection_manager: MagicMock,
    tmp_path: Path,
) -> None:
    room_uuid = uuid.uuid4()
    pl = MagicMock()
    pl.current_room_id = room_uuid
    pl.name = "BroadCaster"
    mock_ws_connection_manager.get_player = AsyncMock(return_value=pl)
    mock_ws_connection_manager.async_persistence = MagicMock()
    mock_ws_connection_manager.app = MagicMock()
    mock_ws_connection_manager.app.state = MagicMock()

    aliases_dir = str(tmp_path / "aliases")
    with patch("server.config.get_config") as mock_get_config:
        mock_config = MagicMock()
        mock_config.game.aliases_dir = aliases_dir
        mock_get_config.return_value = mock_config
        with patch(
            "server.command_handler_unified.process_command_unified",
            new_callable=AsyncMock,
            return_value={
                "result": "You say hello.",
                "broadcast": {"message": "hello"},
                "broadcast_type": "say",
            },
        ):
            with patch(
                "server.realtime.websocket_handler_app_state.resolve_and_setup_app_state_services",
                MagicMock(),
            ):
                await handle_game_command(
                    mock_websocket,
                    TEST_PLAYER_ID_STR,
                    "say hello",
                    connection_manager=mock_ws_connection_manager,
                )

    assert mock_websocket.send_json.await_count >= 1
    mock_ws_connection_manager.broadcast_to_room.assert_awaited_once()
