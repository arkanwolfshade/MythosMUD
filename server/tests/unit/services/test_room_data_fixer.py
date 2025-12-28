"""
Unit tests for room data fixer.

Tests the RoomDataFixer class for applying automatic fixes to room data.
"""

import time
from unittest.mock import patch

import pytest

from server.services.room_data_fixer import RoomDataFixer


class TestRoomDataFixer:
    """Test suite for RoomDataFixer class."""

    def test_fix_missing_name(self):
        """Test fix_missing_name adds default name."""
        fixed_data = {"id": "test_room_1"}
        errors = ["Missing required field: name"]
        RoomDataFixer.fix_missing_name(fixed_data, errors)
        assert fixed_data["name"] == "Room test_room_1"

    def test_fix_missing_name_no_error(self):
        """Test fix_missing_name does nothing when no error."""
        fixed_data = {"id": "test_room_1", "name": "Existing Name"}
        errors = []
        RoomDataFixer.fix_missing_name(fixed_data, errors)
        assert fixed_data["name"] == "Existing Name"

    def test_fix_missing_name_unknown_id(self):
        """Test fix_missing_name with unknown ID."""
        fixed_data = {}
        errors = ["Missing required field: name"]
        RoomDataFixer.fix_missing_name(fixed_data, errors)
        assert fixed_data["name"] == "Room unknown"

    def test_fix_missing_description(self):
        """Test fix_missing_description adds default description."""
        fixed_data = {"id": "test_room_1"}
        errors = ["Missing required field: description"]
        RoomDataFixer.fix_missing_description(fixed_data, errors)
        assert fixed_data["description"] == "No description available"

    def test_fix_missing_description_no_error(self):
        """Test fix_missing_description does nothing when no error."""
        fixed_data = {"id": "test_room_1", "description": "Existing Description"}
        errors = []
        RoomDataFixer.fix_missing_description(fixed_data, errors)
        assert fixed_data["description"] == "Existing Description"

    def test_fix_occupant_count_mismatch(self):
        """Test fix_occupant_count_mismatch fixes count."""
        fixed_data = {"occupants": ["player1", "player2", "player3"]}
        errors = ["Occupant count mismatch: expected 3, got 5"]
        RoomDataFixer.fix_occupant_count_mismatch(fixed_data, errors)
        assert fixed_data["occupant_count"] == 3

    def test_fix_occupant_count_mismatch_no_error(self):
        """Test fix_occupant_count_mismatch does nothing when no error."""
        fixed_data = {"occupants": ["player1"], "occupant_count": 1}
        errors = []
        RoomDataFixer.fix_occupant_count_mismatch(fixed_data, errors)
        assert fixed_data["occupant_count"] == 1

    def test_fix_occupant_count_mismatch_no_occupants(self):
        """Test fix_occupant_count_mismatch with no occupants field."""
        fixed_data = {}
        errors = ["Occupant count mismatch: expected 0, got 1"]
        RoomDataFixer.fix_occupant_count_mismatch(fixed_data, errors)
        assert "occupant_count" not in fixed_data

    def test_fix_missing_timestamp(self):
        """Test fix_missing_timestamp adds timestamp."""
        with patch("time.time", return_value=1234567890.0):
            fixed_data = {}
            RoomDataFixer.fix_missing_timestamp(fixed_data)
            assert fixed_data["timestamp"] == 1234567890.0

    def test_fix_missing_timestamp_existing(self):
        """Test fix_missing_timestamp does nothing when timestamp exists."""
        fixed_data = {"timestamp": 1234567890.0}
        RoomDataFixer.fix_missing_timestamp(fixed_data)
        assert fixed_data["timestamp"] == 1234567890.0

    def test_count_applied_fixes(self):
        """Test count_applied_fixes counts fixable errors."""
        errors = [
            "Missing required field: name",
            "Missing required field: description",
            "Occupant count mismatch: expected 2, got 3",
            "Some other error",
        ]
        count = RoomDataFixer.count_applied_fixes(errors)
        assert count == 3  # Three fixable errors

    def test_count_applied_fixes_no_fixable(self):
        """Test count_applied_fixes with no fixable errors."""
        errors = ["Some other error", "Another error"]
        count = RoomDataFixer.count_applied_fixes(errors)
        assert count == 0

    def test_apply_room_data_fixes_all_fixes(self):
        """Test apply_room_data_fixes applies all fixes."""
        with patch("time.time", return_value=1234567890.0):
            room_data = {"id": "test_room_1", "occupants": ["player1", "player2"]}
            errors = [
                "Missing required field: name",
                "Missing required field: description",
                "Occupant count mismatch: expected 2, got 3",
            ]
            fixed = RoomDataFixer.apply_room_data_fixes(room_data, errors)
            assert fixed["name"] == "Room test_room_1"
            assert fixed["description"] == "No description available"
            assert fixed["occupant_count"] == 2
            assert fixed["timestamp"] == 1234567890.0

    def test_apply_room_data_fixes_no_errors(self):
        """Test apply_room_data_fixes with no errors."""
        with patch("time.time", return_value=1234567890.0):
            room_data = {"id": "test_room_1", "name": "Test Room", "description": "A description"}
            errors = []
            fixed = RoomDataFixer.apply_room_data_fixes(room_data, errors)
            assert fixed["name"] == "Test Room"
            assert fixed["description"] == "A description"
            assert fixed["timestamp"] == 1234567890.0  # Timestamp always added

    def test_apply_room_data_fixes_preserves_original(self):
        """Test apply_room_data_fixes does not modify original data."""
        room_data = {"id": "test_room_1"}
        errors = ["Missing required field: name"]
        fixed = RoomDataFixer.apply_room_data_fixes(room_data, errors)
        assert "name" not in room_data  # Original not modified
        assert "name" in fixed  # Fixed copy has name

    def test_apply_room_data_fixes_invalid_input(self):
        """Test apply_room_data_fixes handles invalid input."""
        result = RoomDataFixer.apply_room_data_fixes(None, [])
        assert result is None

    def test_apply_room_data_fixes_exception_handling(self):
        """Test apply_room_data_fixes handles exceptions."""
        room_data = {"id": "test_room_1"}
        errors = ["Missing required field: name"]
        # Simulate an error during fixing
        with patch.object(RoomDataFixer, "fix_missing_name", side_effect=AttributeError("Test error")):
            result = RoomDataFixer.apply_room_data_fixes(room_data, errors)
            # Should return original data on error
            assert result == room_data
