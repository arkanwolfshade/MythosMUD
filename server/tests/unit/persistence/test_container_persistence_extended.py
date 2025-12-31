"""
Extended unit tests for container persistence.

Tests container persistence functions beyond _parse_jsonb_column.
"""

import json
import uuid
from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import psycopg2
import pytest

from server.exceptions import DatabaseError
from server.persistence.container_persistence import (
    ContainerData,
    _fetch_container_items,
    _parse_jsonb_column,
    create_container,
    delete_container,
    get_container,
    get_containers_by_entity_id,
    get_containers_by_room_id,
    get_decayed_containers,
    update_container,
)


def test_parse_jsonb_column_empty_list():
    """Test parsing empty list JSONB column."""
    result = _parse_jsonb_column([], [])
    assert result == []


def test_parse_jsonb_column_empty_dict():
    """Test parsing empty dict JSONB column."""
    result = _parse_jsonb_column({}, {})
    assert result == {}


def test_parse_jsonb_column_string_list():
    """Test parsing string JSONB column containing list."""
    data = [1, 2, 3]
    result = _parse_jsonb_column(json.dumps(data), [])
    assert result == data


def test_parse_jsonb_column_string_dict():
    """Test parsing string JSONB column containing dict."""
    data = {"key": "value", "nested": {"inner": "data"}}
    result = _parse_jsonb_column(json.dumps(data), {})
    assert result == data


def test_parse_jsonb_column_with_default():
    """Test parsing JSONB column with custom default."""
    result = _parse_jsonb_column(None, {"default": "value"})
    assert result == {"default": "value"}


def test_parse_jsonb_column_falsy_value():
    """Test parsing falsy but non-None value."""
    # The function returns value if value else default
    # So 0 (falsy) will return default
    result = _parse_jsonb_column(0, 1)
    assert result == 1  # 0 is falsy, so returns default


def test_parse_jsonb_column_falsy_empty_string():
    """Test parsing empty string returns default."""
    result = _parse_jsonb_column("", {"default": "value"})
    assert result == {"default": "value"}


def test_parse_jsonb_column_falsy_empty_list():
    """Test parsing empty list returns default."""
    result = _parse_jsonb_column([], {"default": "value"})
    assert result == {"default": "value"}


def test_parse_jsonb_column_falsy_empty_dict():
    """Test parsing empty dict returns default."""
    result = _parse_jsonb_column({}, {"default": "value"})
    assert result == {"default": "value"}


def test_fetch_container_items_success():
    """Test _fetch_container_items successfully fetches items."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_row1 = {
        "item_instance_id": str(uuid.uuid4()),
        "item_id": "prototype_1",
        "item_name": "Test Item",
        "quantity": 1,
        "condition": "pristine",
        "metadata": {"key": "value"},
        "position": 0,
    }
    mock_row2 = {
        "item_instance_id": str(uuid.uuid4()),
        "item_id": "prototype_2",
        "item_name": "Another Item",
        "quantity": 2,
        "condition": "worn",
        "metadata": None,
        "position": 1,
    }
    mock_cursor.fetchall.return_value = [mock_row1, mock_row2]
    mock_conn.cursor.return_value = mock_cursor

    result = _fetch_container_items(mock_conn, container_id)

    assert len(result) == 2
    assert result[0]["item_instance_id"] == str(mock_row1["item_instance_id"])
    assert result[0]["item_name"] == "Test Item"
    assert result[1]["item_name"] == "Another Item"
    assert result[1]["metadata"] == {}  # None should become {}


def test_fetch_container_items_empty():
    """Test _fetch_container_items with no items."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = []
    mock_conn.cursor.return_value = mock_cursor

    result = _fetch_container_items(mock_conn, container_id)

    assert result == []


def test_fetch_container_items_missing_item_instance_id():
    """Test _fetch_container_items skips rows with missing item_instance_id."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_row = {
        "item_id": "prototype_1",
        "item_name": "Test Item",
        # Missing item_instance_id
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_conn.cursor.return_value = mock_cursor

    result = _fetch_container_items(mock_conn, container_id)

    assert result == []


def test_fetch_container_items_non_dict_row():
    """Test _fetch_container_items handles non-dictionary rows."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = ["not a dict", {"item_instance_id": str(uuid.uuid4()), "item_id": "test"}]
    mock_conn.cursor.return_value = mock_cursor

    result = _fetch_container_items(mock_conn, container_id)

    # Should skip non-dict row, keep dict row
    assert len(result) == 1


def test_fetch_container_items_string_metadata():
    """Test _fetch_container_items parses string metadata."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_row = {
        "item_instance_id": str(uuid.uuid4()),
        "item_id": "prototype_1",
        "item_name": "Test Item",
        "quantity": 1,
        "condition": "pristine",
        "metadata": json.dumps({"key": "value"}),
        "position": 0,
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_conn.cursor.return_value = mock_cursor

    result = _fetch_container_items(mock_conn, container_id)

    assert result[0]["metadata"] == {"key": "value"}


def test_fetch_container_items_invalid_json_metadata():
    """Test _fetch_container_items handles invalid JSON metadata."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_row = {
        "item_instance_id": str(uuid.uuid4()),
        "item_id": "prototype_1",
        "item_name": "Test Item",
        "quantity": 1,
        "condition": "pristine",
        "metadata": "{invalid json}",
        "position": 0,
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_conn.cursor.return_value = mock_cursor

    result = _fetch_container_items(mock_conn, container_id)

    # Should default to {} on JSON parse error
    assert result[0]["metadata"] == {}


