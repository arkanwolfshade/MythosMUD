"""
Unit tests for inventory command factories.

Tests factory methods for inventory and item management commands.
"""

import pytest

from server.exceptions import ValidationError as MythosValidationError
from server.utils.command_factories_inventory import InventoryCommandFactory


def test_create_inventory_command_no_args():
    """Test create_inventory_command with no arguments."""
    result = InventoryCommandFactory.create_inventory_command([])
    
    assert result is not None
    assert hasattr(result, "command_type")


def test_create_inventory_command_with_args():
    """Test create_inventory_command raises error with arguments."""
    with pytest.raises(MythosValidationError, match="takes no arguments"):
        InventoryCommandFactory.create_inventory_command(["extra"])


def test_create_pickup_command_no_args():
    """Test create_pickup_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="Usage"):
        InventoryCommandFactory.create_pickup_command([])


def test_create_pickup_command_with_index():
    """Test create_pickup_command with numeric index."""
    result = InventoryCommandFactory.create_pickup_command(["1"])
    
    assert result.index == 1
    assert result.search_term is None
    assert result.quantity is None


def test_create_pickup_command_with_index_and_quantity():
    """Test create_pickup_command with index and quantity."""
    result = InventoryCommandFactory.create_pickup_command(["1", "5"])
    
    assert result.index == 1
    assert result.quantity == 5


def test_create_pickup_command_with_search_term():
    """Test create_pickup_command with search term."""
    result = InventoryCommandFactory.create_pickup_command(["sword"])
    
    assert result.index is None
    assert result.search_term == "sword"
    assert result.quantity is None


def test_create_pickup_command_with_search_term_and_quantity():
    """Test create_pickup_command with search term and quantity."""
    result = InventoryCommandFactory.create_pickup_command(["iron sword", "3"])
    
    assert result.index is None
    assert result.search_term == "iron sword"
    assert result.quantity == 3


def test_create_pickup_command_negative_index():
    """Test create_pickup_command raises error with negative index."""
    with pytest.raises(MythosValidationError, match="positive integer"):
        InventoryCommandFactory.create_pickup_command(["-1"])


def test_create_pickup_command_zero_index():
    """Test create_pickup_command raises error with zero index."""
    with pytest.raises(MythosValidationError, match="positive integer"):
        InventoryCommandFactory.create_pickup_command(["0"])


def test_create_pickup_command_negative_quantity():
    """Test create_pickup_command raises error with negative quantity."""
    with pytest.raises(MythosValidationError, match="positive integer"):
        InventoryCommandFactory.create_pickup_command(["sword", "-1"])


def test_create_pickup_command_zero_quantity():
    """Test create_pickup_command raises error with zero quantity."""
    with pytest.raises(MythosValidationError, match="positive integer"):
        InventoryCommandFactory.create_pickup_command(["sword", "0"])


def test_create_pickup_command_index_with_extra_args():
    """Test create_pickup_command raises error when index has extra args."""
    with pytest.raises(MythosValidationError, match="Usage"):
        InventoryCommandFactory.create_pickup_command(["1", "extra"])


def test_create_pickup_command_empty_search_term():
    """Test create_pickup_command raises error with empty search term."""
    with pytest.raises(MythosValidationError, match="cannot be empty"):
        InventoryCommandFactory.create_pickup_command(["", "5"])


def test_create_drop_command_no_args():
    """Test create_drop_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="Usage"):
        InventoryCommandFactory.create_drop_command([])


def test_create_drop_command_with_index():
    """Test create_drop_command with index."""
    result = InventoryCommandFactory.create_drop_command(["1"])
    
    assert result.index == 1
    assert result.quantity is None


def test_create_drop_command_with_index_and_quantity():
    """Test create_drop_command with index and quantity."""
    result = InventoryCommandFactory.create_drop_command(["1", "5"])
    
    assert result.index == 1
    assert result.quantity == 5


