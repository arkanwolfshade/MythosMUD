"""
Unit tests for inventory command factory helper functions.

Tests the helper functions in command_factories_inventory.py.
"""

import pytest

from server.exceptions import ValidationError
from server.utils.command_factories_inventory import InventoryCommandFactory


def test_create_inventory_command():
    """Test create_inventory_command() creates InventoryCommand."""
    command = InventoryCommandFactory.create_inventory_command([])
    assert command is not None


def test_create_inventory_command_with_args():
    """Test create_inventory_command() raises error with args."""
    with pytest.raises(ValidationError):
        InventoryCommandFactory.create_inventory_command(["arg"])


def test_create_pickup_command_with_index():
    """Test create_pickup_command() with numeric index."""
    command = InventoryCommandFactory.create_pickup_command(["1"])
    assert command.index == 1
    assert command.search_term is None


def test_create_pickup_command_with_quantity():
    """Test create_pickup_command() with quantity."""
    command = InventoryCommandFactory.create_pickup_command(["item", "5"])
    assert command.search_term == "item"
    assert command.quantity == 5


def test_create_pickup_command_invalid_quantity():
    """Test create_pickup_command() raises error for invalid quantity."""
    with pytest.raises(ValidationError):
        InventoryCommandFactory.create_pickup_command(["item", "0"])


def test_create_pickup_command_invalid_index():
    """Test create_pickup_command() raises error for invalid index."""
    with pytest.raises(ValidationError):
        InventoryCommandFactory.create_pickup_command(["0"])


def test_create_drop_command_with_quantity():
    """Test create_drop_command() with quantity."""
    command = InventoryCommandFactory.create_drop_command(["1", "5"])
    assert command.index == 1
    assert command.quantity == 5


def test_create_drop_command_invalid_index():
    """Test create_drop_command() raises error for invalid index."""
    with pytest.raises(ValidationError):
        InventoryCommandFactory.create_drop_command(["not_a_number"])


def test_create_put_command():
    """Test create_put_command() creates PutCommand."""
    command = InventoryCommandFactory.create_put_command(["item", "container"])
    assert command.item == "item"
    assert command.container == "container"


def test_create_put_command_with_in():
    """Test create_put_command() handles optional 'in' keyword."""
    command = InventoryCommandFactory.create_put_command(["item", "in", "container"])
    assert command.item == "item"
    assert command.container == "container"


def test_create_put_command_with_quantity():
    """Test create_put_command() with quantity."""
    command = InventoryCommandFactory.create_put_command(["item", "container", "5"])
    assert command.quantity == 5


def test_create_get_command():
    """Test create_get_command() creates GetCommand."""
    command = InventoryCommandFactory.create_get_command(["item", "container"])
    assert command.item == "item"
    assert command.container == "container"


def test_create_get_command_with_from():
    """Test create_get_command() handles optional 'from' keyword."""
    command = InventoryCommandFactory.create_get_command(["item", "from", "container"])
    assert command.item == "item"
    assert command.container == "container"


def test_create_equip_command_with_slot():
    """Test create_equip_command() with slot."""
    command = InventoryCommandFactory.create_equip_command(["1", "head"])
    assert command.index == 1
    assert command.target_slot == "head"


def test_create_equip_command_with_name_and_slot():
    """Test create_equip_command() with item name and inferred slot."""
    command = InventoryCommandFactory.create_equip_command(["sword", "head"])
    assert command.search_term == "sword"
    assert command.target_slot == "head"


def test_create_unequip_command_with_slot():
    """Test create_unequip_command() with slot."""
    command = InventoryCommandFactory.create_unequip_command(["head"])
    assert command.slot == "head"
    assert command.search_term is None


def test_create_unequip_command_with_name():
    """Test create_unequip_command() with item name."""
    command = InventoryCommandFactory.create_unequip_command(["sword"])
    assert command.search_term == "sword"
    assert command.slot is None
