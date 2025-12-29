"""
Unit tests for container_persistence package container persistence module.

Tests the container persistence functions from server.container_persistence.container_persistence.
"""

import json
from unittest.mock import MagicMock, patch
from uuid import uuid4

import psycopg2
import pytest

from server.container_persistence.container_persistence import (
    ContainerData,
    _fetch_container_items,
    _parse_jsonb_column,
    create_container,
    delete_container,
    get_container,
    get_containers_by_entity_id,
    get_containers_by_room_id,
    update_container,
)
from server.exceptions import DatabaseError, ValidationError


def test_parse_jsonb_column_none():
    """Test parsing None JSONB column."""
    result = _parse_jsonb_column(None, {})
    assert result == {}


def test_parse_jsonb_column_string():
    """Test parsing string JSONB column."""
    data = {"key": "value"}
    result = _parse_jsonb_column(json.dumps(data), {})
    assert result == data


def test_parse_jsonb_column_dict():
    """Test parsing dict JSONB column."""
    data = {"key": "value"}
    result = _parse_jsonb_column(data, {})
    assert result == data


def test_parse_jsonb_column_empty_string():
    """Test parsing empty string JSONB column."""
    result = _parse_jsonb_column("", {})
    assert result == {}


def test_parse_jsonb_column_list():
    """Test parsing list JSONB column."""
    data = [1, 2, 3]
    result = _parse_jsonb_column(data, [])
    assert result == data


def test_parse_jsonb_column_invalid_json():
    """Test parsing invalid JSON string."""
    with pytest.raises(json.JSONDecodeError):
        _parse_jsonb_column("{invalid json}", {})


def test_container_data_init():
    """Test ContainerData initialization."""
    container_id = uuid4()
    data = ContainerData(
        container_instance_id=container_id,
        source_type="environment",
        owner_id=uuid4(),
        room_id="room_001",
    )
    assert data.container_instance_id == container_id
    assert data.source_type == "environment"
    assert data.room_id == "room_001"


def test_container_data_to_dict():
    """Test ContainerData.to_dict() conversion."""
    container_id = uuid4()
    owner_id = uuid4()
    data = ContainerData(
        container_instance_id=container_id,
        source_type="environment",
        owner_id=owner_id,
        room_id="room_001",
        items_json=[{"item_id": "item_001"}],
        metadata_json={"key": "value"},
    )
    result = data.to_dict()
    assert result["container_id"] == container_id
    assert result["source_type"] == "environment"
    assert result["owner_id"] == owner_id
    assert result["room_id"] == "room_001"
    assert result["items"] == [{"item_id": "item_001"}]
    assert result["metadata"] == {"key": "value"}


