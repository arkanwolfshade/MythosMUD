"""
Unit tests for emote command handlers.

Tests the emote command functionality.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.emote_commands import handle_emote_command


@pytest.mark.asyncio
async def test_handle_emote_command():
    """Test handle_emote_command() processes emote."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_chat_service.send_emote_message = AsyncMock(return_value={"success": True})
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_player.id = "player_id_001"
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.chat_service = mock_chat_service
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_emote_command({"action": "smiles"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    mock_chat_service.send_emote_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_emote_command_no_message():
    """Test handle_emote_command() handles missing message."""
    result = await handle_emote_command({}, {}, MagicMock(), None, "TestPlayer")
    assert "result" in result
    assert "message" in result["result"].lower() or "usage" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_emote_command_no_chat_service():
    """Test handle_emote_command() handles missing chat service."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_emote_command({"action": "smiles"}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower() or "functionality" in result["result"].lower()
