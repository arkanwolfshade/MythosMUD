import uuid
from unittest.mock import MagicMock

import pytest

from server.commands.exploration_commands import (
    _get_health_label,
    _get_players_in_room,
    _get_sanity_label,
    _get_visible_equipment,
    _parse_instance_number,
    handle_look_command,
)


def _build_request(persistence, connection_manager):
    request = MagicMock()
    request.app = MagicMock()
    request.app.state = MagicMock()
    request.app.state.persistence = persistence
    request.app.state.connection_manager = connection_manager
    return request


@pytest.mark.asyncio
async def test_handle_look_command_includes_room_drops():
    persistence = MagicMock()
    connection_manager = MagicMock()
    room_manager = MagicMock()
    connection_manager.room_manager = room_manager

    player = MagicMock()
    player.current_room_id = "arkham_observatory"
    persistence.get_player_by_name.return_value = player

    room = MagicMock()
    room.name = "Arkham Observatory"
    room.description = "Dusty brass instruments point toward uncaring stars."
    room.exits = {"north": "arkham_rooftop"}
    persistence.get_room.return_value = room

    room_manager.list_room_drops.return_value = [
        {
            "item_instance_id": "instance-sigil_elder_sign",
            "prototype_id": "sigil_elder_sign",
            "item_id": "sigil_elder_sign",
            "item_name": "Elder Sign Token",
            "slot_type": "backpack",
            "quantity": 1,
        },
        {
            "item_instance_id": "instance-phial_ichor",
            "prototype_id": "phial_ichor",
            "item_id": "phial_ichor",
            "item_name": "Phial of Viscid Ichor",
            "slot_type": "belt",
            "quantity": 3,
        },
    ]

    request = _build_request(persistence, connection_manager)
    current_user = {"username": "Armitage"}

    result = await handle_look_command({}, current_user, request, None, "Armitage")

    text = result["result"]
    assert "Scattered upon the floor" in text
    assert "1. Elder Sign Token x1 (backpack)" in text
    assert "2. Phial of Viscid Ichor x3 (belt)" in text
    assert "Exits: north" in text


@pytest.mark.asyncio
async def test_handle_look_command_no_room_drops_uses_mythos_tone():
    persistence = MagicMock()
    connection_manager = MagicMock()
    room_manager = MagicMock()
    connection_manager.room_manager = room_manager

    player = MagicMock()
    player.current_room_id = "innsmouth_dock"
    persistence.get_player_by_name.return_value = player

    room = MagicMock()
    room.name = "Innsmouth Dock"
    room.description = "Brackish waves slap against rotten pilings."
    room.exits = {}
    persistence.get_room.return_value = room

    room_manager.list_room_drops.return_value = []

    request = _build_request(persistence, connection_manager)
    current_user = {"username": "Marsh"}

    result = await handle_look_command({}, current_user, request, None, "Marsh")

    text = result["result"]
    assert "The floor bears no abandoned curios." in text
    assert "Exits: none" in text


class TestParseInstanceNumber:
    """Test _parse_instance_number helper function."""

    def test_parse_instance_number_hyphen_syntax(self):
        """Test parsing instance number with hyphen syntax."""
        target, instance = _parse_instance_number("backpack-2")
        assert target == "backpack"
        assert instance == 2

        target, instance = _parse_instance_number("lantern-1")
        assert target == "lantern"
        assert instance == 1

        target, instance = _parse_instance_number("sword-10")
        assert target == "sword"
        assert instance == 10

    def test_parse_instance_number_space_syntax(self):
        """Test parsing instance number with space syntax."""
        target, instance = _parse_instance_number("backpack 2")
        assert target == "backpack"
        assert instance == 2

        target, instance = _parse_instance_number("lantern 1")
        assert target == "lantern"
        assert instance == 1

        target, instance = _parse_instance_number("sword 10")
        assert target == "sword"
        assert instance == 10

    def test_parse_instance_number_no_instance(self):
        """Test parsing target without instance number."""
        target, instance = _parse_instance_number("backpack")
        assert target == "backpack"
        assert instance is None

        target, instance = _parse_instance_number("lantern")
        assert target == "lantern"
        assert instance is None

    def test_parse_instance_number_multi_word_hyphen(self):
        """Test parsing instance number with multi-word target and hyphen."""
        target, instance = _parse_instance_number("leather backpack-2")
        assert target == "leather backpack"
        assert instance == 2

    def test_parse_instance_number_multi_word_space(self):
        """Test parsing instance number with multi-word target and space."""
        target, instance = _parse_instance_number("leather backpack 2")
        assert target == "leather backpack"
        assert instance == 2


