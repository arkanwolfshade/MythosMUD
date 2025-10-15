"""
Tests for NPC Instance Management Service.

This module tests the high-level operations for managing NPC instances,
including spawning, despawning, movement, and status retrieval.

As the Cultes des Goules instructs: "Proper management of eldritch entities
requires meticulous testing of all containment protocols."
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.npc_instance_service import (
    NPCInstanceService,
    get_npc_instance_service,
    initialize_npc_instance_service,
)


@pytest.fixture
def mock_lifecycle_manager():
    """Create a mock NPC lifecycle manager."""
    manager = MagicMock()
    manager.spawn_npc = MagicMock(return_value="npc_test_001")
    manager.despawn_npc = MagicMock(return_value=True)
    manager.lifecycle_records = {}
    return manager


@pytest.fixture
def mock_spawning_service():
    """Create a mock NPC spawning service."""
    service = MagicMock()
    service.active_npc_instances = {}
    return service


@pytest.fixture
def mock_population_controller():
    """Create a mock NPC population controller."""
    controller = MagicMock()
    return controller


@pytest.fixture
def mock_event_bus():
    """Create a mock event bus."""
    bus = MagicMock()
    return bus


@pytest.fixture
def npc_instance_service_fixture(
    mock_lifecycle_manager, mock_spawning_service, mock_population_controller, mock_event_bus
):
    """Create an NPCInstanceService instance for testing."""
    return NPCInstanceService(
        lifecycle_manager=mock_lifecycle_manager,
        spawning_service=mock_spawning_service,
        population_controller=mock_population_controller,
        event_bus=mock_event_bus,
    )


class TestNPCInstanceServiceInitialization:
    """Test NPCInstanceService initialization."""

    def test_service_initialization(
        self, mock_lifecycle_manager, mock_spawning_service, mock_population_controller, mock_event_bus
    ):
        """Test service initializes with dependencies."""
        service = NPCInstanceService(
            lifecycle_manager=mock_lifecycle_manager,
            spawning_service=mock_spawning_service,
            population_controller=mock_population_controller,
            event_bus=mock_event_bus,
        )

        assert service.lifecycle_manager == mock_lifecycle_manager
        assert service.spawning_service == mock_spawning_service
        assert service.population_controller == mock_population_controller
        assert service.event_bus == mock_event_bus


class TestSpawnNPCInstance:
    """Test NPC instance spawning."""

    @pytest.mark.asyncio
    @patch("server.services.npc_instance_service.get_npc_session")
    @patch("server.services.npc_instance_service.npc_service")
    async def test_spawn_npc_instance_success(
        self, mock_npc_service_module, mock_get_session, npc_instance_service_fixture
    ):
        """Test successful NPC instance spawning."""
        # Setup mock definition
        mock_definition = MagicMock()
        mock_definition.id = 1
        mock_definition.name = "Test Shopkeeper"

        mock_npc_service = AsyncMock()
        mock_npc_service.get_npc_definition = AsyncMock(return_value=mock_definition)
        mock_npc_service_module.get_npc_definition = mock_npc_service.get_npc_definition

        # Setup mock session
        mock_session = AsyncMock()

        async def mock_session_generator():
            yield mock_session

        mock_get_session.return_value = mock_session_generator()

        # Spawn NPC
        result = await npc_instance_service_fixture.spawn_npc_instance(definition_id=1, room_id="earth_arkham_001")

        assert result["success"] is True
        assert result["npc_id"] == "npc_test_001"
        assert result["definition_id"] == 1
        assert result["definition_name"] == "Test Shopkeeper"
        assert result["room_id"] == "earth_arkham_001"
        assert "Successfully spawned" in result["message"]

    @pytest.mark.asyncio
    @patch("server.services.npc_instance_service.get_npc_session")
    @patch("server.services.npc_instance_service.npc_service")
    async def test_spawn_npc_instance_definition_not_found(
        self, mock_npc_service_module, mock_get_session, npc_instance_service_fixture
    ):
        """Test spawning fails when definition not found."""
        mock_npc_service = AsyncMock()
        mock_npc_service.get_npc_definition = AsyncMock(return_value=None)
        mock_npc_service_module.get_npc_definition = mock_npc_service.get_npc_definition

        mock_session = AsyncMock()

        async def mock_session_generator():
            yield mock_session

        mock_get_session.return_value = mock_session_generator()

        with pytest.raises(ValueError, match="NPC definition with ID 999 not found"):
            await npc_instance_service_fixture.spawn_npc_instance(definition_id=999, room_id="earth_arkham_001")

    @pytest.mark.asyncio
    @patch("server.services.npc_instance_service.get_npc_session")
    @patch("server.services.npc_instance_service.npc_service")
    async def test_spawn_npc_instance_spawn_fails(
        self, mock_npc_service_module, mock_get_session, npc_instance_service_fixture
    ):
        """Test spawning handles lifecycle manager failure."""
        mock_definition = MagicMock()
        mock_definition.id = 1
        mock_definition.name = "Test NPC"

        mock_npc_service = AsyncMock()
        mock_npc_service.get_npc_definition = AsyncMock(return_value=mock_definition)
        mock_npc_service_module.get_npc_definition = mock_npc_service.get_npc_definition

        mock_session = AsyncMock()

        async def mock_session_generator():
            yield mock_session

        mock_get_session.return_value = mock_session_generator()

        # Mock lifecycle manager to return None (spawn failure)
        npc_instance_service_fixture.lifecycle_manager.spawn_npc.return_value = None

        with pytest.raises(RuntimeError, match="Failed to spawn NPC from definition 1"):
            await npc_instance_service_fixture.spawn_npc_instance(definition_id=1, room_id="earth_arkham_001")


class TestDespawnNPCInstance:
    """Test NPC instance despawning."""

    @pytest.mark.asyncio
    async def test_despawn_npc_instance_success(self, npc_instance_service_fixture):
        """Test successful NPC instance despawning."""
        # Setup active NPC
        mock_npc = MagicMock()
        mock_npc.name = "Test NPC"
        mock_npc.current_room_id = "earth_arkham_001"
        npc_instance_service_fixture.spawning_service.active_npc_instances["npc_test_001"] = mock_npc

        result = await npc_instance_service_fixture.despawn_npc_instance(npc_id="npc_test_001", reason="admin_despawn")

        assert result["success"] is True
        assert result["npc_id"] == "npc_test_001"
        assert result["npc_name"] == "Test NPC"
        assert result["room_id"] == "earth_arkham_001"
        assert "Successfully despawned" in result["message"]

    @pytest.mark.asyncio
    async def test_despawn_npc_instance_not_found(self, npc_instance_service_fixture):
        """Test despawning fails when NPC not found."""
        with pytest.raises(ValueError, match="NPC instance npc_invalid not found"):
            await npc_instance_service_fixture.despawn_npc_instance(npc_id="npc_invalid")

    @pytest.mark.asyncio
    async def test_despawn_npc_instance_lifecycle_failure(self, npc_instance_service_fixture):
        """Test despawning handles lifecycle manager failure."""
        mock_npc = MagicMock()
        mock_npc.name = "Test NPC"
        mock_npc.current_room_id = "earth_arkham_001"
        npc_instance_service_fixture.spawning_service.active_npc_instances["npc_test_001"] = mock_npc

        # Mock lifecycle manager to return False (despawn failure)
        npc_instance_service_fixture.lifecycle_manager.despawn_npc.return_value = False

        with pytest.raises(RuntimeError, match="Failed to despawn NPC npc_test_001"):
            await npc_instance_service_fixture.despawn_npc_instance(npc_id="npc_test_001")


class TestMoveNPCInstance:
    """Test NPC instance movement."""

    @pytest.mark.asyncio
    async def test_move_npc_instance_success(self, npc_instance_service_fixture):
        """Test successful NPC instance movement."""
        mock_npc = MagicMock()
        mock_npc.name = "Test NPC"
        mock_npc.current_room_id = "earth_arkham_001"
        mock_npc.move_to_room = MagicMock()
        npc_instance_service_fixture.spawning_service.active_npc_instances["npc_test_001"] = mock_npc

        result = await npc_instance_service_fixture.move_npc_instance(
            npc_id="npc_test_001", new_room_id="earth_arkham_002", reason="admin_move"
        )

        assert result["success"] is True
        assert result["npc_id"] == "npc_test_001"
        assert result["npc_name"] == "Test NPC"
        assert result["old_room_id"] == "earth_arkham_001"
        assert result["new_room_id"] == "earth_arkham_002"
        mock_npc.move_to_room.assert_called_once_with("earth_arkham_002")

    @pytest.mark.asyncio
    async def test_move_npc_instance_without_move_method(self, npc_instance_service_fixture):
        """Test moving NPC that doesn't have move_to_room method."""
        mock_npc = MagicMock(spec=["name", "current_room_id"])  # No move_to_room method
        mock_npc.name = "Test NPC"
        mock_npc.current_room_id = "earth_arkham_001"
        npc_instance_service_fixture.spawning_service.active_npc_instances["npc_test_001"] = mock_npc

        result = await npc_instance_service_fixture.move_npc_instance(
            npc_id="npc_test_001", new_room_id="earth_arkham_002"
        )

        # Should update current_room_id directly
        assert result["success"] is True
        assert mock_npc.current_room_id == "earth_arkham_002"

    @pytest.mark.asyncio
    async def test_move_npc_instance_not_found(self, npc_instance_service_fixture):
        """Test moving fails when NPC not found."""
        with pytest.raises(ValueError, match="NPC instance npc_invalid not found"):
            await npc_instance_service_fixture.move_npc_instance(npc_id="npc_invalid", new_room_id="earth_arkham_002")


