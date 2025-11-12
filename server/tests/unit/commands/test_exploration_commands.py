from unittest.mock import MagicMock

import pytest

from server.commands.exploration_commands import handle_look_command


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
            "item_id": "sigil_elder_sign",
            "item_name": "Elder Sign Token",
            "slot_type": "backpack",
            "quantity": 1,
        },
        {
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
