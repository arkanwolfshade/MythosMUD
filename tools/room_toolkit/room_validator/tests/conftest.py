"""
Pytest configuration and fixtures for room validator tests.

Provides test data and fixtures for comprehensive testing of the
validation system.
"""

import json
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def temp_rooms_dir():
    """Create a temporary directory with test room files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        rooms_dir = Path(temp_dir) / "rooms" / "test_zone"
        rooms_dir.mkdir(parents=True)

        # Create test room files
        test_rooms = {
            "test_zone_001.json": {
                "id": "test_zone_001",
                "name": "Test Room 1",
                "description": "A test room for validation",
                "zone": "test_zone",
                "exits": {
                    "north": "test_zone_002",
                    "south": None,
                    "east": "test_zone_003",
                    "west": None,
                    "up": None,
                    "down": None,
                },
                "field1": None,
                "field2": None,
                "field3": None,
            },
            "test_zone_002.json": {
                "id": "test_zone_002",
                "name": "Test Room 2",
                "description": "Another test room",
                "zone": "test_zone",
                "exits": {
                    "north": None,
                    "south": "test_zone_001",
                    "east": None,
                    "west": None,
                    "up": None,
                    "down": None,
                },
                "field1": None,
                "field2": None,
                "field3": None,
            },
            "test_zone_003.json": {
                "id": "test_zone_003",
                "name": "Test Room 3",
                "description": "A third test room",
                "zone": "test_zone",
                "exits": {
                    "north": None,
                    "south": None,
                    "east": None,
                    "west": "test_zone_001",
                    "up": None,
                    "down": None,
                },
                "field1": None,
                "field2": None,
                "field3": None,
            },
        }

        for filename, room_data in test_rooms.items():
            room_file = rooms_dir / filename
            with open(room_file, "w", encoding="utf-8") as f:
                json.dump(room_data, f, indent=2)

        yield temp_dir


@pytest.fixture
def sample_room_data():
    """Sample room data for testing."""
    return {
        "id": "test_001",
        "name": "Test Room",
        "description": "A test room for validation",
        "zone": "test_zone",
        "exits": {"north": "test_002", "south": None, "east": "test_003", "west": None, "up": None, "down": None},
        "field1": None,
        "field2": None,
        "field3": None,
    }


@pytest.fixture
def sample_room_database():
    """Sample room database for testing."""
    return {
        "test_001": {
            "id": "test_001",
            "name": "Test Room 1",
            "description": "A test room",
            "zone": "test_zone",
            "exits": {"north": "test_002", "south": None, "east": "test_003", "west": None, "up": None, "down": None},
        },
        "test_002": {
            "id": "test_002",
            "name": "Test Room 2",
            "description": "Another test room",
            "zone": "test_zone",
            "exits": {"north": None, "south": "test_001", "east": None, "west": None, "up": None, "down": None},
        },
        "test_003": {
            "id": "test_003",
            "name": "Test Room 3",
            "description": "A third test room",
            "zone": "test_zone",
            "exits": {"north": None, "south": None, "east": None, "west": "test_001", "up": None, "down": None},
        },
    }


@pytest.fixture
def invalid_room_data():
    """Invalid room data for testing error conditions."""
    return {
        "id": "invalid_room",
        "name": "",  # Invalid: empty name
        "description": "A room with invalid data",
        "zone": "test_zone",
        "exits": {
            "north": "nonexistent_room",  # Invalid: references non-existent room
            "south": None,
            "east": None,
            "west": None,
            "up": None,
            "down": None,
        },
    }


@pytest.fixture
def room_with_new_exit_format():
    """Room data using the new object format for exits."""
    return {
        "id": "new_format_001",
        "name": "New Format Room",
        "description": "A room using new exit format",
        "zone": "test_zone",
        "exits": {
            "north": {"target": "new_format_002", "flags": ["one_way"]},
            "south": {"target": "new_format_003", "flags": []},
            "east": None,
            "west": None,
            "up": None,
            "down": None,
        },
    }


@pytest.fixture
def room_with_self_reference():
    """Room data with self-reference exit."""
    return {
        "id": "self_ref_001",
        "name": "Self Reference Room",
        "description": "A room that references itself",
        "zone": "test_zone",
        "exits": {
            "north": {"target": "self_ref_001", "flags": ["self_reference"]},
            "south": None,
            "east": None,
            "west": None,
            "up": None,
            "down": None,
        },
    }


@pytest.fixture
def dead_end_room():
    """Room data with no exits (dead end)."""
    return {
        "id": "dead_end_001",
        "name": "Dead End Room",
        "description": "A room with no exits",
        "zone": "test_zone",
        "exits": {"north": None, "south": None, "east": None, "west": None, "up": None, "down": None},
    }


@pytest.fixture
def unreachable_room():
    """Room data that would be unreachable from the starting room."""
    return {
        "id": "unreachable_001",
        "name": "Unreachable Room",
        "description": "A room with no connection to starting room",
        "zone": "test_zone",
        "exits": {"north": None, "south": None, "east": None, "west": None, "up": None, "down": None},
    }
