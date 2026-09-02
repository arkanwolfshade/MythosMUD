"""Unit tests for admin NPC instances API endpoints."""

from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from pydantic import ValidationError

from server.api.admin.npc_instances_api import (
    despawn_npc_instance,
    get_npc_instances,
    get_npc_stats,
    move_npc_instance,
    spawn_npc_instance,
)
from server.api.admin.npc_schemas import NPCMoveRequest, NPCSpawnRequest
from server.exceptions import LoggedHTTPException
from server.schemas.shared.base import SecureBaseModel


@pytest.mark.parametrize(
    "model_cls,payload",
    [
        (NPCSpawnRequest, {"definition_id": 1, "room_id": "room-1"}),
        (NPCMoveRequest, {"room_id": "room-1"}),
    ],
)
def test_npc_instance_request_schemas_reject_unknown_field(
    model_cls: type[SecureBaseModel], payload: dict[str, object]
) -> None:
    """#755: NPCSpawnRequest/NPCMoveRequest now inherit SecureBaseModel - extra fields rejected."""
    with pytest.raises(ValidationError):
        _ = model_cls.model_validate({**payload, "unexpected_field": "nope"})


@pytest.fixture
def admin_user() -> MagicMock:
    user = MagicMock()
    user.id = "admin-id"
    return user


@pytest.mark.asyncio
async def test_get_npc_instances_success(admin_user: MagicMock) -> None:
    request = MagicMock()
    service = MagicMock()
    service.get_npc_instances = AsyncMock(return_value=[{"npc_id": "npc-1"}])
    auth = MagicMock()
    auth.get_username.return_value = "admin"
    with (
        patch("server.api.admin.npc_instances_api.validate_admin_permission"),
        patch("server.api.admin.npc_instances_api.get_npc_instance_service", return_value=service),
        patch("server.api.admin.npc_instances_api.get_admin_auth_service", return_value=auth),
    ):
        result = await get_npc_instances(request, admin_user)
    assert result == [{"npc_id": "npc-1"}]


@pytest.mark.asyncio
async def test_spawn_npc_instance_success(admin_user: MagicMock) -> None:
    request = MagicMock()
    body = NPCSpawnRequest(definition_id=1, room_id="room-1")
    service = MagicMock()
    service.spawn_npc_instance = AsyncMock(return_value={"npc_id": "npc-new", "definition_id": 1, "room_id": "room-1"})
    auth = MagicMock()
    auth.get_username.return_value = "admin"
    with (
        patch("server.api.admin.npc_instances_api.validate_admin_permission"),
        patch("server.api.admin.npc_instances_api.get_npc_instance_service", return_value=service),
        patch("server.api.admin.npc_instances_api.get_admin_auth_service", return_value=auth),
    ):
        result = await spawn_npc_instance(body, request, admin_user)
    assert result.npc_id == "npc-new"


@pytest.mark.asyncio
async def test_spawn_npc_instance_not_found(admin_user: MagicMock) -> None:
    request = MagicMock()
    body = NPCSpawnRequest(definition_id=99, room_id="room-x")
    service = MagicMock()
    service.spawn_npc_instance = AsyncMock(side_effect=ValueError("missing definition"))
    with (
        patch("server.api.admin.npc_instances_api.validate_admin_permission"),
        patch("server.api.admin.npc_instances_api.get_npc_instance_service", return_value=service),
        patch("server.api.admin.npc_instances_api.get_admin_auth_service", return_value=MagicMock()),
    ):
        with pytest.raises(LoggedHTTPException):
            await spawn_npc_instance(body, request, admin_user)


@pytest.mark.asyncio
async def test_despawn_npc_instance_success(admin_user: MagicMock) -> None:
    request = MagicMock()
    service = MagicMock()
    service.despawn_npc_instance = AsyncMock(return_value={"npc_id": "npc-1", "npc_name": "Mob"})
    with (
        patch("server.api.admin.npc_instances_api.validate_admin_permission"),
        patch("server.api.admin.npc_instances_api.get_npc_instance_service", return_value=service),
        patch("server.api.admin.npc_instances_api.get_admin_auth_service", return_value=MagicMock()),
    ):
        result = await despawn_npc_instance("npc-1", request, admin_user)
    assert result.npc_id == "npc-1"


@pytest.mark.asyncio
async def test_move_npc_instance_success(admin_user: MagicMock) -> None:
    request = MagicMock()
    body = NPCMoveRequest(room_id="room-b")
    service = MagicMock()
    service.move_npc_instance = AsyncMock(
        return_value={"npc_id": "npc-1", "old_room_id": "room-a", "new_room_id": "room-b"}
    )
    with (
        patch("server.api.admin.npc_instances_api.validate_admin_permission"),
        patch("server.api.admin.npc_instances_api.get_npc_instance_service", return_value=service),
        patch("server.api.admin.npc_instances_api.get_admin_auth_service", return_value=MagicMock()),
    ):
        result = await move_npc_instance("npc-1", body, request, admin_user)
    assert result.new_room_id == "room-b"


@pytest.mark.asyncio
async def test_get_npc_stats_success(admin_user: MagicMock) -> None:
    request = MagicMock()
    service = MagicMock()
    service.get_npc_stats = AsyncMock(return_value={"name": "Mob", "hp": 10})
    with (
        patch("server.api.admin.npc_instances_api.validate_admin_permission"),
        patch("server.api.admin.npc_instances_api.get_npc_instance_service", return_value=service),
        patch("server.api.admin.npc_instances_api.get_admin_auth_service", return_value=MagicMock()),
    ):
        result = await get_npc_stats("npc-1", request, admin_user)
    # NPCStatsResponse is deliberately field-less (extra="allow") to pass through whatever
    # the instance service returns, so "name" only exists as an extra field, not a declared
    # attribute - go through model_extra rather than static attribute access.
    extra = cast(dict[str, object], result.model_extra or {})
    assert extra.get("name") == "Mob"


@pytest.mark.asyncio
async def test_get_npc_instances_server_error(admin_user: MagicMock) -> None:
    request = MagicMock()
    service = MagicMock()
    service.get_npc_instances = AsyncMock(side_effect=RuntimeError("db down"))
    with (
        patch("server.api.admin.npc_instances_api.validate_admin_permission"),
        patch("server.api.admin.npc_instances_api.get_npc_instance_service", return_value=service),
        patch("server.api.admin.npc_instances_api.get_admin_auth_service", return_value=MagicMock()),
    ):
        with pytest.raises(LoggedHTTPException):
            await get_npc_instances(request, admin_user)


@pytest.mark.asyncio
async def test_despawn_npc_instance_not_found(admin_user: MagicMock) -> None:
    request = MagicMock()
    service = MagicMock()
    service.despawn_npc_instance = AsyncMock(side_effect=ValueError("missing npc"))
    with (
        patch("server.api.admin.npc_instances_api.validate_admin_permission"),
        patch("server.api.admin.npc_instances_api.get_npc_instance_service", return_value=service),
        patch("server.api.admin.npc_instances_api.get_admin_auth_service", return_value=MagicMock()),
    ):
        with pytest.raises(LoggedHTTPException):
            await despawn_npc_instance("npc-x", request, admin_user)
