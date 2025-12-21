"""
Tests for World Loader utilities.

This module tests the world loading utility functions including room ID generation,
environment determination, and room data validation.

AI Agent: Tests for world loader utility functions covering room ID generation,
         environment inheritance, and schema validation with various configurations.
"""


# pylint: disable=redefined-outer-name
# Justification: pytest fixtures redefine names

from typing import Any
from unittest.mock import Mock, patch

from server.world_loader import (
    generate_room_id,
    get_room_environment,
    validate_room_data,
)


class TestGenerateRoomID:
    """Test room ID generation."""

    def test_generate_room_id_basic(self) -> None:
        """Test basic room ID generation."""
        room_id = generate_room_id("earth", "arkhamcity", "french_hill", "mansion_01")

        assert room_id == "earth_arkhamcity_french_hill_mansion_01"
        assert isinstance(room_id, str)

    def test_generate_room_id_with_underscores(self) -> None:
        """Test room ID generation preserves underscores in components."""
        room_id = generate_room_id("earth", "arkham_city", "north_side", "S_Garrison_St_001")

        assert room_id == "earth_arkham_city_north_side_S_Garrison_St_001"

    def test_generate_room_id_different_plane(self) -> None:
        """Test room ID generation with different planes."""
        room_id1 = generate_room_id("earth", "zone1", "subzone1", "room1")
        room_id2 = generate_room_id("yeng", "zone1", "subzone1", "room1")

        assert room_id1 != room_id2
        assert room_id1.startswith("earth_")
        assert room_id2.startswith("yeng_")


class TestGetRoomEnvironment:
    """Test room environment determination."""

    def test_room_specific_environment_takes_priority(self) -> None:
        """Test room-specific environment overrides zone and subzone."""
        room_data = {"environment": "underwater"}
        subzone_config = {"environment": "indoors"}
        zone_config = {"environment": "outdoors"}

        result = get_room_environment(room_data, subzone_config, zone_config)

        assert result == "underwater"

    def test_subzone_environment_when_room_not_specified(self) -> None:
        """Test subzone environment used when room doesn't specify."""
        room_data: dict[str, Any] = {}
        subzone_config = {"environment": "indoors"}
        zone_config = {"environment": "outdoors"}

        result = get_room_environment(room_data, subzone_config, zone_config)

        assert result == "indoors"

    def test_zone_environment_when_subzone_not_specified(self) -> None:
        """Test zone environment used when subzone doesn't specify."""
        room_data: dict[str, Any] = {}
        subzone_config: dict[str, Any] = {}
        zone_config = {"environment": "outdoors"}

        result = get_room_environment(room_data, subzone_config, zone_config)

        assert result == "outdoors"

    def test_default_environment_when_none_specified(self) -> None:
        """Test default 'outdoors' when no environment specified."""
        room_data: dict[str, Any] = {}
        subzone_config: dict[str, Any] = {}
        zone_config: dict[str, Any] = {}

        result = get_room_environment(room_data, subzone_config, zone_config)

        assert result == "outdoors"

    def test_handles_none_configs(self) -> None:
        """Test gracefully handles None configs."""
        room_data: dict[str, Any] = {}

        result = get_room_environment(room_data, None, None)

        assert result == "outdoors"

    def test_subzone_none_falls_back_to_zone(self) -> None:
        """Test None subzone config falls back to zone."""
        room_data: dict[str, Any] = {}
        zone_config = {"environment": "indoors"}

        result = get_room_environment(room_data, None, zone_config)

        assert result == "indoors"


class TestValidateRoomData:
    """Test room data validation."""

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", False)
    def test_validation_returns_empty_when_not_available(self) -> None:
        """Test validation returns empty list when schema validation not available."""
        room_data = {"name": "Test Room"}
        errors = validate_room_data(room_data, "test_room.json")

        assert not errors

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", False)
    def test_validation_skipped_when_not_available(self) -> None:
        """Test validation is skipped when not available."""
        room_data = {"name": "Test Room"}
        errors = validate_room_data(room_data, "test_room.json")

        assert not errors

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True)
    @patch("server.world_loader.create_validator")
    def test_validation_with_none_validator_attempts_creation(self, mock_create_validator) -> None:
        """Test validation attempts to create validator when None."""
        # Mock validator creation to return a validator
        mock_validator = Mock()
        mock_validator.validate_room.return_value = []
        mock_create_validator.return_value = mock_validator

        room_data = {"name": "Test Room"}

        # This should not raise even if validator creation fails
        errors = validate_room_data(room_data, "test_room.json", validator=None)

        assert isinstance(errors, list)
        mock_create_validator.assert_called_once()

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True)
    @patch("server.world_loader.create_validator")
    def test_validation_handles_validator_creation_error(self, mock_create_validator):
        """Test validation handles validator creation errors gracefully."""
        mock_create_validator.side_effect = Exception("Validator creation failed")

        room_data = {"name": "Test Room"}
        errors = validate_room_data(room_data, "test_room.json", validator=None, strict_validation=False)

        assert not errors

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True)
    def test_validation_with_mock_validator_success(self) -> None:
        """Test validation with mocked validator returning no errors."""
        mock_validator = Mock()
        mock_validator.validate_room.return_value = []

        room_data = {"name": "Test Room", "description": "A test room"}
        errors = validate_room_data(room_data, "test_room.json", validator=mock_validator)

        assert not errors
        mock_validator.validate_room.assert_called_once_with(room_data, "test_room.json")

    @patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True)
    def test_validation_with_mock_validator_errors(self) -> None:
        """Test validation with mocked validator returning errors."""
        mock_validator = Mock()
        mock_validator.validate_room.return_value = ["Missing required field: exits", "Invalid room type"]

        room_data = {"name": "Test Room"}
        errors = validate_room_data(room_data, "test_room.json", validator=mock_validator, strict_validation=False)

        assert len(errors) == 2
        assert "Missing required field: exits" in errors
        assert "Invalid room type" in errors
