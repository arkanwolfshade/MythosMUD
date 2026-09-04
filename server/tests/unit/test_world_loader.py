"""
Unit tests for world loader utility functions.

Tests room ID generation, environment determination, and validation functions.
"""

from typing import Any
from unittest.mock import MagicMock, Mock, patch

import pytest

from server.exceptions import ValidationError
from server.world_loader import (
    generate_room_id,
    get_room_environment,
    validate_room_data,
)


class TestGenerateRoomId:
    """Test generate_room_id() function."""

    def test_generate_room_id_basic(self):
        """Test generate_room_id() with basic components."""
        result = generate_room_id("earth", "arkhamcity", "french_hill", "S_Garrison_St_001")
        assert result == "earth_arkhamcity_french_hill_S_Garrison_St_001"

    def test_generate_room_id_with_underscores(self):
        """Test generate_room_id() handles components with underscores."""
        result = generate_room_id("earth", "arkham_city", "french_hill", "main_street")
        assert result == "earth_arkham_city_french_hill_main_street"

    def test_generate_room_id_empty_components(self):
        """Test generate_room_id() with empty components."""
        result = generate_room_id("", "zone", "subzone", "room")
        assert result == "_zone_subzone_room"

    def test_generate_room_id_special_characters(self):
        """Test generate_room_id() preserves special characters in components."""
        result = generate_room_id("plane-1", "zone-2", "sub-zone", "room_file")
        assert result == "plane-1_zone-2_sub-zone_room_file"


class TestGetRoomEnvironment:
    """Test get_room_environment() function."""

    def test_get_room_environment_from_room_data(self):
        """Test get_room_environment() returns room-specific environment."""
        room_data = {"environment": "indoors"}
        result = get_room_environment(room_data, None, None)
        assert result == "indoors"

    def test_get_room_environment_from_subzone(self):
        """Test get_room_environment() returns subzone environment when room doesn't have one."""
        room_data: dict[str, Any] = {}
        subzone_config: dict[str, Any] = {"environment": "outdoors"}
        result = get_room_environment(room_data, subzone_config, None)
        assert result == "outdoors"

    def test_get_room_environment_from_zone(self):
        """Test get_room_environment() returns zone environment when room and subzone don't have one."""
        room_data: dict[str, Any] = {}
        subzone_config: dict[str, Any] = {}
        zone_config = {"environment": "underwater"}
        result = get_room_environment(room_data, subzone_config, zone_config)
        assert result == "underwater"

    def test_get_room_environment_default(self):
        """Test get_room_environment() returns default 'outdoors' when no environment specified."""
        room_data: dict[str, Any] = {}
        result = get_room_environment(room_data, None, None)
        assert result == "outdoors"

    def test_get_room_environment_room_takes_priority(self):
        """Test get_room_environment() prioritizes room environment over subzone and zone."""
        room_data = {"environment": "indoors"}
        subzone_config = {"environment": "outdoors"}
        zone_config = {"environment": "underwater"}
        result = get_room_environment(room_data, subzone_config, zone_config)
        assert result == "indoors"

    def test_get_room_environment_subzone_takes_priority_over_zone(self):
        """Test get_room_environment() prioritizes subzone environment over zone."""
        room_data: dict[str, Any] = {}
        subzone_config = {"environment": "outdoors"}
        zone_config = {"environment": "underwater"}
        result = get_room_environment(room_data, subzone_config, zone_config)
        assert result == "outdoors"

    def test_get_room_environment_subzone_none(self):
        """Test get_room_environment() handles None subzone_config."""
        room_data: dict[str, Any] = {}
        zone_config = {"environment": "indoors"}
        result = get_room_environment(room_data, None, zone_config)
        assert result == "indoors"

    def test_get_room_environment_zone_none(self):
        """Test get_room_environment() handles None zone_config."""
        room_data: dict[str, Any] = {}
        subzone_config = {"environment": "outdoors"}
        result = get_room_environment(room_data, subzone_config, None)
        assert result == "outdoors"

    def test_get_room_environment_empty_string_in_room_data(self):
        """Test get_room_environment() treats empty string as no environment."""
        room_data = {"environment": ""}
        subzone_config = {"environment": "indoors"}
        result = get_room_environment(room_data, subzone_config, None)
        # Empty string should be falsy, so should use subzone
        assert result == "indoors"


