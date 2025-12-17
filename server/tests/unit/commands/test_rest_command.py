"""
Tests for rest command handler.

This module tests the handle_rest_command function which handles
MP regeneration while in a resting position.
"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.commands.rest_command import handle_rest_command


class TestHandleRestCommand:
    """Test handle_rest_command function."""

    @pytest.mark.asyncio
    async def test_handle_rest_command_success(self):
        """Test successfully handling rest command."""
        player_id = uuid4()
        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.get_stats.return_value = {"position": "sitting"}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        mock_mp_service = MagicMock()
        mock_mp_service.restore_mp_from_rest = AsyncMock(
            return_value={"success": True, "message": "You rest and recover 10 MP."}
        )

        mock_app = MagicMock()
        mock_app.state.persistence = mock_persistence
        mock_app.state.mp_regeneration_service = mock_mp_service

        mock_request = MagicMock()
        mock_request.app = mock_app

        command_data = {"duration": 60}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.get_username_from_user", return_value="testuser"):
            with patch("server.commands.rest_command.logger"):
                result = await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

                assert "result" in result
                assert "rest and recover" in result["result"].lower()
                mock_mp_service.restore_mp_from_rest.assert_called_once_with(player_id, 60)

    @pytest.mark.asyncio
    async def test_handle_rest_command_no_app(self):
        """Test handling rest command when app is not available."""
        mock_request = None

        command_data = {}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.logger"):
            result = await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

            assert result["result"] == "System error: application not available."

    @pytest.mark.asyncio
    async def test_handle_rest_command_no_persistence(self):
        """Test handling rest command when persistence is not available."""
        mock_app = MagicMock()
        mock_app.state.persistence = None

        mock_request = MagicMock()
        mock_request.app = mock_app

        command_data = {}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.logger"):
            result = await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

            assert result["result"] == "System error: persistence layer not available."

    @pytest.mark.asyncio
    async def test_handle_rest_command_no_mp_service(self):
        """Test handling rest command when MP regeneration service is not available."""
        mock_persistence = AsyncMock()

        mock_app = MagicMock()
        mock_app.state.persistence = mock_persistence
        mock_app.state.mp_regeneration_service = None

        mock_request = MagicMock()
        mock_request.app = mock_app

        command_data = {}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.logger"):
            result = await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

            assert result["result"] == "MP regeneration system not initialized."

    @pytest.mark.asyncio
    async def test_handle_rest_command_player_not_found(self):
        """Test handling rest command when player is not found."""
        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=None)

        mock_mp_service = MagicMock()

        mock_app = MagicMock()
        mock_app.state.persistence = mock_persistence
        mock_app.state.mp_regeneration_service = mock_mp_service

        mock_request = MagicMock()
        mock_request.app = mock_app

        command_data = {}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.get_username_from_user", return_value="testuser"):
            with patch("server.commands.rest_command.logger"):
                result = await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

                assert "not recognized" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_handle_rest_command_not_resting_position(self):
        """Test handling rest command when player is not in resting position."""
        mock_player = MagicMock()
        mock_player.get_stats.return_value = {"position": "standing"}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        mock_mp_service = MagicMock()

        mock_app = MagicMock()
        mock_app.state.persistence = mock_persistence
        mock_app.state.mp_regeneration_service = mock_mp_service

        mock_request = MagicMock()
        mock_request.app = mock_app

        command_data = {}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.get_username_from_user", return_value="testuser"):
            with patch("server.commands.rest_command.logger"):
                result = await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

                assert "sitting or lying" in result["result"].lower()
                mock_mp_service.restore_mp_from_rest.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_rest_command_lying_position(self):
        """Test handling rest command when player is lying down."""
        player_id = uuid4()
        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.get_stats.return_value = {"position": "lying"}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        mock_mp_service = MagicMock()
        mock_mp_service.restore_mp_from_rest = AsyncMock(
            return_value={"success": True, "message": "You rest and recover."}
        )

        mock_app = MagicMock()
        mock_app.state.persistence = mock_persistence
        mock_app.state.mp_regeneration_service = mock_mp_service

        mock_request = MagicMock()
        mock_request.app = mock_app

        command_data = {}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.get_username_from_user", return_value="testuser"):
            with patch("server.commands.rest_command.logger"):
                result = await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

                assert "result" in result
                mock_mp_service.restore_mp_from_rest.assert_called_once_with(player_id, 60)

    @pytest.mark.asyncio
    async def test_handle_rest_command_custom_duration(self):
        """Test handling rest command with custom duration."""
        player_id = uuid4()
        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.get_stats.return_value = {"position": "sitting"}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        mock_mp_service = MagicMock()
        mock_mp_service.restore_mp_from_rest = AsyncMock(
            return_value={"success": True, "message": "You rest and recover."}
        )

        mock_app = MagicMock()
        mock_app.state.persistence = mock_persistence
        mock_app.state.mp_regeneration_service = mock_mp_service

        mock_request = MagicMock()
        mock_request.app = mock_app

        command_data = {"duration": 120}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.get_username_from_user", return_value="testuser"):
            with patch("server.commands.rest_command.logger"):
                await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

                mock_mp_service.restore_mp_from_rest.assert_called_once_with(player_id, 120)

    @pytest.mark.asyncio
    async def test_handle_rest_command_duration_too_low(self):
        """Test handling rest command with duration too low."""
        player_id = uuid4()
        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.get_stats.return_value = {"position": "sitting"}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        mock_mp_service = MagicMock()
        mock_mp_service.restore_mp_from_rest = AsyncMock(
            return_value={"success": True, "message": "You rest and recover."}
        )

        mock_app = MagicMock()
        mock_app.state.persistence = mock_persistence
        mock_app.state.mp_regeneration_service = mock_mp_service

        mock_request = MagicMock()
        mock_request.app = mock_app

        command_data = {"duration": 0}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.get_username_from_user", return_value="testuser"):
            with patch("server.commands.rest_command.logger"):
                await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

                # Duration should be clamped to 60
                mock_mp_service.restore_mp_from_rest.assert_called_once_with(player_id, 60)

    @pytest.mark.asyncio
    async def test_handle_rest_command_duration_too_high(self):
        """Test handling rest command with duration too high."""
        player_id = uuid4()
        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.get_stats.return_value = {"position": "sitting"}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        mock_mp_service = MagicMock()
        mock_mp_service.restore_mp_from_rest = AsyncMock(
            return_value={"success": True, "message": "You rest and recover."}
        )

        mock_app = MagicMock()
        mock_app.state.persistence = mock_persistence
        mock_app.state.mp_regeneration_service = mock_mp_service

        mock_request = MagicMock()
        mock_request.app = mock_app

        command_data = {"duration": 500}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.get_username_from_user", return_value="testuser"):
            with patch("server.commands.rest_command.logger"):
                await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

                # Duration should be clamped to 300
                mock_mp_service.restore_mp_from_rest.assert_called_once_with(player_id, 300)

    @pytest.mark.asyncio
    async def test_handle_rest_command_invalid_duration(self):
        """Test handling rest command with invalid duration."""
        player_id = uuid4()
        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.get_stats.return_value = {"position": "sitting"}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        mock_mp_service = MagicMock()
        mock_mp_service.restore_mp_from_rest = AsyncMock(
            return_value={"success": True, "message": "You rest and recover."}
        )

        mock_app = MagicMock()
        mock_app.state.persistence = mock_persistence
        mock_app.state.mp_regeneration_service = mock_mp_service

        mock_request = MagicMock()
        mock_request.app = mock_app

        command_data = {"duration": "invalid"}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.get_username_from_user", return_value="testuser"):
            with patch("server.commands.rest_command.logger"):
                await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

                # Duration should default to 60
                mock_mp_service.restore_mp_from_rest.assert_called_once_with(player_id, 60)

    @pytest.mark.asyncio
    async def test_handle_rest_command_mp_service_failure(self):
        """Test handling rest command when MP service returns failure."""
        player_id = uuid4()
        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.get_stats.return_value = {"position": "sitting"}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        mock_mp_service = MagicMock()
        mock_mp_service.restore_mp_from_rest = AsyncMock(
            return_value={"success": False, "message": "Cannot rest right now."}
        )

        mock_app = MagicMock()
        mock_app.state.persistence = mock_persistence
        mock_app.state.mp_regeneration_service = mock_mp_service

        mock_request = MagicMock()
        mock_request.app = mock_app

        command_data = {}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.get_username_from_user", return_value="testuser"):
            with patch("server.commands.rest_command.logger"):
                result = await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

                assert result["result"] == "Cannot rest right now."

    @pytest.mark.asyncio
    async def test_handle_rest_command_no_message_in_result(self):
        """Test handling rest command when result has no message."""
        player_id = uuid4()
        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_player.get_stats.return_value = {"position": "sitting"}

        mock_persistence = AsyncMock()
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        mock_mp_service = MagicMock()
        mock_mp_service.restore_mp_from_rest = AsyncMock(return_value={"success": True})

        mock_app = MagicMock()
        mock_app.state.persistence = mock_persistence
        mock_app.state.mp_regeneration_service = mock_mp_service

        mock_request = MagicMock()
        mock_request.app = mock_app

        command_data = {}
        current_user = {"username": "testuser"}

        with patch("server.commands.rest_command.get_username_from_user", return_value="testuser"):
            with patch("server.commands.rest_command.logger"):
                result = await handle_rest_command(command_data, current_user, mock_request, None, "TestPlayer")

                assert result["result"] == "You rest and recover."
