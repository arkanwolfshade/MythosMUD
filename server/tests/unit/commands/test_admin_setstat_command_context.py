"""
Unit tests for admin setstat context failures, logging, and notify posture.

Split from test_admin_setstat_command.py to stay under file-nloc limit.
"""

# pyright: reportPrivateUsage=false
# Reason: Unit tests intentionally call admin_setstat_command private helpers.

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.admin_setstat_command import _handle_admin_set_stat_command


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_case_insensitive_stat_names():
    """Test case-insensitive stat name handling."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = AsyncMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    mock_target_player.get_stats = MagicMock(return_value={"strength": 50})
    mock_target_player.set_stats = MagicMock()

    async def resolve_player_side_effect(name: str):
        if name == "AdminPlayer":
            return mock_current_player
        return mock_target_player

    mock_player_service.resolve_player_name = AsyncMock(side_effect=resolve_player_side_effect)
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_target_player)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["str", "TargetPlayer", "60"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Set TargetPlayer's str" in result["result"]

    mock_target_player.get_stats = MagicMock(return_value={"strength": 60})
    mock_target_player.set_stats = MagicMock()
    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "65"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Set TargetPlayer's STR" in result["result"]

    mock_target_player.get_stats = MagicMock(return_value={"strength": 65})
    mock_target_player.set_stats = MagicMock()
    result = await _handle_admin_set_stat_command(
        {"args": ["strength", "TargetPlayer", "70"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "Set TargetPlayer's strength" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_no_app_context():
    """Test handling when app context is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_no_user_manager():
    """Test handling when user manager is not available."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.user_manager = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_no_player_service():
    """Test handling when player service is not available."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_admin_set_stat_command_no_persistence():
    """Test handling when persistence layer is not available."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = AsyncMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_current_player)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_state.persistence = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"]


@pytest.mark.asyncio
@patch("server.commands.admin_setstat_support.get_admin_actions_logger")
async def test_handle_admin_set_stat_command_logging(mock_get_logger: MagicMock):
    """Test admin action logging."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = AsyncMock(return_value=True)
    mock_player_service = AsyncMock()
    mock_persistence = AsyncMock()
    mock_admin_logger = MagicMock()
    log_admin_command: MagicMock = MagicMock()
    mock_admin_logger.log_admin_command = log_admin_command
    mock_get_logger.return_value = mock_admin_logger
    mock_current_player = MagicMock()
    mock_current_player.id = uuid.uuid4()
    mock_target_player = MagicMock()
    mock_target_player.player_id = uuid.uuid4()
    mock_target_player.get_stats = MagicMock(return_value={"strength": 50})
    mock_target_player.set_stats = MagicMock()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_current_player, mock_target_player])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_target_player)
    mock_state.user_manager = mock_user_manager
    mock_state.player_service = mock_player_service
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    _ = await _handle_admin_set_stat_command(
        {"args": ["STR", "TargetPlayer", "75"]}, {"name": "AdminPlayer"}, mock_request, None, "AdminPlayer"
    )

    log_admin_command.assert_called_once()
    call_args = log_admin_command.call_args
    assert call_args is not None
    assert call_args.kwargs["admin_name"] == "AdminPlayer"
    assert "admin set STR TargetPlayer 75" in call_args.kwargs["command"]
    assert call_args.kwargs["success"] is True
    assert "target_player" in call_args.kwargs["additional_data"]
    assert "stat_name" in call_args.kwargs["additional_data"]
    assert "old_value" in call_args.kwargs["additional_data"]
    assert "new_value" in call_args.kwargs["additional_data"]


@pytest.mark.asyncio
async def test_notify_player_stat_change_dp_attaches_posture_message():
    """Admin DP notify attaches posture_message from emit_posture_change (M9)."""
    from server.commands.admin_setstat_command import AdminSetStatNotifyContext, _notify_player_stat_change

    mock_app: MagicMock = MagicMock()
    mock_state: MagicMock = MagicMock()
    mock_cm: MagicMock = MagicMock()
    send_personal_message: AsyncMock = AsyncMock()
    mock_cm.send_personal_message = send_personal_message
    mock_state.connection_manager = mock_cm
    mock_app.state = mock_state

    target_id = uuid.uuid4()
    target = MagicMock()
    target.player_id = target_id
    target.name = "TargetPlayer"
    target.current_room_id = "room-1"
    get_stats: MagicMock = MagicMock(return_value={"current_dp": 0, "position": "lying"})
    target.get_stats = get_stats

    with patch("server.commands.admin_setstat_command.emit_posture_change", new_callable=AsyncMock) as mock_emit:
        mock_emit.return_value = "You stretch out and lie down."
        await _notify_player_stat_change(
            AdminSetStatNotifyContext(
                app=mock_app,
                target_player_obj=target,
                stat_name_input="DP",
                old_value=20,
                value=0,
                warning_message="",
                range_warning="",
                stat_key="current_dp",
                previous_position="standing",
            )
        )

    mock_emit.assert_awaited_once()
    player_update = cast(dict[str, object], send_personal_message.call_args_list[-1].args[1])
    data = cast(dict[str, object], player_update.get("data", {}))
    assert data.get("posture_message") == "You stretch out and lie down."
