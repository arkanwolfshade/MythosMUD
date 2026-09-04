"""
Tests for the room loader module.

Tests file discovery, JSON parsing, and room database building
functionality.
"""

import json
import tempfile
from pathlib import Path

import pytest
from core.room_loader import RoomLoader


class TestRoomLoader:
    """Test cases for the RoomLoader class."""

    def test_init_with_default_path(self):
        """Test RoomLoader initialization with default path."""
        loader = RoomLoader()
        assert loader.base_path == Path("./data/local/rooms")
        assert loader.room_database == {}
        assert loader.parsing_errors == []

    def test_init_with_custom_path(self):
        """Test RoomLoader initialization with custom path."""
        custom_path = "./custom/rooms"
        loader = RoomLoader(custom_path)
        assert loader.base_path == Path(custom_path)

    def test_discover_room_files_success(self, temp_rooms_dir):
        """Test successful discovery of room files."""
        loader = RoomLoader(temp_rooms_dir)
        files = loader.discover_room_files()

        assert len(files) == 3
        file_names = [f.name for f in files]
        assert "test_zone_001.json" in file_names
        assert "test_zone_002.json" in file_names
        assert "test_zone_003.json" in file_names

    def test_discover_room_files_nonexistent_path(self):
        """Test discovery with non-existent path."""
        loader = RoomLoader("./nonexistent/path")

        with pytest.raises(FileNotFoundError):
            loader.discover_room_files()

    def test_load_room_data_valid(self, sample_room_data):
        """Test loading valid room data."""
        loader = RoomLoader()

        # Create a temporary file with valid room data
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(sample_room_data, f)
            file_path = Path(f.name)

        try:
            result = loader.load_room_data(file_path)
            assert result == sample_room_data
            assert len(loader.parsing_errors) == 0
        finally:
            file_path.unlink()

    def test_load_room_data_invalid_json(self):
        """Test loading room data with invalid JSON."""
        loader = RoomLoader()

        # Create a temporary file with invalid JSON
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write('{"invalid": json}')
            file_path = Path(f.name)

        try:
            result = loader.load_room_data(file_path)
            assert result is None
            assert len(loader.parsing_errors) == 1
            assert "Invalid JSON" in loader.parsing_errors[0][1]
        finally:
            file_path.unlink()

    def test_load_room_data_missing_required_fields(self):
        """Test loading room data with missing required fields."""
        loader = RoomLoader()

        # Create room data missing required fields
        invalid_data = {
            "id": "test_001",
            "name": "Test Room",
            # Missing description, zone, exits
        }

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(invalid_data, f)
            file_path = Path(f.name)

        try:
            result = loader.load_room_data(file_path)
            assert result is None
            assert len(loader.parsing_errors) == 1
            assert "Missing required field" in loader.parsing_errors[0][1]
        finally:
            file_path.unlink()

    def test_load_room_data_not_dict(self):
        """Test loading room data that is not a dictionary."""
        loader = RoomLoader()

        # Create a file with non-dict data
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(["not", "a", "dict"], f)
            file_path = Path(f.name)

        try:
            result = loader.load_room_data(file_path)
            assert result is None
            assert len(loader.parsing_errors) == 1
            assert "must be a JSON object" in loader.parsing_errors[0][1]
        finally:
            file_path.unlink()

    def test_build_room_database_success(self, temp_rooms_dir):
        """Test successful building of room database."""
        loader = RoomLoader(temp_rooms_dir)
        database = loader.build_room_database(show_progress=False)

        assert len(database) == 3
        assert "test_zone_001" in database
        assert "test_zone_002" in database
        assert "test_zone_003" in database

        # Check that room data is properly loaded
        room_001 = database["test_zone_001"]
        assert room_001["name"] == "Test Room 1"
        assert room_001["zone"] == "test_zone"
        assert room_001["exits"]["north"] == "test_zone_002"

    def test_build_room_database_empty_directory(self):
        """Test building database from empty directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            loader = RoomLoader(temp_dir)
            database = loader.build_room_database(show_progress=False)

            assert database == {}
            assert len(loader.parsing_errors) == 0

    def test_build_room_database_with_errors(self):
        """Test building database with some invalid files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            rooms_dir = Path(temp_dir) / "rooms" / "test_zone"
            rooms_dir.mkdir(parents=True)

            # Create one valid file
            valid_room = {
                "id": "valid_001",
                "name": "Valid Room",
                "description": "A valid room",
                "zone": "test_zone",
                "exits": {"north": None, "south": None, "east": None, "west": None, "up": None, "down": None},
            }

            with open(rooms_dir / "valid_001.json", "w", encoding="utf-8") as f:
                json.dump(valid_room, f)

            # Create one invalid file
            with open(rooms_dir / "invalid.json", "w", encoding="utf-8") as f:
                f.write('{"invalid": json}')

            loader = RoomLoader(temp_dir)
            database = loader.build_room_database(show_progress=False)

            # Should load the valid room
            assert len(database) == 1
            assert "valid_001" in database

            # Should record the parsing error
            assert len(loader.parsing_errors) == 1
            assert "invalid.json" in loader.parsing_errors[0][0]

    def test_get_zones(self, sample_room_database):
        """Test getting zones from room database."""
        loader = RoomLoader()
        loader.room_database = sample_room_database

        zones = loader.get_zones()
        assert zones == ["test_zone"]

    def test_get_rooms_by_zone(self, sample_room_database):
        """Test getting rooms by zone."""
        loader = RoomLoader()
        loader.room_database = sample_room_database

        zone_rooms = loader.get_rooms_by_zone("test_zone")
        assert len(zone_rooms) == 3
        assert "test_001" in zone_rooms
        assert "test_002" in zone_rooms
        assert "test_003" in zone_rooms

        # Test with non-existent zone
        empty_rooms = loader.get_rooms_by_zone("nonexistent")
        assert empty_rooms == {}

    def test_get_parsing_errors(self):
        """Test getting parsing errors."""
        loader = RoomLoader()
        loader.parsing_errors = [("file1.json", "Error 1"), ("file2.json", "Error 2")]

        errors = loader.get_parsing_errors()
        assert len(errors) == 2
        assert errors[0] == ("file1.json", "Error 1")
        assert errors[1] == ("file2.json", "Error 2")

    def test_validate_file_structure(self, temp_rooms_dir):
        """Test file structure validation."""
        loader = RoomLoader(temp_rooms_dir)
        warnings = loader.validate_file_structure()

        # Should not have warnings for properly structured files
        assert len(warnings) == 0

    def test_validate_file_structure_unusual_names(self):
        """Test file structure validation with unusual filenames."""
        with tempfile.TemporaryDirectory() as temp_dir:
            rooms_dir = Path(temp_dir) / "rooms" / "test_zone"
            rooms_dir.mkdir(parents=True)

            # Create file with unusual name
            with open(rooms_dir / "unusual.json", "w", encoding="utf-8") as f:
                json.dump({"id": "test", "name": "Test", "description": "Test", "zone": "test", "exits": {}}, f)
