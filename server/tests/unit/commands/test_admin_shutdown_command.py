"""
Unit tests for admin shutdown command handler.

Tests the shutdown command functionality.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.admin_shutdown_command import handle_shutdown_command


@pytest.mark.asyncio
async def test_handle_shutdown_command_no_player_service():
    """Test handle_shutdown_command() when player service is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_shutdown_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_shutdown_command_player_not_found():
    """Test handle_shutdown_command() when player is not found."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player_service.get_player_by_name = AsyncMock(return_value=None)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_shutdown_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Unable to verify" in result["result"] or "credentials" in result["result"]


@pytest.mark.asyncio
async def test_handle_shutdown_command_no_permission():
    """Test handle_shutdown_command() when player lacks admin permission."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = False
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=False):
        result = await handle_shutdown_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "authorization" in result["result"] or "permission" in result["result"]


@pytest.mark.asyncio
async def test_handle_shutdown_command_invalid_parameters():
    """Test handle_shutdown_command() with invalid parameters."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("error", None)),
    ):
        result = await handle_shutdown_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Invalid shutdown parameters" in result["result"] or "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_shutdown_command_cancel():
    """Test handle_shutdown_command() with cancel action."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("cancel", None)),
        patch("server.commands.admin_shutdown_command.cancel_shutdown_countdown", return_value=True),
    ):
        result = await handle_shutdown_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "cancelled" in result["result"].lower() or "cancel" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_shutdown_command_cancel_no_active():
    """Test handle_shutdown_command() with cancel when no active shutdown."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("cancel", None)),
        patch("server.commands.admin_shutdown_command.cancel_shutdown_countdown", return_value=False),
    ):
        result = await handle_shutdown_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "no active shutdown" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_shutdown_command_initiate():
    """Test handle_shutdown_command() with initiate action."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_state.shutdown_data = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("initiate", 60)),
        patch("server.commands.admin_shutdown_command.initiate_shutdown_countdown", return_value=True),
    ):
        result = await handle_shutdown_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "shutdown" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_shutdown_command_initiate_superseding():
    """Test handle_shutdown_command() with initiate action superseding existing shutdown."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_state.shutdown_data = {"seconds": 30}
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("initiate", 60)),
        patch("server.commands.admin_shutdown_command.initiate_shutdown_countdown", return_value=True),
    ):
        result = await handle_shutdown_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "previous shutdown cancelled" in result["result"].lower() or "superseding" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_shutdown_command_initiate_no_seconds():
    """Test handle_shutdown_command() with initiate action but no seconds."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("initiate", None)),
    ):
        result = await handle_shutdown_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Invalid shutdown configuration" in result["result"] or "seconds" in result["result"]


@pytest.mark.asyncio
async def test_handle_shutdown_command_initiate_failure():
    """Test handle_shutdown_command() with initiate action that fails."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with (
        patch("server.commands.admin_shutdown_command.validate_shutdown_admin_permission", return_value=True),
        patch("server.commands.admin_shutdown_command.parse_shutdown_parameters", return_value=("initiate", 60)),
        patch("server.commands.admin_shutdown_command.initiate_shutdown_countdown", return_value=False),
    ):
        result = await handle_shutdown_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "error" in result["result"].lower() or "failed" in result["result"].lower()
