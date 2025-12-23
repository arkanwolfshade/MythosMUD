"""
Tests for PlayerService.

This module tests the PlayerService class covering player creation, retrieval,
validation, state management, and various player operations.
"""


# pylint: disable=redefined-outer-name
# Justification: pytest fixtures redefine names

from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, Mock
from uuid import uuid4

import pytest

from server.exceptions import DatabaseError, ValidationError
from server.game.player_service import PlayerService
from server.models.player import Player
from server.schemas.player import PlayerRead


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock()
    persistence.get_player_by_name = AsyncMock()
    persistence.list_players = AsyncMock()
    persistence.get_active_players_by_user_id = AsyncMock()
    persistence.save_player = AsyncMock()
    persistence.delete_player = AsyncMock()
    persistence.soft_delete_player = AsyncMock()
    persistence.apply_lucidity_loss = AsyncMock()
    persistence.apply_fear = AsyncMock()
    persistence.apply_corruption = AsyncMock()
    persistence.async_gain_occult_knowledge = AsyncMock()
    persistence.async_heal_player = AsyncMock()
    persistence.async_damage_player = AsyncMock()
    persistence.get_profession_by_id = AsyncMock()
    persistence.get_room_by_id = Mock()
    return persistence


@pytest.fixture
def player_service(mock_persistence):
    """Create a PlayerService instance for testing."""
    return PlayerService(persistence=mock_persistence)


@pytest.fixture
def sample_player():
    """Create a sample player mock."""
    player = Mock(spec=Player)
    player.player_id = uuid4()
    player.user_id = uuid4()
    player.name = "TestPlayer"
    player.current_room_id = "test_room_001"
    player.profession_id = 0
    player.is_deleted = False
    player.experience_points = 0
    player.level = 1
    player.created_at = datetime.now(UTC).replace(tzinfo=None)
    player.last_active = datetime.now(UTC).replace(tzinfo=None)
    player.is_admin = False
    player.get_stats.return_value = {
        "current_dp": 100,
        "max_dp": 100,
        "lucidity": 50,
        "fear": 0,
        "corruption": 0,
        "occult_knowledge": 0,
        "position": "standing",
        "constitution": 50,
        "size": 50,
    }
    player.get_inventory.return_value = []
    player.get_status_effects.return_value = []
    return player


@pytest.fixture
def sample_player_read(sample_player):
    """Create a PlayerRead schema from sample player."""
    return PlayerRead(
        id=str(sample_player.player_id),
        name=sample_player.name,
        current_room_id=sample_player.current_room_id,
        profession_id=sample_player.profession_id,
        stats=sample_player.get_stats(),
        inventory=[],
        status_effects=[],
    )


class TestPlayerServiceRetrieval:
    """Test player retrieval methods."""

    @pytest.mark.asyncio
    async def test_get_player_by_id_success(self, player_service, mock_persistence, sample_player):
        """Test successful player retrieval by ID."""
        mock_persistence.get_player_by_id.return_value = sample_player
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.get_player_by_id(sample_player.player_id)

        assert result is not None
        assert result.name == sample_player.name
        mock_persistence.get_player_by_id.assert_called_once_with(sample_player.player_id)

    @pytest.mark.asyncio
    async def test_get_player_by_id_not_found(self, player_service, mock_persistence):
        """Test player retrieval when player doesn't exist."""
        mock_persistence.get_player_by_id.return_value = None

        result = await player_service.get_player_by_id(uuid4())

        assert result is None
        mock_persistence.get_player_by_id.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_player_by_name_success(self, player_service, mock_persistence, sample_player):
        """Test successful player retrieval by name."""
        mock_persistence.get_player_by_name.return_value = sample_player
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.get_player_by_name("TestPlayer")

        assert result is not None
        assert result.name == sample_player.name
        mock_persistence.get_player_by_name.assert_called_once_with("TestPlayer")

    @pytest.mark.asyncio
    async def test_get_player_by_name_not_found(self, player_service, mock_persistence):
        """Test player retrieval by name when player doesn't exist."""
        mock_persistence.get_player_by_name.return_value = None

        result = await player_service.get_player_by_name("NonExistent")

        assert result is None

    @pytest.mark.asyncio
    async def test_list_players_success(self, player_service, mock_persistence, sample_player):
        """Test listing all players."""
        mock_persistence.list_players.return_value = [sample_player]
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.list_players()

        assert len(result) == 1
        assert result[0].name == sample_player.name
        mock_persistence.list_players.assert_called_once()


