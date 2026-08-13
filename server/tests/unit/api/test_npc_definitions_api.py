"""Unit tests for admin NPC definitions API."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException

from server.api.admin.npc_definitions_api import (
    _update_npc_definition_internal,
    create_npc_definition,
    delete_npc_definition,
    get_npc_definition,
    get_npc_definitions,
)
from server.api.admin.npc_schemas import (
    NPCAIIntegrationModel,
    NPCBaseStatsModel,
    NPCBehaviorConfigModel,
    NPCDefinitionCreate,
    NPCDefinitionUpdate,
)
from server.exceptions import LoggedHTTPException
from server.models.npc import NPCDefinitionType
from server.models.user import User


def _admin_user() -> User:
    return User(
        id="user-1",
        username="admin",
        email="admin@test.com",
        hashed_password="x",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )


def _mock_definition():
    definition = MagicMock()
    definition.id = 1
    definition.name = "Shopkeep"
    definition.npc_type = NPCDefinitionType.SHOPKEEPER
    definition.sub_zone_id = "arkham"
    definition.room_id = "room_1"
    definition.base_stats = "{}"
    definition.behavior_config = "{}"
    definition.ai_integration_stub = "{}"
    definition.created_at = None
    definition.updated_at = None
    return definition


@pytest.mark.asyncio
@patch("server.api.admin.npc_definitions_api.validate_admin_permission")
@patch("server.api.admin.npc_definitions_api.get_admin_auth_service")
@patch("server.api.admin.npc_definitions_api.npc_service")
async def test_get_npc_definitions(mock_service, mock_auth_svc, mock_validate):
    mock_auth_svc.return_value.get_username.return_value = "admin"
    definition = _mock_definition()
    mock_service.get_npc_definitions = AsyncMock(return_value=[definition])
    with patch("server.api.admin.npc_definitions_api.NPCDefinitionResponse") as resp_cls:
        resp_cls.from_orm.return_value = MagicMock(id=1)
        result = await get_npc_definitions(MagicMock(), _admin_user(), AsyncMock())
    assert len(result) == 1
    mock_validate.assert_called_once()


@pytest.mark.asyncio
@patch("server.api.admin.npc_definitions_api.validate_admin_permission", side_effect=HTTPException(status_code=403))
async def test_get_npc_definitions_http_exception(mock_validate):
    with pytest.raises(HTTPException):
        await get_npc_definitions(MagicMock(), _admin_user(), AsyncMock())


@pytest.mark.asyncio
@patch("server.api.admin.npc_definitions_api.validate_admin_permission")
@patch("server.api.admin.npc_definitions_api.get_admin_auth_service")
@patch("server.api.admin.npc_definitions_api.npc_service")
async def test_get_npc_definition_found(mock_service, mock_auth_svc, mock_validate):
    mock_auth_svc.return_value.get_username.return_value = "admin"
    definition = _mock_definition()
    mock_service.get_npc_definition = AsyncMock(return_value=definition)
    with patch("server.api.admin.npc_definitions_api.NPCDefinitionResponse") as resp_cls:
        resp_cls.from_orm.return_value = MagicMock(id=1)
        result = await get_npc_definition(1, MagicMock(), _admin_user(), AsyncMock())
    assert result.id == 1


@pytest.mark.asyncio
@patch("server.api.admin.npc_definitions_api.validate_admin_permission")
@patch("server.api.admin.npc_definitions_api.get_admin_auth_service")
@patch("server.api.admin.npc_definitions_api.npc_service")
async def test_get_npc_definition_not_found(mock_service, mock_auth_svc, mock_validate):
    mock_auth_svc.return_value.get_username.return_value = "admin"
    mock_service.get_npc_definition = AsyncMock(return_value=None)
    with pytest.raises(LoggedHTTPException) as exc:
        await get_npc_definition(99, MagicMock(), _admin_user(), AsyncMock())
    assert exc.value.status_code == 404


@pytest.mark.asyncio
@patch("server.api.admin.npc_definitions_api.validate_admin_permission")
@patch("server.api.admin.npc_definitions_api.get_admin_auth_service")
@patch("server.api.admin.npc_definitions_api.npc_service")
@patch("server.api.admin.npc_definitions_api.build_update_params_from_model")
async def test_update_npc_definition_internal(mock_build, mock_service, mock_auth_svc, mock_validate):
    mock_auth_svc.return_value.get_username.return_value = "admin"
    mock_build.return_value = MagicMock()
    definition = _mock_definition()
    mock_service.update_npc_definition = AsyncMock(return_value=definition)
    session = AsyncMock()
    body = NPCDefinitionUpdate(name="Updated")
    with patch("server.api.admin.npc_definitions_api.NPCDefinitionResponse") as resp_cls:
        resp_cls.from_orm.return_value = MagicMock(id=1)
        result = await _update_npc_definition_internal(1, body, MagicMock(), _admin_user(), session)
    session.commit.assert_awaited_once()
    assert result.id == 1


@pytest.mark.asyncio
@patch("server.api.admin.npc_definitions_api.validate_admin_permission")
@patch("server.api.admin.npc_definitions_api.get_admin_auth_service")
@patch("server.api.admin.npc_definitions_api.npc_service")
@patch("server.api.admin.npc_definitions_api.build_update_params_from_model")
async def test_update_npc_definition_not_found(mock_build, mock_service, mock_auth_svc, mock_validate):
    mock_auth_svc.return_value.get_username.return_value = "admin"
    mock_build.return_value = MagicMock()
    mock_service.update_npc_definition = AsyncMock(return_value=None)
    session = AsyncMock()
    with pytest.raises(LoggedHTTPException) as exc:
        await _update_npc_definition_internal(99, NPCDefinitionUpdate(), MagicMock(), _admin_user(), session)
    assert exc.value.status_code == 404


@pytest.mark.asyncio
@patch("server.api.admin.npc_definitions_api.validate_admin_permission")
@patch("server.api.admin.npc_definitions_api.get_admin_auth_service")
@patch("server.api.admin.npc_definitions_api.npc_service")
async def test_delete_npc_definition(mock_service, mock_auth_svc, mock_validate):
    mock_auth_svc.return_value.get_username.return_value = "admin"
    mock_service.delete_npc_definition = AsyncMock(return_value=True)
    session = AsyncMock()
    await delete_npc_definition(1, MagicMock(), _admin_user(), session)
    session.commit.assert_awaited_once()


@pytest.mark.asyncio
@patch("server.api.admin.npc_definitions_api.validate_admin_permission")
@patch("server.api.admin.npc_definitions_api.get_admin_auth_service")
@patch("server.api.admin.npc_definitions_api.npc_service")
async def test_delete_npc_definition_not_found(mock_service, mock_auth_svc, mock_validate):
    mock_auth_svc.return_value.get_username.return_value = "admin"
    mock_service.delete_npc_definition = AsyncMock(return_value=False)
    session = AsyncMock()
    with pytest.raises(LoggedHTTPException) as exc:
        await delete_npc_definition(99, MagicMock(), _admin_user(), session)
    assert exc.value.status_code == 404


@pytest.mark.asyncio
@patch("server.api.admin.npc_definitions_api.validate_admin_permission")
@patch("server.api.admin.npc_definitions_api.get_admin_auth_service")
@patch("server.api.admin.npc_definitions_api.npc_service")
async def test_create_npc_definition(mock_service, mock_auth_svc, mock_validate):
    mock_auth_svc.return_value.get_username.return_value = "admin"
    definition = _mock_definition()

    async def fake_session():
        session = AsyncMock()
        yield session

    mock_service.create_npc_definition = AsyncMock(return_value=definition)
    body = NPCDefinitionCreate(
        name="Shopkeep",
        npc_type=NPCDefinitionType.SHOPKEEPER,
        sub_zone_id="arkham",
        room_id="room_1",
        base_stats=NPCBaseStatsModel(),
        behavior_config=NPCBehaviorConfigModel(),
        ai_integration_stub=NPCAIIntegrationModel(),
    )
    with (
        patch("server.api.admin.npc_definitions_api.get_npc_session", return_value=fake_session()),
        patch("server.api.admin.npc_definitions_api.NPCDefinitionResponse") as resp_cls,
    ):
        resp_cls.from_orm.return_value = MagicMock(id=1)
        result = await create_npc_definition(body, MagicMock(), _admin_user())
    assert result.id == 1


@pytest.mark.asyncio
@patch("server.api.admin.npc_definitions_api.validate_admin_permission", side_effect=Exception("db down"))
async def test_get_npc_definitions_internal_error(mock_validate):
    with pytest.raises(LoggedHTTPException) as exc:
        await get_npc_definitions(MagicMock(), _admin_user(), AsyncMock())
    assert exc.value.status_code == 500
