"""
Unit tests for character creation service.

Tests the CharacterCreationService class for character creation and stats generation.
"""

import uuid
from unittest.mock import MagicMock

import pytest
from pydantic import ValidationError as PydanticValidationError

from server.exceptions import ValidationError
from server.game.character_creation_service import CharacterCreationService
from server.models import Stats

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_player_service():
    """Create a mock player service."""
    return MagicMock()


@pytest.fixture
def character_creation_service(mock_player_service):
    """Create a CharacterCreationService instance."""
    return CharacterCreationService(mock_player_service)


@pytest.fixture
def sample_stats():
    """Create sample stats dictionary."""
    return {
        "strength": 12,
        "dexterity": 14,
        "constitution": 13,
        "intelligence": 15,
        "wisdom": 11,
        "charisma": 10,
    }


def test_character_creation_service_init(mock_player_service):
    """Test CharacterCreationService initialization."""
    service = CharacterCreationService(mock_player_service)
    assert service.player_service == mock_player_service
    assert service.stats_generator is not None


def test_roll_character_stats_with_profession(character_creation_service):
    """Test roll_character_stats() with profession_id."""
    mock_stats = MagicMock(spec=Stats)
    mock_stats.model_dump.return_value = {"strength": 12}
    mock_stat_summary = {"total": 75}
    character_creation_service.stats_generator.roll_stats_with_profession = MagicMock(return_value=(mock_stats, True))
    character_creation_service.stats_generator.get_stat_summary = MagicMock(return_value=mock_stat_summary)

    result = character_creation_service.roll_character_stats(method="3d6", profession_id=1)

    assert "stats" in result
    assert "stat_summary" in result
    assert result["profession_id"] == 1
    assert result["meets_requirements"] is True
    assert result["method_used"] == "3d6"


def test_roll_character_stats_with_class(character_creation_service):
    """Test roll_character_stats() with required_class."""
    mock_stats = MagicMock(spec=Stats)
    mock_stats.model_dump.return_value = {"strength": 12}
    mock_stat_summary = {"total": 75}
    character_creation_service.stats_generator.roll_stats_with_validation = MagicMock(
        return_value=(mock_stats, ["investigator", "detective"])
    )
    character_creation_service.stats_generator.get_stat_summary = MagicMock(return_value=mock_stat_summary)

    result = character_creation_service.roll_character_stats(method="3d6", required_class="investigator")

    assert "stats" in result
    assert "stat_summary" in result
    assert "available_classes" in result
    assert result["meets_class_requirements"] is True
    assert result["method_used"] == "3d6"


def test_roll_character_stats_without_class_or_profession(character_creation_service):
    """Test roll_character_stats() without class or profession."""
    mock_stats = MagicMock(spec=Stats)
    mock_stats.model_dump.return_value = {"strength": 12}
    mock_stat_summary = {"total": 75}
    character_creation_service.stats_generator.roll_stats_with_validation = MagicMock(
        return_value=(mock_stats, ["investigator", "detective"])
    )
    character_creation_service.stats_generator.get_stat_summary = MagicMock(return_value=mock_stat_summary)

    result = character_creation_service.roll_character_stats(method="3d6")

    assert "stats" in result
    assert "available_classes" in result
    assert result["meets_class_requirements"] is True


def test_roll_character_stats_class_not_available(character_creation_service):
    """Test roll_character_stats() when required_class is not available."""
    mock_stats = MagicMock(spec=Stats)
    mock_stats.model_dump.return_value = {"strength": 12}
    mock_stat_summary = {"total": 75}
    character_creation_service.stats_generator.roll_stats_with_validation = MagicMock(
        return_value=(mock_stats, ["investigator"])  # detective not available
    )
    character_creation_service.stats_generator.get_stat_summary = MagicMock(return_value=mock_stat_summary)

    result = character_creation_service.roll_character_stats(method="3d6", required_class="detective")

    assert result["meets_class_requirements"] is False


