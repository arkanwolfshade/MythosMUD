import logging
from copy import deepcopy
from typing import Protocol, cast
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
from server.services.inventory_service import InventoryCapacityError, InventoryService


class DropCommandLogRecord(Protocol):
    # Scholars of the waking realm: these contracts mirror the structured log payloads recorded for a successful drop.
    # Tireless machine aides: preserve these attributes so mypy remains appeased while we verify log contents.
    player: str
    player_id: str
    item_id: str
    quantity: int
    room_id: object


class PickupFailureLogRecord(Protocol):
    # Archivists in the stacks: this protocol captures the structured context for rejected pickups.
    # Algorithmic custodians: lean on these fields to keep static type wards intact.
    player: str
    player_id: str
    reason: str
    room_id: object


@pytest.fixture
def command_context():
    """Build a request context with mocked persistence and connection services."""

    persistence = MagicMock()
    # CRITICAL: get_player_by_name must be AsyncMock because it's awaited in _resolve_player
    persistence.get_player_by_name = AsyncMock(return_value=None)
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
                "item_instance_id": "instance-tonic_laudanum",
                "prototype_id": "tonic_laudanum",
                "item_id": "tonic_laudanum",
                "item_name": "Laudanum Tonic",
                "slot_type": "backpack",
                "quantity": 3,
                "metadata": {"dose_ml": 10},
            },
            {
                "item_instance_id": "instance-lantern_battered",
                "prototype_id": "lantern_battered",
                "item_id": "lantern_battered",
                "item_name": "Battered Lantern",
                "slot_type": "left_hand",
                "quantity": 1,
            },
            {
                "item_instance_id": "instance-scrap_paper",
                "prototype_id": "scrap_paper",
                "item_id": "scrap_paper",
                "item_name": "Scrap Paper",
                "quantity": 2,
                # No slot_type - this is in general inventory
            },
        ]
    )
    player.set_equipped_items(
        {
            "head": {
                "item_instance_id": "instance-obsidian_helm",
                "prototype_id": "obsidian_helm",
                "item_id": "obsidian_helm",
                "item_name": "Obsidian Helm",
                "slot_type": "head",
                "quantity": 1,
            }
        }
    )
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)

    result = await handle_inventory_command({}, {"username": player_name}, request, alias_storage, player_name)

    output = result["result"]
    # Items with slot_type='backpack' (in container) and slot_type='left_hand' (equipped) don't count
    # Only items in general inventory (no slot_type) count toward regular inventory
    assert "You are carrying 1 / 20 slots" in output
    assert "Laudanum Tonic" in output  # In container (slot_type='backpack')
    assert "dose_ml=10" in output
    assert "Battered Lantern" in output  # Equipped (slot_type='left_hand')
    assert "Scrap Paper" in output  # In general inventory (no slot_type)
    assert "Equipped:" in output
    assert "head: Obsidian Helm" in output


@pytest.mark.asyncio
async def test_pickup_command_transfers_room_item(command_context):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)
    player_room_id = cast(str, player.current_room_id)

    drop_stack = {
        "item_instance_id": "instance-eldritch_relic",
        "prototype_id": "eldritch_relic",
        "item_id": "eldritch_relic",
        "item_name": "Eldritch Relic",
        "slot_type": "backpack",
        "quantity": 2,
    }
    room_manager.add_room_drop(player_room_id, drop_stack)

    result = await handle_pickup_command(
        {"index": 1, "quantity": 1},
        {"username": player_name},
        request,
        alias_storage,
        player_name,
    )

    inventory = player.get_inventory()
    assert len(inventory) == 1
    assert inventory[0]["prototype_id"] == "eldritch_relic"
    assert inventory[0]["quantity"] == 1
    assert "item_instance_id" in inventory[0]

    remaining_drop = room_manager.list_room_drops(player_room_id)
    assert remaining_drop[0]["quantity"] == 1
    persistence.save_player.assert_called_once_with(player)
    assert "You pick up 1x Eldritch Relic" in result["result"]
    connection_manager.broadcast_to_room.assert_awaited()


