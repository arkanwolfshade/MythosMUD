"""Unit tests for NPC spawn rules admin API."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException

from server.api.admin.npc_spawn_rules_api import (
    create_npc_spawn_rule,
    delete_npc_spawn_rule,
    get_npc_spawn_rules,
)
from server.exceptions import LoggedHTTPException


@pytest.fixture
def mock_user() -> MagicMock:
    user = MagicMock()
    user.id = "user-1"
    return user


@pytest.fixture
def mock_session() -> AsyncMock:
    session = AsyncMock()
    session.commit = AsyncMock()
    session.rollback = AsyncMock()
    return session


@pytest.mark.asyncio
async def test_get_npc_spawn_rules_success(mock_user: MagicMock, mock_session: AsyncMock) -> None:
    rule = MagicMock()
    request = MagicMock()
    auth_service = MagicMock()
    auth_service.get_username.return_value = "admin"

    with (
        patch("server.api.admin.npc_spawn_rules_api.validate_admin_permission"),
        patch("server.api.admin.npc_spawn_rules_api.get_admin_auth_service", return_value=auth_service),
        patch("server.api.admin.npc_spawn_rules_api.npc_service") as svc,
        patch("server.api.admin.npc_spawn_rules_api.NPCSpawnRuleResponse") as resp_cls,
    ):
        svc.get_spawn_rules = AsyncMock(return_value=[rule])
        resp_cls.from_orm.return_value = MagicMock()
        result = await get_npc_spawn_rules(request, mock_user, mock_session)

    assert len(result) == 1
    svc.get_spawn_rules.assert_awaited_once_with(mock_session)


@pytest.mark.asyncio
async def test_get_npc_spawn_rules_http_exception_propagates(mock_user: MagicMock, mock_session: AsyncMock) -> None:
    request = MagicMock()
    with patch(
        "server.api.admin.npc_spawn_rules_api.validate_admin_permission",
        side_effect=HTTPException(status_code=403, detail="forbidden"),
    ):
        with pytest.raises(HTTPException):
            await get_npc_spawn_rules(request, mock_user, mock_session)


@pytest.mark.asyncio
async def test_get_npc_spawn_rules_generic_error(mock_user: MagicMock, mock_session: AsyncMock) -> None:
    request = MagicMock()
    with (
        patch("server.api.admin.npc_spawn_rules_api.validate_admin_permission"),
        patch("server.api.admin.npc_spawn_rules_api.get_admin_auth_service") as auth_svc,
        patch("server.api.admin.npc_spawn_rules_api.npc_service") as svc,
    ):
        auth_svc.return_value.get_username.return_value = "admin"
        svc.get_spawn_rules = AsyncMock(side_effect=RuntimeError("db down"))
        with pytest.raises(LoggedHTTPException):
            await get_npc_spawn_rules(request, mock_user, mock_session)


@pytest.mark.asyncio
async def test_create_npc_spawn_rule_success(mock_user: MagicMock, mock_session: AsyncMock) -> None:
    request = MagicMock()
    body = MagicMock()
    body.npc_definition_id = 1
    body.sub_zone_id = "zone_a"
    body.min_population = 0
    body.max_population = 3
    body.spawn_conditions.model_dump.return_value = {"time": "night"}
    rule = MagicMock()
    auth_service = MagicMock()
    auth_service.get_username.return_value = "admin"

    with (
        patch("server.api.admin.npc_spawn_rules_api.validate_admin_permission"),
        patch("server.api.admin.npc_spawn_rules_api.get_admin_auth_service", return_value=auth_service),
        patch("server.api.admin.npc_spawn_rules_api.npc_service") as svc,
        patch("server.api.admin.npc_spawn_rules_api.NPCSpawnRuleResponse") as resp_cls,
    ):
        svc.create_spawn_rule = AsyncMock(return_value=rule)
        resp_cls.from_orm.return_value = MagicMock()
        await create_npc_spawn_rule(body, request, mock_user, mock_session)

    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_npc_spawn_rule_rolls_back(mock_user: MagicMock, mock_session: AsyncMock) -> None:
    request = MagicMock()
    body = MagicMock()
    body.spawn_conditions.model_dump.return_value = {}
    with (
        patch("server.api.admin.npc_spawn_rules_api.validate_admin_permission"),
        patch("server.api.admin.npc_spawn_rules_api.get_admin_auth_service") as auth_svc,
        patch("server.api.admin.npc_spawn_rules_api.npc_service") as svc,
    ):
        auth_svc.return_value.get_username.return_value = "admin"
        svc.create_spawn_rule = AsyncMock(side_effect=RuntimeError("fail"))
        with pytest.raises(LoggedHTTPException):
            await create_npc_spawn_rule(body, request, mock_user, mock_session)

    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_delete_npc_spawn_rule_success(mock_user: MagicMock, mock_session: AsyncMock) -> None:
    request = MagicMock()
    auth_service = MagicMock()
    auth_service.get_username.return_value = "admin"

    with (
        patch("server.api.admin.npc_spawn_rules_api.validate_admin_permission"),
        patch("server.api.admin.npc_spawn_rules_api.get_admin_auth_service", return_value=auth_service),
        patch("server.api.admin.npc_spawn_rules_api.npc_service") as svc,
    ):
        svc.delete_spawn_rule = AsyncMock(return_value=True)
        await delete_npc_spawn_rule(7, request, mock_user, mock_session)

    mock_session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_delete_npc_spawn_rule_not_found(mock_user: MagicMock, mock_session: AsyncMock) -> None:
    request = MagicMock()
    auth_service = MagicMock()
    auth_service.get_username.return_value = "admin"

    with (
        patch("server.api.admin.npc_spawn_rules_api.validate_admin_permission"),
        patch("server.api.admin.npc_spawn_rules_api.get_admin_auth_service", return_value=auth_service),
        patch("server.api.admin.npc_spawn_rules_api.npc_service") as svc,
    ):
        svc.delete_spawn_rule = AsyncMock(return_value=False)
        with pytest.raises(LoggedHTTPException):
            await delete_npc_spawn_rule(99, request, mock_user, mock_session)