def test_roll_character_stats_value_error(character_creation_service):
    """Test roll_character_stats() handles ValueError."""
    character_creation_service.stats_generator.roll_stats_with_profession = MagicMock(
        side_effect=ValueError("Invalid profession")
    )

    with pytest.raises(ValidationError):
        character_creation_service.roll_character_stats(method="3d6", profession_id=999)


def test_validate_character_stats_with_class(character_creation_service, sample_stats):
    """Test validate_character_stats() with class_name."""
    character_creation_service.stats_generator.validate_class_prerequisites = MagicMock(return_value=(True, []))
    character_creation_service.stats_generator.get_available_classes = MagicMock(
        return_value=["investigator", "detective"]
    )

    result = character_creation_service.validate_character_stats(sample_stats, class_name="investigator")

    assert "meets_prerequisites" in result
    assert result["meets_prerequisites"] is True
    assert "available_classes" in result
    assert "requested_class" in result
    assert result["requested_class"] == "investigator"


def test_validate_character_stats_without_class(character_creation_service, sample_stats):
    """Test validate_character_stats() without class_name."""
    mock_stat_summary = {"total": 75}
    character_creation_service.stats_generator.get_available_classes = MagicMock(
        return_value=["investigator", "detective"]
    )
    character_creation_service.stats_generator.get_stat_summary = MagicMock(return_value=mock_stat_summary)

    result = character_creation_service.validate_character_stats(sample_stats)

    assert "available_classes" in result
    assert "stat_summary" in result
    assert "meets_prerequisites" not in result


def test_validate_character_stats_invalid_format(character_creation_service):
    """Test validate_character_stats() handles invalid stats format."""
    # Stats model has extra="ignore" and optional fields, so it's lenient
    # Test with a type that Pydantic will actually reject (list for int field)
    invalid_stats = {"strength": [1, 2, 3]}  # Invalid type (list instead of int)

    # Pydantic should reject list for int field
    with pytest.raises((ValidationError, PydanticValidationError, TypeError)):
        character_creation_service.validate_character_stats(invalid_stats)


def test_validate_character_stats_value_error(character_creation_service, sample_stats):
    """Test validate_character_stats() handles ValueError from stats_generator."""
    character_creation_service.stats_generator.validate_class_prerequisites = MagicMock(
        side_effect=ValueError("Invalid class")
    )

    with pytest.raises(ValidationError):
        character_creation_service.validate_character_stats(sample_stats, class_name="invalid_class")


def test_create_character_with_stats_success(character_creation_service, sample_stats):
    """Test create_character_with_stats() successfully creates character."""
    mock_player = MagicMock()
    mock_player.id = uuid.uuid4()
    mock_player.model_dump.return_value = {"id": str(mock_player.id), "name": "TestCharacter"}
    character_creation_service.player_service.create_player_with_stats = MagicMock(return_value=mock_player)

    result = character_creation_service.create_character_with_stats(
        name="TestCharacter", stats=sample_stats, profession_id=1
    )

    assert "message" in result
    assert "player" in result
    assert "stats" in result
    assert "TestCharacter" in result["message"]
    character_creation_service.player_service.create_player_with_stats.assert_called_once()


def test_create_character_with_stats_with_user_id(character_creation_service, sample_stats):
    """Test create_character_with_stats() with user_id."""
    user_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_player.id = uuid.uuid4()
    mock_player.model_dump.return_value = {"id": str(mock_player.id), "name": "TestCharacter"}
    character_creation_service.player_service.create_player_with_stats = MagicMock(return_value=mock_player)

    result = character_creation_service.create_character_with_stats(
        name="TestCharacter", stats=sample_stats, user_id=user_id
    )

    assert result is not None
    call_args = character_creation_service.player_service.create_player_with_stats.call_args
    assert call_args[1]["user_id"] == user_id


def test_create_character_with_stats_custom_starting_room(character_creation_service, sample_stats):
    """Test create_character_with_stats() with custom starting_room_id."""
    mock_player = MagicMock()
    mock_player.id = uuid.uuid4()
    mock_player.model_dump.return_value = {"id": str(mock_player.id), "name": "TestCharacter"}
    character_creation_service.player_service.create_player_with_stats = MagicMock(return_value=mock_player)

    custom_room = "earth_arkhamcity_downtown_market_square"
    result = character_creation_service.create_character_with_stats(
        name="TestCharacter", stats=sample_stats, starting_room_id=custom_room
    )

    assert result is not None
    call_args = character_creation_service.player_service.create_player_with_stats.call_args
    assert call_args[1]["starting_room_id"] == custom_room


