"""
Tests for NPC stats and monitoring commands (stats, population, zone, status).

This module tests NPC statistics and system monitoring operations.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.npc_admin_commands import (
    handle_npc_population_command,
    handle_npc_stats_command,
    handle_npc_status_command,
    handle_npc_zone_command,
)


class TestNPCStatsCommands:
    """Test class for NPC stats and monitoring commands."""

    @pytest.mark.asyncio
    async def test_handle_npc_stats_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC stats retrieval."""
        command_data = {"command_type": "npc", "args": ["stats", "npc_001"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.get_npc_stats = AsyncMock(return_value={"dp": 100, "mp": 50, "level": 5})
            mock_get_service.return_value = mock_service

            result = await handle_npc_stats_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "NPC npc_001 stats:" in result["result"]
            assert "dp: 100" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_population_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC population stats retrieval."""
        command_data = {"command_type": "npc", "args": ["population"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.get_population_stats = AsyncMock(
                return_value={
                    "total_npcs": 5,
                    "by_type": {"shopkeeper": 2, "passive_mob": 3},
                    "by_zone": {"arkham/city": 5},
                }
            )
            mock_get_service.return_value = mock_service

            result = await handle_npc_population_command(
                command_data, {}, mock_request, mock_alias_storage, "admin_player"
            )

            assert "result" in result
            assert "NPC Population Statistics:" in result["result"]
            assert "Total NPCs: 5" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_zone_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC zone stats retrieval."""
        command_data = {"command_type": "npc", "args": ["zone", "arkham/city"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.get_zone_stats = AsyncMock(
                return_value={
                    "zones": [
                        {"zone_key": "arkham/city", "npc_count": 3, "active_npcs": ["npc_001", "npc_002", "npc_003"]}
                    ],
                    "total_zones": 1,
                    "total_npcs": 3,
                }
            )
            mock_get_service.return_value = mock_service

            result = await handle_npc_zone_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "NPC Zone Statistics:" in result["result"]
            assert "arkham/city: 3 NPCs" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_status_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC system status retrieval."""
        command_data = {"command_type": "npc", "args": ["status"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.get_system_stats = AsyncMock(
                return_value={
                    "system_status": "healthy",
                    "active_npcs": 5,
                    "lifecycle_manager_status": "active",
                    "population_controller_status": "active",
                }
            )
            mock_get_service.return_value = mock_service

            result = await handle_npc_status_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "NPC System Status:" in result["result"]
            assert "Status: healthy" in result["result"]
