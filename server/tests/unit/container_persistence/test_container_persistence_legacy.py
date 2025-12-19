"""
Tests for container persistence operations in container_persistence package.

This module tests container creation, retrieval, update, and deletion
operations for the unified container system.
"""

import uuid
from datetime import UTC, datetime
from typing import Any
from unittest.mock import Mock, patch

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


class TestParseJsonbColumn:
    """Test _parse_jsonb_column helper function."""

    def test_parse_jsonb_column_with_none(self) -> None:
        """Test _parse_jsonb_column returns default for None."""
        result = _parse_jsonb_column(None, {})
        assert result == {}

    def test_parse_jsonb_column_with_string(self) -> None:
        """Test _parse_jsonb_column parses JSON string."""
        json_str = '{"key": "value"}'
        result = _parse_jsonb_column(json_str, {})
        assert result == {"key": "value"}

    def test_parse_jsonb_column_with_empty_string(self) -> None:
        """Test _parse_jsonb_column returns default for empty string."""
        result = _parse_jsonb_column("", {})
        assert result == {}

    def test_parse_jsonb_column_with_dict(self) -> None:
        """Test _parse_jsonb_column returns dict as-is."""
        data = {"key": "value"}
        result = _parse_jsonb_column(data, {})
        assert result == data

    def test_parse_jsonb_column_with_list(self) -> None:
        """Test _parse_jsonb_column returns list as-is."""
        data = [1, 2, 3]
        result = _parse_jsonb_column(data, [])
        assert result == data

    def test_parse_jsonb_column_with_empty_dict(self) -> None:
        """Test _parse_jsonb_column returns default for empty dict (falsy value)."""
        # Empty dict {} is falsy, so function returns default
        result = _parse_jsonb_column({}, {"default": "value"})
        assert result == {"default": "value"}


