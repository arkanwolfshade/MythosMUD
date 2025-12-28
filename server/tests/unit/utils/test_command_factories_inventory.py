"""
Unit tests for inventory command factories.

Tests the InventoryCommandFactory class methods.
"""

import pytest

from server.exceptions import ValidationError
from server.utils.command_factories_inventory import InventoryCommandFactory


def test_create_pickup_command():
    """Test create_pickup_command() creates PickupCommand."""
    command = InventoryCommandFactory.create_pickup_command(["item"])
    assert command.search_term == "item"


def test_create_pickup_command_no_args():
    """Test create_pickup_command() raises error with no args."""
    with pytest.raises(ValidationError):
        InventoryCommandFactory.create_pickup_command([])


def test_create_drop_command():
    """Test create_drop_command() creates DropCommand."""
    command = InventoryCommandFactory.create_drop_command(["1"])
    assert command.index == 1


def test_create_drop_command_no_args():
    """Test create_drop_command() raises error with no args."""
    with pytest.raises(ValidationError):
        InventoryCommandFactory.create_drop_command([])


def test_create_equip_command():
    """Test create_equip_command() creates EquipCommand."""
    command = InventoryCommandFactory.create_equip_command(["item"])
    assert command.search_term == "item"


def test_create_equip_command_no_args():
    """Test create_equip_command() raises error with no args."""
    with pytest.raises(ValidationError):
        InventoryCommandFactory.create_equip_command([])


def test_create_unequip_command():
    """Test create_unequip_command() creates UnequipCommand."""
    command = InventoryCommandFactory.create_unequip_command(["item"])
    assert command.search_term == "item"


def test_create_unequip_command_no_args():
    """Test create_unequip_command() raises error with no args."""
    with pytest.raises(ValidationError):
        InventoryCommandFactory.create_unequip_command([])