def test_fetch_container_items_empty():
    """Test _fetch_container_items with no items."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = []
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    result = _fetch_container_items(mock_conn, container_id)
    assert result == []
    mock_cursor.execute.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_fetch_container_items_with_items():
    """Test _fetch_container_items with items."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    # Create mock row with all required fields
    mock_row = {
        "item_instance_id": str(uuid4()),
        "item_id": str(uuid4()),
        "item_name": "Test Item",
        "quantity": 1,
        "condition": "pristine",
        "metadata": {"key": "value"},
        "position": 0,
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    result = _fetch_container_items(mock_conn, container_id)
    assert len(result) == 1
    assert result[0]["item_name"] == "Test Item"
    assert result[0]["quantity"] == 1


def test_fetch_container_items_missing_item_instance_id():
    """Test _fetch_container_items skips rows with missing item_instance_id."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor

    # Row without item_instance_id
    mock_row = {
        "item_id": str(uuid4()),
        "item_name": "Test Item",
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    with patch("server.container_persistence.container_persistence.logger") as mock_logger:
        result = _fetch_container_items(mock_conn, container_id)
        assert result == []
        mock_logger.warning.assert_called()


def test_create_container_invalid_source_type():
    """Test create_container with invalid source_type."""
    mock_conn = MagicMock()
    with pytest.raises(ValidationError):
        create_container(mock_conn, source_type="invalid")


def test_create_container_invalid_capacity():
    """Test create_container with invalid capacity_slots."""
    mock_conn = MagicMock()
    with pytest.raises(ValidationError):
        create_container(mock_conn, source_type="environment", capacity_slots=0)


def test_create_container_invalid_lock_state():
    """Test create_container with invalid lock_state."""
    mock_conn = MagicMock()
    with pytest.raises(ValidationError):
        create_container(mock_conn, source_type="environment", lock_state="invalid")


def test_get_container_not_found():
    """Test get_container when container doesn't exist."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = None
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    result = get_container(mock_conn, container_id)
    assert result is None


def test_get_containers_by_room_id_empty():
    """Test get_containers_by_room_id with no containers."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = []
    mock_cursor.close = MagicMock()

    result = get_containers_by_room_id(mock_conn, "room_001")
    assert result == []


def test_get_containers_by_entity_id_empty():
    """Test get_containers_by_entity_id with no containers."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = []
    mock_cursor.close = MagicMock()

    entity_id = uuid4()
    result = get_containers_by_entity_id(mock_conn, entity_id)
    assert result == []


def test_update_container_invalid_lock_state():
    """Test update_container with invalid lock_state."""
    mock_conn = MagicMock()
    container_id = uuid4()
    with pytest.raises(ValidationError):
        update_container(mock_conn, container_id, lock_state="invalid")


def test_delete_container_not_found():
    """Test delete_container when container doesn't exist."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = None
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    result = delete_container(mock_conn, container_id)
    assert result is False


def test_delete_container_success():
    """Test delete_container when container exists."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = (uuid4(),)  # Return container_id
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    with patch("server.container_persistence.container_persistence.logger"):
        result = delete_container(mock_conn, container_id)
        assert result is True


def test_create_container_database_error():
    """Test create_container handles database errors."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.execute.side_effect = psycopg2.Error("Database error")
    mock_conn.rollback = MagicMock()

    with pytest.raises(DatabaseError):
        create_container(mock_conn, source_type="environment")


def test_get_container_database_error():
    """Test get_container handles database errors."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.execute.side_effect = psycopg2.Error("Database error")
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    with pytest.raises(DatabaseError):
        get_container(mock_conn, container_id)


def test_fetch_container_items_non_dict_row():
    """Test _fetch_container_items handles non-dictionary rows."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    # Mix of dict and non-dict rows
    mock_cursor.fetchall.return_value = [
        "not a dict",
        {
            "item_instance_id": str(uuid4()),
            "item_id": str(uuid4()),
            "item_name": "Test Item",
            "quantity": 1,
            "condition": "pristine",
            "metadata": {},
            "position": 0,
        },
    ]
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    with patch("server.container_persistence.container_persistence.logger") as mock_logger:
        result = _fetch_container_items(mock_conn, container_id)

    # Should skip non-dict row, keep dict row
    assert len(result) == 1
    mock_logger.warning.assert_called()


def test_fetch_container_items_string_metadata():
    """Test _fetch_container_items parses string metadata."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_row = {
        "item_instance_id": str(uuid4()),
        "item_id": str(uuid4()),
        "item_name": "Test Item",
        "quantity": 1,
        "condition": "pristine",
        "metadata": json.dumps({"key": "value"}),
        "position": 0,
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    result = _fetch_container_items(mock_conn, container_id)

    assert result[0]["metadata"] == {"key": "value"}


def test_fetch_container_items_invalid_json_metadata():
    """Test _fetch_container_items handles invalid JSON metadata."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_row = {
        "item_instance_id": str(uuid4()),
        "item_id": str(uuid4()),
        "item_name": "Test Item",
        "quantity": 1,
        "condition": "pristine",
        "metadata": "{invalid json}",
        "position": 0,
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    result = _fetch_container_items(mock_conn, container_id)

    # Should default to {} on JSON parse error
    assert result[0]["metadata"] == {}


def test_fetch_container_items_non_dict_metadata():
    """Test _fetch_container_items handles non-dict metadata."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_row = {
        "item_instance_id": str(uuid4()),
        "item_id": str(uuid4()),
        "item_name": "Test Item",
        "quantity": 1,
        "condition": "pristine",
        "metadata": "not a dict",
        "position": 0,
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    result = _fetch_container_items(mock_conn, container_id)

    # Should default to {} for non-dict metadata
    assert result[0]["metadata"] == {}


def test_fetch_container_items_missing_fields():
    """Test _fetch_container_items handles missing optional fields."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_row = {
        "item_instance_id": str(uuid4()),
        # Missing item_id, item_name, quantity, condition, position
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    result = _fetch_container_items(mock_conn, container_id)

    assert len(result) == 1
    assert result[0]["item_id"] is None
    assert result[0]["item_name"] == "Unknown Item"
    assert result[0]["quantity"] == 1
    assert result[0]["condition"] == "pristine"
    assert result[0]["position"] == 0


def test_create_container_success():
    """Test create_container successfully creates container."""
    from datetime import UTC, datetime

    container_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {
        "container_instance_id": container_id,
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
    }
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.commit = MagicMock()

    with patch("server.container_persistence.container_persistence.get_container", return_value=None):
        with patch("server.container_persistence.container_persistence.logger"):
            result = create_container(
                mock_conn,
                source_type="environment",
                room_id="room_001",
                capacity_slots=10,
            )

    assert isinstance(result, ContainerData)
    assert result.source_type == "environment"
    assert result.room_id == "room_001"
    assert result.capacity_slots == 10
    mock_conn.commit.assert_called()


def test_create_container_with_items():
    """Test create_container with items_json."""
    from datetime import UTC, datetime

    container_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {
        "container_instance_id": container_id,
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
    }
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.commit = MagicMock()

    items_json = [{"item_instance_id": str(uuid4())}, {"item_id": str(uuid4())}]

    with patch("server.container_persistence.container_persistence.get_container", return_value=None):
        with patch("server.container_persistence.container_persistence.logger"):
            create_container(
                mock_conn,
                source_type="environment",
                items_json=items_json,
            )

    # Should have called execute for each item
    assert mock_cursor.execute.call_count >= 2  # At least clear + items
    mock_conn.commit.assert_called()


def test_create_container_no_id_returned():
    """Test create_container handles case where no ID is returned."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None  # No row returned
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.commit = MagicMock()

    with pytest.raises(DatabaseError, match="Failed to create container - no ID returned"):
        create_container(mock_conn, source_type="environment")


def test_create_container_capacity_too_high():
    """Test create_container with capacity_slots > 20."""
    mock_conn = MagicMock()
    with pytest.raises(ValidationError):
        create_container(mock_conn, source_type="environment", capacity_slots=21)


def test_get_container_success():
    """Test get_container successfully retrieves container."""
    from datetime import UTC, datetime

    container_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_row = {
        "container_instance_id": container_id,
        "source_type": "environment",
        "owner_id": None,
        "room_id": "room_001",
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
    mock_cursor.close = MagicMock()

    with patch("server.container_persistence.container_persistence._fetch_container_items", return_value=[]):
        result = get_container(mock_conn, container_id)

    assert isinstance(result, ContainerData)
    assert result.container_instance_id == container_id
    assert result.source_type == "environment"


def test_get_containers_by_room_id_success():
    """Test get_containers_by_room_id successfully retrieves containers."""
    from datetime import UTC, datetime

    container_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_row = {
        "container_instance_id": container_id,
        "source_type": "environment",
        "owner_id": None,
        "room_id": "room_001",
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
    mock_cursor.close = MagicMock()

    with patch("server.container_persistence.container_persistence._fetch_container_items", return_value=[]):
        result = get_containers_by_room_id(mock_conn, "room_001")

    assert len(result) == 1
    assert isinstance(result[0], ContainerData)
    assert result[0].container_instance_id == container_id


def test_get_containers_by_room_id_database_error():
    """Test get_containers_by_room_id handles database errors."""
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = psycopg2.Error("Database error")

    with pytest.raises(DatabaseError):
        get_containers_by_room_id(mock_conn, "room_001")


def test_get_containers_by_entity_id_success():
    """Test get_containers_by_entity_id successfully retrieves containers."""
    from datetime import UTC, datetime

    container_id = uuid4()
    entity_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
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
    mock_cursor.close = MagicMock()

    with patch("server.container_persistence.container_persistence._fetch_container_items", return_value=[]):
        result = get_containers_by_entity_id(mock_conn, entity_id)

    assert len(result) == 1
    assert isinstance(result[0], ContainerData)
    assert result[0].entity_id == entity_id


def test_get_containers_by_entity_id_database_error():
    """Test get_containers_by_entity_id handles database errors."""
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = psycopg2.Error("Database error")

    entity_id = uuid4()
    with pytest.raises(DatabaseError):
        get_containers_by_entity_id(mock_conn, entity_id)


def test_update_container_success():
    """Test update_container successfully updates container."""

    container_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (container_id,)
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.commit = MagicMock()
    mock_cursor.close = MagicMock()

    with patch("server.container_persistence.container_persistence.get_container") as mock_get:
        mock_container = ContainerData(
            container_instance_id=container_id,
            source_type="environment",
        )
        mock_get.return_value = mock_container
        with patch("server.container_persistence.container_persistence.logger"):
            result = update_container(
                mock_conn,
                container_id,
                lock_state="locked",
                metadata_json={"key": "value"},
            )

    assert result == mock_container
    mock_conn.commit.assert_called()


def test_update_container_with_items():
    """Test update_container with items_json."""

    container_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (container_id,)
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.commit = MagicMock()
    mock_cursor.close = MagicMock()

    items_json = [{"item_instance_id": str(uuid4())}]

    with patch("server.container_persistence.container_persistence.get_container") as mock_get:
        mock_container = ContainerData(
            container_instance_id=container_id,
            source_type="environment",
        )
        mock_get.return_value = mock_container
        with patch("server.container_persistence.container_persistence.logger"):
            update_container(mock_conn, container_id, items_json=items_json)

    # Should have called clear_container_contents and add_item_to_container
    assert mock_cursor.execute.call_count >= 2
    mock_conn.commit.assert_called()


def test_update_container_database_error():
    """Test update_container handles database errors."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.execute.side_effect = psycopg2.Error("Database error")
    mock_conn.rollback = MagicMock()

    container_id = uuid4()
    with pytest.raises(DatabaseError):
        update_container(mock_conn, container_id, lock_state="locked")


def test_update_container_only_items_json_no_updates():
    """Test update_container with only items_json (no lock_state or metadata_json)."""

    container_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None  # No row returned when updates is empty
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.commit = MagicMock()
    mock_cursor.close = MagicMock()

    items_json = [{"item_instance_id": str(uuid4())}]

    result = update_container(mock_conn, container_id, items_json=items_json)

    # When only items_json is provided, updates list is empty, so row is None
    # This should return None (container not found or no updates)
    assert result is None
    # Should have called clear_container_contents and add_item_to_container
    assert mock_cursor.execute.call_count >= 2
    mock_conn.commit.assert_called()


def test_update_container_items_json_only_no_item_ids():
    """Test update_container with items_json containing items without IDs."""

    container_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.commit = MagicMock()
    mock_cursor.close = MagicMock()

    # Items without item_instance_id or item_id should be skipped
    items_json = [
        {"item_name": "Item without ID"},  # Missing both IDs
        {"item_id": str(uuid4())},  # Has item_id
    ]

    with patch("server.container_persistence.container_persistence.get_container"):
        update_container(mock_conn, container_id, items_json=items_json)

    # Should only call execute for clear_container_contents and the item with item_id
    # clear_container_contents + 1 item with ID = 2 calls
    assert mock_cursor.execute.call_count == 2


def test_delete_container_database_error():
    """Test delete_container handles database errors."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.execute.side_effect = psycopg2.Error("Database error")
    mock_conn.rollback = MagicMock()

    container_id = uuid4()
    with pytest.raises(DatabaseError):
        delete_container(mock_conn, container_id)


def test_container_data_to_dict_with_datetimes():
    """Test ContainerData.to_dict() with datetime fields."""
    from datetime import UTC, datetime

    container_id = uuid4()
    created_at = datetime.now(UTC)
    updated_at = datetime.now(UTC)
    decay_at = datetime.now(UTC)

    data = ContainerData(
        container_instance_id=container_id,
        source_type="corpse",
        decay_at=decay_at,
        created_at=created_at,
        updated_at=updated_at,
    )
    result = data.to_dict()

    assert result["decay_at"] == decay_at
    # Note: created_at and updated_at are not in to_dict() result
    # They're stored but not returned in the dict


def test_container_data_to_dict_with_all_fields():
    """Test ContainerData.to_dict() with all optional fields."""
    from datetime import UTC, datetime

    container_id = uuid4()
    owner_id = uuid4()
    entity_id = uuid4()
    decay_at = datetime.now(UTC)

    data = ContainerData(
        container_instance_id=container_id,
        source_type="equipment",
        owner_id=owner_id,
        entity_id=entity_id,
        lock_state="locked",
        capacity_slots=15,
        weight_limit=100,
        decay_at=decay_at,
        allowed_roles=["admin", "moderator"],
        items_json=[{"item_id": "item_001"}],
        metadata_json={"key": "value"},
    )
    result = data.to_dict()

    assert result["container_id"] == container_id
    assert result["owner_id"] == owner_id
    assert result["entity_id"] == entity_id
    assert result["lock_state"] == "locked"
    assert result["capacity_slots"] == 15
    assert result["weight_limit"] == 100
    assert result["decay_at"] == decay_at
    assert result["allowed_roles"] == ["admin", "moderator"]
    assert result["items"] == [{"item_id": "item_001"}]
    assert result["metadata"] == {"key": "value"}


def test_create_container_get_container_success():
    """Test create_container returns get_container result when successful."""
    from datetime import UTC, datetime

    container_id = uuid4()
    owner_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {
        "container_instance_id": container_id,
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
    }
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.commit = MagicMock()

    # Mock get_container to return a ContainerData
    mock_container = ContainerData(
        container_instance_id=container_id,
        source_type="environment",
        owner_id=owner_id,
        room_id="room_001",
    )

    with patch("server.container_persistence.container_persistence.get_container", return_value=mock_container):
        with patch("server.container_persistence.container_persistence.logger"):
            result = create_container(
                mock_conn,
                source_type="environment",
                owner_id=owner_id,
                room_id="room_001",
            )

    # Should return the result from get_container, not fallback
    assert result == mock_container
    assert result.container_instance_id == container_id


def test_create_container_get_container_fallback():
    """Test create_container uses fallback ContainerData when get_container returns None."""
    from datetime import UTC, datetime

    container_id = uuid4()
    owner_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {
        "container_instance_id": container_id,
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
    }
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.commit = MagicMock()

    with patch("server.container_persistence.container_persistence.get_container", return_value=None):
        with patch("server.container_persistence.container_persistence.logger"):
            result = create_container(
                mock_conn,
                source_type="environment",
                owner_id=owner_id,
                room_id="room_001",
                items_json=[{"item_id": "item_001"}],
            )

    # Should return fallback ContainerData
    assert isinstance(result, ContainerData)
    assert result.container_instance_id == container_id
    assert result.owner_id == owner_id
    assert result.room_id == "room_001"
    assert result.items_json == [{"item_id": "item_001"}]


def test_create_container_items_missing_item_id():
    """Test create_container skips items without item_instance_id or item_id."""
    from datetime import UTC, datetime

    container_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {
        "container_instance_id": container_id,
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
    }
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.commit = MagicMock()

    # Items without item_instance_id or item_id should be skipped
    items_json = [
        {"item_name": "Item without ID"},  # Missing both item_instance_id and item_id
        {"item_instance_id": str(uuid4())},  # Has item_instance_id
    ]

    with patch("server.container_persistence.container_persistence.get_container", return_value=None):
        with patch("server.container_persistence.container_persistence.logger"):
            create_container(
                mock_conn,
                source_type="environment",
                items_json=items_json,
            )

    # Should only call execute for the item with item_instance_id
    # create_container calls add_item_to_container for each valid item
    # So we should see execute called for the valid item (skipping the one without ID)
    assert mock_cursor.execute.call_count >= 1
