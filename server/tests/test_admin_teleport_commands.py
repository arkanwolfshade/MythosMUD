"""
Tests for admin teleport commands.

This module tests the admin teleport functionality including command validation,
player lookup, teleportation logic, and security checks.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.admin_teleport_commands import (
    create_teleport_effect_message,
    get_online_player_by_display_name,
    handle_confirm_goto_command,
    handle_confirm_teleport_command,
    handle_goto_command,
    handle_teleport_command,
    validate_admin_permission,
)


class TestAdminPermissionValidation:
    """Test admin permission validation."""

    @pytest.mark.asyncio
    async def test_validate_admin_permission_success(self):
        """Test successful admin permission validation."""
        mock_player = MagicMock()
        mock_player.is_admin = True

        result = await validate_admin_permission(mock_player, "test_admin")

        assert result is True

    @pytest.mark.asyncio
    async def test_validate_admin_permission_failure(self):
        """Test failed admin permission validation."""
        mock_player = MagicMock()
        mock_player.is_admin = False

        result = await validate_admin_permission(mock_player, "test_user")

        assert result is False

    @pytest.mark.asyncio
    async def test_validate_admin_permission_no_player(self):
        """Test admin permission validation with no player."""
        result = await validate_admin_permission(None, "test_user")

        assert result is False


class TestOnlinePlayerLookup:
    """Test online player lookup functionality."""

    @pytest.mark.asyncio
    async def test_get_online_player_by_display_name_success(self):
        """Test successful online player lookup."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {
            "player1": {"display_name": "TestPlayer", "room_id": "room1"},
            "player2": {"display_name": "OtherPlayer", "room_id": "room2"},
        }

        result = await get_online_player_by_display_name("TestPlayer", mock_connection_manager)

        assert result is not None
        assert result["display_name"] == "TestPlayer"
        assert result["room_id"] == "room1"

    @pytest.mark.asyncio
    async def test_get_online_player_by_display_name_not_found(self):
        """Test online player lookup when player not found."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {"player1": {"display_name": "TestPlayer", "room_id": "room1"}}

        result = await get_online_player_by_display_name("NonExistentPlayer", mock_connection_manager)

        assert result is None

    @pytest.mark.asyncio
    async def test_get_online_player_by_display_name_case_insensitive(self):
        """Test online player lookup is case insensitive."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {"player1": {"display_name": "TestPlayer", "room_id": "room1"}}

        result = await get_online_player_by_display_name("testplayer", mock_connection_manager)

        assert result is not None
        assert result["display_name"] == "TestPlayer"


class TestTeleportEffectMessages:
    """Test teleport effect message creation."""

    def test_create_teleport_effect_message_arrival(self):
        """Test creating arrival teleport effect message."""
        message = create_teleport_effect_message("TestPlayer", "arrival")

        assert "TestPlayer" in message
        assert "materializes" in message.lower() or "appears" in message.lower()

    def test_create_teleport_effect_message_departure(self):
        """Test creating departure teleport effect message."""
        message = create_teleport_effect_message("TestPlayer", "departure")

        assert "TestPlayer" in message
        assert "departs" in message.lower() or "vanishes" in message.lower()

    def test_create_teleport_effect_message_invalid_type(self):
        """Test creating teleport effect message with invalid type."""
        message = create_teleport_effect_message("TestPlayer", "invalid")

        # Should return a default message
        assert "TestPlayer" in message


