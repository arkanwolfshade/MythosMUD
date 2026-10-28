"""
Unit tests for item catalog API, service projection, and repository helpers.
"""

from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest
from fastapi import Request
from sqlalchemy.exc import SQLAlchemyError

from server.api.item_catalog import get_item_catalog
from server.exceptions import DatabaseError, LoggedHTTPException
from server.game.item_catalog_service import (
    ItemCatalogService,
    normalize_catalog_query,
    project_admin_item,
    project_player_item,
)
from server.persistence.repositories.item_catalog_repository import (
    ItemCatalogPage,
    ItemCatalogRepository,
    ItemPrototypeRow,
)
from server.schemas.item_catalog import ItemCatalogAdminItem, ItemCatalogPlayerItem, ItemCatalogResponse


class _MappingsProxy:
    """Typed stand-in for Result.mappings() so .all() is not MagicMock Any."""

    def __init__(self, rows: list[dict[str, object]]) -> None:
        self._rows: list[dict[str, object]] = rows

    def all(self) -> list[dict[str, object]]:
        return self._rows


class _ExecuteResult:
    """Typed stand-in for sqlalchemy Result when only .mappings().all() is used."""

    def __init__(self, rows: list[dict[str, object]]) -> None:
        self._rows: list[dict[str, object]] = rows

    def mappings(self) -> _MappingsProxy:
        return _MappingsProxy(self._rows)


class _SessionCM:
    """Typed async context manager for session_maker()."""

    def __init__(self, session: AsyncMock) -> None:
        self._session: AsyncMock = session

    async def __aenter__(self) -> AsyncMock:
        return self._session

    async def __aexit__(self, *_args: object) -> None:
        return None


def _sample_row() -> ItemPrototypeRow:
    return ItemPrototypeRow(
        prototype_id="core.weapon.knife",
        name="Knife",
        short_description="A blade",
        long_description="A longer blade",
        item_type="weapon",
        weight=0.5,
        base_value=10,
        durability=None,
        flags=["sharp"],
        wear_slots=[],
        stacking_rules={},
        usage_restrictions={},
        effect_components=[],
        metadata={"namespace": "core"},
        tags=["melee"],
        created_at=datetime.now(UTC),
    )


def _mock_user(*, is_admin: bool = False, is_superuser: bool = False) -> MagicMock:
    user: MagicMock = MagicMock()
    user.id = uuid4()
    user.is_admin = is_admin
    user.is_superuser = is_superuser
    return user


def test_normalize_catalog_query_clamps_and_strips() -> None:
    query = normalize_catalog_query(item_type="  weapon ", page=0, page_size=500, search="  x ")
    assert query.item_type == "weapon"
    assert query.page == 1
    assert query.page_size == 100
    assert query.search == "x"


def test_normalize_catalog_query_blank_filters_become_none() -> None:
    query = normalize_catalog_query(item_type="   ", namespace="", search=None)
    assert query.item_type is None
    assert query.namespace is None
    assert query.search is None


def test_project_player_and_admin() -> None:
    row = _sample_row()
    player = project_player_item(row)
    assert isinstance(player, ItemCatalogPlayerItem)
    assert player.name == "Knife"
    admin = project_admin_item(row)
    assert isinstance(admin, ItemCatalogAdminItem)
    assert admin.prototype_id == "core.weapon.knife"
    assert admin.metadata["namespace"] == "core"


async def _repo_list_page(rows: list[dict[str, object]]) -> ItemCatalogPage:
    mock_session: AsyncMock = AsyncMock()
    mock_session.execute = AsyncMock(return_value=_ExecuteResult(rows))
    with patch(
        "server.persistence.repositories.item_catalog_repository.get_session_maker",
        return_value=MagicMock(return_value=_SessionCM(mock_session)),
    ):
        return await ItemCatalogRepository().list_page(
            item_type=None,
            namespace=None,
            search=None,
            limit=25,
            offset=0,
        )


@pytest.mark.asyncio
async def test_service_list_catalog_player_projection() -> None:
    repo = MagicMock()
    list_page: AsyncMock = AsyncMock(return_value=ItemCatalogPage(rows=[_sample_row()], total=1))
    repo.list_page = list_page
    service = ItemCatalogService(repository=repo)
    response = await service.list_catalog(normalize_catalog_query(), is_admin=False)
    assert response.is_admin is False
    assert len(response.items) == 1
    assert isinstance(response.items[0], ItemCatalogPlayerItem)


@pytest.mark.asyncio
async def test_service_list_catalog_admin_projection() -> None:
    repo = MagicMock()
    list_page: AsyncMock = AsyncMock(return_value=ItemCatalogPage(rows=[_sample_row()], total=1))
    repo.list_page = list_page
    service = ItemCatalogService(repository=repo)
    response = await service.list_catalog(normalize_catalog_query(page=2, page_size=10), is_admin=True)
    assert response.is_admin is True
    assert isinstance(response.items[0], ItemCatalogAdminItem)
    list_page.assert_awaited_once()
    await_args = list_page.await_args
    assert await_args is not None
    kwargs = await_args.kwargs
    assert kwargs["offset"] == 10
    assert kwargs["limit"] == 10