class TestGetHealthLabel:
    """Test _get_health_label helper function."""

    def test_get_health_label_healthy(self):
        """Test health label for healthy player (>75%)."""
        stats = {"health": 100, "max_health": 100}
        assert _get_health_label(stats) == "healthy"

        stats = {"health": 80, "max_health": 100}
        assert _get_health_label(stats) == "healthy"

        stats = {"health": 76, "max_health": 100}
        assert _get_health_label(stats) == "healthy"

    def test_get_health_label_wounded(self):
        """Test health label for wounded player (25-75%)."""
        stats = {"health": 75, "max_health": 100}
        assert _get_health_label(stats) == "wounded"

        stats = {"health": 50, "max_health": 100}
        assert _get_health_label(stats) == "wounded"

        stats = {"health": 25, "max_health": 100}
        assert _get_health_label(stats) == "wounded"

    def test_get_health_label_critical(self):
        """Test health label for critical player (1-24%)."""
        stats = {"health": 24, "max_health": 100}
        assert _get_health_label(stats) == "critical"

        stats = {"health": 10, "max_health": 100}
        assert _get_health_label(stats) == "critical"

        stats = {"health": 1, "max_health": 100}
        assert _get_health_label(stats) == "critical"

    def test_get_health_label_mortally_wounded(self):
        """Test health label for mortally wounded player (<=0%)."""
        stats = {"health": 0, "max_health": 100}
        assert _get_health_label(stats) == "mortally wounded"

        stats = {"health": -10, "max_health": 100}
        assert _get_health_label(stats) == "mortally wounded"


class TestGetSanityLabel:
    """Test _get_sanity_label helper function."""

    def test_get_sanity_label_sane(self):
        """Test sanity label for sane player (>75%)."""
        stats = {"sanity": 100, "max_sanity": 100}
        assert _get_sanity_label(stats) == "sane"

        stats = {"sanity": 80, "max_sanity": 100}
        assert _get_sanity_label(stats) == "sane"

        stats = {"sanity": 76, "max_sanity": 100}
        assert _get_sanity_label(stats) == "sane"

    def test_get_sanity_label_disturbed(self):
        """Test sanity label for disturbed player (25-75%)."""
        stats = {"sanity": 75, "max_sanity": 100}
        assert _get_sanity_label(stats) == "disturbed"

        stats = {"sanity": 50, "max_sanity": 100}
        assert _get_sanity_label(stats) == "disturbed"

        stats = {"sanity": 25, "max_sanity": 100}
        assert _get_sanity_label(stats) == "disturbed"

    def test_get_sanity_label_unstable(self):
        """Test sanity label for unstable player (1-24%)."""
        stats = {"sanity": 24, "max_sanity": 100}
        assert _get_sanity_label(stats) == "unstable"

        stats = {"sanity": 10, "max_sanity": 100}
        assert _get_sanity_label(stats) == "unstable"

        stats = {"sanity": 1, "max_sanity": 100}
        assert _get_sanity_label(stats) == "unstable"

    def test_get_sanity_label_mad(self):
        """Test sanity label for mad player (<=0%)."""
        stats = {"sanity": 0, "max_sanity": 100}
        assert _get_sanity_label(stats) == "mad"

        stats = {"sanity": -10, "max_sanity": 100}
        assert _get_sanity_label(stats) == "mad"