class TestGetNPCInstances:
    """Test retrieving NPC instances."""

    @pytest.mark.asyncio
    async def test_get_npc_instances_empty(self, npc_instance_service_fixture):
        """Test retrieving instances when none active."""
        result = await npc_instance_service_fixture.get_npc_instances()

        assert isinstance(result, list)
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_get_npc_instances_with_active_npcs(self, npc_instance_service_fixture):
        """Test retrieving active NPC instances."""
        # Create mock NPCs
        mock_npc1 = MagicMock()
        mock_npc1.name = "Shopkeeper"
        mock_npc1.npc_type = "shopkeeper"
        mock_npc1.current_room_id = "earth_arkham_001"
        mock_npc1.is_alive = lambda: True
        mock_npc1.stats = {"health": 100}

        mock_npc2 = MagicMock()
        mock_npc2.name = "Guard"
        mock_npc2.npc_type = "guard"
        mock_npc2.current_room_id = "earth_arkham_002"
        mock_npc2.is_alive = lambda: True
        mock_npc2.stats = {"health": 150}

        npc_instance_service_fixture.spawning_service.active_npc_instances = {
            "npc_001": mock_npc1,
            "npc_002": mock_npc2,
        }

        result = await npc_instance_service_fixture.get_npc_instances()

        assert len(result) == 2
        assert result[0]["npc_id"] in ["npc_001", "npc_002"]
        assert result[0]["name"] in ["Shopkeeper", "Guard"]

    @pytest.mark.asyncio
    async def test_get_npc_instances_with_lifecycle_info(self, npc_instance_service_fixture):
        """Test retrieving instances includes lifecycle information."""
        mock_npc = MagicMock()
        mock_npc.name = "Shopkeeper"
        mock_npc.npc_type = "shopkeeper"
        mock_npc.current_room_id = "earth_arkham_001"
        mock_npc.is_alive = lambda: True
        mock_npc.stats = {}

        # Add lifecycle record
        mock_record = MagicMock()
        mock_record.current_state = MagicMock(value="active")
        mock_record.spawn_time = "2025-01-01T12:00:00"
        mock_record.last_activity = "2025-01-01T12:05:00"

        npc_instance_service_fixture.spawning_service.active_npc_instances["npc_001"] = mock_npc
        npc_instance_service_fixture.lifecycle_manager.lifecycle_records["npc_001"] = mock_record

        result = await npc_instance_service_fixture.get_npc_instances()

        assert len(result) == 1
        assert result[0]["lifecycle_state"] == "active"
        assert result[0]["spawn_time"] == "2025-01-01T12:00:00"


