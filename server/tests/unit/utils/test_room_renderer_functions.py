"""
Unit tests for room_renderer utility functions.

Tests the utility functions in room_renderer.py module.
"""

from server.utils.room_renderer import (
    build_room_drop_summary,
    clone_room_drops,
    format_room_drop_lines,
)


def test_format_room_drop_lines():
    """Test format_room_drop_lines() formats room drops."""
    drops = [
        {"item_name": "Sword", "slot_type": "weapon", "quantity": 1},
        {"item_name": "Arrow", "slot_type": "ammo", "quantity": 10},
    ]

    result = format_room_drop_lines(drops)

    assert len(result) == 3
    assert "Scattered upon the floor" in result[0]
    assert "1. Sword x1" in result[1]
    assert "2. Arrow x10" in result[2]


def test_format_room_drop_lines_empty():
    """Test format_room_drop_lines() returns empty message for empty drops."""
    drops = []

    result = format_room_drop_lines(drops)

    assert len(result) == 1
    assert "no abandoned curios" in result[0].lower()


def test_format_room_drop_lines_none():
    """Test format_room_drop_lines() handles None."""
    result = format_room_drop_lines(None)

    assert len(result) == 1
    assert "no abandoned curios" in result[0].lower()


def test_format_room_drop_lines_fallback_name():
    """Test format_room_drop_lines() uses fallback for missing item_name."""
    drops = [
        {"item_id": "item_001", "slot_type": "weapon", "quantity": 1},
    ]

    result = format_room_drop_lines(drops)

    assert "item_001" in result[1] or "Uncatalogued Relic" in result[1]


def test_build_room_drop_summary():
    """Test build_room_drop_summary() returns newline-separated summary."""
    drops = [
        {"item_name": "Sword", "slot_type": "weapon", "quantity": 1},
    ]

    result = build_room_drop_summary(drops)

    assert isinstance(result, str)
    assert "\n" in result
    assert "Sword" in result


def test_build_room_drop_summary_empty():
    """Test build_room_drop_summary() handles empty drops."""
    result = build_room_drop_summary([])

    assert "no abandoned curios" in result.lower()


def test_clone_room_drops():
    """Test clone_room_drops() creates deep copy."""
    drops = [
        {"item_name": "Sword", "quantity": 1},
    ]

    result = clone_room_drops(drops)

    assert result == drops
    assert result is not drops  # Different object
    assert result[0] is not drops[0]  # Deep copy


def test_clone_room_drops_empty():
    """Test clone_room_drops() returns empty list for empty drops."""
    result = clone_room_drops([])

    assert result == []


def test_clone_room_drops_none():
    """Test clone_room_drops() returns empty list for None."""
    result = clone_room_drops(None)

    assert result == []
