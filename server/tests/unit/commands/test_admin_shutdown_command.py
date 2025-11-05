"""
Tests for admin shutdown command.

This module tests the admin shutdown functionality including command validation,
parameter parsing, authorization checks, and the shutdown/cancel command logic.

As documented in the Necronomicon's appendices, proper termination rituals
are essential for maintaining the integrity of dimensional boundaries.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.admin_shutdown_command import (
    handle_shutdown_command,
    parse_shutdown_parameters,
    validate_shutdown_admin_permission,
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


class TestShutdownAdminPermissionValidation:
    """Test admin permission validation for shutdown command."""

    @pytest.mark.asyncio
    async def test_validate_shutdown_admin_permission_success(self):
        """Test successful admin permission validation."""
        mock_player = MagicMock()
        mock_player.is_admin = True

        result = await validate_shutdown_admin_permission(mock_player, "test_admin")

        assert result is True

    @pytest.mark.asyncio
    async def test_validate_shutdown_admin_permission_failure(self):
        """Test failed admin permission validation - non-admin player."""
        mock_player = MagicMock()
        mock_player.is_admin = False

        result = await validate_shutdown_admin_permission(mock_player, "test_user")

        assert result is False

    @pytest.mark.asyncio
    async def test_validate_shutdown_admin_permission_no_player(self):
        """Test admin permission validation with no player object."""
        result = await validate_shutdown_admin_permission(None, "test_user")

        assert result is False

    @pytest.mark.asyncio
    async def test_validate_shutdown_admin_permission_no_admin_attribute(self):
        """Test admin permission validation when player has no is_admin attribute."""
        mock_player = MagicMock(spec=[])  # Player without is_admin attribute

        result = await validate_shutdown_admin_permission(mock_player, "test_user")

        assert result is False


class TestShutdownParameterParsing:
    """Test parameter parsing for shutdown command."""

    def test_parse_shutdown_parameters_with_seconds(self):
        """Test parsing seconds parameter."""
        command_data = {"args": ["30"]}

        action, seconds = parse_shutdown_parameters(command_data)

        assert action == "initiate"
        assert seconds == 30

    def test_parse_shutdown_parameters_with_cancel(self):
        """Test parsing cancel parameter."""
        command_data = {"args": ["cancel"]}

        action, seconds = parse_shutdown_parameters(command_data)

        assert action == "cancel"
        assert seconds is None

    def test_parse_shutdown_parameters_default_seconds(self):
        """Test default seconds when no parameter provided."""
        command_data = {"args": []}

        action, seconds = parse_shutdown_parameters(command_data)

        assert action == "initiate"
        assert seconds == 10  # Default value

    def test_parse_shutdown_parameters_no_args_key(self):
        """Test parsing when args key is missing."""
        command_data = {}

        action, seconds = parse_shutdown_parameters(command_data)

        assert action == "initiate"
        assert seconds == 10  # Default value

    def test_parse_shutdown_parameters_invalid_number(self):
        """Test parsing invalid number parameter."""
        command_data = {"args": ["invalid"]}

        action, seconds = parse_shutdown_parameters(command_data)

        assert action == "error"
        assert seconds is None

    def test_parse_shutdown_parameters_negative_number(self):
        """Test parsing negative number parameter."""
        command_data = {"args": ["-10"]}

        action, seconds = parse_shutdown_parameters(command_data)

        assert action == "error"
        assert seconds is None

    def test_parse_shutdown_parameters_zero_seconds(self):
        """Test parsing zero seconds parameter."""
        command_data = {"args": ["0"]}

        action, seconds = parse_shutdown_parameters(command_data)

        assert action == "error"
        assert seconds is None

    def test_parse_shutdown_parameters_large_number(self):
        """Test parsing large valid number."""
        command_data = {"args": ["3600"]}  # 1 hour

        action, seconds = parse_shutdown_parameters(command_data)

        assert action == "initiate"
        assert seconds == 3600

    def test_parse_shutdown_parameters_case_insensitive_cancel(self):
        """Test that cancel is case insensitive."""
        for cancel_variant in ["cancel", "Cancel", "CANCEL", "CaNcEl"]:
            command_data = {"args": [cancel_variant]}

            action, seconds = parse_shutdown_parameters(command_data)

            assert action == "cancel"
            assert seconds is None


class TestShutdownCommand:
    """Test shutdown command functionality."""

    @pytest.mark.asyncio
    async def test_handle_shutdown_command_admin_initiate_default(self):
        """Test admin initiating shutdown with default countdown."""
        command_data = {"command_type": "shutdown", "args": []}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service
        mock_player_service = MagicMock()
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_admin_player)
        mock_app.state.player_service = mock_player_service

        # Mock task registry (properly consumes coroutines)
        mock_task_registry, mock_task = create_mock_task_registry()
        mock_app.state.task_registry = mock_task_registry

        # Mock connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.broadcast_global_event = AsyncMock()
        mock_app.state.connection_manager = mock_connection_manager

        # Initialize state attributes
        mock_app.state.server_shutdown_pending = False
        mock_app.state.shutdown_data = None

        result = await handle_shutdown_command(command_data, mock_current_user, mock_request, None, "admin_user")

        assert "result" in result
        assert "10" in result["result"]  # Default countdown
        assert "shutdown" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_handle_shutdown_command_admin_initiate_custom_seconds(self):
        """Test admin initiating shutdown with custom countdown."""
        command_data = {"command_type": "shutdown", "args": ["60"]}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service
        mock_player_service = MagicMock()
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_admin_player)
        mock_app.state.player_service = mock_player_service

        # Mock task registry (properly consumes coroutines)
        mock_task_registry, mock_task = create_mock_task_registry()
        mock_app.state.task_registry = mock_task_registry

        # Mock connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.broadcast_global_event = AsyncMock()
        mock_app.state.connection_manager = mock_connection_manager

        # Initialize state attributes
        mock_app.state.server_shutdown_pending = False
        mock_app.state.shutdown_data = None

        result = await handle_shutdown_command(command_data, mock_current_user, mock_request, None, "admin_user")

        assert "result" in result
        assert "60" in result["result"]
        assert "shutdown" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_handle_shutdown_command_admin_cancel(self):
        """Test admin canceling shutdown."""
        command_data = {"command_type": "shutdown", "args": ["cancel"]}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service
        mock_player_service = MagicMock()
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_admin_player)
        mock_app.state.player_service = mock_player_service

        # No active shutdown
        mock_app.state.shutdown_data = None

        result = await handle_shutdown_command(command_data, mock_current_user, mock_request, None, "admin_user")

        assert "result" in result
        assert "no active shutdown" in result["result"].lower() or "not" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_handle_shutdown_command_non_admin_denied(self):
        """Test non-admin player being denied shutdown command."""
        command_data = {"command_type": "shutdown", "args": []}
        mock_current_user = {"username": "regular_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service
        mock_player_service = MagicMock()
        mock_regular_player = MagicMock()
        mock_regular_player.is_admin = False
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_regular_player)
        mock_app.state.player_service = mock_player_service

        result = await handle_shutdown_command(command_data, mock_current_user, mock_request, None, "regular_user")

        assert "result" in result
        # Should contain thematic denial message
        assert any(
            keyword in result["result"].lower() for keyword in ["authorization", "permission", "clearance", "ritual"]
        )

    @pytest.mark.asyncio
    async def test_handle_shutdown_command_invalid_parameter(self):
        """Test shutdown command with invalid parameter."""
        command_data = {"command_type": "shutdown", "args": ["invalid"]}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service
        mock_player_service = MagicMock()
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_admin_player)
        mock_app.state.player_service = mock_player_service

        result = await handle_shutdown_command(command_data, mock_current_user, mock_request, None, "admin_user")

        assert "result" in result
        assert "invalid" in result["result"].lower() or "error" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_handle_shutdown_command_no_player_service(self):
        """Test shutdown command when player service unavailable."""
        command_data = {"command_type": "shutdown", "args": []}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app
        mock_app.state.player_service = None

        result = await handle_shutdown_command(command_data, mock_current_user, mock_request, None, "admin_user")

        assert "result" in result
        assert "not available" in result["result"].lower() or "unavailable" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_handle_shutdown_command_player_not_found(self):
        """Test shutdown command when player not found."""
        command_data = {"command_type": "shutdown", "args": []}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service returning None
        mock_player_service = MagicMock()
        mock_player_service.get_player_by_name = AsyncMock(return_value=None)
        mock_app.state.player_service = mock_player_service

        result = await handle_shutdown_command(command_data, mock_current_user, mock_request, None, "admin_user")

        assert "result" in result
        assert "not found" in result["result"].lower() or "unavailable" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_handle_shutdown_command_negative_seconds(self):
        """Test shutdown command with negative seconds."""
        command_data = {"command_type": "shutdown", "args": ["-5"]}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service
        mock_player_service = MagicMock()
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_admin_player)
        mock_app.state.player_service = mock_player_service

        result = await handle_shutdown_command(command_data, mock_current_user, mock_request, None, "admin_user")

        assert "result" in result
        assert "invalid" in result["result"].lower() or "positive" in result["result"].lower()