class TestGetNPCStats:
    """Test retrieving NPC statistics."""

    @pytest.mark.asyncio
    async def test_get_npc_stats_success(self, npc_instance_service_fixture):
        """Test successful NPC stats retrieval."""
        mock_npc = MagicMock()
        mock_npc.name = "Test NPC"
        mock_npc.npc_type = "shopkeeper"
        mock_npc.current_room_id = "earth_arkham_001"
        mock_npc.is_alive = lambda: True
        mock_npc.stats = {"health": 100, "level": 5}

        npc_instance_service_fixture.spawning_service.active_npc_instances["npc_001"] = mock_npc

        result = await npc_instance_service_fixture.get_npc_stats(npc_id="npc_001")

        assert result["npc_id"] == "npc_001"
        assert result["name"] == "Test NPC"
        assert result["npc_type"] == "shopkeeper"
        assert result["stats"] == {"health": 100, "level": 5}

    @pytest.mark.asyncio
    async def test_get_npc_stats_not_found(self, npc_instance_service_fixture):
        """Test getting stats for non-existent NPC."""
        with pytest.raises(ValueError, match="NPC instance npc_invalid not found"):
            await npc_instance_service_fixture.get_npc_stats(npc_id="npc_invalid")

    @pytest.mark.asyncio
    async def test_get_npc_stats_with_lifecycle_data(self, npc_instance_service_fixture):
        """Test stats include lifecycle data when available."""
        mock_npc = MagicMock()
        mock_npc.name = "Test NPC"
        mock_npc.npc_type = "guard"
        mock_npc.current_room_id = "earth_arkham_001"
        mock_npc.is_alive = lambda: True
        mock_npc.stats = {}

        mock_record = MagicMock()
        mock_record.current_state = MagicMock(value="active")
        mock_record.spawn_time = "2025-01-01T12:00:00"
        mock_record.last_activity = "2025-01-01T12:05:00"
        mock_record.spawn_count = 1
        mock_record.despawn_count = 0

        npc_instance_service_fixture.spawning_service.active_npc_instances["npc_001"] = mock_npc
        npc_instance_service_fixture.lifecycle_manager.lifecycle_records["npc_001"] = mock_record

        result = await npc_instance_service_fixture.get_npc_stats(npc_id="npc_001")

        assert result["lifecycle_state"] == "active"
        assert result["spawn_count"] == 1
        assert result["despawn_count"] == 0


