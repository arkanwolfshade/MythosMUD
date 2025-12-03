"""
Tests for the player service functionality.

This module tests player-related operations including creation, retrieval,
name resolution, and validation for the chat system.
"""

import uuid
from datetime import datetime
from unittest.mock import AsyncMock, Mock

import pytest

from server.exceptions import DatabaseError
from server.exceptions import ValidationError as CustomValidationError
from server.game.player_service import PlayerService
from server.models import Stats
from server.schemas.player import PlayerRead


@pytest.mark.asyncio
class TestPlayerService:
    """Test cases for PlayerService."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a mock persistence object with the required methods
        self.mock_persistence = AsyncMock()
        self.mock_persistence.async_get_player_by_name = AsyncMock()
        self.mock_persistence.async_list_players = AsyncMock()

        # Mock profession data to return proper string values
        mock_profession = Mock()
        mock_profession.name = "Scholar"
        mock_profession.description = "A learned academic"
        mock_profession.flavor_text = "Knowledge is power"
        self.mock_persistence.async_get_profession_by_id = AsyncMock(return_value=mock_profession)

        self.player_service = PlayerService(self.mock_persistence)

    async def test_resolve_player_name_exact_match(self):
        """Test player name resolution with exact match."""
        # Mock player data (as dictionary, like persistence would return)
        mock_player_data = {
            "player_id": str(uuid.uuid4()),
            "user_id": str(uuid.uuid4()),
            "name": "TestPlayer",
            "current_room_id": "test_room_001",
            "experience_points": 100,
            "level": 5,
            "stats": {"health": 100, "lucidity": 100, "strength": 10},
            "inventory": [],
            "status_effects": [],
            "created_at": datetime.now(),
            "last_active": datetime.now(),
        }

        # Mock the persistence method to return our test player
        self.mock_persistence.async_get_player_by_name.return_value = mock_player_data

        # Test exact match
        result = await self.player_service.resolve_player_name("TestPlayer")

        # Verify the result
        assert result is not None
        assert result.name == "TestPlayer"
        assert result.id == uuid.UUID(mock_player_data["player_id"])

        # Verify the persistence method was called correctly
        self.mock_persistence.async_get_player_by_name.assert_called_once_with("TestPlayer")

    async def test_resolve_player_name_case_insensitive(self):
        """Test player name resolution with case-insensitive matching."""
        # Mock player data (as dictionary, like persistence would return)
        mock_player_data = {
            "player_id": str(uuid.uuid4()),
            "user_id": str(uuid.uuid4()),
            "name": "TestPlayer",
            "current_room_id": "test_room_001",
            "experience_points": 100,
            "level": 5,
            "stats": {"health": 100, "lucidity": 100, "strength": 10},
            "inventory": [],
            "status_effects": [],
            "created_at": datetime.now(),
            "last_active": datetime.now(),
        }

        # Mock the persistence methods
        self.mock_persistence.async_get_player_by_name.return_value = None
        self.mock_persistence.async_list_players.return_value = [mock_player_data]

        # Test case-insensitive match
        result = await self.player_service.resolve_player_name("testplayer")

        # Verify the result
        assert result is not None
        assert result.name == "TestPlayer"

    async def test_resolve_player_name_partial_match(self):
        """Test player name resolution with partial matching."""
        # Mock player data (as dictionary, like persistence would return)
        mock_player_data = {
            "player_id": str(uuid.uuid4()),
            "user_id": str(uuid.uuid4()),
            "name": "TestPlayer",
            "current_room_id": "test_room_001",
            "experience_points": 100,
            "level": 5,
            "stats": {"health": 100, "lucidity": 100, "strength": 10},
            "inventory": [],
            "status_effects": [],
            "created_at": datetime.now(),
            "last_active": datetime.now(),
        }

        # Mock the persistence methods
        self.mock_persistence.async_get_player_by_name.return_value = None
        self.mock_persistence.async_list_players.return_value = [mock_player_data]

        # Test partial match
        result = await self.player_service.resolve_player_name("Test")

        # Verify the result
        assert result is not None
        assert result.name == "TestPlayer"

    async def test_resolve_player_name_not_found(self):
        """Test player name resolution when player is not found."""
        # Mock the persistence methods
        self.mock_persistence.async_get_player_by_name.return_value = None
        self.mock_persistence.async_list_players.return_value = []

        # Test with non-existent player
        result = await self.player_service.resolve_player_name("NonExistentPlayer")

        # Verify the result
        assert result is None

    async def test_resolve_player_name_empty_input(self):
        """Test player name resolution with empty input."""
        # Test with empty string
        result = await self.player_service.resolve_player_name("")
        assert result is None

        # Test with whitespace only
        result = await self.player_service.resolve_player_name("   ")
        assert result is None

        # Test with None
        result = await self.player_service.resolve_player_name(None)
        assert result is None

    async def test_resolve_player_name_multiple_candidates(self):
        """Test player name resolution with multiple matching candidates."""
        # Mock multiple players (as dictionaries, like persistence would return)
        mock_players = [
            {
                "player_id": str(uuid.uuid4()),
                "user_id": str(uuid.uuid4()),
                "name": "TestPlayer",
                "current_room_id": "test_room_001",
                "experience_points": 100,
                "level": 5,
                "stats": {"health": 100, "lucidity": 100, "strength": 10},
                "inventory": [],
                "status_effects": [],
                "created_at": datetime.now(),
                "last_active": datetime.now(),
            },
            {
                "player_id": str(uuid.uuid4()),
                "user_id": str(uuid.uuid4()),
                "name": "TestPlayer2",
                "current_room_id": "test_room_002",
                "experience_points": 200,
                "level": 10,
                "stats": {"health": 100, "lucidity": 100, "strength": 10},
                "inventory": [],
                "status_effects": [],
                "created_at": datetime.now(),
                "last_active": datetime.now(),
            },
        ]

        # Mock the persistence methods
        self.mock_persistence.async_get_player_by_name.return_value = None
        self.mock_persistence.async_list_players.return_value = mock_players

        # Test partial match that could match multiple players
        result = await self.player_service.resolve_player_name("Test")

        # Should return the first match (TestPlayer)
        assert result is not None
        assert result.name == "TestPlayer"

    async def test_resolve_player_name_special_characters(self):
        """Test player name resolution with special characters."""
        # Mock player data (as dictionary, like persistence would return)
        mock_player_data = {
            "player_id": str(uuid.uuid4()),
            "user_id": str(uuid.uuid4()),
            "name": "Test-Player_123",
            "current_room_id": "test_room_001",
            "experience_points": 100,
            "level": 5,
            "stats": {"health": 100, "lucidity": 100, "strength": 10},
            "inventory": [],
            "status_effects": [],
            "created_at": datetime.now(),
            "last_active": datetime.now(),
        }

        # Mock the persistence methods
        self.mock_persistence.async_get_player_by_name.return_value = None
        self.mock_persistence.async_list_players.return_value = [mock_player_data]

        # Test with special characters
        result = await self.player_service.resolve_player_name("test-player")

        # Verify the result
        assert result is not None
        assert result.name == "Test-Player_123"


# ============================================================================
# Tests merged from test_player_service_layer_legacy.py
# ============================================================================


"""
Tests for PlayerService layer implementation.

