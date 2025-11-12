from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.inventory_commands import (
    handle_drop_command,
    handle_equip_command,
    handle_inventory_command,
    handle_pickup_command,
    handle_unequip_command,
)
from server.models.player import Player
from server.realtime.room_subscription_manager import RoomSubscriptionManager


@pytest.fixture
def command_context():
    """Build a request context with mocked persistence and connection services."""

    persistence = MagicMock()
    room_manager = RoomSubscriptionManager()
    connection_manager = MagicMock()
    connection_manager.room_manager = room_manager
    connection_manager.broadcast_to_room = AsyncMock()
    connection_manager.online_players = {}

    state = MagicMock()
    state.persistence = persistence
    state.connection_manager = connection_manager

    request = MagicMock()
    request.app = MagicMock()
    request.app.state = state

    alias_storage = MagicMock()

    return request, persistence, connection_manager, room_manager, alias_storage


def make_player(name: str = "Armitage", room_id: str = "earth_arkhamcity_test_room") -> Player:
    """Create a Player model instance with baseline inventory state."""

    player = Player(
        player_id=f"player-{name}",
        user_id=f"user-{name}",
        name=name,
        current_room_id=room_id,
    )
    player.set_inventory([])
    player.set_equipped_items({})
    return player


@pytest.mark.asyncio
async def test_inventory_command_renders_inventory_and_equipped(command_context):
    request, persistence, _connection_manager, _room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory(
        [
            {
                "item_id": "tonic_laudanum",
                "item_name": "Laudanum Tonic",
                "slot_type": "backpack",
                "quantity": 3,
                "metadata": {"dose_ml": 10},
            },
            {
                "item_id": "lantern_battered",
                "item_name": "Battered Lantern",
                "slot_type": "left_hand",
                "quantity": 1,
            },
        ]
    )
    player.set_equipped_items(
        {
            "head": {
                "item_id": "obsidian_helm",
                "item_name": "Obsidian Helm",
                "slot_type": "head",
                "quantity": 1,
            }
        }
    )
    persistence.get_player_by_name.return_value = player

    result = await handle_inventory_command({}, {"username": player.name}, request, alias_storage, player.name)

    output = result["result"]
    assert "You are carrying 2 / 20 slots" in output
    assert "1. Laudanum Tonic" in output
    assert "dose_ml=10" in output
    assert "2. Battered Lantern" in output
    assert "Equipped:" in output
    assert "head: Obsidian Helm" in output


@pytest.mark.asyncio
async def test_pickup_command_transfers_room_item(command_context):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    persistence.get_player_by_name.return_value = player

    drop_stack = {
        "item_id": "eldritch_relic",
        "item_name": "Eldritch Relic",
        "slot_type": "backpack",
        "quantity": 2,
    }
    room_manager.add_room_drop(player.current_room_id, drop_stack)

    result = await handle_pickup_command(
        {"index": 1, "quantity": 1},
        {"username": player.name},
        request,
        alias_storage,
        player.name,
    )

    inventory = player.get_inventory()
    assert len(inventory) == 1
    assert inventory[0]["item_id"] == "eldritch_relic"
    assert inventory[0]["quantity"] == 1

    remaining_drop = room_manager.list_room_drops(player.current_room_id)
    assert remaining_drop[0]["quantity"] == 1
    persistence.save_player.assert_called_once_with(player)
    assert "You pick up 1x Eldritch Relic" in result["result"]
    connection_manager.broadcast_to_room.assert_awaited()


@pytest.mark.asyncio
async def test_drop_command_moves_item_to_room(command_context):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory(
        [
            {
                "item_id": "eldritch_relic",
                "item_name": "Eldritch Relic",
                "slot_type": "backpack",
                "quantity": 3,
            }
        ]
    )
    persistence.get_player_by_name.return_value = player

    result = await handle_drop_command(
        {"index": 1, "quantity": 2},
        {"username": player.name},
        request,
        alias_storage,
        player.name,
    )

    inventory = player.get_inventory()
    assert inventory[0]["quantity"] == 1

    drops = room_manager.list_room_drops(player.current_room_id)
    assert len(drops) == 1
    assert drops[0]["quantity"] == 2

    persistence.save_player.assert_called_once_with(player)
    assert "You drop 2x Eldritch Relic" in result["result"]
    connection_manager.broadcast_to_room.assert_awaited()


@pytest.mark.asyncio
async def test_equip_command_moves_item_to_equipped(command_context):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory(
        [
            {
                "item_id": "lantern_battered",
                "item_name": "Battered Lantern",
                "slot_type": "left_hand",
                "quantity": 1,
            }
        ]
    )
    persistence.get_player_by_name.return_value = player

    result = await handle_equip_command(
        {"index": 1, "target_slot": None},
        {"username": player.name},
        request,
        alias_storage,
        player.name,
    )

    inventory = player.get_inventory()
    assert inventory == []
    equipped = player.get_equipped_items()
    assert equipped["left_hand"]["item_name"] == "Battered Lantern"
    persistence.save_player.assert_called_once_with(player)
    assert "You equip Battered Lantern" in result["result"]
    connection_manager.broadcast_to_room.assert_awaited()


@pytest.mark.asyncio
async def test_unequip_command_returns_item_to_inventory(command_context):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory([])
    player.set_equipped_items(
        {
            "head": {
                "item_id": "obsidian_helm",
                "item_name": "Obsidian Helm",
                "slot_type": "head",
                "quantity": 1,
            }
        }
    )
    persistence.get_player_by_name.return_value = player

    result = await handle_unequip_command(
        {"slot": "head"},
        {"username": player.name},
        request,
        alias_storage,
        player.name,
    )

    inventory = player.get_inventory()
    assert len(inventory) == 1
    assert inventory[0]["item_name"] == "Obsidian Helm"
    assert player.get_equipped_items().get("head") is None
    persistence.save_player.assert_called_once_with(player)
    assert "You remove Obsidian Helm" in result["result"]
    connection_manager.broadcast_to_room.assert_awaited()
