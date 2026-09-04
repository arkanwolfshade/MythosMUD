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


def test_create_pickup_command_quantity_zero():
    """Test create_pickup_command() raises error when quantity is zero."""
    with pytest.raises(ValidationError, match="Quantity must be a positive integer"):
        InventoryCommandFactory.create_pickup_command(["sword", "0"])


def test_create_pickup_command_quantity_negative():
    """Test create_pickup_command() raises error when quantity is negative."""
    with pytest.raises(ValidationError, match="Quantity must be a positive integer"):
        InventoryCommandFactory.create_pickup_command(["sword", "-1"])


def test_create_pickup_command_index_zero():
    """Test create_pickup_command() raises error when index is zero."""
    with pytest.raises(ValidationError, match="Item number must be a positive integer"):
        InventoryCommandFactory.create_pickup_command(["0"])


def test_create_pickup_command_index_negative():
    """Test create_pickup_command() raises error when index is negative."""
    with pytest.raises(ValidationError, match="Item number must be a positive integer"):
        InventoryCommandFactory.create_pickup_command(["-1"])


def test_create_pickup_command_index_with_extra_tokens():
    """Test create_pickup_command() raises error when index has extra tokens."""
    with pytest.raises(ValidationError, match="Usage: pickup"):
        InventoryCommandFactory.create_pickup_command(["1", "extra"])


def test_create_pickup_command_empty_search_term():
    """Test create_pickup_command() raises error when search term is empty."""
    with pytest.raises(ValidationError, match="Pickup item name cannot be empty"):
        InventoryCommandFactory.create_pickup_command(["   "])


def test_create_pickup_command_quantity_only():
    """Test create_pickup_command() handles single number as index."""
    # Single number is treated as index, not quantity
    result = InventoryCommandFactory.create_pickup_command(["5"])
    assert result.index == 5
    assert result.search_term is None
    assert result.quantity is None


def test_create_drop_command_invalid_index():
    """Test create_drop_command() raises error when index is not integer."""
    with pytest.raises(ValidationError, match="Inventory index must be an integer"):
        InventoryCommandFactory.create_drop_command(["not_a_number"])


def test_create_drop_command_invalid_quantity():
    """Test create_drop_command() raises error when quantity is not integer."""
    with pytest.raises(ValidationError, match="Quantity must be an integer"):
        InventoryCommandFactory.create_drop_command(["1", "not_a_number"])


def test_create_put_command_no_args():
    """Test create_put_command() raises error with no args."""
    with pytest.raises(ValidationError, match="Usage: put"):
        InventoryCommandFactory.create_put_command([])


def test_create_put_command_only_item():
    """Test create_put_command() raises error with only item."""
    with pytest.raises(ValidationError, match="Usage: put"):
        InventoryCommandFactory.create_put_command(["sword"])


def test_create_put_command_with_in_keyword():
    """Test create_put_command() handles 'in' keyword."""
    result = InventoryCommandFactory.create_put_command(["sword", "in", "bag"])
    assert result.item == "sword"
    assert result.container == "bag"
    assert result.quantity is None


def test_create_put_command_quantity_zero():
    """Test create_put_command() raises error when quantity is zero."""
    with pytest.raises(ValidationError, match="Quantity must be a positive integer"):
        InventoryCommandFactory.create_put_command(["sword", "bag", "0"])


def test_create_put_command_quantity_negative():
    """Test create_put_command() raises error when quantity is negative."""
    with pytest.raises(ValidationError, match="Quantity must be a positive integer"):
        InventoryCommandFactory.create_put_command(["sword", "bag", "-1"])


def test_create_put_command_multi_word_container():
    """Test create_put_command() handles multi-word container."""
    result = InventoryCommandFactory.create_put_command(["sword", "leather", "bag", "5"])
    assert result.item == "sword"
    assert result.container == "leather bag"
    assert result.quantity == 5


def test_create_put_command_multi_word_container_no_quantity():
    """Test create_put_command() handles multi-word container without quantity."""
    result = InventoryCommandFactory.create_put_command(["sword", "leather", "bag"])
    assert result.item == "sword"
    assert result.container == "leather bag"
    assert result.quantity is None


def test_create_get_command_no_args():
    """Test create_get_command() raises error with no args."""
    with pytest.raises(ValidationError, match="Usage: get"):
        InventoryCommandFactory.create_get_command([])


def test_create_get_command_only_item_get_from_room():
    """Test create_get_command() with single arg returns get-from-room (container='room')."""
    result = InventoryCommandFactory.create_get_command(["sword"])
    assert result.item == "sword"
    assert result.container == "room"
    assert result.quantity is None