class TestPlayerServiceNameResolution:
    """Test player name resolution and fuzzy matching."""

    @pytest.mark.asyncio
    async def test_resolve_player_name_exact_match(self, player_service, mock_persistence, sample_player):
        """Test resolving player name with exact match."""
        mock_persistence.get_player_by_name.return_value = sample_player
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.resolve_player_name("TestPlayer")

        assert result is not None
        assert result.name == sample_player.name
        # Should use get_player_by_name for exact match
        mock_persistence.get_player_by_name.assert_called_with("TestPlayer")

    @pytest.mark.asyncio
    async def test_resolve_player_name_case_insensitive(self, player_service, mock_persistence, sample_player):
        """Test resolving player name with case-insensitive match."""
        mock_persistence.get_player_by_name.side_effect = [None]  # Exact match fails
        mock_persistence.list_players.return_value = [sample_player]
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.resolve_player_name("testplayer")

        assert result is not None
        assert result.name == sample_player.name

    @pytest.mark.asyncio
    async def test_resolve_player_name_partial_match_starts_with(self, player_service, mock_persistence, sample_player):
        """Test resolving player name with partial match (starts with)."""
        mock_persistence.get_player_by_name.side_effect = [None]  # Exact match fails
        mock_persistence.list_players.return_value = [sample_player]
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.resolve_player_name("Test")

        assert result is not None
        assert result.name == sample_player.name

    @pytest.mark.asyncio
    async def test_resolve_player_name_partial_match_contains(self, player_service, mock_persistence, sample_player):
        """Test resolving player name with partial match (contains)."""
        other_player = Mock(spec=Player)
        other_player.name = "OtherPlayer"
        other_player.player_id = uuid4()
        other_player.user_id = uuid4()
        other_player.experience_points = 0
        other_player.level = 1
        other_player.created_at = datetime.now(UTC).replace(tzinfo=None)
        other_player.last_active = datetime.now(UTC).replace(tzinfo=None)
        other_player.is_admin = False
        other_player.profession_id = 0
        other_player.current_room_id = "test_room"
        other_player.get_stats.return_value = {"position": "standing", "constitution": 50, "size": 50}
        other_player.get_inventory.return_value = []
        other_player.get_status_effects.return_value = []
        mock_persistence.get_player_by_name.side_effect = [None]
        mock_persistence.list_players.return_value = [other_player, sample_player]
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.resolve_player_name("Player")

        assert result is not None
        # Should match first player with "Player" in name
        assert result.name == other_player.name

    @pytest.mark.asyncio
    async def test_resolve_player_name_empty_string(self, player_service, mock_persistence):
        """Test resolving empty player name returns None."""
        result = await player_service.resolve_player_name("")

        assert result is None
        mock_persistence.get_player_by_name.assert_not_called()

    @pytest.mark.asyncio
    async def test_resolve_player_name_not_found(self, player_service, mock_persistence):
        """Test resolving player name when no match found."""
        mock_persistence.get_player_by_name.return_value = None
        mock_persistence.list_players.return_value = []

        result = await player_service.resolve_player_name("NonExistent")

        assert result is None

    @pytest.mark.asyncio
    async def test_search_players_by_name_exact_match(self, player_service, mock_persistence, sample_player):
        """Test searching players by name with exact match."""
        mock_persistence.list_players.return_value = [sample_player]
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.search_players_by_name("TestPlayer")

        assert len(result) == 1
        assert result[0].name == sample_player.name

    @pytest.mark.asyncio
    async def test_search_players_by_name_starts_with(self, player_service, mock_persistence, sample_player):
        """Test searching players by name with starts-with match."""
        mock_persistence.list_players.return_value = [sample_player]
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.search_players_by_name("Test")

        assert len(result) == 1
        assert result[0].name == sample_player.name

    @pytest.mark.asyncio
    async def test_search_players_by_name_contains(self, player_service, mock_persistence, sample_player):
        """Test searching players by name with contains match."""
        mock_persistence.list_players.return_value = [sample_player]
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.search_players_by_name("Player")

        assert len(result) == 1
        assert result[0].name == sample_player.name

    @pytest.mark.asyncio
    async def test_search_players_by_name_limit(self, player_service, mock_persistence):
        """Test searching players respects limit."""
        players = []
        for i in range(20):
            player = Mock(spec=Player)
            player.name = f"TestPlayer{i}"
            player.player_id = uuid4()
            player.user_id = uuid4()
            player.experience_points = 0
            player.level = 1
            player.created_at = datetime.now(UTC).replace(tzinfo=None)
            player.last_active = datetime.now(UTC).replace(tzinfo=None)
            player.is_admin = False
            player.profession_id = 0
            player.current_room_id = "test_room"
            player.get_stats.return_value = {"position": "standing", "constitution": 50, "size": 50}
            player.get_inventory.return_value = []
            player.get_status_effects.return_value = []
            players.append(player)
        mock_persistence.list_players.return_value = players
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.search_players_by_name("Test", limit=5)

        assert len(result) == 5

    @pytest.mark.asyncio
    async def test_search_players_by_name_empty_term(self, player_service, mock_persistence):
        """Test searching with empty term returns empty list."""
        result = await player_service.search_players_by_name("")

        assert result == []

    @pytest.mark.asyncio
    async def test_validate_player_name_valid(self, player_service, mock_persistence, sample_player):
        """Test validating a valid player name."""
        mock_persistence.get_player_by_name.return_value = sample_player
        mock_persistence.list_players.return_value = [sample_player]
        mock_persistence.get_profession_by_id.return_value = None

        is_valid, message = await player_service.validate_player_name("TestPlayer")

        assert is_valid is True
        assert "Valid" in message

    @pytest.mark.asyncio
    async def test_validate_player_name_too_short(self, player_service, mock_persistence):
        """Test validating a player name that's too short."""
        is_valid, message = await player_service.validate_player_name("A")

        assert is_valid is False
        assert "2 characters" in message

    @pytest.mark.asyncio
    async def test_validate_player_name_too_long(self, player_service, mock_persistence):
        """Test validating a player name that's too long."""
        long_name = "A" * 21
        is_valid, message = await player_service.validate_player_name(long_name)

        assert is_valid is False
        assert "20 characters" in message

    @pytest.mark.asyncio
    async def test_validate_player_name_invalid_chars(self, player_service, mock_persistence):
        """Test validating a player name with invalid characters."""
        invalid_names = ["<Player>", "Player&", 'Player"', "Player'", "Player\\", "Player/"]
        for invalid_name in invalid_names:
            is_valid, message = await player_service.validate_player_name(invalid_name)
            assert is_valid is False
            assert "cannot contain" in message

    @pytest.mark.asyncio
    async def test_validate_player_name_not_found(self, player_service, mock_persistence):
        """Test validating a player name that doesn't exist."""
        mock_persistence.get_player_by_name.return_value = None
        mock_persistence.list_players.return_value = []

        is_valid, message = await player_service.validate_player_name("NonExistent")

        assert is_valid is False
        assert "not found" in message


