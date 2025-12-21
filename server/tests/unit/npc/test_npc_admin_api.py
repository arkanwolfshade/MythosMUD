"""
Tests for NPC Admin API endpoints.

This module tests all NPC administrative API operations including
definition management, instance control, population monitoring, and spawn rules.

As the Necronomicon instructs: "Control over the entities requires vigilant testing
of all administrative protocols and containment procedures."
"""

import json
from typing import Any, cast
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import HTTPException, Request

from server.api.admin.npc import (
    NPCDefinitionCreate,
    NPCDefinitionResponse,
    NPCDefinitionUpdate,
    NPCMoveRequest,
    NPCSpawnRequest,
    NPCSpawnRuleCreate,
    NPCSpawnRuleResponse,
    cleanup_admin_sessions,
    create_npc_definition,
    create_npc_spawn_rule,
    delete_npc_definition,
    despawn_npc_instance,
    get_admin_audit_log,
    get_admin_sessions,
    get_npc_definition,
    get_npc_definitions,
    get_npc_instances,
    get_npc_population_stats,
    get_npc_spawn_rules,
    get_npc_stats,
    get_npc_system_status,
    get_npc_zone_stats,
    move_npc_instance,
    spawn_npc_instance,
    update_npc_definition,
    validate_admin_permission,
)
from server.exceptions import LoggedHTTPException
from server.models.npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
from server.services.admin_auth_service import AdminAction


@pytest.fixture
def mock_current_user():
    """Create mock authenticated user with admin permissions."""
    user = {"user_id": "test_user_001", "username": "testadmin", "is_admin": True}
    return user


@pytest.fixture
def mock_request():
    """Create mock FastAPI request."""
    request = Mock(spec=Request)
    request.client = Mock()
    request.client.host = "127.0.0.1"
    request.url = Mock()
    request.url.path = "/admin/npc/test"
    return request


@pytest.fixture
def sample_npc_definition():
    """Create sample NPC definition."""
    return NPCDefinition(
        id=1,
        name="Test Shopkeeper",
        description="A friendly merchant",
        npc_type="shopkeeper",
        sub_zone_id="arkhamcity_downtown",
        room_id="earth_arkhamcity_downtown_001",
        required_npc=False,
        max_population=1,
        spawn_probability=1.0,
        base_stats=json.dumps({"health": 100}),
        behavior_config=json.dumps({"friendly": True}),
        ai_integration_stub=json.dumps({}),
    )


class TestNPCDefinitionResponseModel:
    """Test NPCDefinitionResponse Pydantic model."""

    def test_from_orm_with_string_json_fields(self, sample_npc_definition):
        """Test from_orm converts string JSON fields correctly."""
        response = NPCDefinitionResponse.from_orm(sample_npc_definition)

        assert response.id == 1
        assert response.name == "Test Shopkeeper"
        assert response.npc_type == "shopkeeper"
        assert isinstance(response.base_stats, dict)
        assert response.base_stats == {"health": 100}

    def test_from_orm_with_dict_json_fields(self) -> None:
        """Test from_orm handles fields already as dicts."""
        definition = MagicMock()
        definition.id = 1
        definition.name = "Test"
        definition.npc_type = "shopkeeper"
        definition.sub_zone_id = "zone"
        definition.room_id = "room"
        definition.base_stats = {"health": 100}  # Already a dict
        definition.behavior_config = {"friendly": True}
        definition.ai_integration_stub = {}

        response = NPCDefinitionResponse.from_orm(definition)

        assert response.base_stats == {"health": 100}
        assert response.behavior_config == {"friendly": True}


class TestNPCSpawnRuleResponseModel:
    """Test NPCSpawnRuleResponse Pydantic model."""

    def test_from_orm_with_string_conditions(self) -> None:
        """Test from_orm converts string conditions correctly."""
        rule = NPCSpawnRule(
            id=1,
            npc_definition_id=1,
            sub_zone_id="zone",
            min_population=0,
            max_population=10,
            spawn_conditions=json.dumps({"time": "day"}),
        )

        response = NPCSpawnRuleResponse.from_orm(rule)

        assert response.id == 1
        assert isinstance(response.spawn_conditions, dict)
        assert response.spawn_conditions == {"time": "day"}


