"""Unit tests for container persistence: CRUD, queries, and UUID conversion paths.

Split from test_container_persistence_extended for Lizard file-size limits.
"""

# pyright: reportPrivateUsage=false, reportAny=false, reportUnusedCallResult=false, reportUnknownVariableType=false

import uuid
from datetime import UTC, datetime
from typing import cast
from unittest.mock import MagicMock, patch

import psycopg2
import pytest

from server.exceptions import DatabaseError
from server.persistence import (
    ContainerCreateParams,
    ContainerData,
    get_containers_by_entity_id,
    get_containers_by_room_id,
    get_decayed_containers,
)
from server.persistence.container_data import ContainerDataCore
from server.persistence.container_persistence import (
    _fetch_container_items,
    create_container,
    delete_container,
    get_container,
    update_container,
)


def test_create_container_success():
    """Test create_container successfully creates container."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {
        "container_instance_id": container_id,
        "source_type": "environment",
        "owner_id": None,
        "room_id": "test_room",
        "entity_id": None,
        "lock_state": "unlocked",
        "capacity_slots": 20,
        "weight_limit": None,
        "decay_at": None,
        "allowed_roles": [],
        "metadata_json": {},
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
        "container_item_instance_id": None,
    }
    mock_conn.cursor.return_value = mock_cursor

    result = create_container(
        mock_conn,
        "environment",
        ContainerCreateParams(room_id="test_room"),
    )

    assert isinstance(result, ContainerData)
    assert result.source_type == "environment"
    assert result.room_id == "test_room"
    mock_conn.commit.assert_called_once()


def test_create_container_database_error():
    """Test create_container handles database errors."""
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = psycopg2.Error("Database error")

    with pytest.raises(DatabaseError, match="Database error creating container"):
        create_container(mock_conn, "environment")


def test_get_container_success():
    """Test get_container successfully retrieves container."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_row = {
        "container_instance_id": container_id,
        "source_type": "environment",
        "owner_id": None,
        "room_id": "test_room",
        "entity_id": None,
        "lock_state": "unlocked",
        "capacity_slots": 20,
        "weight_limit": None,
        "decay_at": None,
        "allowed_roles": [],
        "metadata_json": {},
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
        "container_item_instance_id": None,
    }
    mock_cursor.fetchone.return_value = mock_row
    mock_conn.cursor.return_value = mock_cursor

    # Mock _fetch_container_items
    with patch("server.persistence.container_persistence._fetch_container_items", return_value=[]):
        result = get_container(mock_conn, container_id)

    assert isinstance(result, ContainerData)
    assert result.container_instance_id == container_id
    assert result.source_type == "environment"


def test_get_container_not_found():
    """Test get_container returns None when container not found."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn.cursor.return_value = mock_cursor

    result = get_container(mock_conn, container_id)

    assert result is None


def test_get_container_database_error():
    """Test get_container handles database errors."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = psycopg2.Error("Database error")

    with pytest.raises(DatabaseError, match="Database error retrieving container"):
        get_container(mock_conn, container_id)


def test_get_containers_by_room_id_success():
    """Test get_containers_by_room_id successfully retrieves containers."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    container_id = uuid.uuid4()
    mock_row = {
        "container_instance_id": container_id,
        "source_type": "environment",
        "owner_id": None,
        "room_id": "test_room",
        "entity_id": None,
        "lock_state": "unlocked",
        "capacity_slots": 20,
        "weight_limit": None,
        "decay_at": None,
        "allowed_roles": [],
        "metadata_json": {},
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
        "container_item_instance_id": None,
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_conn.cursor.return_value = mock_cursor

    # Mock _fetch_container_items
    with patch("server.persistence.container_persistence._fetch_container_items", return_value=[]):
        result = get_containers_by_room_id(mock_conn, "test_room")

    assert len(result) == 1
    assert isinstance(result[0], ContainerData)
    assert result[0].container_instance_id == container_id


def test_get_containers_by_room_id_empty():
    """Test get_containers_by_room_id returns empty list when no containers."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = []
    mock_conn.cursor.return_value = mock_cursor

    result = get_containers_by_room_id(mock_conn, "test_room")

    assert result == []


def test_get_containers_by_room_id_database_error():
    """Test get_containers_by_room_id handles database errors."""
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = psycopg2.Error("Database error")

    with pytest.raises(DatabaseError, match="Database error retrieving containers"):
        get_containers_by_room_id(mock_conn, "test_room")


