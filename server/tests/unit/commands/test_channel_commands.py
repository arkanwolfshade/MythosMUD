"""Unit tests for channel command handlers."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.commands.channel_commands import (
    _extract_channel_from_command,
    _get_persistence_and_player,
    _handle_default_channel_setting,
    _validate_channel_name,
    handle_channel_command,
)


@pytest.mark.asyncio
async def test_get_persistence_and_player_no_persistence():
    """Returns None pair when persistence is missing."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    request.app.state.persistence = None
    result = await _get_persistence_and_player(request, {"username": "alice"}, "alice")
    assert result == (None, None)


@pytest.mark.asyncio
async def test_get_persistence_and_player_not_found():
    """Returns None player when username does not resolve."""
    request = MagicMock()
    persistence = AsyncMock()
    persistence.get_player_by_name = AsyncMock(return_value=None)
    request.app = MagicMock()
    request.app.state = MagicMock()
    request.app.state.persistence = persistence

    result = await _get_persistence_and_player(request, {"username": "ghost"}, "ghost")
    assert result == (None, None)


def test_extract_channel_from_command_direct():
    """Reads channel from command_data channel field."""
    channel = _extract_channel_from_command({"channel": "Local"}, "alice")
    assert channel == "local"


def test_extract_channel_from_command_parsed_fallback():
    """Falls back to parsed_command.channel when direct field missing."""
    parsed = MagicMock()
    parsed.channel = "global"
    channel = _extract_channel_from_command({"parsed_command": parsed}, "alice")
    assert channel == "global"


def test_extract_channel_from_command_missing():
    """Returns None when channel cannot be resolved."""
    assert _extract_channel_from_command({}, "alice") is None


def test_validate_channel_name_invalid():
    """Invalid channel names return error dict."""
    result = _validate_channel_name("invalid")
    assert result is not None
    assert "Invalid channel" in result["result"]


@pytest.mark.asyncio
async def test_handle_channel_command_no_persistence():
    """handle_channel_command returns unavailable when persistence missing."""
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    request.app.state.persistence = None

    result = await handle_channel_command({}, {"username": "alice"}, request, None, "alice")
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_channel_command_usage_when_channel_missing():
    """handle_channel_command returns usage when channel is absent."""
    request = MagicMock()
    persistence = AsyncMock()
    player = MagicMock()
    player.player_id = uuid.uuid4()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    request.app = MagicMock()
    request.app.state = MagicMock()
    request.app.state.persistence = persistence

    result = await handle_channel_command({}, {"username": "alice"}, request, None, "alice")
    assert "Usage:" in result["result"]


@pytest.mark.asyncio
async def test_handle_channel_command_switch_valid_channel():
    """handle_channel_command acknowledges valid channel switch."""
    request = MagicMock()
    persistence = AsyncMock()
    player = MagicMock()
    player.player_id = uuid.uuid4()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    request.app = MagicMock()
    request.app.state = MagicMock()
    request.app.state.persistence = persistence

    result = await handle_channel_command({"channel": "whisper"}, {"username": "alice"}, request, None, "alice")
    assert "Switching to whisper channel" in result["result"]


@pytest.mark.asyncio
async def test_handle_default_channel_setting_success():
    """Default channel update commits and returns confirmation."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    session = AsyncMock()

    async def session_gen():
        yield session

    with patch("server.commands.channel_commands.get_async_session", return_value=session_gen()):
        with patch("server.commands.channel_commands.PlayerPreferencesService") as mock_prefs_cls:
            mock_prefs_cls.return_value.update_default_channel = AsyncMock(return_value={"success": True})
            result = await _handle_default_channel_setting({"action": "local"}, player, "alice")

    assert "Default channel set to local" in result["result"]
    session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_default_channel_setting_invalid_channel():
    """Default channel rejects invalid channel names."""
    player = MagicMock()
    result = await _handle_default_channel_setting({"action": "radio"}, player, "alice")
    assert "Invalid channel" in result["result"]


@pytest.mark.asyncio
async def test_handle_default_channel_setting_sqlalchemy_error():
    """Default channel rolls back and returns error on SQLAlchemy failure."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    session = AsyncMock()

    async def session_gen():
        yield session

    with patch("server.commands.channel_commands.get_async_session", return_value=session_gen()):
        with patch("server.commands.channel_commands.PlayerPreferencesService") as mock_prefs_cls:
            mock_prefs_cls.return_value.update_default_channel = AsyncMock(side_effect=SQLAlchemyError("db fail"))
            result = await _handle_default_channel_setting({"action": "local"}, player, "alice")

    assert "Error setting default channel" in result["result"]
    session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_channel_command_default_subcommand():
    """handle_channel_command routes default keyword to preference handler."""
    request = MagicMock()
    persistence = AsyncMock()
    player = MagicMock()
    player.player_id = uuid.uuid4()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    request.app = MagicMock()
    request.app.state = MagicMock()
    request.app.state.persistence = persistence

    with patch(
        "server.commands.channel_commands._handle_default_channel_setting",
        new=AsyncMock(return_value={"result": "Default channel set to global."}),
    ) as mock_default:
        result = await handle_channel_command(
            {"channel": "default", "action": "global"}, {"username": "alice"}, request, None, "alice"
        )

    mock_default.assert_awaited_once()
    assert "Default channel set" in result["result"]
