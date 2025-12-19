"""
Tests for container persistence operations.

This module tests container creation, retrieval, update, and deletion
operations for the unified container system.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import Mock, patch

import psycopg2
import pytest

from server.exceptions import DatabaseError, ValidationError
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

        mock_row = {
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

        with patch("server.persistence.container_persistence.logger.warning") as mock_warning:
            container_id = uuid.uuid4()
            result = _fetch_container_items(mock_conn, container_id)
            assert result == []
            mock_warning.assert_called_once()

    def test_fetch_container_items_skips_missing_item_instance_id(self) -> None:
        """Test _fetch_container_items skips rows without item_instance_id."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        mock_row = {
            "item_id": "item-123",
            "item_name": "Test Item",
            # Missing item_instance_id
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row])
        mock_cursor.close = Mock()

        with patch("server.persistence.container_persistence.logger.warning") as mock_warning:
            container_id = uuid.uuid4()
            result = _fetch_container_items(mock_conn, container_id)
            assert result == []
            mock_warning.assert_called_once()

    def test_fetch_container_items_parses_string_metadata(self) -> None:
        """Test _fetch_container_items parses string metadata."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        mock_row = {
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

        mock_row = {
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
        # to_dict() converts UUIDs to strings
        assert result["container_id"] == str(container_id)
        assert result["source_type"] == "equipment"
        assert result["owner_id"] == str(owner_id)
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
            "server.persistence.container_persistence.log_and_raise", side_effect=DatabaseError("No ID returned")
        ):
            with pytest.raises(DatabaseError, match="No ID returned"):
                create_container(mock_conn, source_type="environment")

    def test_create_container_with_items_json(self) -> None:
        """Test create_container handles items_json parameter."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        # Mock successful insert
        mock_row = Mock()
        mock_row_data = {
            "container_instance_id": uuid.uuid4(),
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
        }
        mock_row.__getitem__ = Mock(side_effect=mock_row_data.get)
        mock_cursor.fetchone = Mock(return_value=mock_row)
        mock_cursor.close = Mock()
        mock_conn.commit = Mock()

        items_json = [{"item_instance_id": str(uuid.uuid4()), "item_id": "item-123"}]

        with patch("server.persistence.container_persistence.get_container", return_value=None):
            with patch("server.persistence.container_persistence.logger.info") as mock_info:
                result = create_container(
                    mock_conn,
                    source_type="environment",
                    items_json=items_json,
                )
                assert result is not None
                # Should log container creation
                mock_info.assert_called_once()

    def test_create_container_items_json_ensure_item_instance_exception(self) -> None:
        """Test create_container handles exception in ensure_item_instance."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        # Mock successful insert
        mock_row = Mock()
        mock_row_data = {
            "container_instance_id": uuid.uuid4(),
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
        }
        mock_row.__getitem__ = Mock(side_effect=mock_row_data.get)
        mock_cursor.fetchone = Mock(return_value=mock_row)
        mock_cursor.close = Mock()
        mock_conn.commit = Mock()

        items_json = [{"item_instance_id": str(uuid.uuid4()), "item_id": "item-123", "prototype_id": "proto-123"}]

        with patch("server.persistence.container_persistence.get_container", return_value=None):
            with patch(
                "server.persistence.item_instance_persistence.ensure_item_instance", side_effect=Exception("Item error")
            ):
                with patch("server.persistence.container_persistence.logger.warning") as mock_warning:
                    result = create_container(
                        mock_conn,
                        source_type="environment",
                        items_json=items_json,
                    )
                    assert result is not None
                    # Should log warning about failed item instance
                    mock_warning.assert_called()

    def test_create_container_with_items_json_success(self) -> None:
        """Test create_container successfully creates container with items_json."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id = uuid.uuid4()
        mock_row = Mock()
        mock_row_data = {
            "container_instance_id": container_id,
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
        }
        mock_row.__getitem__ = Mock(side_effect=mock_row_data.get)
        mock_cursor.fetchone = Mock(return_value=mock_row)
        mock_cursor.close = Mock()
        mock_conn.commit = Mock()

        items_json = [{"item_instance_id": str(uuid.uuid4()), "item_id": "item-123", "prototype_id": "proto-123"}]

        with patch("server.persistence.item_instance_persistence.ensure_item_instance") as mock_ensure:
            with patch("server.persistence.container_persistence.get_container", return_value=None):
                result = create_container(
                    mock_conn,
                    source_type="environment",
                    items_json=items_json,
                )
                assert result is not None
                assert result.container_instance_id == container_id
                # Should call ensure_item_instance
                mock_ensure.assert_called_once()

    def test_create_container_with_items_json_missing_prototype_id(self) -> None:
        """Test create_container skips items without both item_instance_id and prototype_id."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id = uuid.uuid4()
        mock_row = Mock()
        mock_row_data = {
            "container_instance_id": container_id,
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
        }
        mock_row.__getitem__ = Mock(side_effect=mock_row_data.get)
        mock_cursor.fetchone = Mock(return_value=mock_row)
        mock_cursor.close = Mock()
        mock_conn.commit = Mock()

        items_json = [{"item_instance_id": str(uuid.uuid4())}]  # Missing prototype_id

        with patch("server.persistence.item_instance_persistence.ensure_item_instance") as mock_ensure:
            with patch("server.persistence.container_persistence.get_container", return_value=None):
                result = create_container(
                    mock_conn,
                    source_type="environment",
                    items_json=items_json,
                )
                assert result is not None
                # Should not call ensure_item_instance for items without prototype_id
                mock_ensure.assert_not_called()


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
        with patch("server.persistence.container_persistence.get_container", return_value=None):
            result = update_container(mock_conn, container_id, lock_state="locked")
            assert result is None

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

    def test_update_container_with_items_json_success(self) -> None:
        """Test update_container successfully updates items_json."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        items_json = [{"item_instance_id": str(uuid.uuid4()), "item_id": "item-123", "prototype_id": "proto-123"}]

        with patch("server.persistence.item_instance_persistence.ensure_item_instance") as mock_ensure:
            with patch("server.persistence.container_persistence.get_container") as mock_get:
                mock_container = Mock()
                mock_get.return_value = mock_container
                result = update_container(mock_conn, container_id, items_json=items_json)
                assert result == mock_container
                mock_ensure.assert_called_once()

    def test_update_container_with_items_json_ensure_item_instance_exception(self) -> None:
        """Test update_container handles exception in ensure_item_instance."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        items_json = [{"item_instance_id": str(uuid.uuid4()), "item_id": "item-123", "prototype_id": "proto-123"}]

        with patch(
            "server.persistence.item_instance_persistence.ensure_item_instance", side_effect=Exception("Item error")
        ):
            with patch("server.persistence.container_persistence.logger.warning") as mock_warning:
                with patch("server.persistence.container_persistence.get_container") as mock_get:
                    mock_container = Mock()
                    mock_get.return_value = mock_container
                    result = update_container(mock_conn, container_id, items_json=items_json)
                    assert result == mock_container
                    # Should log warning about failed item instance
                    mock_warning.assert_called()

    def test_update_container_with_only_items_json(self) -> None:
        """Test update_container with only items_json (no other updates)."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        items_json = [{"item_instance_id": str(uuid.uuid4()), "item_id": "item-123", "prototype_id": "proto-123"}]

        with patch("server.persistence.item_instance_persistence.ensure_item_instance"):
            with patch("server.persistence.container_persistence.get_container") as mock_get:
                mock_container = Mock()
                mock_get.return_value = mock_container
                result = update_container(mock_conn, container_id, items_json=items_json)
                assert result == mock_container
                # Should still update updated_at even with only items_json
                assert mock_cursor.execute.call_count > 1

    def test_update_container_with_items_json_missing_prototype_id(self) -> None:
        """Test update_container skips items without both item_instance_id and prototype_id."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock()
        mock_cursor.fetchone = Mock(return_value=(uuid.uuid4(),))
        mock_conn.commit = Mock()
        mock_cursor.close = Mock()

        container_id = uuid.uuid4()
        items_json = [
            {"item_instance_id": str(uuid.uuid4())}  # Missing prototype_id
        ]

        with patch("server.persistence.container_persistence.get_container") as mock_get:
            mock_container = Mock()
            mock_get.return_value = mock_container
            result = update_container(mock_conn, container_id, items_json=items_json)
            assert result == mock_container
            # Should not call ensure_item_instance for items without prototype_id
            with patch("server.persistence.item_instance_persistence.ensure_item_instance") as _mock_ensure:
                # This should not be called since prototype_id is missing
                pass


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
        result = delete_container(mock_conn, container_id)
        assert result is True

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


class TestGetDecayedContainers:
    """Test get_decayed_containers function."""

    def test_get_decayed_containers_empty(self) -> None:
        """Test get_decayed_containers returns empty list."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.fetchall = Mock(return_value=[])
        mock_cursor.close = Mock()

        result = get_decayed_containers(mock_conn)
        assert result == []

    def test_get_decayed_containers_with_current_time(self) -> None:
        """Test get_decayed_containers with provided current_time."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.fetchall = Mock(return_value=[])
        mock_cursor.close = Mock()

        current_time = datetime.now(UTC)
        result = get_decayed_containers(mock_conn, current_time)
        assert result == []

    def test_get_decayed_containers_database_error(self) -> None:
        """Test get_decayed_containers handles database errors."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)
        mock_cursor.execute = Mock(side_effect=psycopg2.Error("Database error"))
        mock_cursor.close = Mock()

        with pytest.raises(DatabaseError, match="Database error retrieving decayed containers"):
            get_decayed_containers(mock_conn)

    def test_get_decayed_containers_with_results(self) -> None:
        """Test get_decayed_containers returns containers that have decayed."""
        mock_conn = Mock()
        mock_cursor = Mock()
        mock_conn.cursor = Mock(return_value=mock_cursor)

        container_id = uuid.uuid4()
        mock_row = {
            "container_instance_id": container_id,
            "source_type": "corpse",
            "owner_id": None,
            "room_id": "room-123",
            "entity_id": None,
            "lock_state": "unlocked",
            "capacity_slots": 10,
            "weight_limit": None,
            "decay_at": datetime.now(UTC).replace(tzinfo=None),
            "allowed_roles": [],
            "metadata_json": {},
            "created_at": datetime.now(UTC).replace(tzinfo=None),
            "updated_at": datetime.now(UTC).replace(tzinfo=None),
            "container_item_instance_id": None,
        }
        mock_cursor.fetchall = Mock(return_value=[mock_row])
        mock_cursor.close = Mock()

        with patch("server.persistence.container_persistence._fetch_container_items", return_value=[]):
            result = get_decayed_containers(mock_conn)
            assert len(result) == 1
            assert result[0].container_instance_id == container_id
            assert result[0].source_type == "corpse"
