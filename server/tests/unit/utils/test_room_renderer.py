"""
Unit tests for room rendering utilities.

Tests helpers for formatting room drop information for consistent presentation.
"""

from collections.abc import Mapping

import pytest

from server.utils.room_renderer import (
    DROP_EMPTY_LINE,
    DROP_INTRO_LINE,
    build_room_drop_summary,
    clone_room_drops,
    format_room_drop_lines,
)


def test_format_room_drop_lines_empty_none():
    """Test format_room_drop_lines returns empty line for None."""
    result = format_room_drop_lines(None)
    
    assert result == [DROP_EMPTY_LINE]


def test_format_room_drop_lines_empty_list():
    """Test format_room_drop_lines returns empty line for empty list."""
    result = format_room_drop_lines([])
    
    assert result == [DROP_EMPTY_LINE]


def test_format_room_drop_lines_single_drop():
    """Test format_room_drop_lines formats single drop correctly."""
    drops = [{"item_name": "Ancient Tome", "slot_type": "book", "quantity": 1}]
    result = format_room_drop_lines(drops)
    
    assert len(result) == 2
    assert result[0] == DROP_INTRO_LINE
    assert result[1] == "1. Ancient Tome x1 (book)"


def test_format_room_drop_lines_multiple_drops():
    """Test format_room_drop_lines formats multiple drops correctly."""
    drops = [
        {"item_name": "Ancient Tome", "slot_type": "book", "quantity": 1},
        {"item_name": "Rusty Knife", "slot_type": "weapon", "quantity": 2},
    ]
    result = format_room_drop_lines(drops)
    
    assert len(result) == 3
    assert result[0] == DROP_INTRO_LINE
    assert result[1] == "1. Ancient Tome x1 (book)"
    assert result[2] == "2. Rusty Knife x2 (weapon)"


def test_format_room_drop_lines_uses_item_id_when_no_item_name():
    """Test format_room_drop_lines uses item_id when item_name is missing."""
    drops = [{"item_id": "tome_001", "slot_type": "book", "quantity": 1}]
    result = format_room_drop_lines(drops)
    
    assert result[1] == "1. tome_001 x1 (book)"


def test_format_room_drop_lines_uses_default_when_no_name_or_id():
    """Test format_room_drop_lines uses default when both item_name and item_id are missing."""
    drops = [{"slot_type": "book", "quantity": 1}]
    result = format_room_drop_lines(drops)
    
    assert result[1] == "1. Uncatalogued Relic x1 (book)"


def test_format_room_drop_lines_handles_missing_slot_type():
    """Test format_room_drop_lines handles missing slot_type."""
    drops = [{"item_name": "Ancient Tome", "quantity": 1}]
    result = format_room_drop_lines(drops)
    
    assert result[1] == "1. Ancient Tome x1 (unknown)"


def test_format_room_drop_lines_handles_missing_quantity():
    """Test format_room_drop_lines handles missing quantity."""
    drops = [{"item_name": "Ancient Tome", "slot_type": "book"}]
    result = format_room_drop_lines(drops)
    
    assert result[1] == "1. Ancient Tome x0 (book)"


def test_format_room_drop_lines_handles_invalid_quantity_string():
    """Test format_room_drop_lines handles invalid quantity string."""
    drops = [{"item_name": "Ancient Tome", "slot_type": "book", "quantity": "invalid"}]
    result = format_room_drop_lines(drops)
    
    assert result[1] == "1. Ancient Tome x0 (book)"


def test_format_room_drop_lines_handles_invalid_quantity_type():
    """Test format_room_drop_lines handles invalid quantity type."""
    drops = [{"item_name": "Ancient Tome", "slot_type": "book", "quantity": None}]
    result = format_room_drop_lines(drops)
    
    assert result[1] == "1. Ancient Tome x0 (book)"


