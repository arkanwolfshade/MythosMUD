"""
Tests for the players API endpoints.

This module tests all player-related API operations including
creation, retrieval, listing, deletion, and effects application.
Following the academic rigor outlined in the Pnakotic Manuscripts of Testing Methodology.
"""

import uuid
from datetime import datetime
from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from server.api.players import (
    CreateCharacterRequest,
    apply_corruption,
    apply_fear,
    apply_sanity_loss,
    create_character_with_stats,
    create_player,
    damage_player,
    delete_player,
    gain_occult_knowledge,
    get_available_classes,
    get_class_description,
    get_player,
    get_player_by_name,
    heal_player,
    list_players,
    roll_character_stats,
    validate_character_stats,
)
from server.exceptions import RateLimitError, ValidationError, create_error_context
from server.game.stats_generator import StatsGenerator
from server.models import AttributeType, Stats


@pytest.fixture
def mock_current_user():
    """Mock authenticated user for testing."""
    user = Mock()
    user.id = str(uuid.uuid4())
    user.username = "testuser"
    # Make the mock support dictionary access for all attributes
    user.__getitem__ = lambda self, key: getattr(self, key)
    return user


@pytest.fixture
def sample_player_data():
    """Sample player data for testing."""
    player = Mock()
    player.player_id = str(uuid.uuid4())
    player.user_id = str(uuid.uuid4())
    player.name = "TestPlayer"
    player.current_room_id = "earth_arkham_city_northside_intersection_derby_high"
    player.experience_points = 100
    player.level = 5
    player.stats = {"health": 100, "sanity": 100, "strength": 10}
    player.inventory = []
    player.status_effects = []
    player.created_at = datetime.now()
    player.last_active = datetime.now()
    return player


@pytest.fixture
def sample_stats_data():
    """Sample stats data for testing."""
    return {
        "strength": 12,
        "dexterity": 14,
        "constitution": 10,
        "intelligence": 16,
        "wisdom": 8,
        "charisma": 11,
    }


@pytest.fixture
def mock_player_service():
    """Mock PlayerService for testing."""
    service = Mock()
    service.create_player = Mock()
    service.create_player_with_stats = Mock()
    service.list_players = Mock()
    service.get_player_by_id = Mock()
    service.get_player_by_name = Mock()
    service.delete_player = Mock()
    return service


@pytest.fixture
def mock_stats_generator():
    """Mock StatsGenerator for testing."""
    generator = Mock(spec=StatsGenerator)
    generator.roll_stats_with_validation = Mock()
    generator.get_stat_summary = Mock()
    generator.validate_class_prerequisites = Mock()
    generator.get_available_classes = Mock()
    generator.CLASS_PREREQUISITES = {
        "investigator": {AttributeType.INT: 12, AttributeType.WIS: 10},
        "occultist": {AttributeType.INT: 14, AttributeType.WIS: 12},
        "survivor": {AttributeType.CON: 12, AttributeType.DEX: 10},
        "cultist": {AttributeType.CHA: 12, AttributeType.INT: 10},
        "academic": {AttributeType.INT: 14, AttributeType.WIS: 10},
        "detective": {AttributeType.INT: 12, AttributeType.WIS: 12},
    }
    return generator


@pytest.fixture
def mock_persistence():
    """Mock persistence layer for testing."""
    persistence = Mock()
    persistence.get_player = Mock()
    persistence.apply_sanity_loss = Mock()
    persistence.apply_fear = Mock()
    persistence.apply_corruption = Mock()
    persistence.gain_occult_knowledge = Mock()
    persistence.heal_player = Mock()
    persistence.damage_player = Mock()
    return persistence


@pytest.fixture
def mock_request():
    """Mock FastAPI request object."""
    request = Mock()
    request.app.state.persistence = Mock()
    return request


