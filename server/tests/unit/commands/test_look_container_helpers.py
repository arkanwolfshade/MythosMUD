"""
Unit tests for look container helper functions.

Tests the helper functions in look_container.py.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.look_container import (
    _extract_container_metadata,
    _find_container_in_room,
    _find_container_via_inner_container,
    _find_container_wearable,
    _format_container_contents,
    _format_container_display,
    _get_container_data_from_component,
    _get_container_description,
    _matches_item_instance_id,
    _matches_name_or_slot,
)


def test_find_container_in_room_found():
    """Test _find_container_in_room() finds container by name."""
    containers = [
        {"container_id": "container_001", "metadata": {"name": "chest"}},
        {"container_id": "container_002", "metadata": {"name": "barrel"}},
    ]
    result = _find_container_in_room(containers, "chest")
    assert result is not None
    assert result["container_id"] == "container_001"


def test_find_container_in_room_not_found():
    """Test _find_container_in_room() returns None when container not found."""
    containers = [{"container_id": "container_001", "metadata": {"name": "chest"}}]
    result = _find_container_in_room(containers, "bag")
    assert result is None


def test_find_container_in_room_instance_number():
    """Test _find_container_in_room() with instance number."""
    containers = [
        {"container_id": "container_001", "metadata": {"name": "chest"}},
        {"container_id": "container_002", "metadata": {"name": "chest"}},
    ]
    result = _find_container_in_room(containers, "chest", instance_number=2)
    assert result is not None
    assert result["container_id"] == "container_002"


def test_find_container_wearable_found():
    """Test _find_container_wearable() finds wearable container."""
    equipped = {
        "back": {"item_name": "backpack", "item_id": "item_001", "inner_container": True},
        "weapon": {"item_name": "sword", "item_id": "item_002"},
    }
    result = _find_container_wearable(equipped, "backpack")
    assert result is not None
    assert result[0] == "back"
    assert result[1]["item_name"] == "backpack"


def test_find_container_wearable_not_found():
    """Test _find_container_wearable() returns None when container not found."""
    equipped = {"weapon": {"item_name": "sword", "item_id": "item_001"}}
    result = _find_container_wearable(equipped, "backpack")
    assert result is None


def test_find_container_in_room_empty():
    """Test _find_container_in_room() with empty list."""
    result = _find_container_in_room([], "backpack")
    assert result is None


def test_find_container_in_room_no_match():
    """Test _find_container_in_room() with no matching containers."""
    containers = [{"container_id": "container_001", "metadata": {"name": "Chest"}}]
    result = _find_container_in_room(containers, "backpack")
    assert result is None


def test_find_container_in_room_multiple_matches():
    """Test _find_container_in_room() with multiple matches (ambiguous)."""
    containers = [
        {"container_id": "container_001", "metadata": {"name": "Backpack"}},
        {"container_id": "container_002", "metadata": {"name": "Large Backpack"}},
    ]
    result = _find_container_in_room(containers, "backpack")
    assert result is None  # Ambiguous


def test_find_container_in_room_with_instance_number():
    """Test _find_container_in_room() with instance number."""
    containers = [
        {"container_id": "container_001", "metadata": {"name": "Backpack"}},
        {"container_id": "container_002", "metadata": {"name": "Large Backpack"}},
    ]
    result = _find_container_in_room(containers, "backpack", instance_number=1)
    assert result is not None
    assert result["container_id"] == "container_001"


def test_find_container_in_room_instance_number_out_of_range():
    """Test _find_container_in_room() with instance number out of range."""
    containers = [{"container_id": "container_001", "metadata": {"name": "Backpack"}}]
    result = _find_container_in_room(containers, "backpack", instance_number=5)
    assert result is None


def test_find_container_in_room_instance_number_zero():
    """Test _find_container_in_room() with instance number zero."""
    containers = [{"container_id": "container_001", "metadata": {"name": "Backpack"}}]
    result = _find_container_in_room(containers, "backpack", instance_number=0)
    assert result is None


def test_find_container_wearable_empty():
    """Test _find_container_wearable() with empty dict."""
    result = _find_container_wearable({}, "backpack")
    assert result is None


def test_find_container_wearable_no_match():
    """Test _find_container_wearable() with no matching containers."""
    equipped = {"head": {"item_name": "Helmet", "item_id": "helmet_001"}}
    result = _find_container_wearable(equipped, "backpack")
    assert result is None


def test_find_container_wearable_multiple_matches():
    """Test _find_container_wearable() with multiple matches (ambiguous)."""
    equipped = {
        "left_hand": {"item_name": "Backpack", "item_id": "backpack_001", "inner_container": "container_001"},
        "right_hand": {"item_name": "Large Backpack", "item_id": "backpack_002", "inner_container": "container_002"},
    }
    result = _find_container_wearable(equipped, "backpack")
    assert result is None  # Ambiguous


def test_find_container_wearable_with_instance_number():
    """Test _find_container_wearable() with instance number."""
    equipped = {
        "left_hand": {"item_name": "Backpack", "item_id": "backpack_001", "inner_container": "container_001"},
        "right_hand": {"item_name": "Large Backpack", "item_id": "backpack_002", "inner_container": "container_002"},
    }
    result = _find_container_wearable(equipped, "backpack", instance_number=2)
    assert result is not None
    assert result[0] == "right_hand"
    assert result[1]["item_name"] == "Large Backpack"


def test_find_container_wearable_instance_number_out_of_range():
    """Test _find_container_wearable() with instance number out of range."""
    equipped = {"back": {"item_name": "Backpack", "item_id": "backpack_001", "inner_container": "container_001"}}
    result = _find_container_wearable(equipped, "backpack", instance_number=5)
    assert result is None


@pytest.mark.asyncio
async def test_find_container_via_inner_container_no_inner_container():
    """Test _find_container_via_inner_container() when item has no inner_container."""
    item = {"item_name": "Sword", "item_id": "sword_001"}
    mock_persistence = MagicMock()
    result = await _find_container_via_inner_container(item, mock_persistence)
    assert result is None


@pytest.mark.asyncio
async def test_find_container_via_inner_container_invalid_uuid():
    """Test _find_container_via_inner_container() with invalid UUID."""
    item = {"item_name": "Backpack", "inner_container": "invalid_uuid"}
    mock_persistence = MagicMock()
    result = await _find_container_via_inner_container(item, mock_persistence)
    assert result is None


@pytest.mark.asyncio
async def test_find_container_via_inner_container_no_get_container():
    """Test _find_container_via_inner_container() when persistence has no get_container."""
    item = {"item_name": "Backpack", "inner_container": str(uuid.uuid4())}
    mock_persistence = MagicMock()
    del mock_persistence.get_container
    result = await _find_container_via_inner_container(item, mock_persistence)
    assert result is None


def test_matches_item_instance_id_true():
    """Test _matches_item_instance_id() returns True when IDs match."""
    result = _matches_item_instance_id("item_001", "item_001")
    assert result is True


def test_matches_item_instance_id_false():
    """Test _matches_item_instance_id() returns False when IDs don't match."""
    result = _matches_item_instance_id("item_001", "item_002")
    assert result is False


