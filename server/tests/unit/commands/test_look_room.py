"""
Unit tests for look room command handlers.

Tests room look functionality including formatting and display.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.look_room import (
    _filter_other_players,
    _format_containers_section,
    _format_exits_list,
    _format_items_section,
    _format_npcs_section,
    _format_players_section,
    _get_room_description,
    _get_room_id,
    _handle_direction_look,
    _handle_room_look,
)


def test_format_items_section_empty():
    """Test _format_items_section with no items."""
    result = _format_items_section([])
    # May return empty list or list with empty strings
    assert isinstance(result, list)


def test_format_items_section_with_items():
    """Test _format_items_section with items."""
    room_drops = [
        {"item_name": "sword", "quantity": 1, "slot_type": "weapon"},
        {"item_name": "potion", "quantity": 3, "slot_type": "consumable"},
    ]
    result = _format_items_section(room_drops)
    assert len(result) > 0
    assert any("sword" in str(line).lower() for line in result)


@pytest.mark.asyncio
async def test_format_containers_section_no_room_id():
    """Test _format_containers_section with no room_id."""
    result = await _format_containers_section(None, MagicMock())
    assert not result


@pytest.mark.asyncio
async def test_format_containers_section_no_persistence():
    """Test _format_containers_section with no persistence."""
    result = await _format_containers_section("test_room", None)
    assert not result


@pytest.mark.asyncio
async def test_format_containers_section_with_containers():
    """Test _format_containers_section with containers."""
    mock_persistence = AsyncMock()
    mock_persistence.get_containers_by_room_id = AsyncMock(
        return_value=[
            {"source_type": "environment", "metadata": {"name": "Chest"}},
            {"source_type": "corpse", "metadata": {"player_name": "DeadPlayer"}},
        ]
    )

    result = await _format_containers_section("test_room", mock_persistence)

    assert len(result) > 0
    assert any("Chest" in line for line in result)
    assert any("corpse" in line.lower() for line in result)


@pytest.mark.asyncio
async def test_format_containers_section_empty():
    """Test _format_containers_section with no containers."""
    mock_persistence = AsyncMock()
    mock_persistence.get_containers_by_room_id = AsyncMock(return_value=[])

    result = await _format_containers_section("test_room", mock_persistence)
    assert not result


@pytest.mark.asyncio
async def test_format_npcs_section_no_room_id():
    """Test _format_npcs_section with no room_id."""
    result = await _format_npcs_section(None)
    assert result == []


@pytest.mark.asyncio
async def test_format_npcs_section_with_npcs():
    """Test _format_npcs_section with NPCs."""
    # _format_npcs_section imports _get_npcs_in_room from look_npc, patch it at the import location
    with patch("server.commands.look_room._get_npcs_in_room", new_callable=AsyncMock) as mock_get_npcs:
        mock_get_npcs.return_value = ["Goblin", "Orc"]
        result = await _format_npcs_section("test_room")

        assert len(result) > 0
        assert any("Goblin" in line for line in result)
        assert any("Orc" in line for line in result)


@pytest.mark.asyncio
async def test_format_npcs_section_empty():
    """Test _format_npcs_section with no NPCs."""
    # _format_npcs_section imports _get_npcs_in_room from look_npc, patch it at the import location
    with patch("server.commands.look_room._get_npcs_in_room", new_callable=AsyncMock) as mock_get_npcs:
        mock_get_npcs.return_value = []
        result = await _format_npcs_section("test_room")
        assert not result


@pytest.mark.asyncio
async def test_filter_other_players_excludes_current():
    """Test _filter_other_players excludes current player."""
    player1 = MagicMock()
    player1.name = "Player1"
    player2 = MagicMock()
    player2.name = "Player2"
    player3 = MagicMock()
    player3.name = "CurrentPlayer"

    result = await _filter_other_players([player1, player2, player3], "CurrentPlayer")

    assert "Player1" in result
    assert "Player2" in result
    assert "CurrentPlayer" not in result


@pytest.mark.asyncio
async def test_filter_other_players_no_name_attribute():
    """Test _filter_other_players handles players without name attribute."""
    player1 = MagicMock()
    player1.name = "Player1"
    player2 = MagicMock()
    del player2.name

    result = await _filter_other_players([player1, player2], "CurrentPlayer")

    assert "Player1" in result
    assert len(result) == 1


def test_format_players_section_empty():
    """Test _format_players_section with no players."""
    result = _format_players_section([])
    assert not result


def test_format_players_section_with_players():
    """Test _format_players_section with players."""
    result = _format_players_section(["Player1", "Player2"])

    assert len(result) > 0
    assert any("Player1" in line for line in result)
    assert any("Player2" in line for line in result)


def test_get_room_description_with_description():
    """Test _get_room_description with description."""
    room = MagicMock()
    room.description = "A dark room"

    result = _get_room_description(room)
    assert result == "A dark room"


def test_get_room_description_no_description():
    """Test _get_room_description without description."""
    room = MagicMock()
    room.description = None

    result = _get_room_description(room)
    assert result == "You see nothing special."


def test_get_room_id_with_id():
    """Test _get_room_id with id attribute."""
    room = MagicMock()
    room.id = "test_room"

    result = _get_room_id(room)
    assert result == "test_room"


def test_get_room_id_no_id():
    """Test _get_room_id without id attribute."""
    room = MagicMock()
    del room.id

    result = _get_room_id(room)
    assert result is None


def test_format_exits_list_with_exits():
    """Test _format_exits_list with exits."""
    exits = {
        "north": {"room_id": "room_north"},
        "south": {"room_id": "room_south"},
    }

    result = _format_exits_list(exits)
    assert "north" in result.lower()
    assert "south" in result.lower()


def test_format_exits_list_no_exits():
    """Test _format_exits_list with no exits."""
    result = _format_exits_list({})
    assert result == "none"


@pytest.mark.asyncio
async def test_handle_room_look_success():
    """Test _handle_room_look successful execution."""
    mock_room = MagicMock()
    mock_room.id = "test_room"
    mock_room.name = "Test Room"
    mock_room.description = "A test room description"
    mock_room.exits = {"north": "room_north"}
    mock_room.get_players = MagicMock(return_value=[])

    mock_persistence = AsyncMock()
    mock_persistence.get_containers_by_room_id = AsyncMock(return_value=[])
    mock_persistence.get_player_by_id = AsyncMock(return_value=None)

    with patch("server.commands.look_room._get_npcs_in_room", new_callable=AsyncMock) as mock_get_npcs:
        mock_get_npcs.return_value = []

        result = await _handle_room_look(
            room=mock_room,
            room_drops=[],
            persistence=mock_persistence,
            player_name="TestPlayer",
        )

        assert "test room description" in result["result"].lower()
        assert "result" in result


@pytest.mark.asyncio
async def test_handle_direction_look_success():
    """Test _handle_direction_look successful execution."""
    mock_room = MagicMock()
    mock_room.exits = {"north": "room_north"}

    mock_target_room = MagicMock()
    mock_target_room.name = "Target Room"
    mock_target_room.description = "A target room"

    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id.return_value = mock_target_room

    result = await _handle_direction_look(
        direction="north",
        room=mock_room,
        persistence=mock_persistence,
        player_name="TestPlayer",
    )

    assert result is not None
    assert "Target Room" in result["result"]
    assert "target room" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_direction_look_no_exit():
    """Test _handle_direction_look when exit doesn't exist."""
    mock_room = MagicMock()
    mock_room.exits = {}

    mock_persistence = MagicMock()

    result = await _handle_direction_look(
        direction="north",
        room=mock_room,
        persistence=mock_persistence,
        player_name="TestPlayer",
    )

    assert result is not None
    assert "nothing special" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_direction_look_target_room_not_found():
    """Test _handle_direction_look when target room is not found."""
    mock_room = MagicMock()
    mock_room.exits = {"north": "nonexistent_room"}

    mock_persistence = MagicMock()
    mock_persistence.get_room_by_id.return_value = None

    result = await _handle_direction_look(
        direction="north",
        room=mock_room,
        persistence=mock_persistence,
        player_name="TestPlayer",
    )

    assert result is not None
    assert "nothing special" in result["result"].lower()