class TestGetVisibleEquipment:
    """Test _get_visible_equipment helper function."""

    def test_get_visible_equipment_all_slots(self):
        """Test getting visible equipment with all external slots."""
        player = MagicMock()
        player.get_equipped_items.return_value = {
            "head": {"item_name": "Hat", "prototype_id": "hat"},
            "torso": {"item_name": "Coat", "prototype_id": "coat"},
            "legs": {"item_name": "Pants", "prototype_id": "pants"},
            "hands": {"item_name": "Gloves", "prototype_id": "gloves"},
            "feet": {"item_name": "Boots", "prototype_id": "boots"},
            "main_hand": {"item_name": "Sword", "prototype_id": "sword"},
            "off_hand": {"item_name": "Shield", "prototype_id": "shield"},
        }

        visible = _get_visible_equipment(player)
        assert "head" in visible
        assert "torso" in visible
        assert "legs" in visible
        assert "hands" in visible
        assert "feet" in visible
        assert "main_hand" in visible
        assert "off_hand" in visible
        assert len(visible) == 7

    def test_get_visible_equipment_excludes_internal_slots(self):
        """Test that internal slots are excluded from visible equipment."""
        player = MagicMock()
        player.get_equipped_items.return_value = {
            "head": {"item_name": "Hat", "prototype_id": "hat"},
            "ring": {"item_name": "Ring", "prototype_id": "ring"},
            "amulet": {"item_name": "Amulet", "prototype_id": "amulet"},
            "belt": {"item_name": "Belt", "prototype_id": "belt"},
            "backpack": {"item_name": "Backpack", "prototype_id": "backpack"},
        }

        visible = _get_visible_equipment(player)
        assert "head" in visible
        assert "ring" not in visible
        assert "amulet" not in visible
        assert "belt" not in visible
        assert "backpack" not in visible
        assert len(visible) == 1

    def test_get_visible_equipment_partial_equipment(self):
        """Test getting visible equipment with partial equipment."""
        player = MagicMock()
        player.get_equipped_items.return_value = {
            "head": {"item_name": "Hat", "prototype_id": "hat"},
            "main_hand": {"item_name": "Sword", "prototype_id": "sword"},
        }

        visible = _get_visible_equipment(player)
        assert "head" in visible
        assert "main_hand" in visible
        assert len(visible) == 2

    def test_get_visible_equipment_no_equipment(self):
        """Test getting visible equipment with no equipment."""
        player = MagicMock()
        player.get_equipped_items.return_value = {}

        visible = _get_visible_equipment(player)
        assert len(visible) == 0


class TestGetPlayersInRoom:
    """Test _get_players_in_room helper function."""

    def test_get_players_in_room_single_player(self):
        """Test getting players from room with one player."""
        room = MagicMock()
        player_id_1 = str(uuid.uuid4())
        room.get_players.return_value = [player_id_1]

        persistence = MagicMock()
        player1 = MagicMock()
        player1.name = "Armitage"
        persistence.get_player.return_value = player1

        players = _get_players_in_room(room, persistence)
        assert len(players) == 1
        assert players[0].name == "Armitage"

    def test_get_players_in_room_multiple_players(self):
        """Test getting players from room with multiple players."""
        room = MagicMock()
        player_id_1 = str(uuid.uuid4())
        player_id_2 = str(uuid.uuid4())
        room.get_players.return_value = [player_id_1, player_id_2]

        persistence = MagicMock()
        player1 = MagicMock()
        player1.name = "Armitage"
        player2 = MagicMock()
        player2.name = "Marsh"

        def get_player_side_effect(player_id):
            if str(player_id) == player_id_1:
                return player1
            elif str(player_id) == player_id_2:
                return player2
            return None

        persistence.get_player.side_effect = get_player_side_effect

        players = _get_players_in_room(room, persistence)
        assert len(players) == 2
        assert {p.name for p in players} == {"Armitage", "Marsh"}

    def test_get_players_in_room_no_players(self):
        """Test getting players from empty room."""
        room = MagicMock()
        room.get_players.return_value = []

        persistence = MagicMock()
        players = _get_players_in_room(room, persistence)
        assert len(players) == 0

    def test_get_players_in_room_filters_none(self):
        """Test that None players are filtered out."""
        room = MagicMock()
        player_id_1 = str(uuid.uuid4())
        player_id_2 = str(uuid.uuid4())
        room.get_players.return_value = [player_id_1, player_id_2]

        persistence = MagicMock()
        player1 = MagicMock()
        player1.name = "Armitage"

        def get_player_side_effect(player_id):
            if str(player_id) == player_id_1:
                return player1
            elif str(player_id) == player_id_2:
                return None  # Player not found
            return None

        persistence.get_player.side_effect = get_player_side_effect

        players = _get_players_in_room(room, persistence)
        assert len(players) == 1
        assert players[0].name == "Armitage"