@pytest.mark.asyncio
async def test_get_item_catalog_endpoint_player() -> None:
    request = MagicMock(spec=Request)
    service = MagicMock(spec=ItemCatalogService)
    list_catalog: AsyncMock = AsyncMock(
        return_value=ItemCatalogResponse(
            items=[ItemCatalogPlayerItem(name="Knife", item_type="weapon", short_description="A blade")],
            page=1,
            page_size=25,
            total=1,
            is_admin=False,
        )
    )
    service.list_catalog = list_catalog
    result = await get_item_catalog(
        request,
        current_user=_mock_user(),
        catalog_service=service,
        item_type="weapon",
        namespace=None,
        search=None,
        page=1,
        page_size=25,
    )
    assert result.total == 1
    assert result.is_admin is False
    list_catalog.assert_awaited_once()
    call_kwargs = list_catalog.await_args
    assert call_kwargs is not None
    assert call_kwargs.kwargs["is_admin"] is False


@pytest.mark.asyncio
async def test_get_item_catalog_endpoint_admin() -> None:
    request = MagicMock(spec=Request)
    service = MagicMock(spec=ItemCatalogService)
    list_catalog: AsyncMock = AsyncMock(
        return_value=ItemCatalogResponse(items=[], page=1, page_size=25, total=0, is_admin=True)
    )
    service.list_catalog = list_catalog
    result = await get_item_catalog(
        request,
        current_user=_mock_user(is_admin=True),
        catalog_service=service,
        item_type=None,
        namespace="core",
        search="knife",
        page=1,
        page_size=25,
    )
    assert result.is_admin is True
    call_kwargs = list_catalog.await_args
    assert call_kwargs is not None
    assert call_kwargs.kwargs["is_admin"] is True


@pytest.mark.asyncio
async def test_get_item_catalog_endpoint_superuser_is_admin() -> None:
    request = MagicMock(spec=Request)
    service = MagicMock(spec=ItemCatalogService)
    list_catalog: AsyncMock = AsyncMock(
        return_value=ItemCatalogResponse(items=[], page=1, page_size=25, total=0, is_admin=True)
    )
    service.list_catalog = list_catalog
    _ = await get_item_catalog(
        request,
        current_user=_mock_user(is_superuser=True),
        catalog_service=service,
        item_type=None,
        namespace=None,
        search=None,
        page=1,
        page_size=25,
    )
    call_kwargs = list_catalog.await_args
    assert call_kwargs is not None
    assert call_kwargs.kwargs["is_admin"] is True


@pytest.mark.asyncio
async def test_get_item_catalog_endpoint_error() -> None:
    request = MagicMock(spec=Request)
    service = MagicMock(spec=ItemCatalogService)
    service.list_catalog = AsyncMock(side_effect=RuntimeError("db down"))
    with pytest.raises(LoggedHTTPException) as exc_info:
        _ = await get_item_catalog(
            request,
            current_user=_mock_user(),
            catalog_service=service,
            item_type=None,
            namespace=None,
            search=None,
            page=1,
            page_size=25,
        )
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_repository_list_page_success() -> None:
    page = await _repo_list_page(
        [
            {
                "prototype_id": "core.tool.lantern",
                "name": "Lantern",
                "short_description": "Light",
                "long_description": "Bright",
                "item_type": "tool",
                "weight": 1.0,
                "base_value": 5,
                "durability": 10,
                "flags": [],
                "wear_slots": "bad",
                "stacking_rules": [],
                "usage_restrictions": {},
                "effect_components": [],
                "metadata": {"namespace": "core"},
                "tags": [],
                "created_at": datetime.now(UTC),
                "total_count": "7",
            }
        ]
    )
    assert page.total == 7
    assert page.rows[0].name == "Lantern"
    assert page.rows[0].wear_slots == []
    assert page.rows[0].stacking_rules == {}


@pytest.mark.asyncio
async def test_repository_list_page_empty() -> None:
    page = await _repo_list_page([])
    assert page.total == 0
    assert page.rows == []


@pytest.mark.asyncio
async def test_repository_list_page_invalid_total_count() -> None:
    with pytest.raises(DatabaseError):
        _ = await _repo_list_page(
            [
                {
                    "prototype_id": "a",
                    "name": "A",
                    "short_description": "s",
                    "long_description": "l",
                    "item_type": "tool",
                    "weight": 1.0,
                    "base_value": 1,
                    "durability": None,
                    "flags": [],
                    "wear_slots": [],
                    "stacking_rules": {},
                    "usage_restrictions": {},
                    "effect_components": [],
                    "metadata": {},
                    "tags": [],
                    "created_at": None,
                    "total_count": True,
                }
            ]
        )


@pytest.mark.asyncio
async def test_repository_list_page_db_error() -> None:
    mock_session: AsyncMock = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    with patch(
        "server.persistence.repositories.item_catalog_repository.get_session_maker",
        return_value=MagicMock(return_value=_SessionCM(mock_session)),
    ):
        with pytest.raises(DatabaseError):
            _ = await ItemCatalogRepository().list_page(
                item_type=None,
                namespace=None,
                search=None,
                limit=25,
                offset=0,
            )
