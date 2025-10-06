"""
Tests for the player service functionality.

This module tests player-related operations including creation, retrieval,
name resolution, and validation for the chat system.
"""

import uuid
from datetime import datetime
from unittest.mock import AsyncMock, Mock

import pytest

from ..game.player_service import PlayerService


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
            "stats": {"health": 100, "sanity": 100, "strength": 10},
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
            "stats": {"health": 100, "sanity": 100, "strength": 10},
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
            "stats": {"health": 100, "sanity": 100, "strength": 10},
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
                "stats": {"health": 100, "sanity": 100, "strength": 10},
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
                "stats": {"health": 100, "sanity": 100, "strength": 10},
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
            "stats": {"health": 100, "sanity": 100, "strength": 10},
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
