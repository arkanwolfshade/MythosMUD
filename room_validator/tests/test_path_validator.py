"""
Tests for the path validator module.

Tests graph traversal, connectivity analysis, and path validation.
"""

# Removed unused import: pytest

from core.path_validator import PathValidator
from core.schema_validator import SchemaValidator


# pylint: disable=too-many-public-methods
class TestPathValidator:
    """Test cases for the PathValidator class."""

    def test_init_without_schema_validator(self):
        """Test PathValidator initialization without schema validator."""
        validator = PathValidator()
        assert validator.schema_validator is None
        assert validator.graph == {}
        assert validator.reverse_graph == {}

    def test_init_with_schema_validator(self):
        """Test PathValidator initialization with schema validator."""
        schema_validator = SchemaValidator()
        validator = PathValidator(schema_validator)
        assert validator.schema_validator == schema_validator

    def test_build_graph_success(self, sample_room_database):
        """Test successful graph building."""
        validator = PathValidator()
        graph = validator.build_graph(sample_room_database)

        assert len(graph) == 3
        assert "test_001" in graph
        assert "test_002" in graph
        assert "test_003" in graph

        # Check connections
        assert graph["test_001"]["north"] == "test_002"
        assert graph["test_001"]["east"] == "test_003"
        assert graph["test_002"]["south"] == "test_001"
        assert graph["test_003"]["west"] == "test_001"

    def test_build_graph_with_nonexistent_targets(self):
        """Test graph building with exits to non-existent rooms."""
        validator = PathValidator()

        room_database = {
            "room_001": {
                "id": "room_001",
                "name": "Room 1",
                "description": "A room",
                "zone": "test_zone",
                "exits": {
                    "north": "nonexistent_room",
                    "south": None,
                    "east": None,
                    "west": None,
                    "up": None,
                    "down": None,
                },
            }
        }

        graph = validator.build_graph(room_database)

        # Should not include exits to non-existent rooms
        assert len(graph) == 1
        assert "room_001" in graph
        assert "north" not in graph["room_001"]

    def test_find_unreachable_rooms_all_reachable(self, sample_room_database):
        """Test finding unreachable rooms when all are reachable."""
        validator = PathValidator()
        unreachable = validator.find_unreachable_rooms(start_room_id="test_001", room_database=sample_room_database)

        assert len(unreachable) == 0

    def test_find_unreachable_rooms_some_unreachable(self, sample_room_database, unreachable_room):
        """Test finding unreachable rooms when some are unreachable."""
        validator = PathValidator()

        # Add an unreachable room to the database
        room_database = sample_room_database.copy()
        room_database["unreachable_001"] = unreachable_room

        unreachable = validator.find_unreachable_rooms(start_room_id="test_001", room_database=room_database)

        assert len(unreachable) == 1
        assert "unreachable_001" in unreachable

    def test_find_unreachable_rooms_starting_room_not_exists(self, sample_room_database):
        """Test finding unreachable rooms when starting room doesn't exist."""
        validator = PathValidator()
        unreachable = validator.find_unreachable_rooms(
            start_room_id="nonexistent_room", room_database=sample_room_database
        )

        # All rooms should be unreachable
        assert len(unreachable) == 3
        assert "test_001" in unreachable
        assert "test_002" in unreachable
        assert "test_003" in unreachable

    def test_check_bidirectional_connections_all_valid(self, sample_room_database):
        """Test bidirectional connection checking with valid connections."""
        validator = PathValidator()
        missing_returns = validator.check_bidirectional_connections(sample_room_database)

        assert len(missing_returns) == 0

    def test_check_bidirectional_connections_missing_returns(self):
        """Test bidirectional connection checking with missing return paths."""
        validator = PathValidator()

        room_database = {
            "room_001": {
                "id": "room_001",
                "name": "Room 1",
                "description": "A room",
                "zone": "test_zone",
                "exits": {"north": "room_002", "south": None, "east": None, "west": None, "up": None, "down": None},
            },
            "room_002": {
                "id": "room_002",
                "name": "Room 2",
                "description": "Another room",
                "zone": "test_zone",
                "exits": {
                    "north": None,
                    "south": None,  # Missing return to room_001
                    "east": None,
                    "west": None,
                    "up": None,
                    "down": None,
                },
            },
        }

        missing_returns = validator.check_bidirectional_connections(room_database)

        assert len(missing_returns) == 1
        assert missing_returns[0] == ("room_001", "north", "room_002", "south")

    def test_check_bidirectional_connections_one_way_exit(self):
        """Test bidirectional connection checking with one-way exits."""
        validator = PathValidator()

        room_database = {
            "room_001": {
                "id": "room_001",
                "name": "Room 1",
                "description": "A room",
                "zone": "test_zone",
                "exits": {
                    "north": {"target": "room_002", "flags": ["one_way"]},
                    "south": None,
                    "east": None,
                    "west": None,
                    "up": None,
                    "down": None,
                },
            },
            "room_002": {
                "id": "room_002",
                "name": "Room 2",
                "description": "Another room",
                "zone": "test_zone",
                "exits": {
                    "north": None,
                    "south": None,  # Missing return, but should be allowed
                    "east": None,
                    "west": None,
                    "up": None,
                    "down": None,
                },
            },
        }

        missing_returns = validator.check_bidirectional_connections(room_database)

        # Should not report missing return for one-way exit
        assert len(missing_returns) == 0

    def test_find_dead_ends_none(self, sample_room_database):
        """Test finding dead ends when none exist."""
        validator = PathValidator()
        dead_ends = validator.find_dead_ends(sample_room_database)

        assert len(dead_ends) == 0

    def test_find_dead_ends_some_exist(self, sample_room_database, dead_end_room):
        """Test finding dead ends when some exist."""
        validator = PathValidator()

        room_database = sample_room_database.copy()
        room_database["dead_end_001"] = dead_end_room

        dead_ends = validator.find_dead_ends(room_database)

        assert len(dead_ends) == 1
        assert "dead_end_001" in dead_ends

    def test_find_potential_dead_ends_none(self, sample_room_database):
        """Test finding potential dead ends when none exist."""
        validator = PathValidator()
        potential_dead_ends = validator.find_potential_dead_ends(sample_room_database)

        # The sample database has rooms with only one exit, so they are potential dead ends
        assert len(potential_dead_ends) == 2
        assert "test_002" in potential_dead_ends
        assert "test_003" in potential_dead_ends

    def test_find_potential_dead_ends_some_exist(self):
        """Test finding potential dead ends when some exist."""
        validator = PathValidator()

        room_database = {
            "room_001": {
                "id": "room_001",
                "name": "Room 1",
                "description": "A room",
                "zone": "test_zone",
                "exits": {"north": "room_002", "south": None, "east": None, "west": None, "up": None, "down": None},
            },
            "room_002": {
                "id": "room_002",
                "name": "Room 2",
                "description": "Another room",
                "zone": "test_zone",
                "exits": {"north": None, "south": "room_001", "east": None, "west": None, "up": None, "down": None},
            },
        }

        potential_dead_ends = validator.find_potential_dead_ends(room_database)

        assert len(potential_dead_ends) == 2
        assert "room_001" in potential_dead_ends
        assert "room_002" in potential_dead_ends

    def test_find_self_references_none(self, sample_room_database):
        """Test finding self-references when none exist."""
        validator = PathValidator()
        self_references = validator.find_self_references(sample_room_database)

        assert len(self_references) == 0

    def test_find_self_references_without_flag(self):
        """Test finding self-references without proper flag."""
        validator = PathValidator()

        room_database = {
            "room_001": {
                "id": "room_001",
                "name": "Room 1",
                "description": "A room",
                "zone": "test_zone",
                "exits": {
                    "north": "room_001",  # Self-reference without flag
                    "south": None,
                    "east": None,
                    "west": None,
                    "up": None,
                    "down": None,
                },
            }
        }

        self_references = validator.find_self_references(room_database)

        assert len(self_references) == 1
        assert self_references[0] == ("room_001", "north")

    def test_find_self_references_with_flag(self, room_with_self_reference):
        """Test finding self-references with proper flag."""
        validator = PathValidator()

        room_database = {"self_ref_001": room_with_self_reference}
        self_references = validator.find_self_references(room_database)

        # Should not report self-reference with proper flag
        assert len(self_references) == 0

    def test_find_cycles_none(self, sample_room_database):
        """Test finding cycles when none exist."""
        validator = PathValidator()
        cycles = validator.find_cycles(sample_room_database)

        assert len(cycles) == 0

    def test_find_cycles_simple_cycle(self):
        """Test finding simple cycles."""
        validator = PathValidator()

        room_database = {
            "room_001": {
                "id": "room_001",
                "name": "Room 1",
                "description": "A room",
                "zone": "test_zone",
                "exits": {"north": "room_002", "south": None, "east": None, "west": None, "up": None, "down": None},
            },
            "room_002": {
                "id": "room_002",
                "name": "Room 2",
                "description": "Another room",
                "zone": "test_zone",
                "exits": {
                    "north": None,
                    "south": "room_001",  # Creates cycle
                    "east": None,
                    "west": None,
                    "up": None,
                    "down": None,
                },
            },
        }

        cycles = validator.find_cycles(room_database)

        assert len(cycles) == 1
        # Should find the cycle: room_001 -> room_002 -> room_001
        cycle = cycles[0]
        assert "room_001" in cycle
        assert "room_002" in cycle

    def test_get_room_connectivity_stats(self, sample_room_database):
        """Test getting connectivity statistics."""
        validator = PathValidator()
        stats = validator.get_room_connectivity_stats(sample_room_database)

        assert stats["total_rooms"] == 3
        assert stats["total_exits"] == 4  # 2 from room_001, 1 from room_002, 1 from room_003
        assert stats["average_exits_per_room"] == 4 / 3
        assert stats["unreachable_rooms"] == 0
        assert stats["dead_ends"] == 0
        assert stats["potential_dead_ends"] == 2  # test_002 and test_003 have only one exit
        assert stats["missing_return_paths"] == 0
        assert stats["self_references"] == 0
        assert stats["cycles"] == 0
        assert 0 <= stats["connectivity_score"] <= 100

    def test_get_opposite_direction(self):
        """Test getting opposite directions."""
        validator = PathValidator()

        assert validator._get_opposite_direction("north") == "south"
        assert validator._get_opposite_direction("south") == "north"
        assert validator._get_opposite_direction("east") == "west"
        assert validator._get_opposite_direction("west") == "east"
        assert validator._get_opposite_direction("up") == "down"
        assert validator._get_opposite_direction("down") == "up"
        assert validator._get_opposite_direction("unknown") == "unknown"
