"""
Unit tests for GameMechanicsService.

This module tests the GameMechanicsService class covering all game mechanics
operations including lucidity, fear, corruption, healing, damage, and experience.
"""


# pylint: disable=redefined-outer-name
# Justification: pytest fixtures redefine names

from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4

import pytest

from server.exceptions import ValidationError
from server.game.mechanics import GameMechanicsService


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = Mock()
    persistence.get_player_by_id = AsyncMock()
    persistence.get_player = Mock()  # Used by gain_experience
    persistence.apply_lucidity_loss = AsyncMock()
    persistence.apply_fear = AsyncMock()
    persistence.apply_corruption = AsyncMock()
    persistence.heal_player = AsyncMock()
    persistence.damage_player = AsyncMock()
    persistence.gain_experience = Mock()
    return persistence


@pytest.fixture
def mechanics_service(mock_persistence):
    """Create a GameMechanicsService instance for testing."""
    return GameMechanicsService(mock_persistence)


@pytest.fixture
def sample_player():
    """Create a sample player mock."""
    player = Mock()
    player.player_id = uuid4()
    player.name = "TestPlayer"
    return player


class TestGameMechanicsServiceInitialization:
    """Test GameMechanicsService initialization."""

    def test_initialization(self, mechanics_service, mock_persistence):
        """Test that GameMechanicsService initializes correctly."""
        assert mechanics_service.persistence == mock_persistence
        assert hasattr(mechanics_service, "apply_lucidity_loss")
        assert hasattr(mechanics_service, "apply_fear")
        assert hasattr(mechanics_service, "apply_corruption")
        assert hasattr(mechanics_service, "gain_occult_knowledge")
        assert hasattr(mechanics_service, "heal_player")
        assert hasattr(mechanics_service, "damage_player")
        assert hasattr(mechanics_service, "gain_experience")


class TestGameMechanicsServiceApplyLucidityLoss:
    """Test apply_lucidity_loss method."""

    @pytest.mark.asyncio
    async def test_apply_lucidity_loss_success_with_str_id(self, mechanics_service, mock_persistence, sample_player):
        """Test successful lucidity loss application with string player ID."""
        player_id_str = str(sample_player.player_id)
        amount = 10
        source = "eldritch tome"

        mock_persistence.get_player_by_id.return_value = sample_player

        success, message = await mechanics_service.apply_lucidity_loss(player_id_str, amount, source)

        assert success is True
        assert f"Applied {amount} lucidity loss to {sample_player.name}" in message
        mock_persistence.get_player_by_id.assert_called_once()
        # Verify UUID conversion
        call_arg = mock_persistence.get_player_by_id.call_args[0][0]
        assert call_arg == sample_player.player_id
        mock_persistence.apply_lucidity_loss.assert_called_once_with(sample_player, amount, source)

    @pytest.mark.asyncio
    async def test_apply_lucidity_loss_success_with_uuid(self, mechanics_service, mock_persistence, sample_player):
        """Test successful lucidity loss application with UUID player ID."""
        amount = 10
        source = "eldritch tome"

        mock_persistence.get_player_by_id.return_value = sample_player

        success, message = await mechanics_service.apply_lucidity_loss(sample_player.player_id, amount, source)

        assert success is True
        assert f"Applied {amount} lucidity loss to {sample_player.name}" in message
        mock_persistence.apply_lucidity_loss.assert_called_once_with(sample_player, amount, source)

    @pytest.mark.asyncio
    async def test_apply_lucidity_loss_player_not_found(self, mechanics_service, mock_persistence):
        """Test lucidity loss application when player is not found."""
        player_id = uuid4()
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Player not found for lucidity loss"):
            await mechanics_service.apply_lucidity_loss(str(player_id), 10)

    @pytest.mark.asyncio
    async def test_apply_lucidity_loss_default_source(self, mechanics_service, mock_persistence, sample_player):
        """Test lucidity loss application with default source."""
        mock_persistence.get_player_by_id.return_value = sample_player

        success, _message = await mechanics_service.apply_lucidity_loss(str(sample_player.player_id), 10)

        assert success is True
        mock_persistence.apply_lucidity_loss.assert_called_once_with(sample_player, 10, "unknown")


class TestGameMechanicsServiceApplyFear:
    """Test apply_fear method."""

    @pytest.mark.asyncio
    async def test_apply_fear_success(self, mechanics_service, mock_persistence, sample_player):
        """Test successful fear application."""
        amount = 15
        source = "dark ritual"

        mock_persistence.get_player_by_id.return_value = sample_player

        success, message = await mechanics_service.apply_fear(str(sample_player.player_id), amount, source)

        assert success is True
        assert f"Applied {amount} fear to {sample_player.name}" in message
        mock_persistence.apply_fear.assert_called_once_with(sample_player, amount, source)

    @pytest.mark.asyncio
    async def test_apply_fear_player_not_found(self, mechanics_service, mock_persistence):
        """Test fear application when player is not found."""
        player_id = uuid4()
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Player not found for fear application"):
            await mechanics_service.apply_fear(str(player_id), 15)


class TestGameMechanicsServiceApplyCorruption:
    """Test apply_corruption method."""

    @pytest.mark.asyncio
    async def test_apply_corruption_success(self, mechanics_service, mock_persistence, sample_player):
        """Test successful corruption application."""
        amount = 5
        source = "forbidden knowledge"

        mock_persistence.get_player_by_id.return_value = sample_player

        success, message = await mechanics_service.apply_corruption(str(sample_player.player_id), amount, source)

        assert success is True
        assert f"Applied {amount} corruption to {sample_player.name}" in message
        mock_persistence.apply_corruption.assert_called_once_with(sample_player, amount, source)

    @pytest.mark.asyncio
    async def test_apply_corruption_player_not_found(self, mechanics_service, mock_persistence):
        """Test corruption application when player is not found."""
        player_id = uuid4()
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Player not found for corruption application"):
            await mechanics_service.apply_corruption(str(player_id), 5)


