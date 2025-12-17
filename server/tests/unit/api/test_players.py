"""
Tests for the players API endpoints.

This module tests all player-related API operations including
creation, retrieval, listing, deletion, and effects application.
Following the academic rigor outlined in the Pnakotic Manuscripts of Testing Methodology.
"""

import types
import uuid
from datetime import datetime
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi import HTTPException

from server.api.character_creation import (
    create_character_with_stats,
    roll_character_stats,
    validate_character_stats,
)
from server.api.player_effects import (
    apply_corruption,
    apply_fear,
    apply_lucidity_loss,
    damage_player,
    gain_occult_knowledge,
    heal_player,
)
from server.api.players import (
    create_player,
    delete_player,
    get_available_classes,
    get_class_description,
    get_player,
    get_player_by_name,
    list_players,
)
from server.exceptions import LoggedHTTPException, RateLimitError, ValidationError, create_error_context
from server.game.stats_generator import StatsGenerator
from server.models import AttributeType, Stats
from server.schemas.player_requests import (
    CorruptionRequest,
    CreateCharacterRequest,
    DamageRequest,
    FearRequest,
    HealRequest,
    LucidityLossRequest,
    OccultKnowledgeRequest,
    RollStatsRequest,
)

# pylint: disable=redefined-outer-name
# Pytest fixtures are commonly used as function parameters, which triggers
# redefined-outer-name warnings. This is expected behavior in pytest tests.


def _mock_getitem(self, key):
    """Helper function to support dictionary-style access on mock objects."""
    return getattr(self, key)


@pytest.fixture
def mock_current_user():
    """Mock authenticated user for testing."""
    user = Mock()
    user.id = str(uuid.uuid4())
    user.username = "testuser"
    # Make the mock support dictionary access for all attributes
    user.__getitem__ = types.MethodType(_mock_getitem, user)
    return user


@pytest.fixture
def sample_player_data():
    """Sample player data for testing."""
    player = Mock()
    player.player_id = uuid.uuid4()
    player.user_id = uuid.uuid4()
    player.name = "TestPlayer"
    player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
    player.experience_points = 100
    player.level = 5
    player.stats = {"health": 100, "lucidity": 100, "strength": 10}
    player.inventory = []
    player.status_effects = []
    player.created_at = datetime.now()
    player.last_active = datetime.now()
    # Configure model_dump() to return a dict representation for API endpoint compatibility
    player_dict = {
        "player_id": player.player_id,
        "user_id": player.user_id,
        "name": player.name,
        "current_room_id": player.current_room_id,
        "experience_points": player.experience_points,
        "level": player.level,
        "stats": player.stats,
        "inventory": player.inventory,
        "status_effects": player.status_effects,
        "created_at": player.created_at.isoformat()
        if hasattr(player.created_at, "isoformat")
        else str(player.created_at),
        "last_active": player.last_active.isoformat()
        if hasattr(player.last_active, "isoformat")
        else str(player.last_active),
    }
    player.model_dump = Mock(return_value=player_dict)
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
    service.list_players = AsyncMock()  # list_players is async
    service.get_player_by_id = Mock()
    service.get_player_by_name = Mock()
    service.delete_player = AsyncMock()  # delete_player is async
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
        "investigator": {AttributeType.INT: 12, AttributeType.EDU: 10},
        "occultist": {AttributeType.INT: 14, AttributeType.POW: 12},
        "survivor": {AttributeType.CON: 12, AttributeType.DEX: 10},
        "cultist": {AttributeType.CHA: 12, AttributeType.INT: 10},
        "academic": {AttributeType.INT: 14, AttributeType.EDU: 10},
        "detective": {AttributeType.INT: 12, AttributeType.EDU: 12},
    }
    return generator


@pytest.fixture
def mock_persistence():
    """Mock persistence layer for testing."""
    persistence = Mock()
    persistence.get_player = Mock()
    persistence.apply_lucidity_loss = Mock()
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
    request.app = Mock()
    request.app.state = Mock()
    request.app.state.persistence = Mock()
    request.app.state.server_shutdown_pending = False  # No shutdown by default
    return request


