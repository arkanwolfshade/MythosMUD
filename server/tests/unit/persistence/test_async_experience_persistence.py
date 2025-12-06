"""
Greenfield async unit tests for AsyncPersistenceLayer experience operations.

These tests cover all experience-related persistence operations using the
async persistence layer directly.
"""

from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.events.event_bus import EventBus
from server.models.player import Player


class TestAsyncExperiencePersistence:
    """Test async experience persistence operations."""

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
        player.lucidity = 50
        player.fear = 0
        player.corruption = 0
        return player

    @pytest.mark.asyncio
    async def test_apply_lucidity_loss(self, async_persistence, sample_player):
        """Test applying lucidity loss to a player."""
        # Mock the repository update method
        async_persistence._experience_repo.update_player_stat_field = AsyncMock(return_value=None)

        await async_persistence.apply_lucidity_loss(sample_player, 10, "test_source")

        async_persistence._experience_repo.update_player_stat_field.assert_called_once_with(
            sample_player.player_id, "lucidity", -10, "test_source: lucidity loss"
        )

    @pytest.mark.asyncio
    async def test_apply_fear(self, async_persistence, sample_player):
        """Test applying fear to a player."""
        # Mock the repository update method
        async_persistence._experience_repo.update_player_stat_field = AsyncMock(return_value=None)

        await async_persistence.apply_fear(sample_player, 5, "test_source")

        async_persistence._experience_repo.update_player_stat_field.assert_called_once_with(
            sample_player.player_id, "fear", 5, "test_source: fear increase"
        )

    @pytest.mark.asyncio
    async def test_apply_corruption(self, async_persistence, sample_player):
        """Test applying corruption to a player."""
        # Mock the repository update method
        async_persistence._experience_repo.update_player_stat_field = AsyncMock(return_value=None)

        await async_persistence.apply_corruption(sample_player, 3, "test_source")

        async_persistence._experience_repo.update_player_stat_field.assert_called_once_with(
            sample_player.player_id, "corruption", 3, "test_source: corruption increase"
        )

    @pytest.mark.asyncio
    async def test_apply_lucidity_loss_default_source(self, async_persistence, sample_player):
        """Test applying lucidity loss with default source."""
        # Mock the repository update method
        async_persistence._experience_repo.update_player_stat_field = AsyncMock(return_value=None)

        await async_persistence.apply_lucidity_loss(sample_player, 10)

        async_persistence._experience_repo.update_player_stat_field.assert_called_once_with(
            sample_player.player_id, "lucidity", -10, "unknown: lucidity loss"
        )