def test_create_character_with_stats_validation_error(character_creation_service, sample_stats):
    """Test create_character_with_stats() handles ValidationError."""
    character_creation_service.player_service.create_player_with_stats = MagicMock(
        side_effect=ValidationError("Invalid name")
    )

    with pytest.raises(ValidationError):
        character_creation_service.create_character_with_stats(name="TestCharacter", stats=sample_stats)


def test_create_character_with_stats_pydantic_error(character_creation_service):
    """Test create_character_with_stats() handles PydanticValidationError."""
    # Stats model has extra="ignore" and optional fields, so it's lenient
    # Use a type that Pydantic will actually reject (e.g., list instead of int)
    invalid_stats = {"strength": [1, 2, 3]}  # Invalid type (list instead of int)

    with pytest.raises((ValidationError, PydanticValidationError)):
        character_creation_service.create_character_with_stats(name="TestCharacter", stats=invalid_stats)


def test_create_character_with_stats_value_error(character_creation_service, sample_stats):
    """Test create_character_with_stats() handles ValueError."""
    character_creation_service.player_service.create_player_with_stats = MagicMock(
        side_effect=ValueError("Invalid parameters")
    )

    with pytest.raises(ValidationError):
        character_creation_service.create_character_with_stats(name="TestCharacter", stats=sample_stats)


def test_get_available_classes_info(character_creation_service):
    """Test get_available_classes_info() returns class information."""
    result = character_creation_service.get_available_classes_info()

    assert "classes" in result
    assert "stat_range" in result
    assert "min" in result["stat_range"]
    assert "max" in result["stat_range"]
    assert isinstance(result["classes"], dict)


def test_get_class_description_known_class(character_creation_service):
    """Test _get_class_description() returns description for known class."""
    description = character_creation_service._get_class_description("investigator")
    assert "investigator" in description.lower() or "detective" in description.lower()
    assert len(description) > 0


def test_get_class_description_unknown_class(character_creation_service):
    """Test _get_class_description() returns default for unknown class."""
    description = character_creation_service._get_class_description("unknown_class")
    assert "mysterious" in description.lower() or "unknown" in description.lower()


def test_get_class_description_all_classes(character_creation_service):
    """Test _get_class_description() works for all known classes."""
    known_classes = ["investigator", "occultist", "survivor", "cultist", "academic", "detective"]
    for class_name in known_classes:
        description = character_creation_service._get_class_description(class_name)
        assert len(description) > 0
        assert "mysterious" not in description.lower()  # Should not be default


def test_roll_character_stats_profession_meets_requirements_false(character_creation_service):
    """Test roll_character_stats() when profession requirements not met."""
    mock_stats = MagicMock(spec=Stats)
    mock_stats.model_dump.return_value = {"strength": 12}
    mock_stat_summary = {"total": 75}
    character_creation_service.stats_generator.roll_stats_with_profession = MagicMock(
        return_value=(mock_stats, False)  # Does not meet requirements
    )
    character_creation_service.stats_generator.get_stat_summary = MagicMock(return_value=mock_stat_summary)

    result = character_creation_service.roll_character_stats(method="3d6", profession_id=1)

    assert result["meets_requirements"] is False


def test_validate_character_stats_failed_prerequisites(character_creation_service, sample_stats):
    """Test validate_character_stats() when prerequisites not met."""
    failed_requirements = ["strength >= 15"]
    character_creation_service.stats_generator.validate_class_prerequisites = MagicMock(
        return_value=(False, failed_requirements)
    )
    character_creation_service.stats_generator.get_available_classes = MagicMock(return_value=["investigator"])

    result = character_creation_service.validate_character_stats(sample_stats, class_name="occultist")

    assert result["meets_prerequisites"] is False
    assert result["failed_requirements"] == failed_requirements
