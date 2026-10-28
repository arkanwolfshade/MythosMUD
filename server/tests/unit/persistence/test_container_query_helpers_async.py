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
    get_bank_container_async,
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


def _session_whose_fetchone_is(row: tuple[object, ...] | None) -> tuple[AsyncMock, AsyncMock]:
    """A session whose execute() yields a result with fetchone() == row; returns (session, execute)."""
    result = MagicMock()
    result.configure_mock(fetchone=MagicMock(return_value=row))
    execute = AsyncMock(return_value=result)
    session = AsyncMock()
    session.execute = execute
    return session, execute


@pytest.mark.asyncio
async def test_get_bank_container_returns_the_owners_box() -> None:
    session, execute = _session_whose_fetchone_is(_sample_row())

    with patch(
        "server.persistence.container_query_helpers_async.fetch_container_items_async",
        new_callable=AsyncMock,
        return_value=[{"item_id": "lamp"}],
    ):
        box = await get_bank_container_async(session, ENTITY_ID)

    assert box is not None
    assert box.container_instance_id == CONTAINER_ID
    assert box.items_json == [{"item_id": "lamp"}]
    assert execute.await_args is not None
    # the procedure takes the owner as text, never a UUID object
    assert execute.await_args.args[1] == {"owner_id": str(ENTITY_ID)}


@pytest.mark.asyncio
async def test_get_bank_container_is_none_when_the_player_has_no_box() -> None:
    session, _ = _session_whose_fetchone_is(None)

    with patch(
        "server.persistence.container_query_helpers_async.fetch_container_items_async",
        new_callable=AsyncMock,
    ) as fetch_items:
        assert await get_bank_container_async(session, ENTITY_ID) is None

    fetch_items.assert_not_awaited()  # nothing to load items for


@pytest.mark.asyncio
async def test_get_bank_container_db_error() -> None:
    session = AsyncMock()
    session.execute = AsyncMock(side_effect=SQLAlchemyError("fail"))

    with pytest.raises(DatabaseError):
        _ = await get_bank_container_async(session, ENTITY_ID)
