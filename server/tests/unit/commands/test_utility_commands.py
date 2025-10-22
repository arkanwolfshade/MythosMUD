"""
Tests for utility_commands.py - Utility command handlers.

This module tests the utility command handlers including who, quit, status,
inventory, and emote commands. Tests cover both success and error scenarios
to ensure robust error handling and edge case coverage.
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

import pytest

from server.commands.utility_commands import (
    filter_players_by_name,
    format_player_entry,
    format_player_location,
    get_username_from_user,
    handle_emote_command,
    handle_inventory_command,
    handle_quit_command,
    handle_status_command,
    handle_who_command,
)
from server.exceptions import ValidationError


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
        with pytest.raises(ValidationError, match="User object must have username or name attribute or key"):
            get_username_from_user(user_dict)

    def test_get_username_from_user_invalid_object(self):
        """Test extracting username from invalid object."""

        # Create a simple object without username or name attributes
        class InvalidUserObject:
            def __init__(self):
                self.email = "test@example.com"  # Different attribute

        user_obj = InvalidUserObject()
        with pytest.raises(ValidationError, match="User object must have username or name attribute or key"):
            get_username_from_user(user_obj)

    def test_get_username_from_user_none(self):
        """Test that ValueError is raised for None input."""
        with pytest.raises(ValidationError, match="User object must have username or name attribute or key"):
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
            {"target_player": ""},
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
            {"target_player": ""},
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
                current_room_id="earth_arkhamcity_northside_intersection_derby_high",
                is_admin=False,
                last_active=old_time,
            ),
            MagicMock(
                name="user2",
                level=1,
                current_room_id="earth_arkhamcity_northside_room_derby_st_001",
                is_admin=False,
                last_active=old_time,
            ),
        ]
        mock_persistence.list_players.return_value = offline_players

        result = await handle_who_command(
            {"target_player": ""},
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

        # Create simple mock players without complex comparison methods
        alice = MagicMock()
        alice.name = "alice"
        alice.level = 5
        alice.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        alice.is_admin = False
        alice.last_active = recent_time

        bob = MagicMock()
        bob.name = "bob"
        bob.level = 3
        bob.current_room_id = "earth_arkhamcity_northside_room_derby_st_001"
        bob.is_admin = False
        bob.last_active = recent_time

        charlie = MagicMock()
        charlie.name = "charlie"
        charlie.level = 7
        charlie.current_room_id = "earth_arkhamcity_northside_room_high_ln_002"
        charlie.is_admin = False
        charlie.last_active = recent_time

        online_players = [alice, bob, charlie]
        mock_persistence.list_players.return_value = online_players

        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Online Players (3):" in result["result"]
        assert "alice" in result["result"]
        assert "bob" in result["result"]
        assert "charlie" in result["result"]

    @pytest.mark.asyncio
    async def test_who_command_mixed_online_offline(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command with mix of online and offline players."""
        mock_request.app.state.persistence = mock_persistence

        # Create players with mixed last_active timestamps
        recent_time = datetime.now(UTC) - timedelta(minutes=2)
        old_time = datetime.now(UTC) - timedelta(minutes=10)

        online_player = MagicMock(
            name="online_user",
            level=1,
            current_room_id="earth_arkhamcity_northside_intersection_derby_high",
            is_admin=False,
        )
        online_player.last_active = recent_time
        online_player.__lt__ = lambda self, other: self.name < other.name
        online_player.__gt__ = lambda self, other: self.name > other.name
        online_player.__eq__ = lambda self, other: self.name == other.name

        offline_player = MagicMock(
            name="offline_user",
            level=1,
            current_room_id="earth_arkhamcity_northside_room_derby_st_001",
            is_admin=False,
        )
        offline_player.last_active = old_time
        offline_player.__lt__ = lambda self, other: self.name < other.name
        offline_player.__gt__ = lambda self, other: self.name > other.name
        offline_player.__eq__ = lambda self, other: self.name == other.name

        all_players = [online_player, offline_player]
        mock_persistence.list_players.return_value = all_players

        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Online Players (1):" in result["result"]
        assert "online_user" in result["result"]
        assert "offline_user" not in result["result"]

    @pytest.mark.asyncio
    async def test_who_command_persistence_exception(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command when persistence raises an exception."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.list_players.side_effect = Exception("Database error")

        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Error retrieving player list:" in result["result"]

    @pytest.mark.asyncio
    async def test_who_command_enhanced_functionality(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command enhanced functionality with filtering."""
        mock_request.app.state.persistence = mock_persistence

        # Create players with recent last_active timestamps
        recent_time = datetime.now(UTC) - timedelta(minutes=2)

        alice = MagicMock()
        alice.name = "alice"
        alice.level = 5
        alice.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        alice.is_admin = False
        alice.last_active = recent_time

        bob = MagicMock()
        bob.name = "bob"
        bob.level = 3
        bob.current_room_id = "earth_arkhamcity_northside_room_derby_st_001"
        bob.is_admin = False
        bob.last_active = recent_time

        charlie = MagicMock()
        charlie.name = "charlie"
        charlie.level = 7
        charlie.current_room_id = "earth_arkhamcity_northside_room_high_ln_002"
        charlie.is_admin = False
        charlie.last_active = recent_time

        online_players = [alice, bob, charlie]
        mock_persistence.list_players.return_value = online_players

        # Test filtering
        result = await handle_who_command(
            {"target_player": "al"},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Players matching 'al' (1):" in result["result"]
        assert "alice" in result["result"]
        assert "bob" not in result["result"]
        assert "charlie" not in result["result"]

        # Test no matches
        result = await handle_who_command(
            {"target_player": "xyz"},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "No players found matching 'xyz'" in result["result"]


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
        player.name = "testuser"
        player.current_room_id = "room_123"
        player.pose = "adjusting spectacles"

        # Create a proper stats dictionary that get_stats() should return
        stats_dict = {
            "current_health": 85,
            "max_health": 100,
            "sanity": 75,
            "max_sanity": 100,
            "fear": 15,
            "corruption": 5,
            "occult_knowledge": 25,
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10,
            "cult_affiliation": 0,
        }

        # Mock the get_stats method to return the dictionary
        player.get_stats.return_value = stats_dict
        return player

    @pytest.fixture
    def mock_room(self):
        """Create a mock room."""
        room = MagicMock()
        room.name = "Miskatonic University Library"
        return room

    @pytest.fixture
    def mock_combat_service(self):
        """Create a mock combat service."""
        from unittest.mock import AsyncMock

        combat_service = MagicMock()
        combat_service.get_combat_by_participant = AsyncMock(return_value=None)
        return combat_service

    @pytest.mark.asyncio
    async def test_status_command_success(
        self, mock_request, mock_alias_storage, mock_persistence, mock_player, mock_room, mock_combat_service
    ):
        """Test status command with complete player information."""
        mock_request.app.state.persistence = mock_persistence
        mock_request.app.state.combat_service = mock_combat_service
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
    async def test_status_command_room_not_found(
        self, mock_request, mock_alias_storage, mock_persistence, mock_player, mock_combat_service
    ):
        """Test status command when room is not found."""
        mock_request.app.state.persistence = mock_persistence
        mock_request.app.state.combat_service = mock_combat_service
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
        self, mock_request, mock_alias_storage, mock_persistence, mock_player, mock_combat_service
    ):
        """Test status command when player has no current room."""
        mock_request.app.state.persistence = mock_persistence
        mock_request.app.state.combat_service = mock_combat_service
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
    async def test_status_command_minimal_stats(
        self, mock_request, mock_alias_storage, mock_persistence, mock_room, mock_combat_service
    ):
        """Test status command with minimal stats (no fear, corruption, occult knowledge)."""
        mock_request.app.state.persistence = mock_persistence
        mock_request.app.state.combat_service = mock_combat_service

        # Create player with minimal stats
        player = MagicMock()
        player.name = "testuser"
        player.current_room_id = "room_123"
        player.pose = None

        # Create a proper stats dictionary that get_stats() should return
        stats_dict = {
            "current_health": 100,
            "max_health": 100,
            "sanity": 100,
            "max_sanity": 100,
            "fear": 0,
            "corruption": 0,
            "occult_knowledge": 0,
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10,
            "cult_affiliation": 0,
        }

        # Mock the get_stats method to return the dictionary
        player.get_stats.return_value = stats_dict
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
            {"action": "adjusts spectacles"},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert result["result"] == "testuser adjusts spectacles"

    @pytest.mark.asyncio
    async def test_emote_command_complex_action(self, mock_request, mock_alias_storage):
        """Test emote command with complex multi-word action."""
        result = await handle_emote_command(
            {"action": "opens the forbidden tome with trembling hands"},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert result["result"] == "testuser opens the forbidden tome with trembling hands"

    @pytest.mark.asyncio
    async def test_emote_command_no_args(self, mock_request, mock_alias_storage):
        """Test emote command with no arguments."""
        result = await handle_emote_command(
            {"action": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert result["result"] == "Emote what? Usage: emote <action>"

    @pytest.mark.asyncio
    async def test_emote_command_empty_string_args(self, mock_request, mock_alias_storage):
        """Test emote command with empty string arguments."""
        result = await handle_emote_command(
            {"action": "  "},  # Two spaces
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert result["result"] == "testuser   "  # Two spaces from empty strings

    @pytest.mark.asyncio
    async def test_emote_command_special_characters(self, mock_request, mock_alias_storage):
        """Test emote command with special characters in action."""
        result = await handle_emote_command(
            {"action": "whispers something in an ancient tongue..."},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert result["result"] == "testuser whispers something in an ancient tongue..."


class TestPlayerFilteringLogic:
    """Test the player filtering logic functions."""

    def test_filter_players_by_name_exact_match(self):
        """Test filtering players by exact name match."""
        # Create mock players
        alice = MagicMock()
        alice.name = "alice"

        bob = MagicMock()
        bob.name = "bob"

        charlie = MagicMock()
        charlie.name = "charlie"

        players = [alice, bob, charlie]

        # Test exact match
        result = filter_players_by_name(players, "alice")
        assert len(result) == 1
        assert result[0].name == "alice"

        result = filter_players_by_name(players, "bob")
        assert len(result) == 1
        assert result[0].name == "bob"

    def test_filter_players_by_name_partial_match(self):
        """Test filtering players by partial name match."""
        # Create mock players
        alice = MagicMock()
        alice.name = "alice"

        bob = MagicMock()
        bob.name = "bob"

        charlie = MagicMock()
        charlie.name = "charlie"

        players = [alice, bob, charlie]

        # Test partial match
        result = filter_players_by_name(players, "al")
        assert len(result) == 1
        assert result[0].name == "alice"

        result = filter_players_by_name(players, "ch")
        assert len(result) == 1
        assert result[0].name == "charlie"

    def test_filter_players_by_name_case_insensitive(self):
        """Test filtering players with case-insensitive matching."""
        # Create mock players
        alice = MagicMock()
        alice.name = "Alice"

        bob = MagicMock()
        bob.name = "BOB"

        charlie = MagicMock()
        charlie.name = "Charlie"

        players = [alice, bob, charlie]

        # Test case-insensitive matching
        result = filter_players_by_name(players, "alice")
        assert len(result) == 1
        assert result[0].name == "Alice"

        result = filter_players_by_name(players, "bob")
        assert len(result) == 1
        assert result[0].name == "BOB"

        result = filter_players_by_name(players, "ALICE")
        assert len(result) == 1
        assert result[0].name == "Alice"

    def test_filter_players_by_name_empty_filter(self):
        """Test filtering players with empty filter returns all players."""
        # Create mock players
        alice = MagicMock()
        alice.name = "alice"

        bob = MagicMock()
        bob.name = "bob"

        players = [alice, bob]

        # Test empty filter
        result = filter_players_by_name(players, "")
        assert len(result) == 2
        assert result == players

        result = filter_players_by_name(players, None)
        assert len(result) == 2
        assert result == players

    def test_filter_players_by_name_no_matches(self):
        """Test filtering players with no matches."""
        # Create mock players
        alice = MagicMock()
        alice.name = "alice"

        bob = MagicMock()
        bob.name = "bob"

        players = [alice, bob]

        # Test no matches
        result = filter_players_by_name(players, "xyz")
        assert len(result) == 0

        result = filter_players_by_name(players, "nonexistent")
        assert len(result) == 0

    def test_filter_players_by_name_special_characters(self):
        """Test filtering players with special characters in names."""
        # Create mock players with special characters
        player1 = MagicMock()
        player1.name = "player_123"

        player2 = MagicMock()
        player2.name = "test-user"

        player3 = MagicMock()
        player3.name = "admin@server"

        players = [player1, player2, player3]

        # Test filtering with special characters
        result = filter_players_by_name(players, "123")
        assert len(result) == 1
        assert result[0].name == "player_123"

        result = filter_players_by_name(players, "test")
        assert len(result) == 1
        assert result[0].name == "test-user"

        result = filter_players_by_name(players, "admin")
        assert len(result) == 1
        assert result[0].name == "admin@server"


class TestLocationFormatting:
    """Test the location formatting functions."""

    def test_format_player_location_standard_format(self):
        """Test formatting player location with standard room ID format."""
        room_id = "earth_arkhamcity_northside_intersection_derby_high"
        result = format_player_location(room_id)
        expected = "Arkhamcity: Northside: Intersection Derby High"
        assert result == expected

    def test_format_player_location_different_zones(self):
        """Test formatting player location with different zone formats."""
        # Test different zone
        room_id = "earth_dunwich_village_old_man_whateley_farm"
        result = format_player_location(room_id)
        expected = "Dunwich: Village: Old Man Whateley Farm"
        assert result == expected

        # Test another format
        room_id = "earth_innsmouth_waterfront_docks_warehouse_7"
        result = format_player_location(room_id)
        expected = "Innsmouth: Waterfront: Docks Warehouse 7"
        assert result == expected

    def test_format_player_location_edge_cases(self):
        """Test formatting player location with edge cases."""
        # Test minimal format
        room_id = "earth_zone_subzone_room"
        result = format_player_location(room_id)
        expected = "Zone: Subzone: Room"
        assert result == expected

        # Test single word room name
        room_id = "earth_arkhamcity_center"
        result = format_player_location(room_id)
        expected = "Earth Arkhamcity Center"
        assert result == expected

    def test_format_player_location_invalid_format(self):
        """Test formatting player location with invalid format."""
        # Test too few parts
        room_id = "earth_arkham"
        result = format_player_location(room_id)
        expected = "Earth Arkham"  # Fallback formatting
        assert result == expected

        # Test empty string
        room_id = ""
        result = format_player_location(room_id)
        expected = ""  # Empty string
        assert result == expected

    def test_format_player_location_special_characters(self):
        """Test formatting player location with special characters."""
        # Test with underscores in room names
        room_id = "earth_arkhamcity_old_man_whateley_house"
        result = format_player_location(room_id)
        expected = "Arkhamcity: Old: Man Whateley House"
        assert result == expected


class TestMockPlayerSorting:
    """Test that mock players can be sorted properly (regression test for MagicMock comparison issue)."""

    def create_mock_player(self, name, level, room_id, is_admin, last_active):
        """Create a mock player with proper comparison methods."""
        player = MagicMock()
        player.name = name
        player.level = level
        player.current_room_id = room_id
        player.is_admin = is_admin
        player.last_active = last_active

        # Add comparison methods to prevent MagicMock comparison issues
        player.__lt__ = lambda self, other: self.name < other.name if hasattr(other, "name") else NotImplemented
        player.__le__ = lambda self, other: self.name <= other.name if hasattr(other, "name") else NotImplemented
        player.__gt__ = lambda self, other: self.name > other.name if hasattr(other, "name") else NotImplemented
        player.__ge__ = lambda self, other: self.name >= other.name if hasattr(other, "name") else NotImplemented
        player.__eq__ = lambda self, other: self.name == other.name if hasattr(other, "name") else NotImplemented
        player.__ne__ = lambda self, other: self.name != other.name if hasattr(other, "name") else NotImplemented

        return player

    def test_mock_player_sorting(self):
        """Test that mock players can be sorted without comparison errors."""
        from datetime import UTC, datetime, timedelta

        recent_time = datetime.now(UTC) - timedelta(minutes=2)

        # Create mock players with different names
        players = [
            self.create_mock_player("charlie", 3, "room1", False, recent_time),
            self.create_mock_player("alice", 1, "room2", False, recent_time),
            self.create_mock_player("bob", 2, "room3", False, recent_time),
        ]

        # This should not raise an exception
        sorted_players = sorted(players, key=lambda p: (p.name, id(p)))

        # Check that sorting worked correctly
        assert sorted_players[0].name == "alice"
        assert sorted_players[1].name == "bob"
        assert sorted_players[2].name == "charlie"

    def test_format_player_entry_with_mock(self):
        """Test that format_player_entry works with mock players."""
        from datetime import UTC, datetime, timedelta

        recent_time = datetime.now(UTC) - timedelta(minutes=2)
        player = self.create_mock_player("testuser", 5, "earth_arkhamcity_center", False, recent_time)

        # This should not raise an exception
        result = format_player_entry(player)

        # Check basic formatting
        assert "testuser" in result
        assert "[5]" in result
        assert "Earth Arkhamcity Center" in result


class TestPlayerEntryFormatting:
    """Test the player entry formatting functions."""

    def test_format_player_entry_normal_player(self):
        """Test formatting player entry for normal (non-admin) player."""
        # Create mock player
        player = MagicMock()
        player.name = "alice"
        player.level = 5
        player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        player.is_admin = False

        result = format_player_entry(player)
        expected = "alice [5] - Arkhamcity: Northside: Intersection Derby High"
        assert result == expected

    def test_format_player_entry_admin_player(self):
        """Test formatting player entry for admin player."""
        # Create mock admin player
        player = MagicMock()
        player.name = "admin"
        player.level = 10
        player.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        player.is_admin = True

        result = format_player_entry(player)
        expected = "admin [10] [ADMIN] - Arkhamcity: Northside: Intersection Derby High"
        assert result == expected

    def test_format_player_entry_different_levels(self):
        """Test formatting player entry with different levels."""
        # Create mock players with different levels
        player1 = MagicMock()
        player1.name = "newbie"
        player1.level = 1
        player1.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        player1.is_admin = False

        player2 = MagicMock()
        player2.name = "veteran"
        player2.level = 50
        player2.current_room_id = "earth_arkhamcity_northside_intersection_derby_high"
        player2.is_admin = False

        result1 = format_player_entry(player1)
        expected1 = "newbie [1] - Arkhamcity: Northside: Intersection Derby High"
        assert result1 == expected1

        result2 = format_player_entry(player2)
        expected2 = "veteran [50] - Arkhamcity: Northside: Intersection Derby High"
        assert result2 == expected2


class TestWhoCommandIntegration:
    """Integration tests for the who command with real data scenarios."""

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

    def create_mock_player(self, name, level, room_id, is_admin, last_active):
        """Create a mock player with proper comparison methods."""
        player = MagicMock()
        player.name = name
        player.level = level
        player.current_room_id = room_id
        player.is_admin = is_admin
        player.last_active = last_active

        # Add comparison methods to prevent MagicMock comparison issues
        player.__lt__ = lambda self, other: self.name < other.name if hasattr(other, "name") else NotImplemented
        player.__le__ = lambda self, other: self.name <= other.name if hasattr(other, "name") else NotImplemented
        player.__gt__ = lambda self, other: self.name > other.name if hasattr(other, "name") else NotImplemented
        player.__ge__ = lambda self, other: self.name >= other.name if hasattr(other, "name") else NotImplemented
        player.__eq__ = lambda self, other: self.name == other.name if hasattr(other, "name") else NotImplemented
        player.__ne__ = lambda self, other: self.name != other.name if hasattr(other, "name") else NotImplemented

        return player

    @pytest.mark.asyncio
    async def test_who_command_with_real_player_data(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command with realistic player data scenarios."""
        mock_request.app.state.persistence = mock_persistence

        # Create realistic player data
        recent_time = datetime.now(UTC) - timedelta(minutes=2)
        old_time = datetime.now(UTC) - timedelta(minutes=10)

        # Create diverse player scenarios
        players = [
            # Online admin player
            self.create_mock_player(
                "admin_user", 25, "earth_arkhamcity_northside_intersection_derby_high", True, recent_time
            ),
            # Online regular player
            self.create_mock_player(
                "investigator_alice", 8, "earth_arkhamcity_northside_room_derby_st_001", False, recent_time
            ),
            # Online player with special characters in name
            self.create_mock_player(
                "professor_whateley", 15, "earth_dunwich_village_old_man_whateley_farm", False, recent_time
            ),
            # Offline player (should not appear)
            self.create_mock_player("offline_user", 3, "earth_arkhamcity_northside_room_high_ln_002", False, old_time),
        ]

        mock_persistence.list_players.return_value = players

        # Test who command without filter
        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        # Should show 3 online players (excluding offline_user)
        assert "Online Players (3):" in result["result"]
        assert "admin_user" in result["result"]
        assert "[ADMIN]" in result["result"]  # Admin indicator
        assert "investigator_alice" in result["result"]
        assert "professor_whateley" in result["result"]
        assert "offline_user" not in result["result"]

        # Test filtering with partial match
        result = await handle_who_command(
            {"target_player": "alice"},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Players matching 'alice' (1):" in result["result"]
        assert "investigator_alice" in result["result"]
        assert "admin_user" not in result["result"]

        # Test filtering with case-insensitive match
        result = await handle_who_command(
            {"target_player": "ADMIN"},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Players matching 'ADMIN' (1):" in result["result"]
        assert "admin_user" in result["result"]

    @pytest.mark.asyncio
    async def test_who_command_large_player_list(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command with a large number of players."""
        mock_request.app.state.persistence = mock_persistence

        # Create a large list of players (100 players)
        recent_time = datetime.now(UTC) - timedelta(minutes=2)
        players = []

        for i in range(100):
            player = MagicMock()
            player.name = f"player_{i:03d}"
            player.level = (i % 50) + 1  # Levels 1-50
            player.current_room_id = f"earth_arkhamcity_room_{i:03d}"
            player.is_admin = i % 10 == 0  # Every 10th player is admin
            player.last_active = recent_time
            players.append(player)

        mock_persistence.list_players.return_value = players

        # Test who command with large list
        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        # Should show all 100 players
        assert "Online Players (100):" in result["result"]
        assert "player_000" in result["result"]
        assert "player_099" in result["result"]

        # Test filtering with large list
        result = await handle_who_command(
            {"target_player": "player_01"},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        # Should find players with "player_01" in name (player_010, player_011, etc.)
        assert "Players matching 'player_01'" in result["result"]
        assert "player_010" in result["result"]

    @pytest.mark.asyncio
    async def test_who_command_concurrent_scenarios(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command with concurrent player update scenarios."""
        mock_request.app.state.persistence = mock_persistence

        # Simulate players with different last_active timestamps
        now = datetime.now(UTC)
        very_recent = now - timedelta(seconds=30)  # Very recent
        recent = now - timedelta(minutes=2)  # Recent
        borderline = now - timedelta(minutes=5, seconds=1)  # Just over threshold
        old = now - timedelta(minutes=10)  # Old

        players = [
            self.create_mock_player("very_active", 5, "earth_arkhamcity_center", False, very_recent),
            self.create_mock_player("active", 3, "earth_arkhamcity_northside", False, recent),
            self.create_mock_player("borderline", 7, "earth_arkhamcity_southside", False, borderline),
            self.create_mock_player("inactive", 2, "earth_arkhamcity_eastside", False, old),
        ]

        mock_persistence.list_players.return_value = players

        # Test who command - should show only very_active and active
        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        # Should show 2 online players (very_active and active)
        assert "Online Players (2):" in result["result"]
        assert "very_active" in result["result"]
        assert "active" in result["result"]
        assert "borderline" not in result["result"]  # Just over threshold
        assert "inactive" not in result["result"]  # Too old

    @pytest.mark.asyncio
    async def test_who_command_admin_privileges(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command with admin privilege scenarios."""
        mock_request.app.state.persistence = mock_persistence

        recent_time = datetime.now(UTC) - timedelta(minutes=2)

        # Create players with various admin statuses
        players = [
            self.create_mock_player("super_admin", 50, "earth_arkhamcity_admin_quarters", True, recent_time),
            self.create_mock_player("moderator", 30, "earth_arkhamcity_mod_office", True, recent_time),
            self.create_mock_player("regular_user", 10, "earth_arkhamcity_public_area", False, recent_time),
        ]

        mock_persistence.list_players.return_value = players

        # Test who command - should show all players with proper admin indicators
        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Online Players (3):" in result["result"]
        assert "super_admin" in result["result"]
        assert "moderator" in result["result"]
        assert "regular_user" in result["result"]

        # Count admin indicators
        admin_count = result["result"].count("[ADMIN]")
        assert admin_count == 2  # super_admin and moderator

        # Test filtering admin players
        result = await handle_who_command(
            {"target_player": "admin"},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Players matching 'admin' (1):" in result["result"]
        assert "super_admin" in result["result"]
        assert "[ADMIN]" in result["result"]

    @pytest.mark.asyncio
    async def test_who_command_persistence_failures(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command with persistence layer failures."""
        mock_request.app.state.persistence = mock_persistence

        # Test database connection failure
        mock_persistence.list_players.side_effect = Exception("Database connection lost")

        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Error retrieving player list:" in result["result"]
        assert "Database connection lost" in result["result"]

        # Test with no persistence layer
        mock_request.app.state.persistence = None

        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert result["result"] == "Player information is not available."

    @pytest.mark.asyncio
    async def test_who_command_edge_cases_integration(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command with various edge cases in integration scenarios."""
        mock_request.app.state.persistence = mock_persistence

        recent_time = datetime.now(UTC) - timedelta(minutes=2)

        # Create players with edge case scenarios
        players = [
            # Player with very long name
            self.create_mock_player(
                "very_long_player_name_with_many_characters", 1, "earth_arkhamcity_center", False, recent_time
            ),
            # Player with special characters
            self.create_mock_player("player@#$%", 5, "earth_arkhamcity_northside", False, recent_time),
            # Player with numbers
            self.create_mock_player("player123", 10, "earth_arkhamcity_southside", False, recent_time),
            # Player with mixed case
            self.create_mock_player("PlayerWithMixedCase", 15, "earth_arkhamcity_eastside", False, recent_time),
        ]

        mock_persistence.list_players.return_value = players

        # Test who command with edge case players
        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Online Players (4):" in result["result"]
        assert "very_long_player_name_with_many_characters" in result["result"]
        assert "player@#$%" in result["result"]
        assert "player123" in result["result"]
        assert "PlayerWithMixedCase" in result["result"]

        # Test filtering with edge cases
        result = await handle_who_command(
            {"target_player": "123"},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Players matching '123' (1):" in result["result"]
        assert "player123" in result["result"]

        # Test case-insensitive filtering with mixed case
        result = await handle_who_command(
            {"target_player": "mixedcase"},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        assert "Players matching 'mixedcase' (1):" in result["result"]
        assert "PlayerWithMixedCase" in result["result"]


class TestWhoCommandPerformance:
    """Performance tests for the who command."""

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
    async def test_who_command_performance_large_player_list(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command performance with 1000+ players."""
        import time

        mock_request.app.state.persistence = mock_persistence

        # Create a large list of players (1000 players)
        recent_time = datetime.now(UTC) - timedelta(minutes=2)
        players = []

        for i in range(1000):
            player = MagicMock()
            player.name = f"player_{i:04d}"
            player.level = (i % 50) + 1  # Levels 1-50
            player.current_room_id = f"earth_arkhamcity_room_{i:04d}"
            player.is_admin = i % 20 == 0  # Every 20th player is admin
            player.last_active = recent_time
            players.append(player)

        mock_persistence.list_players.return_value = players

        # Measure response time
        start_time = time.time()

        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        end_time = time.time()
        response_time = (end_time - start_time) * 1000  # Convert to milliseconds

        # Should show all 1000 players
        assert "Online Players (1000):" in result["result"]

        # Performance requirement: response time under 100ms
        assert response_time < 100, f"Response time {response_time:.2f}ms exceeds 100ms limit"

        print(f"Who command with 1000 players: {response_time:.2f}ms")

    @pytest.mark.asyncio
    async def test_who_command_performance_filtering(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command performance with filtering on large dataset."""
        import time

        mock_request.app.state.persistence = mock_persistence

        # Create a large list of players (500 players)
        recent_time = datetime.now(UTC) - timedelta(minutes=2)
        players = []

        for i in range(500):
            player = MagicMock()
            player.name = f"player_{i:03d}"
            player.level = (i % 50) + 1
            player.current_room_id = f"earth_arkhamcity_room_{i:03d}"
            player.is_admin = i % 25 == 0
            player.last_active = recent_time
            players.append(player)

        mock_persistence.list_players.return_value = players

        # Test filtering performance
        start_time = time.time()

        result = await handle_who_command(
            {"target_player": "player_01"},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )

        end_time = time.time()
        response_time = (end_time - start_time) * 1000

        # Should find players with "player_01" in name
        assert "Players matching 'player_01'" in result["result"]

        # Performance requirement: response time under 100ms
        assert response_time < 100, f"Filtering response time {response_time:.2f}ms exceeds 100ms limit"

        print(f"Who command filtering with 500 players: {response_time:.2f}ms")

    # TEMPORARILY REMOVED: test_who_command_performance_memory_usage
    # This test was causing hangs in the full test suite due to memory pressure
    # when creating 2000 mock players and running 10 iterations
    # TODO: Rewrite this test with smaller dataset or different approach

    @pytest.mark.skip(reason="Temporarily skipping performance consistency test that hangs in full test suite")
    @pytest.mark.asyncio
    async def test_who_command_performance_consistency(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command performance consistency across multiple runs."""
        import time

        mock_request.app.state.persistence = mock_persistence

        # Create a moderate list of players (200 players)
        recent_time = datetime.now(UTC) - timedelta(minutes=2)
        players = []

        for i in range(200):
            player = MagicMock()
            player.name = f"player_{i:03d}"
            player.level = (i % 50) + 1
            player.current_room_id = f"earth_arkhamcity_room_{i:03d}"
            player.is_admin = i % 20 == 0
            player.last_active = recent_time
            players.append(player)

        mock_persistence.list_players.return_value = players

        # Run multiple times and measure consistency
        response_times = []

        for _ in range(20):
            start_time = time.time()

            result = await handle_who_command(
                {"target_player": ""},
                {"username": "testuser"},
                mock_request,
                mock_alias_storage,
                "testuser",
            )

            end_time = time.time()
            response_time = (end_time - start_time) * 1000
            response_times.append(response_time)

            assert "Online Players (200):" in result["result"]

        # Calculate statistics
        avg_response_time = sum(response_times) / len(response_times)
        max_response_time = max(response_times)
        min_response_time = min(response_times)

        # Performance requirements
        assert avg_response_time < 50, f"Average response time {avg_response_time:.2f}ms exceeds 50ms limit"
        assert max_response_time < 100, f"Max response time {max_response_time:.2f}ms exceeds 100ms limit"

        # Consistency requirement: max should not be more than 3x min (or 50ms if min is 0)
        consistency_threshold = max(min_response_time * 3, 50) if min_response_time > 0 else 50
        assert max_response_time < consistency_threshold, (
            f"Performance inconsistency: max {max_response_time:.2f}ms vs threshold {consistency_threshold:.2f}ms (min: {min_response_time:.2f}ms)"
        )

        print(
            f"Performance consistency - Avg: {avg_response_time:.2f}ms, Min: {min_response_time:.2f}ms, Max: {max_response_time:.2f}ms"
        )

    @pytest.mark.asyncio
    async def test_who_command_performance_edge_cases(self, mock_request, mock_alias_storage, mock_persistence):
        """Test who command performance with edge cases."""
        import time

        mock_request.app.state.persistence = mock_persistence

        # Test with no players
        mock_persistence.list_players.return_value = []

        start_time = time.time()
        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )
        end_time = time.time()
        response_time = (end_time - start_time) * 1000

        assert result["result"] == "No players found."
        assert response_time < 10, f"Empty list response time {response_time:.2f}ms exceeds 10ms limit"

        # Test with single player
        recent_time = datetime.now(UTC) - timedelta(minutes=2)
        single_player = MagicMock(
            name="single_player",
            level=1,
            current_room_id="earth_arkhamcity_center",
            is_admin=False,
            last_active=recent_time,
        )
        mock_persistence.list_players.return_value = [single_player]

        start_time = time.time()
        result = await handle_who_command(
            {"target_player": ""},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )
        end_time = time.time()
        response_time = (end_time - start_time) * 1000

        assert "Online Players (1):" in result["result"]
        assert response_time < 10, f"Single player response time {response_time:.2f}ms exceeds 10ms limit"

        # Test with very long filter term
        start_time = time.time()
        result = await handle_who_command(
            {"target_player": "very_long_filter_term_that_should_not_match_anything"},
            {"username": "testuser"},
            mock_request,
            mock_alias_storage,
            "testuser",
        )
        end_time = time.time()
        response_time = (end_time - start_time) * 1000

        assert "No players found matching" in result["result"]
        assert response_time < 10, f"Long filter response time {response_time:.2f}ms exceeds 10ms limit"

        print("Edge case performance tests passed - all under 10ms")
