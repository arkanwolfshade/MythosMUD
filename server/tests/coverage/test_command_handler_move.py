"""
Movement and exploration command tests for command_handler_unified.py.
"""

import uuid
from unittest.mock import AsyncMock, Mock

import pytest

from server.command_handler_unified import process_command
from server.middleware.command_rate_limiter import command_rate_limiter
from server.models.room import Room


class TestMovementAndExplorationCommands:
    """Test movement and exploration commands."""

    @pytest.fixture(autouse=True)
    def reset_rate_limiter(self):
        """Reset rate limiter before each test to prevent test interference."""
        command_rate_limiter.reset_player("testuser")
        command_rate_limiter.reset_player("targetuser")
        yield
        # Cleanup after test
        command_rate_limiter.reset_player("testuser")
        command_rate_limiter.reset_player("targetuser")

    @pytest.mark.asyncio
    async def test_process_command_go_no_persistence(self) -> None:
        """Test go command with no persistence layer."""
        mock_request = Mock()
        mock_request.app.state.persistence = None
        mock_alias_storage = Mock()
        # Mock alias storage to return None for any alias lookup
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        result = await process_command("go", ["north"], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "you can't go that way" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_go_no_direction(self) -> None:
        """Test go command with no direction."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        # Mock player for catatonia check
        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        result = await process_command("go", [], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        # New validation system returns different error message
        assert "go command requires a direction" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_go_player_not_found(self) -> None:
        """Test go command when player not found."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        # Use AsyncMock for get_player_by_name since it's awaited
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=None)
        mock_alias_storage = Mock()
        # Mock alias storage to return None for any alias lookup
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        result = await process_command("go", ["north"], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "you can't go that way" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_go_current_room_not_found(self) -> None:
        """Test go command when current room not found."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_player.get_stats.return_value = {"position": "standing"}
        # Use AsyncMock for get_player_by_name since it's awaited
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        # Mock room not found - go command uses get_room_by_id, not get_room
        mock_request.app.state.persistence.get_room_by_id.return_value = None

        result = await process_command("go", ["north"], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "you can't go that way" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_go_no_exit_in_direction(self) -> None:
        """Test go command when no exit in direction."""
        mock_request = Mock()
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_player.player_id = "test_player_id"
        mock_player.id = "test_player_id"
        mock_player.get_stats.return_value = {"position": "standing"}
        # Use AsyncMock for get_player_by_name since it's awaited
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        # Mock room data with no north exit
        mock_room = Mock(spec=Room)
        mock_room.id = "test_room_001"
        mock_room.name = "Test Room"
        mock_room.description = "A test room"
        mock_room.exits = {"south": "room2"}  # No north exit
        # Go command uses get_room_by_id, not get_room
        mock_request.app.state.persistence.get_room_by_id.return_value = mock_room

        result = await process_command("go", ["north"], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "you can't go that way" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_go_target_room_not_found(self) -> None:
        """Test go command when target room not found."""
        mock_request = Mock()
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_player.player_id = "test_player_id"
        mock_player.id = "test_player_id"
        mock_player.get_stats.return_value = {"position": "standing"}
        # Use AsyncMock for get_player_by_name since it's awaited
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        # Mock room data with invalid target
        mock_room = Mock(spec=Room)
        mock_room.id = "test_room_001"
        mock_room.name = "Test Room"
        mock_room.description = "A test room"
        mock_room.exits = {"north": "nonexistent_room"}

        # Mock get_room_by_id to return the mock room for current room, but None for target room
        # Go command uses get_room_by_id, not get_room
        def mock_get_room_by_id(room_id):
            if room_id == "test_room_001":
                return mock_room
            elif room_id == "nonexistent_room":
                return None
            return None

        mock_request.app.state.persistence.get_room_by_id.side_effect = mock_get_room_by_id

        result = await process_command("go", ["north"], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "you can't go that way" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_go_blocked_when_not_standing(self) -> None:
        """Test go command blocks movement when player is not standing."""
        mock_request = Mock()
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        mock_player.player_id = "test_player_id"
        mock_player.id = "test_player_id"
        mock_player.get_stats.return_value = {"position": "sitting"}
        # Use AsyncMock for get_player_by_name since it's awaited
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        mock_room = Mock(spec=Room)
        mock_room.id = "test_room_001"
        mock_room.name = "Test Room"
        mock_room.description = "A test room"
        mock_room.exits = {"north": "room2"}
        mock_request.app.state.persistence.get_room.return_value = mock_room

        result = await process_command("go", ["north"], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "stand" in result["result"].lower()
        mock_player.get_stats.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_command_look_no_persistence(self) -> None:
        """Test look command with no persistence layer."""
        mock_request = Mock()
        mock_request.app.state.persistence = None
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        result = await process_command("look", [], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "you see nothing special" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_look_player_not_found(self) -> None:
        """Test look command when player not found."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        # Use AsyncMock for get_player_by_name since it's awaited
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=None)
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        result = await process_command("look", [], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "you see nothing special" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_look_room_not_found(self) -> None:
        """Test look command when room not found."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        # Use AsyncMock for get_player_by_name since it's awaited
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        # Mock room not found - look command uses get_room_by_id, not get_room
        mock_request.app.state.persistence.get_room_by_id.return_value = None

        result = await process_command("look", [], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "you see nothing special" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_look_in_direction_no_exit(self) -> None:
        """Test look command in direction with no exit."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        # Use AsyncMock for get_player_by_name since it's awaited
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        # Mock room data with no north exit
        mock_room = Mock(spec=Room)
        mock_room.id = "test_room_001"
        mock_room.name = "Test Room"
        mock_room.description = "A test room"
        mock_room.exits = {"south": "room2"}  # No north exit
        mock_room.get_players = Mock(return_value=[])
        # Look command uses get_room_by_id, not get_room
        mock_request.app.state.persistence.get_room_by_id.return_value = mock_room

        # Mock connection manager and room manager for room drops
        mock_connection_manager = Mock()
        mock_room_manager = Mock()
        mock_room_manager.list_room_drops = Mock(return_value=[])
        mock_connection_manager.room_manager = mock_room_manager
        mock_request.app.state.connection_manager = mock_connection_manager

        # Mock NPC instance service
        import server.commands.look_npc as look_npc_module
        import server.services.npc_instance_service as npc_service_module

        mock_npc_instance_service = Mock()
        mock_lifecycle_manager = Mock()
        mock_lifecycle_manager.active_npcs = {}
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            m.setattr(look_npc_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            result = await process_command(
                "look", ["north"], current_user, mock_request, mock_alias_storage, "testuser"
            )

        assert "result" in result
        assert "you see nothing special that way" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_look_in_direction_target_room_not_found(self) -> None:
        """Test look command in direction when target room not found."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        # Use AsyncMock for get_player_by_name since it's awaited
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        # Mock room data with invalid target
        mock_room = Mock(spec=Room)
        mock_room.id = "test_room_001"
        mock_room.name = "Test Room"
        mock_room.description = "A test room"
        mock_room.exits = {"north": "nonexistent_room"}
        mock_room.get_players = Mock(return_value=[])
        # Look command uses get_room_by_id, not get_room
        mock_request.app.state.persistence.get_room_by_id.return_value = mock_room

        # Mock connection manager and room manager for room drops
        mock_connection_manager = Mock()
        mock_room_manager = Mock()
        mock_room_manager.list_room_drops = Mock(return_value=[])
        mock_connection_manager.room_manager = mock_room_manager
        mock_request.app.state.connection_manager = mock_connection_manager

        # Mock NPC instance service
        import server.commands.look_npc as look_npc_module
        import server.services.npc_instance_service as npc_service_module

        mock_npc_instance_service = Mock()
        mock_lifecycle_manager = Mock()
        mock_lifecycle_manager.active_npcs = {}
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            m.setattr(look_npc_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            result = await process_command(
                "look", ["north"], current_user, mock_request, mock_alias_storage, "testuser"
            )

        assert "result" in result
        assert "test room" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_process_command_look_with_null_exits(self) -> None:
        """Test look command with null exits."""
        mock_request = Mock()
        mock_request.app.state.persistence = Mock()
        mock_alias_storage = Mock()
        mock_alias_storage.get_alias.return_value = None
        current_user = {"username": "testuser"}

        # Mock player data
        mock_player = Mock()
        mock_player.current_room_id = "test_room_001"
        # Use AsyncMock for get_player_by_name since it's awaited
        mock_request.app.state.persistence.get_player_by_name = AsyncMock(return_value=mock_player)

        # Mock room data with null exits
        mock_room = Mock(spec=Room)
        mock_room.id = "test_room_001"
        mock_room.name = "Test Room"
        mock_room.description = "A test room"
        mock_room.exits = {"north": None, "south": None}
        mock_room.get_players = Mock(return_value=[])
        # Look command uses get_room_by_id, not get_room
        mock_request.app.state.persistence.get_room_by_id.return_value = mock_room

        # Mock connection manager and room manager for room drops
        mock_connection_manager = Mock()
        mock_room_manager = Mock()
        mock_room_manager.list_room_drops = Mock(return_value=[])
        mock_connection_manager.room_manager = mock_room_manager
        mock_request.app.state.connection_manager = mock_connection_manager

        # Mock NPC instance service
        import server.commands.look_npc as look_npc_module
        import server.services.npc_instance_service as npc_service_module

        mock_npc_instance_service = Mock()
        mock_lifecycle_manager = Mock()
        mock_lifecycle_manager.active_npcs = {}
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            m.setattr(look_npc_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            result = await process_command("look", [], current_user, mock_request, mock_alias_storage, "testuser")

        assert "result" in result
        assert "test room" in result["result"].lower()