@pytest.mark.asyncio
async def test_pickup_command_supports_fuzzy_name_lookup(command_context):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)
    player_room_id = cast(str, player.current_room_id)

    room_manager.add_room_drop(
        player_room_id,
        {
            "item_instance_id": "instance-clockwork-crown",
            "prototype_id": "equipment.head.clockwork_crown",
            "item_id": "equipment.head.clockwork_crown",
            "item_name": "Clockwork Aether Crown",
            "slot_type": "head",
            "quantity": 1,
        },
    )
    room_manager.add_room_drop(
        player_room_id,
        {
            "item_instance_id": "instance-spare-tonic",
            "prototype_id": "consumable.tonic_generic",
            "item_id": "consumable.tonic_generic",
            "item_name": "Generic Tonic",
            "slot_type": "backpack",
            "quantity": 2,
        },
    )

    result = await handle_pickup_command(
        {"search_term": "crown"},
        {"username": player_name},
        request,
        alias_storage,
        player_name,
    )

    inventory = player.get_inventory()
    assert len(inventory) == 1
    assert inventory[0]["item_id"] == "equipment.head.clockwork_crown"
    assert result["result"].startswith("You pick up 1x Clockwork Aether Crown")
    remaining_drop = room_manager.list_room_drops(player_room_id)
    assert len(remaining_drop) == 1
    assert remaining_drop[0]["item_id"] == "consumable.tonic_generic"


@pytest.mark.asyncio
async def test_pickup_command_reports_missing_fuzzy_match(command_context):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)
    player_room_id = cast(str, player.current_room_id)

    room_manager.add_room_drop(
        player_room_id,
        {
            "item_instance_id": "instance-spare-tonic",
            "prototype_id": "consumable.tonic_generic",
            "item_id": "consumable.tonic_generic",
            "item_name": "Generic Tonic",
            "slot_type": "backpack",
            "quantity": 1,
        },
    )

    result = await handle_pickup_command(
        {"search_term": "eldritch"},
        {"username": player_name},
        request,
        alias_storage,
        player_name,
    )

    assert result["result"] == "There is no item here matching 'eldritch'."
    assert room_manager.list_room_drops(player_room_id)[0]["item_id"] == "consumable.tonic_generic"
    persistence.save_player.assert_not_called()


@pytest.mark.asyncio
async def test_drop_command_moves_item_to_room(command_context):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory(
        [
            {
                "item_instance_id": "instance-eldritch_relic",
                "prototype_id": "eldritch_relic",
                "item_id": "eldritch_relic",
                "item_name": "Eldritch Relic",
                "slot_type": "backpack",
                "quantity": 3,
            }
        ]
    )
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)
    player_room_id = cast(str, player.current_room_id)

    result = await handle_drop_command(
        {"index": 1, "quantity": 2},
        {"username": player_name},
        request,
        alias_storage,
        player_name,
    )

    inventory = player.get_inventory()
    assert inventory[0]["quantity"] == 1

    drops = room_manager.list_room_drops(player_room_id)
    assert len(drops) == 1
    assert drops[0]["quantity"] == 2
    assert drops[0]["prototype_id"] == "eldritch_relic"

    persistence.save_player.assert_called_once_with(player)
    assert "You drop 2x Eldritch Relic" in result["result"]
    connection_manager.broadcast_to_room.assert_awaited()