def test_create_drop_command_invalid_index():
    """Test create_drop_command raises error with invalid index."""
    with pytest.raises(MythosValidationError, match="must be an integer"):
        InventoryCommandFactory.create_drop_command(["invalid"])


def test_create_drop_command_invalid_quantity():
    """Test create_drop_command raises error with invalid quantity."""
    with pytest.raises(MythosValidationError, match="must be an integer"):
        InventoryCommandFactory.create_drop_command(["1", "invalid"])


def test_create_put_command_no_args():
    """Test create_put_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="Usage"):
        InventoryCommandFactory.create_put_command([])


def test_create_put_command_basic():
    """Test create_put_command with item and container."""
    result = InventoryCommandFactory.create_put_command(["sword", "backpack"])
    
    assert result.item == "sword"
    assert result.container == "backpack"
    assert result.quantity is None


def test_create_put_command_with_in_keyword():
    """Test create_put_command handles optional 'in' keyword."""
    result = InventoryCommandFactory.create_put_command(["sword", "in", "backpack"])
    
    assert result.item == "sword"
    assert result.container == "backpack"


def test_create_put_command_with_quantity():
    """Test create_put_command with quantity."""
    result = InventoryCommandFactory.create_put_command(["sword", "backpack", "5"])
    
    assert result.item == "sword"
    assert result.container == "backpack"
    assert result.quantity == 5


def test_create_put_command_with_in_and_quantity():
    """Test create_put_command with 'in' keyword and quantity."""
    result = InventoryCommandFactory.create_put_command(["sword", "in", "backpack", "5"])
    
    assert result.item == "sword"
    assert result.container == "backpack"
    assert result.quantity == 5


def test_create_put_command_multi_word_container():
    """Test create_put_command with multi-word container."""
    result = InventoryCommandFactory.create_put_command(["sword", "leather backpack", "5"])
    
    assert result.item == "sword"
    assert result.container == "leather backpack"
    assert result.quantity == 5


def test_create_put_command_negative_quantity():
    """Test create_put_command raises error with negative quantity."""
    with pytest.raises(MythosValidationError, match="positive integer"):
        InventoryCommandFactory.create_put_command(["sword", "backpack", "-1"])


def test_create_put_command_zero_quantity():
    """Test create_put_command raises error with zero quantity."""
    with pytest.raises(MythosValidationError, match="positive integer"):
        InventoryCommandFactory.create_put_command(["sword", "backpack", "0"])


def test_create_get_command_no_args():
    """Test create_get_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="Usage"):
        InventoryCommandFactory.create_get_command([])


def test_create_get_command_basic():
    """Test create_get_command with item and container."""
    result = InventoryCommandFactory.create_get_command(["sword", "backpack"])
    
    assert result.item == "sword"
    assert result.container == "backpack"
    assert result.quantity is None


def test_create_get_command_with_from_keyword():
    """Test create_get_command handles optional 'from' keyword."""
    result = InventoryCommandFactory.create_get_command(["sword", "from", "backpack"])
    
    assert result.item == "sword"
    assert result.container == "backpack"


def test_create_get_command_with_quantity():
    """Test create_get_command with quantity."""
    result = InventoryCommandFactory.create_get_command(["sword", "backpack", "5"])
    
    assert result.item == "sword"
    assert result.container == "backpack"
    assert result.quantity == 5


def test_create_get_command_with_from_and_quantity():
    """Test create_get_command with 'from' keyword and quantity."""
    result = InventoryCommandFactory.create_get_command(["sword", "from", "backpack", "5"])
    
    assert result.item == "sword"
    assert result.container == "backpack"
    assert result.quantity == 5


def test_create_get_command_multi_word_container():
    """Test create_get_command with multi-word container."""
    result = InventoryCommandFactory.create_get_command(["sword", "leather backpack", "5"])
    
    assert result.item == "sword"
    assert result.container == "leather backpack"
    assert result.quantity == 5


def test_create_get_command_negative_quantity():
    """Test create_get_command raises error with negative quantity."""
    with pytest.raises(MythosValidationError, match="positive integer"):
        InventoryCommandFactory.create_get_command(["sword", "backpack", "-1"])


