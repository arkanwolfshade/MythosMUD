"""
Greenfield async unit tests for AsyncPersistenceLayer room operations.

These tests cover all room-related persistence operations using the
async persistence layer directly.
"""

import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.events.event_bus import EventBus
from server.models.room import Room


class TestAsyncRoomPersistence:
    """Test async room persistence operations."""

    @pytest.fixture
    def event_bus(self):
        """Create an event bus for testing."""
        return EventBus()

    @pytest.fixture
    def async_persistence(self, event_bus):
        """Create an AsyncPersistenceLayer instance for testing."""
        return AsyncPersistenceLayer(event_bus=event_bus)

    @pytest.fixture
    def sample_room(self, event_bus):
        """Create a sample room for testing."""
        room_data = {
            "id": "earth_arkhamcity_downtown_room_derby_st_001",
            "name": "Derby Street",
            "description": "A quiet street in downtown Arkham.",
        }
        return Room(room_data, event_bus)

    @pytest.mark.asyncio
    async def test_get_room_by_id_exists(self, async_persistence, sample_room):
        """Test getting a room by ID when room exists in cache."""
        # Add room to cache
        async_persistence._room_cache[sample_room.id] = sample_room

        result = async_persistence.get_room_by_id(sample_room.id)

        assert result is not None
        assert result.id == sample_room.id
        assert result.name == sample_room.name

    @pytest.mark.asyncio
    async def test_get_room_by_id_not_exists(self, async_persistence):
        """Test getting a room by ID when room does not exist."""
        room_id = "nonexistent_room_001"

        result = async_persistence.get_room_by_id(room_id)

        assert result is None

    @pytest.mark.asyncio
    async def test_get_room_by_id_cache_hit(self, async_persistence, sample_room):
        """Test that get_room_by_id uses cache efficiently."""
        # Add room to cache
        async_persistence._room_cache[sample_room.id] = sample_room

        # First call should hit cache
        result1 = async_persistence.get_room_by_id(sample_room.id)
        assert result1 is not None

        # Second call should also hit cache (no database call)
        result2 = async_persistence.get_room_by_id(sample_room.id)
        assert result2 is not None
        assert result1 is result2  # Same object from cache
