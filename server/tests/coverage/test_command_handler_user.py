"""
User management command tests for command_handler_unified.py.
"""

import uuid
from unittest.mock import AsyncMock, Mock

import pytest

from server.command_handler_unified import process_command
from server.middleware.command_rate_limiter import command_rate_limiter


class TestUserManagementCommands:
    """Test user management commands."""

    @pytest.fixture(autouse=True)
    def reset_rate_limiter(self):
        """Reset rate limiter before each test to prevent test interference."""
        command_rate_limiter.reset_player("testuser")
        command_rate_limiter.reset_player("targetuser")
        yield
        # Cleanup after test
        command_rate_limiter.reset_player("testuser")
        command_rate_limiter.reset_player("targetuser")

    @pytest.mark.asyncio
    async def test_process_command_mute_no_args(self) -> None:
        """Test mute command with no arguments."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        # Mock player for catatonia check
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        result = await process_command("mute", [], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        # New validation system returns different error message
        assert "mute command requires a player name" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_mute_with_duration(self) -> None:
        """Test mute command with duration."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.id = "testuser_id"
        mock_player.player_id = uuid.uuid4()
        mock_player.current_room_id = "test_room_001"
        mock_player.is_admin = True

        # Mock target player
        mock_target_player = Mock()
        mock_target_player.id = "targetuser_id"
        mock_target_player.username = "targetuser"
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(side_effect=[mock_player, mock_target_player])

        # Mock player_service with AsyncMock for resolve_player_name
        mock_player_service = Mock()
        mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_player, mock_target_player])
        mock_request.app.state.player_service = mock_player_service

        # Mock user_manager
        mock_user_manager = Mock()
        mock_user_manager.mute_player.return_value = True
        mock_request.app.state.user_manager = mock_user_manager

        result = await process_command(
            "mute", ["targetuser", "30"], current_user, mock_request, mock_alias_storage, "testuser"
        )

        assert "result" in result
        assert "muted targetuser for 30 minutes" in result["result"]

    @pytest.mark.asyncio
    async def test_process_command_mute_with_reason(self) -> None:
        """Test mute command with reason."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.id = "testuser_id"
        mock_player.player_id = uuid.uuid4()
        mock_player.current_room_id = "test_room_001"
        mock_player.is_admin = True

        # Mock target player
        mock_target_player = Mock()
        mock_target_player.id = "targetuser_id"
        mock_target_player.username = "targetuser"
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(side_effect=[mock_player, mock_target_player])

        # Mock player_service with AsyncMock for resolve_player_name
        mock_player_service = Mock()
        mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_player, mock_target_player])
        mock_request.app.state.player_service = mock_player_service

        # Mock user_manager
        mock_user_manager = Mock()
        mock_user_manager.mute_player.return_value = True
        mock_request.app.state.user_manager = mock_user_manager

        result = await process_command(
            "mute", ["targetuser", "60", "spam"], current_user, mock_request, mock_alias_storage, "testuser"
        )

        assert "result" in result
        assert "muted targetuser for 60 minutes" in result["result"]

    @pytest.mark.asyncio
    async def test_process_command_mute_player_not_found(self) -> None:
        """Test mute command when target player not found."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.id = "testuser_id"
        mock_player.player_id = uuid.uuid4()
        mock_player.current_room_id = "test_room_001"
        mock_player.is_admin = True
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(side_effect=[mock_player, None])

        # Mock player_service with AsyncMock for resolve_player_name
        mock_player_service = Mock()
        mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_player, None])
        mock_request.app.state.player_service = mock_player_service

        # Mock user_manager
        mock_user_manager = Mock()
        mock_user_manager.mute_player.return_value = True
        mock_request.app.state.user_manager = mock_user_manager

        result = await process_command(
            "mute", ["nonexistent", "30"], current_user, mock_request, mock_alias_storage, "testuser"
        )

        assert "result" in result
        assert "not found" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_mute_failure(self) -> None:
        """Test mute command failure."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data (not admin)
        mock_player = Mock()
        mock_player.id = "testuser_id"
        mock_player.player_id = uuid.uuid4()
        mock_player.current_room_id = "test_room_001"
        mock_player.is_admin = False

        # Mock target player
        mock_target_player = Mock()
        mock_target_player.id = "targetuser_id"
        mock_target_player.username = "targetuser"
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(side_effect=[mock_player, mock_target_player])

        # Mock player_service with AsyncMock for resolve_player_name
        mock_player_service = Mock()
        mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_player, mock_target_player])
        mock_request.app.state.player_service = mock_player_service

        # Mock user_manager to return failure
        mock_user_manager = Mock()
        mock_user_manager.mute_player.return_value = False
        mock_request.app.state.user_manager = mock_user_manager

        result = await process_command(
            "mute", ["targetuser", "30"], current_user, mock_request, mock_alias_storage, "testuser"
        )

        assert "result" in result
        assert "failed" in result["result"].lower() or "error" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_unmute_success(self) -> None:
        """Test successful unmute command."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.id = "testuser_id"
        mock_player.player_id = uuid.uuid4()
        mock_player.current_room_id = "test_room_001"
        mock_player.is_admin = True

        # Mock target player
        mock_target_player = Mock()
        mock_target_player.id = "targetuser_id"
        mock_target_player.username = "targetuser"
        mock_target_player.is_muted = True
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(side_effect=[mock_player, mock_target_player])

        # Mock player_service with AsyncMock for resolve_player_name
        mock_player_service = Mock()
        mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_player, mock_target_player])
        mock_request.app.state.player_service = mock_player_service

        # Mock user_manager
        mock_user_manager = Mock()
        mock_user_manager.unmute_player.return_value = True
        mock_request.app.state.user_manager = mock_user_manager

        result = await process_command(
            "unmute", ["targetuser"], current_user, mock_request, mock_alias_storage, "testuser"
        )

        assert "result" in result
        assert "unmute" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_mute_global_success(self) -> None:
        """Test successful global mute command."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.current_room_id = "test_room_001"
        mock_player.is_admin = True

        # Mock target player
        mock_target_player = Mock()
        mock_target_player.username = "targetuser"
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(side_effect=[mock_player, mock_target_player])

        result = await process_command(
            "mute_global", ["targetuser", "120"], current_user, mock_request, mock_alias_storage, "testuser"
        )

        assert "result" in result
        assert "Global mute has been activated" in result["result"]

    @pytest.mark.asyncio
    async def test_process_command_unmute_global_success(self) -> None:
        """Test successful global unmute command."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.current_room_id = "test_room_001"
        mock_player.is_admin = True

        # Mock target player
        mock_target_player = Mock()
        mock_target_player.username = "targetuser"
        mock_target_player.is_muted_global = True
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(side_effect=[mock_player, mock_target_player])

        result = await process_command(
            "unmute_global", ["targetuser"], current_user, mock_request, mock_alias_storage, "testuser"
        )

        assert "result" in result
        assert "Global mute has been deactivated" in result["result"]

    @pytest.mark.asyncio
    async def test_process_command_add_admin_success(self) -> None:
        """Test successful add admin command."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.current_room_id = "test_room_001"
        mock_player.is_admin = True

        # Mock target player
        mock_target_player = Mock()
        mock_target_player.username = "targetuser"
        mock_target_player.is_admin = False
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(side_effect=[mock_player, mock_target_player])

        result = await process_command(
            "add_admin", ["targetuser"], current_user, mock_request, mock_alias_storage, "testuser"
        )

        assert "result" in result
        assert "targetuser has been granted administrator privileges." == result["result"]
        mock_request.app.state.user_manager.add_admin.assert_called_once_with("targetuser", "testuser")

    @pytest.mark.asyncio
    async def test_process_command_mutes(self) -> None:
        """Test mutes command."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.current_room_id = "test_room_001"
        mock_player.is_admin = True
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        result = await process_command("mutes", [], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "mute" in result["result"].lower()