@pytest.mark.asyncio
async def test_drop_command_logs_structured_success(
    command_context,
    caplog: pytest.LogCaptureFixture,
    capsys: pytest.CaptureFixture[str],
):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory(
        [
            {
                "item_instance_id": "instance-eldritch_relic",
                "prototype_id": "eldritch_relic",
                "item_id": "eldritch_relic",
                "item_name": "Eldritch Relic",
                "slot_type": "backpack",
                "quantity": 3,
            }
        ]
    )
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)
    player_id = cast(str, player.player_id)
    player_room_id = cast(str, player.current_room_id)

    capsys.readouterr()

    with caplog.at_level(logging.INFO, logger="server.commands.inventory_commands"):
        await handle_drop_command(
            {"index": 1, "quantity": 2},
            {"username": player_name},
            request,
            alias_storage,
            player_name,
        )

    drop_logs = [record for record in caplog.records if record.message == "Item dropped"]
    if drop_logs:
        log_record = cast(DropCommandLogRecord, drop_logs[0])
        assert log_record.player == player_name
        assert log_record.player_id == player_id
        assert log_record.item_id == "eldritch_relic"
        assert log_record.quantity == 2
        assert str(log_record.room_id) == player_room_id
    else:
        combined_output = (caplog.text or "") + capsys.readouterr().out
        assert "Item dropped" in combined_output
        assert player_name in combined_output
        assert player_id in combined_output
        assert "eldritch_relic" in combined_output
        assert "quantity=2" in combined_output
        assert player_room_id in combined_output


@pytest.mark.asyncio
async def test_pickup_command_logs_capacity_failure(
    monkeypatch: pytest.MonkeyPatch,
    command_context,
    caplog: pytest.LogCaptureFixture,
    capsys: pytest.CaptureFixture[str],
):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)
    player_id = cast(str, player.player_id)
    player_room_id = cast(str, player.current_room_id)

    drop_stack = {
        "item_instance_id": "instance-obsidian_amulet",
        "prototype_id": "obsidian_amulet",
        "item_id": "obsidian_amulet",
        "item_name": "Obsidian Amulet",
        "slot_type": "backpack",
        "quantity": 1,
    }
    room_manager.add_room_drop(player_room_id, drop_stack)

    def raise_capacity_error(self, inventory, incoming):  # noqa: D401, ANN001
        raise InventoryCapacityError("Inventory is at capacity for eldritch artifacts.")

    monkeypatch.setattr(InventoryService, "add_stack", raise_capacity_error, raising=False)

    capsys.readouterr()

    with caplog.at_level(logging.INFO, logger="server.commands.inventory_commands"):
        result = await handle_pickup_command(
            {"index": 1, "quantity": 1},
            {"username": player_name},
            request,
            alias_storage,
            player_name,
        )

    assert "You cannot pick that up" in result["result"]

    failure_logs = [record for record in caplog.records if record.message == "Pickup rejected"]
    if failure_logs:
        log_record = cast(PickupFailureLogRecord, failure_logs[0])
        assert log_record.player == player_name
        assert log_record.player_id == player_id
        assert log_record.reason == "Inventory is at capacity for eldritch artifacts."
        assert str(log_record.room_id) == player_room_id
    else:
        combined_output = (caplog.text or "") + capsys.readouterr().out
        assert "Pickup rejected" in combined_output
        assert player_name in combined_output
        assert player_id in combined_output
        assert "Inventory is at capacity for eldritch artifacts." in combined_output


@pytest.mark.asyncio
async def test_equip_command_moves_item_to_equipped(command_context):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory(
        [
            {
                "item_instance_id": "instance-lantern_battered",
                "prototype_id": "lantern_battered",
                "item_id": "lantern_battered",
                "item_name": "Battered Lantern",
                "slot_type": "left_hand",
                "quantity": 1,
            }
        ]
    )
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)

    result = await handle_equip_command(
        {"index": 1, "target_slot": None},
        {"username": player_name},
        request,
        alias_storage,
        player_name,
    )

    inventory = player.get_inventory()
    assert inventory == []
    equipped = player.get_equipped_items()
    assert equipped["left_hand"]["item_name"] == "Battered Lantern"
    persistence.save_player.assert_called_once_with(player)
    assert "You equip Battered Lantern" in result["result"]
    connection_manager.broadcast_to_room.assert_awaited()