def test_matches_item_instance_id_none():
    """Test _matches_item_instance_id() returns False when either ID is None."""
    # Function checks: item_instance_id and container_item_instance_id and str(item_instance_id) == str(container_item_instance_id)
    # When either is None, the 'and' short-circuits and returns None (falsy)
    result = _matches_item_instance_id(None, "item_001")
    assert not result  # Should be falsy (False or None)
    result = _matches_item_instance_id("item_001", None)
    assert not result  # Should be falsy (False or None)


def test_matches_name_or_slot_slot_match():
    """Test _matches_name_or_slot() returns True for slot match."""
    result = _matches_name_or_slot("back", "Backpack", "back", "backpack")
    assert result is True


def test_matches_name_or_slot_name_match():
    """Test _matches_name_or_slot() returns True for name match."""
    result = _matches_name_or_slot("back", "Backpack", "back", "pack")
    assert result is True


def test_matches_name_or_slot_no_match():
    """Test _matches_name_or_slot() returns False when no match."""
    result = _matches_name_or_slot("head", "Helmet", "back", "backpack")
    assert result is False


@pytest.mark.asyncio
async def test_get_container_data_from_component_no_container_id():
    """Test _get_container_data_from_component() when component has no container_id."""
    mock_component = MagicMock()
    mock_component.container_id = None
    mock_persistence = MagicMock()
    result = await _get_container_data_from_component(mock_component, mock_persistence)
    assert result is None


@pytest.mark.asyncio
async def test_get_container_data_from_component_no_get_container():
    """Test _get_container_data_from_component() when persistence has no get_container."""
    mock_component = MagicMock()
    mock_component.container_id = uuid.uuid4()
    mock_persistence = MagicMock()
    del mock_persistence.get_container
    result = await _get_container_data_from_component(mock_component, mock_persistence)
    assert result is None


def test_extract_container_metadata_no_metadata():
    """Test _extract_container_metadata() when component has no metadata."""
    mock_component = MagicMock()
    del mock_component.metadata
    result = _extract_container_metadata(mock_component)
    assert isinstance(result, dict)
    assert "item_name" in result
    assert "slot" in result


def test_format_container_contents_empty():
    """Test _format_container_contents() with empty list."""
    result = _format_container_contents([])
    assert len(result) == 1
    assert "(empty)" in result[0]


def test_format_container_contents_with_quantity():
    """Test _format_container_contents() with items having quantity."""
    items = [
        {"item_name": "Potion", "quantity": 5},
        {"item_name": "Scroll", "quantity": 1},
    ]
    result = _format_container_contents(items)
    assert len(result) == 2
    assert "Potion x5" in result[0]
    assert "Scroll" in result[1]  # No quantity shown for 1


def test_format_container_display_locked():
    """Test _format_container_display() with locked container."""
    container = {
        "container_id": uuid.uuid4(),
        "metadata": {"name": "Chest"},
        "items": [],
        "capacity_slots": 10,
        "lock_state": "locked",
    }
    result = _format_container_display(container, None, {})
    assert "Locked" in result


def test_format_container_display_sealed():
    """Test _format_container_display() with sealed container."""
    container = {
        "container_id": uuid.uuid4(),
        "metadata": {"name": "Chest"},
        "items": [],
        "capacity_slots": 10,
        "lock_state": "sealed",
    }
    result = _format_container_display(container, None, {})
    assert "Sealed" in result


def test_format_container_display_with_look_in():
    """Test _format_container_display() with look_in flag."""
    container = {
        "container_id": str(uuid.uuid4()),
        "metadata": {"name": "Chest"},
        "items": [{"item_name": "Potion", "quantity": 1}],
        "capacity_slots": 10,
        "lock_state": "unlocked",
    }
    command_data = {"look_in": True}
    result = _format_container_display(container, None, command_data)
    assert "Contents:" in result
    assert "Potion" in result


def test_format_container_display_with_target_type_container():
    """Test _format_container_display() with target_type container."""
    container = {
        "container_id": str(uuid.uuid4()),
        "metadata": {"name": "Chest"},
        "items": [{"item_name": "Potion", "quantity": 1}],
        "capacity_slots": 10,
        "lock_state": "unlocked",
    }
    command_data = {"target_type": "container"}
    result = _format_container_display(container, None, command_data)
    assert "Contents:" in result
    assert "Potion" in result