class TestFetchContainerItems:
    """Test _fetch_container_items helper function."""

    def test_fetch_container_items_empty(self) -> None:
        """Test _fetch_container_items returns empty list when no items."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.fetchall = Mock(return_value=[])
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        result = _fetch_container_items(mock_conn, container_id)
        assert result == []

    def test_fetch_container_items_with_items(self) -> None:
        """Test _fetch_container_items returns items list."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        mock_row: dict[str, Any] = {
            "item_instance_id": str(uuid.uuid4()),
            "item_id": "item-123",
            "item_name": "Test Item",
            "quantity": 5,
            "condition": "good",
            "metadata": '{"key": "value"}',
            "position": 0,
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row])
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        result = _fetch_container_items(mock_conn, container_id)
        assert len(result) == 1
        assert result[0]["item_instance_id"] == mock_row["item_instance_id"]
        assert result[0]["item_name"] == "Test Item"

    def test_fetch_container_items_skips_non_dict_row(self) -> None:
        """Test _fetch_container_items skips non-dictionary rows."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        # Return a non-dict row (tuple)
        mock_cursor.fetchall = Mock(return_value=[("not", "a", "dict")])
        mock_cursor.close = Mock()

        with patch("server.container_persistence.container_persistence.logger.warning") as mock_warning:
            container_id = uuid.uuid4()
            result = _fetch_container_items(mock_conn, container_id)
            assert result == []
            mock_warning.assert_called_once()

    def test_fetch_container_items_skips_missing_item_instance_id(self) -> None:
        """Test _fetch_container_items skips rows without item_instance_id."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        mock_row: dict[str, Any] = {
            "item_id": "item-123",
            "item_name": "Test Item",
            # Missing item_instance_id
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row])
        mock_cursor.close = Mock()

        with patch("server.container_persistence.container_persistence.logger.warning") as mock_warning:
            container_id = uuid.uuid4()
            result = _fetch_container_items(mock_conn, container_id)
            assert result == []
            mock_warning.assert_called_once()

    def test_fetch_container_items_parses_string_metadata(self) -> None:
        """Test _fetch_container_items parses string metadata."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        mock_row: dict[str, Any] = {
            "item_instance_id": str(uuid.uuid4()),
            "item_id": "item-123",
            "item_name": "Test Item",
            "quantity": 1,
            "condition": "pristine",
            "metadata": '{"key": "value"}',
            "position": 0,
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row])
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        result = _fetch_container_items(mock_conn, container_id)
        assert result[0]["metadata"] == {"key": "value"}

    def test_fetch_container_items_handles_invalid_json_metadata(self) -> None:
        """Test _fetch_container_items handles invalid JSON metadata."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        mock_row: dict[str, Any] = {
            "item_instance_id": str(uuid.uuid4()),
            "item_id": "item-123",
            "item_name": "Test Item",
            "quantity": 1,
            "condition": "pristine",
            "metadata": "{invalid json}",  # Invalid JSON
            "position": 0,
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row])
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        result = _fetch_container_items(mock_conn, container_id)
        assert result[0]["metadata"] == {}  # Should default to empty dict

    def test_fetch_container_items_handles_none_quantity_and_condition(self) -> None:
        """Test _fetch_container_items handles None quantity and condition."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        mock_row: dict[str, Any] = {
            "item_instance_id": str(uuid.uuid4()),
            "item_id": "item-123",
            "item_name": "Test Item",
            "quantity": None,
            "condition": None,
            "metadata": None,
            "position": None,
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row])
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        result = _fetch_container_items(mock_conn, container_id)
        assert result[0]["quantity"] == 1  # Should default to 1
        assert result[0]["condition"] == "pristine"  # Should default to pristine
        assert result[0]["position"] == 0  # Should default to 0
        assert result[0]["metadata"] == {}  # Should default to empty dict

    def test_fetch_container_items_handles_none_item_name(self) -> None:
        """Test _fetch_container_items handles None item_name."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        mock_row: dict[str, Any] = {
            "item_instance_id": str(uuid.uuid4()),
            "item_id": "item-123",
            "item_name": None,
            "quantity": 1,
            "condition": "pristine",
            "metadata": {},
            "position": 0,
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row])
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        result = _fetch_container_items(mock_conn, container_id)
        assert result[0]["item_name"] == "Unknown Item"  # Should default to Unknown Item

    def test_fetch_container_items_handles_none_metadata(self) -> None:
        """Test _fetch_container_items handles None metadata."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        mock_row: dict[str, Any] = {
            "item_instance_id": str(uuid.uuid4()),
            "item_id": "item-123",
            "item_name": "Test Item",
            "quantity": 1,
            "condition": "pristine",
            "metadata": None,
            "position": 0,
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row])
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        result = _fetch_container_items(mock_conn, container_id)
        assert result[0]["metadata"] == {}

    def test_fetch_container_items_handles_non_dict_metadata(self) -> None:
        """Test _fetch_container_items handles non-dict metadata."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        mock_row: dict[str, Any] = {
            "item_instance_id": str(uuid.uuid4()),
            "item_id": "item-123",
            "item_name": "Test Item",
            "quantity": 1,
            "condition": "pristine",
            "metadata": ["not", "a", "dict"],  # Not a dict
            "position": 0,
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row])
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        result = _fetch_container_items(mock_conn, container_id)
        assert result[0]["metadata"] == {}


