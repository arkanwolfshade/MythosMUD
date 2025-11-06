"""
Tests for shutdown command audit logging.

This module tests that all shutdown events (initiation and cancellation)
are properly logged for administrative audit purposes.

As documented in the Miskatonic University Archives of Administrative Actions,
all invocations of forbidden shutdown rituals must be meticulously recorded.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.admin_shutdown_command import (
    cancel_shutdown_countdown,
    handle_shutdown_command,
    initiate_shutdown_countdown,
)


def create_mock_task_registry():
    """
    Create a mock task registry that properly consumes coroutines.

    This prevents "coroutine was never awaited" warnings by ensuring
    any coroutines passed to register_task are properly consumed.
    """
    mock_registry = MagicMock()
    mock_task = MagicMock()
    mock_task.cancel = MagicMock()
    mock_task.done = MagicMock(return_value=False)

    def register_task_side_effect(coro, *args, **kwargs):
        # Close the coroutine to prevent "never awaited" warning
        coro.close()
        return mock_task

    mock_registry.register_task.side_effect = register_task_side_effect
    return mock_registry, mock_task


class TestShutdownAuditLogging:
    """Test audit logging for shutdown command."""

    @pytest.mark.asyncio
    @patch("server.commands.admin_shutdown_command.admin_logger")
    async def test_shutdown_initiation_logs_to_audit(self, mock_admin_logger):
        """Test that shutdown initiation is logged to audit trail."""
        mock_app = MagicMock()
        mock_app.state.connection_manager = MagicMock()
        mock_app.state.connection_manager.broadcast_global_event = AsyncMock(return_value={"successful_deliveries": 5})

        # Mock task registry
        # Mock task registry (properly consumes coroutines)
        mock_task_registry, mock_task = create_mock_task_registry()
        mock_app.state.task_registry = mock_task_registry

        # No existing shutdown
        mock_app.state.server_shutdown_pending = False
        mock_app.state.shutdown_data = None

        await initiate_shutdown_countdown(mock_app, 60, "admin_user")

        # Verify audit log was called
        mock_admin_logger.log_admin_command.assert_called_once()
        call_args = mock_admin_logger.log_admin_command.call_args

        assert call_args.kwargs["admin_name"] == "admin_user"
        assert call_args.kwargs["command"] == "/shutdown"
        assert call_args.kwargs["success"] is True
        assert "countdown_seconds" in call_args.kwargs["additional_data"]
        assert call_args.kwargs["additional_data"]["countdown_seconds"] == 60

    @pytest.mark.asyncio
    @patch("server.commands.admin_shutdown_command.admin_logger")
    async def test_shutdown_superseding_logs_to_audit(self, mock_admin_logger):
        """Test that superseding shutdown is logged to audit trail."""
        mock_app = MagicMock()
        mock_app.state.connection_manager = MagicMock()
        mock_app.state.connection_manager.broadcast_global_event = AsyncMock(return_value={"successful_deliveries": 5})

        # Existing shutdown
        existing_task = MagicMock()
        existing_task.cancel = MagicMock()
        existing_task.done = MagicMock(return_value=False)
        mock_app.state.server_shutdown_pending = True
        mock_app.state.shutdown_data = {
            "countdown_seconds": 30,
            "admin_username": "old_admin",
            "task": existing_task,
        }

        # Mock task registry
        # Mock task registry (properly consumes coroutines)
        mock_task_registry, mock_task = create_mock_task_registry()
        mock_app.state.task_registry = mock_task_registry

        await initiate_shutdown_countdown(mock_app, 60, "new_admin")

        # Verify audit log was called for new shutdown
        mock_admin_logger.log_admin_command.assert_called_once()
        call_args = mock_admin_logger.log_admin_command.call_args

        assert call_args.kwargs["admin_name"] == "new_admin"
        assert call_args.kwargs["command"] == "/shutdown"
        assert call_args.kwargs["success"] is True
        assert call_args.kwargs["additional_data"]["countdown_seconds"] == 60
        assert "scheduled_time" in call_args.kwargs["additional_data"]

    @pytest.mark.asyncio
    @patch("server.commands.admin_shutdown_command.admin_logger")
    async def test_shutdown_cancellation_logs_to_audit(self, mock_admin_logger):
        """Test that shutdown cancellation is logged to audit trail."""
        mock_app = MagicMock()
        mock_app.state.connection_manager = MagicMock()
        mock_app.state.connection_manager.broadcast_global_event = AsyncMock(return_value={"successful_deliveries": 5})

        # Set up existing shutdown
        mock_task = MagicMock()
        mock_task.cancel = MagicMock()
        mock_task.done = MagicMock(return_value=False)
        mock_app.state.server_shutdown_pending = True
        mock_app.state.shutdown_data = {
            "countdown_seconds": 30,
            "admin_username": "original_admin",
            "start_time": 1000.0,
            "end_time": 1030.0,
            "task": mock_task,
        }

        await cancel_shutdown_countdown(mock_app, "cancelling_admin")

        # Verify audit log was called
        mock_admin_logger.log_admin_command.assert_called_once()
        call_args = mock_admin_logger.log_admin_command.call_args

        assert call_args.kwargs["admin_name"] == "cancelling_admin"
        assert call_args.kwargs["command"] == "/shutdown cancel"
        assert call_args.kwargs["success"] is True
        assert "remaining_seconds" in call_args.kwargs["additional_data"]
        assert "cancelled_at" in call_args.kwargs["additional_data"]

    @pytest.mark.asyncio
    @patch("server.commands.admin_shutdown_command.admin_logger")
    async def test_shutdown_cancellation_no_active_shutdown_logs_failure(self, mock_admin_logger):
        """Test that cancellation with no active shutdown logs failure."""
        mock_app = MagicMock()
        mock_app.state.server_shutdown_pending = False
        mock_app.state.shutdown_data = None

        result = await cancel_shutdown_countdown(mock_app, "admin_user")

        # Verify result is False
        assert result is False

        # Verify audit log was NOT called (no active shutdown to cancel)
        mock_admin_logger.log_admin_command.assert_not_called()

    @pytest.mark.asyncio
    @patch("server.commands.admin_shutdown_command.admin_logger")
    async def test_handle_shutdown_command_logs_initiation(self, mock_admin_logger):
        """Test that handle_shutdown_command logs shutdown initiation."""
        # Mock dependencies
        mock_app = MagicMock()
        mock_app.state.connection_manager = MagicMock()
        mock_app.state.connection_manager.broadcast_global_event = AsyncMock(return_value={"successful_deliveries": 5})
        mock_app.state.server_shutdown_pending = False
        mock_app.state.shutdown_data = None

        # Mock task registry (properly consumes coroutines)
        mock_task_registry, mock_task = create_mock_task_registry()
        mock_app.state.task_registry = mock_task_registry

        mock_request = MagicMock()
        mock_request.app = mock_app

        mock_player = MagicMock()
        mock_player.is_admin = True
        mock_player.name = "AdminPlayer"

        # Mock player service to return the player
        mock_player_service = MagicMock()
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.player_service = mock_player_service

        mock_current_user = MagicMock()
        mock_current_user.username = "admin_user"

        command_data = {"args": ["30"]}

        # Execute
        await handle_shutdown_command(command_data, mock_current_user, mock_request, MagicMock(), "AdminPlayer")

        # Verify audit log was called
        mock_admin_logger.log_admin_command.assert_called_once()
        call_args = mock_admin_logger.log_admin_command.call_args

        # Admin name should be the player_name, not current_user.username
        assert call_args.kwargs["admin_name"] == "AdminPlayer"
        assert call_args.kwargs["command"] == "/shutdown"
        assert call_args.kwargs["success"] is True
        assert call_args.kwargs["additional_data"]["countdown_seconds"] == 30

    @pytest.mark.asyncio
    @patch("server.commands.admin_shutdown_command.admin_logger")
    async def test_handle_shutdown_cancel_logs_cancellation(self, mock_admin_logger):
        """Test that handle_shutdown_command logs shutdown cancellation."""
        # Mock dependencies
        mock_app = MagicMock()
        mock_app.state.connection_manager = MagicMock()
        mock_app.state.connection_manager.broadcast_global_event = AsyncMock(return_value={"successful_deliveries": 5})

        # Set up existing shutdown
        mock_task = MagicMock()
        mock_task.cancel = MagicMock()
        mock_task.done = MagicMock(return_value=False)
        mock_app.state.server_shutdown_pending = True
        mock_app.state.shutdown_data = {
            "countdown_seconds": 30,
            "admin_username": "original_admin",
            "start_time": 1000.0,
            "end_time": 1030.0,
            "task": mock_task,
        }

        mock_request = MagicMock()
        mock_request.app = mock_app

        mock_player = MagicMock()
        mock_player.is_admin = True
        mock_player.name = "CancellingAdmin"

        # Mock player service to return the player
        mock_player_service = MagicMock()
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.player_service = mock_player_service

        mock_current_user = MagicMock()
        mock_current_user.username = "cancelling_admin_user"

        command_data = {"args": ["cancel"]}

        # Execute
        await handle_shutdown_command(command_data, mock_current_user, mock_request, MagicMock(), "CancellingAdmin")

        # Verify audit log was called
        mock_admin_logger.log_admin_command.assert_called_once()
        call_args = mock_admin_logger.log_admin_command.call_args

        # Admin name should be the player_name
        assert call_args.kwargs["admin_name"] == "CancellingAdmin"
        assert call_args.kwargs["command"] == "/shutdown cancel"
        assert call_args.kwargs["success"] is True

    @pytest.mark.asyncio
    @patch("server.commands.admin_shutdown_command.admin_logger")
    async def test_audit_log_includes_timestamp(self, mock_admin_logger):
        """Test that audit log includes timestamp information."""
        mock_app = MagicMock()
        mock_app.state.connection_manager = MagicMock()
        mock_app.state.connection_manager.broadcast_global_event = AsyncMock(return_value={"successful_deliveries": 5})
        mock_app.state.server_shutdown_pending = False
        mock_app.state.shutdown_data = None

        # Mock task registry (properly consumes coroutines)
        mock_task_registry, mock_task = create_mock_task_registry()
        mock_app.state.task_registry = mock_task_registry

        await initiate_shutdown_countdown(mock_app, 10, "admin_user")

        # Verify audit log was called
        assert mock_admin_logger.log_admin_command.called
        call_args = mock_admin_logger.log_admin_command.call_args

        # Verify scheduled_time is present (AdminActionsLogger adds its own timestamp)
        assert "scheduled_time" in call_args.kwargs["additional_data"]
        assert "countdown_seconds" in call_args.kwargs["additional_data"]

    @pytest.mark.asyncio
    @patch("server.commands.admin_shutdown_command.admin_logger")
    async def test_unauthorized_shutdown_not_logged(self, mock_admin_logger):
        """Test that unauthorized shutdown attempts are not logged to audit."""
        mock_app = MagicMock()
        mock_app.state.server_shutdown_pending = False
        mock_app.state.shutdown_data = None

        mock_request = MagicMock()
        mock_request.app = mock_app

        # Non-admin player
        mock_player = MagicMock()
        mock_player.is_admin = False
        mock_player.name = "RegularPlayer"

        # Mock player service to return the player
        mock_player_service = MagicMock()
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_app.state.player_service = mock_player_service

        mock_current_user = MagicMock()
        mock_current_user.username = "regular_user"

        command_data = {"args": ["30"]}

        # Execute
        result = await handle_shutdown_command(
            command_data, mock_current_user, mock_request, MagicMock(), "RegularPlayer"
        )

        # Verify unauthorized message returned
        assert "authorization" in result["result"].lower()

        # Verify audit log was NOT called for unauthorized attempt
        mock_admin_logger.log_admin_command.assert_not_called()
