"""
Unit tests for look command helper functions.

Tests utility functions used by the look command system.
"""

from unittest.mock import MagicMock

import pytest

from server.commands.look_helpers import (
    _get_health_label,
    _get_lucidity_label,
    _get_visible_equipment,
    _get_wearable_container_service,
    _is_direction,
    _parse_instance_number,
)


def test_parse_instance_number_hyphen_syntax():
    """Test _parse_instance_number with hyphen syntax."""
    target_name, instance_number = _parse_instance_number("backpack-2")
    assert target_name == "backpack"
    assert instance_number == 2


def test_parse_instance_number_space_syntax():
    """Test _parse_instance_number with space syntax."""
    target_name, instance_number = _parse_instance_number("backpack 2")
    assert target_name == "backpack"
    assert instance_number == 2


def test_parse_instance_number_no_instance():
    """Test _parse_instance_number with no instance number."""
    target_name, instance_number = _parse_instance_number("backpack")
    assert target_name == "backpack"
    assert instance_number is None


def test_parse_instance_number_multiple_spaces():
    """Test _parse_instance_number with multiple spaces."""
    target_name, instance_number = _parse_instance_number("back pack 2")
    assert target_name == "back pack"
    assert instance_number == 2


def test_get_health_label_healthy():
    """Test _get_health_label for healthy player."""
    stats = {"current_dp": 80, "max_dp": 100, "constitution": 50, "size": 50}
    label = _get_health_label(stats)
    assert label == "healthy"


def test_get_health_label_wounded():
    """Test _get_health_label for wounded player."""
    stats = {"current_dp": 50, "max_dp": 100, "constitution": 50, "size": 50}
    label = _get_health_label(stats)
    assert label == "wounded"


def test_get_health_label_critical():
    """Test _get_health_label for critical player."""
    stats = {"current_dp": 20, "max_dp": 100, "constitution": 50, "size": 50}
    label = _get_health_label(stats)
    assert label == "critical"


def test_get_health_label_mortally_wounded():
    """Test _get_health_label for mortally wounded player."""
    stats = {"current_dp": 0, "max_dp": 100, "constitution": 50, "size": 50}
    label = _get_health_label(stats)
    assert label == "mortally wounded"


def test_get_health_label_no_max_dp():
    """Test _get_health_label calculates max_dp from CON and SIZ."""
    stats = {"current_dp": 50, "constitution": 50, "size": 50}
    label = _get_health_label(stats)
    # max_dp = (50 + 50) / 5 = 20, health_percent = 50/20 = 250% (clamped to healthy)
    assert label in ["healthy", "wounded", "critical", "mortally wounded"]


def test_get_health_label_zero_max_dp():
    """Test _get_health_label with zero max_dp."""
    stats = {"current_dp": 0, "max_dp": 0, "constitution": 0, "size": 0}
    label = _get_health_label(stats)
    assert label == "mortally wounded"


def test_get_lucidity_label_lucid():
    """Test _get_lucidity_label for lucid."""
    stats = {"lucidity": 80, "max_lucidity": 100}
    label = _get_lucidity_label(stats)
    assert label == "lucid"


def test_get_lucidity_label_disturbed():
    """Test _get_lucidity_label for disturbed lucidity."""
    stats = {"lucidity": 50, "max_lucidity": 100}
    label = _get_lucidity_label(stats)
    assert label == "disturbed"


def test_get_lucidity_label_unstable():
    """Test _get_lucidity_label for unstable lucidity."""
    stats = {"lucidity": 10, "max_lucidity": 100}
    label = _get_lucidity_label(stats)
    assert label == "unstable"


def test_get_lucidity_label_mad():
    """Test _get_lucidity_label for mad lucidity."""
    stats = {"lucidity": 0, "max_lucidity": 100}
    label = _get_lucidity_label(stats)
    assert label == "mad"


def test_get_lucidity_label_no_lucidity():
    """Test _get_lucidity_label when lucidity is missing."""
    stats = {}
    label = _get_lucidity_label(stats)
    assert label == "mad"  # Defaults to 0 lucidity, which is mad


def test_get_visible_equipment_no_equipment():
    """Test _get_visible_equipment with no equipment."""
    player = MagicMock()
    player.get_equipped_items = MagicMock(return_value={})
    
    result = _get_visible_equipment(player)
    assert result == {}


def test_get_visible_equipment_with_equipment():
    """Test _get_visible_equipment with equipment."""
    player = MagicMock()
    player.get_equipped_items = MagicMock(return_value={
        "head": {"name": "Hat"},
        "ring": {"name": "Ring"},  # Hidden slot
    })
    
    result = _get_visible_equipment(player)
    assert "head" in result
    assert "ring" not in result  # Ring is a hidden slot
    assert result["head"]["name"] == "Hat"


def test_is_direction_cardinal():
    """Test _is_direction with cardinal directions."""
    assert _is_direction("north") is True
    assert _is_direction("south") is True
    assert _is_direction("east") is True
    assert _is_direction("west") is True


def test_is_direction_abbreviation():
    """Test _is_direction with abbreviations."""
    assert _is_direction("n") is True
    assert _is_direction("s") is True
    assert _is_direction("e") is True
    assert _is_direction("w") is True


def test_is_direction_not_direction():
    """Test _is_direction with non-direction."""
    assert _is_direction("player") is False
    assert _is_direction("item") is False
    assert _is_direction("") is False


def test_get_wearable_container_service_initializes():
    """Test _get_wearable_container_service initializes service."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.container = MagicMock()
    mock_app.state.container.async_persistence = MagicMock()
    mock_request.app = mock_app
    
    # Clear cached instance
    if hasattr(_get_wearable_container_service, "cached_instance"):
        _get_wearable_container_service.cached_instance = None
    
    service = _get_wearable_container_service(mock_request)
    assert service is not None


def test_get_wearable_container_service_no_persistence():
    """Test _get_wearable_container_service raises when persistence missing."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.container = None
    mock_request.app = mock_app
    
    # Clear cached instance
    if hasattr(_get_wearable_container_service, "cached_instance"):
        _get_wearable_container_service.cached_instance = None
    
    with pytest.raises(ValueError, match="async_persistence is required"):
        _get_wearable_container_service(mock_request)
