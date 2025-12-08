"""
Greenfield async unit tests for AsyncPersistenceLayer player operations.

These tests cover all player-related persistence operations using the
async persistence layer directly.
"""

from unittest.mock import AsyncMock, Mock
from uuid import uuid4

import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.events.event_bus import EventBus
from server.models.player import Player


class TestAsyncPlayerPersistence:
    """Test async player persistence operations."""

    @pytest.fixture
    def event_bus(self):
        """Create an event bus for testing."""
        return EventBus()

    @pytest.fixture
    def async_persistence(self, event_bus):
        """Create an AsyncPersistenceLayer instance for testing."""
        return AsyncPersistenceLayer(event_bus=event_bus)

    @pytest.fixture
    def sample_player(self):
        """Create a sample player for testing."""
        player = Player(
            player_id=uuid4(),
            name="TestPlayer",
            user_id="test_user_123",
            current_room_id="earth_arkhamcity_downtown_room_derby_st_001",
        )
        return player

    @pytest.mark.asyncio
    async def test_get_player_by_id_exists(self, async_persistence, sample_player):
        """Test getting a player by ID when player exists."""
        # Mock the repository to return the player
        async_persistence._player_repo.get_player_by_id = AsyncMock(return_value=sample_player)

        result = await async_persistence.get_player_by_id(sample_player.player_id)

        assert result is not None
        assert result.player_id == sample_player.player_id
        assert result.name == sample_player.name
        async_persistence._player_repo.get_player_by_id.assert_called_once_with(sample_player.player_id)

    @pytest.mark.asyncio
    async def test_get_player_by_id_not_exists(self, async_persistence):
        """Test getting a player by ID when player does not exist."""
        # Mock the repository to return None
        async_persistence._player_repo.get_player_by_id = AsyncMock(return_value=None)

        player_id = uuid4()
        result = await async_persistence.get_player_by_id(player_id)

        assert result is None
        async_persistence._player_repo.get_player_by_id.assert_called_once_with(player_id)

    @pytest.mark.asyncio
    async def test_get_player_by_name_exists(self, async_persistence, sample_player):
        """Test getting a player by name when player exists."""
        # Mock the repository to return the player
        async_persistence._player_repo.get_player_by_name = AsyncMock(return_value=sample_player)

        result = await async_persistence.get_player_by_name("TestPlayer")

        assert result is not None
        assert result.name == "TestPlayer"
        async_persistence._player_repo.get_player_by_name.assert_called_once_with("TestPlayer")

    @pytest.mark.asyncio
    async def test_get_player_by_name_not_exists(self, async_persistence):
        """Test getting a player by name when player does not exist."""
        # Mock the repository to return None
        async_persistence._player_repo.get_player_by_name = AsyncMock(return_value=None)

        result = await async_persistence.get_player_by_name("NonExistentPlayer")

        assert result is None
        async_persistence._player_repo.get_player_by_name.assert_called_once_with("NonExistentPlayer")

    @pytest.mark.asyncio
    async def test_get_player_by_user_id_exists(self, async_persistence, sample_player):
        """Test getting a player by user ID when player exists."""
        # Mock the repository to return the player
        async_persistence._player_repo.get_player_by_user_id = AsyncMock(return_value=sample_player)

        result = await async_persistence.get_player_by_user_id("test_user_123")

        assert result is not None
        assert result.user_id == "test_user_123"
        async_persistence._player_repo.get_player_by_user_id.assert_called_once_with("test_user_123")

    @pytest.mark.asyncio
    async def test_save_player(self, async_persistence, sample_player):
        """Test saving a player."""
        # Mock the repository save method
        async_persistence._player_repo.save_player = AsyncMock(return_value=None)

        await async_persistence.save_player(sample_player)

        async_persistence._player_repo.save_player.assert_called_once_with(sample_player)

    @pytest.mark.asyncio
    async def test_list_players(self, async_persistence, sample_player):
        """Test listing all players."""
        # Mock the repository to return a list of players
        players = [sample_player]
        async_persistence._player_repo.list_players = AsyncMock(return_value=players)

        result = await async_persistence.list_players()

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0].player_id == sample_player.player_id
        async_persistence._player_repo.list_players.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_player(self, async_persistence):
        """Test deleting a player."""
        player_id = uuid4()
        # Mock the repository to return True (success)
        async_persistence._player_repo.delete_player = AsyncMock(return_value=True)

        result = await async_persistence.delete_player(player_id)

        assert result is True
        async_persistence._player_repo.delete_player.assert_called_once_with(player_id)

    @pytest.mark.asyncio
    async def test_delete_player_not_exists(self, async_persistence):
        """Test deleting a player that does not exist."""
        player_id = uuid4()
        # Mock the repository to return False (not found)
        async_persistence._player_repo.delete_player = AsyncMock(return_value=False)

        result = await async_persistence.delete_player(player_id)

        assert result is False
        async_persistence._player_repo.delete_player.assert_called_once_with(player_id)

    @pytest.mark.asyncio
    async def test_get_players_in_room(self, async_persistence, sample_player):
        """Test getting players in a specific room."""
        room_id = "earth_arkhamcity_downtown_room_derby_st_001"
        # Mock the repository to return players in room
        players = [sample_player]
        async_persistence._player_repo.get_players_in_room = AsyncMock(return_value=players)

        result = await async_persistence.get_players_in_room(room_id)

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0].current_room_id == room_id
        async_persistence._player_repo.get_players_in_room.assert_called_once_with(room_id)

    @pytest.mark.asyncio
    async def test_save_players(self, async_persistence, sample_player):
        """Test saving multiple players."""
        players = [sample_player]
        # Mock the repository save method
        async_persistence._player_repo.save_players = AsyncMock(return_value=None)

        await async_persistence.save_players(players)

        async_persistence._player_repo.save_players.assert_called_once_with(players)

    @pytest.mark.asyncio
    async def test_validate_and_fix_player_room(self, async_persistence, sample_player):
        """Test validating and fixing player room."""
        # Mock the repository validate method
        async_persistence._player_repo.validate_and_fix_player_room = Mock(return_value=True)

        result = async_persistence.validate_and_fix_player_room(sample_player)

        assert result is True
        async_persistence._player_repo.validate_and_fix_player_room.assert_called_once_with(sample_player)
