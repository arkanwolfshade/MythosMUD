"""
Tests for NPC behavior control commands (behavior, react, stop).

This module tests NPC behavior modification and reaction triggering.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.npc_admin_commands import (
    handle_npc_behavior_command,
    handle_npc_react_command,
    handle_npc_stop_command,
)


class TestNPCBehaviorCommands:
    """Test class for NPC behavior control commands."""

    @pytest.mark.asyncio
    async def test_handle_npc_behavior_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC behavior setting."""
        command_data = {"command_type": "npc", "args": ["behavior", "npc_001", "aggressive"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.set_npc_behavior = AsyncMock(return_value=True)
            mock_get_service.return_value = mock_service

            result = await handle_npc_behavior_command(
                command_data, {}, mock_request, mock_alias_storage, "admin_player"
            )

            assert "result" in result
            assert result["result"] == "NPC behavior modification not yet implemented"
            mock_service.set_npc_behavior.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_handle_npc_behavior_command_insufficient_args(
        self, mock_admin_player, mock_request, mock_alias_storage
    ):
        """Test NPC behavior command with insufficient arguments."""
        command_data = {"command_type": "npc", "args": ["behavior", "npc_001"]}

        result = await handle_npc_behavior_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Usage: npc behavior <npc_id> <behavior_type>" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_behavior_command_invalid_behavior(
        self, mock_admin_player, mock_request, mock_alias_storage
    ):
        """Test NPC behavior command with invalid behavior type."""
        command_data = {"command_type": "npc", "args": ["behavior", "npc_001", "invalid_behavior"]}

        result = await handle_npc_behavior_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Invalid behavior type: invalid_behavior" in result["result"]
        assert "passive, aggressive, defensive, wander, patrol, guard, idle" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_react_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC reaction triggering."""
        command_data = {"command_type": "npc", "args": ["react", "npc_001", "greet"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.trigger_npc_reaction = AsyncMock(return_value=True)
            mock_get_service.return_value = mock_service

            result = await handle_npc_react_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert result["result"] == "NPC reaction triggering not yet implemented"
            mock_service.trigger_npc_reaction.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_handle_npc_react_command_insufficient_args(
        self, mock_admin_player, mock_request, mock_alias_storage
    ):
        """Test NPC react command with insufficient arguments."""
        command_data = {"command_type": "npc", "args": ["react", "npc_001"]}

        result = await handle_npc_react_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Usage: npc react <npc_id> <reaction_type>" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_react_command_invalid_reaction(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC react command with invalid reaction type."""
        command_data = {"command_type": "npc", "args": ["react", "npc_001", "invalid_reaction"]}

        result = await handle_npc_react_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Invalid reaction type: invalid_reaction" in result["result"]
        assert "greet, attack, flee, investigate, alert, calm, excited, suspicious" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_stop_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC behavior stopping."""
        command_data = {"command_type": "npc", "args": ["stop", "npc_001"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.stop_npc_behavior = AsyncMock(return_value=True)
            mock_get_service.return_value = mock_service

            result = await handle_npc_stop_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert result["result"] == "NPC behavior stopping not yet implemented"
            mock_service.stop_npc_behavior.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_handle_npc_stop_command_insufficient_args(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC stop command with insufficient arguments."""
        command_data = {"command_type": "npc", "args": ["stop"]}

        result = await handle_npc_stop_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Usage: npc stop <npc_id>" in result["result"]