class TestPlayerLookFunctionality:
    """Test player look functionality in handle_look_command."""

    @pytest.mark.asyncio
    async def test_look_player_explicit_syntax(self):
        """Test looking at player with explicit syntax."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        # Current player
        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"
        persistence.get_player_by_name.return_value = current_player

        # Room
        room = MagicMock()
        room.get_players.return_value = ["target-player-id"]
        room.get_npcs.return_value = []
        persistence.get_room.return_value = room

        # Target player
        target_player = MagicMock()
        target_player.name = "Armitage"
        target_player.get_stats.return_value = {"health": 100, "max_health": 100, "sanity": 100, "max_sanity": 100}
        target_player.get_equipped_items.return_value = {"head": {"item_name": "Hat"}}
        target_player_id = uuid.uuid4()
        room.get_players.return_value = [str(target_player_id)]
        persistence.get_player.return_value = target_player

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        command_data = {"target": "Armitage", "target_type": "player"}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        assert "Armitage" in result["result"]
        assert "healthy" in result["result"] or "sane" in result["result"]

    @pytest.mark.asyncio
    async def test_look_player_health_states(self):
        """Test player look with various health states."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"
        persistence.get_player_by_name.return_value = current_player

        room = MagicMock()
        room.get_players.return_value = ["target-player-id"]
        room.get_npcs.return_value = []
        persistence.get_room.return_value = room

        # Test healthy player
        target_player = MagicMock()
        target_player.name = "Armitage"
        target_player.get_stats.return_value = {"health": 100, "max_health": 100, "sanity": 100, "max_sanity": 100}
        target_player.get_equipped_items.return_value = {}
        target_player_id = uuid.uuid4()
        room.get_players.return_value = [str(target_player_id)]
        persistence.get_player.return_value = target_player

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        command_data = {"target": "Armitage", "target_type": "player"}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        assert "healthy" in result["result"]

        # Test wounded player
        target_player.get_stats.return_value = {"health": 50, "max_health": 100, "sanity": 100, "max_sanity": 100}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")
        assert "wounded" in result["result"]

        # Test critical player
        target_player.get_stats.return_value = {"health": 10, "max_health": 100, "sanity": 100, "max_sanity": 100}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")
        assert "critical" in result["result"]

    @pytest.mark.asyncio
    async def test_look_player_sanity_states(self):
        """Test player look with various sanity states."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"
        persistence.get_player_by_name.return_value = current_player

        room = MagicMock()
        room.get_players.return_value = ["target-player-id"]
        room.get_npcs.return_value = []
        persistence.get_room.return_value = room

        target_player = MagicMock()
        target_player.name = "Armitage"
        target_player.get_stats.return_value = {"health": 100, "max_health": 100, "sanity": 50, "max_sanity": 100}
        target_player.get_equipped_items.return_value = {}
        target_player_id = uuid.uuid4()
        room.get_players.return_value = [str(target_player_id)]
        persistence.get_player.return_value = target_player

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        command_data = {"target": "Armitage", "target_type": "player"}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        assert "disturbed" in result["result"]

    @pytest.mark.asyncio
    async def test_look_player_visible_equipment(self):
        """Test player look displays visible equipment."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"
        persistence.get_player_by_name.return_value = current_player

        room = MagicMock()
        room.get_players.return_value = ["target-player-id"]
        room.get_npcs.return_value = []
        persistence.get_room.return_value = room

        target_player = MagicMock()
        target_player.name = "Armitage"
        target_player.get_stats.return_value = {"health": 100, "max_health": 100, "sanity": 100, "max_sanity": 100}
        target_player.get_equipped_items.return_value = {
            "head": {"item_name": "Hat"},
            "torso": {"item_name": "Coat"},
            "main_hand": {"item_name": "Sword"},
        }
        target_player_id = uuid.uuid4()
        room.get_players.return_value = [str(target_player_id)]
        persistence.get_player.return_value = target_player

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        command_data = {"target": "Armitage", "target_type": "player"}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        assert "Hat" in result["result"] or "Coat" in result["result"] or "Sword" in result["result"]

    @pytest.mark.asyncio
    async def test_look_player_not_found(self):
        """Test player look when player not found."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"
        persistence.get_player_by_name.return_value = current_player

        room = MagicMock()
        room.get_players.return_value = []
        room.get_npcs.return_value = []
        persistence.get_room.return_value = room

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        command_data = {"target": "Nonexistent", "target_type": "player"}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        assert "don't see anyone" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_look_player_multiple_matches(self):
        """Test player look with multiple matching players."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"
        persistence.get_player_by_name.return_value = current_player

        room = MagicMock()
        room.get_players.return_value = ["player-id-1", "player-id-2"]
        room.get_npcs.return_value = []
        persistence.get_room.return_value = room

        player_id_1 = uuid.uuid4()
        player_id_2 = uuid.uuid4()
        room.get_players.return_value = [str(player_id_1), str(player_id_2)]

        player1 = MagicMock()
        player1.name = "Armitage"
        player2 = MagicMock()
        player2.name = "Armitage"

        def get_player_side_effect(player_id):
            if str(player_id) == str(player_id_1):
                return player1
            elif str(player_id) == str(player_id_2):
                return player2
            return None

        persistence.get_player.side_effect = get_player_side_effect

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        command_data = {"target": "Armitage", "target_type": "player"}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        assert "multiple" in result["result"].lower() or "see multiple" in result["result"].lower()

    @pytest.mark.asyncio
    async def test_look_player_instance_targeting(self):
        """Test player look with instance targeting."""
        persistence = MagicMock()
        connection_manager = MagicMock()
        room_manager = MagicMock()
        connection_manager.room_manager = room_manager

        current_player = MagicMock()
        current_player.current_room_id = "test_room"
        current_player.name = "CurrentPlayer"
        persistence.get_player_by_name.return_value = current_player

        room = MagicMock()
        room.get_players.return_value = ["player-id-1", "player-id-2"]
        room.get_npcs.return_value = []
        persistence.get_room.return_value = room

        player_id_1 = uuid.uuid4()
        player_id_2 = uuid.uuid4()
        room.get_players.return_value = [str(player_id_1), str(player_id_2)]

        player1 = MagicMock()
        player1.name = "Armitage"
        player1.get_stats.return_value = {"health": 100, "max_health": 100, "sanity": 100, "max_sanity": 100}
        player1.get_equipped_items.return_value = {}
        player2 = MagicMock()
        player2.name = "Armitage"
        player2.get_stats.return_value = {"health": 50, "max_health": 100, "sanity": 100, "max_sanity": 100}
        player2.get_equipped_items.return_value = {}

        def get_player_side_effect(player_id):
            if str(player_id) == str(player_id_1):
                return player1
            elif str(player_id) == str(player_id_2):
                return player2
            return None

        persistence.get_player.side_effect = get_player_side_effect

        request = _build_request(persistence, connection_manager)
        current_user = {"username": "CurrentPlayer"}

        # Look at second instance
        command_data = {"target": "Armitage", "target_type": "player", "instance_number": 2}
        result = await handle_look_command(command_data, current_user, request, None, "CurrentPlayer")

        # Should show the second player (wounded)
        assert "wounded" in result["result"] or "Armitage" in result["result"]