class TestContainerData:
    """Test ContainerData class."""

    def test_container_data_initialization(self) -> None:
        """Test ContainerData initialization."""
        container_id = uuid.uuid4()
        container = ContainerData(
            container_instance_id=container_id,
            source_type="environment",
            owner_id=uuid.uuid4(),
            room_id="room-123",
            lock_state="unlocked",
            capacity_slots=10,
        )
        assert container.container_instance_id == container_id
        assert container.source_type == "environment"
        assert container.lock_state == "unlocked"
        assert container.capacity_slots == 10

    def test_container_data_to_dict(self) -> None:
        """Test ContainerData.to_dict() method."""
        container_id = uuid.uuid4()
        owner_id = uuid.uuid4()
        container = ContainerData(
            container_instance_id=container_id,
            source_type="equipment",
            owner_id=owner_id,
            lock_state="locked",
            capacity_slots=5,
            items_json=[{"item_id": "item-1"}],
            metadata_json={"key": "value"},
        )
        result = container.to_dict()
        # to_dict() converts UUIDs to UUID objects
        assert isinstance(result["container_id"], uuid.UUID)
        assert result["container_id"] == container_id
        assert result["source_type"] == "equipment"
        assert isinstance(result["owner_id"], uuid.UUID)
        assert result["owner_id"] == owner_id

    def test_container_data_to_dict_with_none_values(self) -> None:
        """Test ContainerData.to_dict() with None owner_id and entity_id."""
        container_id = uuid.uuid4()
        container = ContainerData(
            container_instance_id=container_id,
            source_type="environment",
            owner_id=None,
            entity_id=None,
            room_id="room-123",
        )
        result = container.to_dict()
        assert result["owner_id"] is None
        assert result["entity_id"] is None
        assert result["room_id"] == "room-123"

    def test_container_data_to_dict_with_all_fields(self) -> None:
        """Test ContainerData.to_dict() with all fields populated."""
        container_id = uuid.uuid4()
        owner_id = uuid.uuid4()
        entity_id = uuid.uuid4()
        decay_at = datetime.now(UTC).replace(tzinfo=None)
        created_at = datetime.now(UTC).replace(tzinfo=None)
        updated_at = datetime.now(UTC).replace(tzinfo=None)

        container = ContainerData(
            container_instance_id=container_id,
            source_type="corpse",
            owner_id=owner_id,
            room_id="room-123",
            entity_id=entity_id,
            lock_state="sealed",
            capacity_slots=15,
            weight_limit=100,
            decay_at=decay_at,
            allowed_roles=["investigator", "researcher"],
            items_json=[{"item_id": "item-1"}],
            metadata_json={"key": "value"},
            created_at=created_at,
            updated_at=updated_at,
        )
        result = container.to_dict()
        assert isinstance(result["container_id"], uuid.UUID)
        assert result["container_id"] == container_id
        assert result["source_type"] == "corpse"
        assert isinstance(result["owner_id"], uuid.UUID)
        assert result["owner_id"] == owner_id
        assert isinstance(result["entity_id"], uuid.UUID)
        assert result["entity_id"] == entity_id
        assert result["lock_state"] == "sealed"
        assert result["capacity_slots"] == 15
        assert result["weight_limit"] == 100
        assert result["decay_at"] == decay_at
        assert result["allowed_roles"] == ["investigator", "researcher"]
        assert result["items"] == [{"item_id": "item-1"}]
        assert result["metadata"] == {"key": "value"}