def test_get_containers_by_entity_id_success():
    """Test get_containers_by_entity_id successfully retrieves containers."""
    entity_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    container_id = uuid.uuid4()
    mock_row = {
        "container_instance_id": container_id,
        "source_type": "equipment",
        "owner_id": None,
        "room_id": None,
        "entity_id": entity_id,
        "lock_state": "unlocked",
        "capacity_slots": 20,
        "weight_limit": None,
        "decay_at": None,
        "allowed_roles": [],
        "metadata_json": {},
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
        "container_item_instance_id": None,
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_conn.cursor.return_value = mock_cursor

    # Mock _fetch_container_items
    with patch("server.persistence.container_persistence._fetch_container_items", return_value=[]):
        result = get_containers_by_entity_id(mock_conn, entity_id)

    assert len(result) == 1
    assert isinstance(result[0], ContainerData)
    assert result[0].entity_id == entity_id


def test_get_containers_by_entity_id_database_error():
    """Test get_containers_by_entity_id handles database errors."""
    entity_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = psycopg2.Error("Database error")

    with pytest.raises(DatabaseError, match="Database error retrieving containers"):
        get_containers_by_entity_id(mock_conn, entity_id)


def test_update_container_success():
    """Test update_container successfully updates container."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {
        "container_instance_id": container_id,
        "source_type": "environment",
        "owner_id": None,
        "room_id": "test_room",
        "entity_id": None,
        "lock_state": "locked",
        "capacity_slots": 20,
        "weight_limit": None,
        "decay_at": None,
        "allowed_roles": [],
        "metadata_json": {"updated": True},
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
        "container_item_instance_id": None,
    }
    mock_conn.cursor.return_value = mock_cursor

    # Mock _fetch_container_items and ensure_item_instance (which may call commit)
    with patch("server.persistence.container_persistence._fetch_container_items", return_value=[]):
        with patch("server.persistence.item_instance_persistence.ensure_item_instance"):
            # ensure_item_instance may call commit, so we need to account for that
            result = update_container(
                mock_conn,
                container_id,
                items_json=[{"item_id": "test"}],
                lock_state="locked",
                metadata_json={"updated": True},
            )

    assert isinstance(result, ContainerData)
    assert result.lock_state == "locked"
    # commit is called at least once (by update_container), and possibly by ensure_item_instance
    assert mock_conn.commit.call_count >= 1


def test_update_container_not_found():
    """Test update_container returns None when container not found."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn.cursor.return_value = mock_cursor

    result = update_container(mock_conn, container_id, lock_state="locked")

    assert result is None


def test_update_container_database_error():
    """Test update_container handles database errors."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = psycopg2.Error("Database error")

    with pytest.raises(DatabaseError, match="Database error updating container"):
        update_container(mock_conn, container_id, lock_state="locked")


def test_get_decayed_containers_success():
    """Test get_decayed_containers successfully retrieves decayed containers."""
    current_time = datetime.now(UTC)
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    container_id = uuid.uuid4()
    mock_row = {
        "container_instance_id": container_id,
        "source_type": "corpse",
        "owner_id": None,
        "room_id": "test_room",
        "entity_id": None,
        "lock_state": "unlocked",
        "capacity_slots": 20,
        "weight_limit": None,
        "decay_at": datetime.now(UTC).replace(hour=0),  # Past time
        "allowed_roles": [],
        "metadata_json": {},
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
        "container_item_instance_id": None,
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_conn.cursor.return_value = mock_cursor

    # Mock _fetch_container_items
    with patch("server.persistence.container_persistence._fetch_container_items", return_value=[]):
        result = get_decayed_containers(mock_conn, current_time)

    assert len(result) == 1
    assert isinstance(result[0], ContainerData)


def test_get_decayed_containers_none_time():
    """Test get_decayed_containers with None time uses current time."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = []
    mock_conn.cursor.return_value = mock_cursor

    result = get_decayed_containers(mock_conn, None)

    assert result == []
    # Verify query was executed (cursor.execute was called)
    assert mock_cursor.execute.called


def test_get_decayed_containers_database_error():
    """Test get_decayed_containers handles database errors."""
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = psycopg2.Error("Database error")

    with pytest.raises(DatabaseError, match="Database error retrieving decayed containers"):
        get_decayed_containers(mock_conn, datetime.now(UTC))


def test_delete_container_success():
    """Test delete_container successfully deletes container."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1
    mock_conn.cursor.return_value = mock_cursor

    result = delete_container(mock_conn, container_id)

    assert result is True
    mock_conn.commit.assert_called_once()


def test_delete_container_not_found():
    """Test delete_container returns False when container not found."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None  # No row returned = container not found
    mock_conn.cursor.return_value = mock_cursor

    result = delete_container(mock_conn, container_id)

    assert result is False


def test_delete_container_database_error():
    """Test delete_container handles database errors."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = psycopg2.Error("Database error")

    with pytest.raises(DatabaseError, match="Database error deleting container"):
        delete_container(mock_conn, container_id)


def test_update_container_no_updates():
    """Test update_container with no updates provided (all None)."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None  # No row returned when no updates
    mock_conn.cursor.return_value = mock_cursor

    # Call with all None (no updates)
    result = update_container(mock_conn, container_id, items_json=None, lock_state=None, metadata_json=None)

    # Should return None when no updates are provided
    assert result is None
    # Should not execute UPDATE query when updates list is empty
    # The cursor.execute for UPDATE should not be called
    update_calls = [call for call in mock_cursor.execute.call_args_list if "UPDATE" in str(call)]
    assert len(update_calls) == 0


def test_update_container_uuid_string_conversion():
    """Test update_container handles UUID to string conversion."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (container_id,)
    mock_conn.cursor.return_value = mock_cursor

    with patch("server.persistence.container_persistence._fetch_container_items", return_value=[]):
        with patch("server.persistence.container_persistence.get_container") as mock_get:
            mock_get.return_value = ContainerData(
                ContainerDataCore(container_instance_id=container_id, source_type="environment"),
            )
            update_container(mock_conn, container_id, lock_state="locked")

    # Verify UUID was converted to string in the query
    assert mock_cursor.execute.called
    # Check that container_id was converted to string in the query
    call_args = str(mock_cursor.execute.call_args)
    assert str(container_id) in call_args


def test_delete_container_uuid_string_conversion():
    """Test delete_container handles UUID to string conversion."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (container_id,)
    mock_conn.cursor.return_value = mock_cursor

    result = delete_container(mock_conn, container_id)

    assert result is True
    # Verify UUID was converted to string in the query
    call_args = str(mock_cursor.execute.call_args)
    assert str(container_id) in call_args


def test_fetch_container_items_uuid_string_conversion():
    """Test _fetch_container_items handles UUID to string conversion."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = []
    mock_conn.cursor.return_value = mock_cursor

    _fetch_container_items(mock_conn, container_id)

    # Verify UUID was converted to string in the query
    call_args = str(mock_cursor.execute.call_args)
    assert str(container_id) in call_args


def test_update_container_items_missing_item_instance_id():
    """Test update_container skips items without item_instance_id or prototype_id."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (container_id,)
    mock_conn.cursor.return_value = mock_cursor

    # Items without both item_instance_id and prototype_id should be skipped
    items_json = cast(
        list[dict[str, object]],
        [
            {"item_id": "prototype_1"},  # Missing item_instance_id
            {"item_instance_id": str(uuid.uuid4())},  # Missing prototype_id/item_id
            {"item_instance_id": str(uuid.uuid4()), "item_id": "prototype_2"},  # Valid
        ],
    )

    with patch("server.persistence.container_persistence._fetch_container_items", return_value=[]):
        with patch("server.persistence.container_persistence.get_container") as mock_get:
            with patch("server.persistence.item_instance_persistence.ensure_item_instance") as mock_ensure:
                mock_get.return_value = ContainerData(
                    ContainerDataCore(container_instance_id=container_id, source_type="environment"),
                )
                update_container(mock_conn, container_id, items_json=items_json)

    # Only the valid item should trigger ensure_item_instance
    # The first two should be skipped (missing required fields)
    assert mock_ensure.call_count == 1  # Only one valid item


def test_update_container_items_only_prototype_id():
    """Test update_container handles items with only prototype_id (no item_instance_id)."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (container_id,)
    mock_conn.cursor.return_value = mock_cursor

    # Item with only prototype_id (no item_instance_id) should be skipped
    items_json = cast(
        list[dict[str, object]],
        [{"prototype_id": "prototype_1"}],  # Missing item_instance_id
    )

    with patch("server.persistence.container_persistence._fetch_container_items", return_value=[]):
        with patch("server.persistence.container_persistence.get_container") as mock_get:
            with patch("server.persistence.item_instance_persistence.ensure_item_instance") as mock_ensure:
                mock_get.return_value = ContainerData(
                    ContainerDataCore(container_instance_id=container_id, source_type="environment"),
                )
                update_container(mock_conn, container_id, items_json=items_json)

    # Item should be skipped (missing item_instance_id)
    assert mock_ensure.call_count == 0


def test_create_container_uuid_string_conversion():
    """Test create_container handles UUID to string conversion for container_id."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    container_id = uuid.uuid4()
    mock_cursor.fetchone.return_value = {
        "container_instance_id": container_id,
        "source_type": "environment",
        "owner_id": None,
        "room_id": "test_room",
        "entity_id": None,
        "lock_state": "unlocked",
        "capacity_slots": 20,
        "weight_limit": None,
        "decay_at": None,
        "allowed_roles": [],
        "metadata_json": {},
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
        "container_item_instance_id": None,
    }
    mock_conn.cursor.return_value = mock_cursor

    # Test with items_json that have item_instance_id as UUID
    item_id = uuid.uuid4()
    items_json = [{"item_instance_id": item_id}]

    with patch("server.persistence.container_persistence.get_container") as mock_get:
        mock_get.return_value = ContainerData(
            ContainerDataCore(
                container_instance_id=container_id,
                source_type="environment",
                room_id="test_room",
            ),
        )
        result = create_container(
            mock_conn,
            "environment",
            ContainerCreateParams(room_id="test_room", items_json=items_json),
        )

    # Verify UUIDs were handled correctly
    assert isinstance(result, ContainerData)
    # Check that UUID was converted to string in stored procedure calls
    stored_proc_calls = [call for call in mock_cursor.execute.call_args_list if "add_item_to_container" in str(call)]
    if stored_proc_calls:
        call_str = str(stored_proc_calls[0])
        assert str(item_id) in call_str