@pytest.mark.asyncio
async def test_equip_command_accepts_fuzzy_name(command_context):
    request, persistence, connection_manager, _room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory(
        [
            {
                "item_instance_id": "instance-lantern_battered",
                "prototype_id": "lantern_battered",
                "item_id": "lantern_battered",
                "item_name": "Battered Lantern",
                "slot_type": "left_hand",
                "quantity": 1,
            }
        ]
    )
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)

    result = await handle_equip_command(
        {"index": None, "search_term": "lantern", "target_slot": None},
        {"username": player_name},
        request,
        alias_storage,
        player_name,
    )

    assert "You equip Battered Lantern" in result["result"]
    assert player.get_inventory() == []
    assert player.get_equipped_items()["left_hand"]["item_name"] == "Battered Lantern"
    connection_manager.broadcast_to_room.assert_awaited()


@pytest.mark.asyncio
async def test_equip_command_normalizes_slot_type(command_context):
    request, persistence, connection_manager, _room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory(
        [
            {
                "item_instance_id": "instance-clockwork_crown",
                "prototype_id": "equipment.head.clockwork_crown",
                "item_id": "equipment.head.clockwork_crown",
                "item_name": "Clockwork Aether Crown",
                "slot_type": "head",
                "quantity": 1,
            }
        ]
    )
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)

    persistence.save_player.reset_mock()

    result = await handle_equip_command(
        {"index": 1, "target_slot": "HEAD"},
        {"username": player_name},
        request,
        alias_storage,
        player_name,
    )

    assert "You equip Clockwork Aether Crown" in result["result"]
    equipped = player.get_equipped_items()
    assert "head" in equipped
    assert equipped["head"]["slot_type"] == "head"
    persistence.save_player.assert_called_once_with(player)
    connection_manager.broadcast_to_room.assert_awaited()


@pytest.mark.asyncio
async def test_equip_command_reports_missing_fuzzy_match(command_context):
    request, persistence, connection_manager, _room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory(
        [
            {
                "item_instance_id": "instance-tonic",
                "prototype_id": "tonic_laudanum",
                "item_id": "tonic_laudanum",
                "item_name": "Laudanum Tonic",
                "slot_type": "backpack",
                "quantity": 1,
            }
        ]
    )
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)

    result = await handle_equip_command(
        {"index": None, "search_term": "lantern", "target_slot": None},
        {"username": player_name},
        request,
        alias_storage,
        player_name,
    )

    assert result["result"] == "You do not have an item matching 'lantern'."
    assert player.get_inventory()[0]["item_name"] == "Laudanum Tonic"
    persistence.save_player.assert_not_called()
    connection_manager.broadcast_to_room.assert_not_called()


@pytest.mark.asyncio
async def test_equip_command_duplicate_token_suppresses_second_attempt(command_context):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    starting_inventory = [
        {
            "item_instance_id": "instance-lantern_battered",
            "prototype_id": "lantern_battered",
            "item_id": "lantern_battered",
            "item_name": "Battered Lantern",
            "slot_type": "left_hand",
            "quantity": 1,
        }
    ]
    player.set_inventory(deepcopy(starting_inventory))
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)

    command = {"index": 1, "target_slot": None, "mutation_token": "token-equip-1"}

    first_result = await handle_equip_command(command, {"username": player_name}, request, alias_storage, player_name)
    assert "You equip Battered Lantern" in first_result["result"]

    player.set_inventory(deepcopy(starting_inventory))
    player.set_equipped_items({})
    persistence.save_player.reset_mock()

    second_result = await handle_equip_command(command, {"username": player_name}, request, alias_storage, player_name)
    assert second_result["result"] == "That action is already being processed."
    persistence.save_player.assert_not_called()


