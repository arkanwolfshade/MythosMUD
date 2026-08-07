"""
Unit tests for container_persistence helpers and fetch_container_items.

Tests the container persistence functions from server.container_persistence.container_persistence.
"""

# pyright: reportAny=false
# MagicMock attribute chains are Any in typeshed; suppressing matches test_container_persistence_extended_*.
# Typed locals alone cannot make mock_conn.cursor.execute... reportAny-clean without cast noise.

import json
from unittest.mock import MagicMock, patch
from uuid import uuid4

import pytest

from server.container_persistence.container_persistence import (
    ContainerData,
    fetch_container_items,
    parse_jsonb_column,
)


def test_parse_jsonb_column_none():
    """Test parsing None JSONB column."""
    result = parse_jsonb_column(None, {})
    assert result == {}


def test_parse_jsonb_column_string():
    """Test parsing string JSONB column."""
    data = {"key": "value"}
    result = parse_jsonb_column(json.dumps(data), {})
    assert result == data


def test_parse_jsonb_column_dict():
    """Test parsing dict JSONB column."""
    data = {"key": "value"}
    result = parse_jsonb_column(data, {})
    assert result == data


def test_parse_jsonb_column_empty_string():
    """Test parsing empty string JSONB column."""
    result = parse_jsonb_column("", {})
    assert result == {}


def test_parse_jsonb_column_list():
    """Test parsing list JSONB column."""
    data = [1, 2, 3]
    result = parse_jsonb_column(data, [])
    assert result == data


def test_parse_jsonb_column_invalid_json():
    """Test parsing invalid JSON string."""
    with pytest.raises(json.JSONDecodeError):
        _ = parse_jsonb_column("{invalid json}", {})


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
    """Test fetch_container_items with no items."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = []
    mock_cursor.close = MagicMock()

    container_id = uuid4()
    result = fetch_container_items(mock_conn, container_id)
    assert result == []
    mock_cursor.execute.assert_called_once()
    mock_cursor.close.assert_called_once()


def test_fetch_container_items_with_items():
    """Test fetch_container_items with items."""
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
    result = fetch_container_items(mock_conn, container_id)
    assert len(result) == 1
    assert result[0]["item_name"] == "Test Item"
    assert result[0]["quantity"] == 1


def test_fetch_container_items_missing_item_instance_id():
    """Test fetch_container_items skips rows with missing item_instance_id."""
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
    with patch("server.container_persistence.container_helpers.logger") as mock_logger:
        result = fetch_container_items(mock_conn, container_id)
        assert result == []
        mock_logger.warning.assert_called()


def test_fetch_container_items_non_dict_row():
    """Test fetch_container_items handles non-dictionary rows."""
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
    with patch("server.container_persistence.container_helpers.logger") as mock_logger:
        result = fetch_container_items(mock_conn, container_id)

    # Should skip non-dict row, keep dict row
    assert len(result) == 1
    mock_logger.warning.assert_called()


def test_fetch_container_items_string_metadata():
    """Test fetch_container_items parses string metadata."""
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
    result = fetch_container_items(mock_conn, container_id)

    assert result[0]["metadata"] == {"key": "value"}


def test_fetch_container_items_invalid_json_metadata():
    """Test fetch_container_items handles invalid JSON metadata."""
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
    result = fetch_container_items(mock_conn, container_id)

    # Should default to {} on JSON parse error
    assert result[0]["metadata"] == {}


def test_fetch_container_items_non_dict_metadata():
    """Test fetch_container_items handles non-dict metadata."""
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
    result = fetch_container_items(mock_conn, container_id)

    # Should default to {} for non-dict metadata
    assert result[0]["metadata"] == {}


def test_fetch_container_items_missing_fields():
    """Test fetch_container_items handles missing optional fields."""
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
    result = fetch_container_items(mock_conn, container_id)

    assert len(result) == 1
    assert result[0]["item_id"] is None
    assert result[0]["item_name"] == "Unknown Item"
    assert result[0]["quantity"] == 1
    assert result[0]["condition"] == "pristine"
    assert result[0]["position"] == 0


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