def test_create_get_command_with_from_keyword():
    """Test create_get_command() handles 'from' keyword."""
    result = InventoryCommandFactory.create_get_command(["sword", "from", "bag"])
    assert result.item == "sword"
    assert result.container == "bag"
    assert result.quantity is None


def test_create_get_command_quantity_zero():
    """Test create_get_command() raises error when quantity is zero."""
    with pytest.raises(ValidationError, match="Quantity must be a positive integer"):
        InventoryCommandFactory.create_get_command(["sword", "bag", "0"])


def test_create_get_command_quantity_negative():
    """Test create_get_command() raises error when quantity is negative."""
    with pytest.raises(ValidationError, match="Quantity must be a positive integer"):
        InventoryCommandFactory.create_get_command(["sword", "bag", "-1"])


def test_create_get_command_multi_word_container():
    """Test create_get_command() handles multi-word container."""
    result = InventoryCommandFactory.create_get_command(["sword", "leather", "bag", "5"])
    assert result.item == "sword"
    assert result.container == "leather bag"
    assert result.quantity == 5


def test_create_get_command_multi_word_container_no_quantity():
    """Test create_get_command() handles multi-word container without quantity."""
    result = InventoryCommandFactory.create_get_command(["sword", "leather", "bag"])
    assert result.item == "sword"
    assert result.container == "leather bag"
    assert result.quantity is None


def test_create_equip_command_index_zero():
    """Test create_equip_command() raises error when index is zero."""
    with pytest.raises(ValidationError, match="Inventory index must be a positive integer"):
        InventoryCommandFactory.create_equip_command(["0"])


def test_create_equip_command_index_negative():
    """Test create_equip_command() raises error when index is negative."""
    with pytest.raises(ValidationError, match="Inventory index must be a positive integer"):
        InventoryCommandFactory.create_equip_command(["-1"])


def test_create_equip_command_index_with_slot():
    """Test create_equip_command() handles index with slot."""
    result = InventoryCommandFactory.create_equip_command(["1", "head"])
    assert result.index == 1
    assert result.search_term is None
    assert result.target_slot == "head"


def test_create_equip_command_search_term_with_slot():
    """Test create_equip_command() handles search term with slot."""
    result = InventoryCommandFactory.create_equip_command(["sword", "main_hand"])
    assert result.index is None
    assert result.search_term == "sword"
    assert result.target_slot == "main_hand"


def test_create_equip_command_empty_search_term():
    """Test create_equip_command() raises error when search term is empty."""
    with pytest.raises(ValidationError, match="Equip item name cannot be empty"):
        InventoryCommandFactory.create_equip_command(["   "])


def test_create_equip_command_inferred_slot():
    """Test create_equip_command() infers slot from known slots."""
    result = InventoryCommandFactory.create_equip_command(["sword", "head"])
    assert result.index is None
    assert result.search_term == "sword"
    assert result.target_slot == "head"


def test_create_unequip_command_empty():
    """Test create_unequip_command() raises error with empty args."""
    with pytest.raises(ValidationError, match="Usage: unequip"):
        InventoryCommandFactory.create_unequip_command([])


def test_create_unequip_command_whitespace():
    """Test create_unequip_command() raises error with whitespace only."""
    with pytest.raises(ValidationError, match="Usage: unequip"):
        InventoryCommandFactory.create_unequip_command(["   "])


def test_create_unequip_command_known_slot():
    """Test create_unequip_command() handles known slot."""
    result = InventoryCommandFactory.create_unequip_command(["head"])
    assert result.slot == "head"
    assert result.search_term is None


def test_create_unequip_command_unknown_slot():
    """Test create_unequip_command() handles unknown slot as search term."""
    result = InventoryCommandFactory.create_unequip_command(["my_sword"])
    assert result.slot is None
    assert result.search_term == "my_sword"


def test_create_unequip_command_multi_word():
    """Test create_unequip_command() handles multi-word search term."""
    result = InventoryCommandFactory.create_unequip_command(["leather", "boots"])
    assert result.slot is None
    assert result.search_term == "leather boots"


def test_create_unequip_command_all_slots():
    """Test create_unequip_command() handles all known slots."""
    known_slots = [
        "head",
        "torso",
        "legs",
        "feet",
        "hands",
        "left_hand",
        "right_hand",
        "main_hand",
        "off_hand",
        "accessory",
        "ring",
        "amulet",
        "belt",
        "backpack",
        "waist",
        "neck",
    ]
    for slot in known_slots:
        result = InventoryCommandFactory.create_unequip_command([slot])
        assert result.slot == slot
        assert result.search_term is None