class TestTeleportCommand:
    """Test teleport command functionality."""

    @pytest.mark.asyncio
    async def test_handle_teleport_command_success(self):
        """Test successful teleport command execution."""
        # Mock command data
        command_data = {"command_type": "teleport", "target_player": "TestPlayer"}

        # Mock current user (admin)
        mock_current_user = {"username": "admin_user"}

        # Mock request with app state
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service
        mock_player_service = MagicMock()
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_admin_player.current_room_id = "admin_room"
        mock_player_service.get_player_by_name.return_value = mock_admin_player

        # Mock target player
        mock_target_player = MagicMock()
        mock_target_player.current_room_id = "target_room"
        mock_player_service.get_player_by_name.side_effect = (
            lambda name: mock_admin_player if name == "admin_user" else mock_target_player
        )

        mock_app.state.player_service = mock_player_service

        # Mock connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {"target_id": {"display_name": "TestPlayer", "room_id": "target_room"}}
        mock_app.state.connection_manager = mock_connection_manager

        # Mock persistence
        mock_persistence = MagicMock()
        mock_app.state.persistence = mock_persistence

        # Mock alias storage
        mock_alias_storage = MagicMock()

        result = await handle_teleport_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "admin_user"
        )

        # Should return confirmation message
        assert "result" in result
        assert "confirm" in result["result"].lower()
        assert "TestPlayer" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_teleport_command_not_admin(self):
        """Test teleport command with non-admin user."""
        command_data = {"command_type": "teleport", "target_player": "TestPlayer"}
        mock_current_user = {"username": "regular_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service with non-admin player
        mock_player_service = MagicMock()
        mock_regular_player = MagicMock()
        mock_regular_player.is_admin = False
        mock_player_service.get_player_by_name.return_value = mock_regular_player
        mock_app.state.player_service = mock_player_service

        mock_alias_storage = MagicMock()

        result = await handle_teleport_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "regular_user"
        )

        assert "result" in result
        assert "permission" in result["result"].lower() or "admin" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_handle_teleport_command_player_not_found(self):
        """Test teleport command with non-existent target player."""
        command_data = {"command_type": "teleport", "target_player": "NonExistentPlayer"}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service with admin player
        mock_player_service = MagicMock()
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_player_service.get_player_by_name.return_value = mock_admin_player
        mock_app.state.player_service = mock_player_service

        # Mock connection manager with no online players
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {}
        mock_app.state.connection_manager = mock_connection_manager

        mock_alias_storage = MagicMock()

        result = await handle_teleport_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "admin_user"
        )

        assert "result" in result
        assert "not found" in result["result"].lower() or "not online" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_handle_teleport_command_missing_target(self):
        """Test teleport command with missing target player."""
        command_data = {"command_type": "teleport"}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_alias_storage = MagicMock()

        result = await handle_teleport_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "admin_user"
        )

        assert "result" in result
        assert "usage" in result["result"].lower() or "target" in result["result"].lower()


class TestGotoCommand:
    """Test goto command functionality."""

    @pytest.mark.asyncio
    async def test_handle_goto_command_success(self):
        """Test successful goto command execution."""
        command_data = {"command_type": "goto", "target_player": "TestPlayer"}

        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service with admin player
        mock_player_service = MagicMock()
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_admin_player.current_room_id = "admin_room"

        # Mock target player
        mock_target_player = MagicMock()
        mock_target_player.current_room_id = "target_room"
        mock_player_service.get_player_by_name.side_effect = (
            lambda name: mock_admin_player if name == "admin_user" else mock_target_player
        )
        mock_app.state.player_service = mock_player_service

        # Mock connection manager with target player
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {"target_id": {"display_name": "TestPlayer", "room_id": "target_room"}}
        mock_app.state.connection_manager = mock_connection_manager

        # Mock persistence
        mock_persistence = MagicMock()
        mock_app.state.persistence = mock_persistence

        mock_alias_storage = MagicMock()

        result = await handle_goto_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "admin_user"
        )

        assert "result" in result
        assert "confirm" in result["result"].lower()
        assert "TestPlayer" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_goto_command_not_admin(self):
        """Test goto command with non-admin user."""
        command_data = {"command_type": "goto", "target_player": "TestPlayer"}
        mock_current_user = {"username": "regular_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service with non-admin player
        mock_player_service = MagicMock()
        mock_regular_player = MagicMock()
        mock_regular_player.is_admin = False
        mock_player_service.get_player_by_name.return_value = mock_regular_player
        mock_app.state.player_service = mock_player_service

        mock_alias_storage = MagicMock()

        result = await handle_goto_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "regular_user"
        )

        assert "result" in result
        assert "permission" in result["result"].lower() or "admin" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_handle_goto_command_player_not_found(self):
        """Test goto command with non-existent target player."""
        command_data = {"command_type": "goto", "target_player": "NonExistentPlayer"}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service with admin player
        mock_player_service = MagicMock()
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_player_service.get_player_by_name.return_value = mock_admin_player
        mock_app.state.player_service = mock_player_service

        # Mock connection manager with no online players
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {}
        mock_app.state.connection_manager = mock_connection_manager

        mock_alias_storage = MagicMock()

        result = await handle_goto_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "admin_user"
        )

        assert "result" in result
        assert "not found" in result["result"].lower() or "not online" in result["result"].lower()