class TestPlayerCRUD:
    """Test cases for basic CRUD operations."""

    @patch("server.api.players.PlayerService")
    def test_create_player_success(
        self, mock_player_service_class, mock_current_user, sample_player_data, mock_request
    ):
        """Test successful player creation."""
        # Setup mocks
        mock_service = Mock()
        mock_service.create_player.return_value = sample_player_data
        mock_player_service_class.return_value = mock_service

        result = create_player(
            "TestPlayer", "earth_arkham_city_northside_intersection_derby_high", mock_current_user, mock_request
        )

        assert result == sample_player_data
        mock_service.create_player.assert_called_once_with(
            "TestPlayer", "earth_arkham_city_northside_intersection_derby_high"
        )

    @patch("server.api.players.PlayerService")
    def test_create_player_validation_error(self, mock_player_service_class, mock_current_user, mock_request):
        """Test player creation with validation error."""
        # Setup mocks
        mock_service = Mock()
        mock_service.create_player.side_effect = ValidationError("Invalid player name")
        mock_player_service_class.return_value = mock_service

        with pytest.raises(HTTPException) as exc_info:
            create_player(
                "InvalidName", "earth_arkham_city_northside_intersection_derby_high", mock_current_user, mock_request
            )

        assert exc_info.value.status_code == 400
        assert "Invalid input" in str(exc_info.value.detail)

    @patch("server.api.players.PlayerService")
    def test_list_players_empty(self, mock_player_service_class, mock_current_user, mock_request):
        """Test listing players when no players exist."""
        # Setup mocks
        mock_service = Mock()
        mock_service.list_players.return_value = []
        mock_player_service_class.return_value = mock_service

        result = list_players(mock_current_user, mock_request)

        assert result == []

    @patch("server.api.players.PlayerService")
    def test_list_players_populated(
        self, mock_player_service_class, mock_current_user, sample_player_data, mock_request
    ):
        """Test listing players when players exist."""
        # Setup mocks
        mock_service = Mock()
        mock_service.list_players.return_value = [sample_player_data]
        mock_player_service_class.return_value = mock_service

        result = list_players(mock_current_user, mock_request)

        assert result == [sample_player_data]

    @patch("server.api.players.PlayerService")
    def test_get_player_success(self, mock_player_service_class, mock_current_user, sample_player_data, mock_request):
        """Test successful player retrieval by ID."""
        # Setup mocks
        mock_service = Mock()
        mock_service.get_player_by_id.return_value = sample_player_data
        mock_player_service_class.return_value = mock_service

        player_id = str(uuid.uuid4())
        result = get_player(player_id, mock_current_user, mock_request)

        assert result == sample_player_data
        mock_service.get_player_by_id.assert_called_once_with(player_id)

    @patch("server.api.players.PlayerService")
    def test_get_player_not_found(self, mock_player_service_class, mock_current_user, mock_request):
        """Test player retrieval when player not found."""
        # Setup mocks
        mock_service = Mock()
        mock_service.get_player_by_id.return_value = None
        mock_player_service_class.return_value = mock_service

        player_id = str(uuid.uuid4())
        with pytest.raises(HTTPException) as exc_info:
            get_player(player_id, mock_current_user, mock_request)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    @patch("server.api.players.PlayerService")
    def test_get_player_by_name_success(
        self, mock_player_service_class, mock_current_user, sample_player_data, mock_request
    ):
        """Test successful player retrieval by name."""
        # Setup mocks
        mock_service = Mock()
        mock_service.get_player_by_name.return_value = sample_player_data
        mock_player_service_class.return_value = mock_service

        result = get_player_by_name("TestPlayer", mock_current_user, mock_request)

        assert result == sample_player_data
        mock_service.get_player_by_name.assert_called_once_with("TestPlayer")

    @patch("server.api.players.PlayerService")
    def test_get_player_by_name_not_found(self, mock_player_service_class, mock_current_user, mock_request):
        """Test player retrieval by name when player not found."""
        # Setup mocks
        mock_service = Mock()
        mock_service.get_player_by_name.return_value = None
        mock_player_service_class.return_value = mock_service

        with pytest.raises(HTTPException) as exc_info:
            get_player_by_name("NonexistentPlayer", mock_current_user, mock_request)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    @patch("server.api.players.PlayerService")
    def test_delete_player_success(self, mock_player_service_class, mock_current_user, mock_request):
        """Test successful player deletion."""
        # Setup mocks
        mock_service = Mock()
        mock_service.delete_player.return_value = (True, "Player deleted successfully")
        mock_player_service_class.return_value = mock_service

        player_id = str(uuid.uuid4())
        result = delete_player(player_id, mock_current_user, mock_request)

        assert result["message"] == "Player deleted successfully"
        mock_service.delete_player.assert_called_once_with(player_id)

    @patch("server.api.players.PlayerService")
    def test_delete_player_not_found(self, mock_player_service_class, mock_current_user, mock_request):
        """Test player deletion when player not found."""
        # Setup mocks
        mock_service = Mock()
        mock_service.delete_player.return_value = (False, "Player not found")
        mock_player_service_class.return_value = mock_service

        player_id = str(uuid.uuid4())
        with pytest.raises(HTTPException) as exc_info:
            delete_player(player_id, mock_current_user, mock_request)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)


