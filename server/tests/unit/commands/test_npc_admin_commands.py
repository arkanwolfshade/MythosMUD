"""
Unit tests for NPC admin command handlers.

Tests the NPC admin command functionality.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.npc_admin_commands import (
    handle_npc_command,
    handle_npc_create_command,
    handle_npc_delete_command,
    handle_npc_list_command,
    validate_npc_admin_permission,
)


@pytest.mark.asyncio
async def test_handle_npc_command_no_player_service():
    """Test handle_npc_command() when player service is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_npc_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_command_player_not_found():
    """Test handle_npc_command() when player is not found."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=None)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not found" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_command_no_permission():
    """Test handle_npc_command() when player lacks admin permission."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = False
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "permission" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_npc_command_no_args():
    """Test handle_npc_command() with no arguments."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Usage" in result["result"] or "subcommand" in result["result"].lower()


@pytest.mark.asyncio
async def test_validate_npc_admin_permission_no_player():
    """Test validate_npc_admin_permission() with no player."""
    result = validate_npc_admin_permission(None, "TestPlayer")
    assert result is False


@pytest.mark.asyncio
async def test_validate_npc_admin_permission_not_admin():
    """Test validate_npc_admin_permission() when player is not admin."""
    mock_player = MagicMock()
    mock_player.is_admin = False
    result = validate_npc_admin_permission(mock_player, "TestPlayer")
    assert result is False


@pytest.mark.asyncio
async def test_validate_npc_admin_permission_admin():
    """Test validate_npc_admin_permission() when player is admin."""
    mock_player = MagicMock()
    mock_player.is_admin = True
    result = validate_npc_admin_permission(mock_player, "TestPlayer")
    assert result is True


@pytest.mark.asyncio
async def test_handle_npc_create_command_no_args():
    """Test handle_npc_create_command() with no arguments."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_create_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Usage" in result["result"] or "name" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_npc_list_command():
    """Test handle_npc_list_command() lists NPCs."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.npc_admin_commands.npc_service") as mock_npc_service:
        mock_npc_service.list_npc_definitions.return_value = []
        result = await handle_npc_list_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result


@pytest.mark.asyncio
async def test_handle_npc_delete_command_no_args():
    """Test handle_npc_delete_command() with no arguments."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_npc_delete_command({}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Usage" in result["result"] or "name" in result["result"].lower()
