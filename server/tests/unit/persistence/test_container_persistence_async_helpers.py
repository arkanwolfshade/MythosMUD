"""Unit tests for async container persistence helper functions."""

import json
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError, ValidationError
from server.persistence.container_persistence_async import (
    _build_item_dict,
    _call_create_container_procedure,
    _finalize_container_creation,
    _parse_item_metadata,
    _parse_jsonb,
    _populate_container_items_async,
    _prepare_container_create_params,
    _row_to_mapping,
    _validate_container_create_params,
    create_container_async,
    delete_container_async,
    fetch_container_items_async,
    get_container_async,
    update_container_async,
)


def test_parse_jsonb_delegates_to_helper() -> None:
    assert _parse_jsonb('{"a": 1}', {}) == {"a": 1}


def test_prepare_container_create_params() -> None:
    owner_id = uuid.uuid4()
    entity_id = uuid.uuid4()
    params = _prepare_container_create_params(
        source_type="environment",
        owner_id=owner_id,
        room_id="room-1",
        entity_id=entity_id,
        lock_state="unlocked",
        capacity_slots=5,
        weight_limit=100,
        decay_at=None,
        allowed_roles=["player"],
        metadata_json={"tag": "chest"},
        container_item_instance_id="item-1",
    )
    assert params["source_type"] == "environment"
    assert params["owner_id"] == str(owner_id)
    assert params["entity_id"] == str(entity_id)
    assert json.loads(params["allowed_roles"]) == ["player"]
    assert json.loads(params["metadata_json"]) == {"tag": "chest"}


@pytest.mark.parametrize(
    ("source_type", "capacity", "lock_state"),
    [
        ("invalid", 5, "unlocked"),
        ("environment", 0, "unlocked"),
        ("environment", 21, "unlocked"),
        ("environment", 5, "broken"),
    ],
)
def test_validate_container_create_params_rejects_invalid(source_type: str, capacity: int, lock_state: str) -> None:
    with pytest.raises(ValidationError):
        _validate_container_create_params(source_type, capacity, lock_state)


def test_validate_container_create_params_accepts_valid() -> None:
    _validate_container_create_params("corpse", 10, "sealed")


def test_row_to_mapping_from_sqlalchemy_row() -> None:
    row = MagicMock()
    row._mapping = {"item_instance_id": "id-1", "item_name": "Lantern"}
    assert _row_to_mapping(row)["item_instance_id"] == "id-1"


def test_row_to_mapping_positional_fallback() -> None:
    row = ("id-2", "proto", "Torch", 1, "worn", None, 0)
    mapping = _row_to_mapping(row)
    assert mapping["item_name"] == "Torch"
    assert mapping["quantity"] == 1


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (None, {}),
        ({"k": "v"}, {"k": "v"}),
        ('{"x": 1}', {"x": 1}),
        ("", {}),
        ("not-json", {}),
        (123, {}),
    ],
)
def test_parse_item_metadata(raw: object, expected: dict[str, object]) -> None:
    assert _parse_item_metadata(raw) == expected


def test_build_item_dict_success() -> None:
    item = _build_item_dict(
        {
            "item_instance_id": uuid.uuid4(),
            "item_id": "proto-1",
            "item_name": "Dagger",
            "quantity": 2,
            "condition": "worn",
            "metadata": {"sharp": True},
            "position": 3,
        }
    )
    assert item is not None
    assert item["item_name"] == "Dagger"
    assert item["quantity"] == 2
    assert item["metadata"] == {"sharp": True}


def test_build_item_dict_missing_instance_id() -> None:
    assert _build_item_dict({"item_name": "Ghost Item"}) is None


@pytest.mark.asyncio
async def test_fetch_container_items_async() -> None:
    container_id = uuid.uuid4()
    instance_id = uuid.uuid4()
    row = MagicMock()
    row._mapping = {
        "item_instance_id": instance_id,
        "item_id": "p1",
        "item_name": "Relic",
        "quantity": 1,
        "condition": "pristine",
        "metadata": None,
        "position": 0,
    }
    session = MagicMock()
    result = MagicMock()
    result.fetchall.return_value = [row]
    session.execute = AsyncMock(return_value=result)
    items = await fetch_container_items_async(session, container_id)
    assert len(items) == 1
    assert items[0]["item_name"] == "Relic"


@pytest.mark.asyncio
async def test_get_container_async_not_found() -> None:
    session = MagicMock()
    result = MagicMock()
    result.fetchone.return_value = None
    session.execute = AsyncMock(return_value=result)
    assert await get_container_async(session, uuid.uuid4()) is None


