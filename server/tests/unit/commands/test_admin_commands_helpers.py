"""
Unit tests for admin command helper functions.

Tests utility functions in admin_commands.py that don't require complex dependencies.
"""

from unittest.mock import MagicMock

import pytest

from server.commands.admin_commands import DIRECTION_OPPOSITES, create_teleport_effect_message


def test_direction_opposites_complete():
    """Test that DIRECTION_OPPOSITES contains all expected directions."""
    expected_directions = {
        "north",
        "south",
        "east",
        "west",
        "up",
        "down",
        "northeast",
        "southwest",
        "northwest",
        "southeast",
    }
    assert set(DIRECTION_OPPOSITES.keys()) == expected_directions


def test_direction_opposites_bidirectional():
    """Test that direction opposites are bidirectional."""
    for direction, opposite in DIRECTION_OPPOSITES.items():
        assert DIRECTION_OPPOSITES[opposite] == direction, f"{direction} -> {opposite} should be reversible"


def test_direction_opposites_values():
    """Test specific direction opposite values."""
    assert DIRECTION_OPPOSITES["north"] == "south"
    assert DIRECTION_OPPOSITES["south"] == "north"
    assert DIRECTION_OPPOSITES["east"] == "west"
    assert DIRECTION_OPPOSITES["west"] == "east"
    assert DIRECTION_OPPOSITES["up"] == "down"
    assert DIRECTION_OPPOSITES["down"] == "up"


def test_create_teleport_effect_message_teleport_arrival():
    """Test create_teleport_effect_message for teleport arrival."""
    result = create_teleport_effect_message("TestPlayer", "arrival", teleport_type="teleport")
    assert "TestPlayer" in result
    assert "arrives" in result.lower() or "shimmer" in result.lower() or "energy" in result.lower()


def test_create_teleport_effect_message_teleport_departure():
    """Test create_teleport_effect_message for teleport departure."""
    result = create_teleport_effect_message("TestPlayer", "departure", teleport_type="teleport")
    assert "TestPlayer" in result
    assert "disappears" in result.lower() or "ripple" in result.lower() or "distorted" in result.lower()


def test_create_teleport_effect_message_teleport_departure_with_direction():
    """Test create_teleport_effect_message for teleport departure with direction."""
    result = create_teleport_effect_message("TestPlayer", "departure", teleport_type="teleport", direction="north")
    assert "TestPlayer" in result
    assert "north" in result.lower()
    assert "leaves" in result.lower()


def test_create_teleport_effect_message_teleport_arrival_with_direction():
    """Test create_teleport_effect_message for teleport arrival with direction."""
    result = create_teleport_effect_message("TestPlayer", "arrival", teleport_type="teleport", arrival_direction="south")
    assert "TestPlayer" in result
    assert "south" in result.lower()
    assert "arrives" in result.lower()


def test_create_teleport_effect_message_goto_arrival():
    """Test create_teleport_effect_message for goto arrival."""
    result = create_teleport_effect_message("TestPlayer", "arrival", teleport_type="goto")
    assert "TestPlayer" in result
    assert "appears" in result.lower() or "displaced" in result.lower()


def test_create_teleport_effect_message_goto_departure():
    """Test create_teleport_effect_message for goto departure."""
    result = create_teleport_effect_message("TestPlayer", "departure", teleport_type="goto")
    assert "TestPlayer" in result
    assert "vanishes" in result.lower() or "flash" in result.lower() or "light" in result.lower()


def test_create_teleport_effect_message_goto_arrival_with_direction():
    """Test create_teleport_effect_message for goto arrival with direction."""
    result = create_teleport_effect_message("TestPlayer", "arrival", teleport_type="goto", arrival_direction="east")
    assert "TestPlayer" in result
    assert "east" in result.lower()
    assert "arrives" in result.lower()


def test_create_teleport_effect_message_unknown_command():
    """Test create_teleport_effect_message with unknown command type."""
    result = create_teleport_effect_message("TestPlayer", "arrival", teleport_type="unknown")
    assert "TestPlayer" in result
    assert "mysterious" in result.lower() or "forces" in result.lower()
    assert isinstance(result, str)
    assert len(result) > 0