class TestGetPopulationStats:
    """Test population statistics retrieval."""

    @pytest.mark.asyncio
    async def test_get_population_stats_empty(self, npc_instance_service_fixture):
        """Test population stats with no active NPCs."""
        result = await npc_instance_service_fixture.get_population_stats()

        assert result["total_npcs"] == 0
        assert result["by_type"] == {}
        assert result["by_zone"] == {}
        assert result["active_instances"] == 0

    @pytest.mark.asyncio
    async def test_get_population_stats_with_npcs(self, npc_instance_service_fixture):
        """Test population stats with active NPCs."""
        # Create mock NPCs of different types
        mock_npc1 = MagicMock()
        mock_npc1.npc_type = "shopkeeper"
        mock_npc1.current_room_id = "earth_arkhamcity_downtown_001"

        mock_npc2 = MagicMock()
        mock_npc2.npc_type = "guard"
        mock_npc2.current_room_id = "earth_arkhamcity_downtown_002"

        mock_npc3 = MagicMock()
        mock_npc3.npc_type = "shopkeeper"
        mock_npc3.current_room_id = "earth_innsmouth_harbor_001"

        npc_instance_service_fixture.spawning_service.active_npc_instances = {
            "npc_001": mock_npc1,
            "npc_002": mock_npc2,
            "npc_003": mock_npc3,
        }

        result = await npc_instance_service_fixture.get_population_stats()

        assert result["total_npcs"] == 3
        assert result["by_type"]["shopkeeper"] == 2
        assert result["by_type"]["guard"] == 1
        assert "arkhamcity/downtown" in result["by_zone"]
        assert "innsmouth/harbor" in result["by_zone"]

    @pytest.mark.asyncio
    async def test_get_population_stats_with_spawn_queue(self, npc_instance_service_fixture):
        """Test population stats includes spawn queue size."""
        npc_instance_service_fixture.lifecycle_manager.respawn_queue = {
            "npc_001": {"definition_id": 1},
            "npc_002": {"definition_id": 2},
        }

        result = await npc_instance_service_fixture.get_population_stats()

        assert result["spawn_queue_size"] == 2