class TestPlayerCRUD:
    """Test cases for basic CRUD operations."""

    @patch("server.api.players.PlayerService")
    @pytest.mark.asyncio
    async def test_create_player_success(
        self,
        mock_player_service_class,
        mock_current_user,
        sample_player_data,
        mock_request,
    ):
        """Test successful player creation."""
        # Setup mocks
        mock_service = AsyncMock()
        mock_service.create_player.return_value = sample_player_data
        mock_player_service_class.return_value = mock_service

        result = await create_player(
            name="TestPlayer",
            request=mock_request,
            starting_room_id="earth_arkhamcity_northside_intersection_derby_high",
            current_user=mock_current_user,
            player_service=mock_service,
        )

        # The API endpoint calls .model_dump() on the player object, so we need to compare with the dict
        expected_dict = sample_player_data.model_dump()
        assert result == expected_dict
        mock_service.create_player.assert_called_once_with(
            "TestPlayer", profession_id=0, starting_room_id="earth_arkhamcity_northside_intersection_derby_high"
        )

    @patch("server.api.players.PlayerService")
    @pytest.mark.asyncio
    async def test_create_player_validation_error(self, mock_player_service_class, mock_current_user, mock_request):
        """Test player creation with validation error."""
        # Setup mocks
        mock_service = AsyncMock()
        mock_service.create_player.side_effect = ValidationError("Invalid player name")
        mock_player_service_class.return_value = mock_service

        with pytest.raises(HTTPException) as exc_info:
            await create_player(
                name="InvalidName",
                request=mock_request,
                starting_room_id="earth_arkhamcity_northside_intersection_derby_high",
                current_user=mock_current_user,
                player_service=mock_service,
            )

        assert exc_info.value.status_code == 400
        assert "Invalid input" in str(exc_info.value.detail)

    @patch("server.api.players.PlayerService")
    @pytest.mark.asyncio
    async def test_list_players_empty(self, mock_player_service_class, mock_current_user, mock_request):
        """Test listing players when no players exist."""
        # Setup mocks
        mock_service = AsyncMock()
        mock_service.list_players.return_value = []
        mock_player_service_class.return_value = mock_service

        result = await list_players(mock_current_user, mock_request, mock_service)

        assert result == []

    @patch("server.api.players.PlayerService")
    @pytest.mark.asyncio
    async def test_list_players_populated(
        self, mock_player_service_class, mock_current_user, sample_player_data, mock_request
    ):
        """Test listing players when players exist."""
        # Setup mocks
        mock_service = AsyncMock()
        mock_service.list_players.return_value = [sample_player_data]
        mock_player_service_class.return_value = mock_service

        result = await list_players(mock_current_user, mock_request, mock_service)

        assert result == [sample_player_data.model_dump()]

    @patch("server.api.players.PlayerService")
    @pytest.mark.asyncio
    async def test_get_player_success(
        self, mock_player_service_class, mock_current_user, sample_player_data, mock_request
    ):
        """Test successful player retrieval by ID."""
        # Setup mocks
        mock_service = AsyncMock()
        mock_service.get_player_by_id.return_value = sample_player_data
        mock_player_service_class.return_value = mock_service

        player_id = uuid.uuid4()
        result = await get_player(player_id, mock_current_user, mock_request, mock_service)

        assert result == sample_player_data.model_dump()
        mock_service.get_player_by_id.assert_called_once_with(player_id)

    @patch("server.api.players.PlayerService")
    @pytest.mark.asyncio
    async def test_get_player_not_found(self, mock_player_service_class, mock_current_user, mock_request):
        """Test player retrieval when player not found."""
        # Setup mocks
        mock_service = AsyncMock()
        mock_service.get_player_by_id.return_value = None
        mock_player_service_class.return_value = mock_service

        player_id = uuid.uuid4()
        with pytest.raises(HTTPException) as exc_info:
            await get_player(player_id, mock_current_user, mock_request, mock_service)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    @patch("server.api.players.PlayerService")
    @pytest.mark.asyncio
    async def test_get_player_by_name_success(
        self, mock_player_service_class, mock_current_user, sample_player_data, mock_request
    ):
        """Test successful player retrieval by name."""
        # Setup mocks
        mock_service = AsyncMock()
        mock_service.get_player_by_name.return_value = sample_player_data
        mock_player_service_class.return_value = mock_service

        result = await get_player_by_name("TestPlayer", mock_current_user, mock_request, mock_service)

        assert result == sample_player_data.model_dump()
        mock_service.get_player_by_name.assert_called_once_with("TestPlayer")

    @patch("server.api.players.PlayerService")
    @pytest.mark.asyncio
    async def test_get_player_by_name_not_found(self, mock_player_service_class, mock_current_user, mock_request):
        """Test player retrieval by name when player not found."""
        # Setup mocks
        mock_service = AsyncMock()
        mock_service.get_player_by_name.return_value = None
        mock_player_service_class.return_value = mock_service

        with pytest.raises(HTTPException) as exc_info:
            await get_player_by_name("NonexistentPlayer", mock_current_user, mock_request, mock_service)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    @patch("server.api.players.PlayerService")
    @pytest.mark.asyncio
    async def test_delete_player_success(self, mock_player_service_class, mock_current_user, mock_request):
        """Test successful player deletion."""
        # Setup mocks
        mock_service = AsyncMock()
        mock_service.delete_player.return_value = (True, "Player deleted successfully")
        mock_player_service_class.return_value = mock_service

        player_id = uuid.uuid4()
        result = await delete_player(player_id, mock_current_user, mock_request, mock_service)

        assert result["message"] == "Player deleted successfully"
        mock_service.delete_player.assert_called_once_with(player_id)

    @patch("server.api.players.PlayerService")
    @pytest.mark.asyncio
    async def test_delete_player_not_found(self, mock_player_service_class, mock_current_user, mock_request):
        """Test player deletion when player not found."""
        # Setup mocks
        mock_service = AsyncMock()
        mock_service.delete_player.return_value = (False, "Player not found")
        mock_player_service_class.return_value = mock_service

        player_id = uuid.uuid4()
        with pytest.raises(HTTPException) as exc_info:
            await delete_player(player_id, mock_current_user, mock_request, mock_service)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)