class TestGameMechanicsServiceGainOccultKnowledge:
    """Test gain_occult_knowledge method."""

    @pytest.mark.asyncio
    async def test_gain_occult_knowledge_success(self, mechanics_service, mock_persistence, sample_player):
        """Test successful occult knowledge gain."""
        amount = 20
        source = "necronomicon"

        mock_persistence.get_player_by_id.return_value = sample_player

        with patch(
            "server.persistence.repositories.experience_repository.ExperienceRepository"
        ) as mock_experience_repo:
            mock_experience_instance = AsyncMock()
            mock_experience_repo.return_value = mock_experience_instance

            success, message = await mechanics_service.gain_occult_knowledge(
                str(sample_player.player_id), amount, source
            )

            assert success is True
            assert f"Gained {amount} occult knowledge for {sample_player.name}" in message
            mock_experience_instance.update_player_stat_field.assert_called_once()
            # Should apply lucidity loss equal to half the amount
            mock_persistence.apply_lucidity_loss.assert_called_once_with(
                sample_player, amount // 2, f"{source}: occult knowledge lucidity cost"
            )

    @pytest.mark.asyncio
    async def test_gain_occult_knowledge_player_not_found(self, mechanics_service, mock_persistence):
        """Test occult knowledge gain when player is not found."""
        player_id = uuid4()
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Player not found for occult knowledge gain"):
            await mechanics_service.gain_occult_knowledge(str(player_id), 20)


class TestGameMechanicsServiceHealPlayer:
    """Test heal_player method."""

    @pytest.mark.asyncio
    async def test_heal_player_success(self, mechanics_service, mock_persistence, sample_player):
        """Test successful player healing."""
        amount = 25

        mock_persistence.get_player_by_id.return_value = sample_player

        success, message = await mechanics_service.heal_player(str(sample_player.player_id), amount)

        assert success is True
        assert f"Healed {sample_player.name} for {amount} health" in message
        mock_persistence.heal_player.assert_called_once_with(sample_player, amount)

    @pytest.mark.asyncio
    async def test_heal_player_not_found(self, mechanics_service, mock_persistence):
        """Test healing when player is not found."""
        player_id = uuid4()
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Player not found for healing"):
            await mechanics_service.heal_player(str(player_id), 25)


class TestGameMechanicsServiceDamagePlayer:
    """Test damage_player method."""

    @pytest.mark.asyncio
    async def test_damage_player_success(self, mechanics_service, mock_persistence, sample_player):
        """Test successful player damage."""
        amount = 30
        damage_type = "psychic"

        mock_persistence.get_player_by_id.return_value = sample_player

        success, message = await mechanics_service.damage_player(str(sample_player.player_id), amount, damage_type)

        assert success is True
        assert f"Damaged {sample_player.name} for {amount} {damage_type} damage" in message
        mock_persistence.damage_player.assert_called_once_with(sample_player, amount, damage_type)

    @pytest.mark.asyncio
    async def test_damage_player_default_type(self, mechanics_service, mock_persistence, sample_player):
        """Test player damage with default damage type."""
        amount = 30

        mock_persistence.get_player_by_id.return_value = sample_player

        success, message = await mechanics_service.damage_player(str(sample_player.player_id), amount)

        assert success is True
        assert "physical damage" in message
        mock_persistence.damage_player.assert_called_once_with(sample_player, amount, "physical")

    @pytest.mark.asyncio
    async def test_damage_player_not_found(self, mechanics_service, mock_persistence):
        """Test damage when player is not found."""
        player_id = uuid4()
        mock_persistence.get_player_by_id.return_value = None

        with pytest.raises(ValidationError, match="Player not found for damage"):
            await mechanics_service.damage_player(str(player_id), 30)


class TestGameMechanicsServiceGainExperience:
    """Test gain_experience method."""

    def test_gain_experience_success(self, mechanics_service, mock_persistence, sample_player):
        """Test successful experience gain."""
        player_id_str = str(sample_player.player_id)
        amount = 100
        source = "killed_nightgaunt"

        mock_persistence.get_player.return_value = sample_player

        success, message = mechanics_service.gain_experience(player_id_str, amount, source)

        assert success is True
        assert f"Awarded {amount} XP to {sample_player.name}" in message
        mock_persistence.get_player.assert_called_once_with(player_id_str)
        mock_persistence.gain_experience.assert_called_once_with(sample_player, amount, source)

    def test_gain_experience_player_not_found(self, mechanics_service, mock_persistence):
        """Test experience gain when player is not found."""
        player_id_str = str(uuid4())
        mock_persistence.get_player.return_value = None

        with pytest.raises(ValidationError, match="Player not found for XP gain"):
            mechanics_service.gain_experience(player_id_str, 100)

    def test_gain_experience_default_source(self, mechanics_service, mock_persistence, sample_player):
        """Test experience gain with default source."""
        mock_persistence.get_player.return_value = sample_player

        success, _message = mechanics_service.gain_experience(str(sample_player.player_id), 100)

        assert success is True
        mock_persistence.gain_experience.assert_called_once_with(sample_player, 100, "unknown")
