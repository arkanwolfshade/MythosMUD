"""
Unit tests for admin command handlers.

Tests the admin command handler functions.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.admin_commands import (
    handle_add_admin_command,
    handle_admin_command,
    handle_mute_command,
    handle_mute_global_command,
    handle_mutes_command,
    handle_unmute_command,
    handle_unmute_global_command,
)
from server.commands.admin_teleport_commands import handle_goto_command, handle_teleport_command


@pytest.mark.asyncio
async def test_handle_admin_command_status():
    """Test handle_admin_command() with status subcommand."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.id = uuid.uuid4()
    mock_player.is_admin = True
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_state.player_service = mock_player_service
    mock_state.user_manager = MagicMock()
    mock_state.user_manager.is_admin = MagicMock(return_value=True)
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_admin_command(
        {"subcommand": "status"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )

    assert "result" in result
    assert "ADMIN STATUS" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_command_time():
    """Test handle_admin_command() with time subcommand."""
    from datetime import UTC, datetime

    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_chronicle = MagicMock()
    mock_components = MagicMock()
    mock_components.daypart = "afternoon"
    mock_components.season = "autumn"
    mock_mythos_dt = datetime(1926, 10, 31, 14, 30, 0, tzinfo=UTC)
    mock_chronicle.get_current_mythos_datetime.return_value = mock_mythos_dt
    mock_chronicle.get_calendar_components.return_value = mock_components
    mock_state.holiday_service = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    with patch("server.commands.admin_commands.get_mythos_chronicle", return_value=mock_chronicle):
        result = await handle_admin_command(
            {"subcommand": "time"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
        )

    assert "result" in result
    assert "Mythos time" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_command_unknown():
    """Test handle_admin_command() with unknown subcommand."""
    result = await handle_admin_command(
        {"subcommand": "unknown"}, {"name": "TestPlayer"}, MagicMock(), None, "TestPlayer"
    )

    assert "result" in result
    assert "Unknown admin subcommand" in result["result"]


@pytest.mark.asyncio
async def test_handle_mute_command_no_user_manager():
    """Test handle_mute_command() when user manager is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_mute_command(
        {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_mute_command_no_target():
    """Test handle_mute_command() with no target player."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.user_manager = MagicMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_mute_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_mute_command_success():
    """Test handle_mute_command() successful execution."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.mute_player = MagicMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, mock_target_player])
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_mute_command(
        {"target_player": "OtherPlayer", "duration_minutes": 60},
        {"name": "TestPlayer"},
        mock_request,
        None,
        "TestPlayer",
    )

    assert "result" in result
    assert "muted" in result["result"].lower()
    mock_user_manager.mute_player.assert_called_once()


@pytest.mark.asyncio
async def test_handle_unmute_command_no_user_manager():
    """Test handle_unmute_command() when user manager is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_unmute_command(
        {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_unmute_command_no_target():
    """Test handle_unmute_command() with no target player."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.user_manager = MagicMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_unmute_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_unmute_command_success():
    """Test handle_unmute_command() successful execution."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.unmute_player = MagicMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, mock_target_player])
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_unmute_command(
        {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )

    assert "result" in result
    assert "unmuted" in result["result"].lower()
    mock_user_manager.unmute_player.assert_called_once()


@pytest.mark.asyncio
async def test_handle_mute_global_command_no_user_manager():
    """Test handle_mute_global_command() when user manager is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_mute_global_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_mute_global_command_success():
    """Test handle_mute_global_command() successful execution."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.mute_global = MagicMock(return_value=True)
    mock_state.user_manager = mock_user_manager
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_mute_global_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "activated" in result["result"].lower()
    mock_user_manager.mute_global.assert_called_once()


@pytest.mark.asyncio
async def test_handle_unmute_global_command_no_user_manager():
    """Test handle_unmute_global_command() when user manager is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_unmute_global_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_unmute_global_command_success():
    """Test handle_unmute_global_command() successful execution."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.unmute_global = MagicMock(return_value=True)
    mock_state.user_manager = mock_user_manager
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_unmute_global_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "deactivated" in result["result"].lower()
    mock_user_manager.unmute_global.assert_called_once()


@pytest.mark.asyncio
async def test_handle_add_admin_command_no_user_manager():
    """Test handle_add_admin_command() when user manager is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_add_admin_command(
        {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_add_admin_command_no_target():
    """Test handle_add_admin_command() with no target player."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.user_manager = MagicMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_add_admin_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_add_admin_command_success():
    """Test handle_add_admin_command() successful execution."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.add_admin = MagicMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, mock_target_player])
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_add_admin_command(
        {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )

    assert "result" in result
    assert "admin" in result["result"].lower()
    mock_user_manager.add_admin.assert_called_once()


@pytest.mark.asyncio
async def test_handle_mutes_command_no_user_manager():
    """Test handle_mutes_command() when user manager is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_mutes_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_mutes_command_success():
    """Test handle_mutes_command() successful execution."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.get_player_mutes = MagicMock(return_value=[])
    mock_state.user_manager = mock_user_manager
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_mutes_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "No active mutes" in result["result"]
    mock_user_manager.get_player_mutes.assert_called_once()


@pytest.mark.asyncio
async def test_handle_teleport_command_no_app():
    """Test handle_teleport_command() when app is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_teleport_command(
        {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_teleport_command_no_target():
    """Test handle_teleport_command() with no target player."""
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

    with patch("server.commands.admin_teleport_commands.validate_admin_permission", return_value=True):
        result = await handle_teleport_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_goto_command_no_app():
    """Test handle_goto_command() when app is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_goto_command(
        {"target_room": "room_001"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_goto_command_no_target():
    """Test handle_goto_command() with no target room."""
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

    with patch("server.commands.admin_teleport_commands.validate_admin_permission", return_value=True):
        result = await handle_goto_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "Usage" in result["result"]


@pytest.mark.asyncio
async def test_handle_mute_command_no_player_service():
    """Test handle_mute_command() when player service is not available."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.user_manager = MagicMock()
    mock_state.player_service = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_mute_command(
        {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_mute_command_current_player_not_found():
    """Test handle_mute_command() when current player is not found."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=None)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_mute_command(
        {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "not found" in result["result"]


@pytest.mark.asyncio
async def test_handle_mute_command_target_player_not_found():
    """Test handle_mute_command() when target player is not found."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_player_service = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, None])
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_mute_command(
        {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "not found" in result["result"]


@pytest.mark.asyncio
async def test_handle_mute_command_mute_failure():
    """Test handle_mute_command() when mute operation fails."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.mute_player = MagicMock(return_value=False)
    mock_player_service = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, mock_target_player])
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_mute_command(
        {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "failed" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_mute_command_exception():
    """Test handle_mute_command() handles exceptions."""
    from server.exceptions import DatabaseError

    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=DatabaseError("Database error"))
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_mute_command(
        {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "error" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_unmute_command_target_not_found():
    """Test handle_unmute_command() when target player is not found."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_player_service = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, None])
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_unmute_command(
        {"target_player": "OtherPlayer"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "not found" in result["result"]


@pytest.mark.asyncio
async def test_handle_mutes_command_with_mutes():
    """Test handle_mutes_command() when player has active mutes."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    from datetime import UTC, datetime, timedelta

    mock_mutes = [
        {
            "target_player": "Player1",
            "expires_at": (datetime.now(UTC) + timedelta(hours=1)).isoformat(),
            "reason": "Spam",
        },
        {"target_player": "Player2", "expires_at": None, "reason": "Harassment"},
    ]
    mock_user_manager.get_player_mutes = MagicMock(return_value=mock_mutes)
    mock_state.user_manager = mock_user_manager
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_mutes_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "Player1" in result["result"] or "Player2" in result["result"] or "mute" in result["result"].lower()