This module tests the PlayerService to ensure proper business logic
separation and service layer functionality.
"""


class TestPlayerServiceLayer:
    """Test the PlayerService layer functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.mock_persistence = AsyncMock()
        self.player_service = PlayerService(self.mock_persistence)

    def test_player_service_initialization(self):
        """Test that PlayerService initializes correctly."""
        assert self.player_service.persistence == self.mock_persistence

    @pytest.mark.asyncio
    async def test_create_player_success(self):
        """Test successful player creation."""
        # Mock persistence methods
        self.mock_persistence.async_get_player_by_name.return_value = None
        self.mock_persistence.async_save_player.return_value = None
        self.mock_persistence.async_get_profession_by_id.return_value = None

        # Create player
        result = await self.player_service.create_player("TestPlayer")

        # Verify result
        assert isinstance(result, PlayerRead)
        assert result.name == "TestPlayer"
        assert result.profession_id == 0
        assert result.current_room_id == "earth_arkhamcity_sanitarium_room_foyer_001"

        # Verify persistence calls
        self.mock_persistence.async_get_player_by_name.assert_called_once_with("TestPlayer")
        self.mock_persistence.async_save_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_create_player_name_already_exists(self):
        """Test player creation fails when name already exists."""
        # Mock existing player
        existing_player = Mock()
        existing_player.player_id = uuid.uuid4()
        self.mock_persistence.async_get_player_by_name.return_value = existing_player

        # Attempt to create player with existing name
        with pytest.raises(CustomValidationError) as exc_info:
            await self.player_service.create_player("ExistingPlayer")

        assert "Player name already exists" in str(exc_info.value)
        self.mock_persistence.async_get_player_by_name.assert_called_once_with("ExistingPlayer")
        self.mock_persistence.async_save_player.assert_not_called()

    @pytest.mark.asyncio
    async def test_create_player_with_stats_success(self):
        """Test successful player creation with custom stats."""
        # Mock persistence methods
        self.mock_persistence.async_get_player_by_name.return_value = None
        self.mock_persistence.async_save_player.return_value = None
        self.mock_persistence.async_get_profession_by_id.return_value = None

        # Create stats
        stats = Stats(strength=15, dexterity=12, constitution=14, intelligence=13, wisdom=11, charisma=10)

        # Create player with stats
        result = await self.player_service.create_player_with_stats("TestPlayer", stats)

        # Verify result
        assert isinstance(result, PlayerRead)
        assert result.name == "TestPlayer"
        assert result.stats == stats.model_dump()

        # Verify persistence calls
        self.mock_persistence.async_get_player_by_name.assert_called_once_with("TestPlayer")
        self.mock_persistence.async_save_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_player_by_id_success(self):
        """Test successful player retrieval by ID."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.user_id = uuid.uuid4()
        mock_player.name = "TestPlayer"
        mock_player.profession_id = 0
        mock_player.current_room_id = "test_room"
        mock_player.experience_points = 0
        mock_player.level = 1
        mock_player.get_stats.return_value = {}
        mock_player.get_inventory.return_value = []
        mock_player.get_status_effects.return_value = []
        mock_player.created_at = "2023-01-01T00:00:00"
        mock_player.last_active = "2023-01-01T00:00:00"
        mock_player.is_admin = 0

        self.mock_persistence.async_get_player.return_value = mock_player
        self.mock_persistence.async_get_profession_by_id.return_value = None

        # Get player
        result = await self.player_service.get_player_by_id(str(mock_player.player_id))

        # Verify result
        assert isinstance(result, PlayerRead)
        assert result.id == mock_player.player_id
        assert result.name == "TestPlayer"

        # Verify persistence calls
        self.mock_persistence.async_get_player.assert_called_once_with(str(mock_player.player_id))

    @pytest.mark.asyncio
    async def test_get_player_by_id_not_found(self):
        """Test player retrieval by ID when player doesn't exist."""
        self.mock_persistence.async_get_player.return_value = None

        # Get non-existent player
        result = await self.player_service.get_player_by_id("nonexistent-id")

        # Verify result
        assert result is None
        self.mock_persistence.async_get_player.assert_called_once_with("nonexistent-id")

    @pytest.mark.asyncio
    async def test_get_player_by_name_success(self):
        """Test successful player retrieval by name."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.user_id = uuid.uuid4()
        mock_player.name = "TestPlayer"
        mock_player.profession_id = 0
        mock_player.current_room_id = "test_room"
        mock_player.experience_points = 0
        mock_player.level = 1
        mock_player.get_stats.return_value = {}
        mock_player.get_inventory.return_value = []
        mock_player.get_status_effects.return_value = []
        mock_player.created_at = "2023-01-01T00:00:00"
        mock_player.last_active = "2023-01-01T00:00:00"
        mock_player.is_admin = 0

        self.mock_persistence.async_get_player_by_name.return_value = mock_player
        self.mock_persistence.async_get_profession_by_id.return_value = None

        # Get player
        result = await self.player_service.get_player_by_name("TestPlayer")

        # Verify result
        assert isinstance(result, PlayerRead)
        assert result.name == "TestPlayer"

        # Verify persistence calls
        self.mock_persistence.async_get_player_by_name.assert_called_once_with("TestPlayer")

    @pytest.mark.asyncio
    async def test_list_players_success(self):
        """Test successful player listing."""
        # Mock player data
        mock_player1 = Mock()
        mock_player1.player_id = uuid.uuid4()
        mock_player1.user_id = uuid.uuid4()
        mock_player1.name = "Player1"
        mock_player1.profession_id = 0
        mock_player1.current_room_id = "test_room"
        mock_player1.experience_points = 0
        mock_player1.level = 1
        mock_player1.get_stats.return_value = {}
        mock_player1.get_inventory.return_value = []
        mock_player1.get_status_effects.return_value = []
        mock_player1.created_at = "2023-01-01T00:00:00"
        mock_player1.last_active = "2023-01-01T00:00:00"
        mock_player1.is_admin = 0

        mock_player2 = Mock()
        mock_player2.player_id = uuid.uuid4()
        mock_player2.user_id = uuid.uuid4()
        mock_player2.name = "Player2"
        mock_player2.profession_id = 1
        mock_player2.current_room_id = "test_room2"
        mock_player2.experience_points = 100
        mock_player2.level = 2
        mock_player2.get_stats.return_value = {}
        mock_player2.get_inventory.return_value = []
        mock_player2.get_status_effects.return_value = []
        mock_player2.created_at = "2023-01-01T00:00:00"
        mock_player2.last_active = "2023-01-01T00:00:00"
        mock_player2.is_admin = 0

        self.mock_persistence.async_list_players.return_value = [mock_player1, mock_player2]
        self.mock_persistence.async_get_profession_by_id.return_value = None

        # List players
        result = await self.player_service.list_players()

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(player, PlayerRead) for player in result)
        assert result[0].name == "Player1"
        assert result[1].name == "Player2"

        # Verify persistence calls
        self.mock_persistence.async_list_players.assert_called_once()

    @pytest.mark.asyncio
    async def test_resolve_player_name_exact_match(self):
        """Test player name resolution with exact match."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.user_id = uuid.uuid4()
        mock_player.name = "TestPlayer"
        mock_player.profession_id = 0
        mock_player.current_room_id = "test_room"
        mock_player.experience_points = 0
        mock_player.level = 1
        mock_player.get_stats.return_value = {}
        mock_player.get_inventory.return_value = []
        mock_player.get_status_effects.return_value = []
        mock_player.created_at = "2023-01-01T00:00:00"
        mock_player.last_active = "2023-01-01T00:00:00"
        mock_player.is_admin = 0

        self.mock_persistence.async_get_player_by_name.return_value = mock_player
        self.mock_persistence.async_get_profession_by_id.return_value = None

        # Resolve player name
        result = await self.player_service.resolve_player_name("TestPlayer")

        # Verify result
        assert isinstance(result, PlayerRead)
        assert result.name == "TestPlayer"

    @pytest.mark.asyncio
    async def test_resolve_player_name_case_insensitive(self):
        """Test player name resolution with case-insensitive matching."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.user_id = uuid.uuid4()
        mock_player.name = "TestPlayer"
        mock_player.profession_id = 0
        mock_player.current_room_id = "test_room"
        mock_player.experience_points = 0
        mock_player.level = 1
        mock_player.get_stats.return_value = {}
        mock_player.get_inventory.return_value = []
        mock_player.get_status_effects.return_value = []
        mock_player.created_at = "2023-01-01T00:00:00"
        mock_player.last_active = "2023-01-01T00:00:00"
        mock_player.is_admin = 0

        # Mock no exact match, but return player in list
        self.mock_persistence.async_get_player_by_name.return_value = None
        self.mock_persistence.async_list_players.return_value = [mock_player]
        self.mock_persistence.async_get_profession_by_id.return_value = None

        # Resolve player name with different case
        result = await self.player_service.resolve_player_name("testplayer")

        # Verify result
        assert isinstance(result, PlayerRead)
        assert result.name == "TestPlayer"

    @pytest.mark.asyncio
    async def test_validate_player_name_valid(self):
        """Test player name validation with valid name."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.user_id = uuid.uuid4()
        mock_player.name = "TestPlayer"
        mock_player.profession_id = 0
        mock_player.current_room_id = "test_room"
        mock_player.experience_points = 0
        mock_player.level = 1
        mock_player.get_stats.return_value = {}
        mock_player.get_inventory.return_value = []
        mock_player.get_status_effects.return_value = []
        mock_player.created_at = "2023-01-01T00:00:00"
        mock_player.last_active = "2023-01-01T00:00:00"
        mock_player.is_admin = 0

        self.mock_persistence.async_get_player_by_name.return_value = None
        self.mock_persistence.async_list_players.return_value = [mock_player]
        self.mock_persistence.async_get_profession_by_id.return_value = None

        # Validate player name
        is_valid, message = await self.player_service.validate_player_name("TestPlayer")

        # Verify result
        assert is_valid is True
        assert message == "Valid player name"

    @pytest.mark.asyncio
    async def test_validate_player_name_invalid_empty(self):
        """Test player name validation with empty name."""
        # Validate empty player name
        is_valid, message = await self.player_service.validate_player_name("")

        # Verify result
        assert is_valid is False
        assert message == "Player name cannot be empty"

    @pytest.mark.asyncio
    async def test_validate_player_name_invalid_too_short(self):
        """Test player name validation with name too short."""
        # Validate short player name
        is_valid, message = await self.player_service.validate_player_name("A")

        # Verify result
        assert is_valid is False
        assert message == "Player name must be at least 2 characters long"

    @pytest.mark.asyncio
    async def test_validate_player_name_invalid_characters(self):
        """Test player name validation with invalid characters."""
        # Validate player name with invalid characters
        is_valid, message = await self.player_service.validate_player_name("Test<Player>")

        # Verify result
        assert is_valid is False
        assert "'<'" in message

    @pytest.mark.asyncio
    async def test_delete_player_success(self):
        """Test successful player deletion."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.name = "TestPlayer"

        self.mock_persistence.async_get_player.return_value = mock_player
        self.mock_persistence.async_delete_player.return_value = True

        # Delete player
        success, message = await self.player_service.delete_player(str(mock_player.player_id))

        # Verify result
        assert success is True
        assert "TestPlayer" in message

        # Verify persistence calls
        self.mock_persistence.async_get_player.assert_called_once_with(str(mock_player.player_id))
        self.mock_persistence.async_delete_player.assert_called_once_with(str(mock_player.player_id))

    @pytest.mark.asyncio
    async def test_delete_player_not_found(self):
        """Test player deletion when player doesn't exist."""
        self.mock_persistence.async_get_player.return_value = None

        # Attempt to delete non-existent player
        with pytest.raises(CustomValidationError) as exc_info:
            await self.player_service.delete_player("nonexistent-id")

        assert "Player not found for deletion" in str(exc_info.value)
        self.mock_persistence.async_get_player.assert_called_once_with("nonexistent-id")
        self.mock_persistence.async_delete_player.assert_not_called()

    @pytest.mark.asyncio
    async def test_update_player_location_success(self):
        """Test successful player location update."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.name = "TestPlayer"
        mock_player.current_room_id = "old_room"

        self.mock_persistence.async_get_player_by_name.return_value = mock_player
        self.mock_persistence.async_save_player.return_value = None

        # Update player location
        result = await self.player_service.update_player_location("TestPlayer", "new_room")

        # Verify result
        assert result is True
        assert mock_player.current_room_id == "new_room"

        # Verify persistence calls
        self.mock_persistence.async_get_player_by_name.assert_called_once_with("TestPlayer")
        self.mock_persistence.async_save_player.assert_called_once_with(mock_player)

    @pytest.mark.asyncio
    async def test_update_player_location_not_found(self):
        """Test player location update when player doesn't exist."""
        self.mock_persistence.async_get_player_by_name.return_value = None

        # Attempt to update location for non-existent player
        with pytest.raises(DatabaseError) as exc_info:
            await self.player_service.update_player_location("NonexistentPlayer", "new_room")

        assert "Failed to update player location" in str(exc_info.value)
        self.mock_persistence.async_get_player_by_name.assert_called_once_with("NonexistentPlayer")
        self.mock_persistence.async_save_player.assert_not_called()

    @pytest.mark.asyncio
    async def test_search_players_by_name_success(self):
        """Test successful player search by name."""
        # Mock player data
        mock_player1 = Mock()
        mock_player1.player_id = uuid.uuid4()
        mock_player1.user_id = uuid.uuid4()
        mock_player1.name = "TestPlayer"
        mock_player1.profession_id = 0
        mock_player1.current_room_id = "test_room"
        mock_player1.experience_points = 0
        mock_player1.level = 1
        mock_player1.get_stats.return_value = {}
        mock_player1.get_inventory.return_value = []
        mock_player1.get_status_effects.return_value = []
        mock_player1.created_at = "2023-01-01T00:00:00"
        mock_player1.last_active = "2023-01-01T00:00:00"
        mock_player1.is_admin = 0

        mock_player2 = Mock()
        mock_player2.player_id = uuid.uuid4()
        mock_player2.user_id = uuid.uuid4()
        mock_player2.name = "TestPlayer2"
        mock_player2.profession_id = 0
        mock_player2.current_room_id = "test_room"
        mock_player2.experience_points = 0
        mock_player2.level = 1
        mock_player2.get_stats.return_value = {}
        mock_player2.get_inventory.return_value = []
        mock_player2.get_status_effects.return_value = []
        mock_player2.created_at = "2023-01-01T00:00:00"
        mock_player2.last_active = "2023-01-01T00:00:00"
        mock_player2.is_admin = 0

        self.mock_persistence.async_list_players.return_value = [mock_player1, mock_player2]
        self.mock_persistence.async_get_profession_by_id.return_value = None

        # Search players
        result = await self.player_service.search_players_by_name("Test")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(player, PlayerRead) for player in result)
        assert result[0].name == "TestPlayer"  # Exact match should be first
        assert result[1].name == "TestPlayer2"

        # Verify persistence calls
        self.mock_persistence.async_list_players.assert_called_once()

    @pytest.mark.asyncio
    async def test_search_players_by_name_empty_term(self):
        """Test player search with empty search term."""
        # Search with empty term
        result = await self.player_service.search_players_by_name("")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 0
        self.mock_persistence.async_list_players.assert_not_called()

    @pytest.mark.asyncio
    async def test_get_online_players(self):
        """Test getting online players."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.user_id = uuid.uuid4()
        mock_player.name = "TestPlayer"
        mock_player.profession_id = 0
        mock_player.current_room_id = "test_room"
        mock_player.experience_points = 0
        mock_player.level = 1
        mock_player.get_stats.return_value = {}
        mock_player.get_inventory.return_value = []
        mock_player.get_status_effects.return_value = []
        mock_player.created_at = "2023-01-01T00:00:00"
        mock_player.last_active = "2023-01-01T00:00:00"
        mock_player.is_admin = 0

        self.mock_persistence.async_list_players.return_value = [mock_player]
        self.mock_persistence.async_get_profession_by_id.return_value = None

        # Get online players
        result = await self.player_service.get_online_players()

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PlayerRead)
        assert result[0].name == "TestPlayer"

        # Verify persistence calls
        self.mock_persistence.async_list_players.assert_called_once()

    @pytest.mark.asyncio
    async def test_apply_Lucidity_loss_success(self):
        """Test successful lucidity loss application."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.name = "TestPlayer"

        self.mock_persistence.async_get_player.return_value = mock_player
        self.mock_persistence.async_apply_Lucidity_loss.return_value = None

        # Apply lucidity loss
        result = await self.player_service.apply_lucidity_loss("test-player-id", 10, "test-source")

        # Verify result
        assert isinstance(result, dict)
        assert "Applied 10 lucidity loss to TestPlayer" in result["message"]

        # Verify persistence calls
        self.mock_persistence.async_get_player.assert_called_once_with("test-player-id")
        self.mock_persistence.async_apply_Lucidity_loss.assert_called_once_with(mock_player, 10, "test-source")

    @pytest.mark.asyncio
    async def test_apply_Lucidity_loss_player_not_found(self):
        """Test lucidity loss application when player doesn't exist."""
        self.mock_persistence.async_get_player.return_value = None

        # Attempt to apply lucidity loss to non-existent player
        with pytest.raises(CustomValidationError) as exc_info:
            await self.player_service.apply_lucidity_loss("nonexistent-id", 10, "test-source")

        assert "Player not found: nonexistent-id" in str(exc_info.value)
        self.mock_persistence.async_get_player.assert_called_once_with("nonexistent-id")
        self.mock_persistence.async_apply_Lucidity_loss.assert_not_called()

    @pytest.mark.asyncio
    async def test_apply_fear_success(self):
        """Test successful fear application."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.name = "TestPlayer"

        self.mock_persistence.async_get_player.return_value = mock_player
        self.mock_persistence.async_apply_fear.return_value = None

        # Apply fear
        result = await self.player_service.apply_fear("test-player-id", 5, "test-source")

        # Verify result
        assert isinstance(result, dict)
        assert "Applied 5 fear to TestPlayer" in result["message"]

        # Verify persistence calls
        self.mock_persistence.async_get_player.assert_called_once_with("test-player-id")
        self.mock_persistence.async_apply_fear.assert_called_once_with(mock_player, 5, "test-source")

    @pytest.mark.asyncio
    async def test_apply_corruption_success(self):
        """Test successful corruption application."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.name = "TestPlayer"

        self.mock_persistence.async_get_player.return_value = mock_player
        self.mock_persistence.async_apply_corruption.return_value = None

        # Apply corruption
        result = await self.player_service.apply_corruption("test-player-id", 3, "test-source")

        # Verify result
        assert isinstance(result, dict)
        assert "Applied 3 corruption to TestPlayer" in result["message"]

        # Verify persistence calls
        self.mock_persistence.async_get_player.assert_called_once_with("test-player-id")
        self.mock_persistence.async_apply_corruption.assert_called_once_with(mock_player, 3, "test-source")

    @pytest.mark.asyncio
    async def test_gain_occult_knowledge_success(self):
        """Test successful occult knowledge gain."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.name = "TestPlayer"

        self.mock_persistence.async_get_player.return_value = mock_player
        self.mock_persistence.async_gain_occult_knowledge.return_value = None

        # Gain occult knowledge
        result = await self.player_service.gain_occult_knowledge("test-player-id", 15, "test-source")

        # Verify result
        assert isinstance(result, dict)
        assert "Gained 15 occult knowledge for TestPlayer" in result["message"]

        # Verify persistence calls
        self.mock_persistence.async_get_player.assert_called_once_with("test-player-id")
        self.mock_persistence.async_gain_occult_knowledge.assert_called_once_with(mock_player, 15, "test-source")

    @pytest.mark.asyncio
    async def test_heal_player_success(self):
        """Test successful player healing."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.name = "TestPlayer"

        self.mock_persistence.async_get_player.return_value = mock_player
        self.mock_persistence.async_heal_player.return_value = None

        # Heal player
        result = await self.player_service.heal_player("test-player-id", 20)

        # Verify result
        assert isinstance(result, dict)
        assert "Healed TestPlayer for 20 health" in result["message"]

        # Verify persistence calls
        self.mock_persistence.async_get_player.assert_called_once_with("test-player-id")
        self.mock_persistence.async_heal_player.assert_called_once_with(mock_player, 20)

    @pytest.mark.asyncio
    async def test_damage_player_success(self):
        """Test successful player damage."""
        # Mock player data
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.name = "TestPlayer"

        self.mock_persistence.async_get_player.return_value = mock_player
        self.mock_persistence.async_damage_player.return_value = None

        # Damage player
        result = await self.player_service.damage_player("test-player-id", 15, "magical")

        # Verify result
        assert isinstance(result, dict)
        assert "Damaged TestPlayer for 15 magical damage" in result["message"]

        # Verify persistence calls
        self.mock_persistence.async_get_player.assert_called_once_with("test-player-id")
        self.mock_persistence.async_damage_player.assert_called_once_with(mock_player, 15, "magical")
