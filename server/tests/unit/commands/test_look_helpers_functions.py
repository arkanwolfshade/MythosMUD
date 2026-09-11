"""
Unit tests for look_helpers functions.

Tests the helper functions in look_helpers.py module.
"""

from unittest.mock import MagicMock

from server.commands.look_helpers import (
    _get_corruption_label,
    _get_corruption_prose,
    _get_health_label,
    _get_lucidity_label,
    _get_visible_equipment,
    _is_direction,
    _parse_instance_number,
)


def test_parse_instance_number_hyphen_syntax():
    """Test _parse_instance_number() parses hyphen syntax."""
    result = _parse_instance_number("backpack-2")

    assert result == ("backpack", 2)


def test_parse_instance_number_space_syntax():
    """Test _parse_instance_number() parses space syntax."""
    result = _parse_instance_number("backpack 2")

    assert result == ("backpack", 2)


def test_parse_instance_number_no_instance():
    """Test _parse_instance_number() returns None when no instance number."""
    result = _parse_instance_number("backpack")

    assert result == ("backpack", None)


def test_get_health_label_healthy():
    """Test _get_health_label() returns 'healthy' for high health."""
    stats = {"current_dp": 18, "max_dp": 20, "constitution": 50, "size": 50}

    result = _get_health_label(stats)

    assert result == "healthy"


def test_get_health_label_wounded():
    """Test _get_health_label() returns 'wounded' for medium health."""
    stats = {"current_dp": 10, "max_dp": 20, "constitution": 50, "size": 50}

    result = _get_health_label(stats)

    assert result == "wounded"


def test_get_health_label_critical():
    """Test _get_health_label() returns 'critical' for low health."""
    stats = {"current_dp": 3, "max_dp": 20, "constitution": 50, "size": 50}

    result = _get_health_label(stats)

    assert result == "critical"


def test_get_health_label_mortally_wounded():
    """Test _get_health_label() returns 'mortally wounded' for negative DP."""
    stats = {"current_dp": -5, "max_dp": 20, "constitution": 50, "size": 50}

    result = _get_health_label(stats)

    assert result == "mortally wounded"


def test_get_corruption_label_all_tiers():
    """#815: every tier boundary maps to its own label word, both edges."""
    cases = [
        (0, "untainted"),
        (1, "faintly tainted"),
        (24, "faintly tainted"),
        (25, "marked"),
        (49, "marked"),
        (50, "defiled"),
        (74, "defiled"),
        (75, "warped"),
        (100, "warped"),
    ]
    for corruption, expected in cases:
        assert _get_corruption_label({"corruption": corruption}) == expected


def test_get_corruption_label_defaults_to_untainted_when_missing():
    """No 'corruption' key at all -- same fail-safe default as the tier cache miss."""
    assert _get_corruption_label({}) == "untainted"


def test_get_corruption_prose_none_below_marked():
    """#815: the permanent 'touched' scar gets a label but no atmosphere -- undramatic on purpose."""
    assert _get_corruption_prose({"corruption": 0}) is None
    assert _get_corruption_prose({"corruption": 24}) is None


def test_get_corruption_prose_present_from_marked():
    assert _get_corruption_prose({"corruption": 25}) is not None
    assert _get_corruption_prose({"corruption": 74}) is not None
    assert _get_corruption_prose({"corruption": 100}) is not None


def test_get_lucidity_label_lucid():
    """Test _get_lucidity_label() returns 'lucid' for high lucidity."""
    stats = {"lucidity": 80, "corruption": 0}

    result = _get_lucidity_label(stats)

    assert result == "lucid"


def test_get_lucidity_label_disturbed_medium():
    """Test _get_lucidity_label() returns 'disturbed' for medium lucidity."""
    stats = {"lucidity": 60, "max_lucidity": 100}

    result = _get_lucidity_label(stats)

    assert result == "disturbed"


def test_get_lucidity_label_unstable():
    """Test _get_lucidity_label() returns 'unstable' for low lucidity."""
    stats = {"lucidity": 20, "max_lucidity": 100}

    result = _get_lucidity_label(stats)

    assert result == "unstable"


def test_get_lucidity_label_mad():
    """Test _get_lucidity_label() returns 'mad' for very low lucidity."""
    stats = {"lucidity": -20, "max_lucidity": 100}

    result = _get_lucidity_label(stats)

    assert result == "mad"


def test_get_lucidity_label_mad_negative():
    """Test _get_lucidity_label() returns 'mad' for negative lucidity."""
    stats = {"lucidity": -80, "max_lucidity": 100}

    result = _get_lucidity_label(stats)

    assert result == "mad"


def test_get_visible_equipment():
    """Test _get_visible_equipment() returns visible equipment slots."""
    player = MagicMock()
    player.get_equipped_items.return_value = {
        "main_hand": {"item_name": "Sword"},
        "head": {"item_name": "Helmet"},
        "backpack": {"item_name": "Backpack"},  # Hidden slot
    }

    result = _get_visible_equipment(player)

    assert "main_hand" in result
    assert "head" in result
    assert "backpack" not in result  # Hidden slot filtered out


def test_get_visible_equipment_no_equipment():
    """Test _get_visible_equipment() returns empty dict when no equipment."""
    player = MagicMock()
    player.get_equipped_items.return_value = {}

    result = _get_visible_equipment(player)

    assert result == {}


def test_is_direction():
    """Test _is_direction() returns True for valid directions."""
    assert _is_direction("north") is True
    assert _is_direction("south") is True
    assert _is_direction("east") is True
    assert _is_direction("west") is True
    assert _is_direction("up") is True
    assert _is_direction("down") is True


def test_is_direction_false():
    """Test _is_direction() returns False for invalid directions."""
    assert _is_direction("invalid") is False
    assert _is_direction("northeast") is False
    assert _is_direction("") is False
