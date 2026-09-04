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


def test_render_map_empty_and_connected_rooms(renderer: AsciiMapRenderer) -> None:
    """render_map covers empty map, styles, exits, and row rendering."""
    empty = renderer.render_map([], viewport_width=10, viewport_height=4)
    assert "ascii-map" in empty

    rooms = [
        {
            "id": "a",
            "stable_id": "a",
            "map_x": 0,
            "map_y": 0,
            "name": "A",
            "environment": "outdoors",
            "exits": {"east": "b", "south": "c"},
        },
        {
            "id": "b",
            "stable_id": "b",
            "map_x": 1,
            "map_y": 0,
            "name": "B",
            "environment": "outdoors",
            "exits": {"west": "a"},
        },
        {
            "id": "c",
            "stable_id": "c",
            "map_x": 0,
            "map_y": 1,
            "name": "C",
            "environment": "city",
            "exits": {"north": "a"},
            "map_style": "city",
        },
    ]
    html = renderer.render_map(rooms, current_room_id="a", viewport_width=20, viewport_height=10)
    assert "ascii-map" in html
    assert "@" in html or "■" in html or "#" in html or "." in html


def test_determine_map_style_and_symbols(renderer: AsciiMapRenderer) -> None:
    assert renderer._determine_map_style([]) == "world"
    assert renderer._determine_map_style([{"environment": "indoors"}]) == "interior"
    assert renderer._determine_map_style([{"environment": "town"}]) == "city"
    assert renderer._determine_map_style([{"map_style": "world"}]) == "world"
    room = {"terrain": "road", "name": "Road"}
    assert isinstance(renderer._get_room_symbol(room, "world"), str)
    assert renderer._get_reverse_direction("north") == "south"
    assert renderer._get_reverse_direction("east") == "west"
