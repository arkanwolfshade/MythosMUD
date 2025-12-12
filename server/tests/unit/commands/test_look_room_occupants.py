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


class TestLookCommandRoomOccupants:
    """Test look command with room occupants and objects."""

    @pytest.mark.asyncio
    async def test_look_command_with_players_in_room(self):
        """Test look command displays other players in room."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        player = MagicMock()
        player.current_room_id = "test_room"
        player.name = "CurrentPlayer"
        persistence.get_player_by_name = AsyncMock(return_value=player)

        room = MagicMock()
        room.name = "Test Room"
        room.description = "A test room."
        room.exits = {"north": "other_room"}
        # Use proper UUIDs for player IDs
        player1_id = str(uuid.uuid4())
        player2_id = str(uuid.uuid4())
        room.get_players = MagicMock(return_value=[player1_id, player2_id])
        persistence.get_room_by_id = MagicMock(return_value=room)

        room_manager.list_room_drops.return_value = []

        # Mock other players
        player1 = MagicMock()
        player1.name = "Alice"
        player2 = MagicMock()
        player2.name = "Bob"

        async def get_player_side_effect(player_id):
            player_id_str = str(player_id)
            if player_id_str == player1_id:
                return player1
            elif player_id_str == player2_id:
                return player2
            return None

        persistence.get_player_by_id = AsyncMock(side_effect=get_player_side_effect)

        # Mock NPC instance service - patch where it's imported
        import server.commands.look_npc as look_npc_module
        import server.services.npc_instance_service as npc_service_module

        mock_npc_instance_service = MagicMock()
        mock_lifecycle_manager = MagicMock()
        mock_lifecycle_manager.active_npcs = {}
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            m.setattr(look_npc_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            result = await handle_look_command({}, current_user, request, None, "CurrentPlayer")

        text = result["result"]
        assert "Also here: Alice, Bob" in text or "Also here: Bob, Alice" in text
        assert "CurrentPlayer" not in text  # Current player should not be listed

    @pytest.mark.asyncio
    async def test_look_command_with_npcs_in_room(self):
        """Test look command displays NPCs in room."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        player = MagicMock()
        player.current_room_id = "test_room"
        player.name = "CurrentPlayer"
        persistence.get_player_by_name = AsyncMock(return_value=player)

        room = MagicMock()
        room.id = "test_room"
        room.name = "Test Room"
        room.description = "A test room."
        room.exits = {"north": "other_room"}
        room.get_players = MagicMock(return_value=[])
        persistence.get_room_by_id = MagicMock(return_value=room)

        room_manager.list_room_drops.return_value = []

        # Mock containers (empty for this test)
        persistence.get_containers_by_room_id = AsyncMock(return_value=[])

        # Mock NPC instance service
        npc_instance = MagicMock()
        npc_instance.name = "Guard"
        npc_instance.is_alive = True
        npc_instance.current_room_id = "test_room"

        npc_instance_service = MagicMock()
        lifecycle_manager = MagicMock()
        lifecycle_manager.active_npcs = {"npc1": npc_instance}
        npc_instance_service.lifecycle_manager = lifecycle_manager

        # Patch the get_npc_instance_service function - patch where it's imported
        import server.commands.look_npc as look_npc_module
        import server.services.npc_instance_service as npc_service_module

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        # Temporarily patch the import
        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: npc_instance_service)
            m.setattr(look_npc_module, "get_npc_instance_service", lambda: npc_instance_service)
            result = await handle_look_command({}, current_user, request, None, "CurrentPlayer")

        text = result["result"]
        assert "Also here: Guard" in text

    @pytest.mark.asyncio
    async def test_look_npc_as_admin_shows_stats(self):
        """Test that admins see NPC stats when looking at an NPC."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        # Create admin player
        admin_player = MagicMock()
        admin_player.current_room_id = "test_room"
        admin_player.name = "AdminPlayer"
        admin_player.is_admin = True
        persistence.get_player_by_name = AsyncMock(return_value=admin_player)

        room = MagicMock()
        room.id = "test_room"
        room.name = "Test Room"
        room.description = "A test room."
        room.exits = {}
        room.get_players = MagicMock(return_value=[])
        room.get_npcs = MagicMock(return_value=["npc1"])
        persistence.get_room_by_id = MagicMock(return_value=room)

        room_manager.list_room_drops.return_value = []
        persistence.get_containers_by_room_id = AsyncMock(return_value=[])

        # Mock NPC instance
        npc_instance = MagicMock()
        npc_instance.name = "Guard"
        npc_instance.npc_id = "npc1"
        npc_instance.is_alive = True
        npc_instance.current_room_id = "test_room"
        npc_instance.npc_type = "aggressive_mob"
        npc_instance.stats = {"strength": 50, "dexterity": 40, "constitution": 60}

        # Mock NPC definition
        npc_definition = MagicMock()
        npc_definition.description = "A fierce guard."
        npc_instance.definition = npc_definition

        # Mock NPC instance service
        npc_instance_service = MagicMock()
        lifecycle_manager = MagicMock()
        lifecycle_manager.active_npcs = {"npc1": npc_instance}
        lifecycle_manager.lifecycle_records = {}
        npc_instance_service.lifecycle_manager = lifecycle_manager

        # Mock get_npc_stats to return stats
        async def mock_get_npc_stats(npc_id: str):
            return {
                "npc_id": npc_id,
                "name": "Guard",
                "npc_type": "aggressive_mob",
                "current_room_id": "test_room",
                "is_alive": True,
                "stats": {"strength": 50, "dexterity": 40, "constitution": 60},
            }

        npc_instance_service.get_npc_stats = AsyncMock(side_effect=mock_get_npc_stats)

        # Patch the get_npc_instance_service function
        import server.commands.look_npc as look_npc_module
        import server.services.npc_instance_service as npc_service_module

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "AdminPlayer"}

        # Temporarily patch the import
        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: npc_instance_service)
            m.setattr(look_npc_module, "get_npc_instance_service", lambda: npc_instance_service)
            result = await handle_look_command(
                {"target": "Guard", "target_type": None}, current_user, request, None, "AdminPlayer"
            )

        text = result["result"]
        # Should show normal NPC description
        assert "Guard" in text
        assert "A fierce guard." in text
        # Should also show admin stats
        assert "Admin Stats" in text
        assert "npc1" in text or "NPC ID" in text
        assert "aggressive_mob" in text or "Type" in text

    @pytest.mark.asyncio
    async def test_look_npc_as_non_admin_no_stats(self):
        """Test that non-admins don't see NPC stats when looking at an NPC."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        # Create non-admin player
        player = MagicMock()
        player.current_room_id = "test_room"
        player.name = "RegularPlayer"
        player.is_admin = False
        persistence.get_player_by_name = AsyncMock(return_value=player)

        room = MagicMock()
        room.id = "test_room"
        room.name = "Test Room"
        room.description = "A test room."
        room.exits = {}
        room.get_players = MagicMock(return_value=[])
        room.get_npcs = MagicMock(return_value=["npc1"])
        persistence.get_room_by_id = MagicMock(return_value=room)

        room_manager.list_room_drops.return_value = []
        persistence.get_containers_by_room_id = AsyncMock(return_value=[])

        # Mock NPC instance
        npc_instance = MagicMock()
        npc_instance.name = "Guard"
        npc_instance.npc_id = "npc1"
        npc_instance.is_alive = True
        npc_instance.current_room_id = "test_room"

        # Mock NPC definition
        npc_definition = MagicMock()
        npc_definition.description = "A fierce guard."
        npc_instance.definition = npc_definition

        # Mock NPC instance service
        npc_instance_service = MagicMock()
        lifecycle_manager = MagicMock()
        lifecycle_manager.active_npcs = {"npc1": npc_instance}
        npc_instance_service.lifecycle_manager = lifecycle_manager

        # Patch the get_npc_instance_service function
        import server.commands.look_npc as look_npc_module
        import server.services.npc_instance_service as npc_service_module

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "RegularPlayer"}

        # Temporarily patch the import
        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: npc_instance_service)
            m.setattr(look_npc_module, "get_npc_instance_service", lambda: npc_instance_service)
            result = await handle_look_command(
                {"target": "Guard", "target_type": None}, current_user, request, None, "RegularPlayer"
            )

        text = result["result"]
        # Should show normal NPC description
        assert "Guard" in text
        assert "A fierce guard." in text
        # Should NOT show admin stats
        assert "Admin Stats" not in text

    @pytest.mark.asyncio
    async def test_look_command_with_containers_in_room(self):
        """Test look command displays containers in room."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        player = MagicMock()
        player.current_room_id = "test_room"
        player.name = "CurrentPlayer"
        persistence.get_player_by_name = AsyncMock(return_value=player)

        room = MagicMock()
        room.id = "test_room"
        room.name = "Test Room"
        room.description = "A test room."
        room.exits = {"north": "other_room"}
        room.get_players = MagicMock(return_value=[])
        persistence.get_room_by_id = MagicMock(return_value=room)

        room_manager.list_room_drops.return_value = []

        # Mock containers
        containers_data = [
            {
                "container_id": "container1",
                "source_type": "environment",
                "metadata": {"name": "Wooden Chest"},
            },
            {
                "container_id": "container2",
                "source_type": "environment",
                "metadata": {"name": "Barrel"},
            },
        ]
        persistence.get_containers_by_room_id = AsyncMock(return_value=containers_data)

        # Mock NPC instance service - patch where it's imported
        import server.commands.look_npc as look_npc_module
        import server.services.npc_instance_service as npc_service_module

        mock_npc_instance_service = MagicMock()
        mock_lifecycle_manager = MagicMock()
        mock_lifecycle_manager.active_npcs = {}
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            m.setattr(look_npc_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            result = await handle_look_command({}, current_user, request, None, "CurrentPlayer")

        text = result["result"]
        assert "You see: Wooden Chest, Barrel" in text or "You see: Barrel, Wooden Chest" in text

    @pytest.mark.asyncio
    async def test_look_command_with_corpses_in_room(self):
        """Test look command displays corpses in room."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        player = MagicMock()
        player.current_room_id = "test_room"
        player.name = "CurrentPlayer"
        persistence.get_player_by_name = AsyncMock(return_value=player)

        room = MagicMock()
        room.id = "test_room"
        room.name = "Test Room"
        room.description = "A test room."
        room.exits = {"north": "other_room"}
        room.get_players = MagicMock(return_value=[])
        persistence.get_room_by_id = MagicMock(return_value=room)

        room_manager.list_room_drops.return_value = []

        # Mock corpses
        containers_data = [
            {
                "container_id": "corpse1",
                "source_type": "corpse",
                "metadata": {"player_name": "DeadPlayer"},
            },
        ]
        persistence.get_containers_by_room_id = AsyncMock(return_value=containers_data)

        # Mock NPC instance service - patch where it's imported
        import server.commands.look_npc as look_npc_module
        import server.services.npc_instance_service as npc_service_module

        mock_npc_instance_service = MagicMock()
        mock_lifecycle_manager = MagicMock()
        mock_lifecycle_manager.active_npcs = {}
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            m.setattr(look_npc_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            result = await handle_look_command({}, current_user, request, None, "CurrentPlayer")

        text = result["result"]
        assert "the corpse of DeadPlayer" in text

    @pytest.mark.asyncio
    async def test_look_command_with_all_entities(self):
        """Test look command displays all entities when present."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        player = MagicMock()
        player.current_room_id = "test_room"
        player.name = "CurrentPlayer"
        persistence.get_player_by_name = AsyncMock(return_value=player)

        room = MagicMock()
        room.id = "test_room"
        room.name = "Test Room"
        room.description = "A test room."
        room.exits = {"north": "other_room"}
        # Use proper UUID for player ID
        player1_id = str(uuid.uuid4())
        room.get_players = MagicMock(return_value=[player1_id])
        persistence.get_room_by_id = MagicMock(return_value=room)

        room_manager.list_room_drops.return_value = []

        # Mock other player
        other_player = MagicMock()
        other_player.name = "Alice"

        async def get_player_side_effect(player_id):
            if str(player_id) == player1_id:
                return other_player
            return None

        persistence.get_player_by_id = AsyncMock(side_effect=get_player_side_effect)

        # Mock NPC
        npc_instance = MagicMock()
        npc_instance.name = "Guard"
        npc_instance.is_alive = True
        npc_instance.current_room_id = "test_room"

        npc_instance_service = MagicMock()
        lifecycle_manager = MagicMock()
        lifecycle_manager.active_npcs = {"npc1": npc_instance}
        npc_instance_service.lifecycle_manager = lifecycle_manager

        # Mock containers and corpses
        containers_data = [
            {
                "container_id": "container1",
                "source_type": "environment",
                "metadata": {"name": "Chest"},
            },
            {
                "container_id": "corpse1",
                "source_type": "corpse",
                "metadata": {"player_name": "DeadPlayer"},
            },
        ]
        persistence.get_containers_by_room_id = AsyncMock(return_value=containers_data)

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        # Temporarily patch the import - patch where it's imported
        import server.commands.look_npc as look_npc_module
        import server.services.npc_instance_service as npc_service_module

        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: npc_instance_service)
            m.setattr(look_npc_module, "get_npc_instance_service", lambda: npc_instance_service)
            result = await handle_look_command({}, current_user, request, None, "CurrentPlayer")

        text = result["result"]
        assert "Also here:" in text
        assert "Alice" in text or "Guard" in text
        assert "You see:" in text
        assert "Chest" in text
        assert "the corpse of DeadPlayer" in text

    @pytest.mark.asyncio
    async def test_look_command_filters_dead_npcs(self):
        """Test look command filters out dead NPCs."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        player = MagicMock()
        player.current_room_id = "test_room"
        player.name = "CurrentPlayer"
        persistence.get_player_by_name = AsyncMock(return_value=player)

        room = MagicMock()
        room.id = "test_room"
        room.name = "Test Room"
        room.description = "A test room."
        room.exits = {"north": "other_room"}
        room.get_players = MagicMock(return_value=[])
        persistence.get_room_by_id = MagicMock(return_value=room)

        room_manager.list_room_drops.return_value = []

        # Mock containers (empty for this test)
        persistence.get_containers_by_room_id = AsyncMock(return_value=[])

        # Mock NPC instance service with one alive and one dead NPC
        alive_npc = MagicMock()
        alive_npc.name = "AliveGuard"
        alive_npc.is_alive = True
        alive_npc.current_room_id = "test_room"

        dead_npc = MagicMock()
        dead_npc.name = "DeadGuard"
        dead_npc.is_alive = False
        dead_npc.current_room_id = "test_room"

        npc_instance_service = MagicMock()
        lifecycle_manager = MagicMock()
        lifecycle_manager.active_npcs = {"npc1": alive_npc, "npc2": dead_npc}
        npc_instance_service.lifecycle_manager = lifecycle_manager

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        # Temporarily patch the import - patch where it's imported
        import server.commands.look_npc as look_npc_module
        import server.services.npc_instance_service as npc_service_module

        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: npc_instance_service)
            m.setattr(look_npc_module, "get_npc_instance_service", lambda: npc_instance_service)
            result = await handle_look_command({}, current_user, request, None, "CurrentPlayer")

        text = result["result"]
        assert "AliveGuard" in text
        assert "DeadGuard" not in text

    @pytest.mark.asyncio
    async def test_look_command_empty_room(self):
        """Test look command with no additional entities."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        player = MagicMock()
        player.current_room_id = "test_room"
        player.name = "CurrentPlayer"
        persistence.get_player_by_name = AsyncMock(return_value=player)

        room = MagicMock()
        room.id = "test_room"
        room.name = "Test Room"
        room.description = "A test room."
        room.exits = {"north": "other_room"}
        room.get_players = MagicMock(return_value=[])
        persistence.get_room_by_id = MagicMock(return_value=room)

        room_manager.list_room_drops.return_value = []
        persistence.get_containers_by_room_id = AsyncMock(return_value=[])

        # Mock NPC instance service - patch where it's imported
        import server.commands.look_npc as look_npc_module
        import server.services.npc_instance_service as npc_service_module

        mock_npc_instance_service = MagicMock()
        mock_lifecycle_manager = MagicMock()
        mock_lifecycle_manager.active_npcs = {}
        mock_npc_instance_service.lifecycle_manager = mock_lifecycle_manager

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        with pytest.MonkeyPatch().context() as m:
            m.setattr(npc_service_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            m.setattr(look_npc_module, "get_npc_instance_service", lambda: mock_npc_instance_service)
            result = await handle_look_command({}, current_user, request, None, "CurrentPlayer")

        text = result["result"]
        assert "Also here:" not in text
        assert "You see:" not in text
        assert "Exits: north" in text
