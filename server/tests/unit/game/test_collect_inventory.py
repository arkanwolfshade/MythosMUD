"""Unit tests for collect_n inventory helpers."""

from unittest.mock import MagicMock

from server.game.quest.collect_inventory import (
    collect_player_stacks,
    consume_prototype_from_player,
    count_prototype_in_stacks,
)


def test_count_prototype_in_stacks_top_level():
    """Count stackable items at top level."""
    stacks = [
        {"prototype_id": "misc.herb.daisy", "quantity": 2},
        {"prototype_id": "misc.herb.rose", "quantity": 1},
    ]
    assert count_prototype_in_stacks(stacks, "misc.herb.daisy") == 2


def test_count_prototype_in_stacks_nested_container():
    """Count items inside nested inner_container.items."""
    stacks = [
        {
            "prototype_id": "wearable.backpack",
            "quantity": 1,
            "inner_container": {
                "items": [
                    {"prototype_id": "misc.herb.daisy", "quantity": 2},
                    {"item_id": "misc.herb.daisy", "quantity": 1},
                ],
            },
        },
        {"prototype_id": "misc.herb.daisy", "quantity": 1},
    ]
    assert count_prototype_in_stacks(stacks, "misc.herb.daisy") == 4


def test_consume_prototype_from_player_partial_stack():
    """Consume reduces quantity on partial stack without removing stack."""
    player = MagicMock()
    inventory = [{"prototype_id": "misc.herb.daisy", "quantity": 5}]
    player.get_inventory.return_value = inventory
    player.get_equipped_items.return_value = {}
    saved: list = []

    def _save(items):
        saved.extend(items)

    player.set_inventory = MagicMock(side_effect=_save)
    player.set_equipped_items = MagicMock()

    assert consume_prototype_from_player(player, "misc.herb.daisy", 2) is True
    assert saved[0]["quantity"] == 3


def test_consume_prototype_from_player_insufficient_returns_false():
    """Consume fails without mutating player when holdings are short."""
    player = MagicMock()
    inventory = [{"prototype_id": "misc.herb.daisy", "quantity": 1}]
    player.get_inventory.return_value = list(inventory)
    player.get_equipped_items.return_value = {}
    player.set_inventory = MagicMock()

    assert consume_prototype_from_player(player, "misc.herb.daisy", 3) is False
    player.set_inventory.assert_not_called()


def test_collect_player_stacks_merges_inventory_and_equipped():
    """collect_player_stacks includes equipped item dict values."""
    player = MagicMock()
    player.get_inventory.return_value = [{"prototype_id": "a", "quantity": 1}]
    player.get_equipped_items.return_value = {"hand": {"prototype_id": "b", "quantity": 1}}
    stacks = collect_player_stacks(player)
    assert len(stacks) == 2
