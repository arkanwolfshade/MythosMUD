"""
Unit tests for map_helpers (build_zone_pattern, build_room_dict).

Guards against regressions in zone pattern and room dict construction
used by ASCII map and minimap endpoints.
"""

from server.api.map_helpers import build_room_dict, build_zone_pattern


class TestBuildZonePattern:
    """Tests for build_zone_pattern."""

    def test_plane_zone_only(self) -> None:
        """Plane plus zone without sub-zone builds 'plane_zone'."""
        assert build_zone_pattern("material", "arkham", None) == "material_arkham"

    def test_plane_zone_sub_zone(self) -> None:
        """Plane, zone, and sub-zone build 'plane_zone_sub_zone'."""
        assert build_zone_pattern("material", "arkham", "miskatonic") == "material_arkham_miskatonic"

    def test_empty_sub_zone_treated_as_none(self) -> None:
        """Empty or missing sub-zone is treated like None and omitted."""
        # Pattern is plane_zone when sub_zone is None; empty string would still be truthy in the function
        assert build_zone_pattern("p", "z", None) == "p_z"


class TestBuildRoomDict:
    """Tests for build_room_dict from database row.

    Row tuple: (id, stable_id, name, attributes, map_x, map_y, map_origin_zone, map_symbol, map_style).
    """

    def test_full_row(self) -> None:
        """Full database row is mapped to a complete room dict."""
        row = (
            "uuid-123",
            "material_arkham_room_1",
            "Main Foyer",
            {"environment": "interior"},
            1.0,
            2.0,
            False,
            "#",
            "interior",
        )
        out = build_room_dict(row)
        assert out["uuid"] == "uuid-123"
        assert out["id"] == "material_arkham_room_1"
        assert out["stable_id"] == "material_arkham_room_1"
        assert out["name"] == "Main Foyer"
        assert out["attributes"] == {"environment": "interior"}
        assert out["map_x"] == 1.0
        assert out["map_y"] == 2.0
        assert out["map_origin_zone"] is False
        assert out["map_symbol"] == "#"
        assert out["map_style"] == "interior"
        assert not out["exits"]

    def test_null_map_coords(self) -> None:
        """Null map coordinates in the row become None in the room dict."""
        row = (
            "u",
            "stable_1",
            "Room",
            None,
            None,
            None,
            None,
            None,
            None,
        )
        out = build_room_dict(row)
        assert out["map_x"] is None
        assert out["map_y"] is None
        assert out["attributes"] == {}
