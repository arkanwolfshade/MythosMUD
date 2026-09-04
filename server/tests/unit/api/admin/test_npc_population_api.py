"""Unit tests for admin NPC population API endpoints."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException

from server.api.admin.npc_population_api import (
    get_npc_population_stats,
    get_npc_system_status,
    get_npc_zone_stats,
)
from server.exceptions import LoggedHTTPException


@pytest.fixture
def admin_user() -> MagicMock:
    user = MagicMock()
    user.id = "admin-id"
    return user


@pytest.mark.asyncio
async def test_get_npc_population_stats_success(admin_user: MagicMock) -> None:
    request = MagicMock()
    service = MagicMock()
    service.get_population_stats = AsyncMock(return_value={"total_npcs": 5, "by_zone": {}})
    auth = MagicMock()
    auth.get_username.return_value = "admin"
    with (
        patch("server.api.admin.npc_population_api.validate_admin_permission"),
        patch("server.api.admin.npc_population_api.get_npc_instance_service", return_value=service),
        patch("server.api.admin.npc_population_api.get_admin_auth_service", return_value=auth),
    ):
        result = await get_npc_population_stats(request, admin_user)
    assert result.total_npcs == 5


@pytest.mark.asyncio
async def test_get_npc_population_stats_http_exception_reraises(admin_user: MagicMock) -> None:
    request = MagicMock()
    with patch(
        "server.api.admin.npc_population_api.validate_admin_permission",
        side_effect=HTTPException(status_code=403, detail="forbidden"),
    ):
        with pytest.raises(HTTPException):
            await get_npc_population_stats(request, admin_user)


@pytest.mark.asyncio
async def test_get_npc_population_stats_generic_error(admin_user: MagicMock) -> None:
    request = MagicMock()
    service = MagicMock()
    service.get_population_stats = AsyncMock(side_effect=RuntimeError("db down"))
    with (
        patch("server.api.admin.npc_population_api.validate_admin_permission"),
        patch("server.api.admin.npc_population_api.get_npc_instance_service", return_value=service),
        patch("server.api.admin.npc_population_api.get_admin_auth_service", return_value=MagicMock()),
    ):
        with pytest.raises(LoggedHTTPException):
            await get_npc_population_stats(request, admin_user)


@pytest.mark.asyncio
async def test_get_npc_zone_stats_success(admin_user: MagicMock) -> None:
    request = MagicMock()
    service = MagicMock()
    service.get_zone_stats = AsyncMock(return_value={"zones": []})
    with (
        patch("server.api.admin.npc_population_api.validate_admin_permission"),
        patch("server.api.admin.npc_population_api.get_npc_instance_service", return_value=service),
        patch("server.api.admin.npc_population_api.get_admin_auth_service", return_value=MagicMock()),
    ):
        result = await get_npc_zone_stats(request, admin_user)
    assert result.zones == []


@pytest.mark.asyncio
async def test_get_npc_system_status_success(admin_user: MagicMock) -> None:
    request = MagicMock()
    service = MagicMock()
    service.get_system_stats = AsyncMock(return_value={"status": "ok", "active_npcs": 3})
    with (
        patch("server.api.admin.npc_population_api.validate_admin_permission"),
        patch("server.api.admin.npc_population_api.get_npc_instance_service", return_value=service),
        patch("server.api.admin.npc_population_api.get_admin_auth_service", return_value=MagicMock()),
    ):
        result = await get_npc_system_status(request, admin_user)
    assert result.status == "ok"