class TestPlayerEffects:
    """Test cases for player effects endpoints."""

    def test_apply_sanity_loss_success(self, mock_current_user, sample_player_data, mock_persistence, mock_request):
        """Test successful sanity loss application."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = sample_player_data

        result = apply_sanity_loss("test-player-id", 10, "test", mock_current_user, mock_request)

        assert "Applied 10 sanity loss to TestPlayer" in result["message"]
        mock_persistence.apply_sanity_loss.assert_called_once_with(sample_player_data, 10, "test")

    def test_apply_sanity_loss_player_not_found(self, mock_current_user, mock_persistence, mock_request):
        """Test sanity loss application when player not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = None

        with pytest.raises(HTTPException) as exc_info:
            apply_sanity_loss("nonexistent-id", 10, "test", mock_current_user, mock_request)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    def test_apply_fear_success(self, mock_current_user, sample_player_data, mock_persistence, mock_request):
        """Test successful fear application."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = sample_player_data

        result = apply_fear("test-player-id", 5, "test", mock_current_user, mock_request)

        assert "Applied 5 fear to TestPlayer" in result["message"]
        mock_persistence.apply_fear.assert_called_once_with(sample_player_data, 5, "test")

    def test_apply_fear_player_not_found(self, mock_current_user, mock_persistence, mock_request):
        """Test fear application when player not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = None

        with pytest.raises(HTTPException) as exc_info:
            apply_fear("nonexistent-id", 5, "test", mock_current_user, mock_request)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    def test_apply_corruption_success(self, mock_current_user, sample_player_data, mock_persistence, mock_request):
        """Test successful corruption application."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = sample_player_data

        result = apply_corruption("test-player-id", 3, "test", mock_current_user, mock_request)

        assert "Applied 3 corruption to TestPlayer" in result["message"]
        mock_persistence.apply_corruption.assert_called_once_with(sample_player_data, 3, "test")

    def test_apply_corruption_player_not_found(self, mock_current_user, mock_persistence, mock_request):
        """Test corruption application when player not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = None

        with pytest.raises(HTTPException) as exc_info:
            apply_corruption("nonexistent-id", 3, "test", mock_current_user, mock_request)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    def test_gain_occult_knowledge_success(self, mock_current_user, sample_player_data, mock_persistence, mock_request):
        """Test successful occult knowledge gain."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = sample_player_data

        result = gain_occult_knowledge("test-player-id", 2, "test", mock_current_user, mock_request)

        assert "Gained 2 occult knowledge for TestPlayer" in result["message"]
        mock_persistence.gain_occult_knowledge.assert_called_once_with(sample_player_data, 2, "test")

    def test_gain_occult_knowledge_player_not_found(self, mock_current_user, mock_persistence, mock_request):
        """Test occult knowledge gain when player not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = None

        with pytest.raises(HTTPException) as exc_info:
            gain_occult_knowledge("nonexistent-id", 2, "test", mock_current_user, mock_request)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    def test_heal_player_success(self, mock_current_user, sample_player_data, mock_persistence, mock_request):
        """Test successful player healing."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = sample_player_data

        result = heal_player("test-player-id", 20, mock_current_user, mock_request)

        assert "Healed TestPlayer for 20 health" in result["message"]
        mock_persistence.heal_player.assert_called_once_with(sample_player_data, 20)

    def test_heal_player_not_found(self, mock_current_user, mock_persistence, mock_request):
        """Test player healing when player not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = None

        with pytest.raises(HTTPException) as exc_info:
            heal_player("nonexistent-id", 20, mock_current_user, mock_request)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    def test_damage_player_success(self, mock_current_user, sample_player_data, mock_persistence, mock_request):
        """Test successful player damage."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = sample_player_data

        result = damage_player("test-player-id", 15, "physical", mock_current_user, mock_request)

        assert "Damaged TestPlayer for 15 physical damage" in result["message"]
        mock_persistence.damage_player.assert_called_once_with(sample_player_data, 15, "physical")

    def test_damage_player_not_found(self, mock_current_user, mock_persistence, mock_request):
        """Test player damage when player not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = None

        with pytest.raises(HTTPException) as exc_info:
            damage_player("nonexistent-id", 15, "physical", mock_current_user, mock_request)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)


