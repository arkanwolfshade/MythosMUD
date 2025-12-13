"""
Greenfield async unit tests for AsyncPersistenceLayer health operations.

These tests cover all health-related persistence operations using the
async persistence layer directly.
"""

from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.events.event_bus import EventBus
from server.models.player import Player


class TestAsyncHealthPersistence:
    """Test async health persistence operations."""

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
        player.current_dp = 100
        player.max_dp = 100
        return player

    @pytest.mark.asyncio
    async def test_heal_player(self, async_persistence, sample_player):
        """Test healing a player."""
        # Mock the repository heal method
        async_persistence._health_repo.heal_player = AsyncMock(return_value=None)

        await async_persistence.heal_player(sample_player, 20)

        async_persistence._health_repo.heal_player.assert_called_once_with(sample_player, 20)

    @pytest.mark.asyncio
    async def test_damage_player(self, async_persistence, sample_player):
        """Test damaging a player."""
        # Mock the repository damage method
        async_persistence._health_repo.damage_player = AsyncMock(return_value=None)

        await async_persistence.damage_player(sample_player, 10, "physical")

        async_persistence._health_repo.damage_player.assert_called_once_with(sample_player, 10, "physical")

    @pytest.mark.asyncio
    async def test_damage_player_default_type(self, async_persistence, sample_player):
        """Test damaging a player with default damage type."""
        # Mock the repository damage method
        async_persistence._health_repo.damage_player = AsyncMock(return_value=None)

        await async_persistence.damage_player(sample_player, 10)

        async_persistence._health_repo.damage_player.assert_called_once_with(sample_player, 10, "physical")
