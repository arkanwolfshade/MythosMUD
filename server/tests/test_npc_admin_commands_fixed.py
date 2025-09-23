"""
Tests for NPC admin slash commands.

This module tests the NPC admin command parsing, validation, and execution
for administrative NPC management functionality.

As documented in the Cultes des Goules, proper administrative protocols
are essential for maintaining control over the eldritch entities that
lurk in the shadows of our world.
"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.commands.npc_admin_commands import (
    handle_npc_behavior_command,
    handle_npc_command,
    handle_npc_create_command,
    handle_npc_delete_command,
    handle_npc_despawn_command,
    handle_npc_edit_command,
    handle_npc_list_command,
    handle_npc_move_command,
    handle_npc_population_command,
    handle_npc_react_command,
    handle_npc_spawn_command,
    handle_npc_stats_command,
    handle_npc_status_command,
    handle_npc_stop_command,
    handle_npc_zone_command,
    validate_npc_admin_permission,
)


class TestNPCAdminCommands:
    """Test class for NPC admin commands."""

    @pytest.fixture
    def mock_admin_player(self):
        """Create a mock admin player."""
        player = MagicMock()
        player.id = str(uuid4())
        player.name = "admin_player"
        player.is_admin = True
        player.current_room_id = "earth_arkham_city_downtown_001"
        return player

    @pytest.fixture
    def mock_regular_player(self):
        """Create a mock regular player."""
        player = MagicMock()
        player.id = str(uuid4())
        player.name = "regular_player"
        player.is_admin = False
        player.current_room_id = "earth_arkham_city_downtown_001"
        return player

    @pytest.fixture
    def mock_request(self):
        """Create a mock FastAPI request."""
        request = MagicMock()
        request.app = MagicMock()
        request.app.state = MagicMock()
        return request

    @pytest.fixture
    def mock_alias_storage(self):
        """Create a mock alias storage."""
        return MagicMock()

    @pytest.fixture
    def sample_npc_definition(self):
        """Create a sample NPC definition."""
        return {
            "id": 1,
            "name": "Test Shopkeeper",
            "npc_type": "shopkeeper",
            "sub_zone_id": "arkham_city_downtown",
            "room_id": "earth_arkham_city_downtown_001",
            "base_stats": {"hp": 100, "mp": 50},
            "behavior_config": {"aggressive": False},
            "ai_integration_stub": {"enabled": True},
        }

    # --- Permission Validation Tests ---

    def test_validate_npc_admin_permission_admin_user(self, mock_admin_player):
        """Test that admin users have NPC admin permissions."""
        result = validate_npc_admin_permission(mock_admin_player, "admin_player")
        assert result is True

    def test_validate_npc_admin_permission_regular_user(self, mock_regular_player):
        """Test that regular users do not have NPC admin permissions."""
        result = validate_npc_admin_permission(mock_regular_player, "regular_player")
        assert result is False

    def test_validate_npc_admin_permission_no_player(self):
        """Test that None player returns False."""
        result = validate_npc_admin_permission(None, "nonexistent_player")
        assert result is False

    def test_validate_npc_admin_permission_no_admin_attr(self):
        """Test that player without is_admin attribute returns False."""

        class MockPlayer:
            def __init__(self):
                self.name = "test_player"
                # No is_admin attribute

        player = MockPlayer()
        result = validate_npc_admin_permission(player, "test_player")
        assert result is False

    # --- Main NPC Command Tests ---

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

    # --- NPC Create Command Tests ---

    @pytest.mark.asyncio
    async def test_handle_npc_create_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC creation."""
        command_data = {
            "command_type": "npc",
            "args": ["create", "Test NPC", "shopkeeper", "arkham_city_downtown", "earth_arkham_city_downtown_001"],
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
            "args": ["create", "Test NPC", "invalid_type", "arkham_city_downtown", "earth_arkham_city_downtown_001"],
        }

        result = await handle_npc_create_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Invalid NPC type: invalid_type" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_create_command_service_error(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC creation with service error."""
        command_data = {
            "command_type": "npc",
            "args": ["create", "Test NPC", "shopkeeper", "arkham_city_downtown", "earth_arkham_city_downtown_001"],
        }

        # Mock the NPC service to raise an exception
        with patch("server.commands.npc_admin_commands.npc_service") as mock_npc_service:
            mock_npc_service.create_npc_definition = AsyncMock(side_effect=Exception("Database error"))

            result = await handle_npc_create_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "Error creating NPC: Database error" in result["result"]

    # --- NPC Edit Command Tests ---

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

    # --- NPC Delete Command Tests ---

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

    # --- NPC List Command Tests ---

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
            mock_definition.sub_zone_id = "arkham_city_downtown"
            mock_definition.room_id = "earth_arkham_city_downtown_001"
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

    # --- NPC Spawn Command Tests ---

    @pytest.mark.asyncio
    async def test_handle_npc_spawn_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC spawning."""
        command_data = {"command_type": "npc", "args": ["spawn", "1", "earth_arkham_city_downtown_001"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.spawn_npc_instance = AsyncMock(
                return_value={"npc_id": "npc_001", "room_id": "earth_arkham_city_downtown_001"}
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

    # --- NPC Despawn Command Tests ---

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

    # --- NPC Move Command Tests ---

    @pytest.mark.asyncio
    async def test_handle_npc_move_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC movement."""
        command_data = {"command_type": "npc", "args": ["move", "npc_001", "earth_arkham_city_downtown_002"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.move_npc_instance = AsyncMock(return_value=True)
            mock_get_service.return_value = mock_service

            result = await handle_npc_move_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "NPC npc_001 moved to earth_arkham_city_downtown_002" in result["result"]

    # --- NPC Stats Command Tests ---

    @pytest.mark.asyncio
    async def test_handle_npc_stats_command_success(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test successful NPC stats retrieval."""
        command_data = {"command_type": "npc", "args": ["stats", "npc_001"]}

        # Mock the NPC instance service
        with patch("server.commands.npc_admin_commands.get_npc_instance_service") as mock_get_service:
            mock_service = MagicMock()
            mock_service.get_npc_stats = AsyncMock(return_value={"hp": 100, "mp": 50, "level": 5})
            mock_get_service.return_value = mock_service

            result = await handle_npc_stats_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

            assert "result" in result
            assert "NPC npc_001 stats:" in result["result"]
            assert "hp: 100" in result["result"]

    # --- NPC Population Command Tests ---

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

    # --- NPC Zone Command Tests ---

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

    # --- NPC Status Command Tests ---

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

    # --- Permission Tests ---

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

    # --- NPC Behavior Control Command Tests ---

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
            assert "NPC npc_001 behavior set to aggressive" in result["result"]

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
            assert "NPC npc_001 reaction greet triggered" in result["result"]

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
            assert "NPC npc_001 behavior stopped" in result["result"]

    @pytest.mark.asyncio
    async def test_handle_npc_stop_command_insufficient_args(self, mock_admin_player, mock_request, mock_alias_storage):
        """Test NPC stop command with insufficient arguments."""
        command_data = {"command_type": "npc", "args": ["stop"]}

        result = await handle_npc_stop_command(command_data, {}, mock_request, mock_alias_storage, "admin_player")

        assert "result" in result
        assert "Usage: npc stop <npc_id>" in result["result"]

    @pytest.mark.asyncio
    async def test_npc_create_command_requires_admin_permission(
        self, mock_regular_player, mock_request, mock_alias_storage
    ):
        """Test that NPC create command requires admin permission."""
        command_data = {
            "command_type": "npc",
            "args": ["create", "Test NPC", "shopkeeper", "arkham_city_downtown", "earth_arkham_city_downtown_001"],
        }

        # Mock the player service to return the regular player
        mock_request.app.state.player_service = MagicMock()
        mock_request.app.state.player_service.resolve_player_name = MagicMock(return_value=mock_regular_player)

        await handle_npc_command(command_data, {}, mock_request, mock_alias_storage, "regular_player")
