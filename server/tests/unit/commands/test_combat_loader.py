"""Unit tests for combat_loader singleton and command entry points."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

import server.commands.combat_loader as combat_loader_mod
from server.commands.combat_loader import (
    _app_from_request,
    get_combat_command_handler,
    handle_attack_command,
    handle_flee_command,
    handle_kick_command,
    handle_punch_command,
    handle_strike_command,
    handle_taunt_command,
)


@pytest.fixture(autouse=True)
def reset_combat_handler():
    combat_loader_mod._combat_command_handler = None
    yield
    combat_loader_mod._combat_command_handler = None


def _mock_app_with_container():
    container = MagicMock()
    container.combat_service = MagicMock()
    container.event_bus = MagicMock()
    container.player_combat_service = MagicMock()
    container.connection_manager = MagicMock()
    container.async_persistence = MagicMock()
    state = MagicMock()
    state.container = container
    app = MagicMock()
    app.state = state
    return app


def test_get_combat_command_handler_requires_app():
    with pytest.raises(RuntimeError, match="without app instance"):
        get_combat_command_handler(None)


def test_get_combat_command_handler_creates_singleton():
    app = _mock_app_with_container()
    handler1 = get_combat_command_handler(app)
    handler2 = get_combat_command_handler(app)
    assert handler1 is handler2


def test_app_from_request_none():
    assert _app_from_request(None) is None


def test_app_from_request_returns_app():
    request = MagicMock()
    request.app = MagicMock()
    assert _app_from_request(request) is request.app


@pytest.mark.asyncio
async def test_handle_attack_command_delegates():
    app = _mock_app_with_container()
    request = MagicMock()
    request.app = app
    mock_handler = MagicMock()
    mock_handler.handle_attack_command = AsyncMock(return_value={"result": "You attack."})
    with patch.object(combat_loader_mod, "get_combat_command_handler", return_value=mock_handler):
        result = await handle_attack_command({}, {"name": "p"}, request, None, "p")
    assert result["result"] == "You attack."


@pytest.mark.asyncio
async def test_handle_punch_command_sets_type():
    app = _mock_app_with_container()
    request = MagicMock()
    request.app = app
    mock_handler = MagicMock()
    mock_handler.handle_attack_command = AsyncMock(return_value={"result": "punch"})
    with patch.object(combat_loader_mod, "get_combat_command_handler", return_value=mock_handler):
        await handle_punch_command({}, {"name": "p"}, request, None, "p")
    call_data = mock_handler.handle_attack_command.call_args[0][0]
    assert call_data["command_type"] == "punch"


@pytest.mark.asyncio
async def test_handle_kick_command_sets_type():
    app = _mock_app_with_container()
    request = MagicMock()
    request.app = app
    mock_handler = MagicMock()
    mock_handler.handle_attack_command = AsyncMock(return_value={"result": "kick"})
    with patch.object(combat_loader_mod, "get_combat_command_handler", return_value=mock_handler):
        await handle_kick_command({}, {"name": "p"}, request, None, "p")
    call_data = mock_handler.handle_attack_command.call_args[0][0]
    assert call_data["command_type"] == "kick"


@pytest.mark.asyncio
async def test_handle_strike_command_sets_type():
    app = _mock_app_with_container()
    request = MagicMock()
    request.app = app
    mock_handler = MagicMock()
    mock_handler.handle_attack_command = AsyncMock(return_value={"result": "strike"})
    with patch.object(combat_loader_mod, "get_combat_command_handler", return_value=mock_handler):
        await handle_strike_command({}, {"name": "p"}, request, None, "p")
    call_data = mock_handler.handle_attack_command.call_args[0][0]
    assert call_data["command_type"] == "strike"


@pytest.mark.asyncio
async def test_handle_flee_command_delegates():
    app = _mock_app_with_container()
    request = MagicMock()
    request.app = app
    mock_handler = MagicMock()
    mock_handler.handle_flee_command = AsyncMock(return_value={"result": "flee"})
    with patch.object(combat_loader_mod, "get_combat_command_handler", return_value=mock_handler):
        result = await handle_flee_command({}, {"name": "p"}, request, None, "p")
    assert result["result"] == "flee"


@pytest.mark.asyncio
async def test_handle_taunt_command_delegates():
    app = _mock_app_with_container()
    request = MagicMock()
    request.app = app
    mock_handler = MagicMock()
    mock_handler.handle_taunt_command = AsyncMock(return_value={"result": "taunt"})
    with patch.object(combat_loader_mod, "get_combat_command_handler", return_value=mock_handler):
        result = await handle_taunt_command({}, {"name": "p"}, request, None, "p")
    assert result["result"] == "taunt"