class TestPlayerEffects:
    """Test cases for player effects endpoints."""

    @patch("server.api.players.PlayerServiceDep")
    @pytest.mark.asyncio
    async def test_apply_lucidity_loss_success(
        self, mock_player_service_dep, mock_current_user, sample_player_data, mock_persistence, mock_request
    ):
        """Test successful lucidity loss application."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = sample_player_data

        # Mock the PlayerService dependency
        mock_service = AsyncMock()
        mock_service.apply_lucidity_loss.return_value = {"message": "Applied 10 lucidity loss to TestPlayer"}
        mock_player_service_dep.return_value = mock_service

        request_data = LucidityLossRequest(amount=10, source="test")
        result = await apply_lucidity_loss(
            "test-player-id", request_data, mock_request, mock_current_user, mock_service
        )

        assert "Applied 10 lucidity loss to TestPlayer" in result["message"]
        mock_service.apply_lucidity_loss.assert_called_once_with("test-player-id", 10, "test")

    @patch("server.api.players.PlayerServiceDep")
    @pytest.mark.asyncio
    async def test_apply_lucidity_loss_player_not_found(
        self, mock_player_service_dep, mock_current_user, mock_persistence, mock_request
    ):
        """Test lucidity loss application when player not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = None

        # Mock the PlayerService dependency
        mock_service = AsyncMock()
        mock_service.apply_lucidity_loss.side_effect = ValidationError("Player not found")
        mock_player_service_dep.return_value = mock_service

        with pytest.raises(LoggedHTTPException) as exc_info:
            request_data = LucidityLossRequest(amount=10, source="test")
            await apply_lucidity_loss("nonexistent-id", request_data, mock_request, mock_current_user, mock_service)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    @patch("server.api.players.PlayerServiceDep")
    @pytest.mark.asyncio
    async def test_apply_fear_success(
        self, mock_player_service_dep, mock_current_user, sample_player_data, mock_persistence, mock_request
    ):
        """Test successful fear application."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = sample_player_data

        # Mock the PlayerService dependency
        mock_service = AsyncMock()
        mock_service.apply_fear.return_value = {"message": "Applied 5 fear to TestPlayer"}
        mock_player_service_dep.return_value = mock_service

        request_data = FearRequest(amount=5, source="test")
        result = await apply_fear("test-player-id", request_data, mock_request, mock_current_user, mock_service)

        assert "Applied 5 fear to TestPlayer" in result["message"]
        mock_service.apply_fear.assert_called_once_with("test-player-id", 5, "test")

    @patch("server.api.players.PlayerServiceDep")
    @pytest.mark.asyncio
    async def test_apply_fear_player_not_found(
        self, mock_player_service_dep, mock_current_user, mock_persistence, mock_request
    ):
        """Test fear application when player not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = None

        # Mock the PlayerService dependency
        mock_service = AsyncMock()
        mock_service.apply_fear.side_effect = ValidationError("Player not found")
        mock_player_service_dep.return_value = mock_service

        with pytest.raises(LoggedHTTPException) as exc_info:
            request_data = FearRequest(amount=5, source="test")
            await apply_fear("nonexistent-id", request_data, mock_request, mock_current_user, mock_service)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    @patch("server.api.players.PlayerServiceDep")
    @pytest.mark.asyncio
    async def test_apply_corruption_success(
        self, mock_player_service_dep, mock_current_user, sample_player_data, mock_persistence, mock_request
    ):
        """Test successful corruption application."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = sample_player_data

        # Mock the PlayerService dependency
        mock_service = AsyncMock()
        mock_service.apply_corruption.return_value = {"message": "Applied 3 corruption to TestPlayer"}
        mock_player_service_dep.return_value = mock_service

        request_data = CorruptionRequest(amount=3, source="test")
        result = await apply_corruption("test-player-id", request_data, mock_request, mock_current_user, mock_service)

        assert "Applied 3 corruption to TestPlayer" in result["message"]
        mock_service.apply_corruption.assert_called_once_with("test-player-id", 3, "test")

    @patch("server.api.players.PlayerServiceDep")
    @pytest.mark.asyncio
    async def test_apply_corruption_player_not_found(
        self, mock_player_service_dep, mock_current_user, mock_persistence, mock_request
    ):
        """Test corruption application when player not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = None

        # Mock the PlayerService dependency
        mock_service = AsyncMock()
        mock_service.apply_corruption.side_effect = ValidationError("Player not found")
        mock_player_service_dep.return_value = mock_service

        with pytest.raises(LoggedHTTPException) as exc_info:
            request_data = CorruptionRequest(amount=3, source="test")
            await apply_corruption("nonexistent-id", request_data, mock_request, mock_current_user, mock_service)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    @patch("server.api.players.PlayerServiceDep")
    @pytest.mark.asyncio
    async def test_gain_occult_knowledge_success(
        self, mock_player_service_dep, mock_current_user, sample_player_data, mock_persistence, mock_request
    ):
        """Test successful occult knowledge gain."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = sample_player_data

        # Mock the PlayerService dependency
        mock_service = AsyncMock()
        mock_service.gain_occult_knowledge.return_value = {"message": "Gained 2 occult knowledge for TestPlayer"}
        mock_player_service_dep.return_value = mock_service

        request_data = OccultKnowledgeRequest(amount=2, source="test")
        result = await gain_occult_knowledge(
            "test-player-id", request_data, mock_request, mock_current_user, mock_service
        )

        assert "Gained 2 occult knowledge for TestPlayer" in result["message"]
        mock_service.gain_occult_knowledge.assert_called_once_with("test-player-id", 2, "test")

    @patch("server.api.players.PlayerServiceDep")
    @pytest.mark.asyncio
    async def test_gain_occult_knowledge_player_not_found(
        self, mock_player_service_dep, mock_current_user, mock_persistence, mock_request
    ):
        """Test occult knowledge gain when player not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = None

        # Mock the PlayerService dependency
        mock_service = AsyncMock()
        mock_service.gain_occult_knowledge.side_effect = ValidationError("Player not found")
        mock_player_service_dep.return_value = mock_service

        with pytest.raises(LoggedHTTPException) as exc_info:
            request_data = OccultKnowledgeRequest(amount=2, source="test")
            await gain_occult_knowledge("nonexistent-id", request_data, mock_request, mock_current_user, mock_service)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    @patch("server.api.players.PlayerServiceDep")
    @pytest.mark.asyncio
    async def test_heal_player_success(
        self, mock_player_service_dep, mock_current_user, sample_player_data, mock_persistence, mock_request
    ):
        """Test successful player healing."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = sample_player_data

        # Mock the PlayerService dependency
        mock_service = AsyncMock()
        mock_service.heal_player.return_value = {"message": "Healed TestPlayer for 20 health"}
        mock_player_service_dep.return_value = mock_service

        request_data = HealRequest(amount=20)
        result = await heal_player("test-player-id", request_data, mock_request, mock_current_user, mock_service)

        assert "Healed TestPlayer for 20 health" in result["message"]
        mock_service.heal_player.assert_called_once_with("test-player-id", 20)

    @patch("server.api.players.PlayerServiceDep")
    @pytest.mark.asyncio
    async def test_heal_player_not_found(
        self, mock_player_service_dep, mock_current_user, mock_persistence, mock_request
    ):
        """Test player healing when player not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = None

        # Mock the PlayerService dependency
        mock_service = AsyncMock()
        mock_service.heal_player.side_effect = ValidationError("Player not found")
        mock_player_service_dep.return_value = mock_service

        with pytest.raises(LoggedHTTPException) as exc_info:
            request_data = HealRequest(amount=20)
            await heal_player("nonexistent-id", request_data, mock_request, mock_current_user, mock_service)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)

    @patch("server.api.players.PlayerServiceDep")
    @pytest.mark.asyncio
    async def test_damage_player_success(
        self, mock_player_service_dep, mock_current_user, sample_player_data, mock_persistence, mock_request
    ):
        """Test successful player damage."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = sample_player_data

        # Mock the PlayerService dependency
        mock_service = AsyncMock()
        mock_service.damage_player.return_value = {"message": "Damaged TestPlayer for 15 physical damage"}
        mock_player_service_dep.return_value = mock_service

        request_data = DamageRequest(amount=15, damage_type="physical")
        result = await damage_player("test-player-id", request_data, mock_request, mock_current_user, mock_service)

        assert "Damaged TestPlayer for 15 physical damage" in result["message"]
        mock_service.damage_player.assert_called_once_with("test-player-id", 15, "physical")

    @patch("server.api.players.PlayerServiceDep")
    @pytest.mark.asyncio
    async def test_damage_player_not_found(
        self, mock_player_service_dep, mock_current_user, mock_persistence, mock_request
    ):
        """Test player damage when player not found."""
        # Setup mocks
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player.return_value = None

        # Mock the PlayerService dependency
        mock_service = AsyncMock()
        mock_service.damage_player.side_effect = ValidationError("Player not found")
        mock_player_service_dep.return_value = mock_service

        with pytest.raises(LoggedHTTPException) as exc_info:
            request_data = DamageRequest(amount=15, damage_type="physical")
            await damage_player("nonexistent-id", request_data, mock_request, mock_current_user, mock_service)

        assert exc_info.value.status_code == 404
        assert "Player not found" in str(exc_info.value.detail)


class TestCharacterCreation:
    """Test cases for character creation and stats generation."""

    @patch("server.api.players.StatsGenerator")
    @patch("server.api.players.stats_roll_limiter")
    @pytest.mark.asyncio
    async def test_roll_stats_success(
        self, mock_limiter, mock_stats_generator_class, mock_current_user, sample_stats_data, mock_request
    ):
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

        # Pass the mock generator directly since we're calling the function directly (not through FastAPI DI)
        request_data = RollStatsRequest(method="3d6", required_class=None, timeout_seconds=1.0, profession_id=None)
        result = await roll_character_stats(
            request_data, mock_request, max_attempts=10, current_user=mock_current_user, stats_generator=mock_generator
        )

        assert "stats" in result
        assert "stat_summary" in result
        assert "available_classes" in result
        assert result["method_used"] == "3d6"

    @patch("server.api.players.stats_roll_limiter")
    @pytest.mark.asyncio
    async def test_roll_stats_rate_limited(self, mock_limiter, mock_current_user, mock_request):
        """Test stats rolling when rate limited."""
        # Setup mocks
        context = create_error_context(user_id=str(mock_current_user.id))
        mock_limiter.enforce_rate_limit.side_effect = RateLimitError("Rate limit exceeded", context, retry_after=60)
        mock_limiter.get_rate_limit_info.return_value = {"remaining": 0, "reset_time": 60}

        # Create a mock generator for the function call
        mock_generator = Mock()
        request_data = RollStatsRequest(method="3d6", required_class=None, timeout_seconds=1.0, profession_id=None)
        with pytest.raises(LoggedHTTPException) as exc_info:
            await roll_character_stats(
                request_data,
                mock_request,
                max_attempts=10,
                current_user=mock_current_user,
                stats_generator=mock_generator,
            )

        assert exc_info.value.status_code == 429
        assert "Rate limit exceeded" in str(exc_info.value.detail)

    @pytest.mark.asyncio
    async def test_roll_stats_authentication_failure(self, mock_request):
        """Test stats rolling with authentication failure."""
        # Create a mock generator for the function call
        mock_generator = Mock()
        request_data = RollStatsRequest(method="3d6", required_class=None, timeout_seconds=1.0, profession_id=None)
        with pytest.raises(LoggedHTTPException) as exc_info:
            await roll_character_stats(
                request_data, mock_request, max_attempts=10, current_user=None, stats_generator=mock_generator
            )

        assert exc_info.value.status_code == 401
        assert "Authentication required" in str(exc_info.value.detail)

    @patch("server.api.players.StatsGenerator")
    @patch("server.api.players.stats_roll_limiter")
    @pytest.mark.asyncio
    async def test_roll_stats_validation_error(
        self, mock_limiter, mock_stats_generator_class, mock_current_user, mock_request
    ):
        """Test stats rolling with validation error."""
        # Setup mocks
        mock_limiter.enforce_rate_limit.return_value = None
        mock_generator = Mock()
        mock_generator.roll_stats_with_validation.side_effect = Exception("Validation failed")
        mock_stats_generator_class.return_value = mock_generator

        request_data = RollStatsRequest(method="3d6", required_class=None, timeout_seconds=1.0, profession_id=None)
        with pytest.raises(HTTPException) as exc_info:
            await roll_character_stats(
                request_data,
                mock_request,
                max_attempts=10,
                current_user=mock_current_user,
                stats_generator=mock_generator,
            )

        assert exc_info.value.status_code == 500
        assert "An internal error occurred" in str(exc_info.value.detail)

    @pytest.mark.asyncio
    @patch("server.api.players.PlayerServiceDep")
    @patch("server.api.players.character_creation_limiter")
    async def test_create_character_success(
        self,
        mock_limiter,
        mock_player_service_dep,
        mock_current_user,
        sample_player_data,
        sample_stats_data,
        mock_request,
    ):
        """Test successful character creation."""
        # Setup mocks
        mock_limiter.enforce_rate_limit.return_value = None
        mock_service = AsyncMock()
        mock_service.create_player_with_stats.return_value = sample_player_data
        mock_player_service_dep.return_value = mock_service

        request_data = Mock()
        request_data.name = "testuser"
        request_data.stats = sample_stats_data
        request_data.starting_room_id = "earth_arkhamcity_northside_intersection_derby_high"

        result = await create_character_with_stats(request_data, mock_request, mock_current_user, mock_service)

        # Result is now a PlayerRead object (not a dict)
        assert result is not None
        assert hasattr(result, "name") or isinstance(result, dict)
        mock_service.create_player_with_stats.assert_called_once()

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
        request_data.starting_room_id = "earth_arkhamcity_northside_intersection_derby_high"

        with pytest.raises(HTTPException) as exc_info:
            await create_character_with_stats(request_data, mock_request, mock_current_user)

        assert exc_info.value.status_code == 429
        assert exc_info.value.detail == "Rate limit exceeded"

    @pytest.mark.asyncio
    async def test_create_character_authentication_failure(self, mock_request):
        """Test character creation with authentication failure."""
        request_data = Mock()
        request_data.name = "testuser"
        request_data.stats = {"strength": 10}
        request_data.starting_room_id = "earth_arkhamcity_northside_intersection_derby_high"

        with pytest.raises(HTTPException) as exc_info:
            await create_character_with_stats(request_data, mock_request, None)

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
            starting_room_id="arkhamcity_downtown_001",
        )

        with pytest.raises(HTTPException) as exc_info:
            await create_character_with_stats(request_data, mock_request, mock_current_user)

        assert exc_info.value.status_code == 400
        assert "Invalid input" in str(exc_info.value.detail)

    @pytest.mark.asyncio
    @patch("server.api.players.PlayerServiceDep")
    @patch("server.api.players.character_creation_limiter")
    async def test_create_character_validation_error(
        self, mock_limiter, mock_player_service_dep, mock_current_user, mock_request
    ):
        """Test character creation with validation error."""
        # Setup mocks
        mock_limiter.enforce_rate_limit.return_value = None
        mock_service = Mock()
        mock_service.create_player_with_stats.side_effect = ValueError("Invalid stats")
        mock_player_service_dep.return_value = mock_service

        request_data = Mock()
        request_data.name = "testuser"
        request_data.stats = {"invalid": "stats"}
        request_data.starting_room_id = "earth_arkhamcity_northside_intersection_derby_high"

        with pytest.raises(HTTPException) as exc_info:
            await create_character_with_stats(request_data, mock_request, mock_current_user, mock_service)

        assert exc_info.value.status_code == 400
        assert "Invalid input" in str(exc_info.value.detail)

    @patch("server.api.players.StatsGenerator")
    @patch("server.api.players.stats_roll_limiter")
    @patch("server.async_persistence.get_async_persistence")
    @pytest.mark.asyncio
    async def test_roll_stats_with_profession_success(
        self,
        mock_get_persistence,
        mock_limiter,
        mock_stats_generator_class,
        mock_current_user,
        mock_request,
        sample_stats_data,
    ):
        """Test successful stats rolling with profession ID."""
        # Setup mocks
        mock_limiter.enforce_rate_limit.return_value = None
        mock_generator = Mock()
        mock_generator.roll_stats_with_profession.return_value = (
            Stats(**sample_stats_data),
            True,  # meets_requirements
        )
        mock_generator.get_stat_summary.return_value = {"total": 73, "average": 12.17}
        mock_stats_generator_class.return_value = mock_generator

        # Mock profession lookup
        mock_profession = Mock()
        mock_profession.id = 0
        mock_profession.name = "Scholar"
        mock_profession.description = "A learned academic"
        mock_profession.flavor_text = "Knowledge is power"
        mock_persistence = AsyncMock()
        mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)
        mock_get_persistence.return_value = mock_persistence

        request_data = RollStatsRequest(method="3d6", required_class=None, timeout_seconds=1.0, profession_id=0)
        result = await roll_character_stats(
            request_data,
            mock_request,
            max_attempts=10,
            current_user=mock_current_user,
            stats_generator=mock_generator,
        )

        assert "stats" in result
        assert "stat_summary" in result
        assert "profession_id" in result
        assert "meets_requirements" in result
        assert result["method_used"] == "3d6"
        assert result["profession_id"] == 0
        assert result["meets_requirements"] is True

    @patch("server.api.players.StatsGenerator")
    @patch("server.api.players.stats_roll_limiter")
    @pytest.mark.asyncio
    async def test_roll_stats_with_profession_requirements_not_met(
        self, mock_limiter, mock_stats_generator_class, mock_current_user, mock_request, sample_stats_data
    ):
        """Test stats rolling with profession when requirements are not met."""
        # Setup mocks
        mock_limiter.enforce_rate_limit.return_value = None
        mock_generator = Mock()
        mock_generator.roll_stats_with_profession.return_value = (
            Stats(**sample_stats_data),
            False,  # does not meet requirements
        )
        mock_generator.get_stat_summary.return_value = {"total": 73, "average": 12.17}
        mock_stats_generator_class.return_value = mock_generator

        # Mock shutdown check and async_persistence
        mock_profession = Mock()
        mock_profession.id = 1
        mock_profession.name = "TestProfession"

        with (
            patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False),
            patch("server.async_persistence.get_async_persistence") as mock_get_persistence,
        ):
            mock_persistence = AsyncMock()
            mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)
            mock_get_persistence.return_value = mock_persistence

            request_data = RollStatsRequest(method="3d6", required_class=None, timeout_seconds=1.0, profession_id=1)
            result = await roll_character_stats(
                request_data,
                mock_request,
                max_attempts=10,
                current_user=mock_current_user,
                stats_generator=mock_generator,
            )

        assert "stats" in result
        assert "stat_summary" in result
        assert "profession_id" in result
        assert "meets_requirements" in result
        assert result["profession_id"] == 1
        assert result["meets_requirements"] is False

    @patch("server.api.players.StatsGenerator")
    @patch("server.api.players.stats_roll_limiter")
    @pytest.mark.asyncio
    async def test_roll_stats_with_invalid_profession(
        self, mock_limiter, mock_stats_generator_class, mock_current_user, mock_request
    ):
        """Test stats rolling with invalid profession ID."""
        # Setup mocks
        mock_limiter.enforce_rate_limit.return_value = None
        mock_generator = Mock()
        mock_generator.roll_stats_with_profession.side_effect = ValueError("Invalid profession ID")
        mock_stats_generator_class.return_value = mock_generator

        # Mock shutdown check and async_persistence
        with (
            patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False),
            patch("server.async_persistence.get_async_persistence") as mock_get_persistence,
        ):
            # Mock persistence to return None for invalid profession
            mock_persistence = AsyncMock()
            mock_persistence.get_profession_by_id = AsyncMock(return_value=None)
            mock_get_persistence.return_value = mock_persistence

            request_data = RollStatsRequest(method="3d6", required_class=None, timeout_seconds=1.0, profession_id=999)
            with pytest.raises(LoggedHTTPException) as exc_info:
                await roll_character_stats(
                    request_data,
                    mock_request,
                    max_attempts=10,
                    current_user=mock_current_user,
                    stats_generator=mock_generator,
                )

            assert exc_info.value.status_code == 404  # Profession not found
            assert "not found" in str(exc_info.value.detail).lower()

    @patch("server.api.players.StatsGenerator")
    @patch("server.api.players.stats_roll_limiter")
    @patch("server.async_persistence.get_async_persistence")
    @pytest.mark.asyncio
    async def test_roll_stats_with_profession_validation_error(
        self,
        mock_get_persistence,
        mock_limiter,
        mock_stats_generator_class,
        mock_current_user,
        mock_request,
    ):
        """Test stats rolling with profession when validation fails."""
        # Setup mocks
        mock_limiter.enforce_rate_limit.return_value = None
        mock_generator = Mock()
        mock_generator.roll_stats_with_profession.side_effect = Exception("Profession validation failed")
        mock_stats_generator_class.return_value = mock_generator

        # Mock profession lookup to return a valid profession so we reach the validation error
        mock_profession = Mock()
        mock_profession.id = 0
        mock_profession.name = "Scholar"
        mock_profession.description = "A learned academic"
        mock_profession.flavor_text = "Knowledge is power"
        mock_persistence = AsyncMock()
        mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)
        mock_get_persistence.return_value = mock_persistence

        request_data = RollStatsRequest(method="3d6", required_class=None, timeout_seconds=1.0, profession_id=0)
        with pytest.raises(LoggedHTTPException) as exc_info:
            await roll_character_stats(
                request_data,
                mock_request,
                max_attempts=10,
                current_user=mock_current_user,
                stats_generator=mock_generator,
            )

        assert exc_info.value.status_code == 500
        assert "An internal error occurred" in str(exc_info.value.detail)


class TestStatsValidation:
    """Test cases for stats validation endpoints."""

    @patch("server.api.players.StatsGenerator")
    @pytest.mark.asyncio
    async def test_validate_stats_success(self, mock_stats_generator_class, mock_current_user, sample_stats_data):
        """Test successful stats validation."""
        # Setup mocks
        mock_generator = Mock()
        mock_generator.get_available_classes.return_value = ["investigator", "academic"]
        mock_generator.get_stat_summary.return_value = {"total": 73, "average": 12.17}
        mock_stats_generator_class.return_value = mock_generator

        result = await validate_character_stats(
            sample_stats_data, None, mock_current_user, stats_generator=mock_generator
        )

        assert "available_classes" in result
        assert "stat_summary" in result

    @patch("server.api.players.StatsGenerator")
    @pytest.mark.asyncio
    async def test_validate_stats_with_class(self, mock_stats_generator_class, mock_current_user, sample_stats_data):
        """Test stats validation with specific class."""
        # Setup mocks
        mock_generator = Mock()
        mock_generator.validate_class_prerequisites.return_value = (True, [])
        mock_generator.get_available_classes.return_value = ["investigator", "academic"]
        mock_stats_generator_class.return_value = mock_generator

        result = await validate_character_stats(
            sample_stats_data, "investigator", mock_current_user, stats_generator=mock_generator
        )

        assert result["meets_prerequisites"] is True
        assert result["requested_class"] == "investigator"

    @patch("server.api.players.StatsGenerator")
    @pytest.mark.asyncio
    async def test_validate_stats_invalid_format(self, mock_stats_generator_class, mock_current_user):
        """Test stats validation with invalid format."""
        # Setup mocks
        mock_generator = Mock()
        mock_generator.get_available_classes.side_effect = Exception("Invalid stats format")
        mock_stats_generator_class.return_value = mock_generator

        invalid_stats = {"invalid": "stats", "format": "here"}

        with pytest.raises(HTTPException) as exc_info:
            await validate_character_stats(invalid_stats, None, mock_current_user, stats_generator=mock_generator)

        assert exc_info.value.status_code == 400
        assert "Invalid format" in str(exc_info.value.detail)

    @patch("server.api.players.StatsGenerator")
    @pytest.mark.asyncio
    async def test_get_available_classes(self, mock_stats_generator_class, mock_current_user):
        """Test getting available classes information."""
        # Setup mocks
        mock_generator = Mock()
        mock_generator.CLASS_PREREQUISITES = {
            "investigator": {AttributeType.INT: 12, AttributeType.EDU: 10},
            "occultist": {AttributeType.INT: 14, AttributeType.POW: 12},
        }
        mock_generator.MIN_STAT = 15
        mock_generator.MAX_STAT = 90
        mock_stats_generator_class.return_value = mock_generator

        result = await get_available_classes(mock_current_user, stats_generator=mock_generator)

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
        assert "lucidity" in description.lower()
