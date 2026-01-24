"""
Unit tests for room_data_validator.

Tests the RoomDataValidator class methods.
"""

from server.services.room_data_validator import RoomDataValidator


def test_validate_required_fields():
    """Test validate_required_fields() detects missing fields."""
    room_data = {"id": "room_001"}
    errors = RoomDataValidator.validate_required_fields(room_data)
    assert len(errors) > 0
    assert any("name" in error.lower() for error in errors)


def test_validate_required_fields_all_present():
    """Test validate_required_fields() passes when all fields present."""
    room_data = {"id": "room_001", "name": "Test Room", "description": "A test room"}
    errors = RoomDataValidator.validate_required_fields(room_data)
    assert len(errors) == 0


def test_validate_field_types():
    """Test validate_field_types() detects type mismatches."""
    room_data = {"id": 123, "name": "Test Room", "description": "A test room"}
    errors = RoomDataValidator.validate_field_types(room_data)
    assert len(errors) > 0
    assert any("id" in error.lower() and "string" in error.lower() for error in errors)


def test_validate_field_types_valid():
    """Test validate_field_types() passes with correct types."""
    room_data = {"id": "room_001", "name": "Test Room", "description": "A test room", "timestamp": 1234567890}
    errors = RoomDataValidator.validate_field_types(room_data)
    assert len(errors) == 0


def test_validate_room_data_valid():
    """Test validate_room_data() returns is_valid=True for valid data."""
    room_data = {"id": "room_001", "name": "Test Room", "description": "A test room"}
    result = RoomDataValidator.validate_room_data(room_data)
    assert result["is_valid"] is True
    assert len(result["errors"]) == 0


def test_validate_room_data_invalid():
    """Test validate_room_data() returns is_valid=False for invalid data."""
    room_data = {"id": "room_001"}  # Missing required fields
    result = RoomDataValidator.validate_room_data(room_data)
    assert result["is_valid"] is False
    assert len(result["errors"]) > 0


def test_validate_room_data_room_id():
    """Test validate_room_data() includes room_id in result."""
    room_data = {"id": "room_001", "name": "Test Room", "description": "A test room"}
    result = RoomDataValidator.validate_room_data(room_data)
    assert result["room_id"] == "room_001"


def test_is_valid_room_id():
    """Test is_valid_room_id() validates room ID format."""
    assert RoomDataValidator.is_valid_room_id("earth_arkhamcity_northside_intersection_derby_high") is True
    assert RoomDataValidator.is_valid_room_id("room_001") is True
    assert RoomDataValidator.is_valid_room_id("invalid room") is False  # Contains space
    assert RoomDataValidator.is_valid_room_id("") is False
    # Reason: Intentionally passing None to test error handling
    assert RoomDataValidator.is_valid_room_id(None) is False  # type: ignore[arg-type]


def test_check_occupant_count_consistency():
    """Test check_occupant_count_consistency() detects mismatches."""
    room_data = {"occupants": ["player1", "player2"], "occupant_count": 1}
    inconsistencies = RoomDataValidator.check_occupant_count_consistency(room_data)
    assert len(inconsistencies) > 0


def test_check_duplicate_occupants():
    """Test check_duplicate_occupants() detects duplicates."""
    room_data = {"occupants": ["player1", "player2", "player1"]}
    inconsistencies = RoomDataValidator.check_duplicate_occupants(room_data)
    assert len(inconsistencies) > 0


def test_check_duplicate_occupants_no_duplicates():
    """Test check_duplicate_occupants() passes when no duplicates."""
    room_data = {"occupants": ["player1", "player2"]}
    inconsistencies = RoomDataValidator.check_duplicate_occupants(room_data)
    assert len(inconsistencies) == 0


def test_check_empty_room_with_occupants():
    """Test check_empty_room_with_occupants() detects empty room with occupants."""
    room_data = {"name": "", "occupant_count": 2}
    inconsistencies = RoomDataValidator.check_empty_room_with_occupants(room_data)
    assert len(inconsistencies) > 0


def test_validate_room_consistency():
    """Test validate_room_consistency() validates room consistency."""
    room_data = {
        "id": "room_001",
        "name": "Test Room",
        "description": "A test room",
        "occupants": ["player1", "player2"],
        "occupant_count": 2,
    }
    result = RoomDataValidator.validate_room_consistency(room_data)
    assert result["is_consistent"] is True
    assert len(result["inconsistencies"]) == 0
