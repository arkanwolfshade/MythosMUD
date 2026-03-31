"""Unit tests for container persistence: row coercion, inserts, and error paths.

Split from test_container_persistence_extended for Lizard file-size limits.
"""

# pyright: reportPrivateUsage=false, reportAny=false, reportUnusedCallResult=false, reportUnknownVariableType=false

import json
import uuid
from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import psycopg2
import pytest

from server.exceptions import DatabaseError, ValidationError
from server.persistence import ContainerCreateParams
from server.persistence.container_helpers import _coerce_row_quantity
from server.persistence.container_persistence import (
    _allowed_roles_from_row,
    _as_opt_datetime,
    _as_opt_str,
    _as_opt_uuid,
    _as_uuid,
    _coerce_item_quantity,
    _container_data_from_row,
    _CreateOutcome,
    _fetch_container_row_dict,
    _insert_bind_tuple,
    _insert_container_row,
    _InsertBindSource,
    _int_from_row,
    _log_and_resolve_created_container,
    _metadata_from_row,
    _opt_int_from_row,
    _run_container_update_execute,
    _seed_new_container_items,
    _validate_new_container_params,
    create_container,
    delete_container,
    get_container,
    update_container,
)

# --- Row coercion helpers (coverage for small branches) ---


def test_as_uuid_from_uuid_and_string():
    u = uuid.uuid4()
    assert _as_uuid(u) == u
    assert _as_uuid(str(u)) == u


def test_as_opt_uuid_branches():
    u = uuid.uuid4()
    assert _as_opt_uuid(None) is None
    assert _as_opt_uuid(u) == u
    assert _as_opt_uuid(str(u)) == u


def test_as_opt_str_and_as_opt_datetime():
    assert _as_opt_str(None) is None
    assert _as_opt_str(99) == "99"
    assert _as_opt_datetime(None) is None
    dt = datetime(2024, 1, 2, 3, 4, 5)
    assert _as_opt_datetime(dt) is dt
    assert _as_opt_datetime("not-a-datetime") is None


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (True, 1),
        (False, 1),
        (7, 7),
        (" 12 ", 12),
        ("nope", 1),
        (3.9, 3),
        (None, 1),
    ],
)
def test_coerce_item_quantity(raw: object, expected: int) -> None:
    assert _coerce_item_quantity(raw) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (True, 1),
        (False, 1),
        (7, 7),
        (" 12 ", 12),
        ("nope", 1),
        (3.9, 3),
        (None, 1),
    ],
)
def test_coerce_row_quantity(raw: object, expected: int) -> None:
    """Row quantity/position coercion matches item quantity rules (PR #461 / int_coercion reuse)."""
    assert _coerce_row_quantity(raw) == expected


def test_allowed_roles_and_metadata_from_row():
    assert _allowed_roles_from_row(json.dumps(["a", "b"])) == ["a", "b"]
    assert _allowed_roles_from_row(json.dumps({"x": 1})) == []
    assert _metadata_from_row(json.dumps({"k": "v"})) == {"k": "v"}
    assert _metadata_from_row(json.dumps([1, 2])) == {}


def test_metadata_from_row_plain_dict_like_jsonb_driver():
    """Drivers may return decoded dicts; normalize path should still yield metadata."""
    cid = str(uuid.uuid4())
    assert _metadata_from_row({"name": "Chest", "container_ref": cid}) == {
        "name": "Chest",
        "container_ref": cid,
    }


def test_container_data_from_row_normalizes_string_instance_uuid():
    """PostgreSQL / psycopg often delivers UUID columns as str; _as_uuid normalizes."""
    cid = uuid.uuid4()
    row_dict: dict[str, object] = {
        "container_instance_id": str(cid),
        "source_type": "equipment",
        "owner_id": None,
        "room_id": None,
        "entity_id": str(uuid.uuid4()),
        "lock_state": "unlocked",
        "capacity_slots": 5,
        "weight_limit": None,
        "decay_at": None,
        "allowed_roles": "[]",
        "metadata_json": "{}",
        "created_at": None,
        "updated_at": None,
        "container_item_instance_id": None,
    }
    mock_conn = MagicMock()
    with patch("server.persistence.container_persistence.fetch_container_items", return_value=[]):
        data = _container_data_from_row(mock_conn, row_dict, cid)
    assert data.container_instance_id == cid


def test_int_from_row_and_opt_int_from_row():
    assert _int_from_row(42, 0) == 42
    assert _int_from_row(" 3 ", 9) == 3
    assert _int_from_row("bad", 7) == 7
    assert _int_from_row(3.14, 2) == 2
    assert _opt_int_from_row(None) is None
    assert _opt_int_from_row(5) == 5
    assert _opt_int_from_row(" 8 ") == 8
    assert _opt_int_from_row("x") is None
    assert _opt_int_from_row(2.5) is None


def test_validate_new_container_params_rejects_invalid():
    with pytest.raises(ValidationError):
        _validate_new_container_params("invalid", 5, "unlocked")
    with pytest.raises(ValidationError):
        _validate_new_container_params("environment", 0, "unlocked")
    with pytest.raises(ValidationError):
        _validate_new_container_params("environment", 21, "unlocked")
    with pytest.raises(ValidationError):
        _validate_new_container_params("environment", 5, "broken")