class TestValidateRoomData:
    """Test validate_room_data() function."""

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", False)
    def test_validate_room_data_validation_not_available(self):
        """Test validate_room_data() returns empty list when validation not available."""
        room_data = {"name": "test room"}
        result = validate_room_data(room_data, "test.json")
        assert result == []

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True)
    @patch("server.world_loader.create_validator")
    def test_validate_room_data_with_validator(self, mock_create_validator):
        """Test validate_room_data() with provided validator."""
        mock_validator = MagicMock()
        mock_validator.validate_room = Mock(return_value=[])
        room_data = {"name": "test room"}
        result = validate_room_data(room_data, "test.json", validator=mock_validator)
        assert result == []
        mock_validator.validate_room.assert_called_once_with(room_data, "test.json")
        mock_create_validator.assert_not_called()

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True)
    @patch("server.world_loader.create_validator")
    def test_validate_room_data_creates_validator(self, mock_create_validator):
        """Test validate_room_data() creates validator when not provided."""
        mock_validator = MagicMock()
        mock_validator.validate_room = Mock(return_value=[])
        mock_create_validator.return_value = mock_validator
        room_data = {"name": "test room"}
        result = validate_room_data(room_data, "test.json")
        assert result == []
        mock_create_validator.assert_called_once_with("unified")
        mock_validator.validate_room.assert_called_once_with(room_data, "test.json")

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True)
    @patch("server.world_loader.create_validator")
    def test_validate_room_data_with_errors(self, mock_create_validator):
        """Test validate_room_data() returns validation errors."""
        mock_validator = MagicMock()
        mock_validator.validate_room = Mock(return_value=["Error 1", "Error 2"])
        mock_create_validator.return_value = mock_validator
        room_data = {"name": "test room"}
        result = validate_room_data(room_data, "test.json")
        assert result == ["Error 1", "Error 2"]

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True)
    @patch("server.world_loader.create_validator")
    def test_validate_room_data_strict_validation_raises(self, mock_create_validator):
        """Test validate_room_data() raises exception in strict mode with errors."""
        mock_validator = MagicMock()
        mock_validator.validate_room = Mock(return_value=["Error 1", "Error 2"])
        mock_create_validator.return_value = mock_validator
        room_data = {"name": "test room"}
        with pytest.raises(ValidationError):
            validate_room_data(room_data, "test.json", strict_validation=True)

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True)
    @patch("server.world_loader.create_validator")
    def test_validate_room_data_validator_creation_fails(self, mock_create_validator):
        """Test validate_room_data() returns empty list when validator creation fails."""
        mock_create_validator.side_effect = Exception("Failed to create validator")
        room_data = {"name": "test room"}
        result = validate_room_data(room_data, "test.json")
        assert result == []

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True)
    @patch("server.world_loader.create_validator")
    def test_validate_room_data_validation_exception(self, mock_create_validator):
        """Test validate_room_data() handles validation exception."""
        mock_validator = MagicMock()
        mock_validator.validate_room = Mock(side_effect=Exception("Validation error"))
        mock_create_validator.return_value = mock_validator
        room_data = {"name": "test room"}
        result = validate_room_data(room_data, "test.json", strict_validation=False)
        assert len(result) == 1
        assert "Validation error" in result[0]

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True)
    @patch("server.world_loader.create_validator")
    def test_validate_room_data_validation_exception_strict(self, mock_create_validator):
        """Test validate_room_data() raises in strict mode when validation exception occurs."""
        mock_validator = MagicMock()
        mock_validator.validate_room = Mock(side_effect=Exception("Validation error"))
        mock_create_validator.return_value = mock_validator
        room_data = {"name": "test room"}
        with pytest.raises(ValidationError):
            validate_room_data(room_data, "test.json", strict_validation=True)