def test_format_room_drop_lines_handles_large_quantity():
    """Test format_room_drop_lines handles large quantity."""
    drops = [{"item_name": "Ancient Tome", "slot_type": "book", "quantity": 100}]
    result = format_room_drop_lines(drops)
    
    assert result[1] == "1. Ancient Tome x100 (book)"


def test_build_room_drop_summary_empty():
    """Test build_room_drop_summary returns empty line for empty drops."""
    result = build_room_drop_summary(None)
    
    assert result == DROP_EMPTY_LINE


def test_build_room_drop_summary_single_drop():
    """Test build_room_drop_summary formats single drop correctly."""
    drops = [{"item_name": "Ancient Tome", "slot_type": "book", "quantity": 1}]
    result = build_room_drop_summary(drops)
    
    assert DROP_INTRO_LINE in result
    assert "1. Ancient Tome x1 (book)" in result
    assert "\n" in result


def test_build_room_drop_summary_multiple_drops():
    """Test build_room_drop_summary formats multiple drops correctly."""
    drops = [
        {"item_name": "Ancient Tome", "slot_type": "book", "quantity": 1},
        {"item_name": "Rusty Knife", "slot_type": "weapon", "quantity": 2},
    ]
    result = build_room_drop_summary(drops)
    
    lines = result.split("\n")
    assert len(lines) == 3
    assert lines[0] == DROP_INTRO_LINE
    assert lines[1] == "1. Ancient Tome x1 (book)"
    assert lines[2] == "2. Rusty Knife x2 (weapon)"


def test_clone_room_drops_none():
    """Test clone_room_drops returns empty list for None."""
    result = clone_room_drops(None)
    
    assert result == []


def test_clone_room_drops_empty_list():
    """Test clone_room_drops returns empty list for empty list."""
    result = clone_room_drops([])
    
    assert result == []


def test_clone_room_drops_single_drop():
    """Test clone_room_drops deep copies single drop."""
    original = [{"item_name": "Ancient Tome", "slot_type": "book", "quantity": 1}]
    cloned = clone_room_drops(original)
    
    assert cloned == original
    assert cloned is not original
    assert cloned[0] is not original[0]
    cloned[0]["item_name"] = "Modified"
    assert original[0]["item_name"] == "Ancient Tome"  # Original unchanged


def test_clone_room_drops_multiple_drops():
    """Test clone_room_drops deep copies multiple drops."""
    original = [
        {"item_name": "Ancient Tome", "slot_type": "book", "quantity": 1},
        {"item_name": "Rusty Knife", "slot_type": "weapon", "quantity": 2},
    ]
    cloned = clone_room_drops(original)
    
    assert cloned == original
    assert cloned is not original
    assert cloned[0] is not original[0]
    assert cloned[1] is not original[1]
    cloned[0]["item_name"] = "Modified"
    assert original[0]["item_name"] == "Ancient Tome"  # Original unchanged


def test_clone_room_drops_nested_structure():
    """Test clone_room_drops deep copies nested structures."""
    original = [{"item_name": "Ancient Tome", "metadata": {"author": "Lovecraft", "year": 1928}}]
    cloned = clone_room_drops(original)
    
    assert cloned == original
    cloned[0]["metadata"]["year"] = 2025
    assert original[0]["metadata"]["year"] == 1928  # Original unchanged


def test_clone_room_drops_converts_to_dict():
    """Test clone_room_drops converts mappings to dict."""
    # Use a custom mapping-like object
    class CustomMapping(Mapping):
        def __init__(self, data):
            self._data = data
        
        def __getitem__(self, key):
            return self._data[key]
        
        def __iter__(self):
            return iter(self._data)
        
        def __len__(self):
            return len(self._data)
    
    original = [CustomMapping({"item_name": "Ancient Tome", "slot_type": "book", "quantity": 1})]
    cloned = clone_room_drops(original)
    
    assert isinstance(cloned[0], dict)
    assert cloned[0] == {"item_name": "Ancient Tome", "slot_type": "book", "quantity": 1}
