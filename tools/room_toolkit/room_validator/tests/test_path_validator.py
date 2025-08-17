"""
Tests for path validator functionality.

Validates room connectivity analysis with special focus on
zone transitions and dimensional boundaries.
"""

import pytest

from room_validator.core.path_validator import PathValidator


class TestPathValidator:
    """Test suite for path validation functionality."""

    @pytest.fixture
    def validator(self):
        """Create a path validator instance."""
        return PathValidator()

    @pytest.fixture
    def zone_transition_rooms(self):
        """Sample rooms with zone transitions."""
        return {
            "earth_arkham_city_northside_derby_st_014": {
                "id": "earth_arkham_city_northside_derby_st_014",
                "zone": "arkham_city",
                "sub_zone": "northside",
                "exits": {
                    "east": "earth_arkham_city_intersection_derby_garrison",
                    "west": "earth_arkham_city_northside_derby_st_013",
                },
            },
            "earth_arkham_city_intersection_derby_garrison": {
                "id": "earth_arkham_city_intersection_derby_garrison",
                "zone": "arkham_city",
                "sub_zone": "downtown",
                "exits": {
                    "west": "earth_arkham_city_northside_derby_st_014",
                    "east": "earth_arkham_city_downtown_derby_st_001",
                },
            },
            "earth_arkham_city_downtown_derby_st_001": {
                "id": "earth_arkham_city_downtown_derby_st_001",
                "zone": "arkham_city",
                "sub_zone": "downtown",
                "exits": {
                    "west": "earth_arkham_city_intersection_derby_garrison",
                    "east": "earth_arkham_city_downtown_derby_st_002",
                },
            },
        }

    def test_zone_transition_detection(self, validator, zone_transition_rooms):
        """Test detection of zone transitions in room connections."""
        missing_returns = validator.check_bidirectional_connections(zone_transition_rooms)
        assert len(missing_returns) == 0, "Valid zone transitions should not report errors"

    def test_broken_zone_transition(self, validator, zone_transition_rooms):
        """Test detection of broken zone transitions."""
        # Break the return path
        broken_rooms = zone_transition_rooms.copy()
        broken_rooms["earth_arkham_city_intersection_derby_garrison"]["exits"]["west"] = None

        missing_returns = validator.check_bidirectional_connections(broken_rooms)
        assert len(missing_returns) == 1
        room_a, dir_a, room_b, dir_b, is_zone_transition = missing_returns[0]
        assert is_zone_transition
        assert room_a == "earth_arkham_city_northside_derby_st_014"
        assert dir_a == "east"
        assert room_b == "earth_arkham_city_intersection_derby_garrison"
        assert dir_b == "west"

    def test_get_room_zone(self, validator, zone_transition_rooms):
        """Test extraction of zone information from room data."""
        room_id = "earth_arkham_city_northside_derby_st_014"
        zone, subzone = validator._get_room_zone(room_id, zone_transition_rooms)
        assert zone == "arkham_city"
        assert subzone == "northside"

    def test_missing_zone_info(self, validator):
        """Test handling of rooms with missing zone information."""
        rooms = {
            "room_a": {"id": "room_a", "exits": {"north": "room_b"}},
            "room_b": {
                "id": "room_b",
                "zone": "test_zone",  # Only zone, no subzone
                "exits": {"south": "room_a"},
            },
        }
        zone, subzone = validator._get_room_zone("room_a", rooms)
        assert zone == ""
        assert subzone == ""

    def test_one_way_zone_transition(self, validator, zone_transition_rooms):
        """Test one-way exits across zone boundaries."""
        one_way_rooms = zone_transition_rooms.copy()
        one_way_rooms["earth_arkham_city_northside_derby_st_014"]["exits"]["east"] = {
            "target": "earth_arkham_city_intersection_derby_garrison",
            "flags": ["one_way"],
        }

        missing_returns = validator.check_bidirectional_connections(one_way_rooms)
        assert len(missing_returns) == 0, "One-way zone transitions should not report errors"

    def test_mismatched_return_path(self, validator, zone_transition_rooms):
        """Test detection of mismatched return paths across zones."""
        mismatched_rooms = zone_transition_rooms.copy()
        mismatched_rooms["earth_arkham_city_intersection_derby_garrison"]["exits"]["west"] = "wrong_room_id"

        missing_returns = validator.check_bidirectional_connections(mismatched_rooms)
        assert len(missing_returns) == 1
        room_a, dir_a, room_b, dir_b, is_zone_transition = missing_returns[0]
        assert is_zone_transition
        assert room_a == "earth_arkham_city_northside_derby_st_014"
        assert room_b == "earth_arkham_city_intersection_derby_garrison"