class TestCreateContainer:
    """Test create_container function."""

    def test_create_container_invalid_source_type(self) -> None:
        """Test create_container raises ValidationError for invalid source_type."""
        mock_conn = Mock()

        with pytest.raises(ValidationError, match="Invalid source_type"):
            create_container(mock_conn, source_type="invalid_type")

    def test_create_container_invalid_capacity_slots_low(self) -> None:
        """Test create_container raises ValidationError for capacity_slots < 1."""
        mock_conn = Mock()

        with pytest.raises(ValidationError, match="Invalid capacity_slots"):
            create_container(mock_conn, source_type="environment", capacity_slots=0)

    def test_create_container_invalid_capacity_slots_high(self) -> None:
        """Test create_container raises ValidationError for capacity_slots > 20."""
        mock_conn = Mock()

        with pytest.raises(ValidationError, match="Invalid capacity_slots"):
            create_container(mock_conn, source_type="environment", capacity_slots=21)

    def test_create_container_invalid_lock_state(self) -> None:
        """Test create_container raises ValidationError for invalid lock_state."""
        mock_conn = Mock()

        with pytest.raises(ValidationError, match="Invalid lock_state"):
            create_container(mock_conn, source_type="environment", lock_state="invalid")

    def test_create_container_database_error(self) -> None:
        """Test create_container handles database errors."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock(side_effect=psycopg2.Error("Database error"))
        mock_conn.rollback = Mock()

        with pytest.raises(DatabaseError, match="Database error creating container"):
            create_container(mock_conn, source_type="environment")

    def test_create_container_no_row_returned(self) -> None:
        """Test create_container raises DatabaseError when no row is returned."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.fetchone = Mock(return_value=None)  # No row returned
        mock_cursor.close = Mock()
        mock_conn.commit = Mock()

        with patch(
            "server.container_persistence.container_persistence.log_and_raise",
            side_effect=DatabaseError("No ID returned"),
        ):
            with pytest.raises(DatabaseError, match="No ID returned"):
                create_container(mock_conn, source_type="environment")

    def test_create_container_success(self) -> None:
        """Test create_container successfully creates container."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id = uuid.uuid4()
        mock_row_data = {
            "container_instance_id": container_id,
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
        }
        mock_row = Mock()
        mock_row.__getitem__ = Mock(side_effect=mock_row_data.__getitem__)
        mock_cursor.fetchone = Mock(return_value=mock_row)
        mock_cursor.close = Mock()
        mock_conn.commit = Mock()

        with patch("server.container_persistence.container_persistence.get_container", return_value=None):
            with patch("server.container_persistence.container_persistence.logger.info") as mock_info:
                result = create_container(mock_conn, source_type="environment")
                assert result is not None
                assert result.container_instance_id == container_id
                # Should log container creation
                mock_info.assert_called_once()

    def test_create_container_with_items_json(self) -> None:
        """Test create_container handles items_json parameter."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id = uuid.uuid4()
        mock_row_data = {
            "container_instance_id": container_id,
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
        }
        mock_row = Mock()
        mock_row.__getitem__ = Mock(side_effect=mock_row_data.__getitem__)
        mock_cursor.fetchone = Mock(return_value=mock_row)
        mock_cursor.close = Mock()
        mock_conn.commit = Mock()

        items_json = [{"item_instance_id": str(uuid.uuid4()), "item_id": "item-123"}]

        with patch("server.container_persistence.container_persistence.get_container", return_value=None):
            result = create_container(mock_conn, source_type="environment", items_json=items_json)
            assert result is not None
            # Should execute add_item_to_container for each item
            assert mock_cursor.execute.call_count > 1

    def test_create_container_with_items_json_using_item_id(self) -> None:
        """Test create_container uses item_id when item_instance_id is missing."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id = uuid.uuid4()
        mock_row_data = {
            "container_instance_id": container_id,
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
        }
        mock_row = Mock()
        mock_row.__getitem__ = Mock(side_effect=mock_row_data.__getitem__)
        mock_cursor.fetchone = Mock(return_value=mock_row)
        mock_cursor.close = Mock()
        mock_conn.commit = Mock()

        # item_id is used when item_instance_id is missing
        items_json = [{"item_id": "item-123"}]  # No item_instance_id, but has item_id

        with patch("server.container_persistence.container_persistence.get_container", return_value=None):
            result = create_container(mock_conn, source_type="environment", items_json=items_json)
            assert result is not None
            # Should execute add_item_to_container using item_id
            assert mock_cursor.execute.call_count > 1

    def test_create_container_with_items_json_no_item_instance_id(self) -> None:
        """Test create_container skips items without item_instance_id."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id = uuid.uuid4()
        mock_row_data = {
            "container_instance_id": container_id,
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
        }
        mock_row = Mock()
        mock_row.__getitem__ = Mock(side_effect=mock_row_data.__getitem__)
        mock_cursor.fetchone = Mock(return_value=mock_row)
        mock_cursor.close = Mock()
        mock_conn.commit = Mock()

        # Items without item_instance_id or item_id should be skipped
        # The code uses: item_instance_id = item.get("item_instance_id") or item.get("item_id")
        # So if both are missing, item_instance_id is None and add_item_to_container is not called
        items_json: list[Any] = [{}]  # Empty dict - no item_instance_id or item_id

        with patch("server.container_persistence.container_persistence.get_container", return_value=None):
            result = create_container(mock_conn, source_type="environment", items_json=items_json)
            assert result is not None
            # Should not execute add_item_to_container for items without item_instance_id
            # Only the INSERT should be executed (items_json loop is skipped)
            assert mock_cursor.execute.call_count == 1

    def test_create_container_with_get_container_returning_value(self) -> None:
        """Test create_container when get_container returns a ContainerData."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id = uuid.uuid4()
        mock_row_data = {
            "container_instance_id": container_id,
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
        }
        mock_row = Mock()
        mock_row.__getitem__ = Mock(side_effect=mock_row_data.__getitem__)
        mock_cursor.fetchone = Mock(return_value=mock_row)
        mock_cursor.close = Mock()
        mock_conn.commit = Mock()

        mock_container = ContainerData(
            container_instance_id=container_id,
            source_type="environment",
        )

        with patch("server.container_persistence.container_persistence.get_container", return_value=mock_container):
            result = create_container(mock_conn, source_type="environment")
            assert result == mock_container
            # Should return the container from get_container, not create a new one

    def test_create_container_with_all_optional_parameters(self) -> None:
        """Test create_container with all optional parameters."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id = uuid.uuid4()
        owner_id = uuid.uuid4()
        entity_id = uuid.uuid4()
        mock_row_data = {
            "container_instance_id": container_id,
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
        }
        mock_row = Mock()
        mock_row.__getitem__ = Mock(side_effect=mock_row_data.__getitem__)
        mock_cursor.fetchone = Mock(return_value=mock_row)
        mock_cursor.close = Mock()
        mock_conn.commit = Mock()

        with patch("server.container_persistence.container_persistence.get_container", return_value=None):
            result = create_container(
                mock_conn,
                source_type="equipment",
                owner_id=owner_id,
                room_id="room-123",
                entity_id=entity_id,
                lock_state="locked",
                capacity_slots=10,
                weight_limit=100,
                decay_at=datetime.now(UTC).replace(tzinfo=None),
                allowed_roles=["admin", "player"],
                metadata_json={"key": "value"},
                container_item_instance_id="item-123",
            )
            assert result is not None
            assert result.owner_id == owner_id
            assert result.entity_id == entity_id
            assert result.lock_state == "locked"
            assert result.capacity_slots == 10


