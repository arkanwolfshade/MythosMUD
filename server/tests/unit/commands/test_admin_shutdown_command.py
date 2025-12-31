"""
Unit tests for admin shutdown command handler.

Tests the shutdown command functionality.
"""

import time
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.admin_shutdown_command import (
    broadcast_shutdown_notification,
    calculate_notification_times,
    cancel_shutdown_countdown,
    get_shutdown_blocking_message,
    handle_shutdown_command,
    initiate_shutdown_countdown,
    is_shutdown_pending,
    parse_shutdown_parameters,
    validate_shutdown_admin_permission,
)


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


def test_is_shutdown_pending_true():
    """Test is_shutdown_pending() returns True when shutdown is pending."""
    mock_app = MagicMock()
    mock_app.state.server_shutdown_pending = True
    result = is_shutdown_pending(mock_app)
    assert result is True


def test_is_shutdown_pending_false():
    """Test is_shutdown_pending() returns False when shutdown is not pending."""
    mock_app = MagicMock()
    mock_app.state.server_shutdown_pending = False
    result = is_shutdown_pending(mock_app)
    assert result is False


def test_is_shutdown_pending_no_state():
    """Test is_shutdown_pending() returns False when app has no state."""
    mock_app = MagicMock()
    del mock_app.state
    result = is_shutdown_pending(mock_app)
    assert result is False


def test_get_shutdown_blocking_message_login():
    """Test get_shutdown_blocking_message() returns login message."""
    result = get_shutdown_blocking_message("login")
    assert "shutting down" in result.lower() or "try again" in result.lower()


def test_get_shutdown_blocking_message_character_creation():
    """Test get_shutdown_blocking_message() returns character creation message."""
    result = get_shutdown_blocking_message("character_creation")
    assert "character creation" in result.lower()


def test_get_shutdown_blocking_message_default():
    """Test get_shutdown_blocking_message() returns default message for unknown context."""
    result = get_shutdown_blocking_message("unknown_context")
    assert "shutting down" in result.lower()


@pytest.mark.asyncio
async def test_validate_shutdown_admin_permission_no_player():
    """Test validate_shutdown_admin_permission() returns False when player is None."""
    result = await validate_shutdown_admin_permission(None, "TestPlayer")
    assert result is False


@pytest.mark.asyncio
async def test_validate_shutdown_admin_permission_not_admin():
    """Test validate_shutdown_admin_permission() returns False when player is not admin."""
    mock_player = MagicMock()
    mock_player.is_admin = False
    result = await validate_shutdown_admin_permission(mock_player, "TestPlayer")
    assert result is False


@pytest.mark.asyncio
async def test_validate_shutdown_admin_permission_admin():
    """Test validate_shutdown_admin_permission() returns True when player is admin."""
    mock_player = MagicMock()
    mock_player.is_admin = True
    result = await validate_shutdown_admin_permission(mock_player, "TestPlayer")
    assert result is True


def test_calculate_notification_times_short():
    """Test calculate_notification_times() for short countdown."""
    result = calculate_notification_times(5)
    assert 5 in result
    assert 4 in result
    assert 3 in result
    assert 2 in result
    assert 1 in result
    assert len(result) == 5


def test_calculate_notification_times_long():
    """Test calculate_notification_times() for long countdown."""
    result = calculate_notification_times(60)
    # Should have final 10 seconds (1-10)
    assert all(i in result for i in range(1, 11))
    # Should have 10-second intervals (10, 20, 30, 40, 50, 60)
    assert 60 in result
    assert 50 in result
    assert 40 in result
    assert 30 in result
    assert 20 in result
    assert 10 in result


def test_calculate_notification_times_sorted():
    """Test calculate_notification_times() returns sorted descending."""
    result = calculate_notification_times(25)
    assert result == sorted(result, reverse=True)


@pytest.mark.asyncio
async def test_broadcast_shutdown_notification_success():
    """Test broadcast_shutdown_notification() successfully broadcasts."""
    mock_connection_manager = AsyncMock()
    mock_connection_manager.broadcast_global_event = AsyncMock()
    result = await broadcast_shutdown_notification(mock_connection_manager, 10)
    assert result is True
    mock_connection_manager.broadcast_global_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_broadcast_shutdown_notification_failure():
    """Test broadcast_shutdown_notification() handles errors."""
    mock_connection_manager = AsyncMock()
    mock_connection_manager.broadcast_global_event = AsyncMock(side_effect=OSError("Network error"))
    result = await broadcast_shutdown_notification(mock_connection_manager, 10)
    assert result is False


