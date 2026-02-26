"""
Unit tests for AsciiMapRenderer grid building.

Guards against regressions in _build_grid, especially player marker
preservation when multiple rooms share the same coordinates.
"""

import pytest

from server.services.ascii_map_renderer import AsciiMapRenderer

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice


@pytest.fixture
def renderer() -> AsciiMapRenderer:
    """Return a fresh AsciiMapRenderer instance for each test."""
    return AsciiMapRenderer()


class TestBuildGridPlayerMarker:
    """Tests for _build_grid player marker when multiple rooms share coordinates."""

    def test_player_marker_preserved_when_player_room_not_last_at_same_coords(self, renderer: AsciiMapRenderer) -> None:
        """Multiple rooms at same (x,y): cell keeps player marker even if player room is not last."""
        rooms = [
            {"id": "player_room", "stable_id": "player_room", "map_x": 0, "map_y": 0, "name": "Player Room"},
            {"id": "other_a", "stable_id": "other_a", "map_x": 0, "map_y": 0, "name": "Other A"},
            {"id": "other_b", "stable_id": "other_b", "map_x": 0, "map_y": 0, "name": "Other B"},
        ]
        grid, _room_positions = renderer._build_grid(rooms, current_room_id="player_room")
        cell = grid.get((0, 0))
        assert isinstance(cell, dict)
        assert cell.get("is_player") is True, "Player marker must be preserved when overwritten by later rooms"
