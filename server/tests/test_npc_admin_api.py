"""
Tests for NPC admin API endpoints.

This module tests the NPC admin API endpoints including CRUD operations
for NPC definitions, instance management, population monitoring, and
authentication/authorization for admin endpoints.

As documented in the Cultes des Goules, proper administrative protocols
are essential for maintaining control over the eldritch entities that
lurk in the shadows of our world.
"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from server.app.factory import create_app
from server.models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule


class TestNPCAdminAPI:
    """Test NPC admin API endpoints."""

    @pytest.fixture
    def app(self, setup_test_environment):
        """Create FastAPI app for testing."""
        return create_app()

    def _mock_auth(self, client, user):
        """Helper method to mock authentication for tests."""
        from server.auth.users import get_current_user

        async def mock_get_current_user():
            return user

        # Store the original override if it exists
        original_override = client.app.dependency_overrides.get(get_current_user)
        client.app.dependency_overrides[get_current_user] = mock_get_current_user

        # Return a cleanup function
        def cleanup():
            if original_override is not None:
                client.app.dependency_overrides[get_current_user] = original_override
            else:
                client.app.dependency_overrides.pop(get_current_user, None)

        return cleanup

    @pytest.fixture
    def client(self, app):
        """Create test client."""
        return TestClient(app)

    @pytest.fixture
    def mock_admin_user(self):
        """Create a mock admin user."""
        user = MagicMock()
        user.id = uuid4()
        user.username = "admin_user"
        user.is_admin = True
        user.is_superuser = True
        # Make it behave like a dictionary for the admin permission check
        user.get = lambda key, default=None: getattr(user, key, default)
        return user

    @pytest.fixture
    def mock_regular_user(self):
        """Create a mock regular user."""
        user = MagicMock()
        user.id = uuid4()
        user.username = "regular_user"
        user.is_admin = False
        user.is_superuser = False
        # Make it behave like a dictionary for the admin permission check
        user.get = lambda key, default=None: getattr(user, key, default)
        return user

    @pytest.fixture
    def sample_npc_definition(self):
        """Create a sample NPC definition."""
        return NPCDefinition(
            id=1,
            name="Test Shopkeeper",
            npc_type=NPCDefinitionType.SHOPKEEPER,
            sub_zone_id="arkham/city",
            room_id="earth_arkhamcity_downtown_001",
            base_stats='{"hp": 100, "mp": 50, "strength": 10, "intelligence": 15}',
            behavior_config='{"greeting": "Welcome to my shop!", "buy_modifier": 0.8}',
            ai_integration_stub='{"model": "gpt-4", "temperature": 0.7}',
        )

    @pytest.fixture
    def sample_spawn_rule(self):
        """Create a sample spawn rule."""
        return NPCSpawnRule(
            id=1,
            npc_definition_id=1,
            sub_zone_id="arkham/city",
            min_players=1,
            max_players=10,
            spawn_conditions='{"time_of_day": "day", "player_count": {"min": 1}}',
        )

    def test_npc_definitions_list_unauthorized(self, client):
        """Test that NPC definitions list requires authentication."""
        response = client.get("/admin/npc/definitions")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_definitions_list_non_admin(self, client, mock_regular_user):
        """Test that non-admin users can access NPC definitions list (VIEWER role allows read access)."""
        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_regular_user)

        try:
            response = client.get("/admin/npc/definitions")
            assert response.status_code == status.HTTP_200_OK
            # Verify that the response contains the expected data structure
            data = response.json()
            assert isinstance(data, list)
        finally:
            cleanup_auth()

    def test_npc_definitions_list_success(self, client, mock_admin_user):
        """Test successful retrieval of NPC definitions list."""
        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            response = client.get("/admin/npc/definitions")
            assert response.status_code == status.HTTP_200_OK

            # Currently returns empty list as placeholder
            data = response.json()
            assert isinstance(data, list)
            # TODO: When actual implementation is added, test with real data
        finally:
            cleanup_auth()

    def test_npc_definition_create_unauthorized(self, client):
        """Test that NPC definition creation requires authentication."""
        npc_data = {
            "name": "New NPC",
            "npc_type": "shopkeeper",
            "sub_zone_id": "arkham/city",
            "room_id": "earth_arkhamcity_downtown_001",
            "base_stats": {"hp": 100, "mp": 50},
            "behavior_config": {"greeting": "Hello!"},
            "ai_integration_stub": {"model": "gpt-4"},
        }

        response = client.post("/admin/npc/definitions", json=npc_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_definition_create_non_admin(self, client, mock_regular_user):
        """Test that NPC definition creation requires admin permissions."""
        npc_data = {
            "name": "New NPC",
            "npc_type": "shopkeeper",
            "sub_zone_id": "arkham/city",
            "room_id": "earth_arkhamcity_downtown_001",
            "base_stats": {"hp": 100, "mp": 50},
            "behavior_config": {"greeting": "Hello!"},
            "ai_integration_stub": {"model": "gpt-4"},
        }

        overrides = self._mock_auth(client, mock_regular_user)
        try:
            response = client.post("/admin/npc/definitions", json=npc_data)
            assert response.status_code == status.HTTP_403_FORBIDDEN
        finally:
            overrides()

    def test_npc_definition_create_success(self, client, mock_admin_user, sample_npc_definition):
        """Test successful NPC definition creation."""
        npc_data = {
            "name": f"Test NPC {uuid4().hex[:8]}",
            "npc_type": "shopkeeper",
            "sub_zone_id": "arkham/city",
            "room_id": "earth_arkhamcity_downtown_001",
            "base_stats": {"hp": 100, "mp": 50},
            "behavior_config": {"greeting": "Hello!"},
            "ai_integration_stub": {"model": "gpt-4"},
        }

        overrides = self._mock_auth(client, mock_admin_user)
        try:
            response = client.post("/admin/npc/definitions", json=npc_data)
            assert response.status_code == status.HTTP_201_CREATED

            data = response.json()
            assert data["name"] == npc_data["name"]
            assert data["npc_type"] == "shopkeeper"
        finally:
            overrides()

    def test_npc_definition_get_unauthorized(self, client):
        """Test that NPC definition retrieval requires authentication."""
        response = client.get("/admin/npc/definitions/1")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_definition_get_success(self, client, mock_admin_user, sample_npc_definition):
        """Test successful NPC definition retrieval."""
        overrides = self._mock_auth(client, mock_admin_user)

        with patch("server.api.admin.npc.npc_service.get_npc_definition", return_value=sample_npc_definition):
            try:
                response = client.get("/admin/npc/definitions/1")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert data["name"] == "Test Shopkeeper"
                assert data["npc_type"] == "shopkeeper"
            finally:
                overrides()

    def test_npc_definition_update_unauthorized(self, client):
        """Test that NPC definition update requires authentication."""
        npc_data = {
            "name": "Updated NPC",
            "base_stats": {"hp": 120, "mp": 60},
        }

        response = client.put("/admin/npc/definitions/1", json=npc_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_definition_update_success(self, client, mock_admin_user, sample_npc_definition):
        """Test successful NPC definition update."""
        npc_data = {
            "name": "Updated NPC",
            "base_stats": {"hp": 120, "mp": 60},
        }

        updated_npc = sample_npc_definition
        updated_npc.name = "Updated NPC"

        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            with patch("server.api.admin.npc.npc_service.update_npc_definition", return_value=updated_npc):
                response = client.put("/admin/npc/definitions/1", json=npc_data)
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert data["name"] == "Updated NPC"
        finally:
            cleanup_auth()

    def test_npc_definition_delete_unauthorized(self, client):
        """Test that NPC definition deletion requires authentication."""
        response = client.delete("/admin/npc/definitions/1")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_definition_delete_success(self, client, mock_admin_user):
        """Test successful NPC definition deletion."""
        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            with patch("server.api.admin.npc.npc_service.delete_npc_definition", return_value=True):
                response = client.delete("/admin/npc/definitions/1")
                assert response.status_code == status.HTTP_204_NO_CONTENT
        finally:
            cleanup_auth()

    def test_npc_instances_list_unauthorized(self, client):
        """Test that NPC instances list requires authentication."""
        response = client.get("/admin/npc/instances")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_instances_list_success(self, client, mock_admin_user):
        """Test successful retrieval of NPC instances list."""
        overrides = self._mock_auth(client, mock_admin_user)

        # Mock the NPC instance service

        async def mock_get_npc_instances():
            return [
                {
                    "npc_id": "npc_001",
                    "name": "Test Shopkeeper",
                    "npc_type": "shopkeeper",
                    "current_room_id": "earth_arkhamcity_downtown_001",
                    "is_alive": True,
                    "stats": {"hp": 100, "mp": 50},
                }
            ]

        mock_service = MagicMock()
        mock_service.get_npc_instances = mock_get_npc_instances

        # Mock the get_npc_instance_service function directly
        with patch("server.api.admin.npc.get_npc_instance_service", return_value=mock_service):
            try:
                response = client.get("/admin/npc/instances")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert isinstance(data, list)
                assert len(data) == 1
                assert data[0]["npc_id"] == "npc_001"
                assert data[0]["name"] == "Test Shopkeeper"
            finally:
                overrides()

    def test_npc_spawn_unauthorized(self, client):
        """Test that NPC spawning requires authentication."""
        spawn_data = {
            "definition_id": 1,
            "room_id": "earth_arkhamcity_downtown_001",
        }

        response = client.post("/admin/npc/instances/spawn", json=spawn_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_spawn_success(self, client, mock_admin_user):
        """Test successful NPC spawning."""
        spawn_data = {
            "definition_id": 1,
            "room_id": "earth_arkhamcity_downtown_001",
        }

        mock_result = {
            "success": True,
            "npc_id": "npc_001",
            "message": "NPC spawned successfully",
        }

        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            # Mock the NPC instance service to return our mock result
            with patch("server.api.admin.npc.get_npc_instance_service") as mock_get_service:
                mock_service = MagicMock()
                mock_service.spawn_npc_instance = AsyncMock(return_value=mock_result)
                mock_get_service.return_value = mock_service

                response = client.post("/admin/npc/instances/spawn", json=spawn_data)
                assert response.status_code == status.HTTP_200_OK
        finally:
            cleanup_auth()

            data = response.json()
            assert data["success"] is True
            assert data["npc_id"] == "npc_001"

    def test_npc_despawn_unauthorized(self, client):
        """Test that NPC despawning requires authentication."""
        response = client.delete("/admin/npc/instances/npc_001")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_despawn_success(self, client, mock_admin_user):
        """Test successful NPC despawning."""
        mock_result = {
            "success": True,
            "message": "NPC despawned successfully",
        }

        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            # Mock the NPC instance service to return our mock result
            with patch("server.api.admin.npc.get_npc_instance_service") as mock_get_service:
                mock_service = MagicMock()
                mock_service.despawn_npc_instance = AsyncMock(return_value=mock_result)
                mock_get_service.return_value = mock_service

                response = client.delete("/admin/npc/instances/npc_001")
                assert response.status_code == status.HTTP_200_OK
        finally:
            cleanup_auth()

            data = response.json()
            assert data["success"] is True

    def test_npc_move_unauthorized(self, client):
        """Test that NPC movement requires authentication."""
        move_data = {
            "room_id": "earth_arkhamcity_downtown_002",
        }

        response = client.put("/admin/npc/instances/npc_001/move", json=move_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_move_success(self, client, mock_admin_user):
        """Test successful NPC movement."""
        move_data = {
            "room_id": "earth_arkhamcity_downtown_002",
        }

        mock_result = {
            "success": True,
            "message": "NPC moved successfully",
            "new_room_id": "earth_arkhamcity_downtown_002",
        }

        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            # Mock the NPC instance service to return our mock result
            with patch("server.api.admin.npc.get_npc_instance_service") as mock_get_service:
                mock_service = MagicMock()
                mock_service.move_npc_instance = AsyncMock(return_value=mock_result)
                mock_get_service.return_value = mock_service

                response = client.put("/admin/npc/instances/npc_001/move", json=move_data)
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert data["success"] is True
                assert data["new_room_id"] == "earth_arkhamcity_downtown_002"
        finally:
            cleanup_auth()

    def test_npc_stats_unauthorized(self, client):
        """Test that NPC stats retrieval requires authentication."""
        response = client.get("/admin/npc/instances/npc_001/stats")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_stats_success(self, client, mock_admin_user):
        """Test successful NPC stats retrieval."""
        mock_stats = {
            "npc_id": "npc_001",
            "name": "Test Shopkeeper",
            "hp": 100,
            "mp": 50,
            "strength": 10,
            "intelligence": 15,
            "status": "active",
            "spawn_time": "2025-01-01T12:00:00Z",
        }

        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            # Mock the NPC instance service to return our mock stats
            with patch("server.api.admin.npc.get_npc_instance_service") as mock_get_service:
                mock_service = MagicMock()
                mock_service.get_npc_stats = AsyncMock(return_value=mock_stats)
                mock_get_service.return_value = mock_service

                response = client.get("/admin/npc/instances/npc_001/stats")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert data["npc_id"] == "npc_001"
                assert data["hp"] == 100
        finally:
            cleanup_auth()

    def test_npc_population_unauthorized(self, client):
        """Test that NPC population monitoring requires authentication."""
        response = client.get("/admin/npc/population")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_population_success(self, client, mock_admin_user):
        """Test successful NPC population monitoring."""
        mock_population = {
            "total_npcs": 25,
            "by_type": {
                "shopkeeper": 5,
                "passive_mob": 15,
                "aggressive_mob": 5,
            },
            "by_zone": {
                "arkham/city": 10,
                "innsmouth/waterfront": 8,
                "dunwich/woods": 7,
            },
            "active_instances": 25,
            "spawn_queue_size": 3,
        }

        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            # Mock the NPC instance service to return our mock population stats
            with patch("server.api.admin.npc.get_npc_instance_service") as mock_get_service:
                mock_service = MagicMock()
                mock_service.get_population_stats = AsyncMock(return_value=mock_population)
                mock_get_service.return_value = mock_service

                response = client.get("/admin/npc/population")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert data["total_npcs"] == 25
                assert data["by_type"]["shopkeeper"] == 5
        finally:
            cleanup_auth()

    def test_npc_zones_unauthorized(self, client):
        """Test that NPC zone monitoring requires authentication."""
        response = client.get("/admin/npc/zones")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_zones_success(self, client, mock_admin_user):
        """Test successful NPC zone monitoring."""
        mock_zones = {
            "zones": [
                {
                    "zone_key": "arkham/city",
                    "npc_count": 10,
                    "spawn_modifier": 1.2,
                    "active_npcs": ["npc_001", "npc_002"],
                },
                {
                    "zone_key": "innsmouth/waterfront",
                    "npc_count": 8,
                    "spawn_modifier": 0.8,
                    "active_npcs": ["npc_003", "npc_004"],
                },
            ],
            "total_zones": 2,
            "total_npcs": 18,
        }

        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            # Mock the NPC instance service to return our mock zone stats
            with patch("server.api.admin.npc.get_npc_instance_service") as mock_get_service:
                mock_service = MagicMock()
                mock_service.get_zone_stats = AsyncMock(return_value=mock_zones)
                mock_get_service.return_value = mock_service

                response = client.get("/admin/npc/zones")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert data["total_zones"] == 2
                assert len(data["zones"]) == 2
        finally:
            cleanup_auth()

    def test_npc_status_unauthorized(self, client):
        """Test that NPC status monitoring requires authentication."""
        response = client.get("/admin/npc/status")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_status_success(self, client, mock_admin_user):
        """Test successful NPC status monitoring."""
        mock_status = {
            "system_status": "healthy",
            "active_npcs": 25,
            "spawn_queue_size": 3,
            "lifecycle_manager_status": "active",
            "population_controller_status": "active",
            "interaction_engine_status": "active",
            "last_maintenance": "2025-01-01T12:00:00Z",
            "uptime_seconds": 3600,
        }

        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            # Mock the NPC instance service to return our mock system status
            with patch("server.api.admin.npc.get_npc_instance_service") as mock_get_service:
                mock_service = MagicMock()
                mock_service.get_system_stats = AsyncMock(return_value=mock_status)
                mock_get_service.return_value = mock_service

                response = client.get("/admin/npc/status")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert data["system_status"] == "healthy"
                assert data["active_npcs"] == 25
        finally:
            cleanup_auth()

    # NPC relationship tests removed - relationship functionality was removed from the codebase
    # The relationship endpoints no longer exist, so these tests are no longer applicable

    def test_npc_spawn_rules_list_unauthorized(self, client):
        """Test that NPC spawn rules list requires authentication."""
        response = client.get("/admin/npc/spawn-rules")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_spawn_rules_list_success(self, client, mock_admin_user, sample_spawn_rule):
        """Test successful retrieval of NPC spawn rules list."""
        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            # Create a mock spawn rule with all the attributes the response model expects
            mock_spawn_rule = MagicMock()
            mock_spawn_rule.id = 1
            mock_spawn_rule.npc_definition_id = 1
            mock_spawn_rule.spawn_probability = 0.5
            mock_spawn_rule.max_population = 3
            mock_spawn_rule.spawn_conditions = '{"time_of_day": "day"}'
            mock_spawn_rule.required_npc = True

            with patch("server.api.admin.npc.npc_service.get_spawn_rules", return_value=[mock_spawn_rule]):
                response = client.get("/admin/npc/spawn-rules")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert len(data) == 1
                assert data[0]["npc_definition_id"] == 1
                assert data[0]["spawn_probability"] == 0.5
                assert data[0]["required_npc"] is True
        finally:
            cleanup_auth()

    def test_npc_spawn_rule_create_unauthorized(self, client):
        """Test that NPC spawn rule creation requires authentication."""
        spawn_rule_data = {
            "npc_definition_id": 1,
            "spawn_probability": 0.5,
            "max_population": 3,
            "spawn_conditions": {"time_of_day": "day"},
            "required_npc": True,
        }

        response = client.post("/admin/npc/spawn-rules", json=spawn_rule_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_spawn_rule_create_success(self, client, mock_admin_user, sample_spawn_rule):
        """Test successful NPC spawn rule creation."""
        spawn_rule_data = {
            "npc_definition_id": 1,
            "spawn_probability": 0.5,
            "max_population": 3,
            "spawn_conditions": {"time_of_day": "day"},
            "required_npc": True,
        }

        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            # Create a mock spawn rule with all the attributes the response model expects
            mock_spawn_rule = MagicMock()
            mock_spawn_rule.id = 1
            mock_spawn_rule.npc_definition_id = 1
            mock_spawn_rule.spawn_probability = 0.5
            mock_spawn_rule.max_population = 3
            mock_spawn_rule.spawn_conditions = '{"time_of_day": "day"}'
            mock_spawn_rule.required_npc = True

            with patch("server.api.admin.npc.npc_service.create_spawn_rule", return_value=mock_spawn_rule):
                response = client.post("/admin/npc/spawn-rules", json=spawn_rule_data)
                assert response.status_code == status.HTTP_201_CREATED

                data = response.json()
                assert data["npc_definition_id"] == 1
                assert data["spawn_probability"] == 0.5
                assert data["required_npc"] is True
        finally:
            cleanup_auth()

    def test_npc_spawn_rule_delete_unauthorized(self, client):
        """Test that NPC spawn rule deletion requires authentication."""
        response = client.delete("/admin/npc/spawn-rules/1")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_spawn_rule_delete_success(self, client, mock_admin_user):
        """Test successful NPC spawn rule deletion."""
        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            with patch("server.api.admin.npc.npc_service.delete_spawn_rule", return_value=True):
                response = client.delete("/admin/npc/spawn-rules/1")
                assert response.status_code == status.HTTP_204_NO_CONTENT
        finally:
            cleanup_auth()

    def test_npc_validation_errors(self, client, mock_admin_user):
        """Test validation errors in NPC API endpoints."""
        # Test invalid NPC type
        invalid_npc_data = {
            "name": "Invalid NPC",
            "npc_type": "invalid_type",
            "sub_zone_id": "arkham/city",
            "room_id": "earth_arkhamcity_downtown_001",
            "base_stats": {"hp": 100},
            "behavior_config": {},
            "ai_integration_stub": {},
        }

        with patch("server.auth.users.get_current_user", return_value=mock_admin_user):
            response = client.post("/admin/npc/definitions", json=invalid_npc_data)
            assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_npc_not_found_errors(self, client, mock_admin_user):
        """Test not found errors in NPC API endpoints."""
        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            with patch("server.api.admin.npc.get_npc_definition", return_value=None):
                response = client.get("/admin/npc/definitions/999")
                assert response.status_code == status.HTTP_404_NOT_FOUND
        finally:
            cleanup_auth()

    def test_npc_server_errors(self, client, mock_admin_user):
        """Test server errors in NPC API endpoints."""
        # Use consistent authentication mocking
        cleanup_auth = self._mock_auth(client, mock_admin_user)

        try:
            with patch("server.api.admin.npc.npc_service.get_npc_definitions", side_effect=Exception("Database error")):
                response = client.get("/admin/npc/definitions")
                assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            cleanup_auth()

    # --- Population Monitoring Tests ---

    def test_npc_population_stats_unauthorized(self, client):
        """Test that NPC population stats require authentication."""
        response = client.get("/admin/npc/population")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_population_stats_success(self, client, mock_admin_user):
        """Test successful retrieval of NPC population statistics."""
        overrides = self._mock_auth(client, mock_admin_user)

        # Mock the NPC instance service
        async def mock_get_population_stats():
            return {
                "total_npcs": 5,
                "by_type": {"shopkeeper": 2, "passive_mob": 2, "aggressive_mob": 1},
                "by_zone": {"arkham/city": 3, "innsmouth/waterfront": 2},
                "active_instances": 5,
                "spawn_queue_size": 1,
            }

        mock_service = MagicMock()
        mock_service.get_population_stats = mock_get_population_stats

        # Mock the get_npc_instance_service function directly
        with patch("server.api.admin.npc.get_npc_instance_service", return_value=mock_service):
            try:
                response = client.get("/admin/npc/population")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert data["total_npcs"] == 5
                assert data["by_type"]["shopkeeper"] == 2
                assert data["by_zone"]["arkham/city"] == 3
                assert data["spawn_queue_size"] == 1
            finally:
                overrides()

    def test_npc_zone_stats_unauthorized(self, client):
        """Test that NPC zone stats require authentication."""
        response = client.get("/admin/npc/zones")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_zone_stats_success(self, client, mock_admin_user):
        """Test successful retrieval of NPC zone statistics."""
        overrides = self._mock_auth(client, mock_admin_user)

        # Mock the NPC instance service
        async def mock_get_zone_stats():
            return {
                "zones": [
                    {
                        "zone_key": "arkham/city",
                        "npc_count": 3,
                        "spawn_modifier": 1.0,
                        "active_npcs": ["npc_001", "npc_002", "npc_003"],
                    },
                    {
                        "zone_key": "innsmouth/waterfront",
                        "npc_count": 2,
                        "spawn_modifier": 1.0,
                        "active_npcs": ["npc_004", "npc_005"],
                    },
                ],
                "total_zones": 2,
                "total_npcs": 5,
            }

        mock_service = MagicMock()
        mock_service.get_zone_stats = mock_get_zone_stats

        # Mock the get_npc_instance_service function directly
        with patch("server.api.admin.npc.get_npc_instance_service", return_value=mock_service):
            try:
                response = client.get("/admin/npc/zones")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert data["total_zones"] == 2
                assert data["total_npcs"] == 5
                assert len(data["zones"]) == 2
                assert data["zones"][0]["zone_key"] == "arkham/city"
                assert data["zones"][0]["npc_count"] == 3
            finally:
                overrides()

    def test_npc_system_status_unauthorized(self, client):
        """Test that NPC system status requires authentication."""
        response = client.get("/admin/npc/status")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_npc_system_status_success(self, client, mock_admin_user):
        """Test successful retrieval of NPC system status."""
        overrides = self._mock_auth(client, mock_admin_user)

        # Mock the NPC instance service
        async def mock_get_system_stats():
            return {
                "system_status": "healthy",
                "active_npcs": 5,
                "spawn_queue_size": 1,
                "lifecycle_manager_status": "active",
                "population_controller_status": "active",
                "spawning_service_status": "active",
                "last_update": "2025-01-01T12:00:00Z",
            }

        mock_service = MagicMock()
        mock_service.get_system_stats = mock_get_system_stats

        # Mock the get_npc_instance_service function directly
        with patch("server.api.admin.npc.get_npc_instance_service", return_value=mock_service):
            try:
                response = client.get("/admin/npc/status")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert data["system_status"] == "healthy"
                assert data["active_npcs"] == 5
                assert data["lifecycle_manager_status"] == "active"
                assert data["population_controller_status"] == "active"
            finally:
                overrides()

    # --- Enhanced Authentication Tests ---

    def test_admin_sessions_unauthorized(self, client):
        """Test that admin sessions endpoint requires authentication."""
        response = client.get("/admin/npc/admin/sessions")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_admin_sessions_success(self, client, mock_admin_user):
        """Test successful retrieval of admin sessions."""
        overrides = self._mock_auth(client, mock_admin_user)

        # Mock the admin auth service

        mock_service = MagicMock()
        mock_service.get_active_sessions.return_value = [
            {
                "user_id": "user_001",
                "username": "admin_user",
                "role": "admin",
                "ip_address": "127.0.0.1",
                "created_at": "2025-01-01T12:00:00Z",
                "last_activity": "2025-01-01T12:30:00Z",
                "action_count": 5,
            }
        ]

        # Mock the get_admin_auth_service function directly
        with patch("server.api.admin.npc.get_admin_auth_service", return_value=mock_service):
            try:
                response = client.get("/admin/npc/admin/sessions")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert "sessions" in data
                assert "count" in data
                assert data["count"] == 1
                assert data["sessions"][0]["username"] == "admin_user"
            finally:
                overrides()

    def test_admin_audit_log_unauthorized(self, client):
        """Test that admin audit log endpoint requires authentication."""
        response = client.get("/admin/npc/admin/audit-log")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_admin_audit_log_success(self, client, mock_admin_user):
        """Test successful retrieval of admin audit log."""
        overrides = self._mock_auth(client, mock_admin_user)

        # Mock the admin auth service

        mock_service = MagicMock()
        mock_service.get_audit_log.return_value = [
            {
                "timestamp": "2025-01-01T12:00:00Z",
                "user_id": "user_001",
                "username": "admin_user",
                "action": "get_population_stats",
                "result": "success",
                "ip_address": "127.0.0.1",
                "user_agent": "testclient",
            }
        ]

        # Mock the get_admin_auth_service function directly
        with patch("server.api.admin.npc.get_admin_auth_service", return_value=mock_service):
            try:
                response = client.get("/admin/npc/admin/audit-log?limit=50")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert "audit_log" in data
                assert "count" in data
                assert data["count"] == 1
                assert data["audit_log"][0]["action"] == "get_population_stats"
            finally:
                overrides()

    def test_cleanup_admin_sessions_unauthorized(self, client):
        """Test that cleanup admin sessions endpoint requires authentication."""
        response = client.post("/admin/npc/admin/cleanup-sessions")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_cleanup_admin_sessions_success(self, client, mock_admin_user):
        """Test successful cleanup of admin sessions."""
        overrides = self._mock_auth(client, mock_admin_user)

        # Mock the admin auth service

        mock_service = MagicMock()
        mock_service.cleanup_expired_sessions.return_value = 3

        # Mock the get_admin_auth_service function directly
        with patch("server.api.admin.npc.get_admin_auth_service", return_value=mock_service):
            try:
                response = client.post("/admin/npc/admin/cleanup-sessions")
                assert response.status_code == status.HTTP_200_OK

                data = response.json()
                assert "message" in data
                assert "cleaned_count" in data
                assert data["cleaned_count"] == 3
            finally:
                overrides()
