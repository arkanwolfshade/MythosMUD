"""
Unit tests for AsciiMapRenderer exit character and exit resolution.

Guards against regressions in horizontal/vertical exit characters
(em dash, >, <, |, v, ^) and viewport bounds.
"""

import pytest

from server.services.ascii_map_renderer import AsciiMapRenderer

# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice


@pytest.fixture
def renderer() -> AsciiMapRenderer:
    """Return a fresh AsciiMapRenderer instance for each test."""
    return AsciiMapRenderer()


class TestHorizontalExitCharBetween:
    """Tests for _horizontal_exit_char_between (em dash, >, <)."""

    def test_bidirectional_returns_em_dash(self, renderer: AsciiMapRenderer) -> None:
        """Bidirectional horizontal exit between two rooms uses an em dash."""
        east_exit = {"target": (2, 1)}
        west_exit_back = {"target": (1, 1)}
        char = renderer._horizontal_exit_char_between(east_exit, west_exit_back, next_x=2, y=1, x=1)
        assert char == "\u2014"  # em dash

    def test_one_way_east_returns_gt(self, renderer: AsciiMapRenderer) -> None:
        """One-way east exit renders as a greater-than sign."""
        east_exit = {"target": (2, 1)}
        char = renderer._horizontal_exit_char_between(east_exit, None, next_x=2, y=1, x=1)
        assert char == ">"

    def test_one_way_west_returns_lt(self, renderer: AsciiMapRenderer) -> None:
        """One-way west exit renders as a less-than sign."""
        west_exit_back = {"target": (1, 1)}
        char = renderer._horizontal_exit_char_between(None, west_exit_back, next_x=2, y=1, x=1)
        assert char == "<"

    def test_no_exit_returns_none(self, renderer: AsciiMapRenderer) -> None:
        """When there are no horizontal exits, the helper returns None."""
        char = renderer._horizontal_exit_char_between(None, None, next_x=2, y=1, x=1)
        assert char is None


class TestVerticalExitCharBetween:
    """Tests for _vertical_exit_char_between (|, v, ^)."""

    def test_bidirectional_returns_pipe(self, renderer: AsciiMapRenderer) -> None:
        """Bidirectional vertical exit renders as a vertical bar."""
        south_exit = {"target": (1, 2)}
        north_exit_back = {"target": (1, 1)}
        char = renderer._vertical_exit_char_between(south_exit, north_exit_back, next_y=2, x=1, y=1)
        assert char == "|"

    def test_one_way_south_returns_v(self, renderer: AsciiMapRenderer) -> None:
        """One-way south exit renders as a lowercase 'v'."""
        south_exit = {"target": (1, 2)}
        char = renderer._vertical_exit_char_between(south_exit, None, next_y=2, x=1, y=1)
        assert char == "v"

    def test_one_way_north_returns_caret(self, renderer: AsciiMapRenderer) -> None:
        """One-way north exit renders as a caret."""
        north_exit_back = {"target": (1, 1)}
        char = renderer._vertical_exit_char_between(None, north_exit_back, next_y=2, x=1, y=1)
        assert char == "^"

    def test_no_exit_returns_none(self, renderer: AsciiMapRenderer) -> None:
        """When there are no vertical exits, the helper returns None."""
        char = renderer._vertical_exit_char_between(None, None, next_y=2, x=1, y=1)
        assert char is None


class TestResolveExitTarget:
    """Tests for _resolve_exit_target."""

    def test_returns_coords_and_bidirectional_when_target_has_reverse_exit(self, renderer: AsciiMapRenderer) -> None:
        """Room with a reverse exit is treated as bidirectional and returns its coordinates."""
        rooms = [
            {"id": "a", "stable_id": "a", "map_x": 0, "map_y": 0, "exits": {"east": "b"}},
            {"id": "b", "stable_id": "b", "map_x": 1, "map_y": 0, "exits": {"west": "a"}},
        ]
        result = renderer._resolve_exit_target(rooms, "b", "east", "a")
        assert result is not None
        (tx, ty), is_bidirectional = result
        assert (tx, ty) == (1, 0)
        assert is_bidirectional is True

    def test_returns_coords_and_not_bidirectional_when_no_reverse(self, renderer: AsciiMapRenderer) -> None:
        """Room without a reverse exit is not considered bidirectional."""
        rooms = [
            {"id": "a", "stable_id": "a", "map_x": 0, "map_y": 0, "exits": {"east": "b"}},
            {"id": "b", "stable_id": "b", "map_x": 1, "map_y": 0, "exits": {}},
        ]
        result = renderer._resolve_exit_target(rooms, "b", "east", "a")
        assert result is not None
        _, is_bidirectional = result
        assert is_bidirectional is False

    def test_returns_none_when_target_room_missing(self, renderer: AsciiMapRenderer) -> None:
        """If the target room ID does not exist, the helper returns None."""
        rooms = [{"id": "a", "stable_id": "a", "map_x": 0, "map_y": 0, "exits": {"east": "c"}}]
        result = renderer._resolve_exit_target(rooms, "c", "east", "a")
        assert result is None

    def test_returns_none_when_target_room_has_no_coords(self, renderer: AsciiMapRenderer) -> None:
        """If the target room lacks map coordinates, the helper returns None."""
        rooms = [
            {"id": "a", "map_x": 0, "map_y": 0, "exits": {"east": "b"}},
            {"id": "b", "stable_id": "b", "map_x": None, "map_y": None, "exits": {}},
        ]
        result = renderer._resolve_exit_target(rooms, "b", "east", "a")
        assert result is None


class TestGetExitEntriesForRoom:
    """Tests for _get_exit_entries_for_room."""

    def test_returns_entries_for_valid_exits(self, renderer: AsciiMapRenderer) -> None:
        """Valid exits for a room produce one entry with correct direction and coordinates."""
        rooms = [
            {"id": "a", "stable_id": "a", "map_x": 0, "map_y": 0, "exits": {"east": "b"}},
            {"id": "b", "stable_id": "b", "map_x": 1, "map_y": 0, "exits": {"west": "a"}},
        ]
        room_a = rooms[0]
        entries = renderer._get_exit_entries_for_room(room_a, rooms)
        assert len(entries) == 1
        direction, coords, is_bidirectional = entries[0]
        assert direction == "east"
        assert coords == (1, 0)
        assert is_bidirectional is True

    def test_skips_exit_with_missing_target(self, renderer: AsciiMapRenderer) -> None:
        """Exits whose targets are missing are skipped when building exit entries."""
        rooms = [
            {"id": "a", "stable_id": "a", "map_x": 0, "map_y": 0, "exits": {"east": "b", "south": "c"}},
        ]
        entries = renderer._get_exit_entries_for_room(rooms[0], rooms)
        assert len(entries) == 0


class TestGetHorizontalExitCharViewportBounds:
    """Viewport bounds: return None when next cell is outside viewport."""

    def test_returns_none_when_next_x_at_or_past_viewport_right(self, renderer: AsciiMapRenderer) -> None:
        """Returns None when the next horizontal cell lies at or beyond the viewport's right edge."""
        exit_from = {(0, 0): {"east": {"target": (1, 0), "is_bidirectional": True}}}
        grid = {(0, 0): {"id": "a"}, (1, 0): {"id": "b"}}
        viewport_x, viewport_width = 0, 1
        char = renderer._get_horizontal_exit_char(0, 0, exit_from, grid, viewport_x, viewport_width)
        assert char is None
