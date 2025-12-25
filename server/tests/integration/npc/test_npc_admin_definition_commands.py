"""
Tests for NPC definition management commands (create, edit, delete, list).

This module tests NPC definition CRUD operations.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.npc_admin_commands import (
    handle_npc_create_command,
    handle_npc_delete_command,
    handle_npc_edit_command,
    handle_npc_list_command,
)

pytestmark = pytest.mark.integration


class TestNPCDefinitionCommands:
    """Test class for NPC definition management commands."""

    @pytest.mark.asyncio
    async def test_handle_npc_create_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC creation."""
        command_data = {
            "command_type": "npc",
            "args": ["create", "Test NPC", "shopkeeper", "arkhamcity_downtown", "earth_arkhamcity_downtown_001"],
        }

        # Mock the database session and NPC service
        mock_request.app.state.db_session_maker = MagicMock()
        mock_session = MagicMock()
        mock_request.app.state.db_session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_request.app.state.db_session_maker.return_value.__aexit__ = AsyncMock(return_value=None)

        with patch("server.commands.npc_admin_commands.npc_service") as mock_npc_service:
            mock_definition = MagicMock()
            mock_definition.id = 1
            mock_definition.name = "Test NPC"
            mock_npc_service.create_npc_definition = AsyncMock(return_value=mock_definition)

            result = await handle_npc_create_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "NPC 'Test NPC' created successfully" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_create_command_insufficient_args(
        self, mock_admin_player, mock_request, mock_alias_storage
    ):
        """Test NPC creation with insufficient arguments."""
        command_data = {"command_type": "npc", "args": ["create", "Test NPC"]}

        result = await handle_npc_create_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Usage: npc create <name> <type> <sub_zone_id> <room_id>" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_create_command_invalid_type(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC creation with invalid NPC type."""
        command_data = {
            "command_type": "npc",
            "args": ["create", "Test NPC", "invalid_type", "arkhamcity_downtown", "earth_arkhamcity_downtown_001"],
        }

        result = await handle_npc_create_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Invalid NPC type: invalid_type" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_create_command_service_error(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC creation with service error."""
        command_data = {
            "command_type": "npc",
            "args": ["create", "Test NPC", "shopkeeper", "arkhamcity_downtown", "earth_arkhamcity_downtown_001"],
        }

        # Mock the NPC service to raise an exception
        with patch("server.commands.npc_admin_commands.npc_service") as mock_npc_service:
            mock_npc_service.create_npc_definition = AsyncMock(side_effect=Exception("Database error"))

            result = await handle_npc_create_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "Error creating NPC: Database error" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_edit_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC editing."""
        command_data = {"command_type": "npc", "args": ["edit", "1", "name", "Updated NPC"]}

        # Mock the NPC service
        with patch("server.commands.npc_admin_commands.npc_service") as mock_npc_service:
            mock_npc_service.update_npc_definition = AsyncMock(return_value={"id": 1, "name": "Updated NPC"})

            result = await handle_npc_edit_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "NPC definition 1 updated successfully" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_edit_command_insufficient_args(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC editing with insufficient arguments."""
        command_data = {"command_type": "npc", "args": ["edit", "1"]}

        result = await handle_npc_edit_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Usage: npc edit <id> <field> <value>" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_edit_command_invalid_id(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC editing with invalid ID."""
        command_data = {"command_type": "npc", "args": ["edit", "invalid", "name", "Updated NPC"]}

        result = await handle_npc_edit_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Invalid NPC ID: invalid" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_delete_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC deletion."""
        command_data = {"command_type": "npc", "args": ["delete", "1"]}

        # Mock the NPC service
        with patch("server.commands.npc_admin_commands.npc_service") as mock_npc_service:
            mock_npc_service.delete_npc_definition = AsyncMock(return_value=True)

            result = await handle_npc_delete_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "NPC definition 1 deleted successfully" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_delete_command_not_found(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC deletion when NPC not found."""
        command_data = {"command_type": "npc", "args": ["delete", "999"]}

        # Mock the NPC service
        with patch("server.commands.npc_admin_commands.npc_service") as mock_npc_service:
            mock_npc_service.delete_npc_definition = AsyncMock(return_value=False)

            result = await handle_npc_delete_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "NPC definition 999 not found" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_list_command_success(
        self, mock_admin_player, mock_request, mock_alias_storage, sample_npc_definition
    ):
        """Test successful NPC listing."""
        command_data = {"command_type": "npc", "args": ["list"]}

        # Mock the database session and NPC service
        mock_request.app.state.db_session_maker = MagicMock()
        mock_session = MagicMock()
        mock_request.app.state.db_session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
        mock_request.app.state.db_session_maker.return_value.__aexit__ = AsyncMock(return_value=None)

        with patch("server.commands.npc_admin_commands.npc_service") as mock_npc_service:
            # Create mock definition objects with attributes
            mock_definition = MagicMock()
            mock_definition.id = 1
            mock_definition.name = "Test Shopkeeper"
            mock_definition.npc_type = "shopkeeper"
            mock_definition.sub_zone_id = "arkhamcity_downtown"
            mock_definition.room_id = "earth_arkhamcity_downtown_001"
            mock_npc_service.get_npc_definitions = AsyncMock(return_value=[mock_definition])

            result = await handle_npc_list_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "NPC Definitions:" in result["result"]
            assert "Test Shopkeeper" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_list_command_empty(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC listing when no NPCs exist."""
        command_data = {"command_type": "npc", "args": ["list"]}

        # Mock the NPC service
        with patch("server.commands.npc_admin_commands.npc_service") as mock_npc_service:
            mock_npc_service.get_npc_definitions = AsyncMock(return_value=[])

            result = await handle_npc_list_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "No NPC definitions found" in result["result"]
