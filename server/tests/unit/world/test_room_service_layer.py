"""
Tests for RoomService layer implementation.

This module tests the RoomService to ensure proper business logic
separation and service layer functionality.
"""

from unittest.mock import AsyncMock, MagicMock, Mock

import pytest

from server.game.room_service import RoomService


class TestRoomServiceLayer:
    """Test the RoomService layer functionality."""

    mock_persistence: AsyncMock
    room_service: RoomService

    def setup_method(self) -> None:
        """Set up test fixtures."""
        # Use MagicMock as base to prevent automatic AsyncMock creation for all attributes
        # Only specific async methods will be AsyncMock instances
        self.mock_persistence = MagicMock()
        self.room_service = RoomService(self.mock_persistence)

    def test_room_service_initialization(self) -> None:
        """Test that RoomService initializes correctly."""
        assert self.room_service.persistence == self.mock_persistence

    @pytest.mark.asyncio
    @pytest.mark.asyncio
    async def test_get_room_success(self) -> None:
        """Test successful room retrieval by ID."""
        # Mock room data
        mock_room = Mock()
        mock_room.to_dict.return_value = {
            "id": "test_room_1",
            "name": "Test Room",
            "description": "A test room",
            "exits": {"north": "test_room_2", "south": "test_room_3"},
        }

        self.mock_persistence.async_get_room = AsyncMock(return_value=mock_room)

        # Get room
        result = await self.room_service.get_room("test_room_1")

        # Verify result
        assert isinstance(result, dict)
        assert result["id"] == "test_room_1"
        assert result["name"] == "Test Room"
        assert result["description"] == "A test room"

        # Verify persistence calls
        self.mock_persistence.async_get_room.assert_called_once_with("test_room_1")

    @pytest.mark.asyncio
    @pytest.mark.asyncio
    async def test_get_room_with_dict_response(self) -> None:
        """Test room retrieval when persistence returns a dictionary."""
        # Mock room data as dictionary
        mock_room_dict = {
            "id": "test_room_1",
            "name": "Test Room",
            "description": "A test room",
            "exits": {"north": "test_room_2", "south": "test_room_3"},
        }

        self.mock_persistence.async_get_room = AsyncMock(return_value=mock_room_dict)

        # Get room
        result = await self.room_service.get_room("test_room_1")

        # Verify result
        assert isinstance(result, dict)
        assert result["id"] == "test_room_1"
        assert result["name"] == "Test Room"

        # Verify persistence calls
        self.mock_persistence.async_get_room.assert_called_once_with("test_room_1")

    @pytest.mark.asyncio
    async def test_get_room_not_found(self) -> None:
        """Test room retrieval when room doesn't exist."""
        self.mock_persistence.async_get_room = AsyncMock(return_value=None)

        # Get non-existent room
        result = await self.room_service.get_room("nonexistent_room")

        # Verify result
        assert result is None
        self.mock_persistence.async_get_room.assert_called_once_with("nonexistent_room")

    def test_get_room_by_name_not_implemented(self) -> None:
        """Test room retrieval by name (not implemented)."""
        # Get room by name
        # pylint: disable=assignment-from-none
        # Suppressed: Method returns dict[str, Any] | None, but current implementation always returns None.
        # This test intentionally verifies the not-implemented behavior returns None.
        result = self.room_service.get_room_by_name("Test Room")

        # Verify result
        assert result is None

    def test_list_rooms_in_zone_not_implemented(self) -> None:
        """Test listing rooms in zone (not implemented)."""
        # List rooms in zone
        result = self.room_service.list_rooms_in_zone("test_zone")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_get_adjacent_rooms_success(self) -> None:
        """Test successful adjacent rooms retrieval."""
        # Mock source room
        mock_source_room = {
            "id": "test_room_1",
            "name": "Test Room",
            "exits": {
                "north": "test_room_2",
                "south": "test_room_3",
                "east": None,  # Null exit
                "west": "test_room_4",
            },
        }

        # Mock adjacent rooms
        mock_room_2 = {"id": "test_room_2", "name": "North Room", "description": "Room to the north"}

        mock_room_3 = {"id": "test_room_3", "name": "South Room", "description": "Room to the south"}

        mock_room_4 = {"id": "test_room_4", "name": "West Room", "description": "Room to the west"}

        # Mock persistence calls
        def mock_get_room(room_id):
            if room_id == "test_room_1":
                return mock_source_room
            elif room_id == "test_room_2":
                return mock_room_2
            elif room_id == "test_room_3":
                return mock_room_3
            elif room_id == "test_room_4":
                return mock_room_4
            return None

        self.mock_persistence.async_get_room = AsyncMock(side_effect=mock_get_room)

        # Get adjacent rooms
        result = await self.room_service.get_adjacent_rooms("test_room_1")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 3  # north, south, west (east is None)

        # Check that all adjacent rooms are included
        room_ids = [room["room_id"] for room in result]
        assert "test_room_2" in room_ids
        assert "test_room_3" in room_ids
        assert "test_room_4" in room_ids

        # Check that directions are correct
        directions = [room["direction"] for room in result]
        assert "north" in directions
        assert "south" in directions
        assert "west" in directions

        # Verify persistence calls
        assert self.mock_persistence.async_get_room.call_count == 4  # source + 3 adjacent

    @pytest.mark.asyncio
    async def test_get_adjacent_rooms_source_not_found(self) -> None:
        """Test adjacent rooms retrieval when source room doesn't exist."""
        self.mock_persistence.async_get_room = AsyncMock(return_value=None)

        # Get adjacent rooms for non-existent room
        result = await self.room_service.get_adjacent_rooms("nonexistent_room")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 0
        self.mock_persistence.async_get_room.assert_called_once_with("nonexistent_room")

    @pytest.mark.asyncio
    async def test_get_adjacent_rooms_missing_adjacent_room(self) -> None:
        """Test adjacent rooms retrieval when some adjacent rooms don't exist."""
        # Mock source room
        mock_source_room = {
            "id": "test_room_1",
            "name": "Test Room",
            "exits": {"north": "test_room_2", "south": "nonexistent_room"},
        }

        # Mock only one adjacent room exists
        mock_room_2 = {"id": "test_room_2", "name": "North Room", "description": "Room to the north"}

        # Mock persistence calls
        def mock_get_room(room_id):
            if room_id == "test_room_1":
                return mock_source_room
            elif room_id == "test_room_2":
                return mock_room_2
            return None  # nonexistent_room returns None

        self.mock_persistence.async_get_room = AsyncMock(side_effect=mock_get_room)

        # Get adjacent rooms
        result = await self.room_service.get_adjacent_rooms("test_room_1")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 1  # Only the existing adjacent room

        # Check that only the existing room is included
        assert result[0]["room_id"] == "test_room_2"
        assert result[0]["direction"] == "north"

        # Verify persistence calls
        assert self.mock_persistence.async_get_room.call_count == 3  # source + 2 adjacent

    @pytest.mark.asyncio
    async def test_get_local_chat_scope_success(self) -> None:
        """Test successful local chat scope retrieval."""
        # Mock source room
        mock_source_room = {
            "id": "test_room_1",
            "name": "Test Room",
            "exits": {"north": "test_room_2", "south": "test_room_3"},
        }

        # Mock adjacent rooms
        mock_room_2 = {"id": "test_room_2", "name": "North Room"}

        mock_room_3 = {"id": "test_room_3", "name": "South Room"}

        # Mock persistence calls
        def mock_get_room(room_id):
            if room_id == "test_room_1":
                return mock_source_room
            elif room_id == "test_room_2":
                return mock_room_2
            elif room_id == "test_room_3":
                return mock_room_3
            return None

        self.mock_persistence.async_get_room = AsyncMock(side_effect=mock_get_room)

        # Get local chat scope
        result = await self.room_service.get_local_chat_scope("test_room_1")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 3  # source room + 2 adjacent rooms
        assert "test_room_1" in result
        assert "test_room_2" in result
        assert "test_room_3" in result

        # Verify persistence calls
        assert self.mock_persistence.async_get_room.call_count == 4  # source + source (for adjacent) + 2 adjacent

    @pytest.mark.asyncio
    async def test_get_local_chat_scope_source_not_found(self) -> None:
        """Test local chat scope retrieval when source room doesn't exist."""
        self.mock_persistence.async_get_room = AsyncMock(return_value=None)

        # Get local chat scope for non-existent room
        result = await self.room_service.get_local_chat_scope("nonexistent_room")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 0
        self.mock_persistence.async_get_room.assert_called_once_with("nonexistent_room")

    @pytest.mark.asyncio
    async def test_get_local_chat_scope_no_exits(self) -> None:
        """Test local chat scope retrieval for room with no exits."""
        # Mock source room with no exits
        mock_source_room = {"id": "test_room_1", "name": "Test Room", "exits": {}}

        self.mock_persistence.async_get_room = AsyncMock(return_value=mock_source_room)

        # Get local chat scope
        result = await self.room_service.get_local_chat_scope("test_room_1")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 1  # Only the source room
        assert result[0] == "test_room_1"

        # Verify persistence calls
        assert self.mock_persistence.async_get_room.call_count == 2  # source + source (for adjacent)

    @pytest.mark.asyncio
    async def test_get_local_chat_scope_with_none_exits(self) -> None:
        """Test local chat scope retrieval for room with None exits."""
        # Mock source room with None exits
        mock_source_room = {
            "id": "test_room_1",
            "name": "Test Room",
            "exits": {"north": "test_room_2", "south": None, "east": "test_room_3"},
        }

        # Mock adjacent rooms
        mock_room_2 = {"id": "test_room_2", "name": "North Room"}

        mock_room_3 = {"id": "test_room_3", "name": "East Room"}

        # Mock persistence calls
        def mock_get_room(room_id):
            if room_id == "test_room_1":
                return mock_source_room
            elif room_id == "test_room_2":
                return mock_room_2
            elif room_id == "test_room_3":
                return mock_room_3
            return None

        self.mock_persistence.async_get_room = AsyncMock(side_effect=mock_get_room)

        # Get local chat scope
        result = await self.room_service.get_local_chat_scope("test_room_1")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 3  # source room + 2 valid adjacent rooms
        assert "test_room_1" in result
        assert "test_room_2" in result
        assert "test_room_3" in result

        # Verify persistence calls
        assert self.mock_persistence.async_get_room.call_count == 4  # source + source (for adjacent) + 2 valid adjacent

    @pytest.mark.asyncio
    async def test_validate_room_exists_success(self) -> None:
        """Test successful room existence validation."""
        # Mock room data
        mock_room = Mock()
        self.mock_persistence.async_get_room = AsyncMock(return_value=mock_room)

        # Validate room exists
        result = await self.room_service.validate_room_exists("test_room")

        # Verify result
        assert result is True
        self.mock_persistence.async_get_room.assert_called_once_with("test_room")

    @pytest.mark.asyncio
    async def test_validate_room_exists_not_found(self) -> None:
        """Test room existence validation when room doesn't exist."""
        self.mock_persistence.async_get_room = AsyncMock(return_value=None)

        # Validate room exists
        result = await self.room_service.validate_room_exists("nonexistent_room")

        # Verify result
        assert result is False
        self.mock_persistence.async_get_room.assert_called_once_with("nonexistent_room")

    @pytest.mark.asyncio
    async def test_validate_exit_exists_success(self) -> None:
        """Test successful exit validation."""
        # Mock room data
        mock_room = {
            "id": "test_room_1",
            "name": "Test Room",
            "exits": {"north": "test_room_2", "south": "test_room_3"},
        }
        self.mock_persistence.async_get_room = AsyncMock(return_value=mock_room)

        # Validate exit exists
        result = await self.room_service.validate_exit_exists("test_room_1", "test_room_2")

        # Verify result
        assert result is True
        self.mock_persistence.async_get_room.assert_called_once_with("test_room_1")

    @pytest.mark.asyncio
    async def test_validate_exit_exists_no_exit(self) -> None:
        """Test exit validation when exit doesn't exist."""
        # Mock room data
        mock_room = {
            "id": "test_room_1",
            "name": "Test Room",
            "exits": {"north": "test_room_2", "south": "test_room_3"},
        }
        self.mock_persistence.async_get_room = AsyncMock(return_value=mock_room)

        # Validate exit exists
        result = await self.room_service.validate_exit_exists("test_room_1", "test_room_4")

        # Verify result
        assert result is False
        self.mock_persistence.async_get_room.assert_called_once_with("test_room_1")

    @pytest.mark.asyncio
    async def test_validate_exit_exists_room_not_found(self) -> None:
        """Test exit validation when source room doesn't exist."""
        self.mock_persistence.async_get_room = AsyncMock(return_value=None)

        # Validate exit exists
        result = await self.room_service.validate_exit_exists("nonexistent_room", "test_room_2")

        # Verify result
        assert result is False
        self.mock_persistence.async_get_room.assert_called_once_with("nonexistent_room")

    @pytest.mark.asyncio
    async def test_get_room_occupants_success(self) -> None:
        """Test successful room occupants retrieval (players + NPCs)."""
        # Mock room data with Room object
        mock_room = Mock()
        mock_room.get_players.return_value = ["player1", "player2"]
        mock_room.get_npcs.return_value = ["npc1"]  # AI Agent: Mock get_npcs() to return list, not Mock
        self.mock_persistence.async_get_room = AsyncMock(return_value=mock_room)

        # Get room occupants
        result = await self.room_service.get_room_occupants("test_room")

        # Verify result includes both players and NPCs
        assert result == ["player1", "player2", "npc1"]
        self.mock_persistence.async_get_room.assert_called_once_with("test_room")
        mock_room.get_players.assert_called_once()
        mock_room.get_npcs.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_room_occupants_dict_response(self) -> None:
        """Test room occupants retrieval with dictionary response."""
        # Mock room data as dictionary
        mock_room = {"id": "test_room", "occupants": ["player1", "player2"]}
        self.mock_persistence.async_get_room = AsyncMock(return_value=mock_room)

        # Get room occupants
        result = await self.room_service.get_room_occupants("test_room")

        # Verify result
        assert result == ["player1", "player2"]
        self.mock_persistence.async_get_room.assert_called_once_with("test_room")

    @pytest.mark.asyncio
    async def test_get_room_occupants_room_not_found(self) -> None:
        """Test room occupants retrieval when room doesn't exist."""
        self.mock_persistence.async_get_room = AsyncMock(return_value=None)

        # Get room occupants
        result = await self.room_service.get_room_occupants("nonexistent_room")

        # Verify result
        assert result == []
        self.mock_persistence.async_get_room.assert_called_once_with("nonexistent_room")

    @pytest.mark.asyncio
    async def test_validate_player_in_room_success(self) -> None:
        """Test successful player room validation."""
        # Mock room data with Room object
        mock_room = Mock()
        mock_room.has_player.return_value = True
        self.mock_persistence.async_get_room = AsyncMock(return_value=mock_room)

        # Validate player in room
        result = await self.room_service.validate_player_in_room("player1", "test_room")

        # Verify result
        assert result is True
        self.mock_persistence.async_get_room.assert_called_once_with("test_room")
        mock_room.has_player.assert_called_once_with("player1")

    @pytest.mark.asyncio
    async def test_validate_player_in_room_dict_response(self) -> None:
        """Test player room validation with dictionary response."""
        # Mock room data as dictionary
        mock_room = {"id": "test_room", "occupants": ["player1", "player2"]}
        self.mock_persistence.async_get_room = AsyncMock(return_value=mock_room)

        # Validate player in room
        result = await self.room_service.validate_player_in_room("player1", "test_room")

        # Verify result
        assert result is True
        self.mock_persistence.async_get_room.assert_called_once_with("test_room")

    @pytest.mark.asyncio
    async def test_validate_player_in_room_not_found(self) -> None:
        """Test player room validation when room doesn't exist."""
        self.mock_persistence.async_get_room = AsyncMock(return_value=None)

        # Validate player in room
        result = await self.room_service.validate_player_in_room("player1", "nonexistent_room")

        # Verify result
        assert result is False
        self.mock_persistence.async_get_room.assert_called_once_with("nonexistent_room")

    @pytest.mark.asyncio
    async def test_get_room_exits_success(self) -> None:
        """Test successful room exits retrieval."""
        # Mock room data
        mock_room = {
            "id": "test_room",
            "name": "Test Room",
            "exits": {"north": "test_room_2", "south": "test_room_3"},
        }
        self.mock_persistence.async_get_room = AsyncMock(return_value=mock_room)

        # Get room exits
        result = await self.room_service.get_room_exits("test_room")

        # Verify result
        assert result == {"north": "test_room_2", "south": "test_room_3"}
        self.mock_persistence.async_get_room.assert_called_once_with("test_room")

    @pytest.mark.asyncio
    async def test_get_room_exits_room_not_found(self) -> None:
        """Test room exits retrieval when room doesn't exist."""
        self.mock_persistence.async_get_room = AsyncMock(return_value=None)

        # Get room exits
        result = await self.room_service.get_room_exits("nonexistent_room")

        # Verify result
        assert result == {}
        self.mock_persistence.async_get_room.assert_called_once_with("nonexistent_room")

    @pytest.mark.asyncio
    async def test_get_room_info_success(self) -> None:
        """Test successful comprehensive room info retrieval."""
        # Mock room data
        mock_room = {
            "id": "test_room",
            "name": "Test Room",
            "description": "A test room",
            "exits": {"north": "test_room_2", "south": "test_room_3"},
        }

        # Mock adjacent rooms
        mock_room_2 = {"id": "test_room_2", "name": "North Room"}
        mock_room_3 = {"id": "test_room_3", "name": "South Room"}

        # Mock persistence calls
        def mock_get_room(room_id):
            if room_id == "test_room":
                return mock_room
            elif room_id == "test_room_2":
                return mock_room_2
            elif room_id == "test_room_3":
                return mock_room_3
            return None

        self.mock_persistence.async_get_room = AsyncMock(side_effect=mock_get_room)

        # Get comprehensive room info
        result = await self.room_service.get_room_info("test_room")

        # Verify result
        assert isinstance(result, dict)
        assert result["id"] == "test_room"
        assert result["name"] == "Test Room"
        assert result["exits"] == {"north": "test_room_2", "south": "test_room_3"}
        assert "occupants" in result
        assert "adjacent_rooms" in result
        assert "occupant_count" in result
        assert "exit_count" in result
        assert result["exit_count"] == 2

    @pytest.mark.asyncio
    async def test_get_room_info_room_not_found(self) -> None:
        """Test comprehensive room info retrieval when room doesn't exist."""
        self.mock_persistence.async_get_room = AsyncMock(return_value=None)

        # Get comprehensive room info
        result = await self.room_service.get_room_info("nonexistent_room")

        # Verify result
        assert result is None
        self.mock_persistence.async_get_room.assert_called_once_with("nonexistent_room")

    def test_search_rooms_by_name_empty_term(self) -> None:
        """Test room search with empty search term."""
        # Search with empty term
        result = self.room_service.search_rooms_by_name("")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_rooms_by_name_short_term(self) -> None:
        """Test room search with short search term."""
        # Search with short term
        result = self.room_service.search_rooms_by_name("A")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 0

    def test_search_rooms_by_name_not_implemented(self) -> None:
        """Test room search by name (not implemented)."""
        # Search with valid term
        result = self.room_service.search_rooms_by_name("Test")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 0

    def test_get_rooms_in_zone_not_implemented(self) -> None:
        """Test getting rooms in zone (not implemented)."""
        # Get rooms in zone
        result = self.room_service.get_rooms_in_zone("test_zone")

        # Verify result
        assert isinstance(result, list)
        assert len(result) == 0