def test_create_get_command_zero_quantity():
    """Test create_get_command raises error with zero quantity."""
    with pytest.raises(MythosValidationError, match="positive integer"):
        InventoryCommandFactory.create_get_command(["sword", "backpack", "0"])


def test_create_equip_command_no_args():
    """Test create_equip_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="Usage"):
        InventoryCommandFactory.create_equip_command([])


def test_create_equip_command_with_index():
    """Test create_equip_command with numeric index."""
    result = InventoryCommandFactory.create_equip_command(["1"])
    
    assert result.index == 1
    assert result.search_term is None
    assert result.target_slot is None


def test_create_equip_command_with_index_and_slot():
    """Test create_equip_command with index and slot."""
    result = InventoryCommandFactory.create_equip_command(["1", "head"])
    
    assert result.index == 1
    assert result.target_slot == "head"


def test_create_equip_command_with_search_term():
    """Test create_equip_command with search term."""
    result = InventoryCommandFactory.create_equip_command(["sword"])
    
    assert result.index is None
    assert result.search_term == "sword"
    assert result.target_slot is None


def test_create_equip_command_with_search_term_and_slot():
    """Test create_equip_command with search term and inferred slot."""
    result = InventoryCommandFactory.create_equip_command(["sword", "main_hand"])
    
    assert result.index is None
    assert result.search_term == "sword"
    assert result.target_slot == "main_hand"


def test_create_equip_command_negative_index():
    """Test create_equip_command raises error with negative index."""
    with pytest.raises(MythosValidationError, match="positive integer"):
        InventoryCommandFactory.create_equip_command(["-1"])


def test_create_equip_command_zero_index():
    """Test create_equip_command raises error with zero index."""
    with pytest.raises(MythosValidationError, match="positive integer"):
        InventoryCommandFactory.create_equip_command(["0"])


def test_create_equip_command_empty_search_term():
    """Test create_equip_command raises error with empty search term."""
    with pytest.raises(MythosValidationError, match="cannot be empty"):
        InventoryCommandFactory.create_equip_command([""])


def test_create_equip_command_all_slots():
    """Test create_equip_command recognizes all valid slots."""
    valid_slots = ["head", "torso", "legs", "feet", "hands", "left_hand", "right_hand", 
                   "main_hand", "off_hand", "accessory", "ring", "amulet", "belt", 
                   "backpack", "waist", "neck"]
    
    for slot in valid_slots:
        result = InventoryCommandFactory.create_equip_command(["sword", slot])
        assert result.target_slot == slot


def test_create_unequip_command_no_args():
    """Test create_unequip_command raises error with no arguments."""
    with pytest.raises(MythosValidationError, match="Usage"):
        InventoryCommandFactory.create_unequip_command([])


def test_create_unequip_command_with_slot():
    """Test create_unequip_command with slot name."""
    result = InventoryCommandFactory.create_unequip_command(["head"])
    
    assert result.slot == "head"
    assert result.search_term is None


def test_create_unequip_command_with_search_term():
    """Test create_unequip_command with item search term."""
    result = InventoryCommandFactory.create_unequip_command(["iron sword"])
    
    assert result.slot is None
    assert result.search_term == "iron sword"


def test_create_unequip_command_empty_string():
    """Test create_unequip_command raises error with empty string."""
    with pytest.raises(MythosValidationError, match="Usage"):
        InventoryCommandFactory.create_unequip_command(["   "])


def test_create_unequip_command_all_slots():
    """Test create_unequip_command recognizes all valid slots."""
    valid_slots = ["head", "torso", "legs", "feet", "hands", "left_hand", "right_hand", 
                   "main_hand", "off_hand", "accessory", "ring", "amulet", "belt", 
                   "backpack", "waist", "neck"]
    
    for slot in valid_slots:
        result = InventoryCommandFactory.create_unequip_command([slot])
        assert result.slot == slot
        assert result.search_term is None
