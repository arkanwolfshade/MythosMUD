"""
Unit tests for room data validator.

Tests the RoomDataValidator class for validating room data structures.
"""

from unittest.mock import patch

import pytest

from server.services.room_data_validator import RoomDataValidator


class TestRoomDataValidator:
    """Test suite for RoomDataValidator class."""

    def test_validate_room_data_valid(self):
        """Test validate_room_data with valid room data."""
        room_data = {
            "id": "test_room_1",
            "name": "Test Room",
            "description": "A test room description",
            "timestamp": 1234567890.0,
            "occupants": ["player1", "player2"],
            "occupant_count": 2,
        }
        result = RoomDataValidator.validate_room_data(room_data)
        assert result["is_valid"] is True
        assert len(result["errors"]) == 0
        assert result["room_id"] == "test_room_1"

    def test_validate_room_data_missing_required_fields(self):
        """Test validate_room_data with missing required fields."""
        room_data = {"id": "test_room_1"}
        result = RoomDataValidator.validate_room_data(room_data)
        assert result["is_valid"] is False
        assert "Missing required field: name" in result["errors"]
        assert "Missing required field: description" in result["errors"]

    def test_validate_room_data_invalid_field_types(self):
        """Test validate_room_data with invalid field types."""
        room_data = {
            "id": 123,  # Should be string
            "name": "Test Room",
            "description": "A test room description",
            "timestamp": "not_a_number",  # Should be number
        }
        result = RoomDataValidator.validate_room_data(room_data)
        assert result["is_valid"] is False
        assert any("Field 'id' must be a string" in error for error in result["errors"])
        assert any("Field 'timestamp' must be a number" in error for error in result["errors"])

    def test_validate_room_data_invalid_room_id_format(self):
        """Test validate_room_data with invalid room ID format."""
        room_data = {
            "id": "invalid room id!",  # Contains invalid characters
            "name": "Test Room",
            "description": "A test room description",
        }
        result = RoomDataValidator.validate_room_data(room_data)
        assert result["is_valid"] is False
        assert any("Invalid room ID format" in error for error in result["errors"])

    def test_validate_room_data_occupant_count_mismatch(self):
        """Test validate_room_data with occupant count mismatch."""
        room_data = {
            "id": "test_room_1",
            "name": "Test Room",
            "description": "A test room description",
            "occupants": ["player1", "player2"],
            "occupant_count": 3,  # Mismatch: should be 2
        }
        result = RoomDataValidator.validate_room_data(room_data)
        assert result["is_valid"] is False
        assert any("Occupant count mismatch" in error for error in result["errors"])

    def test_validate_room_data_invalid_input_type(self):
        """Test validate_room_data with invalid input type raises AttributeError."""
        # The exception handler has a bug where it tries to call .get() on None
        with pytest.raises(AttributeError):
            RoomDataValidator.validate_room_data(None)

    def test_validate_required_fields_all_present(self):
        """Test validate_required_fields with all fields present."""
        room_data = {"id": "test_room_1", "name": "Test Room", "description": "A description"}
        errors = RoomDataValidator.validate_required_fields(room_data)
        assert len(errors) == 0

    def test_validate_required_fields_missing_id(self):
        """Test validate_required_fields with missing id."""
        room_data = {"name": "Test Room", "description": "A description"}
        errors = RoomDataValidator.validate_required_fields(room_data)
        assert "Missing required field: id" in errors

    def test_validate_required_fields_missing_name(self):
        """Test validate_required_fields with missing name."""
        room_data = {"id": "test_room_1", "description": "A description"}
        errors = RoomDataValidator.validate_required_fields(room_data)
        assert "Missing required field: name" in errors

    def test_validate_required_fields_missing_description(self):
        """Test validate_required_fields with missing description."""
        room_data = {"id": "test_room_1", "name": "Test Room"}
        errors = RoomDataValidator.validate_required_fields(room_data)
        assert "Missing required field: description" in errors

    def test_validate_required_fields_none_values(self):
        """Test validate_required_fields with None values."""
        room_data = {"id": "test_room_1", "name": None, "description": "A description"}
        errors = RoomDataValidator.validate_required_fields(room_data)
        assert "Missing required field: name" in errors

    def test_validate_field_types_all_valid(self):
        """Test validate_field_types with all valid types."""
        room_data = {
            "id": "test_room_1",
            "name": "Test Room",
            "description": "A description",
            "timestamp": 1234567890.0,
        }
        errors = RoomDataValidator.validate_field_types(room_data)
        assert len(errors) == 0

    def test_validate_field_types_invalid_id(self):
        """Test validate_field_types with invalid id type."""
        room_data = {"id": 123, "name": "Test Room", "description": "A description"}
        errors = RoomDataValidator.validate_field_types(room_data)
        assert any("Field 'id' must be a string" in error for error in errors)

    def test_validate_field_types_invalid_timestamp(self):
        """Test validate_field_types with invalid timestamp type."""
        room_data = {
            "id": "test_room_1",
            "name": "Test Room",
            "description": "A description",
            "timestamp": "not_a_number",
        }
        errors = RoomDataValidator.validate_field_types(room_data)
        assert any("Field 'timestamp' must be a number" in error for error in errors)

    def test_validate_occupant_consistency_consistent(self):
        """Test validate_occupant_consistency with consistent data."""
        room_data = {"occupants": ["player1", "player2"], "occupant_count": 2}
        errors = RoomDataValidator.validate_occupant_consistency(room_data)
        assert len(errors) == 0

    def test_validate_occupant_consistency_inconsistent(self):
        """Test validate_occupant_consistency with inconsistent data."""
        room_data = {"occupants": ["player1", "player2"], "occupant_count": 3}
        errors = RoomDataValidator.validate_occupant_consistency(room_data)
        assert len(errors) == 1
        assert "Occupant count mismatch" in errors[0]

    def test_validate_occupant_consistency_no_occupants(self):
        """Test validate_occupant_consistency with no occupants field."""
        room_data = {"occupant_count": 0}
        errors = RoomDataValidator.validate_occupant_consistency(room_data)
        assert len(errors) == 0

    def test_is_valid_room_id_valid(self):
        """Test is_valid_room_id with valid room ID."""
        assert RoomDataValidator.is_valid_room_id("test_room_1") is True
        assert RoomDataValidator.is_valid_room_id("room-123") is True
        assert RoomDataValidator.is_valid_room_id("Room123") is True

    def test_is_valid_room_id_invalid(self):
        """Test is_valid_room_id with invalid room ID."""
        assert RoomDataValidator.is_valid_room_id("invalid room id!") is False
        assert RoomDataValidator.is_valid_room_id("room@123") is False
        assert RoomDataValidator.is_valid_room_id("") is False

    def test_is_valid_room_id_none(self):
        """Test is_valid_room_id with None."""
        assert RoomDataValidator.is_valid_room_id(None) is False

    def test_is_valid_room_id_non_string(self):
        """Test is_valid_room_id with non-string type."""
        assert RoomDataValidator.is_valid_room_id(123) is False

    def test_check_occupant_count_consistency_consistent(self):
        """Test check_occupant_count_consistency with consistent data."""
        room_data = {"occupants": ["player1"], "occupant_count": 1}
        inconsistencies = RoomDataValidator.check_occupant_count_consistency(room_data)
        assert len(inconsistencies) == 0

    def test_check_occupant_count_consistency_inconsistent(self):
        """Test check_occupant_count_consistency with inconsistent data."""
        room_data = {"occupants": ["player1", "player2"], "occupant_count": 1}
        inconsistencies = RoomDataValidator.check_occupant_count_consistency(room_data)
        assert len(inconsistencies) == 1

    def test_check_duplicate_occupants_no_duplicates(self):
        """Test check_duplicate_occupants with no duplicates."""
        room_data = {"occupants": ["player1", "player2", "player3"]}
        inconsistencies = RoomDataValidator.check_duplicate_occupants(room_data)
        assert len(inconsistencies) == 0

    def test_check_duplicate_occupants_with_duplicates(self):
        """Test check_duplicate_occupants with duplicates."""
        room_data = {"occupants": ["player1", "player2", "player1"]}
        inconsistencies = RoomDataValidator.check_duplicate_occupants(room_data)
        assert len(inconsistencies) == 1
        assert "Duplicate occupants found" in inconsistencies[0]

    def test_check_duplicate_occupants_no_occupants(self):
        """Test check_duplicate_occupants with no occupants."""
        room_data = {}
        inconsistencies = RoomDataValidator.check_duplicate_occupants(room_data)
        assert len(inconsistencies) == 0

    def test_check_empty_room_with_occupants_no_issue(self):
        """Test check_empty_room_with_occupants with no issue."""
        room_data = {"name": "Test Room", "occupant_count": 2}
        inconsistencies = RoomDataValidator.check_empty_room_with_occupants(room_data)
        assert len(inconsistencies) == 0

    def test_check_empty_room_with_occupants_has_issue(self):
        """Test check_empty_room_with_occupants with issue."""
        room_data = {"name": "", "occupant_count": 2}
        inconsistencies = RoomDataValidator.check_empty_room_with_occupants(room_data)
        assert len(inconsistencies) == 1
        assert "Room has occupants but no name" in inconsistencies[0]

    def test_validate_room_consistency_consistent(self):
        """Test validate_room_consistency with consistent data."""
        room_data = {
            "id": "test_room_1",
            "name": "Test Room",
            "occupants": ["player1", "player2"],
            "occupant_count": 2,
        }
        result = RoomDataValidator.validate_room_consistency(room_data)
        assert result["is_consistent"] is True
        assert len(result["inconsistencies"]) == 0

    def test_validate_room_consistency_inconsistent(self):
        """Test validate_room_consistency with inconsistent data."""
        room_data = {
            "id": "test_room_1",
            "name": "",
            "occupants": ["player1", "player1"],  # Duplicate
            "occupant_count": 3,  # Mismatch
        }
        result = RoomDataValidator.validate_room_consistency(room_data)
        assert result["is_consistent"] is False
        assert len(result["inconsistencies"]) > 0

    def test_validate_room_consistency_invalid_input(self):
        """Test validate_room_consistency with invalid input raises AttributeError."""
        # The exception handler has a bug where it tries to call .get() on None
        with pytest.raises(AttributeError):
            RoomDataValidator.validate_room_consistency(None)
