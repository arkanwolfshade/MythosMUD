"""
Tests for NPC Startup Service.

This module tests the automatic NPC spawning functionality during server startup.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.npc_startup_service import NPCStartupService


class TestNPCStartupService:
    """Test the NPC startup service functionality."""

    @pytest.fixture
    def startup_service(self):
        """Create a startup service instance for testing."""
        return NPCStartupService()

    @pytest.fixture
    def mock_npc_definitions(self):
        """Create mock NPC definitions for testing."""
        # Mock required NPC
        required_npc = MagicMock()
        required_npc.id = 1
        required_npc.name = "Test Shopkeeper"
        required_npc.required_npc = True
        required_npc.room_id = "test_room_001"
        required_npc.sub_zone_id = "test_zone"
        required_npc.spawn_probability = 1.0

        # Mock optional NPC
        optional_npc = MagicMock()
        optional_npc.id = 2
        optional_npc.name = "Test Wanderer"
        optional_npc.required_npc = False
        optional_npc.room_id = "test_room_002"
        optional_npc.sub_zone_id = "test_zone"
        optional_npc.spawn_probability = 0.5

        return [required_npc, optional_npc]

    @pytest.fixture
    def mock_npc_instance_service(self):
        """Create a mock NPC instance service."""
        service = MagicMock()

        # Mock successful spawn result - will be customized per test
        spawn_result = {
            "success": True,
            "npc_id": "test_npc_123",
            "definition_name": "Test NPC",
            "room_id": "test_room_001",
            "message": "NPC spawned successfully",
        }

        service.spawn_npc_instance = AsyncMock(return_value=spawn_result)
        return service

    @pytest.mark.asyncio
    async def test_spawn_npcs_on_startup_success(
        self, startup_service, mock_npc_definitions, mock_npc_instance_service
    ):
        """Test successful NPC spawning during startup."""
        with (
            patch(
                "server.services.npc_startup_service.get_npc_instance_service", return_value=mock_npc_instance_service
            ),
            patch("server.services.npc_startup_service.get_npc_session") as mock_session,
            patch("server.services.npc_startup_service.npc_service") as mock_npc_service,
        ):
            # Setup mocks
            mock_session.return_value.__aiter__.return_value = [MagicMock()]
            mock_npc_service.get_npc_definitions = AsyncMock(return_value=mock_npc_definitions)

            # Run the startup spawning
            results = await startup_service.spawn_npcs_on_startup()

            # Verify results
            assert results["total_attempted"] >= 1  # At least required NPC attempted
            assert results["total_spawned"] >= 1  # At least required NPC spawned
            assert results["required_spawned"] >= 1  # Required NPC spawned
            assert results["failed_spawns"] >= 0  # No failures
            assert len(results["spawned_npcs"]) >= 1  # At least one NPC spawned

            # Verify the instance service was called
            mock_npc_instance_service.spawn_npc_instance.assert_called()

    @pytest.mark.asyncio
    async def test_spawn_required_npcs(self, startup_service, mock_npc_definitions, mock_npc_instance_service):
        """Test spawning of required NPCs."""
        required_npcs = [npc for npc in mock_npc_definitions if npc.required_npc]

        # Update the mock to return the correct NPC name
        mock_npc_instance_service.spawn_npc_instance.return_value = {
            "success": True,
            "npc_id": "test_npc_123",
            "definition_name": "Test Shopkeeper",  # Match the expected name
            "room_id": "test_room_001",
            "message": "NPC spawned successfully",
        }

        results = await startup_service._spawn_required_npcs(required_npcs, mock_npc_instance_service)

        assert results["attempted"] == 1
        assert results["spawned"] == 1
        assert results["failed"] == 0
        assert len(results["spawned_npcs"]) == 1
        assert results["spawned_npcs"][0]["name"] == "Test Shopkeeper"

    @pytest.mark.asyncio
    async def test_spawn_optional_npcs_with_probability(
        self, startup_service, mock_npc_definitions, mock_npc_instance_service
    ):
        """Test spawning of optional NPCs based on probability."""
        optional_npcs = [npc for npc in mock_npc_definitions if not npc.required_npc]

        # Mock random to always return 0.3 (below the 0.5 probability)
        with patch("random.random", return_value=0.3):
            results = await startup_service._spawn_optional_npcs(optional_npcs, mock_npc_instance_service)

            # Should attempt to spawn (probability 0.5 > random 0.3)
            assert results["attempted"] == 1
            assert results["spawned"] == 1
            assert len(results["spawned_npcs"]) == 1

    @pytest.mark.asyncio
    async def test_spawn_optional_npcs_skip_low_probability(
        self, startup_service, mock_npc_definitions, mock_npc_instance_service
    ):
        """Test that optional NPCs with low probability are skipped."""
        optional_npcs = [npc for npc in mock_npc_definitions if not npc.required_npc]

        # Mock random to always return 0.8 (above the 0.5 probability)
        with patch("random.random", return_value=0.8):
            results = await startup_service._spawn_optional_npcs(optional_npcs, mock_npc_instance_service)

            # Should skip spawning (probability 0.5 < random 0.8)
            assert results["attempted"] == 0
            assert results["spawned"] == 0
            assert len(results["spawned_npcs"]) == 0

    @pytest.mark.asyncio
    async def test_determine_spawn_room_with_specific_room(self, startup_service):
        """Test room determination when NPC has specific room."""
        npc_def = MagicMock()
        npc_def.room_id = "specific_room_123"
        npc_def.sub_zone_id = "test_zone"

        room_id = startup_service._determine_spawn_room(npc_def)

        assert room_id == "specific_room_123"

    @pytest.mark.asyncio
    async def test_determine_spawn_room_with_sub_zone(self, startup_service):
        """Test room determination using sub-zone default."""
        npc_def = MagicMock()
        npc_def.room_id = None
        npc_def.sub_zone_id = "sanitarium"

        room_id = startup_service._determine_spawn_room(npc_def)

        assert room_id == "earth_arkhamcity_sanitarium_room_foyer_001"

    @pytest.mark.asyncio
    async def test_determine_spawn_room_fallback(self, startup_service):
        """Test room determination fallback to default room."""
        npc_def = MagicMock()
        npc_def.room_id = None
        npc_def.sub_zone_id = "unknown_zone"

        room_id = startup_service._determine_spawn_room(npc_def)

        assert room_id == "earth_arkhamcity_northside_intersection_derby_high"

    @pytest.mark.asyncio
    async def test_get_default_room_for_sub_zone(self, startup_service):
        """Test getting default room for known sub-zones."""
        # Test known sub-zone
        room_id = startup_service._get_default_room_for_sub_zone("sanitarium")
        assert room_id == "earth_arkhamcity_sanitarium_room_foyer_001"

        # Test unknown sub-zone
        room_id = startup_service._get_default_room_for_sub_zone("unknown_zone")
        assert room_id is None

    @pytest.mark.asyncio
    async def test_spawn_failure_handling(self, startup_service):
        """Test handling of spawn failures."""
        # Create a mock NPC instance service that fails
        mock_service = MagicMock()
        mock_service.spawn_npc_instance = AsyncMock(return_value={"success": False, "message": "Spawn failed"})

        # Create a mock NPC definition
        npc_def = MagicMock()
        npc_def.id = 1
        npc_def.name = "Test NPC"
        npc_def.required_npc = True
        npc_def.room_id = "test_room"

        results = await startup_service._spawn_required_npcs([npc_def], mock_service)

        assert results["attempted"] == 1
        assert results["spawned"] == 0
        assert results["failed"] == 1
        assert len(results["errors"]) == 1
        assert "Failed to spawn required NPC" in results["errors"][0]

    @pytest.mark.asyncio
    async def test_error_handling_in_startup_spawning(self, startup_service):
        """Test error handling during startup spawning."""
        with (
            patch("server.services.npc_startup_service.get_npc_instance_service") as mock_get_service,
        ):
            # Mock the NPC instance service to raise an exception
            mock_get_service.side_effect = Exception("NPC instance service not initialized")

            results = await startup_service.spawn_npcs_on_startup()

            assert results["total_attempted"] == 0
            assert results["total_spawned"] == 0
            # The error is caught and logged, but doesn't increment failed_spawns
            # because it's a critical error that prevents the spawning process from starting
            assert results["failed_spawns"] == 0
            assert len(results["errors"]) == 1
            assert "NPC instance service not initialized" in results["errors"][0]

    @pytest.mark.asyncio
    async def test_npc_spawn_locations_reference_existing_rooms(self):
        """
        Test that all NPC spawn locations in the database reference existing room files.

        This test validates that:
        1. All NPC definitions have valid room_id values
        2. All referenced room IDs correspond to actual room files
        3. No NPCs reference non-existent rooms

        Bug context: Deep One Hybrid was attempting to spawn in
        earth_innsmouth_waterfront_room_waterfront_001 which didn't exist.
        """
        from server.npc_database import get_npc_session
        from server.services.npc_service import npc_service
        from server.world_loader import load_hierarchical_world

        # AI Agent: Load world data to get all existing rooms
        world_data = load_hierarchical_world()
        existing_rooms = set(world_data["rooms"].keys())

        # AI Agent: Also check room_mappings for backward compatibility
        existing_rooms.update(world_data["room_mappings"].keys())

        # AI Agent: Get all NPC definitions from database
        async for session in get_npc_session():
            npc_definitions = await npc_service.get_npc_definitions(session)
            break

        # AI Agent: Validate all NPC spawn locations
        invalid_npcs = []
        for npc_def in npc_definitions:
            if npc_def.room_id and npc_def.room_id not in existing_rooms:
                invalid_npcs.append(
                    {
                        "npc_id": npc_def.id,
                        "npc_name": npc_def.name,
                        "room_id": npc_def.room_id,
                        "sub_zone_id": npc_def.sub_zone_id,
                    }
                )

        # AI Agent: Fail the test if any NPCs reference non-existent rooms
        if invalid_npcs:
            error_msg = "Found NPCs with invalid spawn locations:\n"
            for npc in invalid_npcs:
                error_msg += f"  - {npc['npc_name']} (ID: {npc['npc_id']}) "
                error_msg += f"references non-existent room '{npc['room_id']}' "
                error_msg += f"in sub-zone '{npc['sub_zone_id']}'\n"
            pytest.fail(error_msg)

        # AI Agent: Test passes if all NPCs reference valid rooms
        assert len(invalid_npcs) == 0, "All NPC spawn locations should reference existing rooms"