class TestGetZoneStats:
    """Test zone statistics retrieval."""

    @pytest.mark.asyncio
    async def test_get_zone_stats_empty(self, npc_instance_service_fixture):
        """Test zone stats with no active NPCs."""
        result = await npc_instance_service_fixture.get_zone_stats()

        assert result["total_zones"] == 0
        assert result["total_npcs"] == 0
        assert result["zones"] == []

    @pytest.mark.asyncio
    async def test_get_zone_stats_with_npcs(self, npc_instance_service_fixture):
        """Test zone stats with active NPCs."""
        mock_npc1 = MagicMock()
        mock_npc1.current_room_id = "earth_arkhamcity_downtown_001"

        mock_npc2 = MagicMock()
        mock_npc2.current_room_id = "earth_arkhamcity_downtown_002"

        mock_npc3 = MagicMock()
        mock_npc3.current_room_id = "earth_innsmouth_harbor_001"

        npc_instance_service_fixture.spawning_service.active_npc_instances = {
            "npc_001": mock_npc1,
            "npc_002": mock_npc2,
            "npc_003": mock_npc3,
        }

        result = await npc_instance_service_fixture.get_zone_stats()

        assert result["total_npcs"] == 3
        assert result["total_zones"] == 2
        assert len(result["zones"]) == 2

        # Check zone data structure
        zone_keys = [zone["zone_key"] for zone in result["zones"]]
        assert "arkhamcity/downtown" in zone_keys
        assert "innsmouth/harbor" in zone_keys


class TestGetSystemStats:
    """Test system statistics retrieval."""

    @pytest.mark.asyncio
    async def test_get_system_stats_idle(self, npc_instance_service_fixture):
        """Test system stats when idle."""
        result = await npc_instance_service_fixture.get_system_stats()

        assert result["system_status"] == "idle"
        assert result["active_npcs"] == 0
        assert result["spawn_queue_size"] == 0
        assert result["lifecycle_manager_status"] == "active"
        assert result["spawning_service_status"] == "active"

    @pytest.mark.asyncio
    async def test_get_system_stats_with_active_npcs(self, npc_instance_service_fixture):
        """Test system stats with active NPCs."""
        mock_npc = MagicMock()
        npc_instance_service_fixture.spawning_service.active_npc_instances["npc_001"] = mock_npc

        result = await npc_instance_service_fixture.get_system_stats()

        assert result["system_status"] == "healthy"
        assert result["active_npcs"] == 1

    @pytest.mark.asyncio
    async def test_get_system_stats_with_spawn_queue(self, npc_instance_service_fixture):
        """Test system stats with spawn queue."""
        npc_instance_service_fixture.lifecycle_manager.respawn_queue = {"npc_001": {}}

        result = await npc_instance_service_fixture.get_system_stats()

        assert result["system_status"] == "healthy"
        assert result["spawn_queue_size"] == 1