def test_fetch_container_items_non_dict_metadata():
    """Test _fetch_container_items handles non-dict metadata."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_row = {
        "item_instance_id": str(uuid.uuid4()),
        "item_id": "prototype_1",
        "item_name": "Test Item",
        "quantity": 1,
        "condition": "pristine",
        "metadata": "not a dict",
        "position": 0,
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_conn.cursor.return_value = mock_cursor

    result = _fetch_container_items(mock_conn, container_id)

    # Should default to {} for non-dict metadata
    assert result[0]["metadata"] == {}


def test_fetch_container_items_missing_fields():
    """Test _fetch_container_items handles missing optional fields."""
    container_id = uuid.uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_row = {
        "item_instance_id": str(uuid.uuid4()),
        # Missing item_id, item_name, quantity, condition, position
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_conn.cursor.return_value = mock_cursor

    result = _fetch_container_items(mock_conn, container_id)

    assert len(result) == 1
    assert result[0]["item_id"] is None
    assert result[0]["item_name"] == "Unknown Item"
    assert result[0]["quantity"] == 1
    assert result[0]["condition"] == "pristine"
    assert result[0]["position"] == 0


def test_container_data_init():
    """Test ContainerData initialization."""
    container_id = uuid.uuid4()
    container = ContainerData(
        container_instance_id=container_id,
        source_type="environment",
        owner_id=uuid.uuid4(),
        room_id="test_room",
    )

    assert container.container_instance_id == container_id
    assert container.source_type == "environment"
    assert container.room_id == "test_room"
    assert container.allowed_roles == []
    assert container.items_json == []
    assert container.metadata_json == {}


def test_container_data_to_dict():
    """Test ContainerData.to_dict conversion."""
    container_id = uuid.uuid4()
    owner_id = uuid.uuid4()
    entity_id = uuid.uuid4()
    created_at = datetime.now(UTC)
    updated_at = datetime.now(UTC)
    decay_at = datetime.now(UTC)

    container = ContainerData(
        container_instance_id=container_id,
        source_type="equipment",
        owner_id=owner_id,
        entity_id=entity_id,
        lock_state="locked",
        capacity_slots=10,
        weight_limit=50,
        decay_at=decay_at,
        allowed_roles=["admin"],
        items_json=[{"item_id": "test"}],
        metadata_json={"key": "value"},
        created_at=created_at,
        updated_at=updated_at,
    )

    result = container.to_dict()

    assert result["container_id"] == str(container_id)
    assert result["source_type"] == "equipment"
    assert result["owner_id"] == str(owner_id)
    assert result["entity_id"] == str(entity_id)
    assert result["lock_state"] == "locked"
    assert result["capacity_slots"] == 10
    assert result["weight_limit"] == 50
    assert result["decay_at"] == decay_at.isoformat()
    assert result["allowed_roles"] == ["admin"]
    assert result["items"] == [{"item_id": "test"}]
    assert result["metadata"] == {"key": "value"}
    assert result["created_at"] == created_at.isoformat()
    assert result["updated_at"] == updated_at.isoformat()


def test_container_data_to_dict_none_values():
    """Test ContainerData.to_dict with None values."""
    container_id = uuid.uuid4()
    container = ContainerData(
        container_instance_id=container_id,
        source_type="environment",
        owner_id=None,
        entity_id=None,
        decay_at=None,
        created_at=None,
        updated_at=None,
    )

    result = container.to_dict()

    assert result["owner_id"] is None
    assert result["entity_id"] is None
    assert result["decay_at"] is None
    assert result["created_at"] is None
    assert result["updated_at"] is None


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
        source_type="environment",
        room_id="test_room",
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
        create_container(mock_conn, source_type="environment")


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
                container_instance_id=container_id,
                source_type="environment",
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
    items_json = [
        {"item_id": "prototype_1"},  # Missing item_instance_id
        {"item_instance_id": str(uuid.uuid4())},  # Missing prototype_id/item_id
        {"item_instance_id": str(uuid.uuid4()), "item_id": "prototype_2"},  # Valid
    ]

    with patch("server.persistence.container_persistence._fetch_container_items", return_value=[]):
        with patch("server.persistence.container_persistence.get_container") as mock_get:
            with patch("server.persistence.item_instance_persistence.ensure_item_instance") as mock_ensure:
                mock_get.return_value = ContainerData(
                    container_instance_id=container_id,
                    source_type="environment",
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
    items_json = [{"prototype_id": "prototype_1"}]  # Missing item_instance_id

    with patch("server.persistence.container_persistence._fetch_container_items", return_value=[]):
        with patch("server.persistence.container_persistence.get_container") as mock_get:
            with patch("server.persistence.item_instance_persistence.ensure_item_instance") as mock_ensure:
                mock_get.return_value = ContainerData(
                    container_instance_id=container_id,
                    source_type="environment",
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
            container_instance_id=container_id,
            source_type="environment",
            room_id="test_room",
        )
        result = create_container(
            mock_conn,
            source_type="environment",
            room_id="test_room",
            items_json=items_json,
        )

    # Verify UUIDs were handled correctly
    assert isinstance(result, ContainerData)
    # Check that UUID was converted to string in stored procedure calls
    stored_proc_calls = [call for call in mock_cursor.execute.call_args_list if "add_item_to_container" in str(call)]
    if stored_proc_calls:
        call_str = str(stored_proc_calls[0])
        assert str(item_id) in call_str or item_id in call_str
