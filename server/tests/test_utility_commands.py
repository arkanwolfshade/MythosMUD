"""
Tests for utility_commands.py - Utility command handlers.

This module tests the utility command handlers including who, quit, status,
inventory, and emote commands. Tests cover both success and error scenarios
to ensure robust error handling and edge case coverage.
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

import pytest

from ..commands.utility_commands import (
    get_username_from_user,
    handle_emote_command,
    handle_inventory_command,
    handle_quit_command,
    handle_status_command,
    handle_who_command,
)


class TestGetUsernameFromUser:
    """Test the get_username_from_user utility function."""

    def test_get_username_from_user_object(self):
        """Test extracting username from object with username attribute."""

        # Create a simple object with username attribute
        class UserObject:
            def __init__(self, username):
                self.username = username

        user_obj = UserObject("testuser")
        result = get_username_from_user(user_obj)
        assert result == "testuser"

    def test_get_username_from_user_dict(self):
        """Test extracting username from user dictionary."""
        user_dict = {"username": "testuser", "id": "123"}

        result = get_username_from_user(user_dict)
        assert result == "testuser"

    def test_get_username_from_user_name_key(self):
        """Test extracting username from dictionary with name key."""
        user_dict = {"name": "testuser"}
        result = get_username_from_user(user_dict)
        assert result == "testuser"

    def test_get_username_from_user_name_attr(self):
        """Test extracting username from object with name attribute."""

        # Create a simple object with name attribute
        class UserObject:
            def __init__(self, name):
                self.name = name

        user_obj = UserObject("testuser")
        result = get_username_from_user(user_obj)
        assert result == "testuser"

    def test_get_username_from_user_invalid_dict(self):
        """Test extracting username from invalid dictionary."""
        user_dict = {"invalid_key": "testuser"}
        with pytest.raises(ValueError, match="User object must have username or name attribute or key"):
            get_username_from_user(user_dict)

    def test_get_username_from_user_invalid_object(self):
        """Test extracting username from invalid object."""

        # Create a simple object without username or name attributes
        class InvalidUserObject:
            def __init__(self):
                self.email = "test@example.com"  # Different attribute

        user_obj = InvalidUserObject()
        with pytest.raises(ValueError, match="User object must have username or name attribute or key"):
            get_username_from_user(user_obj)

    def test_get_username_from_user_none(self):
        """Test that ValueError is raised for None input."""
        with pytest.raises(ValueError, match="User object must have username or name attribute or key"):
            get_username_from_user(None)


class TestWhoCommand:
    """Test the who command handler."""

    @pytest.fixture
    def mock_request(self):
        """Create a mock request object."""
        request = MagicMock()
        request.app = MagicMock()
        return request

    @pytest.fixture
    def mock_alias_storage(self):
        """Create a mock alias storage."""
        return MagicMock()

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return MagicMock()

    @pytest.mark.asyncio
    async def test_who_command_no_persistence(self, mock_request, mock_alias_storage):
        """Test who command when persistence is not available."""
        mock_request.app.state.persistence = None

        result = await handle_who_command(
            [],
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert result["result"] == "Player information is not available."

    @pytest.mark.asyncio
    async def test_who_command_no_players(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command when no players exist."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.list_players.return_value = []

        result = await handle_who_command(
            [],
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert result["result"] == "No players found."

    @pytest.mark.asyncio
    async def test_who_command_no_online_players(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command when players exist but none are online."""
        mock_request.app.state.persistence = mock_persistence

        # Create players with old last_active timestamps
        old_time = datetime.now(UTC) - timedelta(minutes=10)
        offline_players = [
            MagicMock(
                name="user1",
                level=1,
                current_room_id="earth_arkham_city_northside_intersection_derby_high",
                is_admin=False,
                last_active=old_time,
            ),
            MagicMock(
                name="user2",
                level=1,
                current_room_id="earth_arkham_city_northside_room_derby_st_001",
                is_admin=False,
                last_active=old_time,
            ),
        ]
        mock_persistence.list_players.return_value = offline_players

        result = await handle_who_command(
            [],
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert result["result"] == "No players are currently online."

    @pytest.mark.asyncio
    async def test_who_command_with_online_players(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command with online players."""
        mock_request.app.state.persistence = mock_persistence

        # Create players with recent last_active timestamps
        recent_time = datetime.now(UTC) - timedelta(minutes=2)

        # Create mock players with proper comparison behavior
        alice = MagicMock(
            name="alice", level=5, current_room_id="earth_arkham_city_northside_intersection_derby_high", is_admin=False
        )
        alice.last_active = recent_time
        alice.__lt__ = lambda self, other: self.name < other.name
        alice.__gt__ = lambda self, other: self.name > other.name
        alice.__eq__ = lambda self, other: self.name == other.name

        bob = MagicMock(
            name="bob", level=3, current_room_id="earth_arkham_city_northside_room_derby_st_001", is_admin=False
        )
        bob.last_active = recent_time
        bob.__lt__ = lambda self, other: self.name < other.name
        bob.__gt__ = lambda self, other: self.name > other.name
        bob.__eq__ = lambda self, other: self.name == other.name

        charlie = MagicMock(
            name="charlie", level=7, current_room_id="earth_arkham_city_northside_room_high_ln_002", is_admin=False
        )
        charlie.last_active = recent_time
        charlie.__lt__ = lambda self, other: self.name < other.name
        charlie.__gt__ = lambda self, other: self.name > other.name
        charlie.__eq__ = lambda self, other: self.name == other.name

        online_players = [alice, bob, charlie]
        mock_persistence.list_players.return_value = online_players

        result = await handle_who_command(
            [],
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert (
            "Online players (3): alice [5] - Arkham: City: Northside Intersection Derby High, bob [3] - Arkham: City: Northside Room Derby St 001, charlie [7] - Arkham: City: Northside Room High Ln 002"
            in result["result"]
        )

    @pytest.mark.asyncio
    async def test_who_command_mixed_online_offline(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command with mix of online and offline players."""
        mock_request.app.state.persistence = mock_persistence

        # Create mix of online and offline players
        recent_time = datetime.now(UTC) - timedelta(minutes=2)
        old_time = datetime.now(UTC) - timedelta(minutes=10)

        # Create mock players with proper comparison behavior
        alice = MagicMock(
            name="alice", level=5, current_room_id="earth_arkham_city_northside_intersection_derby_high", is_admin=False
        )  # Online
        alice.last_active = recent_time
        alice.__lt__ = lambda self, other: self.name < other.name
        alice.__gt__ = lambda self, other: self.name > other.name
        alice.__eq__ = lambda self, other: self.name == other.name

        bob = MagicMock(
            name="bob", level=3, current_room_id="earth_arkham_city_northside_room_derby_st_001", is_admin=False
        )  # Offline
        bob.last_active = old_time
        bob.__lt__ = lambda self, other: self.name < other.name
        bob.__gt__ = lambda self, other: self.name > other.name
        bob.__eq__ = lambda self, other: self.name == other.name

        charlie = MagicMock(
            name="charlie", level=7, current_room_id="earth_arkham_city_northside_room_high_ln_002", is_admin=False
        )  # Online
        charlie.last_active = recent_time
        charlie.__lt__ = lambda self, other: self.name < other.name
        charlie.__gt__ = lambda self, other: self.name > other.name
        charlie.__eq__ = lambda self, other: self.name == other.name

        players = [alice, bob, charlie]
        mock_persistence.list_players.return_value = players

        result = await handle_who_command(
            [],
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert (
            "Online players (2): alice [5] - Arkham: City: Northside Intersection Derby High, charlie [7] - Arkham: City: Northside Room High Ln 002"
            in result["result"]
        )

    @pytest.mark.asyncio
    async def test_who_command_persistence_exception(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command when persistence raises an exception."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.list_players.side_effect = Exception("Database error")

        result = await handle_who_command(
            [],
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Error retrieving player information: Database error" in result["result"]

    @pytest.mark.asyncio
    async def test_who_command_enhanced_functionality(self, mock_request, mock_alias_storage, mock_persistence):
        """Test enhanced who command functionality with real Player objects."""
        from server.models import Player

        mock_request.app.state.persistence = mock_persistence

        # Create real Player objects
        recent_time = datetime.now(UTC) - timedelta(minutes=2)
        old_time = datetime.now(UTC) - timedelta(minutes=10)

        alice = Player(
            name="alice",
            level=5,
            current_room_id="earth_arkham_city_northside_intersection_derby_high",
            is_admin=False,
            last_active=recent_time,
        )

        bob = Player(
            name="bob",
            level=3,
            current_room_id="earth_arkham_city_northside_room_derby_st_001",
            is_admin=False,
            last_active=recent_time,
        )

        charlie = Player(
            name="charlie",
            level=7,
            current_room_id="earth_arkham_city_northside_room_high_ln_002",
            is_admin=True,  # Test admin indicator
            last_active=recent_time,
        )

        offline_player = Player(
            name="offline",
            level=1,
            current_room_id="earth_arkham_city_northside_room_derby_st_002",
            is_admin=False,
            last_active=old_time,
        )

        players = [alice, bob, charlie, offline_player]
        mock_persistence.list_players.return_value = players

        # Test basic who command (no filter)
        result = await handle_who_command(
            [],
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        # Should show 3 online players (alice, bob, charlie) with enhanced formatting
        assert "Online players (3): " in result["result"]
        assert "alice [5] - Arkham: City: Northside Intersection Derby High" in result["result"]
        assert "bob [3] - Arkham: City: Northside Room Derby St 001" in result["result"]
        assert "charlie [7] [ADMIN] - Arkham: City: Northside Room High Ln 002" in result["result"]
        assert "offline" not in result["result"]  # Should not show offline player

        # Test filtering
        result = await handle_who_command(
            ["al"],
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        # Should show only alice
        assert "Players matching 'al' (1): " in result["result"]
        assert "alice [5] - Arkham: City: Northside Intersection Derby High" in result["result"]
        assert "bob" not in result["result"]
        assert "charlie" not in result["result"]

        # Test no matches
        result = await handle_who_command(
            ["xyz"],
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "No players found matching 'xyz'. Try 'who' to see all online players." in result["result"]


class TestQuitCommand:
    """Test the quit command handler."""

    @pytest.fixture
    def mock_request(self):
        """Create a mock request object."""
        request = MagicMock()
        request.app = MagicMock()
        return request

    @pytest.fixture
    def mock_alias_storage(self):
        """Create a mock alias storage."""
        return MagicMock()

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return MagicMock()

    @pytest.mark.asyncio
    async def test_quit_command_success(self, mock_request, mock_alias_storage, mock_persistence):
        """Test quit command with successful player update."""
        mock_request.app.state.persistence = mock_persistence

        # Mock player object
        mock_player = MagicMock()
        mock_player.username = "testuser"
        mock_persistence.get_player_by_name.return_value = mock_player

        result = await handle_quit_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "Goodbye! You have been disconnected from the game."
        mock_persistence.get_player_by_name.assert_called_once_with("testuser")
        mock_persistence.save_player.assert_called_once_with(mock_player)
        assert mock_player.last_active is not None

    @pytest.mark.asyncio
    async def test_quit_command_no_persistence(self, mock_request, mock_alias_storage):
        """Test quit command when persistence is not available."""
        mock_request.app.state.persistence = None

        result = await handle_quit_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "Goodbye! You have been disconnected from the game."

    @pytest.mark.asyncio
    async def test_quit_command_player_not_found(self, mock_request, mock_alias_storage, mock_persistence):
        """Test quit command when player is not found."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player_by_name.return_value = None

        result = await handle_quit_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "Goodbye! You have been disconnected from the game."
        mock_persistence.get_player_by_name.assert_called_once_with("testuser")
        mock_persistence.save_player.assert_not_called()

    @pytest.mark.asyncio
    async def test_quit_command_persistence_exception(self, mock_request, mock_alias_storage, mock_persistence):
        """Test quit command when persistence operations raise exceptions."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player_by_name.side_effect = Exception("Database error")

        result = await handle_quit_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "Goodbye! You have been disconnected from the game."


class TestStatusCommand:
    """Test the status command handler."""

    @pytest.fixture
    def mock_request(self):
        """Create a mock request object."""
        request = MagicMock()
        request.app = MagicMock()
        return request

    @pytest.fixture
    def mock_alias_storage(self):
        """Create a mock alias storage."""
        return MagicMock()

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return MagicMock()

    @pytest.fixture
    def mock_player(self):
        """Create a mock player with stats."""
        player = MagicMock()
        player.username = "testuser"
        player.current_room_id = "room_123"
        player.pose = "adjusting spectacles"

        # Mock stats object
        stats = MagicMock()
        stats.health = 85
        stats.max_health = 100
        stats.sanity = 75
        stats.max_sanity = 100
        stats.fear = 15
        stats.corruption = 5
        stats.occult_knowledge = 25

        player.stats = stats
        return player

    @pytest.fixture
    def mock_room(self):
        """Create a mock room."""
        room = MagicMock()
        room.name = "Miskatonic University Library"
        return room

    @pytest.mark.asyncio
    async def test_status_command_success(
        self, mock_request, mock_alias_storage, mock_persistence, mock_player, mock_room
    ):
        """Test status command with complete player information."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player_by_name.return_value = mock_player
        mock_persistence.get_room.return_value = mock_room

        result = await handle_status_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert "Name: testuser" in result["result"]
        assert "Location: Miskatonic University Library" in result["result"]
        assert "Health: 85/100" in result["result"]
        assert "Sanity: 75/100" in result["result"]
        assert "Fear: 15" in result["result"]
        assert "Corruption: 5" in result["result"]
        assert "Occult Knowledge: 25" in result["result"]
        assert "Pose: adjusting spectacles" in result["result"]

    @pytest.mark.asyncio
    async def test_status_command_no_persistence(self, mock_request, mock_alias_storage):
        """Test status command when persistence is not available."""
        mock_request.app.state.persistence = None

        result = await handle_status_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "Status information is not available."

    @pytest.mark.asyncio
    async def test_status_command_player_not_found(self, mock_request, mock_alias_storage, mock_persistence):
        """Test status command when player is not found."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player_by_name.return_value = None

        result = await handle_status_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "Player information not found."

    @pytest.mark.asyncio
    async def test_status_command_room_not_found(self, mock_request, mock_alias_storage, mock_persistence, mock_player):
        """Test status command when room is not found."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player_by_name.return_value = mock_player
        mock_persistence.get_room.return_value = None

        result = await handle_status_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert "Location: Unknown location" in result["result"]

    @pytest.mark.asyncio
    async def test_status_command_no_current_room(
        self, mock_request, mock_alias_storage, mock_persistence, mock_player
    ):
        """Test status command when player has no current room."""
        mock_request.app.state.persistence = mock_persistence
        mock_player.current_room_id = None
        mock_persistence.get_player_by_name.return_value = mock_player

        result = await handle_status_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert "Location: Unknown location" in result["result"]

    @pytest.mark.asyncio
    async def test_status_command_minimal_stats(self, mock_request, mock_alias_storage, mock_persistence, mock_room):
        """Test status command with minimal stats (no fear, corruption, occult knowledge)."""
        mock_request.app.state.persistence = mock_persistence

        # Create player with minimal stats
        player = MagicMock()
        player.username = "testuser"
        player.current_room_id = "room_123"
        player.pose = None

        stats = MagicMock()
        stats.health = 100
        stats.max_health = 100
        stats.sanity = 100
        stats.max_sanity = 100
        stats.fear = 0
        stats.corruption = 0
        stats.occult_knowledge = 0

        player.stats = stats
        mock_persistence.get_player_by_name.return_value = player
        mock_persistence.get_room.return_value = mock_room

        result = await handle_status_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert "Name: testuser" in result["result"]
        assert "Location: Miskatonic University Library" in result["result"]
        assert "Health: 100/100" in result["result"]
        assert "Sanity: 100/100" in result["result"]
        # Should not include fear, corruption, or occult knowledge when they are 0
        assert "Fear:" not in result["result"]
        assert "Corruption:" not in result["result"]
        assert "Occult Knowledge:" not in result["result"]
        assert "Pose:" not in result["result"]

    @pytest.mark.asyncio
    async def test_status_command_persistence_exception(self, mock_request, mock_alias_storage, mock_persistence):
        """Test status command when persistence raises an exception."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player_by_name.side_effect = Exception("Database error")

        result = await handle_status_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert "Error retrieving status information: Database error" in result["result"]


class TestInventoryCommand:
    """Test the inventory command handler."""

    @pytest.fixture
    def mock_request(self):
        """Create a mock request object."""
        request = MagicMock()
        request.app = MagicMock()
        return request

    @pytest.fixture
    def mock_alias_storage(self):
        """Create a mock alias storage."""
        return MagicMock()

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return MagicMock()

    @pytest.mark.asyncio
    async def test_inventory_command_with_items(self, mock_request, mock_alias_storage, mock_persistence):
        """Test inventory command with items in inventory."""
        mock_request.app.state.persistence = mock_persistence

        # Create player with inventory items
        player = MagicMock()
        player.username = "testuser"

        # Mock inventory items
        item1 = MagicMock()
        item1.name = "Necronomicon"
        item1.description = "A forbidden tome of eldritch knowledge"

        item2 = MagicMock()
        item2.name = "Silver dagger"
        item2.description = "A weapon blessed by ancient rites"

        item3 = MagicMock()
        item3.name = "Herb pouch"
        # No description for this item

        player.inventory = [item1, item2, item3]
        mock_persistence.get_player_by_name.return_value = player

        result = await handle_inventory_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert "You are carrying:" in result["result"]
        assert "Necronomicon - A forbidden tome of eldritch knowledge" in result["result"]
        assert "Silver dagger - A weapon blessed by ancient rites" in result["result"]
        assert "Herb pouch" in result["result"]  # Should not have description separator

    @pytest.mark.asyncio
    async def test_inventory_command_empty(self, mock_request, mock_alias_storage, mock_persistence):
        """Test inventory command with empty inventory."""
        mock_request.app.state.persistence = mock_persistence

        player = MagicMock()
        player.username = "testuser"
        player.inventory = []
        mock_persistence.get_player_by_name.return_value = player

        result = await handle_inventory_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "You are not carrying anything."

    @pytest.mark.asyncio
    async def test_inventory_command_no_persistence(self, mock_request, mock_alias_storage):
        """Test inventory command when persistence is not available."""
        mock_request.app.state.persistence = None

        result = await handle_inventory_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "Inventory information is not available."

    @pytest.mark.asyncio
    async def test_inventory_command_player_not_found(self, mock_request, mock_alias_storage, mock_persistence):
        """Test inventory command when player is not found."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player_by_name.return_value = None

        result = await handle_inventory_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "Player information not found."

    @pytest.mark.asyncio
    async def test_inventory_command_items_without_description(
        self, mock_request, mock_alias_storage, mock_persistence
    ):
        """Test inventory command with items that have no description attribute."""
        mock_request.app.state.persistence = mock_persistence

        player = MagicMock()
        player.username = "testuser"

        # Create mock items without description attribute by using a custom class
        class MockItem:
            def __init__(self, name):
                self.name = name

        item1 = MockItem("Simple key")
        item2 = MockItem("Old coin")

        player.inventory = [item1, item2]
        mock_persistence.get_player_by_name.return_value = player

        result = await handle_inventory_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert "You are carrying:" in result["result"]
        assert "Simple key - No description" in result["result"]
        assert "Old coin - No description" in result["result"]

    @pytest.mark.asyncio
    async def test_inventory_command_persistence_exception(self, mock_request, mock_alias_storage, mock_persistence):
        """Test inventory command when persistence raises an exception."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_player_by_name.side_effect = Exception("Database error")

        result = await handle_inventory_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert "Error retrieving inventory: Database error" in result["result"]

    @pytest.mark.asyncio
    async def test_inventory_command_items_with_falsy_description(
        self, mock_request, mock_alias_storage, mock_persistence
    ):
        """Test inventory command with items that have falsy description values."""
        mock_request.app.state.persistence = mock_persistence

        player = MagicMock()
        player.username = "testuser"

        # Mock inventory items with falsy descriptions
        item1 = MagicMock()
        item1.name = "Mysterious artifact"
        item1.description = None

        item2 = MagicMock()
        item2.name = "Old scroll"
        item2.description = ""

        item3 = MagicMock()
        item3.name = "Strange device"
        item3.description = False

        player.inventory = [item1, item2, item3]
        mock_persistence.get_player_by_name.return_value = player

        result = await handle_inventory_command(
            args=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert "You are carrying:" in result["result"]
        assert "Mysterious artifact - No description" in result["result"]
        assert "Old scroll - No description" in result["result"]
        assert "Strange device - No description" in result["result"]


class TestEmoteCommand:
    """Test the emote command handler."""

    @pytest.fixture
    def mock_request(self):
        """Create a mock request object."""
        request = MagicMock()
        request.app = MagicMock()
        return request

    @pytest.fixture
    def mock_alias_storage(self):
        """Create a mock alias storage."""
        return MagicMock()

    @pytest.mark.asyncio
    async def test_emote_command_with_action(self, mock_request, mock_alias_storage):
        """Test emote command with a single action."""
        result = await handle_emote_command(
            args_or_data=["adjusts", "spectacles"],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "testuser adjusts spectacles"

    @pytest.mark.asyncio
    async def test_emote_command_complex_action(self, mock_request, mock_alias_storage):
        """Test emote command with complex multi-word action."""
        result = await handle_emote_command(
            args_or_data=["opens", "the", "forbidden", "tome", "with", "trembling", "hands"],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "testuser opens the forbidden tome with trembling hands"

    @pytest.mark.asyncio
    async def test_emote_command_no_args(self, mock_request, mock_alias_storage):
        """Test emote command with no arguments."""
        result = await handle_emote_command(
            args_or_data=[],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "Emote what? Usage: emote <action>"

    @pytest.mark.asyncio
    async def test_emote_command_empty_string_args(self, mock_request, mock_alias_storage):
        """Test emote command with empty string arguments."""
        result = await handle_emote_command(
            args_or_data=["", ""],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "testuser  "  # Two spaces from empty strings

    @pytest.mark.asyncio
    async def test_emote_command_special_characters(self, mock_request, mock_alias_storage):
        """Test emote command with special characters in action."""
        result = await handle_emote_command(
            args_or_data=["whispers", "something", "in", "an", "ancient", "tongue..."],
            current_user={"username": "testuser"},
            request=mock_request,
            alias_storage=mock_alias_storage,
            player_name="testuser",
        )

        assert result["result"] == "testuser whispers something in an ancient tongue..."
