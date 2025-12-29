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
    handle_npc_despawn_command,
    handle_npc_list_command,
    handle_npc_move_command,
    handle_npc_spawn_command,
    handle_npc_stats_command,
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


@pytest.mark.asyncio
async def test_handle_npc_create_command_invalid_type():
    """Test handle_npc_create_command() with invalid NPC type."""
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

    result = await handle_npc_create_command(
        {"args": ["create", "TestNPC", "invalid_type", "zone1", "room1"]}, {}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "Invalid NPC type" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_create_command_no_database():
    """Test handle_npc_create_command() when database is not available."""
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
    del mock_app.state.db_session_maker

    result = await handle_npc_create_command(
        {"args": ["create", "TestNPC", "passive_mob", "zone1", "room1"]}, {}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "not available" in result["result"] or "Database" in result["result"]


@pytest.mark.asyncio
async def test_handle_npc_spawn_command_no_args():
    """Test handle_npc_spawn_command() with no arguments."""
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

    result = await handle_npc_spawn_command({}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "Usage" in result["result"] or "name" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_npc_despawn_command_no_args():
    """Test handle_npc_despawn_command() with no arguments."""
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

    result = await handle_npc_despawn_command({}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "Usage" in result["result"] or "name" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_npc_move_command_no_args():
    """Test handle_npc_move_command() with no arguments."""
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

    result = await handle_npc_move_command({}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "Usage" in result["result"] or "name" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_npc_stats_command():
    """Test handle_npc_stats_command() displays NPC stats."""
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

    with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
        mock_service = MagicMock()
        mock_service.get_npc_instance = AsyncMock(return_value=None)
        mock_get_service.return_value = mock_service
        result = await handle_npc_stats_command({"args": ["stats", "npc_001"]}, {}, mock_request, None, "TestPlayer")
        assert "result" in result


@pytest.mark.asyncio
async def test_validate_npc_admin_permission_exception():
    """Test validate_npc_admin_permission() handles exceptions."""
    mock_player = MagicMock()
    # Make getattr raise an exception when checking is_admin
    def side_effect(*args, **kwargs):
        if args[0] == "is_admin":
            raise Exception("Test error")
        return MagicMock()

    mock_player.is_admin = property(side_effect)
    # Make hasattr return False to trigger the exception path
    with patch("builtins.hasattr", return_value=False):
        result = validate_npc_admin_permission(mock_player, "TestPlayer")
        assert result is False


@pytest.mark.asyncio
async def test_handle_npc_command_unknown_subcommand():
    """Test handle_npc_command() with unknown subcommand."""
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

    result = await handle_npc_command({"args": ["unknown"]}, {}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "Unknown" in result["result"] or "Usage" in result["result"]