class TestPlayerServiceMultiCharacter:
    """Test multi-character support methods."""

    @pytest.mark.asyncio
    async def test_get_user_characters_success(self, player_service, mock_persistence, sample_player):
        """Test getting all characters for a user."""
        user_id = sample_player.user_id
        mock_persistence.get_active_players_by_user_id.return_value = [sample_player]
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.get_user_characters(user_id)

        assert len(result) == 1
        assert result[0].name == sample_player.name
        mock_persistence.get_active_players_by_user_id.assert_called_once_with(str(user_id))

    @pytest.mark.asyncio
    async def test_soft_delete_character_success(self, player_service, mock_persistence, sample_player):
        """Test successfully soft-deleting a character."""
        user_id = sample_player.user_id
        mock_persistence.get_player_by_id.return_value = sample_player
        mock_persistence.soft_delete_player.return_value = True

        success, message = await player_service.soft_delete_character(sample_player.player_id, user_id)

        assert success is True
        assert "deleted" in message.lower()
        mock_persistence.soft_delete_player.assert_called_once_with(sample_player.player_id)

    @pytest.mark.asyncio
    async def test_soft_delete_character_not_found(self, player_service, mock_persistence):
        """Test soft-deleting a character that doesn't exist."""
        player_id = uuid4()
        user_id = uuid4()
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Character not found"):
            await player_service.soft_delete_character(player_id, user_id)

    @pytest.mark.asyncio
    async def test_soft_delete_character_wrong_owner(self, player_service, mock_persistence, sample_player):
        """Test soft-deleting a character that belongs to another user."""
        wrong_user_id = uuid4()
        mock_persistence.get_player_by_id.return_value = sample_player

        with pytest.raises(ValidationError, match="does not belong to user"):
            await player_service.soft_delete_character(sample_player.player_id, wrong_user_id)

    @pytest.mark.asyncio
    async def test_soft_delete_character_already_deleted(self, player_service, mock_persistence, sample_player):
        """Test soft-deleting a character that's already deleted."""
        user_id = sample_player.user_id
        sample_player.is_deleted = True
        mock_persistence.get_player_by_id.return_value = sample_player

        success, message = await player_service.soft_delete_character(sample_player.player_id, user_id)

        assert success is False
        assert "already deleted" in message.lower()