class TestExtractZoneFromRoomId:
    """Test zone extraction utility method."""

    def test_extract_zone_standard_format(self, npc_instance_service_fixture):
        """Test extracting zone from standard room ID format."""
        result = npc_instance_service_fixture._extract_zone_from_room_id("earth_arkhamcity_downtown_001")

        assert result == "arkhamcity/downtown"

    def test_extract_zone_different_zones(self, npc_instance_service_fixture):
        """Test extracting zone from various room IDs."""
        test_cases = [
            ("earth_innsmouth_harbor_001", "innsmouth/harbor"),
            ("earth_dunwich_village_001", "dunwich/village"),
            ("earth_miskatonic_library_001", "miskatonic/library"),
        ]

        for room_id, expected_zone in test_cases:
            result = npc_instance_service_fixture._extract_zone_from_room_id(room_id)
            assert result == expected_zone

    def test_extract_zone_invalid_format(self, npc_instance_service_fixture):
        """Test extracting zone from invalid room ID."""
        result = npc_instance_service_fixture._extract_zone_from_room_id("invalid")

        assert result == "unknown/unknown"

    def test_extract_zone_short_format(self, npc_instance_service_fixture):
        """Test extracting zone from short room ID."""
        result = npc_instance_service_fixture._extract_zone_from_room_id("earth_arkham")

        assert result == "arkham/unknown"

    def test_extract_zone_exception_handling(self, npc_instance_service_fixture):
        """Test zone extraction handles exceptions."""
        # Test with None or invalid input
        result = npc_instance_service_fixture._extract_zone_from_room_id("")

        assert result == "unknown/unknown"


class TestGlobalServiceManagement:
    """Test global service instance management."""

    def test_get_npc_instance_service_not_initialized(self):
        """Test getting service before initialization raises error."""
        # Need to temporarily set global to None
        import server.services.npc_instance_service as service_module

        original_service = service_module.npc_instance_service
        service_module.npc_instance_service = None

        try:
            with pytest.raises(RuntimeError, match="NPC instance service not initialized"):
                get_npc_instance_service()
        finally:
            service_module.npc_instance_service = original_service

    def test_initialize_npc_instance_service(
        self, mock_lifecycle_manager, mock_spawning_service, mock_population_controller, mock_event_bus
    ):
        """Test initializing global NPC instance service."""
        initialize_npc_instance_service(
            lifecycle_manager=mock_lifecycle_manager,
            spawning_service=mock_spawning_service,
            population_controller=mock_population_controller,
            event_bus=mock_event_bus,
        )

        service = get_npc_instance_service()
        assert isinstance(service, NPCInstanceService)
        assert service.lifecycle_manager == mock_lifecycle_manager


class TestErrorHandling:
    """Test error handling across service methods."""

    @pytest.mark.asyncio
    @patch("server.services.npc_instance_service.get_npc_session")
    @patch("server.services.npc_instance_service.npc_service")
    async def test_spawn_handles_database_errors(
        self, mock_npc_service_module, mock_get_session, npc_instance_service_fixture
    ):
        """Test spawn handles database errors."""
        mock_npc_service = AsyncMock()
        mock_npc_service.get_npc_definition = AsyncMock(side_effect=Exception("Database error"))
        mock_npc_service_module.get_npc_definition = mock_npc_service.get_npc_definition

        mock_session = AsyncMock()

        async def mock_session_generator():
            yield mock_session

        mock_get_session.return_value = mock_session_generator()

        with pytest.raises(Exception, match="Database error"):
            await npc_instance_service_fixture.spawn_npc_instance(definition_id=1, room_id="earth_arkham_001")

    @pytest.mark.asyncio
    async def test_get_instances_handles_errors(self, npc_instance_service_fixture):
        """Test get_instances handles errors gracefully."""
        # Create mock NPC that raises errors
        mock_npc = MagicMock()
        mock_npc.name = None  # Missing attribute
        type(mock_npc).current_room_id = property(lambda self: 1 / 0)  # Raises error

        npc_instance_service_fixture.spawning_service.active_npc_instances["npc_001"] = mock_npc

        with pytest.raises(ZeroDivisionError):
            await npc_instance_service_fixture.get_npc_instances()


