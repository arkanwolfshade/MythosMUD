"""Unit tests for item_instance_persistence helpers."""

from unittest.mock import MagicMock, patch

import pytest

from server.persistence.item_instance_persistence import (
    ensure_item_instance,
    get_item_instance,
    item_instance_exists,
)


def test_item_instance_exists_true() -> None:
    conn = MagicMock()
    cursor = MagicMock()
    cursor.fetchone.return_value = (1,)
    conn.cursor.return_value = cursor

    assert item_instance_exists(conn, "inst-1") is True
    cursor.close.assert_called_once()


def test_item_instance_exists_false() -> None:
    conn = MagicMock()
    cursor = MagicMock()
    cursor.fetchone.return_value = None
    conn.cursor.return_value = cursor

    assert item_instance_exists(conn, "missing") is False


def test_get_item_instance_found() -> None:
    conn = MagicMock()
    cursor = MagicMock()
    cursor.fetchone.return_value = {"item_instance_id": "inst-1", "prototype_id": "p1"}
    conn.cursor.return_value = cursor

    result = get_item_instance(conn, "inst-1")
    assert result == {"item_instance_id": "inst-1", "prototype_id": "p1"}
    cursor.close.assert_called_once()


def test_get_item_instance_not_found() -> None:
    conn = MagicMock()
    cursor = MagicMock()
    cursor.fetchone.return_value = None
    conn.cursor.return_value = cursor

    assert get_item_instance(conn, "missing") is None


def test_ensure_item_instance_calls_create() -> None:
    conn = MagicMock()
    with patch("server.persistence.item_instance_persistence.create_item_instance") as mock_create:
        ensure_item_instance(conn, "inst-1", "proto-1", owner_type="player", owner_id="p1", quantity=3)
    mock_create.assert_called_once()
    assert mock_create.call_args.kwargs["item_instance_id"] == "inst-1"


def test_create_item_instance_success() -> None:
    from server.persistence.item_instance_persistence import create_item_instance

    conn = MagicMock()
    cursor = MagicMock()
    conn.cursor.return_value = cursor

    create_item_instance(conn, "inst-1", "proto-1", quantity=2, metadata={"color": "red"})
    cursor.execute.assert_called_once()
    conn.commit.assert_called_once()
    cursor.close.assert_called_once()


def test_create_item_instance_missing_id() -> None:
    from server.exceptions import ValidationError
    from server.persistence.item_instance_persistence import create_item_instance

    with pytest.raises(ValidationError):
        create_item_instance(MagicMock(), "", "proto-1")


def test_create_item_instance_db_error() -> None:
    import psycopg2

    from server.exceptions import DatabaseError
    from server.persistence.item_instance_persistence import create_item_instance

    conn = MagicMock()
    cursor = MagicMock()
    cursor.execute.side_effect = psycopg2.Error("db fail")
    conn.cursor.return_value = cursor

    with pytest.raises(DatabaseError):
        create_item_instance(conn, "inst-1", "proto-1")
    conn.rollback.assert_called_once()