class TestGetContainer:
    """Test get_container function."""

    def test_get_container_not_found(self) -> None:
        """Test get_container returns None when container not found."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.fetchone = Mock(return_value=None)
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        result = get_container(mock_conn, container_id)
        assert result is None

    def test_get_container_success(self) -> None:
        """Test get_container returns ContainerData when found."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id = uuid.uuid4()
        mock_row: dict[str, Any] = {
            "container_instance_id": container_id,
            "source_type": "environment",
            "owner_id": None,
            "room_id": "room-123",
            "entity_id": None,
            "lock_state": "unlocked",
            "capacity_slots": 10,
            "weight_limit": None,
            "decay_at": None,
            "allowed_roles": [],
            "metadata_json": {},
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
            "container_item_instance_id": None,
        }
        mock_cursor.fetchone = Mock(return_value=mock_row)
        mock_cursor.close = Mock()

        with patch("server.container_persistence.container_persistence._fetch_container_items", return_value=[]):
            result = get_container(mock_conn, container_id)
            assert result is not None
            assert result.container_instance_id == container_id
            assert result.source_type == "environment"

    def test_get_container_database_error(self) -> None:
        """Test get_container handles database errors."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock(side_effect=psycopg2.Error("Database error"))
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        with pytest.raises(DatabaseError, match="Database error retrieving container"):
            get_container(mock_conn, container_id)


class TestGetContainersByRoomId:
    """Test get_containers_by_room_id function."""

    def test_get_containers_by_room_id_empty(self) -> None:
        """Test get_containers_by_room_id returns empty list."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.fetchall = Mock(return_value=[])
        mock_cursor.close = Mock()

        result = get_containers_by_room_id(mock_conn, "room-123")
        assert result == []

    def test_get_containers_by_room_id_with_results(self) -> None:
        """Test get_containers_by_room_id returns containers."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id = uuid.uuid4()
        mock_row: dict[str, Any] = {
            "container_instance_id": container_id,
            "source_type": "environment",
            "owner_id": None,
            "room_id": "room-123",
            "entity_id": None,
            "lock_state": "unlocked",
            "capacity_slots": 10,
            "weight_limit": None,
            "decay_at": None,
            "allowed_roles": [],
            "metadata_json": {},
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
            "container_item_instance_id": None,
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row])
        mock_cursor.close = Mock()

        with patch("server.container_persistence.container_persistence._fetch_container_items", return_value=[]):
            result = get_containers_by_room_id(mock_conn, "room-123")
            assert len(result) == 1
            assert result[0].container_instance_id == container_id

    def test_get_containers_by_room_id_database_error(self) -> None:
        """Test get_containers_by_room_id handles database errors."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock(side_effect=psycopg2.Error("Database error"))
        mock_cursor.close = Mock()

        with pytest.raises(DatabaseError, match="Database error retrieving containers"):
            get_containers_by_room_id(mock_conn, "room-123")