class TestIntegrationScenarios:
    """Test integration scenarios combining multiple operations."""

    @pytest.mark.asyncio
    @patch("server.services.npc_instance_service.get_npc_session")
    @patch("server.services.npc_instance_service.npc_service")
    async def test_complete_npc_lifecycle(
        self, mock_npc_service_module, mock_get_session, npc_instance_service_fixture
    ):
        """Test complete NPC lifecycle: spawn, move, query, despawn."""
        # Setup
        mock_definition = MagicMock()
        mock_definition.id = 1
        mock_definition.name = "Test Merchant"

        mock_npc_service = AsyncMock()
        mock_npc_service.get_npc_definition = AsyncMock(return_value=mock_definition)
        mock_npc_service_module.get_npc_definition = mock_npc_service.get_npc_definition

        mock_session = AsyncMock()

        async def mock_session_generator():
            yield mock_session

        mock_get_session.return_value = mock_session_generator()

        # Create mock NPC for later operations
        mock_npc = MagicMock()
        mock_npc.name = "Test Merchant"
        mock_npc.current_room_id = "earth_arkham_001"
        mock_npc.npc_type = "shopkeeper"
        mock_npc.is_alive = lambda: True
        mock_npc.stats = {}

        # 1. Spawn NPC
        spawn_result = await npc_instance_service_fixture.spawn_npc_instance(
            definition_id=1, room_id="earth_arkham_001"
        )
        assert spawn_result["success"] is True

        # Add spawned NPC to active instances for subsequent operations
        npc_id = spawn_result["npc_id"]
        npc_instance_service_fixture.spawning_service.active_npc_instances[npc_id] = mock_npc

        # 2. Query stats
        stats = await npc_instance_service_fixture.get_npc_stats(npc_id)
        assert stats["name"] == "Test Merchant"

        # 3. Move NPC
        mock_npc.move_to_room = MagicMock()
        move_result = await npc_instance_service_fixture.move_npc_instance(npc_id, "earth_arkham_002")
        assert move_result["success"] is True

        # 4. Despawn NPC
        despawn_result = await npc_instance_service_fixture.despawn_npc_instance(npc_id)
        assert despawn_result["success"] is True

    @pytest.mark.asyncio
    async def test_population_monitoring_accuracy(self, npc_instance_service_fixture):
        """Test population monitoring provides accurate statistics."""
        # Create diverse NPC population
        npcs = {
            "npc_001": {"type": "shopkeeper", "room": "earth_arkhamcity_downtown_001"},
            "npc_002": {"type": "guard", "room": "earth_arkhamcity_downtown_002"},
            "npc_003": {"type": "shopkeeper", "room": "earth_innsmouth_harbor_001"},
            "npc_004": {"type": "monster", "room": "earth_dunwich_woods_001"},
        }

        for npc_id, data in npcs.items():
            mock_npc = MagicMock()
            mock_npc.npc_type = data["type"]
            mock_npc.current_room_id = data["room"]
            npc_instance_service_fixture.spawning_service.active_npc_instances[npc_id] = mock_npc

        # Get population stats
        pop_stats = await npc_instance_service_fixture.get_population_stats()
        zone_stats = await npc_instance_service_fixture.get_zone_stats()
        system_stats = await npc_instance_service_fixture.get_system_stats()

        assert pop_stats["total_npcs"] == 4
        assert pop_stats["by_type"]["shopkeeper"] == 2
        assert zone_stats["total_zones"] == 3
        assert system_stats["active_npcs"] == 4
        assert system_stats["system_status"] == "healthy"
