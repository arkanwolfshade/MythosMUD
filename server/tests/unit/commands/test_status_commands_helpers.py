"""
Unit tests for status_commands helper functions.

Tests helper functions in status_commands.py module.
"""

from typing import Any
from unittest.mock import MagicMock

from server.commands.status_commands import (
    _add_additional_stats_lines,
    _add_profession_lines,
    _build_base_status_lines,
)


def test_build_base_status_lines():
    """Test _build_base_status_lines() builds status lines."""
    player = MagicMock()
    player.name = "TestPlayer"
    player.experience_points = 100
    stats = {"position": "standing", "current_dp": 80, "max_dp": 100, "lucidity": 90, "max_lucidity": 100}

    result = _build_base_status_lines(player, "Test Room", stats, False)

    assert len(result) == 7
    assert "Name: TestPlayer" in result
    assert "Location: Test Room" in result
    assert "Position: Standing" in result
    assert "Health: 80/100" in result
    assert "lucidity: 90/100" in result
    assert "XP: 100" in result
    assert "In Combat: No" in result


def test_build_base_status_lines_in_combat():
    """Test _build_base_status_lines() shows combat status."""
    player = MagicMock()
    player.name = "TestPlayer"
    player.experience_points = 100
    stats = {"position": "standing", "current_dp": 80, "max_dp": 100, "lucidity": 90, "max_lucidity": 100}

    result = _build_base_status_lines(player, "Test Room", stats, True)

    assert "In Combat: Yes" in result


def test_build_base_status_lines_sitting():
    """Test _build_base_status_lines() formats position correctly."""
    player = MagicMock()
    player.name = "TestPlayer"
    player.experience_points = 100
    stats = {"position": "sitting", "current_dp": 80, "max_dp": 100, "lucidity": 90, "max_lucidity": 100}

    result = _build_base_status_lines(player, "Test Room", stats, False)

    assert "Position: Sitting" in result


def test_add_profession_lines():
    """Test _add_profession_lines() adds profession information."""
    status_lines: list[str] = []
    profession_info = {"name": "Investigator", "description": "A seeker of truth", "flavor_text": "You investigate"}

    _add_profession_lines(status_lines, profession_info)

    assert len(status_lines) == 3
    assert "Profession: Investigator" in status_lines
    assert "Description: A seeker of truth" in status_lines
    assert "Background: You investigate" in status_lines


def test_add_profession_lines_no_profession():
    """Test _add_profession_lines() does nothing when no profession."""
    status_lines: list[str] = []
    profession_info = {"name": None, "description": None, "flavor_text": None}

    _add_profession_lines(status_lines, profession_info)

    assert len(status_lines) == 0


def test_add_additional_stats_lines():
    """Test _add_additional_stats_lines() adds additional stats."""
    status_lines: list[str] = []
    stats: dict[str, Any] = {"fear": 10, "corruption": 5, "occult": 20}

    _add_additional_stats_lines(status_lines, stats)

    assert len(status_lines) > 0
    assert any("fear" in line.lower() or "10" in line for line in status_lines)


def test_add_additional_stats_lines_empty():
    """Test _add_additional_stats_lines() handles empty stats."""
    status_lines: list[str] = []
    stats: dict[str, Any] = {}

    _add_additional_stats_lines(status_lines, stats)

    # Should not add lines for empty stats
    assert len(status_lines) == 0


def test_add_additional_stats_lines_zero_values():
    """Test _add_additional_stats_lines() ignores zero values."""
    status_lines: list[str] = []
    stats = {"fear": 0, "corruption": 0, "occult": 0}

    _add_additional_stats_lines(status_lines, stats)

    # Should not add lines for zero values
    assert len(status_lines) == 0