class TestPlayerServiceLocation:
    """Test player location update methods."""

    @pytest.mark.asyncio
    async def test_update_player_location_success(self, player_service, mock_persistence, sample_player):
        """Test successfully updating player location."""
        mock_persistence.get_player_by_name.return_value = sample_player
        mock_persistence.save_player.return_value = None

        result = await player_service.update_player_location("TestPlayer", "new_room_002")

        assert result is True
        assert sample_player.current_room_id == "new_room_002"
        mock_persistence.save_player.assert_called_once_with(sample_player)

    @pytest.mark.asyncio
    async def test_update_player_location_not_found(self, player_service, mock_persistence):
        """Test updating location for non-existent player."""
        mock_persistence.get_player_by_name.return_value = None

        with pytest.raises(ValidationError, match="Player not found"):
            await player_service.update_player_location("NonExistent", "new_room_002")

    @pytest.mark.asyncio
    async def test_update_player_location_database_error(self, player_service, mock_persistence, sample_player):
        """Test updating location when database error occurs."""
        mock_persistence.get_player_by_name.return_value = sample_player
        mock_persistence.save_player.side_effect = DatabaseError("Database error")

        with pytest.raises(DatabaseError):
            await player_service.update_player_location("TestPlayer", "new_room_002")


class TestPlayerServiceStatsModification:
    """Test player stat modification methods."""

    @pytest.mark.asyncio
    async def test_apply_lucidity_loss_success(self, player_service, mock_persistence, sample_player):
        """Test successfully applying lucidity loss."""
        mock_persistence.get_player_by_id.return_value = sample_player
        mock_persistence.apply_lucidity_loss.return_value = None

        result = await player_service.apply_lucidity_loss(sample_player.player_id, 10, "test_source")

        assert "message" in result
        assert "lucidity loss" in result["message"]
        mock_persistence.apply_lucidity_loss.assert_called_once_with(sample_player, 10, "test_source")

    @pytest.mark.asyncio
    async def test_apply_lucidity_loss_player_not_found(self, player_service, mock_persistence):
        """Test applying lucidity loss when player doesn't exist."""
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Player not found"):
            await player_service.apply_lucidity_loss(uuid4(), 10)

    @pytest.mark.asyncio
    async def test_apply_fear_success(self, player_service, mock_persistence, sample_player):
        """Test successfully applying fear."""
        mock_persistence.get_player_by_id.return_value = sample_player
        mock_persistence.apply_fear.return_value = None

        result = await player_service.apply_fear(sample_player.player_id, 5, "test_source")

        assert "message" in result
        assert "fear" in result["message"]
        mock_persistence.apply_fear.assert_called_once_with(sample_player, 5, "test_source")

    @pytest.mark.asyncio
    async def test_apply_fear_player_not_found(self, player_service, mock_persistence):
        """Test applying fear when player doesn't exist."""
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Player not found"):
            await player_service.apply_fear(uuid4(), 5)

    @pytest.mark.asyncio
    async def test_apply_corruption_success(self, player_service, mock_persistence, sample_player):
        """Test successfully applying corruption."""
        mock_persistence.get_player_by_id.return_value = sample_player
        mock_persistence.apply_corruption.return_value = None

        result = await player_service.apply_corruption(sample_player.player_id, 3, "test_source")

        assert "message" in result
        assert "corruption" in result["message"]
        mock_persistence.apply_corruption.assert_called_once_with(sample_player, 3, "test_source")

    @pytest.mark.asyncio
    async def test_apply_corruption_player_not_found(self, player_service, mock_persistence):
        """Test applying corruption when player doesn't exist."""
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Player not found"):
            await player_service.apply_corruption(uuid4(), 3)

    @pytest.mark.asyncio
    async def test_gain_occult_knowledge_success(self, player_service, mock_persistence, sample_player):
        """Test successfully gaining occult knowledge."""
        mock_persistence.get_player_by_id.return_value = sample_player
        mock_persistence.async_gain_occult_knowledge.return_value = None

        result = await player_service.gain_occult_knowledge(sample_player.player_id, 10, "test_source")

        assert "message" in result
        assert "occult knowledge" in result["message"]
        mock_persistence.async_gain_occult_knowledge.assert_called_once_with(sample_player, 10, "test_source")

    @pytest.mark.asyncio
    async def test_gain_occult_knowledge_player_not_found(self, player_service, mock_persistence):
        """Test gaining occult knowledge when player doesn't exist."""
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Player not found"):
            await player_service.gain_occult_knowledge(uuid4(), 10)


