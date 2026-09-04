"""Unit tests for ItemRepository async delegation."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.persistence.repositories.item_repository import ItemRepository


@pytest.fixture
def repository() -> ItemRepository:
    return ItemRepository()


@pytest.mark.asyncio
async def test_create_item_instance_delegates(repository: ItemRepository) -> None:
    session = MagicMock()
    session.__aenter__ = AsyncMock(return_value=session)
    session.__aexit__ = AsyncMock(return_value=None)
    session_maker = MagicMock(return_value=session)
    with (
        patch("server.persistence.repositories.item_repository.get_session_maker", return_value=session_maker),
        patch(
            "server.persistence.repositories.item_repository.create_item_instance_async",
            new=AsyncMock(),
        ) as create_async,
    ):
        await repository.create_item_instance("inst-1", "proto-1", {"owner_id": "room-1"})
    create_async.assert_awaited_once()


@pytest.mark.asyncio
async def test_ensure_item_instance_delegates(repository: ItemRepository) -> None:
    session = MagicMock()
    session.__aenter__ = AsyncMock(return_value=session)
    session.__aexit__ = AsyncMock(return_value=None)
    session_maker = MagicMock(return_value=session)
    with (
        patch("server.persistence.repositories.item_repository.get_session_maker", return_value=session_maker),
        patch(
            "server.persistence.repositories.item_repository.ensure_item_instance_async",
            new=AsyncMock(),
        ) as ensure_async,
    ):
        await repository.ensure_item_instance("inst-2", "proto-2")
    ensure_async.assert_awaited_once()


@pytest.mark.asyncio
async def test_item_instance_exists_delegates(repository: ItemRepository) -> None:
    session = MagicMock()
    session.__aenter__ = AsyncMock(return_value=session)
    session.__aexit__ = AsyncMock(return_value=None)
    session_maker = MagicMock(return_value=session)
    with (
        patch("server.persistence.repositories.item_repository.get_session_maker", return_value=session_maker),
        patch(
            "server.persistence.repositories.item_repository.item_instance_exists_async",
            new=AsyncMock(return_value=True),
        ) as exists_async,
    ):
        result = await repository.item_instance_exists("inst-3")
    assert result is True
    exists_async.assert_awaited_once()
