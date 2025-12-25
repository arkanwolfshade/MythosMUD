"""
Tests for main NPC admin command routing.

This module tests the main NPC command handler and routing logic.
"""

from unittest.mock import MagicMock

import pytest

from server.commands.npc_admin_commands import handle_npc_command

pytestmark = pytest.mark.integration


class TestNPCMainCommand:
    """Test class for main NPC command routing."""

    @pytest.mark.asyncio
    async def test_handle_npc_command_no_args(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC command with no arguments shows help."""
        command_data = {"command_type": "npc", "args": []}

        result = await handle_npc_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "NPC Admin Commands" in result["result"]
        assert "Usage:" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_command_invalid_subcommand(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC command with invalid subcommand."""
        command_data = {"command_type": "npc", "args": ["invalid"]}

        result = await handle_npc_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Unknown NPC command: invalid" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_command_help(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC command help subcommand."""
        command_data = {"command_type": "npc", "args": ["help"]}

        result = await handle_npc_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "NPC Admin Commands" in result["result"]

    @pytest.mark.asyncio
    async def test_npc_command_requires_admin_permission(self, mock_regular_player, mock_request, mock_alias_storage):
        """Test that NPC commands require admin permission."""
        command_data = {"command_type": "npc", "args": ["list"]}

        # Mock the player service to return the regular player
        mock_request.app.state.player_service = MagicMock()
        mock_request.app.state.player_service.resolve_player_name = MagicMock(return_value=mock_regular_player)

        result = await handle_npc_command(command_data, {}, mock_request, mock_alias_storage, "regular_player")

        assert "result" in result
        assert "You do not have permission to use NPC admin commands" in result["result"]