class TestPlayerServiceHealth:
    """Test player health modification methods."""

    @pytest.mark.asyncio
    async def test_heal_player_success(self, player_service, mock_persistence, sample_player):
        """Test successfully healing a player."""
        mock_persistence.get_player_by_id.return_value = sample_player
        mock_persistence.async_heal_player.return_value = None

        result = await player_service.heal_player(sample_player.player_id, 20)

        assert "message" in result
        assert "Healed" in result["message"]
        mock_persistence.async_heal_player.assert_called_once_with(sample_player, 20)

    @pytest.mark.asyncio
    async def test_heal_player_not_found(self, player_service, mock_persistence):
        """Test healing a player that doesn't exist."""
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Player not found"):
            await player_service.heal_player(uuid4(), 20)

    @pytest.mark.asyncio
    async def test_damage_player_success(self, player_service, mock_persistence, sample_player):
        """Test successfully damaging a player."""
        mock_persistence.get_player_by_id.return_value = sample_player
        mock_persistence.async_damage_player.return_value = None

        result = await player_service.damage_player(sample_player.player_id, 15, "physical")

        assert "message" in result
        assert "Damaged" in result["message"]
        mock_persistence.async_damage_player.assert_called_once_with(sample_player, 15, "physical")

    @pytest.mark.asyncio
    async def test_damage_player_not_found(self, player_service, mock_persistence):
        """Test damaging a player that doesn't exist."""
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Player not found"):
            await player_service.damage_player(uuid4(), 15)

    @pytest.mark.asyncio
    async def test_damage_player_with_damage_type(self, player_service, mock_persistence, sample_player):
        """Test damaging a player with specific damage type."""
        mock_persistence.get_player_by_id.return_value = sample_player
        mock_persistence.async_damage_player.return_value = None

        result = await player_service.damage_player(sample_player.player_id, 10, "mental")

        assert "message" in result
        assert "mental" in result["message"]
        mock_persistence.async_damage_player.assert_called_once_with(sample_player, 10, "mental")


class TestPlayerServiceGetOnlinePlayers:
    """Test get_online_players method."""

    @pytest.mark.asyncio
    async def test_get_online_players(self, player_service, mock_persistence, sample_player):
        """Test getting online players (currently returns all players)."""
        mock_persistence.list_players.return_value = [sample_player]
        mock_persistence.get_profession_by_id.return_value = None

        result = await player_service.get_online_players()

        assert len(result) == 1
        assert result[0].name == sample_player.name
