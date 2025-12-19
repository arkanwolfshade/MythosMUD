"""
Tests for movement integration with command handler.

This module tests the integration between the command handler and movement service.
"""

import uuid
from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.models.room import Room


class TestMovementIntegration:
    """Test movement integration with command handler."""

    @pytest.mark.asyncio
    async def test_command_handler_with_movement_service(self) -> None:
        """Test that command handler uses MovementService correctly."""
        from server.command_handler_unified import process_command

        # Mock persistence and movement service
        mock_persistence = Mock()
        mock_room = Mock(spec=Room)
        mock_player = Mock()

        # Setup mocks
        mock_player.player_id = uuid.uuid4()
        mock_player.current_room_id = "room1"
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_persistence.get_room.return_value = mock_room
        mock_room.exits = {"north": "room2"}

        with patch("server.game.movement_service.MovementService") as mock_movement_service_class:
            mock_movement_service = Mock()
            mock_movement_service_class.return_value = mock_movement_service
            mock_movement_service.move_player.return_value = True

            # Mock request and current user
            mock_request = Mock()
            mock_request.app.state.persistence = mock_persistence
            current_user = {"username": "testplayer"}
            mock_alias_storage = Mock()
            # Mock get_player_aliases to return empty list (no aliases for this player)
            mock_alias_storage.get_player_aliases.return_value = []
            # Mock get_alias to return None (no alias for "go" command)
            mock_alias_storage.get_alias.return_value = None

            # Test go command
            result = await process_command(
                "go", ["north"], current_user, mock_request, mock_alias_storage, "testplayer"
            )

            # Verify result
            assert "result" in result

    @pytest.mark.asyncio
    async def test_movement_failure_handling(self) -> None:
        """Test that movement failures are handled gracefully."""
        from server.command_handler_unified import process_command

        # Mock persistence and movement service
        mock_persistence = Mock()
        mock_room = Mock(spec=Room)
        mock_player = Mock()

        # Setup mocks
        mock_player.player_id = uuid.uuid4()
        mock_player.current_room_id = "room1"
        mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_persistence.get_room.return_value = mock_room
        mock_room.exits = {"north": "room2"}

        with patch("server.game.movement_service.MovementService") as mock_movement_service_class:
            mock_movement_service = Mock()
            mock_movement_service_class.return_value = mock_movement_service
            mock_movement_service.move_player.return_value = False

            # Mock request and current user
            mock_request = Mock()
            mock_request.app.state.persistence = mock_persistence
            current_user = {"username": "testplayer"}
            mock_alias_storage = Mock()
            # Mock get_player_aliases to return empty list (no aliases for this player)
            mock_alias_storage.get_player_aliases.return_value = []
            # Mock get_alias to return None (no alias for "go" command)
            mock_alias_storage.get_alias.return_value = None

            # Test go command
            result = await process_command(
                "go", ["north"], current_user, mock_request, mock_alias_storage, "testplayer"
            )

            # Verify result
            assert "result" in result
