"""
Unit tests for look container helper functions.

Tests the helper functions in look_container.py.
"""

import pytest

from server.commands.look_container import _find_container_in_room, _find_container_wearable


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
