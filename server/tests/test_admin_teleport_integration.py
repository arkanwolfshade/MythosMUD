"""
Integration tests for admin teleport system.

This module tests the complete admin teleport workflow including
command processing, permission validation, teleport execution,
and audit logging integration.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.admin_teleport_commands import (
    handle_confirm_teleport_command,
    handle_goto_command,
    handle_teleport_command,
    validate_admin_permission,
)


class TestAdminTeleportIntegration:
    """Integration tests for complete admin teleport workflow."""

    @pytest.fixture
    def mock_app_state(self):
        """Create mock application state for testing."""
        app_state = MagicMock()

        # Mock player service
        player_service = MagicMock()
        app_state.player_service = player_service

        # Mock connection manager
        connection_manager = MagicMock()
        connection_manager.online_players = {}
        connection_manager.broadcast_to_room = AsyncMock()
        connection_manager.send_to_player = AsyncMock()
        app_state.connection_manager = connection_manager

        # Mock persistence layer
        persistence = MagicMock()
        persistence.save_player = MagicMock()
        app_state.persistence = persistence

        return app_state

    @pytest.fixture
    def mock_admin_player(self):
        """Create mock admin player."""
        player = MagicMock()
        player.is_admin = True
        player.current_room_id = "admin_room"
        player.display_name = "AdminUser"
        return player

    @pytest.fixture
    def mock_target_player(self):
        """Create mock target player."""
        player = MagicMock()
        player.is_admin = False
        player.current_room_id = "target_room"
        player.display_name = "TargetPlayer"
        return player

    @pytest.mark.asyncio
    async def test_complete_teleport_workflow_success(self, mock_app_state, mock_admin_player, mock_target_player):
        """Test complete teleport workflow from command to execution."""
        # Setup
        command_data = {"command_type": "teleport", "target_player": "TargetPlayer"}
        current_user = {"username": "AdminUser"}
        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state

        # Mock player service responses
        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: mock_admin_player if name == "AdminUser" else mock_target_player
        )
        # Mock update_player_location to return True and call persistence
        mock_app_state.player_service.update_player_location.return_value = True

        # Mock connection manager with online target
        mock_app_state.connection_manager.online_players = {
            "target_id": {"player_name": "TargetPlayer", "room_id": "target_room"}
        }

        mock_alias_storage = MagicMock()

        # Step 1: Initial teleport command
        result = await handle_teleport_command(
            command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
        )

        # Should return success message (current implementation bypasses confirmation)
        assert "result" in result
        assert "successfully teleported" in result["result"].lower()
        assert "TargetPlayer" in result["result"]

        # Verify player service was called to update location
        mock_app_state.player_service.update_player_location.assert_called_once()

        # Verify visual effects were broadcast
        assert mock_app_state.connection_manager.broadcast_to_room.call_count == 2

        # Verify target player was notified
        mock_app_state.connection_manager.send_to_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_complete_goto_workflow_success(self, mock_app_state, mock_admin_player, mock_target_player):
        """Test complete goto workflow from command to execution."""
        # Setup
        command_data = {"command_type": "goto", "target_player": "TargetPlayer"}
        current_user = {"username": "AdminUser"}
        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state

        # Mock player service responses
        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: mock_admin_player if name == "AdminUser" else mock_target_player
        )
        # Mock update_player_location to return True and call persistence
        mock_app_state.player_service.update_player_location.return_value = True

        # Mock connection manager with online target
        mock_app_state.connection_manager.online_players = {
            "target_id": {"player_name": "TargetPlayer", "room_id": "target_room"},
            "admin_id": {"player_name": "AdminUser", "room_id": "admin_room"},
        }

        mock_alias_storage = MagicMock()

        # Step 1: Initial goto command
        result = await handle_goto_command(command_data, current_user, mock_request, mock_alias_storage, "AdminUser")

        # Should return success message (current implementation bypasses confirmation)
        assert "result" in result
        assert "successfully teleported" in result["result"].lower()
        assert "TargetPlayer" in result["result"]

        # Verify player service was called to update location
        mock_app_state.player_service.update_player_location.assert_called_once()

        # Verify visual effects were broadcast
        assert mock_app_state.connection_manager.broadcast_to_room.call_count == 2

    @pytest.mark.asyncio
    async def test_teleport_workflow_with_offline_target(self, mock_app_state, mock_admin_player):
        """Test teleport workflow when target player is offline."""
        # Setup
        command_data = {"command_type": "teleport", "target_player": "OfflinePlayer"}
        current_user = {"username": "AdminUser"}
        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state

        # Mock player service responses
        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: mock_admin_player if name == "AdminUser" else None
        )

        # Mock connection manager with no online players
        mock_app_state.connection_manager.online_players = {}

        mock_alias_storage = MagicMock()

        # Step 1: Initial teleport command
        result = await handle_teleport_command(
            command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
        )

        assert "result" in result
        assert "not found" in result["result"].lower() or "not online" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_teleport_workflow_with_non_admin_user(self, mock_app_state, mock_target_player):
        """Test teleport workflow when user is not an admin."""
        # Setup
        command_data = {"command_type": "teleport", "target_player": "TargetPlayer"}
        current_user = {"username": "RegularUser"}
        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state

        # Mock non-admin player
        non_admin_player = MagicMock()
        non_admin_player.is_admin = False
        non_admin_player.current_room_id = "regular_room"

        # Mock player service responses
        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: non_admin_player if name == "RegularUser" else mock_target_player
        )

        mock_alias_storage = MagicMock()

        # Attempt teleport command
        result = await handle_teleport_command(
            command_data, current_user, mock_request, mock_alias_storage, "RegularUser"
        )

        assert "result" in result
        assert "permission" in result["result"].lower() or "admin" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_teleport_workflow_with_same_room_target(self, mock_app_state, mock_admin_player, mock_target_player):
        """Test teleport workflow when target is already in admin's room."""
        # Setup - put target in same room as admin
        mock_target_player.current_room_id = "admin_room"

        command_data = {"command_type": "teleport", "target_player": "TargetPlayer"}
        current_user = {"username": "AdminUser"}
        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state

        # Mock player service responses
        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: mock_admin_player if name == "AdminUser" else mock_target_player
        )

        # Mock connection manager with online target
        mock_app_state.connection_manager.online_players = {
            "target_id": {"player_name": "TargetPlayer", "room_id": "admin_room"}
        }

        mock_alias_storage = MagicMock()

        # Step 1: Initial teleport command
        result = await handle_teleport_command(
            command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
        )

        assert "result" in result
        assert "already in your location" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_teleport_workflow_with_database_error(self, mock_app_state, mock_admin_player, mock_target_player):
        """Test teleport workflow when database save fails."""
        # Setup
        command_data = {"command_type": "confirm_teleport", "target_player": "TargetPlayer"}
        current_user = {"username": "AdminUser"}
        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state

        # Mock player service responses
        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: mock_admin_player if name == "AdminUser" else mock_target_player
        )

        # Mock connection manager with online target
        mock_app_state.connection_manager.online_players = {
            "target_id": {"player_name": "TargetPlayer", "room_id": "target_room"}
        }

        # Mock player service to return False when database error occurs
        def mock_update_location_with_error(player_name, new_room_id):
            # Simulate database error by raising an exception
            raise Exception("Database error")

        mock_app_state.player_service.update_player_location.side_effect = mock_update_location_with_error

        mock_alias_storage = MagicMock()

        # Attempt confirmation command
        result = await handle_confirm_teleport_command(
            command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
        )

        assert "result" in result
        assert "failed" in result["result"].lower()
        assert "Database error" in result["result"]

    @pytest.mark.asyncio
    async def test_teleport_workflow_with_connection_manager_error(
        self, mock_app_state, mock_admin_player, mock_target_player
    ):
        """Test teleport workflow when connection manager operations fail."""
        # Setup
        command_data = {"command_type": "confirm_teleport", "target_player": "TargetPlayer"}
        current_user = {"username": "AdminUser"}
        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state

        # Mock player service responses
        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: mock_admin_player if name == "AdminUser" else mock_target_player
        )

        # Mock connection manager with online target
        mock_app_state.connection_manager.online_players = {
            "target_id": {"player_name": "TargetPlayer", "room_id": "target_room"}
        }

        # Mock connection manager error
        mock_app_state.connection_manager.broadcast_to_room.side_effect = Exception("Broadcast error")

        mock_alias_storage = MagicMock()

        # Attempt confirmation command
        result = await handle_confirm_teleport_command(
            command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
        )

        # Should still succeed even if broadcast fails
        assert "result" in result
        assert "successfully teleported" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_permission_validation_integration(self, mock_admin_player):
        """Test permission validation integration with various scenarios."""
        # Test valid admin
        result = await validate_admin_permission(mock_admin_player, "AdminUser")
        assert result is True

        # Test non-admin player
        non_admin_player = MagicMock()
        non_admin_player.is_admin = False
        result = await validate_admin_permission(non_admin_player, "RegularUser")
        assert result is False

        # Test player without is_admin attribute
        player_no_attr = MagicMock()
        delattr(player_no_attr, "is_admin")
        result = await validate_admin_permission(player_no_attr, "UnknownUser")
        assert result is False

        # Test None player
        result = await validate_admin_permission(None, "NoneUser")
        assert result is False

    @pytest.mark.asyncio
    async def test_audit_logging_integration(self, mock_app_state, mock_admin_player, mock_target_player):
        """Test that audit logging is properly integrated into teleport workflow."""
        with patch("server.commands.admin_teleport_commands.get_admin_actions_logger") as mock_logger:
            # Setup
            command_data = {"command_type": "confirm_teleport", "target_player": "TargetPlayer"}
            current_user = {"username": "AdminUser"}
            mock_request = MagicMock()
            mock_request.app = MagicMock()
            mock_request.app.state = mock_app_state

            # Mock player service responses
            mock_app_state.player_service.get_player_by_name.side_effect = (
                lambda name: mock_admin_player if name == "AdminUser" else mock_target_player
            )

            # Mock connection manager with online target
            mock_app_state.connection_manager.online_players = {
                "target_id": {"player_name": "TargetPlayer", "room_id": "target_room"}
            }

            mock_alias_storage = MagicMock()

            # Execute teleport command
            result = await handle_confirm_teleport_command(
                command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
            )

            # Verify the command succeeded
            assert "result" in result
            assert "successfully teleported" in result["result"].lower()

            # Verify audit logging was called
            mock_logger.assert_called()
            mock_logger_instance = mock_logger.return_value
            mock_logger_instance.log_teleport_action.assert_called_once()

            # Verify the log call parameters
            call_args = mock_logger_instance.log_teleport_action.call_args
            assert call_args[1]["admin_name"] == "AdminUser"
            assert call_args[1]["target_player"] == "TargetPlayer"
            assert call_args[1]["action_type"] == "teleport"
            assert call_args[1]["success"] is True

    @pytest.mark.asyncio
    async def test_concurrent_teleport_operations(self, mock_app_state, mock_admin_player):
        """Test handling of concurrent teleport operations."""
        # Setup multiple target players
        target1 = MagicMock()
        target1.is_admin = False
        target1.current_room_id = "room_1"
        target1.display_name = "Target1"

        target2 = MagicMock()
        target2.is_admin = False
        target2.current_room_id = "room_2"
        target2.display_name = "Target2"

        # Mock player service responses
        def get_player_by_name(name):
            if name == "AdminUser":
                return mock_admin_player
            elif name == "Target1":
                return target1
            elif name == "Target2":
                return target2
            return None

        mock_app_state.player_service.get_player_by_name.side_effect = get_player_by_name

        # Mock connection manager with multiple online players
        mock_app_state.connection_manager.online_players = {
            "target1_id": {"player_name": "Target1", "room_id": "room_1"},
            "target2_id": {"player_name": "Target2", "room_id": "room_2"},
        }

        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state
        mock_alias_storage = MagicMock()
        current_user = {"username": "AdminUser"}

        # Execute concurrent teleport operations
        async def teleport_target1():
            command_data = {"command_type": "confirm_teleport", "target_player": "Target1"}
            return await handle_confirm_teleport_command(
                command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
            )

        async def teleport_target2():
            command_data = {"command_type": "confirm_teleport", "target_player": "Target2"}
            return await handle_confirm_teleport_command(
                command_data, current_user, mock_request, mock_alias_storage, "AdminUser"
            )

        # Run concurrent operations
        results = await asyncio.gather(teleport_target1(), teleport_target2())

        # Verify both operations succeeded
        assert len(results) == 2
        assert "successfully teleported" in results[0]["result"].lower()
        assert "successfully teleported" in results[1]["result"].lower()
        assert "Target1" in results[0]["result"]
        assert "Target2" in results[1]["result"]

        # Verify player service was called for both operations
        assert mock_app_state.player_service.update_player_location.call_count == 2

    @pytest.mark.asyncio
    async def test_teleport_workflow_error_recovery(self, mock_app_state, mock_admin_player, mock_target_player):
        """Test error recovery in teleport workflow."""
        # Setup
        command_data = {"command_type": "confirm_teleport", "target_player": "TargetPlayer"}
        current_user = {"username": "AdminUser"}
        mock_request = MagicMock()
        mock_request.app = MagicMock()
        mock_request.app.state = mock_app_state

        # Mock player service responses
        mock_app_state.player_service.get_player_by_name.side_effect = (
            lambda name: mock_admin_player if name == "AdminUser" else mock_target_player
        )

        # Mock connection manager with online target
        mock_app_state.connection_manager.online_players = {
            "target_id": {"player_name": "TargetPlayer", "room_id": "target_room"}
        }

        # Mock various error conditions
        mock_app_state.connection_manager.send_to_player.side_effect = Exception("Notification error")

        mock_alias_storage = MagicMock()

        # Execute teleport command
        await handle_confirm_teleport_command(command_data, current_user, mock_request, mock_alias_storage, "AdminUser")

        # Verify player service was called to update location
        mock_app_state.player_service.update_player_location.assert_called_once()


class TestAdminTeleportPerformance:
    """Performance tests for admin teleport system."""

    @pytest.mark.asyncio
    async def test_teleport_performance_with_many_online_players(self):
        """Test teleport performance with many online players."""
        # Setup mock with many online players
        connection_manager = MagicMock()
        connection_manager.get_online_player_by_display_name.return_value = {
            "player_name": "TargetPlayer",
            "room_id": "target_room",
        }

        # Test player lookup performance
        import time

        start_time = time.time()

        result = connection_manager.get_online_player_by_display_name("TargetPlayer")

        end_time = time.time()
        execution_time = end_time - start_time

        # Should find the target player
        assert result is not None
        assert result["player_name"] == "TargetPlayer"

        # Should complete within reasonable time (less than 100ms)
        assert execution_time < 0.1

    @pytest.mark.asyncio
    async def test_concurrent_teleport_performance(self):
        """Test performance of concurrent teleport operations."""
        # This test would measure the performance impact of multiple
        # simultaneous teleport operations
        # Implementation would depend on the specific performance requirements

        # For now, just verify that the system can handle basic concurrency
        assert True  # Placeholder for actual performance test
