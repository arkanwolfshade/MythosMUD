"""
Tests for CharacterCreationService layer implementation.

This module tests the CharacterCreationService to ensure proper business logic
separation and service layer functionality.
"""

import uuid
from unittest.mock import Mock

import pytest

from server.exceptions import ValidationError as CustomValidationError
from server.game.character_creation_service import CharacterCreationService
from server.models import AttributeType, Stats


class TestCharacterCreationServiceLayer:
    """Test the CharacterCreationService layer functionality."""

    mock_player_service: Mock
    character_creation_service: CharacterCreationService

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.mock_player_service = Mock()
        self.character_creation_service = CharacterCreationService(self.mock_player_service)

    def test_character_creation_service_initialization(self) -> None:
        """Test that CharacterCreationService initializes correctly."""
        assert self.character_creation_service.player_service == self.mock_player_service
        assert self.character_creation_service.stats_generator is not None

    def test_roll_character_stats_with_profession_success(self) -> None:
        """Test successful stats rolling with profession."""
        # Mock stats generator
        mock_stats = Stats(strength=15, dexterity=12, constitution=14, intelligence=13, wisdom=11, charisma=10)
        self.character_creation_service.stats_generator.roll_stats_with_profession = Mock(  # type: ignore
            return_value=(mock_stats, True)
        )
        self.character_creation_service.stats_generator.get_stat_summary = Mock(return_value={"total": 75})  # type: ignore

        # Roll stats with profession
        result = self.character_creation_service.roll_character_stats(method="3d6", profession_id=1, max_attempts=10)

        # Verify result
        assert isinstance(result, dict)
        assert "stats" in result
        assert "stat_summary" in result
        assert "profession_id" in result
        assert "meets_requirements" in result
        assert "method_used" in result
        assert result["profession_id"] == 1
        assert result["meets_requirements"] is True
        assert result["method_used"] == "3d6"

        # Verify stats generator calls
        self.character_creation_service.stats_generator.roll_stats_with_profession.assert_called_once_with(
            method="3d6", profession_id=1, max_attempts=10, timeout_seconds=5.0
        )

    def test_roll_character_stats_with_class_success(self) -> None:
        """Test successful stats rolling with class validation."""
        # Mock stats generator
        mock_stats = Stats(strength=15, dexterity=12, constitution=14, intelligence=13, wisdom=11, charisma=10)
        self.character_creation_service.stats_generator.roll_stats_with_validation = Mock(  # type: ignore
            return_value=(mock_stats, ["investigator", "detective"])
        )
        self.character_creation_service.stats_generator.get_stat_summary = Mock(return_value={"total": 75})  # type: ignore

        # Roll stats with class
        result = self.character_creation_service.roll_character_stats(
            method="3d6", required_class="investigator", max_attempts=10
        )

        # Verify result
        assert isinstance(result, dict)
        assert "stats" in result
        assert "stat_summary" in result
        assert "available_classes" in result
        assert "method_used" in result
        assert "meets_class_requirements" in result
        assert result["available_classes"] == ["investigator", "detective"]
        assert result["meets_class_requirements"] is True
        assert result["method_used"] == "3d6"

        # Verify stats generator calls
        self.character_creation_service.stats_generator.roll_stats_with_validation.assert_called_once_with(
            method="3d6", required_class="investigator", max_attempts=10
        )

    def test_roll_character_stats_invalid_profession(self) -> None:
        """Test stats rolling with invalid profession ID."""
        # Mock stats generator to raise ValueError
        self.character_creation_service.stats_generator.roll_stats_with_profession = Mock(  # type: ignore
            side_effect=ValueError("Invalid profession ID")
        )

        # Attempt to roll stats with invalid profession
        with pytest.raises(CustomValidationError) as exc_info:
            self.character_creation_service.roll_character_stats(profession_id=999)

        assert "Invalid profession: Invalid profession ID" in str(exc_info.value)

    def test_validate_character_stats_with_class_success(self) -> None:
        """Test successful stats validation with class."""
        # Mock stats generator
        self.character_creation_service.stats_generator.validate_class_prerequisites = Mock(return_value=(True, []))  # type: ignore
        self.character_creation_service.stats_generator.get_available_classes = Mock(  # type: ignore
            return_value=["investigator", "detective"]
        )

        # Validate stats with class
        stats_dict = {
            "strength": 15,
            "dexterity": 12,
            "constitution": 14,
            "intelligence": 13,
            "wisdom": 11,
            "charisma": 10,
        }
        result = self.character_creation_service.validate_character_stats(stats_dict, "investigator")

        # Verify result
        assert isinstance(result, dict)
        assert "meets_prerequisites" in result
        assert "failed_requirements" in result
        assert "available_classes" in result
        assert "requested_class" in result
        assert result["meets_prerequisites"] is True
        assert result["failed_requirements"] == []
        assert result["available_classes"] == ["investigator", "detective"]
        assert result["requested_class"] == "investigator"

    def test_validate_character_stats_without_class_success(self) -> None:
        """Test successful stats validation without class."""
        # Mock stats generator
        self.character_creation_service.stats_generator.get_available_classes = Mock(  # type: ignore
            return_value=["investigator", "detective"]
        )
        self.character_creation_service.stats_generator.get_stat_summary = Mock(return_value={"total": 75})  # type: ignore

        # Validate stats without class
        stats_dict = {
            "strength": 15,
            "dexterity": 12,
            "constitution": 14,
            "intelligence": 13,
            "wisdom": 11,
            "charisma": 10,
        }
        result = self.character_creation_service.validate_character_stats(stats_dict)

        # Verify result
        assert isinstance(result, dict)
        assert "available_classes" in result
        assert "stat_summary" in result
        assert result["available_classes"] == ["investigator", "detective"]
        assert result["stat_summary"] == {"total": 75}

    def test_validate_character_stats_invalid_format(self) -> None:
        """Test stats validation with invalid stats format."""
        # Mock stats generator to raise ValueError (which is caught)
        self.character_creation_service.stats_generator.get_available_classes = Mock(  # type: ignore
            side_effect=ValueError("Invalid stats format")
        )

        # Attempt to validate invalid stats
        with pytest.raises(CustomValidationError) as exc_info:
            self.character_creation_service.validate_character_stats({"invalid": "stats"})

        assert "Invalid stats format" in str(exc_info.value)

    def test_create_character_with_stats_success(self) -> None:
        """Test successful character creation with stats."""
        # Mock player service
        mock_player = Mock()
        mock_player.id = uuid.uuid4()
        mock_player.model_dump.return_value = {"id": str(mock_player.id), "name": "TestPlayer"}
        self.mock_player_service.create_player_with_stats.return_value = mock_player

        # Create character with stats
        stats_dict = {
            "strength": 15,
            "dexterity": 12,
            "constitution": 14,
            "intelligence": 13,
            "wisdom": 11,
            "charisma": 10,
        }
        result = self.character_creation_service.create_character_with_stats(
            name="TestPlayer",
            stats=stats_dict,
            profession_id=1,
            starting_room_id="test_room",
            user_id=uuid.uuid4(),
        )

        # Verify result
        assert isinstance(result, dict)
        assert "message" in result
        assert "player" in result
        assert "stats" in result
        assert "Character TestPlayer created successfully" in result["message"]

        # Verify player service calls
        self.mock_player_service.create_player_with_stats.assert_called_once()

    def test_create_character_with_stats_failure(self) -> None:
        """Test character creation failure."""
        # Mock player service to raise ValueError (which is caught)
        self.mock_player_service.create_player_with_stats = Mock(side_effect=ValueError("Player creation failed"))

        # Attempt to create character
        stats_dict = {
            "strength": 15,
            "dexterity": 12,
            "constitution": 14,
            "intelligence": 13,
            "wisdom": 11,
            "charisma": 10,
        }
        with pytest.raises(CustomValidationError) as exc_info:
            self.character_creation_service.create_character_with_stats(
                name="TestPlayer",
                stats=stats_dict,
                profession_id=1,
            )

        assert "Character creation failed" in str(exc_info.value)

    def test_get_available_classes_info_success(self) -> None:
        """Test successful retrieval of available classes information."""
        # Mock the method directly instead of trying to mock the class attributes
        self.character_creation_service.stats_generator.CLASS_PREREQUISITES = {
            "investigator": {AttributeType.STR: 12, AttributeType.INT: 13},
            "detective": {AttributeType.INT: 14, AttributeType.POW: 12},
        }
        self.character_creation_service.stats_generator.MIN_STAT = 3
        self.character_creation_service.stats_generator.MAX_STAT = 18

        # Mock the _get_class_description method to avoid the AttributeError
        original_method = self.character_creation_service._get_class_description
        self.character_creation_service._get_class_description = Mock(return_value="Test description")  # type: ignore

        try:
            # Get available classes info
            result = self.character_creation_service.get_available_classes_info()

            # Verify result
            assert isinstance(result, dict)
            assert "classes" in result
            assert "stat_range" in result
            assert "investigator" in result["classes"]
            assert "detective" in result["classes"]
            assert result["stat_range"]["min"] == 3
            assert result["stat_range"]["max"] == 18

            # Verify class information structure
            investigator_info = result["classes"]["investigator"]
            assert "prerequisites" in investigator_info
            assert "description" in investigator_info
            assert investigator_info["description"] == "Test description"
        finally:
            # Restore the original method
            self.character_creation_service._get_class_description = original_method  # type: ignore

    def test_get_class_description_known_class(self) -> None:
        """Test getting description for a known class."""
        description = self.character_creation_service._get_class_description("investigator")
        assert "researcher and detective" in description

    def test_get_class_description_unknown_class(self) -> None:
        """Test getting description for an unknown class."""
        description = self.character_creation_service._get_class_description("unknown_class")
        assert "mysterious character with unknown capabilities" in description

    def test_get_available_classes_info_with_string_prerequisites(self) -> None:
        """Test getting available classes info when prerequisites use string keys.

        AI: Tests the else branch (line 232 in character_creation_service.py) where
        prerequisite keys don't have a .value attribute and need to be converted to
        strings. This covers the fallback path for non-enum prerequisite keys.
        """
        # Mock CLASS_PREREQUISITES with string keys instead of enums
        from unittest.mock import patch

        string_prerequisites = {
            "test_class": {
                "strength": 12,  # String key, not an enum
                "intelligence": 10,
            }
        }

        with patch.object(self.character_creation_service.stats_generator, "CLASS_PREREQUISITES", string_prerequisites):
            result = self.character_creation_service.get_available_classes_info()

            assert isinstance(result, dict)
            assert "classes" in result
            assert "test_class" in result["classes"]
            # Verify the string keys were properly converted
            assert "strength" in result["classes"]["test_class"]["prerequisites"]
            assert result["classes"]["test_class"]["prerequisites"]["strength"] == 12