def test_parse_shutdown_parameters_no_args():
    """Test parse_shutdown_parameters() with no args defaults to 10 seconds."""
    action, seconds = parse_shutdown_parameters({})
    assert action == "initiate"
    assert seconds == 10


def test_parse_shutdown_parameters_cancel():
    """Test parse_shutdown_parameters() with cancel action."""
    action, seconds = parse_shutdown_parameters({"args": ["cancel"]})
    assert action == "cancel"
    assert seconds is None


def test_parse_shutdown_parameters_seconds():
    """Test parse_shutdown_parameters() with seconds."""
    action, seconds = parse_shutdown_parameters({"args": ["30"]})
    assert action == "initiate"
    assert seconds == 30


def test_parse_shutdown_parameters_invalid_negative():
    """Test parse_shutdown_parameters() with negative seconds."""
    action, seconds = parse_shutdown_parameters({"args": ["-5"]})
    assert action == "error"
    assert seconds is None


def test_parse_shutdown_parameters_invalid_zero():
    """Test parse_shutdown_parameters() with zero seconds."""
    action, seconds = parse_shutdown_parameters({"args": ["0"]})
    assert action == "error"
    assert seconds is None


def test_parse_shutdown_parameters_invalid_string():
    """Test parse_shutdown_parameters() with invalid string."""
    action, seconds = parse_shutdown_parameters({"args": ["invalid"]})
    assert action == "error"
    assert seconds is None


@pytest.mark.asyncio
async def test_cancel_shutdown_countdown_no_active():
    """Test cancel_shutdown_countdown() when no shutdown is active."""
    mock_app = MagicMock()
    mock_app.state.server_shutdown_pending = False
    result = await cancel_shutdown_countdown(mock_app, "TestAdmin")
    assert result is False


@pytest.mark.asyncio
async def test_cancel_shutdown_countdown_success():
    """Test cancel_shutdown_countdown() successfully cancels shutdown."""
    mock_app = MagicMock()
    mock_app.state.server_shutdown_pending = True
    mock_task = MagicMock()
    mock_task.done = MagicMock(return_value=False)
    mock_app.state.shutdown_data = {
        "task": mock_task,
        "end_time": time.time() + 60,
    }
    mock_app.state.connection_manager = AsyncMock()
    mock_app.state.connection_manager.broadcast_global_event = AsyncMock()
    result = await cancel_shutdown_countdown(mock_app, "TestAdmin")
    assert result is True
    assert mock_app.state.server_shutdown_pending is False


@pytest.mark.asyncio
async def test_initiate_shutdown_countdown_success():
    """Test initiate_shutdown_countdown() successfully initiates shutdown."""
    mock_app = MagicMock()
    mock_app.state.server_shutdown_pending = False
    mock_app.state.task_registry = MagicMock()
    mock_task = MagicMock()
    mock_app.state.task_registry.register_task = MagicMock(return_value=mock_task)
    result = await initiate_shutdown_countdown(mock_app, 60, "TestAdmin")
    assert result is True
    assert mock_app.state.server_shutdown_pending is True


@pytest.mark.asyncio
async def test_initiate_shutdown_countdown_supersedes():
    """Test initiate_shutdown_countdown() cancels existing shutdown."""
    mock_app = MagicMock()
    mock_app.state.server_shutdown_pending = True
    mock_existing_task = MagicMock()
    mock_existing_task.done = MagicMock(return_value=False)
    mock_app.state.shutdown_data = {"task": mock_existing_task}
    mock_app.state.task_registry = MagicMock()
    mock_new_task = MagicMock()
    mock_app.state.task_registry.register_task = MagicMock(return_value=mock_new_task)
    result = await initiate_shutdown_countdown(mock_app, 60, "TestAdmin")
    assert result is True
    mock_existing_task.cancel.assert_called_once()
