"""
Tests for admin teleport commands.

This module tests the admin teleport functionality including command validation,
player lookup, teleportation logic, and security checks.
"""

import uuid
from datetime import UTC, datetime
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock

import pytest

import server.commands.admin_commands as admin_commands
from server.commands.admin_commands import (
    create_teleport_effect_message,
    get_online_player_by_display_name,
    handle_admin_command,
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
        expected_result = {"player_name": "TestPlayer", "room_id": "room1"}
        mock_connection_manager.get_online_player_by_display_name.return_value = expected_result

        result = await get_online_player_by_display_name("TestPlayer", mock_connection_manager)

        assert result is not None
        assert result == expected_result
        mock_connection_manager.get_online_player_by_display_name.assert_called_once_with("TestPlayer")

    @pytest.mark.asyncio
    async def test_get_online_player_by_display_name_not_found(self):
        """Test online player lookup when player not found."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_player_by_display_name.return_value = None

        result = await get_online_player_by_display_name("NonExistentPlayer", mock_connection_manager)

        assert result is None
        mock_connection_manager.get_online_player_by_display_name.assert_called_once_with("NonExistentPlayer")

    @pytest.mark.asyncio
    async def test_get_online_player_by_display_name_case_insensitive(self):
        """Test online player lookup is case insensitive."""
        mock_connection_manager = MagicMock()
        expected_result = {"player_name": "TestPlayer", "room_id": "room1"}
        mock_connection_manager.get_online_player_by_display_name.return_value = expected_result

        result = await get_online_player_by_display_name("testplayer", mock_connection_manager)

        assert result is not None
        assert result == expected_result
        mock_connection_manager.get_online_player_by_display_name.assert_called_once_with("testplayer")


class TestAdminStatusCommand:
    """Test admin status subcommand handling."""

    @pytest.mark.asyncio
    async def test_handle_admin_status_active(self, monkeypatch):
        """Ensure admin status command reports active privileges."""
        command_data = {"command_type": "admin", "subcommand": "status", "args": []}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app
        mock_app.state = SimpleNamespace()

        player_record = SimpleNamespace(name="ArkanWolfshade", id=uuid.uuid4(), is_admin=True)
        mock_player_service = MagicMock()
        mock_player_service.resolve_player_name = AsyncMock(return_value=player_record)
        mock_app.state.player_service = mock_player_service

        mock_user_manager = MagicMock()
        mock_user_manager.is_admin.return_value = True
        mock_app.state.user_manager = mock_user_manager

        dummy_logger = MagicMock()
        monkeypatch.setattr(admin_commands, "get_admin_actions_logger", lambda: dummy_logger)

        result = await handle_admin_command(
            command_data, {"username": "ArkanWolfshade"}, mock_request, None, "ArkanWolfshade"
        )

        assert "Admin privileges: Active" in result["result"]
        assert "- Database record: Active" in result["result"]
        dummy_logger.log_admin_command.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_admin_status_inactive(self, monkeypatch):
        """Ensure admin status command reports inactive privileges for non-admins."""
        command_data = {"command_type": "admin", "subcommand": "status", "args": []}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app
        mock_app.state = SimpleNamespace()

        player_record = SimpleNamespace(name="Ithaqua", id=uuid.uuid4(), is_admin=False)
        mock_player_service = MagicMock()
        mock_player_service.resolve_player_name = AsyncMock(return_value=player_record)
        mock_app.state.player_service = mock_player_service

        mock_user_manager = MagicMock()
        mock_user_manager.is_admin.return_value = False
        mock_app.state.user_manager = mock_user_manager

        dummy_logger = MagicMock()
        monkeypatch.setattr(admin_commands, "get_admin_actions_logger", lambda: dummy_logger)

        result = await handle_admin_command(command_data, {"username": "Ithaqua"}, mock_request, None, "Ithaqua")

        assert "Admin privileges: Inactive" in result["result"]
        assert "- Database record: Inactive" in result["result"]
        dummy_logger.log_admin_command.assert_called_once()


class TestAdminTimeCommand:
    """Test admin time diagnostics."""

    @pytest.mark.asyncio
    async def test_handle_admin_time_command(self, monkeypatch):
        command_data = {"command_type": "admin", "subcommand": "time", "args": []}
        mock_request = MagicMock()
        app_state = SimpleNamespace()
        mock_request.app = SimpleNamespace(state=app_state)

        class FakeChronicle:
            def get_current_mythos_datetime(self):
                return datetime(1930, 1, 1, 10, tzinfo=UTC)

            def get_calendar_components(self, mythos_dt=None):
                return SimpleNamespace(
                    month_name="January",
                    day_of_month=1,
                    week_of_month=1,
                    day_of_week=0,
                    day_name="Primus",
                    daypart="day",
                    season="winter",
                    is_daytime=True,
                    is_witching_hour=False,
                )

            def get_state_snapshot(self):
                return SimpleNamespace(real_timestamp=datetime.now(UTC), mythos_timestamp=datetime(1930, 1, 1, tzinfo=UTC))

            def get_last_freeze_state(self):
                return SimpleNamespace(real_timestamp=datetime.now(UTC), mythos_timestamp=datetime(1930, 1, 1, tzinfo=UTC))

        holiday_service = MagicMock()
        holiday_service.get_active_holiday_names.return_value = ["Innsmouth Tide Offering"]
        holiday_service.get_upcoming_summary.return_value = ["03/05 - Feast of Yig"]
        app_state.holiday_service = holiday_service

        monkeypatch.setattr(admin_commands, "get_mythos_chronicle", lambda: FakeChronicle())

        result = await handle_admin_command(command_data, {"username": "Admin"}, mock_request, None, "Admin")

        assert "MYTHOS TEMPORAL STATUS" in result["result"]
        assert "Innsmouth Tide Offering" in result["result"]
        assert "Feast of Yig" in result["result"]


class TestTeleportEffectMessages:
    """Test teleport effect message creation."""

    def test_create_teleport_effect_message_arrival(self):
        """Test creating arrival teleport effect message."""
        message = create_teleport_effect_message("TestPlayer", "arrival", teleport_type="teleport")

        assert "TestPlayer" in message
        lowered = message.lower()
        assert "arrives" in lowered or "appears" in lowered or "materializes" in lowered

    def test_create_teleport_effect_message_departure(self):
        """Test creating departure teleport effect message."""
        message = create_teleport_effect_message("TestPlayer", "departure", teleport_type="teleport")

        assert "TestPlayer" in message
        lowered = message.lower()
        assert "disappears" in lowered or "vanishes" in lowered or "leaves" in lowered

    def test_create_teleport_effect_message_invalid_type(self):
        """Test creating teleport effect message with invalid type."""
        message = create_teleport_effect_message("TestPlayer", "invalid", teleport_type="teleport")

        # Should return a default message
        assert "TestPlayer" in message
        assert "mysterious forces" in message.lower()


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
        mock_player_service = SimpleNamespace(update_player_location=AsyncMock(return_value=True))
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_admin_player.current_room_id = "admin_room"

        # Mock target player
        mock_target_player = MagicMock()
        mock_target_player.current_room_id = "target_room"
        mock_player_service.get_player_by_name = AsyncMock(
            side_effect=lambda name: mock_admin_player if name == "admin_user" else mock_target_player
        )
        mock_app.state.player_service = mock_player_service

        # Mock connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_player_by_display_name.return_value = {
            "player_id": "test-player-123",
            "player_name": "TestPlayer",
            "room_id": "target_room",
        }
        mock_app.state.connection_manager = mock_connection_manager

        # Mock persistence
        mock_persistence = MagicMock()
        mock_app.state.persistence = mock_persistence

        # Mock alias storage
        mock_alias_storage = MagicMock()

        result = await handle_teleport_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "admin_user"
        )

        # Should return success message (current implementation bypasses confirmation)
        assert "result" in result
        assert "you teleport testplayer to your location" in result["result"].lower()
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
        mock_player_service = SimpleNamespace(update_player_location=AsyncMock(return_value=True))
        mock_regular_player = MagicMock()
        mock_regular_player.is_admin = False
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_regular_player)
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
        mock_player_service = SimpleNamespace(update_player_location=AsyncMock(return_value=True))
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_player_service.get_player_by_name = AsyncMock(
            side_effect=lambda name: mock_admin_player if name == "admin_user" else None
        )
        mock_app.state.player_service = mock_player_service

        # Mock connection manager with no online players
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_player_by_display_name.return_value = None
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
        admin_player = MagicMock()
        admin_player.is_admin = True
        admin_player.current_room_id = "admin_room"
        player_service = SimpleNamespace(
            get_player_by_name=AsyncMock(return_value=admin_player),
            update_player_location=AsyncMock(return_value=True),
        )
        app_state = SimpleNamespace(
            player_service=player_service,
            connection_manager=MagicMock(),
        )
        mock_request.app = SimpleNamespace(state=app_state)
        mock_alias_storage = MagicMock()

        result = await handle_teleport_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "admin_user"
        )

        assert "result" in result
        assert "usage" in result["result"].lower() or "target" in result["result"].lower()


class TestGotoCommand:
    """Test goto command functionality."""

    @pytest.mark.asyncio
    async def test_handle_goto_command_success(self, monkeypatch):
        """Test successful goto command execution."""
        command_data = {"command_type": "goto", "target_player": "TestPlayer"}

        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service with admin player
        mock_player_service = SimpleNamespace(update_player_location=AsyncMock(return_value=True))
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_admin_player.current_room_id = "admin_room"

        # Mock target player
        mock_target_player = MagicMock()
        mock_target_player.current_room_id = "target_room"
        mock_player_service.get_player_by_name = AsyncMock(
            side_effect=lambda name: mock_admin_player if name == "admin_user" else mock_target_player
        )
        mock_app.state.player_service = mock_player_service

        # Mock connection manager with target player
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_player_by_display_name.return_value = {
            "player_id": "test-player-123",
            "player_name": "TestPlayer",
            "room_id": "target_room",
        }
        mock_app.state.connection_manager = mock_connection_manager

        # Mock persistence
        mock_persistence = MagicMock()
        mock_app.state.persistence = mock_persistence

        # Patch async helpers that depend on global app state
        monkeypatch.setattr(admin_commands, "broadcast_room_update", AsyncMock())
        monkeypatch.setattr(admin_commands, "broadcast_teleport_effects", AsyncMock())
        monkeypatch.setattr(admin_commands, "notify_player_of_teleport", AsyncMock())

        mock_alias_storage = MagicMock()

        result = await handle_goto_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "admin_user"
        )

        # Should return success message (current implementation bypasses confirmation)
        assert "result" in result
        assert result["result"] == "You teleport to TestPlayer's location."
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
        mock_player_service = SimpleNamespace()
        mock_regular_player = MagicMock()
        mock_regular_player.is_admin = False
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_regular_player)
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
        mock_player_service = SimpleNamespace(update_player_location=AsyncMock(return_value=True))
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_player_service.get_player_by_name = AsyncMock(
            side_effect=lambda name: mock_admin_player if name == "admin_user" else None
        )
        mock_app.state.player_service = mock_player_service

        # Mock connection manager with no online players
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_player_by_display_name.return_value = None
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
    async def test_confirm_teleport_command_success(self, monkeypatch):
        """Test successful teleport confirmation execution."""
        command_data = {"command_type": "confirm_teleport", "target_player": "TestPlayer"}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service with admin player
        mock_player_service = SimpleNamespace(update_player_location=AsyncMock(return_value=True))
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_admin_player.current_room_id = "admin_room"

        # Mock target player
        mock_target_player = MagicMock()
        mock_target_player.current_room_id = "target_room"
        mock_player_service.get_player_by_name = AsyncMock(
            side_effect=lambda name: mock_admin_player if name == "admin_user" else mock_target_player
        )
        mock_app.state.player_service = mock_player_service

        # Mock connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_player_by_display_name.return_value = {
            "player_id": "test-player-123",
            "player_name": "TestPlayer",
            "room_id": "target_room",
        }
        mock_connection_manager.broadcast_to_room = AsyncMock()
        mock_connection_manager.send_to_player = AsyncMock()
        mock_app.state.connection_manager = mock_connection_manager

        # Mock persistence
        mock_persistence = MagicMock()
        mock_persistence.save_player = MagicMock()
        mock_app.state.persistence = mock_persistence

        monkeypatch.setattr(admin_commands, "broadcast_room_update", AsyncMock())
        monkeypatch.setattr(admin_commands, "broadcast_teleport_effects", AsyncMock())
        monkeypatch.setattr(admin_commands, "notify_player_of_teleport", AsyncMock())

        mock_alias_storage = MagicMock()

        result = await handle_confirm_teleport_command(
            command_data, mock_current_user, mock_request, mock_alias_storage, "admin_user"
        )

        assert "result" in result
        assert "successfully teleported" in result["result"].lower()
        assert "TestPlayer" in result["result"]

    @pytest.mark.asyncio
    async def test_confirm_goto_command_success(self, monkeypatch):
        """Test successful goto confirmation execution."""
        command_data = {"command_type": "confirm_goto", "target_player": "TestPlayer"}
        mock_current_user = {"username": "admin_user"}
        mock_request = MagicMock()
        mock_app = MagicMock()
        mock_request.app = mock_app

        # Mock player service with admin player
        mock_player_service = SimpleNamespace(update_player_location=AsyncMock(return_value=True))
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_admin_player.current_room_id = "admin_room"

        # Mock target player
        mock_target_player = MagicMock()
        mock_target_player.current_room_id = "target_room"
        mock_player_service.get_player_by_name = AsyncMock(
            side_effect=lambda name: mock_admin_player if name == "admin_user" else mock_target_player
        )
        mock_app.state.player_service = mock_player_service

        # Mock connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_player_by_display_name.return_value = {
            "player_id": "test-player-123",
            "player_name": "TestPlayer",
            "room_id": "target_room",
        }
        mock_connection_manager.broadcast_to_room = AsyncMock()
        mock_app.state.connection_manager = mock_connection_manager

        # Mock persistence
        mock_persistence = MagicMock()
        mock_persistence.save_player = MagicMock()
        mock_app.state.persistence = mock_persistence

        monkeypatch.setattr(admin_commands, "broadcast_room_update", AsyncMock())
        monkeypatch.setattr(admin_commands, "broadcast_teleport_effects", AsyncMock())
        monkeypatch.setattr(admin_commands, "notify_player_of_teleport", AsyncMock())

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
        mock_player_service = SimpleNamespace(update_player_location=AsyncMock(return_value=True))
        mock_regular_player = MagicMock()
        mock_regular_player.is_admin = False
        mock_player_service.get_player_by_name = AsyncMock(return_value=mock_regular_player)
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
        mock_player_service = SimpleNamespace(update_player_location=AsyncMock(return_value=True))
        mock_admin_player = MagicMock()
        mock_admin_player.is_admin = True
        mock_player_service.get_player_by_name = AsyncMock(
            side_effect=lambda name: mock_admin_player if name == "admin_user" else None
        )
        mock_app.state.player_service = mock_player_service

        # Mock connection manager with no online players
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_player_by_display_name.return_value = None
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