class TestCharacterCreation:
    """Test cases for character creation and stats generation."""

    @patch("server.api.players.StatsGenerator")
    @patch("server.api.players.stats_roll_limiter")
    def test_roll_stats_success(self, mock_limiter, mock_stats_generator_class, mock_current_user, sample_stats_data):
        """Test successful stats rolling."""
        # Setup mocks
        mock_limiter.enforce_rate_limit.return_value = None
        mock_generator = Mock()
        mock_generator.roll_stats_with_validation.return_value = (
            Stats(**sample_stats_data),
            ["investigator", "academic"],
        )
        mock_generator.get_stat_summary.return_value = {"total": 73, "average": 12.17}
        mock_stats_generator_class.return_value = mock_generator

        result = roll_character_stats("3d6", None, 10, mock_current_user)

        assert "stats" in result
        assert "stat_summary" in result
        assert "available_classes" in result
        assert result["method_used"] == "3d6"

    @patch("server.api.players.stats_roll_limiter")
    def test_roll_stats_rate_limited(self, mock_limiter, mock_current_user):
        """Test stats rolling when rate limited."""
        # Setup mocks
        context = create_error_context(user_id=str(mock_current_user.id))
        mock_limiter.enforce_rate_limit.side_effect = RateLimitError("Rate limit exceeded", context, retry_after=60)
        mock_limiter.get_rate_limit_info.return_value = {"remaining": 0, "reset_time": 60}

        with pytest.raises(HTTPException) as exc_info:
            roll_character_stats("3d6", None, 10, mock_current_user)

        assert exc_info.value.status_code == 429
        assert "Rate limit exceeded" in str(exc_info.value.detail["message"])

    def test_roll_stats_authentication_failure(self):
        """Test stats rolling with authentication failure."""
        with pytest.raises(HTTPException) as exc_info:
            roll_character_stats("3d6", None, 10, None)

        assert exc_info.value.status_code == 401
        assert "Authentication required" in str(exc_info.value.detail)

    @patch("server.api.players.StatsGenerator")
    @patch("server.api.players.stats_roll_limiter")
    def test_roll_stats_validation_error(self, mock_limiter, mock_stats_generator_class, mock_current_user):
        """Test stats rolling with validation error."""
        # Setup mocks
        mock_limiter.enforce_rate_limit.return_value = None
        mock_generator = Mock()
        mock_generator.roll_stats_with_validation.side_effect = Exception("Validation failed")
        mock_stats_generator_class.return_value = mock_generator

        with pytest.raises(HTTPException) as exc_info:
            roll_character_stats("3d6", None, 10, mock_current_user)

        assert exc_info.value.status_code == 500
        assert "An internal error occurred" in str(exc_info.value.detail)

    @pytest.mark.asyncio
    @patch("server.api.players.PlayerService")
    @patch("server.api.players.character_creation_limiter")
    async def test_create_character_success(
        self,
        mock_limiter,
        mock_player_service_class,
        mock_current_user,
        sample_player_data,
        sample_stats_data,
        mock_request,
    ):
        """Test successful character creation."""
        # Setup mocks
        mock_limiter.enforce_rate_limit.return_value = None
        mock_service = Mock()
        mock_service.create_player_with_stats.return_value = sample_player_data
        mock_player_service_class.return_value = mock_service

        request_data = Mock()
        request_data.name = "testuser"
        request_data.stats = sample_stats_data
        request_data.starting_room_id = "earth_arkham_city_northside_intersection_derby_high"

        result = await create_character_with_stats(request_data, mock_current_user, mock_request)

        assert "Character testuser created successfully" in result["message"]
        assert "player" in result
        assert "stats" in result

    @pytest.mark.asyncio
    @patch("server.api.players.character_creation_limiter")
    async def test_create_character_rate_limited(self, mock_limiter, mock_current_user, mock_request):
        """Test character creation when rate limited."""
        # Setup mocks
        context = create_error_context(user_id=str(mock_current_user.id))
        mock_limiter.enforce_rate_limit.side_effect = RateLimitError("Rate limit exceeded", context, retry_after=300)
        mock_limiter.get_rate_limit_info.return_value = {"remaining": 0, "reset_time": 300}

        request_data = Mock()
        request_data.name = "testuser"
        request_data.stats = {"strength": 10}
        request_data.starting_room_id = "earth_arkham_city_northside_intersection_derby_high"

        with pytest.raises(HTTPException) as exc_info:
            await create_character_with_stats(request_data, mock_current_user, mock_request)

        assert exc_info.value.status_code == 429
        assert "Rate limit exceeded" in str(exc_info.value.detail["message"])

    @pytest.mark.asyncio
    async def test_create_character_authentication_failure(self, mock_request):
        """Test character creation with authentication failure."""
        request_data = Mock()
        request_data.name = "testuser"
        request_data.stats = {"strength": 10}
        request_data.starting_room_id = "earth_arkham_city_northside_intersection_derby_high"

        with pytest.raises(HTTPException) as exc_info:
            await create_character_with_stats(request_data, None, mock_request)

        assert exc_info.value.status_code == 401
        assert "Authentication required" in str(exc_info.value.detail)

    @pytest.mark.asyncio
    @patch("server.api.players.PlayerService")
    @patch("server.api.players.character_creation_limiter")
    async def test_create_character_name_mismatch(
        self, mock_limiter, mock_player_service_class, mock_current_user, mock_request
    ):
        """Test character creation with name mismatch."""
        # Setup mocks
        mock_limiter.enforce_rate_limit.return_value = None
        mock_request.app.state.persistence = Mock()

        # Mock PlayerService instance
        mock_player_service = Mock()
        mock_player_service_class.return_value = mock_player_service

        # Test data - use proper CreateCharacterRequest object
        request_data = CreateCharacterRequest(
            name="different_name",  # Different from current_user.username
            stats={
                "strength": 10,
                "dexterity": 10,
                "constitution": 10,
                "intelligence": 10,
                "wisdom": 10,
                "charisma": 10,
            },
            starting_room_id="arkham_city_downtown_001",
        )

        with pytest.raises(HTTPException) as exc_info:
            await create_character_with_stats(request_data, mock_current_user, mock_request)

        assert exc_info.value.status_code == 400
        assert "Invalid input" in str(exc_info.value.detail)

    @pytest.mark.asyncio
    @patch("server.api.players.PlayerService")
    @patch("server.api.players.character_creation_limiter")
    async def test_create_character_validation_error(
        self, mock_limiter, mock_player_service_class, mock_current_user, mock_request
    ):
        """Test character creation with validation error."""
        # Setup mocks
        mock_limiter.enforce_rate_limit.return_value = None
        mock_service = Mock()
        mock_service.create_player_with_stats.side_effect = ValueError("Invalid stats")
        mock_player_service_class.return_value = mock_service

        request_data = Mock()
        request_data.name = "testuser"
        request_data.stats = {"invalid": "stats"}
        request_data.starting_room_id = "earth_arkham_city_northside_intersection_derby_high"

        with pytest.raises(HTTPException) as exc_info:
            await create_character_with_stats(request_data, mock_current_user, mock_request)

        assert exc_info.value.status_code == 400
        assert "Invalid input" in str(exc_info.value.detail)


