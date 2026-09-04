"""
Unit tests for system command handlers.

Tests the system command functionality.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.system_commands import handle_system_command


@pytest.mark.asyncio
async def test_handle_system_command():
    """Test handle_system_command() broadcasts system message."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_chat_service.send_system_message = AsyncMock(return_value={"success": True})
    mock_state.chat_service = mock_chat_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_system_command({"message": "System announcement"}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    mock_chat_service.send_system_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_system_command_no_message():
    """Test handle_system_command() handles missing message."""
    result = await handle_system_command({}, {}, MagicMock(), None, "TestPlayer")
    assert "result" in result
    assert "message" in result["result"].lower() or "usage" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_system_command_no_chat_service():
    """Test handle_system_command() handles missing chat service."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_system_command({"message": "Test"}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower()
