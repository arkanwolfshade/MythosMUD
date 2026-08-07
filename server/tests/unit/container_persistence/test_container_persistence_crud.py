"""
Unit tests for container_persistence create/get/update/delete paths.

Split from test_container_persistence.py to stay under Lizard file-nloc limit.
"""

# pyright: reportAny=false
# MagicMock attribute chains are Any in typeshed; suppressing matches test_container_persistence.py.

from unittest.mock import MagicMock, patch
from uuid import uuid4

import psycopg2
import pytest

from server.container_persistence.container_persistence import (
    ContainerData,
    create_container,
    delete_container,
    get_container,
    get_containers_by_entity_id,
    get_containers_by_room_id,
    update_container,
)
from server.exceptions import DatabaseError, ValidationError
from server.persistence.container_create_params import ContainerCreateParams


def test_create_container_invalid_source_type():
    """Test create_container with invalid source_type."""
    mock_conn = MagicMock()
    with pytest.raises(ValidationError):
        _ = create_container(mock_conn, source_type="invalid")


def test_create_container_invalid_capacity():
    """Test create_container with invalid capacity_slots."""
    mock_conn = MagicMock()
    with pytest.raises(ValidationError):
        _ = create_container(mock_conn, "environment", ContainerCreateParams(capacity_slots=0))


def test_create_container_invalid_lock_state():
    """Test create_container with invalid lock_state."""
    mock_conn = MagicMock()
    with pytest.raises(ValidationError):
        _ = create_container(mock_conn, "environment", ContainerCreateParams(lock_state="invalid"))


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
        _ = update_container(mock_conn, container_id, lock_state="invalid")


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
        _ = create_container(mock_conn, source_type="environment")


def test_get_container_database_error():
    """Test get_container handles database errors."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.execute.side_effect = psycopg2.Error("Database error")
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    with pytest.raises(DatabaseError):
        _ = get_container(mock_conn, container_id)


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
                "environment",
                ContainerCreateParams(room_id="room_001", capacity_slots=10),
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
            _ = create_container(
                mock_conn,
                "environment",
                ContainerCreateParams(items_json=items_json),
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
        _ = create_container(mock_conn, source_type="environment")


def test_create_container_capacity_too_high():
    """Test create_container with capacity_slots > 20."""
    mock_conn = MagicMock()
    with pytest.raises(ValidationError):
        _ = create_container(mock_conn, "environment", ContainerCreateParams(capacity_slots=21))


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
        "allowed_roles": list[str](),
        "metadata_json": dict[str, object](),
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
        "container_item_instance_id": None,
    }
    mock_cursor.fetchone.return_value = mock_row
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.close = MagicMock()

    with patch("server.container_persistence.container_persistence.fetch_container_items", return_value=[]):
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
        "allowed_roles": list[str](),
        "metadata_json": dict[str, object](),
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
        "container_item_instance_id": None,
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.close = MagicMock()

    with patch("server.container_persistence.container_persistence.fetch_container_items", return_value=[]):
        result = get_containers_by_room_id(mock_conn, "room_001")

    assert len(result) == 1
    assert isinstance(result[0], ContainerData)
    assert result[0].container_instance_id == container_id


def test_get_containers_by_room_id_database_error():
    """Test get_containers_by_room_id handles database errors."""
    mock_conn = MagicMock()
    mock_conn.cursor.side_effect = psycopg2.Error("Database error")

    with pytest.raises(DatabaseError):
        _ = get_containers_by_room_id(mock_conn, "room_001")


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
        "allowed_roles": list[str](),
        "metadata_json": dict[str, object](),
        "created_at": datetime.now(UTC),
        "updated_at": datetime.now(UTC),
        "container_item_instance_id": None,
    }
    mock_cursor.fetchall.return_value = [mock_row]
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.close = MagicMock()

    with patch("server.container_persistence.container_persistence.fetch_container_items", return_value=[]):
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
        _ = get_containers_by_entity_id(mock_conn, entity_id)


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

    items_json: list[dict[str, object]] = [{"item_instance_id": str(uuid4())}]

    with patch("server.container_persistence.container_persistence.get_container") as mock_get:
        mock_container = ContainerData(
            container_instance_id=container_id,
            source_type="environment",
        )
        mock_get.return_value = mock_container
        with patch("server.container_persistence.container_persistence.logger"):
            _ = update_container(mock_conn, container_id, items_json=items_json)

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
        _ = update_container(mock_conn, container_id, lock_state="locked")


def test_update_container_only_items_json_no_updates():
    """Test update_container with only items_json (no lock_state or metadata_json)."""

    container_id = uuid4()
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None  # No row returned when updates is empty
    mock_conn.cursor.return_value = mock_cursor
    mock_conn.commit = MagicMock()
    mock_cursor.close = MagicMock()

    items_json: list[dict[str, object]] = [{"item_instance_id": str(uuid4())}]

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
    items_json: list[dict[str, object]] = [
        {"item_name": "Item without ID"},  # Missing both IDs
        {"item_id": str(uuid4())},  # Has item_id
    ]

    with patch("server.container_persistence.container_persistence.get_container"):
        _ = update_container(mock_conn, container_id, items_json=items_json)

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
        _ = delete_container(mock_conn, container_id)


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
                "environment",
                ContainerCreateParams(owner_id=owner_id, room_id="room_001"),
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
                "environment",
                ContainerCreateParams(
                    owner_id=owner_id,
                    room_id="room_001",
                    items_json=[{"item_id": "item_001"}],
                ),
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
            _ = create_container(
                mock_conn,
                "environment",
                ContainerCreateParams(items_json=items_json),
            )

    # Should only call execute for the item with item_instance_id
    # create_container calls add_item_to_container for each valid item
    # So we should see execute called for the valid item (skipping the one without ID)
    assert mock_cursor.execute.call_count >= 1