@pytest.mark.asyncio
async def test_unequip_command_returns_item_to_inventory(command_context):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory([])
    player.set_equipped_items(
        {
            "head": {
                "item_instance_id": "instance-obsidian_helm",
                "prototype_id": "obsidian_helm",
                "item_id": "obsidian_helm",
                "item_name": "Obsidian Helm",
                "slot_type": "head",
                "quantity": 1,
            }
        }
    )
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)

    result = await handle_unequip_command(
        {"slot": "HEAD"},
        {"username": player_name},
        request,
        alias_storage,
        player_name,
    )

    inventory = player.get_inventory()
    assert len(inventory) == 1
    assert inventory[0]["item_name"] == "Obsidian Helm"
    assert player.get_equipped_items().get("head") is None
    persistence.save_player.assert_called_once_with(player)
    assert "You remove Obsidian Helm" in result["result"]
    connection_manager.broadcast_to_room.assert_awaited()


@pytest.mark.asyncio
async def test_unequip_command_duplicate_token_suppresses_second_attempt(command_context):
    request, persistence, connection_manager, room_manager, alias_storage = command_context

    player = make_player()
    equipped_payload = {
        "item_instance_id": "instance-obsidian_helm",
        "prototype_id": "obsidian_helm",
        "item_id": "obsidian_helm",
        "item_name": "Obsidian Helm",
        "slot_type": "head",
        "quantity": 1,
    }
    player.set_inventory([])
    player.set_equipped_items({"head": equipped_payload})
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)

    command = {"slot": "head", "mutation_token": "token-unequip-1"}

    first_result = await handle_unequip_command(command, {"username": player_name}, request, alias_storage, player_name)
    assert "You remove Obsidian Helm" in first_result["result"]

    player.set_inventory([])
    player.set_equipped_items({"head": equipped_payload})
    persistence.save_player.reset_mock()

    second_result = await handle_unequip_command(
        command, {"username": player_name}, request, alias_storage, player_name
    )
    assert second_result["result"] == "That action is already being processed."
    persistence.save_player.assert_not_called()


@pytest.mark.asyncio
async def test_unequip_command_accepts_fuzzy_name(command_context):
    request, persistence, connection_manager, _room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory([])
    player.set_equipped_items(
        {
            "head": {
                "item_instance_id": "instance-clockwork_crown",
                "prototype_id": "equipment.head.clockwork_crown",
                "item_id": "equipment.head.clockwork_crown",
                "item_name": "Clockwork Aether Crown",
                "slot_type": "head",
                "quantity": 1,
            }
        }
    )
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)

    result = await handle_unequip_command(
        {"slot": None, "search_term": "Crown"},
        {"username": player_name},
        request,
        alias_storage,
        player_name,
    )

    assert "You remove Clockwork Aether Crown" in result["result"]
    assert len(player.get_inventory()) == 1
    assert player.get_equipped_items() == {}
    connection_manager.broadcast_to_room.assert_awaited()


@pytest.mark.asyncio
async def test_unequip_command_reports_missing_fuzzy_match(command_context):
    request, persistence, connection_manager, _room_manager, alias_storage = command_context

    player = make_player()
    player.set_inventory([])
    player.set_equipped_items(
        {
            "head": {
                "item_instance_id": "instance-clockwork_crown",
                "prototype_id": "equipment.head.clockwork_crown",
                "item_id": "equipment.head.clockwork_crown",
                "item_name": "Clockwork Aether Crown",
                "slot_type": "head",
                "quantity": 1,
            }
        }
    )
    persistence.get_player_by_name.return_value = player
    player_name = cast(str, player.name)

    result = await handle_unequip_command(
        {"slot": None, "search_term": "amulet"},
        {"username": player_name},
        request,
        alias_storage,
        player_name,
    )

    assert result["result"] == "You do not have an equipped item matching 'amulet'."
    assert player.get_equipped_items()["head"]["item_name"] == "Clockwork Aether Crown"
    persistence.save_player.assert_not_called()
    connection_manager.broadcast_to_room.assert_not_called()
