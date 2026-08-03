"""Unit tests for container_query_helpers_async."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.container_query_helpers_async import (
    _parse_jsonb,
    get_containers_by_entity_id_async,
    get_containers_by_room_id_async,
    get_decayed_containers_async,
)

CONTAINER_ID = uuid.UUID("11111111-1111-1111-1111-111111111111")
ENTITY_ID = uuid.UUID("22222222-2222-2222-2222-222222222222")


def _sample_row() -> tuple[object, ...]:
    now = datetime.now(UTC)
    return (
        CONTAINER_ID,
        "room",
        None,
        "room_001",
        None,
        "unlocked",
        10,
        100.0,
        None,
        '["admin"]',
        '{"label": "chest"}',
        now,
        now,
        None,
    )


def test_parse_jsonb_delegates() -> None:
    assert _parse_jsonb('["a"]', []) == ["a"]


@pytest.mark.asyncio
async def test_get_containers_by_room_id_success() -> None:
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [_sample_row()]
    mock_session.execute = AsyncMock(return_value=mock_result)

    with patch(
        "server.persistence.container_query_helpers_async.fetch_container_items_async",
        new_callable=AsyncMock,
        return_value=[],
    ):
        containers = await get_containers_by_room_id_async(mock_session, "room_001")

    assert len(containers) == 1
    assert containers[0].container_instance_id == CONTAINER_ID


@pytest.mark.asyncio
async def test_get_containers_by_room_id_db_error() -> None:
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))

    with pytest.raises(DatabaseError):
        await get_containers_by_room_id_async(mock_session, "room_001")


@pytest.mark.asyncio
async def test_get_containers_by_entity_id_success() -> None:
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [_sample_row()]
    mock_session.execute = AsyncMock(return_value=mock_result)

    with patch(
        "server.persistence.container_query_helpers_async.fetch_container_items_async",
        new_callable=AsyncMock,
        return_value=[],
    ):
        containers = await get_containers_by_entity_id_async(mock_session, ENTITY_ID)

    assert len(containers) == 1


@pytest.mark.asyncio
async def test_get_containers_by_entity_id_db_error() -> None:
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))

    with pytest.raises(DatabaseError):
        await get_containers_by_entity_id_async(mock_session, ENTITY_ID)


@pytest.mark.asyncio
async def test_get_decayed_containers_default_time() -> None:
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = []
    mock_session.execute = AsyncMock(return_value=mock_result)

    containers = await get_decayed_containers_async(mock_session)
    assert containers == []


@pytest.mark.asyncio
async def test_get_decayed_containers_naive_time_normalized() -> None:
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.fetchall.return_value = []
    mock_session.execute = AsyncMock(return_value=mock_result)
    naive = datetime(2026, 1, 1, 12, 0, 0)

    await get_decayed_containers_async(mock_session, naive)
    call_args = mock_session.execute.await_args
    assert call_args is not None
    params = call_args[0][1]
    assert params["current_time"].tzinfo == UTC


@pytest.mark.asyncio
async def test_get_decayed_containers_db_error() -> None:
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))

    with pytest.raises(DatabaseError):
        await get_decayed_containers_async(mock_session, datetime.now(UTC))
