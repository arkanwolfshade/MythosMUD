"""Unit tests for admin NPC management API endpoints."""

from unittest.mock import MagicMock, patch

import pytest
from fastapi import HTTPException

from server.api.admin.npc_admin_mgmt_api import (
    cleanup_admin_sessions,
    get_admin_audit_log,
    get_admin_sessions,
)
from server.exceptions import LoggedHTTPException


@pytest.fixture
def admin_user() -> MagicMock:
    return MagicMock(id="admin-id")


@pytest.mark.asyncio
async def test_get_admin_sessions_success(admin_user: MagicMock) -> None:
    request = MagicMock()
    auth = MagicMock()
    auth.get_username.return_value = "admin"
    auth.get_active_sessions.return_value = [
        {
            "user_id": "u1",
            "username": "admin",
            "role": "admin",
            "ip_address": "127.0.0.1",
            "created_at": "2026-01-01T00:00:00Z",
            "last_activity": "2026-01-01T01:00:00Z",
        }
    ]
    with (
        patch("server.api.admin.npc_admin_mgmt_api.validate_admin_permission"),
        patch("server.api.admin.npc_admin_mgmt_api.get_admin_auth_service", return_value=auth),
    ):
        result = await get_admin_sessions(request, admin_user)
    assert result.count == 1


@pytest.mark.asyncio
async def test_get_admin_sessions_error(admin_user: MagicMock) -> None:
    request = MagicMock()
    auth = MagicMock()
    auth.get_active_sessions.side_effect = RuntimeError("fail")
    with (
        patch("server.api.admin.npc_admin_mgmt_api.validate_admin_permission"),
        patch("server.api.admin.npc_admin_mgmt_api.get_admin_auth_service", return_value=auth),
    ):
        with pytest.raises(LoggedHTTPException):
            await get_admin_sessions(request, admin_user)


@pytest.mark.asyncio
async def test_get_admin_audit_log_success(admin_user: MagicMock) -> None:
    request = MagicMock()
    auth = MagicMock()
    auth.get_username.return_value = "admin"
    auth.get_audit_log.return_value = [{"timestamp": "2026-01-01T00:00:00Z", "action": "spawn"}]
    with (
        patch("server.api.admin.npc_admin_mgmt_api.validate_admin_permission"),
        patch("server.api.admin.npc_admin_mgmt_api.get_admin_auth_service", return_value=auth),
    ):
        result = await get_admin_audit_log(request, 50, admin_user)
    assert result.count == 1


@pytest.mark.asyncio
async def test_cleanup_admin_sessions_success(admin_user: MagicMock) -> None:
    request = MagicMock()
    auth = MagicMock()
    auth.get_username.return_value = "admin"
    auth.cleanup_expired_sessions.return_value = 2
    with (
        patch("server.api.admin.npc_admin_mgmt_api.validate_admin_permission"),
        patch("server.api.admin.npc_admin_mgmt_api.get_admin_auth_service", return_value=auth),
    ):
        result = await cleanup_admin_sessions(request, admin_user)
    assert result.cleaned_count == 2


@pytest.mark.asyncio
async def test_get_admin_sessions_http_exception_reraises(admin_user: MagicMock) -> None:
    request = MagicMock()
    with patch(
        "server.api.admin.npc_admin_mgmt_api.validate_admin_permission",
        side_effect=HTTPException(status_code=403, detail="forbidden"),
    ):
        with pytest.raises(HTTPException):
            await get_admin_sessions(request, admin_user)
