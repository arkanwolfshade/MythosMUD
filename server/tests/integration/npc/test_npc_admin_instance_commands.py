"""
Tests for NPC instance management commands (spawn, despawn, move).

This module tests NPC instance lifecycle and movement operations.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.npc_admin_commands import (
    handle_npc_despawn_command,
    handle_npc_move_command,
    handle_npc_spawn_command,
)

pytestmark = pytest.mark.integration


class TestNPCInstanceCommands:
    """Test class for NPC instance management commands."""

    @pytest.mark.asyncio
    async def test_handle_npc_spawn_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC spawning."""
        command_data = {"command_type": "npc", "args": ["spawn", "1", "earth_arkhamcity_downtown_001"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.spawn_npc_instance = AsyncMock(
                return_value={"npc_id": "npc_001", "room_id": "earth_arkhamcity_downtown_001"}
            )
            mock_get_service.return_value = mock_service

            result = await handle_npc_spawn_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "NPC spawned successfully" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_spawn_command_insufficient_args(
        self, mock_admin_player, mock_request, mock_alias_storage
    ):
        """Test NPC spawning with insufficient arguments."""
        command_data = {"command_type": "npc", "args": ["spawn", "1"]}

        result = await handle_npc_spawn_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Usage: npc spawn <definition_id> <room_id>" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_despawn_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC despawning."""
        command_data = {"command_type": "npc", "args": ["despawn", "npc_001"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.despawn_npc_instance = AsyncMock(return_value=True)
            mock_get_service.return_value = mock_service

            result = await handle_npc_despawn_command(
                command_data, {}, mock_request, mock_alias_storage, "admin_player"
            )

            assert "result" in result
            assert "NPC npc_001 despawned successfully" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_move_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC movement."""
        command_data = {"command_type": "npc", "args": ["move", "npc_001", "earth_arkhamcity_downtown_002"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.move_npc_instance = AsyncMock(return_value=True)
            mock_get_service.return_value = mock_service

            result = await handle_npc_move_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "NPC npc_001 moved to earth_arkhamcity_downtown_002" in result["result"]
