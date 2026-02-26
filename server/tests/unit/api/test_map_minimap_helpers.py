"""
Unit tests for map_minimap pure helpers.

Guards against regressions in minimap fallback coordinates and
ensuring current room is in the room list (append with fallback coords).
"""

from server.api.map_minimap import (
    _append_room_with_fallback_coords_if_needed,
    _apply_minimap_fallback_coordinates,
)


class TestAppendRoomWithFallbackCoordsIfNeeded:
    """Tests for _append_room_with_fallback_coords_if_needed."""

    def test_appends_room_unchanged_when_has_coords(self) -> None:
        """Room with map_x/map_y is appended as-is."""
        rooms: list[dict] = []
        room = {"id": "r1", "stable_id": "r1", "map_x": 5.0, "map_y": 10.0}
        _append_room_with_fallback_coords_if_needed(rooms, room)
        assert len(rooms) == 1
        assert rooms[0]["map_x"] == 5.0
        assert rooms[0]["map_y"] == 10.0

    def test_appends_copy_with_fallback_0_0_when_coords_missing(self) -> None:
        """Room with missing coords is appended with fallback (0, 0); original unchanged."""
        rooms = []
        room = {"id": "r1", "stable_id": "r1", "map_x": None, "map_y": None}
        _append_room_with_fallback_coords_if_needed(rooms, room)
        assert len(rooms) == 1
        assert rooms[0]["map_x"] == 0.0
        assert rooms[0]["map_y"] == 0.0
        assert room["map_x"] is None  # original unchanged

    def test_appends_fallback_when_only_one_coord_missing(self) -> None:
        """If either map_x or map_y is missing, appended room gets fallback (0, 0)."""
        rooms = []
        room = {"id": "r1", "map_x": 1.0, "map_y": None}
        _append_room_with_fallback_coords_if_needed(rooms, room)
        assert len(rooms) == 1
        assert rooms[0]["map_x"] == 0.0
        assert rooms[0]["map_y"] == 0.0


class TestApplyMinimapFallbackCoordinates:
    """Tests for _apply_minimap_fallback_coordinates (mutates rooms in place)."""

    def test_admin_gets_grid_layout_for_rooms_without_coords(self) -> None:
        """Admin sees all rooms without coords laid out in a grid (fallback applied)."""
        rooms = [
            {"id": "r0", "map_x": None, "map_y": None},
            {"id": "r1", "map_x": None, "map_y": None},
            {"id": "r2", "map_x": None, "map_y": None},
        ]
        _apply_minimap_fallback_coordinates(rooms, current_room_id=None, is_admin=True, fallback_grid_width=2)
        assert rooms[0]["map_x"] == 0.0
        assert rooms[0]["map_y"] == 0.0
        assert rooms[1]["map_x"] == 1.0
        assert rooms[1]["map_y"] == 0.0
        assert rooms[2]["map_x"] == 0.0
        assert rooms[2]["map_y"] == 1.0

    def test_non_admin_gets_fallback_only_for_current_room(self) -> None:
        """Non-admin gets fallback coords only for the current room; others stay None."""
        rooms = [
            {"id": "r0", "map_x": 1.0, "map_y": 1.0},
            {"id": "current", "map_x": None, "map_y": None},
            {"id": "r2", "map_x": None, "map_y": None},
        ]
        _apply_minimap_fallback_coordinates(rooms, current_room_id="current", is_admin=False)
        assert rooms[0]["map_x"] == 1.0
        assert rooms[0]["map_y"] == 1.0
        assert rooms[1]["map_x"] == 0.0
        assert rooms[1]["map_y"] == 0.0
        assert rooms[2]["map_x"] is None  # unchanged
        assert rooms[2]["map_y"] is None

    def test_non_admin_uses_stable_id_for_current_room_match(self) -> None:
        """Current room is matched by stable_id and receives fallback coords."""
        rooms = [{"id": "sid_123", "stable_id": "sid_123", "map_x": None, "map_y": None}]
        _apply_minimap_fallback_coordinates(rooms, current_room_id="sid_123", is_admin=False)
        assert rooms[0]["map_x"] == 0.0
        assert rooms[0]["map_y"] == 0.0
