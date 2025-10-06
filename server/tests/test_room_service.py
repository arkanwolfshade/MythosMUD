"""
Tests for the room service functionality.

This module tests room-related operations including room retrieval,
adjacency logic, and local chat scope determination.
"""

from unittest.mock import AsyncMock

import pytest

from ..game.room_service import RoomService


@pytest.mark.asyncio
class TestRoomService:
    """Test cases for RoomService."""

    def setup_method(self):
        """Set up test fixtures."""
        self.mock_persistence = AsyncMock()
        self.room_service = RoomService(self.mock_persistence)

    async def test_get_room_success(self):
        """Test successful room retrieval."""
        # Mock room data
        mock_room_data = {
            "id": "test_room_001",
            "name": "Test Room",
            "description": "A test room",
            "exits": {"north": "test_room_002", "south": None, "east": "test_room_003", "west": None},
        }

        # Mock the persistence layer
        self.mock_persistence.async_get_room.return_value = mock_room_data

        # Test room retrieval
        result = await self.room_service.get_room("test_room_001")

        assert result == mock_room_data
        self.mock_persistence.async_get_room.assert_called_once_with("test_room_001")

    async def test_get_room_not_found(self):
        """Test room retrieval when room doesn't exist."""
        # Mock the persistence layer to return None
        self.mock_persistence.async_get_room.return_value = None

        # Test room retrieval
        result = await self.room_service.get_room("nonexistent_room")

        assert result is None
        self.mock_persistence.async_get_room.assert_called_once_with("nonexistent_room")

    async def test_get_adjacent_rooms_success(self):
        """Test successful adjacent room retrieval."""
        # Mock source room data
        source_room_data = {
            "id": "test_room_001",
            "name": "Test Room",
            "exits": {"north": "test_room_002", "south": None, "east": "test_room_003", "west": None},
        }

        # Mock adjacent room data
        north_room_data = {"id": "test_room_002", "name": "North Room", "exits": {}}

        east_room_data = {"id": "test_room_003", "name": "East Room", "exits": {}}

        # Mock the persistence layer
        self.mock_persistence.async_get_room.side_effect = lambda room_id: {
            "test_room_001": source_room_data,
            "test_room_002": north_room_data,
            "test_room_003": east_room_data,
        }.get(room_id)

        # Test adjacent room retrieval
        result = await self.room_service.get_adjacent_rooms("test_room_001")

        # Should find 2 adjacent rooms (north and east)
        assert len(result) == 2

        # Check north room
        north_adjacent = next(r for r in result if r["direction"] == "north")
        assert north_adjacent["room_id"] == "test_room_002"
        assert north_adjacent["room_data"] == north_room_data

        # Check east room
        east_adjacent = next(r for r in result if r["direction"] == "east")
        assert east_adjacent["room_id"] == "test_room_003"
        assert east_adjacent["room_data"] == east_room_data

    async def test_get_adjacent_rooms_source_not_found(self):
        """Test adjacent room retrieval when source room doesn't exist."""
        # Mock the persistence layer to return None for source room
        self.mock_persistence.async_get_room.return_value = None

        # Test adjacent room retrieval
        result = await self.room_service.get_adjacent_rooms("nonexistent_room")

        assert result == []

    async def test_get_adjacent_rooms_missing_adjacent(self):
        """Test adjacent room retrieval when some adjacent rooms don't exist."""
        # Mock source room data with one valid and one invalid exit
        source_room_data = {
            "id": "test_room_001",
            "name": "Test Room",
            "exits": {"north": "test_room_002", "south": "nonexistent_room"},
        }

        # Mock adjacent room data (only north room exists)
        north_room_data = {"id": "test_room_002", "name": "North Room", "exits": {}}

        # Mock the persistence layer
        self.mock_persistence.async_get_room.side_effect = lambda room_id: {
            "test_room_001": source_room_data,
            "test_room_002": north_room_data,
        }.get(room_id)

        # Test adjacent room retrieval
        result = await self.room_service.get_adjacent_rooms("test_room_001")

        # Should find 1 adjacent room (only north)
        assert len(result) == 1
        assert result[0]["direction"] == "north"
        assert result[0]["room_id"] == "test_room_002"

    async def test_get_local_chat_scope_success(self):
        """Test successful local chat scope determination."""
        # Mock source room data
        source_room_data = {
            "id": "test_room_001",
            "name": "Test Room",
            "exits": {"north": "test_room_002", "east": "test_room_003"},
        }

        # Mock adjacent room data
        north_room_data = {"id": "test_room_002", "name": "North Room", "exits": {}}
        east_room_data = {"id": "test_room_003", "name": "East Room", "exits": {}}

        # Mock the persistence layer
        self.mock_persistence.async_get_room.side_effect = lambda room_id: {
            "test_room_001": source_room_data,
            "test_room_002": north_room_data,
            "test_room_003": east_room_data,
        }.get(room_id)

        # Test local chat scope
        result = await self.room_service.get_local_chat_scope("test_room_001")

        # Should include current room and 2 adjacent rooms
        expected_scope = ["test_room_001", "test_room_002", "test_room_003"]
        assert result == expected_scope

    async def test_get_local_chat_scope_no_adjacent(self):
        """Test local chat scope when room has no adjacent rooms."""
        # Mock source room data with no exits
        source_room_data = {"id": "test_room_001", "name": "Test Room", "exits": {}}

        # Mock the persistence layer
        self.mock_persistence.async_get_room.return_value = source_room_data

        # Test local chat scope
        result = await self.room_service.get_local_chat_scope("test_room_001")

        # Should only include the current room
        assert result == ["test_room_001"]

    async def test_get_local_chat_scope_source_not_found(self):
        """Test local chat scope when source room doesn't exist."""
        # Mock the persistence layer to return None
        self.mock_persistence.async_get_room.return_value = None

        # Test local chat scope
        result = await self.room_service.get_local_chat_scope("nonexistent_room")

        # Should return empty list
        assert result == []