def test_insert_container_row_raises_when_no_row_returned():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn.cursor.return_value = mock_cursor
    src = _InsertBindSource(
        source_type="environment",
        owner_id=None,
        room_id="room_a",
        entity_id=None,
        lock_state="unlocked",
        capacity_slots=5,
        weight_limit=None,
        decay_at=None,
        allowed_roles=None,
        metadata_json=None,
        container_item_instance_id=None,
        current_time=datetime.now(UTC).replace(tzinfo=None),
    )
    bind = _insert_bind_tuple(src)
    with pytest.raises(DatabaseError):
        _insert_container_row(mock_conn, bind, "environment")


def test_create_container_wraps_psycopg2_error():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = psycopg2.Error("simulated failure")
    mock_conn.cursor.return_value = mock_cursor
    with pytest.raises(DatabaseError):
        create_container(mock_conn, "environment", ContainerCreateParams(room_id="r1"))


def test_get_container_returns_none_when_row_missing():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn.cursor.return_value = mock_cursor
    cid = uuid.uuid4()
    assert get_container(mock_conn, cid) is None


def test_get_container_wraps_psycopg2_error():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = psycopg2.Error("read failed")
    mock_conn.cursor.return_value = mock_cursor
    with pytest.raises(DatabaseError):
        get_container(mock_conn, uuid.uuid4())


def test_run_container_update_execute_no_op_when_no_fields():
    mock_cursor = MagicMock()
    mock_conn = MagicMock()
    when = datetime.now(UTC).replace(tzinfo=None)
    row, n = _run_container_update_execute(mock_cursor, mock_conn, str(uuid.uuid4()), None, None, None, when)
    assert row is None and n == 0
    mock_cursor.execute.assert_not_called()


def test_delete_container_false_and_psycopg_error():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn.cursor.return_value = mock_cursor
    assert delete_container(mock_conn, uuid.uuid4()) is False

    mock_cursor2 = MagicMock()
    mock_cursor2.execute.side_effect = psycopg2.Error("delete failed")
    mock_conn.cursor.return_value = mock_cursor2
    with pytest.raises(DatabaseError):
        delete_container(mock_conn, uuid.uuid4())


def test_update_container_wraps_psycopg2_error():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.execute.side_effect = psycopg2.Error("update failed")
    mock_conn.cursor.return_value = mock_cursor
    with pytest.raises(DatabaseError):
        update_container(mock_conn, uuid.uuid4(), lock_state="locked")


def test_log_and_resolve_created_container_fallback_when_get_missing():
    mock_conn = MagicMock()
    cid = uuid.uuid4()
    now = datetime.now(UTC).replace(tzinfo=None)
    out = _CreateOutcome(
        container_id=cid,
        source_type="environment",
        owner_id=None,
        room_id="here",
        entity_id=None,
        lock_state="unlocked",
        capacity_slots=5,
        weight_limit=10,
        decay_at=None,
        allowed_roles=["viewer"],
        items_json=None,
        metadata_json={"x": 1},
        created_at=now,
        updated_at=now,
    )
    with patch("server.persistence.container_persistence.get_container", return_value=None):
        data = _log_and_resolve_created_container(mock_conn, out)
    assert data.container_instance_id == cid
    assert data.metadata_json == {"x": 1}
    assert data.allowed_roles == ["viewer"]


def test_container_data_from_row_hydrates():
    cid = uuid.uuid4()
    row_dict: dict[str, object] = {
        "container_instance_id": cid,
        "source_type": "equipment",
        "owner_id": None,
        "room_id": None,
        "entity_id": str(uuid.uuid4()),
        "lock_state": "locked",
        "capacity_slots": "4",
        "weight_limit": "100",
        "decay_at": None,
        "allowed_roles": json.dumps(["role_a"]),
        "metadata_json": json.dumps({"m": 1}),
        "created_at": None,
        "updated_at": None,
        "container_item_instance_id": None,
    }
    mock_conn = MagicMock()
    with patch("server.persistence.container_persistence.fetch_container_items", return_value=[]):
        data = _container_data_from_row(mock_conn, row_dict, cid)
    assert data.capacity_slots == 4
    assert data.weight_limit == 100
    assert data.allowed_roles == ["role_a"]
    assert data.metadata_json == {"m": 1}


def test_fetch_container_row_dict_none():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn.cursor.return_value = mock_cursor
    assert _fetch_container_row_dict(mock_conn, str(uuid.uuid4())) is None


def test_seed_new_container_items_skips_bad_rows_and_handles_ensure_error():
    mock_conn = MagicMock()
    mock_items = MagicMock()
    mock_conn.cursor.return_value = mock_items
    cid = uuid.uuid4()
    items_json: list[dict[str, object]] = [
        {},  # skip: no ids
        {
            "item_instance_id": "ii-1",
            "item_id": "proto-1",
            "quantity": "2",
            "metadata": [1, 2, 3],
        },
    ]
    with patch("server.persistence.container_persistence.ensure_item_instance") as mock_ensure:
        mock_ensure.side_effect = [DatabaseError("fail once"), None]
        _seed_new_container_items(mock_conn, cid, items_json)
    assert mock_ensure.call_count == 1
    mock_items.execute.assert_not_called()

    items_ok: list[dict[str, object]] = [
        {"item_instance_id": "ii-2", "item_id": "proto-2", "quantity": 1, "metadata": {"k": "v"}},
    ]
    mock_items2 = MagicMock()
    mock_conn.cursor.return_value = mock_items2
    with patch("server.persistence.container_persistence.ensure_item_instance"):
        _seed_new_container_items(mock_conn, cid, items_ok)
    mock_items2.execute.assert_called()