@pytest.mark.asyncio
async def test_get_container_async_found() -> None:
    container_id = uuid.uuid4()
    row = (
        container_id,
        "environment",
        None,
        "room-1",
        None,
        "unlocked",
        10,
        100,
        None,
        "[]",
        "{}",
        None,
        None,
        None,
    )
    session = MagicMock()
    result = MagicMock()
    result.fetchone.return_value = row
    session.execute = AsyncMock(return_value=result)

    with patch(
        "server.persistence.container_persistence_async.fetch_container_items_async",
        new_callable=AsyncMock,
        return_value=[],
    ):
        container = await get_container_async(session, container_id)

    assert container is not None
    assert container.source_type == "environment"
    assert container.room_id == "room-1"


@pytest.mark.asyncio
async def test_populate_container_items_async() -> None:
    container_id = uuid.uuid4()
    item_id = uuid.uuid4()
    session = MagicMock()
    session.execute = AsyncMock()
    with patch(
        "server.persistence.item_instance_persistence_async.ensure_item_instance_async",
        new_callable=AsyncMock,
    ):
        await _populate_container_items_async(
            session,
            container_id,
            [{"item_instance_id": str(item_id), "item_id": "proto-1", "quantity": 2}],
        )
    assert session.execute.await_count == 2


@pytest.mark.asyncio
async def test_populate_container_items_skips_invalid_and_failed() -> None:
    container_id = uuid.uuid4()
    session = MagicMock()
    session.execute = AsyncMock()
    with patch(
        "server.persistence.item_instance_persistence_async.ensure_item_instance_async",
        new_callable=AsyncMock,
        side_effect=ValidationError("bad item"),
    ):
        await _populate_container_items_async(
            session,
            container_id,
            [
                {"item_name": "no ids"},
                {"item_instance_id": str(uuid.uuid4()), "item_id": "proto-1"},
            ],
        )
    session.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_call_create_container_procedure() -> None:
    session = MagicMock()
    result = MagicMock()
    cid = uuid.uuid4()
    result.fetchone.return_value = (cid, "created", "updated")
    session.execute = AsyncMock(return_value=result)
    out = await _call_create_container_procedure(session, {"source_type": "corpse"}, "corpse")
    assert out == (cid, "created", "updated")


@pytest.mark.asyncio
async def test_call_create_container_procedure_no_row() -> None:
    session = MagicMock()
    result = MagicMock()
    result.fetchone.return_value = None
    session.execute = AsyncMock(return_value=result)
    with pytest.raises(DatabaseError):
        await _call_create_container_procedure(session, {}, "environment")


@pytest.mark.asyncio
async def test_finalize_container_creation_fallback() -> None:
    container_id = uuid.uuid4()
    session = MagicMock()
    session.commit = AsyncMock()
    params = {
        "room_id": "room-1",
        "lock_state": "locked",
        "capacity_slots": 5,
        "items_json": [],
    }
    with patch(
        "server.persistence.container_persistence_async.get_container_async",
        new_callable=AsyncMock,
        return_value=None,
    ):
        out = await _finalize_container_creation(session, container_id, params, "equipment", "c", "u")
    assert out.container_instance_id == container_id
    assert out.lock_state == "locked"


@pytest.mark.asyncio
async def test_update_container_async() -> None:
    container_id = uuid.uuid4()
    session = MagicMock()
    session.execute = AsyncMock()
    session.commit = AsyncMock()
    mock_container = MagicMock()
    with (
        patch(
            "server.persistence.container_persistence_async._populate_container_items_async",
            new_callable=AsyncMock,
        ),
        patch(
            "server.persistence.container_persistence_async.get_container_async",
            new_callable=AsyncMock,
            return_value=mock_container,
        ),
    ):
        result = await update_container_async(
            session,
            container_id,
            items_json=[{"item_instance_id": "i1", "item_id": "p1"}],
            lock_state="locked",
            metadata_json={"tag": "chest"},
        )
    assert result is mock_container
    session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_container_async_success() -> None:
    container_id = uuid.uuid4()
    session = MagicMock()
    mock_container = MagicMock()
    with (
        patch(
            "server.persistence.container_persistence_async._call_create_container_procedure",
            new_callable=AsyncMock,
            return_value=(container_id, "c", "u"),
        ),
        patch(
            "server.persistence.container_persistence_async._finalize_container_creation",
            new_callable=AsyncMock,
            return_value=mock_container,
        ),
    ):
        result = await create_container_async(
            session,
            "environment",
            capacity_slots=5,
            lock_state="unlocked",
        )
    assert result is mock_container


@pytest.mark.asyncio
async def test_delete_container_async_success() -> None:
    session = MagicMock()
    result = MagicMock()
    result.scalar.return_value = True
    session.execute = AsyncMock(return_value=result)
    session.commit = AsyncMock()
    assert await delete_container_async(session, uuid.uuid4()) is True
    session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_delete_container_async_db_error() -> None:
    session = MagicMock()
    session.execute = AsyncMock(side_effect=SQLAlchemyError("db fail"))
    session.rollback = AsyncMock()
    with pytest.raises(DatabaseError):
        await delete_container_async(session, uuid.uuid4())
    session.rollback.assert_awaited_once()
