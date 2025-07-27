"""
Tests for the schema validator module.

Tests JSON schema validation, exit format handling, and error reporting.
"""

import json
import tempfile
from pathlib import Path

import pytest

from core.schema_validator import SchemaValidator


# pylint: disable=too-many-public-methods
class TestSchemaValidator:
    """Test cases for the SchemaValidator class."""

    def test_init_with_default_schema(self):
        """Test SchemaValidator initialization with default schema path."""
        validator = SchemaValidator()
        assert validator.schema_path == Path("./schemas/room_schema.json")
        assert validator.schema is not None

    def test_init_with_custom_schema(self):
        """Test SchemaValidator initialization with custom schema path."""
        # Create a temporary schema file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump({"type": "object", "properties": {"test": {"type": "string"}}}, f)
            schema_path = f.name

        try:
            validator = SchemaValidator(schema_path)
            assert validator.schema_path == Path(schema_path)
            assert validator.schema is not None
        finally:
            Path(schema_path).unlink()

    def test_init_schema_file_not_found(self):
        """Test initialization with non-existent schema file."""
        with pytest.raises(FileNotFoundError):
            SchemaValidator("./nonexistent/schema.json")

    def test_init_invalid_schema_file(self):
        """Test initialization with invalid schema file."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write('{"invalid": json}')
            schema_path = f.name

        try:
            with pytest.raises(ValueError):
                SchemaValidator(schema_path)
        finally:
            Path(schema_path).unlink()

    def test_validate_room_valid(self, sample_room_data):
        """Test validation of valid room data."""
        validator = SchemaValidator()
        errors = validator.validate_room(sample_room_data)
        assert len(errors) == 0

    def test_validate_room_missing_required_field(self):
        """Test validation of room with missing required field."""
        validator = SchemaValidator()

        invalid_room = {
            "id": "test_001",
            "name": "Test Room",
            "description": "A test room"
            # Missing zone and exits
        }

        errors = validator.validate_room(invalid_room)
        assert len(errors) == 1
        assert "zone" in errors[0] or "exits" in errors[0]

    def test_validate_room_invalid_id_format(self):
        """Test validation of room with invalid ID format."""
        validator = SchemaValidator()

        invalid_room = {
            "id": "invalid-id!",  # Invalid characters
            "name": "Test Room",
            "description": "A test room",
            "zone": "test_zone",
            "exits": {"north": None, "south": None, "east": None, "west": None, "up": None, "down": None}
        }

        errors = validator.validate_room(invalid_room)
        assert len(errors) == 1
        assert "id" in errors[0]

    def test_validate_room_empty_name(self):
        """Test validation of room with empty name."""
        validator = SchemaValidator()

        invalid_room = {
            "id": "test_001",
            "name": "",  # Empty name
            "description": "A test room",
            "zone": "test_zone",
            "exits": {"north": None, "south": None, "east": None, "west": None, "up": None, "down": None}
        }

        errors = validator.validate_room(invalid_room)
        assert len(errors) == 1
        assert "name" in errors[0]

    def test_validate_room_with_file_path(self, sample_room_data):
        """Test validation with file path for error reporting."""
        validator = SchemaValidator()
        errors = validator.validate_room(sample_room_data, "test_room.json")
        assert len(errors) == 0

    def test_normalize_exits_legacy_format(self):
        """Test normalization of legacy string format exits."""
        validator = SchemaValidator()

        room_data = {
            "id": "test_001",
            "name": "Test Room",
            "description": "A test room",
            "zone": "test_zone",
            "exits": {
                "north": "test_002",
                "south": None,
                "east": "test_003"
            }
        }

        normalized = validator.normalize_exits(room_data)

        # Check that string exits are converted to object format
        # pylint: disable=invalid-sequence-index
        assert normalized["exits"]["north"]["target"] == "test_002"
        assert normalized["exits"]["north"]["flags"] == []
        assert normalized["exits"]["east"]["target"] == "test_003"
        assert normalized["exits"]["east"]["flags"] == []
        # Note: south exit is None, so we don't check it

    def test_normalize_exits_new_format(self):
        """Test normalization of new object format exits."""
        validator = SchemaValidator()

        room_data = {
            "id": "test_001",
            "name": "Test Room",
            "description": "A test room",
            "zone": "test_zone",
            "exits": {
                "north": {
                    "target": "test_002",
                    "flags": ["one_way"]
                },
                "south": {
                    "target": "test_003",
                    "flags": []
                }
            }
        }

        normalized = validator.normalize_exits(room_data)

        # Check that object exits are preserved
        # pylint: disable=invalid-sequence-index,unsubscriptable-object
        assert normalized["exits"]["north"]["target"] == "test_002"
        assert normalized["exits"]["north"]["flags"] == ["one_way"]
        assert normalized["exits"]["south"]["target"] == "test_003"
        assert normalized["exits"]["south"]["flags"] == []

    def test_validate_room_file_valid(self, sample_room_data):
        """Test validation of valid room file."""
        validator = SchemaValidator()

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(sample_room_data, f)
            file_path = Path(f.name)

        try:
            errors = validator.validate_room_file(file_path)
            assert len(errors) == 0
        finally:
            file_path.unlink()

    def test_validate_room_file_invalid_json(self):
        """Test validation of room file with invalid JSON."""
        validator = SchemaValidator()

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write('{"invalid": json}')
            file_path = Path(f.name)

        try:
            errors = validator.validate_room_file(file_path)
            assert len(errors) == 1
            assert "Invalid JSON" in errors[0]
        finally:
            file_path.unlink()

    def test_validate_room_database(self, sample_room_database):
        """Test validation of room database."""
        validator = SchemaValidator()
        results = validator.validate_room_database(sample_room_database)

        # All rooms should be valid
        assert len(results) == 0

    def test_validate_room_database_with_errors(self, invalid_room_data):
        """Test validation of room database with errors."""
        validator = SchemaValidator()

        database = {
            "valid_room": {
                "id": "valid_001",
                "name": "Valid Room",
                "description": "A valid room",
                "zone": "test_zone",
                "exits": {"north": None, "south": None, "east": None, "west": None, "up": None, "down": None}
            },
            "invalid_room": invalid_room_data
        }

        results = validator.validate_room_database(database)

        # Should have errors for the invalid room
        assert "invalid_room" in results
        assert len(results["invalid_room"]) > 0

    def test_get_exit_target_string_format(self):
        """Test getting exit target from string format."""
        validator = SchemaValidator()

        assert validator.get_exit_target("test_002") == "test_002"
        assert validator.get_exit_target(None) is None

    def test_get_exit_target_object_format(self):
        """Test getting exit target from object format."""
        validator = SchemaValidator()

        exit_data = {"target": "test_002", "flags": ["one_way"]}
        assert validator.get_exit_target(exit_data) == "test_002"

    def test_get_exit_target_invalid_format(self):
        """Test getting exit target from invalid format."""
        validator = SchemaValidator()

        assert validator.get_exit_target(123) is None
        assert validator.get_exit_target({"invalid": "data"}) is None

    def test_get_exit_flags_string_format(self):
        """Test getting exit flags from string format."""
        validator = SchemaValidator()

        assert validator.get_exit_flags("test_002") == []

    def test_get_exit_flags_object_format(self):
        """Test getting exit flags from object format."""
        validator = SchemaValidator()

        exit_data = {"target": "test_002", "flags": ["one_way", "self_reference"]}
        assert validator.get_exit_flags(exit_data) == ["one_way", "self_reference"]

    def test_get_exit_flags_missing_flags(self):
        """Test getting exit flags when flags field is missing."""
        validator = SchemaValidator()

        exit_data = {"target": "test_002"}
        assert validator.get_exit_flags(exit_data) == []

    def test_is_one_way_exit_true(self):
        """Test one-way exit detection when flag is present."""
        validator = SchemaValidator()

        exit_data = {"target": "test_002", "flags": ["one_way"]}
        assert validator.is_one_way_exit(exit_data) is True

    def test_is_one_way_exit_false(self):
        """Test one-way exit detection when flag is not present."""
        validator = SchemaValidator()

        exit_data = {"target": "test_002", "flags": []}
        assert validator.is_one_way_exit(exit_data) is False

        # String format should also return False
        assert validator.is_one_way_exit("test_002") is False

    def test_is_self_reference_exit_true(self):
        """Test self-reference exit detection when flag is present."""
        validator = SchemaValidator()

        exit_data = {"target": "test_002", "flags": ["self_reference"]}
        assert validator.is_self_reference_exit(exit_data) is True

    def test_is_self_reference_exit_false(self):
        """Test self-reference exit detection when flag is not present."""
        validator = SchemaValidator()

        exit_data = {"target": "test_002", "flags": []}
        assert validator.is_self_reference_exit(exit_data) is False

        # String format should also return False
        assert validator.is_self_reference_exit("test_002") is False
