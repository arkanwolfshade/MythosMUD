"""Unit tests for container persistence: JSONB parsing, item fetch, and ContainerData.

Split from test_container_persistence_extended for Lizard file-size limits.
"""

# pyright: reportPrivateUsage=false, reportAny=false, reportUnusedCallResult=false, reportUnknownVariableType=false

import json
import uuid
from datetime import UTC, datetime
from unittest.mock import MagicMock

from server.persistence import ContainerData
from server.persistence.container_data import ContainerDataCore, ContainerDataExtras
from server.persistence.container_persistence import (
    _fetch_container_items,
    _parse_jsonb_column,
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
        ContainerDataCore(
            container_instance_id=container_id,
            source_type="environment",
            owner_id=uuid.uuid4(),
            room_id="test_room",
        ),
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
        ContainerDataCore(
            container_instance_id=container_id,
            source_type="equipment",
            owner_id=owner_id,
            entity_id=entity_id,
            lock_state="locked",
            capacity_slots=10,
        ),
        ContainerDataExtras(
            weight_limit=50,
            decay_at=decay_at,
            allowed_roles=["admin"],
            items_json=[{"item_id": "test"}],
            metadata_json={"key": "value"},
            created_at=created_at,
            updated_at=updated_at,
        ),
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
        ContainerDataCore(
            container_instance_id=container_id,
            source_type="environment",
            owner_id=None,
            entity_id=None,
        ),
        ContainerDataExtras(
            decay_at=None,
            created_at=None,
            updated_at=None,
        ),
    )

    result = container.to_dict()

    assert result["owner_id"] is None
    assert result["entity_id"] is None
    assert result["decay_at"] is None
    assert result["created_at"] is None
    assert result["updated_at"] is None