class TestTeleportConfirmation:
    """Test teleport confirmation functionality."""

    @pytest.mark.asyncio
    async def test_confirm_teleport_command_success(self):
        """Test successful teleport confirmation execution."""
        command_data = {"command_type": "confirm_teleport", "target_player": "TestPlayer"}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service with admin player
        mock_player_service = MagicMock()
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_admin_player.current_room_id = "admin_room"

        # Mock target player
        mock_target_player = MagicMock()
        mock_target_player.current_room_id = "target_room"
        mock_player_service.get_player_by_name.side_effect = (
            lambda name: mock_admin_player if name == "admin_user" else mock_target_player
        )
        mock_app.state.player_service = mock_player_service

        # Mock connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {"target_id": {"display_name": "TestPlayer", "room_id": "target_room"}}
        mock_connection_manager.broadcast_to_room = AsyncMock()
        mock_connection_manager.send_to_player = AsyncMock()
        mock_app.state.connection_manager = mock_connection_manager

        # Mock persistence
        mock_persistence = MagicMock()
        mock_persistence.save_player = MagicMock()
        mock_app.state.persistence = mock_persistence

        mock_alias_storage = MagicMock()

        result = await handle_confirm_teleport_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "admin_user"
        )

        assert "result" in result
        assert "successfully teleported" in result["result"].lower()
        assert "TestPlayer" in result["result"]

    @pytest.mark.asyncio
    async def test_confirm_goto_command_success(self):
        """Test successful goto confirmation execution."""
        command_data = {"command_type": "confirm_goto", "target_player": "TestPlayer"}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service with admin player
        mock_player_service = MagicMock()
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_admin_player.current_room_id = "admin_room"

        # Mock target player
        mock_target_player = MagicMock()
        mock_target_player.current_room_id = "target_room"
        mock_player_service.get_player_by_name.side_effect = (
            lambda name: mock_admin_player if name == "admin_user" else mock_target_player
        )
        mock_app.state.player_service = mock_player_service

        # Mock connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {
            "target_id": {"display_name": "TestPlayer", "room_id": "target_room"},
            "admin_user": {"display_name": "AdminUser", "room_id": "admin_room"},
        }
        mock_connection_manager.broadcast_to_room = AsyncMock()
        mock_app.state.connection_manager = mock_connection_manager

        # Mock persistence
        mock_persistence = MagicMock()
        mock_persistence.save_player = MagicMock()
        mock_app.state.persistence = mock_persistence

        mock_alias_storage = MagicMock()

        result = await handle_confirm_goto_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "admin_user"
        )

        assert "result" in result
        assert "successfully teleported" in result["result"].lower()
        assert "TestPlayer" in result["result"]

    @pytest.mark.asyncio
    async def test_confirm_teleport_command_not_admin(self):
        """Test teleport confirmation with non-admin user."""
        command_data = {"command_type": "confirm_teleport", "target_player": "TestPlayer"}
        mock_current_user = {"username": "regular_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service with non-admin player
        mock_player_service = MagicMock()
        mock_regular_player = MagicMock()
        mock_regular_player.is_admin = False
        mock_player_service.get_player_by_name.return_value = mock_regular_player
        mock_app.state.player_service = mock_player_service

        mock_alias_storage = MagicMock()

        result = await handle_confirm_teleport_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "regular_user"
        )

        assert "result" in result
        assert "permission" in result["result"].lower() or "admin" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_confirm_teleport_command_player_not_found(self):
        """Test teleport confirmation with non-existent target player."""
        command_data = {"command_type": "confirm_teleport", "target_player": "NonExistentPlayer"}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service with admin player
        mock_player_service = MagicMock()
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_player_service.get_player_by_name.return_value = mock_admin_player
        mock_app.state.player_service = mock_player_service

        # Mock connection manager with no online players
        mock_connection_manager = MagicMock()
        mock_connection_manager.online_players = {}
        mock_app.state.connection_manager = mock_connection_manager

        mock_alias_storage = MagicMock()

        result = await handle_confirm_teleport_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "admin_user"
        )

        assert "result" in result
        assert "not found" in result["result"].lower() or "not online" in result["result"].lower()


class TestTeleportLogging:
    """Test teleport action logging."""

    @pytest.mark.asyncio
    async def test_teleport_action_logged(self):
        """Test that teleport actions are logged."""
        # This would test audit logging
        # Implementation will be added in Phase 3
        pass


class TestTeleportVisualEffects:
    """Test teleport visual effects."""

    @pytest.mark.asyncio
    async def test_teleport_visual_effects_broadcast(self):
        """Test that teleport visual effects are broadcast to other players."""
        # This would test visual effect broadcasting
        # Implementation will be added in Phase 2
        pass
