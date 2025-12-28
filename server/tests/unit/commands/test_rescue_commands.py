"""
Unit tests for rescue command handlers.

Tests the rescue command functionality.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.rescue_commands import handle_rescue_command


@pytest.mark.asyncio
@patch("server.commands.rescue_commands.RescueService")
async def test_handle_rescue_command(mock_rescue_service_cls):
    """Test handle_rescue_command() delegates to RescueService."""
    mock_service = AsyncMock()
    mock_service.rescue.return_value = {"result": "rescued"}
    mock_rescue_service_cls.return_value = mock_service

    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock(persistence=MagicMock(), catatonia_registry=None)

    result = await handle_rescue_command(
        {"target": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )

    mock_rescue_service_cls.assert_called_once()
    mock_service.rescue.assert_awaited_once_with("OtherPlayer", {"name": "TestPlayer"}, "TestPlayer")
    assert result == {"result": "rescued"}


@pytest.mark.asyncio
async def test_handle_rescue_command_no_target():
    """Test handle_rescue_command() handles missing target."""
    result = await handle_rescue_command({}, {}, MagicMock(), None, "TestPlayer")
    assert "result" in result
    assert "target" in result["result"].lower() or "usage" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_rescue_command_no_persistence():
    """Test handle_rescue_command() handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_rescue_command({"target": "OtherPlayer"}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower()
