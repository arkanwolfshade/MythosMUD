"""Unit tests for websocket_handler_commands (parse tokens, validate player, resolve CM)."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.websocket_handler_commands import (
    parse_game_command_tokens,
    resolve_websocket_connection_manager,
    validate_player_and_persistence,
)


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