class TestStatsValidation:
    """Test cases for stats validation endpoints."""

    @patch("server.api.players.StatsGenerator")
    def test_validate_stats_success(self, mock_stats_generator_class, mock_current_user, sample_stats_data):
        """Test successful stats validation."""
        # Setup mocks
        mock_generator = Mock()
        mock_generator.get_available_classes.return_value = ["investigator", "academic"]
        mock_generator.get_stat_summary.return_value = {"total": 73, "average": 12.17}
        mock_stats_generator_class.return_value = mock_generator

        result = validate_character_stats(sample_stats_data, None, mock_current_user)

        assert "available_classes" in result
        assert "stat_summary" in result

    @patch("server.api.players.StatsGenerator")
    def test_validate_stats_with_class(self, mock_stats_generator_class, mock_current_user, sample_stats_data):
        """Test stats validation with specific class."""
        # Setup mocks
        mock_generator = Mock()
        mock_generator.validate_class_prerequisites.return_value = (True, [])
        mock_generator.get_available_classes.return_value = ["investigator", "academic"]
        mock_stats_generator_class.return_value = mock_generator

        result = validate_character_stats(sample_stats_data, "investigator", mock_current_user)

        assert result["meets_prerequisites"] is True
        assert result["requested_class"] == "investigator"

    @patch("server.api.players.StatsGenerator")
    def test_validate_stats_invalid_format(self, mock_stats_generator_class, mock_current_user):
        """Test stats validation with invalid format."""
        # Setup mocks
        mock_generator = Mock()
        mock_generator.get_available_classes.side_effect = Exception("Invalid stats format")
        mock_stats_generator_class.return_value = mock_generator

        invalid_stats = {"invalid": "stats", "format": "here"}

        with pytest.raises(HTTPException) as exc_info:
            validate_character_stats(invalid_stats, None, mock_current_user)

        assert exc_info.value.status_code == 400
        assert "Invalid format" in str(exc_info.value.detail)

    @patch("server.api.players.StatsGenerator")
    def test_get_available_classes(self, mock_stats_generator_class, mock_current_user):
        """Test getting available classes information."""
        # Setup mocks
        mock_generator = Mock()
        mock_generator.CLASS_PREREQUISITES = {
            "investigator": {AttributeType.INT: 12, AttributeType.WIS: 10},
            "occultist": {AttributeType.INT: 14, AttributeType.WIS: 12},
        }
        mock_generator.MIN_STAT = 3
        mock_generator.MAX_STAT = 18
        mock_stats_generator_class.return_value = mock_generator

        result = get_available_classes(mock_current_user)

        assert "classes" in result
        assert "stat_range" in result
        assert "investigator" in result["classes"]
        assert "occultist" in result["classes"]


class TestClassDescriptions:
    """Test cases for class description functionality."""

    def test_get_class_description_all_classes(self):
        """Test getting descriptions for all character classes."""
        classes = ["investigator", "occultist", "survivor", "cultist", "academic", "detective"]

        for class_name in classes:
            description = get_class_description(class_name)
            assert description is not None
            assert len(description) > 0
            assert "mysterious" not in description.lower()  # Should have specific descriptions

    def test_get_class_description_unknown_class(self):
        """Test getting description for unknown class."""
        description = get_class_description("unknown_class")
        assert description is not None
        assert "mysterious" in description.lower()
        assert "unknown capabilities" in description

    def test_get_class_description_investigator(self):
        """Test investigator class description."""
        description = get_class_description("investigator")
        assert "researcher" in description.lower()
        assert "detective" in description.lower()
        assert "mysteries" in description.lower()

    def test_get_class_description_occultist(self):
        """Test occultist class description."""
        description = get_class_description("occultist")
        assert "forbidden knowledge" in description.lower()
        assert "magic" in description.lower()
        assert "sanity" in description.lower()
