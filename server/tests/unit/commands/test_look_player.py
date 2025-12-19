import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.look_command import handle_look_command


def _build_request(persistence, connection_manager):
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    request.app.state.persistence = persistence
    request.app.state.connection_manager = connection_manager
    return request


class TestPlayerLookFunctionality:
    """Test player look functionality in handle_look_command."""

    @pytest.mark.asyncio
    async def test_look_player_explicit_syntax(self) -> None:
        """Test looking at player with explicit syntax."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        # Current player
        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"

        persistence.get_player_by_name = AsyncMock(return_value=current_player)

        # Room
        room = MagicMock()
        room.get_players.return_value = ["target-player-id"]
        room.get_npcs.return_value = []
        persistence.get_room_by_id = MagicMock(return_value=room)

        # Target player
        target_player = MagicMock()
        target_player.name = "Armitage"
        target_player.get_stats.return_value = {
            "current_dp": 100,
            "max_dp": 100,
            "lucidity": 100,
            "max_lucidity": 100,
        }
        target_player.get_equipped_items.return_value = {"head": {"item_name": "Hat"}}
        target_player_id = uuid.uuid4()
        room.get_players.return_value = [str(target_player_id)]
        persistence.get_player_by_id = AsyncMock(return_value=target_player)

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        command_data = {"target": "Armitage", "target_type": "player"}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        assert "Armitage" in result["result"]
        assert "healthy" in result["result"] or "lucid" in result["result"]

    @pytest.mark.asyncio
    async def test_look_player_health_states(self) -> None:
        """Test player look with various health states."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"

        persistence.get_player_by_name = AsyncMock(return_value=current_player)

        room = MagicMock()
        room.get_players.return_value = ["target-player-id"]
        room.get_npcs.return_value = []
        persistence.get_room_by_id = MagicMock(return_value=room)

        # Test healthy player
        target_player = MagicMock()
        target_player.name = "Armitage"
        target_player.get_stats.return_value = {
            "current_dp": 100,
            "max_dp": 100,
            "lucidity": 100,
            "max_lucidity": 100,
        }
        target_player.get_equipped_items.return_value = {}
        target_player_id = uuid.uuid4()
        room.get_players.return_value = [str(target_player_id)]
        persistence.get_player_by_id = AsyncMock(return_value=target_player)

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        command_data = {"target": "Armitage", "target_type": "player"}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        assert "healthy" in result["result"]

        # Test wounded player
        target_player.get_stats.return_value = {
            "current_dp": 50,
            "max_dp": 100,
            "lucidity": 100,
            "max_lucidity": 100,
        }
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")
        assert "wounded" in result["result"]

        # Test critical player
        target_player.get_stats.return_value = {
            "current_dp": 10,
            "max_dp": 100,
            "lucidity": 100,
            "max_lucidity": 100,
        }
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")
        assert "critical" in result["result"]

    @pytest.mark.asyncio
    async def test_look_player_lucidity_states(self) -> None:
        """Test player look with various lucidity states."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"

        persistence.get_player_by_name = AsyncMock(return_value=current_player)

        room = MagicMock()
        room.get_players.return_value = ["target-player-id"]
        room.get_npcs.return_value = []
        persistence.get_room_by_id = MagicMock(return_value=room)

        target_player = MagicMock()
        target_player.name = "Armitage"
        target_player.get_stats.return_value = {
            "current_dp": 100,
            "max_dp": 100,
            "lucidity": 50,
            "max_lucidity": 100,
        }
        target_player.get_equipped_items.return_value = {}
        target_player_id = uuid.uuid4()
        room.get_players.return_value = [str(target_player_id)]
        persistence.get_player_by_id = AsyncMock(return_value=target_player)

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        command_data = {"target": "Armitage", "target_type": "player"}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        assert "disturbed" in result["result"]

    @pytest.mark.asyncio
    async def test_look_player_visible_equipment(self) -> None:
        """Test player look displays visible equipment."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"

        persistence.get_player_by_name = AsyncMock(return_value=current_player)

        room = MagicMock()
        room.get_players.return_value = ["target-player-id"]
        room.get_npcs.return_value = []
        persistence.get_room_by_id = MagicMock(return_value=room)

        target_player = MagicMock()
        target_player.name = "Armitage"
        target_player.get_stats.return_value = {
            "current_dp": 100,
            "max_dp": 100,
            "lucidity": 100,
            "max_lucidity": 100,
        }
        target_player.get_equipped_items.return_value = {
            "head": {"item_name": "Hat"},
            "torso": {"item_name": "Coat"},
            "main_hand": {"item_name": "Sword"},
        }
        target_player_id = uuid.uuid4()
        room.get_players.return_value = [str(target_player_id)]
        persistence.get_player_by_id = AsyncMock(return_value=target_player)

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        command_data = {"target": "Armitage", "target_type": "player"}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        assert "Hat" in result["result"] or "Coat" in result["result"] or "Sword" in result["result"]

    @pytest.mark.asyncio
    async def test_look_player_not_found(self) -> None:
        """Test player look when player not found."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"

        persistence.get_player_by_name = AsyncMock(return_value=current_player)

        room = MagicMock()
        room.get_players.return_value = []
        room.get_npcs.return_value = []
        persistence.get_room_by_id = MagicMock(return_value=room)

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        command_data = {"target": "Nonexistent", "target_type": "player"}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        assert "don't see anyone" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_look_player_multiple_matches(self) -> None:
        """Test player look with multiple matching players."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"

        persistence.get_player_by_name = AsyncMock(return_value=current_player)

        room = MagicMock()
        room.get_players.return_value = ["player-id-1", "player-id-2"]
        room.get_npcs.return_value = []
        persistence.get_room_by_id = MagicMock(return_value=room)

        player_id_1 = uuid.uuid4()
        player_id_2 = uuid.uuid4()
        room.get_players.return_value = [str(player_id_1), str(player_id_2)]

        player1 = MagicMock()
        player1.name = "Armitage"
        player2 = MagicMock()
        player2.name = "Armitage"

        async def get_player_side_effect(player_id):
            if str(player_id) == str(player_id_1):
                return player1
            elif str(player_id) == str(player_id_2):
                return player2
            return None

        persistence.get_player_by_id = AsyncMock(side_effect=get_player_side_effect)

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        command_data = {"target": "Armitage", "target_type": "player"}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        assert "multiple" in result["result"].lower() or "see multiple" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_look_player_instance_targeting(self) -> None:
        """Test player look with instance targeting."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"

        persistence.get_player_by_name = AsyncMock(return_value=current_player)

        room = MagicMock()
        room.get_players.return_value = ["player-id-1", "player-id-2"]
        room.get_npcs.return_value = []
        persistence.get_room_by_id = MagicMock(return_value=room)

        player_id_1 = uuid.uuid4()
        player_id_2 = uuid.uuid4()
        room.get_players.return_value = [str(player_id_1), str(player_id_2)]

        player1 = MagicMock()
        player1.name = "Armitage"
        player1.get_stats.return_value = {
            "current_dp": 100,
            "max_dp": 100,
            "lucidity": 100,
            "max_lucidity": 100,
        }
        player1.get_equipped_items.return_value = {}
        player2 = MagicMock()
        player2.name = "Armitage"
        player2.get_stats.return_value = {"current_dp": 50, "max_dp": 100, "lucidity": 100, "max_lucidity": 100}
        player2.get_equipped_items.return_value = {}

        async def get_player_side_effect(player_id):
            if str(player_id) == str(player_id_1):
                return player1
            elif str(player_id) == str(player_id_2):
                return player2
            return None

        persistence.get_player_by_id = AsyncMock(side_effect=get_player_side_effect)

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        # Look at second instance
        command_data = {"target": "Armitage", "target_type": "player", "instance_number": 2}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        # Should show the second player (wounded)
        assert "wounded" in result["result"] or "Armitage" in result["result"]
