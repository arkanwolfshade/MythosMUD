import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.look_helpers import (
    _get_health_label,
    _get_lucidity_label,
    _get_visible_equipment,
    _parse_instance_number,
)
from server.commands.look_player import _get_players_in_room


class TestParseInstanceNumber:
    """Test _parse_instance_number helper function."""

    def test_parse_instance_number_hyphen_syntax(self) -> None:
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

    def test_parse_instance_number_space_syntax(self) -> None:
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

    def test_parse_instance_number_no_instance(self) -> None:
        """Test parsing target without instance number."""
        target, instance = _parse_instance_number("backpack")
        assert target == "backpack"
        assert instance is None

        target, instance = _parse_instance_number("lantern")
        assert target == "lantern"
        assert instance is None

    def test_parse_instance_number_multi_word_hyphen(self) -> None:
        """Test parsing instance number with multi-word target and hyphen."""
        target, instance = _parse_instance_number("leather backpack-2")
        assert target == "leather backpack"
        assert instance == 2

    def test_parse_instance_number_multi_word_space(self) -> None:
        """Test parsing instance number with multi-word target and space."""
        target, instance = _parse_instance_number("leather backpack 2")
        assert target == "leather backpack"
        assert instance == 2


class TestGetHealthLabel:
    """Test _get_health_label helper function."""

    def test_get_health_label_healthy(self) -> None:
        """Test health label for healthy player (>75%)."""
        stats = {"current_dp": 20, "max_dp": 20}  # DP max = (CON + SIZ) / 5
        assert _get_health_label(stats) == "healthy"

        stats = {"current_dp": 80, "max_dp": 100}
        assert _get_health_label(stats) == "healthy"

        stats = {"current_dp": 76, "max_dp": 100}
        assert _get_health_label(stats) == "healthy"

    def test_get_health_label_wounded(self) -> None:
        """Test health label for wounded player (25-75%)."""
        stats = {"current_dp": 75, "max_dp": 100}
        assert _get_health_label(stats) == "wounded"

        stats = {"current_dp": 50, "max_dp": 100}
        assert _get_health_label(stats) == "wounded"

        stats = {"current_dp": 25, "max_dp": 100}
        assert _get_health_label(stats) == "wounded"

    def test_get_health_label_critical(self) -> None:
        """Test health label for critical player (1-24%)."""
        stats = {"current_dp": 24, "max_dp": 100}
        assert _get_health_label(stats) == "critical"

        stats = {"current_dp": 10, "max_dp": 100}
        assert _get_health_label(stats) == "critical"

        stats = {"current_dp": 1, "max_dp": 100}
        assert _get_health_label(stats) == "critical"

    def test_get_health_label_mortally_wounded(self) -> None:
        """Test health label for mortally wounded player (<=0%)."""
        stats = {"current_dp": 0, "max_dp": 100}
        assert _get_health_label(stats) == "mortally wounded"

        stats = {"current_dp": -10, "max_dp": 100}
        assert _get_health_label(stats) == "mortally wounded"


class TestGetLucidityLabel:
    """Test _get_lucidity_label helper function."""

    def test_get_lucidity_label_lucid(self) -> None:
        """Test lucidity label for lucid player (>75%)."""
        stats = {"lucidity": 100, "max_lucidity": 100}
        assert _get_lucidity_label(stats) == "lucid"

        stats = {"lucidity": 80, "max_lucidity": 100}
        assert _get_lucidity_label(stats) == "lucid"

        stats = {"lucidity": 76, "max_lucidity": 100}
        assert _get_lucidity_label(stats) == "lucid"

    def test_get_lucidity_label_disturbed(self) -> None:
        """Test lucidity label for disturbed player (25-75%)."""
        stats = {"lucidity": 75, "max_lucidity": 100}
        assert _get_lucidity_label(stats) == "disturbed"

        stats = {"lucidity": 50, "max_lucidity": 100}
        assert _get_lucidity_label(stats) == "disturbed"

        stats = {"lucidity": 25, "max_lucidity": 100}
        assert _get_lucidity_label(stats) == "disturbed"

    def test_get_lucidity_label_unstable(self) -> None:
        """Test lucidity label for unstable player (1-24%)."""
        stats = {"lucidity": 24, "max_lucidity": 100}
        assert _get_lucidity_label(stats) == "unstable"

        stats = {"lucidity": 10, "max_lucidity": 100}
        assert _get_lucidity_label(stats) == "unstable"

        stats = {"lucidity": 1, "max_lucidity": 100}
        assert _get_lucidity_label(stats) == "unstable"

    def test_get_lucidity_label_mad(self) -> None:
        """Test lucidity label for mad player (<=0%)."""
        stats = {"lucidity": 0, "max_lucidity": 100}
        assert _get_lucidity_label(stats) == "mad"

        stats = {"lucidity": -10, "max_lucidity": 100}
        assert _get_lucidity_label(stats) == "mad"


class TestGetVisibleEquipment:
    """Test _get_visible_equipment helper function."""

    def test_get_visible_equipment_all_slots(self) -> None:
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

    def test_get_visible_equipment_excludes_internal_slots(self) -> None:
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

    def test_get_visible_equipment_partial_equipment(self) -> None:
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

    def test_get_visible_equipment_no_equipment(self) -> None:
        """Test getting visible equipment with no equipment."""
        player = MagicMock()
        player.get_equipped_items.return_value = {}

        visible = _get_visible_equipment(player)
        assert len(visible) == 0


class TestGetPlayersInRoom:
    """Test _get_players_in_room helper function."""

    @pytest.mark.asyncio
    async def test_get_players_in_room_single_player(self) -> None:
        """Test getting players from room with one player."""
        room = MagicMock()
        player_id_1 = str(uuid.uuid4())
        room.get_players.return_value = [player_id_1]

        persistence = MagicMock()
        player1 = MagicMock()
        player1.name = "Armitage"
        persistence.get_player_by_id = AsyncMock(return_value=player1)

        players = await _get_players_in_room(room, persistence)
        assert len(players) == 1
        assert players[0].name == "Armitage"

    @pytest.mark.asyncio
    async def test_get_players_in_room_multiple_players(self) -> None:
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

        async def get_player_side_effect(player_id):
            if str(player_id) == player_id_1:
                return player1
            elif str(player_id) == player_id_2:
                return player2
            return None

        persistence.get_player_by_id = AsyncMock(side_effect=get_player_side_effect)

        players = await _get_players_in_room(room, persistence)
        assert len(players) == 2
        assert {p.name for p in players} == {"Armitage", "Marsh"}

    @pytest.mark.asyncio
    async def test_get_players_in_room_no_players(self) -> None:
        """Test getting players from empty room."""
        room = MagicMock()
        room.get_players.return_value = []

        persistence = MagicMock()
        players = await _get_players_in_room(room, persistence)
        assert len(players) == 0

    @pytest.mark.asyncio
    async def test_get_players_in_room_filters_none(self) -> None:
        """Test that None players are filtered out."""
        room = MagicMock()
        player_id_1 = str(uuid.uuid4())
        player_id_2 = str(uuid.uuid4())
        room.get_players.return_value = [player_id_1, player_id_2]

        persistence = MagicMock()
        player1 = MagicMock()
        player1.name = "Armitage"

        async def get_player_side_effect(player_id):
            if str(player_id) == player_id_1:
                return player1
            elif str(player_id) == player_id_2:
                return None  # Player not found
            return None

        persistence.get_player_by_id = AsyncMock(side_effect=get_player_side_effect)

        players = await _get_players_in_room(room, persistence)
        assert len(players) == 1
        assert players[0].name == "Armitage"