class TestGetContainersByEntityId:
    """Test get_containers_by_entity_id function."""

    def test_get_containers_by_entity_id_empty(self) -> None:
        """Test get_containers_by_entity_id returns empty list."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.fetchall = Mock(return_value=[])
        mock_cursor.close = Mock()

        entity_id = uuid.uuid4()
        result = get_containers_by_entity_id(mock_conn, entity_id)
        assert result == []

    def test_get_containers_by_entity_id_with_results(self) -> None:
        """Test get_containers_by_entity_id returns containers."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id = uuid.uuid4()
        entity_id = uuid.uuid4()
        mock_row: dict[str, Any] = {
            "container_instance_id": container_id,
            "source_type": "equipment",
            "owner_id": None,
            "room_id": None,
            "entity_id": entity_id,
            "lock_state": "unlocked",
            "capacity_slots": 10,
            "weight_limit": None,
            "decay_at": None,
            "allowed_roles": [],
            "metadata_json": {},
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
            "container_item_instance_id": None,
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row])
        mock_cursor.close = Mock()

        with patch("server.container_persistence.container_persistence._fetch_container_items", return_value=[]):
            result = get_containers_by_entity_id(mock_conn, entity_id)
            assert len(result) == 1
            assert result[0].container_instance_id == container_id
            assert result[0].entity_id == entity_id

    def test_get_containers_by_entity_id_with_multiple_containers(self) -> None:
        """Test get_containers_by_entity_id returns multiple containers."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id1 = uuid.uuid4()
        container_id2 = uuid.uuid4()
        entity_id = uuid.uuid4()
        mock_row1 = {
            "container_instance_id": container_id1,
            "source_type": "equipment",
            "owner_id": None,
            "room_id": None,
            "entity_id": entity_id,
            "lock_state": "unlocked",
            "capacity_slots": 10,
            "weight_limit": None,
            "decay_at": None,
            "allowed_roles": [],
            "metadata_json": {},
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
            "container_item_instance_id": None,
        }
        mock_row2 = {
            "container_instance_id": container_id2,
            "source_type": "equipment",
            "owner_id": None,
            "room_id": None,
            "entity_id": entity_id,
            "lock_state": "locked",
            "capacity_slots": 5,
            "weight_limit": 50,
            "decay_at": None,
            "allowed_roles": ["admin"],
            "metadata_json": {"key": "value"},
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
            "container_item_instance_id": None,
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row1, mock_row2])
        mock_cursor.close = Mock()

        with patch("server.container_persistence.container_persistence._fetch_container_items", return_value=[]):
            result = get_containers_by_entity_id(mock_conn, entity_id)
            assert len(result) == 2
            assert result[0].container_instance_id == container_id1
            assert result[1].container_instance_id == container_id2

    def test_get_containers_by_entity_id_database_error(self) -> None:
        """Test get_containers_by_entity_id handles database errors."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock(side_effect=psycopg2.Error("Database error"))
        mock_cursor.close = Mock()

        entity_id = uuid.uuid4()
        with pytest.raises(DatabaseError, match="Database error retrieving containers"):
            get_containers_by_entity_id(mock_conn, entity_id)


