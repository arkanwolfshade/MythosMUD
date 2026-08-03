"""Unit tests for item_instance_persistence_async."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError, ValidationError
from server.persistence.item_instance_persistence_async import (
    create_item_instance_async,
    ensure_item_instance_async,
    item_instance_exists_async,
)


@pytest.mark.asyncio
async def test_create_item_instance_async_success():
    session = AsyncMock()
    session.commit = AsyncMock()
    await create_item_instance_async(session, "inst-1", "proto-1", owner_type="player", owner_id="p1")
    session.execute.assert_awaited_once()
    session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_item_instance_async_missing_id():
    with pytest.raises(ValidationError):
        await create_item_instance_async(AsyncMock(), "", "proto-1")


@pytest.mark.asyncio
async def test_create_item_instance_async_db_error():
    session = AsyncMock()
    session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))
    session.rollback = AsyncMock()
    with pytest.raises(DatabaseError):
        await create_item_instance_async(session, "inst-1", "proto-1")


@pytest.mark.asyncio
async def test_item_instance_exists_async():
    session = AsyncMock()
    result = MagicMock()
    result.scalar.return_value = True
    session.execute = AsyncMock(return_value=result)
    assert await item_instance_exists_async(session, "inst-1") is True


@pytest.mark.asyncio
async def test_ensure_item_instance_async_delegates():
    session = AsyncMock()
    with patch(
        "server.persistence.item_instance_persistence_async.create_item_instance_async",
        new=AsyncMock(),
    ) as mock_create:
        await ensure_item_instance_async(session, "inst-2", "proto-2")
    mock_create.assert_awaited_once()