class TestValidateAdminPermission:
    """Test admin permission validation helper."""

    @patch("server.api.admin.npc.get_admin_auth_service")
    def test_validate_admin_permission_success(self, mock_get_auth, mock_current_user, mock_request):
        """Test successful permission validation."""
        mock_auth_service = MagicMock()
        mock_auth_service.validate_permission = MagicMock()
        mock_get_auth.return_value = mock_auth_service

        # Should not raise
        validate_admin_permission(mock_current_user, AdminAction.LIST_NPC_DEFINITIONS, mock_request)

        mock_auth_service.validate_permission.assert_called_once()

    @patch("server.api.admin.npc.get_admin_auth_service")
    def test_validate_admin_permission_failure(self, mock_get_auth, mock_current_user, mock_request):
        """Test permission validation failure raises HTTPException."""
        mock_auth_service = MagicMock()
        mock_auth_service.validate_permission = MagicMock(
            side_effect=HTTPException(status_code=403, detail="Forbidden")
        )
        mock_get_auth.return_value = mock_auth_service

        with pytest.raises(HTTPException):
            validate_admin_permission(mock_current_user, cast(AdminAction, "dangerous_action"), mock_request)


class TestGetNPCDefinitionsEndpoint:
    """Test GET /admin/npc/definitions endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_async_session")
    @patch("server.api.admin.npc.npc_service")
    async def test_get_npc_definitions_success(
        self,
        mock_npc_service,
        mock_get_session,
        mock_get_auth,
        mock_validate,
        mock_current_user,
        mock_request,
        sample_npc_definition,
    ):
        """Test successful retrieval of NPC definitions."""
        # Setup mocks
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_session = AsyncMock()

        async def mock_session_generator():
            yield mock_session

        mock_get_session.return_value = mock_session_generator()
        mock_npc_service.get_npc_definitions = AsyncMock(return_value=[sample_npc_definition])

        # Call endpoint
        result = await get_npc_definitions(current_user=mock_current_user, request=cast(Any, mock_request))

        assert len(result) == 1
        assert result[0].name == "Test Shopkeeper"

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    async def test_get_npc_definitions_permission_denied(self, mock_validate, mock_current_user, mock_request):
        """Test permission denial returns 403."""
        mock_validate.side_effect = HTTPException(status_code=403, detail="Forbidden")

        with pytest.raises(HTTPException) as exc_info:
            await get_npc_definitions(current_user=mock_current_user, request=cast(Any, mock_request))

        assert exc_info.value.status_code == 403


class TestCreateNPCDefinitionEndpoint:
    """Test POST /admin/npc/definitions endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_npc_session")
    @patch("server.api.admin.npc.npc_service")
    async def test_create_npc_definition_success(
        self,
        mock_npc_service,
        mock_get_npc_session,
        mock_get_auth,
        mock_validate,
        mock_current_user,
        mock_request,
        sample_npc_definition,
    ):
        """Test successful NPC definition creation."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_session = AsyncMock()
        mock_session.commit = AsyncMock()

        async def mock_session_generator():
            yield mock_session

        mock_get_npc_session.return_value = mock_session_generator()
        mock_npc_service.create_npc_definition = AsyncMock(return_value=sample_npc_definition)

        npc_data = NPCDefinitionCreate(
            name="New Shopkeeper",
            npc_type=NPCDefinitionType.SHOPKEEPER,
            sub_zone_id="arkhamcity_downtown",
            room_id="earth_arkhamcity_downtown_001",
        )

        result = await create_npc_definition(
            npc_data=npc_data, current_user=mock_current_user, request=cast(Any, mock_request)
        )

        assert result.name == "Test Shopkeeper"
        mock_session.commit.assert_called_once()


class TestGetNPCDefinitionEndpoint:
    """Test GET /admin/npc/definitions/{definition_id} endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_async_session")
    @patch("server.api.admin.npc.npc_service")
    async def test_get_npc_definition_success(
        self,
        mock_npc_service,
        mock_get_session,
        mock_get_auth,
        mock_validate,
        mock_current_user,
        mock_request,
        sample_npc_definition,
    ):
        """Test successful retrieval of single definition."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_session = AsyncMock()

        async def mock_session_generator():
            yield mock_session

        mock_get_session.return_value = mock_session_generator()
        mock_npc_service.get_npc_definition = AsyncMock(return_value=sample_npc_definition)

        result = await get_npc_definition(
            definition_id=1, current_user=mock_current_user, request=cast(Any, mock_request)
        )

        assert result.id == 1
        assert result.name == "Test Shopkeeper"

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_async_session")
    @patch("server.api.admin.npc.npc_service")
    async def test_get_npc_definition_not_found(
        self, mock_npc_service, mock_get_session, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test 404 when definition not found."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_session = AsyncMock()

        async def mock_session_generator():
            yield mock_session

        mock_get_session.return_value = mock_session_generator()
        mock_npc_service.get_npc_definition = AsyncMock(return_value=None)

        with pytest.raises(HTTPException) as exc_info:
            await get_npc_definition(definition_id=999, current_user=mock_current_user, request=cast(Any, mock_request))

        assert exc_info.value.status_code == 404


class TestUpdateNPCDefinitionEndpoint:
    """Test PUT /admin/npc/definitions/{definition_id} endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.npc_service")
    async def test_update_npc_definition_success(
        self, mock_npc_service, mock_get_auth, mock_validate, mock_current_user, mock_request, sample_npc_definition
    ):
        """Test successful NPC definition update."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_session = AsyncMock()
        mock_session.commit = AsyncMock()
        mock_npc_service.update_npc_definition = AsyncMock(return_value=sample_npc_definition)

        npc_data = NPCDefinitionUpdate(name="Updated Name")

        result = await update_npc_definition(
            definition_id=1,
            npc_data=npc_data,
            current_user=mock_current_user,
            session=mock_session,
            request=cast(Any, mock_request),
        )

        assert result.id == 1
        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.npc_service")
    async def test_update_npc_definition_not_found(
        self, mock_npc_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test updating non-existent definition."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_session = AsyncMock()
        mock_npc_service.update_npc_definition = AsyncMock(return_value=None)

        npc_data = NPCDefinitionUpdate(name="Updated Name")

        with pytest.raises(HTTPException) as exc_info:
            await update_npc_definition(
                definition_id=999,
                npc_data=npc_data,
                current_user=mock_current_user,
                session=mock_session,
                request=cast(Any, mock_request),
            )

        assert exc_info.value.status_code == 404


class TestDeleteNPCDefinitionEndpoint:
    """Test DELETE /admin/npc/definitions/{definition_id} endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.npc_service")
    async def test_delete_npc_definition_success(
        self, mock_npc_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test successful NPC definition deletion."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_session = AsyncMock()
        mock_session.commit = AsyncMock()
        mock_npc_service.delete_npc_definition = AsyncMock(return_value=True)

        # No result returned for 204 No Content
        await delete_npc_definition(
            definition_id=1, current_user=mock_current_user, session=mock_session, request=cast(Any, mock_request)
        )

        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.npc_service")
    async def test_delete_npc_definition_not_found(
        self, mock_npc_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test deleting non-existent definition."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_session = AsyncMock()
        mock_npc_service.delete_npc_definition = AsyncMock(return_value=False)

        with pytest.raises(HTTPException) as exc_info:
            await delete_npc_definition(
                definition_id=999, current_user=mock_current_user, session=mock_session, request=cast(Any, mock_request)
            )

        assert exc_info.value.status_code == 404


class TestGetNPCInstancesEndpoint:
    """Test GET /admin/npc/instances endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_npc_instance_service")
    async def test_get_npc_instances_success(
        self, mock_get_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test successful retrieval of NPC instances."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_instance_service = AsyncMock()
        mock_instance_service.get_npc_instances = AsyncMock(
            return_value=[{"npc_id": "npc_001", "name": "Test NPC", "room_id": "earth_arkham_001"}]
        )
        mock_get_service.return_value = mock_instance_service

        result = await get_npc_instances(current_user=mock_current_user, request=cast(Any, mock_request))

        assert len(result) == 1
        assert result[0]["npc_id"] == "npc_001"


class TestSpawnNPCInstanceEndpoint:
    """Test POST /admin/npc/instances/spawn endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_npc_instance_service")
    async def test_spawn_npc_instance_success(
        self, mock_get_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test successful NPC instance spawning."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_instance_service = AsyncMock()
        mock_instance_service.spawn_npc_instance = AsyncMock(
            return_value={
                "success": True,
                "npc_id": "npc_001",
                "definition_id": 1,
                "room_id": "earth_arkham_001",
                "message": "Spawned successfully",
            }
        )
        mock_get_service.return_value = mock_instance_service

        spawn_data = NPCSpawnRequest(definition_id=1, room_id="earth_arkham_001")

        result = await spawn_npc_instance(
            spawn_data=spawn_data, current_user=mock_current_user, request=cast(Any, mock_request)
        )

        assert result["success"] is True
        assert result["npc_id"] == "npc_001"

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_npc_instance_service")
    async def test_spawn_npc_instance_definition_not_found(
        self, mock_get_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test spawning with invalid definition ID."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_instance_service = AsyncMock()
        mock_instance_service.spawn_npc_instance = AsyncMock(side_effect=ValueError("Definition not found"))
        mock_get_service.return_value = mock_instance_service

        spawn_data = NPCSpawnRequest(definition_id=999, room_id="earth_arkham_001")

        with pytest.raises(HTTPException) as exc_info:
            await spawn_npc_instance(
                spawn_data=spawn_data, current_user=mock_current_user, request=cast(Any, mock_request)
            )

        assert exc_info.value.status_code == 404


class TestDespawnNPCInstanceEndpoint:
    """Test DELETE /admin/npc/instances/{npc_id} endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_npc_instance_service")
    async def test_despawn_npc_instance_success(
        self, mock_get_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test successful NPC instance despawning."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_instance_service = AsyncMock()
        mock_instance_service.despawn_npc_instance = AsyncMock(
            return_value={"success": True, "npc_id": "npc_001", "npc_name": "Test NPC", "message": "Despawned"}
        )
        mock_get_service.return_value = mock_instance_service

        result = await despawn_npc_instance(
            npc_id="npc_001", current_user=mock_current_user, request=cast(Any, mock_request)
        )

        assert result["success"] is True
        assert result["npc_id"] == "npc_001"

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_npc_instance_service")
    async def test_despawn_npc_instance_not_found(
        self, mock_get_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test despawning non-existent NPC."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_instance_service = AsyncMock()
        mock_instance_service.despawn_npc_instance = AsyncMock(side_effect=ValueError("NPC not found"))
        mock_get_service.return_value = mock_instance_service

        with pytest.raises(HTTPException) as exc_info:
            await despawn_npc_instance(
                npc_id="npc_invalid", current_user=mock_current_user, request=cast(Any, mock_request)
            )

        assert exc_info.value.status_code == 404


class TestMoveNPCInstanceEndpoint:
    """Test PUT /admin/npc/instances/{npc_id}/move endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_npc_instance_service")
    async def test_move_npc_instance_success(
        self, mock_get_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test successful NPC instance movement."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_instance_service = AsyncMock()
        mock_instance_service.move_npc_instance = AsyncMock(
            return_value={
                "success": True,
                "npc_id": "npc_001",
                "npc_name": "Test NPC",
                "old_room_id": "earth_arkham_001",
                "new_room_id": "earth_arkham_002",
                "message": "Moved successfully",
            }
        )
        mock_get_service.return_value = mock_instance_service

        move_data = NPCMoveRequest(room_id="earth_arkham_002")

        result = await move_npc_instance(
            npc_id="npc_001", move_data=move_data, current_user=mock_current_user, request=cast(Any, mock_request)
        )

        assert result["success"] is True
        assert result["new_room_id"] == "earth_arkham_002"


class TestGetNPCStatsEndpoint:
    """Test GET /admin/npc/instances/{npc_id}/stats endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_npc_instance_service")
    async def test_get_npc_stats_success(
        self, mock_get_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test successful NPC stats retrieval."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_instance_service = AsyncMock()
        mock_instance_service.get_npc_stats = AsyncMock(
            return_value={"npc_id": "npc_001", "name": "Test NPC", "stats": {"health": 100}}
        )
        mock_get_service.return_value = mock_instance_service

        result = await get_npc_stats(npc_id="npc_001", current_user=mock_current_user, request=cast(Any, mock_request))

        assert result["npc_id"] == "npc_001"
        assert result["name"] == "Test NPC"


class TestPopulationStatsEndpoint:
    """Test GET /admin/npc/population endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_npc_instance_service")
    async def test_get_population_stats_success(
        self, mock_get_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test successful population stats retrieval."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_instance_service = AsyncMock()
        mock_instance_service.get_population_stats = AsyncMock(
            return_value={"total_npcs": 5, "by_type": {"shopkeeper": 3, "guard": 2}, "by_zone": {"arkham": 5}}
        )
        mock_get_service.return_value = mock_instance_service

        result = await get_npc_population_stats(current_user=mock_current_user, request=cast(Any, mock_request))

        assert result["total_npcs"] == 5
        assert result["by_type"]["shopkeeper"] == 3


class TestZoneStatsEndpoint:
    """Test GET /admin/npc/zones endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_npc_instance_service")
    async def test_get_zone_stats_success(
        self, mock_get_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test successful zone stats retrieval."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_instance_service = AsyncMock()
        mock_instance_service.get_zone_stats = AsyncMock(
            return_value={"total_zones": 2, "total_npcs": 5, "zones": [{"zone_key": "arkham", "npc_count": 5}]}
        )
        mock_get_service.return_value = mock_instance_service

        result = await get_npc_zone_stats(current_user=mock_current_user, request=cast(Any, mock_request))

        assert result["total_zones"] == 2
        assert result["total_npcs"] == 5


class TestSystemStatusEndpoint:
    """Test GET /admin/npc/status endpoint."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_npc_instance_service")
    async def test_get_system_status_success(
        self, mock_get_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test successful system status retrieval."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_instance_service = AsyncMock()
        mock_instance_service.get_system_stats = AsyncMock(
            return_value={"system_status": "healthy", "active_npcs": 5, "spawn_queue_size": 2}
        )
        mock_get_service.return_value = mock_instance_service

        result = await get_npc_system_status(current_user=mock_current_user, request=cast(Any, mock_request))

        assert result["system_status"] == "healthy"
        assert result["active_npcs"] == 5


class TestSpawnRulesEndpoints:
    """Test spawn rule management endpoints."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.npc_service")
    async def test_get_spawn_rules_success(
        self, mock_npc_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test successful spawn rules retrieval."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_session = AsyncMock()

        sample_rule = NPCSpawnRule(
            id=1,
            npc_definition_id=1,
            sub_zone_id="zone",
            min_population=0,
            max_population=10,
            spawn_conditions=json.dumps({"time": "day"}),
        )

        mock_npc_service.get_spawn_rules = AsyncMock(return_value=[sample_rule])

        result = await get_npc_spawn_rules(
            current_user=mock_current_user, session=mock_session, request=cast(Any, mock_request)
        )

        assert len(result) == 1
        assert result[0].id == 1

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.npc_service")
    async def test_create_spawn_rule_success(
        self, mock_npc_service, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test successful spawn rule creation."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_session = AsyncMock()
        mock_session.commit = AsyncMock()

        sample_rule = NPCSpawnRule(
            id=1,
            npc_definition_id=1,
            sub_zone_id="default",
            min_population=0,
            max_population=999,
            spawn_conditions=json.dumps({}),
        )

        mock_npc_service.create_spawn_rule = AsyncMock(return_value=sample_rule)

        spawn_rule_data = NPCSpawnRuleCreate(npc_definition_id=1, sub_zone_id="default", max_population=5)

        result = await create_npc_spawn_rule(
            spawn_rule_data=spawn_rule_data,
            current_user=mock_current_user,
            session=mock_session,
            request=cast(Any, mock_request),
        )

        assert result.id == 1
        mock_session.commit.assert_called_once()


class TestAdminManagementEndpoints:
    """Test admin management endpoints."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    async def test_get_admin_sessions_success(self, mock_get_auth, mock_validate, mock_current_user, mock_request):
        """Test successful admin sessions retrieval."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_auth_service.get_active_sessions.return_value = [
            {"session_id": "session_001", "user": "admin1"},
            {"session_id": "session_002", "user": "admin2"},
        ]
        mock_get_auth.return_value = mock_auth_service

        result = await get_admin_sessions(current_user=mock_current_user, request=cast(Any, mock_request))

        assert result["count"] == 2
        assert len(result["sessions"]) == 2

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    async def test_get_audit_log_success(self, mock_get_auth, mock_validate, mock_current_user, mock_request):
        """Test successful audit log retrieval."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_auth_service.get_audit_log.return_value = [
            {"action": "spawn_npc", "user": "admin1", "timestamp": "2025-01-01"}
        ]
        mock_get_auth.return_value = mock_auth_service

        result = await get_admin_audit_log(limit=100, current_user=mock_current_user, request=cast(Any, mock_request))

        assert result["count"] == 1
        assert len(result["audit_log"]) == 1

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    async def test_cleanup_sessions_success(self, mock_get_auth, mock_validate, mock_current_user, mock_request):
        """Test successful session cleanup."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_auth_service.cleanup_expired_sessions.return_value = 3
        mock_get_auth.return_value = mock_auth_service

        result = await cleanup_admin_sessions(current_user=mock_current_user, request=cast(Any, mock_request))

        assert result["cleaned_count"] == 3
        assert "Cleaned up" in result["message"]


class TestErrorHandling:
    """Test error handling across endpoints."""

    @pytest.mark.asyncio
    @patch("server.api.admin.npc.validate_admin_permission")
    @patch("server.api.admin.npc.get_admin_auth_service")
    @patch("server.api.admin.npc.get_npc_session")
    @patch("server.api.admin.npc.npc_service")
    async def test_endpoint_handles_generic_exceptions(
        self, mock_npc_service, mock_get_npc_session, mock_get_auth, mock_validate, mock_current_user, mock_request
    ):
        """Test endpoints handle generic exceptions."""
        mock_validate.return_value = None
        mock_auth_service = MagicMock()
        mock_auth_service.get_username.return_value = "testadmin"
        mock_get_auth.return_value = mock_auth_service

        mock_session = AsyncMock()

        async def mock_session_generator():
            yield mock_session

        mock_get_npc_session.return_value = mock_session_generator()
        mock_npc_service.get_npc_definitions = AsyncMock(side_effect=RuntimeError("Database failure"))

        with pytest.raises(LoggedHTTPException, match="Error retrieving NPC definitions"):
            await get_npc_definitions(current_user=mock_current_user, request=cast(Any, mock_request))


class TestPydanticModelValidation:
    """Test Pydantic model validation in requests."""

    def test_npc_definition_create_validates_fields(self) -> None:
        """Test NPCDefinitionCreate validates required fields."""
        with pytest.raises(ValueError):
            NPCDefinitionCreate(
                name="",  # Too short
                npc_type=NPCDefinitionType.SHOPKEEPER,
                sub_zone_id="zone",
                room_id="room",
            )

    def test_npc_spawn_request_validates_definition_id(self) -> None:
        """Test NPCSpawnRequest validates definition_id > 0."""
        with pytest.raises(ValueError):
            NPCSpawnRequest(definition_id=0, room_id="room")  # Must be > 0

    def test_npc_spawn_rule_create_validates_probability(self) -> None:
        """Test NPCSpawnRuleCreate validates spawn probability range."""
        # Note: spawn_probability is not a field on NPCSpawnRuleCreate (it's on NPCDefinition)
        # This test verifies that Pydantic raises ValidationError for unknown fields
        from pydantic import ValidationError

        with pytest.raises(ValidationError):
            NPCSpawnRuleCreate(  # type: ignore[call-arg]  # Intentionally passing invalid field to test Pydantic validation
                npc_definition_id=1, sub_zone_id="test_zone", spawn_probability=1.5, max_population=5
            )  # spawn_probability is not a valid field