class TestUpdateContainer:
    """Test update_container function."""

    def test_update_container_invalid_lock_state(self) -> None:
        """Test update_container raises ValidationError for invalid lock_state."""
        mock_conn = Mock()
        container_id = uuid.uuid4()

        with pytest.raises(ValidationError, match="Invalid lock_state"):
            update_container(mock_conn, container_id, lock_state="invalid")

    def test_update_container_not_found(self) -> None:
        """Test update_container returns None when container not found."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=None)
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        with patch("server.container_persistence.container_persistence.get_container", return_value=None):
            result = update_container(mock_conn, container_id, lock_state="locked")
            assert result is None

    def test_update_container_with_lock_state(self) -> None:
        """Test update_container successfully updates lock_state."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        with patch("server.container_persistence.container_persistence.get_container") as mock_get:
            mock_container = Mock()
            mock_get.return_value = mock_container
            with patch("server.container_persistence.container_persistence.logger.info") as mock_info:
                result = update_container(mock_conn, container_id, lock_state="locked")
                assert result == mock_container
                # Should log container update
                mock_info.assert_called_once()

    def test_update_container_with_metadata_json(self) -> None:
        """Test update_container successfully updates metadata_json."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        metadata_json = {"key": "value"}
        with patch("server.container_persistence.container_persistence.get_container") as mock_get:
            mock_container = Mock()
            mock_get.return_value = mock_container
            result = update_container(mock_conn, container_id, metadata_json=metadata_json)
            assert result == mock_container

    def test_update_container_with_items_json(self) -> None:
        """Test update_container successfully updates items_json."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        items_json = [{"item_instance_id": str(uuid.uuid4()), "item_id": "item-123"}]
        # Need lock_state or metadata_json to trigger the updates branch and return a row
        with patch("server.container_persistence.container_persistence.get_container") as mock_get:
            mock_container = Mock()
            mock_get.return_value = mock_container
            result = update_container(mock_conn, container_id, items_json=items_json, lock_state="locked")
            assert result == mock_container
            # Should execute clear_container_contents, add_item_to_container, and UPDATE
            assert mock_cursor.execute.call_count >= 3

    def test_update_container_with_items_json_no_item_instance_id(self) -> None:
        """Test update_container skips items without item_instance_id."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        # Items without item_instance_id or item_id should be skipped
        items_json: list[Any] = [{}]  # Empty dict - no item_instance_id or item_id
        # Need lock_state or metadata_json to trigger the updates branch
        with patch("server.container_persistence.container_persistence.get_container") as mock_get:
            mock_container = Mock()
            mock_get.return_value = mock_container
            result = update_container(mock_conn, container_id, items_json=items_json, metadata_json={"key": "value"})
            assert result == mock_container
            # Should execute clear_container_contents and UPDATE, but not add_item_to_container
            assert mock_cursor.execute.call_count >= 2

    def test_update_container_with_multiple_updates(self) -> None:
        """Test update_container with multiple fields updated."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        with patch("server.container_persistence.container_persistence.get_container") as mock_get:
            mock_container = Mock()
            mock_get.return_value = mock_container
            result = update_container(mock_conn, container_id, lock_state="locked", metadata_json={"key": "value"})
            assert result == mock_container

    def test_update_container_with_only_items_json(self) -> None:
        """Test update_container with only items_json (no other updates)."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        # When only items_json is provided, updates list is empty, so row is None
        # But the code path shows: if updates: ... else: row = None
        # So we need to test the case where updates is empty
        mock_cursor.fetchone = Mock(return_value=None)
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        items_json = [{"item_instance_id": str(uuid.uuid4()), "item_id": "item-123"}]
        with patch("server.container_persistence.container_persistence.get_container", return_value=None):
            result = update_container(mock_conn, container_id, items_json=items_json)
            # When only items_json is provided (no lock_state or metadata_json),
            # updates list is empty, so row = None, and function returns None
            assert result is None

    def test_update_container_with_items_json_using_item_id(self) -> None:
        """Test update_container uses item_id when item_instance_id is missing."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        # item_id is used when item_instance_id is missing
        items_json = [{"item_id": "item-123"}]  # No item_instance_id, but has item_id
        with patch("server.container_persistence.container_persistence.get_container") as mock_get:
            mock_container = Mock()
            mock_get.return_value = mock_container
            result = update_container(mock_conn, container_id, items_json=items_json, lock_state="locked")
            assert result == mock_container
            # Should execute add_item_to_container using item_id
            assert mock_cursor.execute.call_count >= 3

    def test_update_container_database_error(self) -> None:
        """Test update_container handles database errors."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock(side_effect=psycopg2.Error("Database error"))
        mock_conn.rollback = Mock()

        container_id = uuid.uuid4()
        with pytest.raises(DatabaseError, match="Database error updating container"):
            update_container(mock_conn, container_id, lock_state="locked")

    def test_update_container_with_no_updates(self) -> None:
        """Test update_container with no updates (only items_json, but no other fields)."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=None)  # No row returned
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        items_json = [{"item_instance_id": str(uuid.uuid4())}]

        result = update_container(mock_conn, container_id, items_json=items_json)
        # When no row is returned and no other updates, should return None
        assert result is None

    def test_update_container_logs_info(self) -> None:
        """Test update_container logs info message when successful."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()

        with patch("server.container_persistence.container_persistence.get_container") as mock_get:
            mock_container = Mock()
            mock_get.return_value = mock_container
            with patch("server.container_persistence.container_persistence.logger.info") as mock_info:
                result = update_container(mock_conn, container_id, lock_state="locked")
                assert result == mock_container
                # Should log container update
                mock_info.assert_called_once()


class TestDeleteContainer:
    """Test delete_container function."""

    def test_delete_container_success(self) -> None:
        """Test delete_container returns True when container deleted."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        with patch("server.container_persistence.container_persistence.logger.info") as mock_info:
            result = delete_container(mock_conn, container_id)
            assert result is True
            # Should log container deletion
            mock_info.assert_called_once()

    def test_delete_container_not_found(self) -> None:
        """Test delete_container returns False when container not found."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.fetchone = Mock(return_value=None)
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        result = delete_container(mock_conn, container_id)
        assert result is False

    def test_delete_container_database_error(self) -> None:
        """Test delete_container handles database errors."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock(side_effect=psycopg2.Error("Database error"))
        mock_conn.rollback = Mock()

        container_id = uuid.uuid4()
        with pytest.raises(DatabaseError, match="Database error deleting container"):
            delete_container(mock_conn, container_id)

    def test_delete_container_logs_info(self) -> None:
        """Test delete_container logs info message when successful."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()

        with patch("server.container_persistence.container_persistence.logger.info") as mock_info:
            result = delete_container(mock_conn, container_id)
            assert result is True
            # Should log container deletion
            mock_info.assert_called_once()
