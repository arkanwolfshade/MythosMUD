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
        _ = InventoryCommandFactory.create_get_command(["sword", "from", "bag", "0"])


def test_create_get_command_quantity_negative():
    """Test create_get_command() raises error when quantity is negative."""
    with pytest.raises(ValidationError, match="Quantity must be a positive integer"):
        _ = InventoryCommandFactory.create_get_command(["sword", "from", "bag", "-1"])


def test_create_get_command_multi_word_container():
    """Test create_get_command() handles multi-word container."""
    result = InventoryCommandFactory.create_get_command(["sword", "from", "leather", "bag", "5"])
    assert result.item == "sword"
    assert result.container == "leather bag"
    assert result.quantity == 5


def test_create_get_command_multi_word_container_no_quantity():
    """Test create_get_command() handles multi-word container without quantity."""
    result = InventoryCommandFactory.create_get_command(["sword", "from", "leather", "bag"])
    assert result.item == "sword"
    assert result.container == "leather bag"
    assert result.quantity is None


def test_create_get_command_multi_word_item_from_room():
    """`get folk tonic` names one item on the floor, not item "folk" in container "tonic" (#982)."""
    result = InventoryCommandFactory.create_get_command(["folk", "tonic"])
    assert result.item == "folk tonic"
    assert result.container == "room"
    assert result.quantity is None


def test_create_get_command_multi_word_item_and_container_with_quantity():
    """`from` separates a multi-word item from a multi-word container (#982)."""
    result = InventoryCommandFactory.create_get_command(["folk", "tonic", "from", "old", "chest", "2"])
    assert result.item == "folk tonic"
    assert result.container == "old chest"
    assert result.quantity == 2


def test_create_get_command_quantity_from_room():
    """`get daisy 3` takes three daisies from the floor, not from a container named "3"."""
    result = InventoryCommandFactory.create_get_command(["daisy", "3"])
    assert result.item == "daisy"
    assert result.container == "room"
    assert result.quantity == 3


def test_create_get_command_splits_on_last_from():
    """An item name containing "from" still parses when the container follows the last "from"."""
    result = InventoryCommandFactory.create_get_command(["letter", "from", "arkham", "FROM", "chest"])
    assert result.item == "letter from arkham"
    assert result.container == "chest"


def test_create_get_command_explicit_room_sentinel():
    """`get daisy from room 3` still routes to the floor."""
    result = InventoryCommandFactory.create_get_command(["daisy", "from", "room", "3"])
    assert result.item == "daisy"
    assert result.container == "room"
    assert result.quantity == 3


def test_create_get_command_single_numeric_selector():
    """A lone number is an index selector, not a quantity."""
    result = InventoryCommandFactory.create_get_command(["2"])
    assert result.item == "2"
    assert result.container == "room"
    assert result.quantity is None


@pytest.mark.parametrize("args", [["from", "chest"], ["sling", "from"], ["from"]])
def test_create_get_command_separator_needs_both_sides(args: list[str]) -> None:
    """A separator with nothing on one side is a usage error."""
    with pytest.raises(ValidationError, match="Usage: get"):
        _ = InventoryCommandFactory.create_get_command(args)


def test_create_put_command_multi_word_item():
    """`put folk tonic into chest` keeps the whole item name (#982)."""
    result = InventoryCommandFactory.create_put_command(["folk", "tonic", "into", "chest"])
    assert result.item == "folk tonic"
    assert result.container == "chest"
    assert result.quantity is None


def test_create_put_command_multi_word_item_with_quantity():
    """Quantity after a multi-word container is still parsed."""
    result = InventoryCommandFactory.create_put_command(["folk", "tonic", "in", "old", "chest", "2"])
    assert result.item == "folk tonic"
    assert result.container == "old chest"
    assert result.quantity == 2


@pytest.mark.parametrize("args", [["into", "chest"], ["sling", "into"]])
def test_create_put_command_separator_needs_both_sides(args: list[str]) -> None:
    """A separator with nothing on one side is a usage error."""
    with pytest.raises(ValidationError, match="Usage: put"):
        _ = InventoryCommandFactory.create_put_command(args)


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


# --- Tests for create_read_command (#813) ---


def test_create_read_command_no_args():
    """Test create_read_command() creates a bare ReadCommand with no args."""
    command = InventoryCommandFactory.create_read_command([])
    assert command.command_type == "read"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime


def test_create_read_command_with_args():
    """Test create_read_command() ignores args at the model level (handler parses command_data['args'])."""
    command = InventoryCommandFactory.create_read_command(["spellbook", "fireball"])
    assert command.command_type == "read"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime


@pytest.mark.parametrize("preposition", ["in", "into", "INTO"])
def test_create_put_command_ignores_in_and_into(preposition: str) -> None:
    """`put sling into chest` names the chest, not a container called "into chest"."""
    command = InventoryCommandFactory.create_put_command(["sling", preposition, "chest"])

    assert command.item == "sling"
    assert command.container == "chest"


def test_create_use_command_by_index():
    """Test create_use_command() treats a number as a 1-based inventory index."""
    command = InventoryCommandFactory.create_use_command(["2"])
    assert command.index == 2
    assert command.search_term is None


def test_create_use_command_by_multi_word_name():
    """Test create_use_command() joins the arguments into a name search."""
    command = InventoryCommandFactory.create_use_command(["folk", "tonic"])
    assert command.index is None
    assert command.search_term == "folk tonic"


@pytest.mark.parametrize("args", [[], ["   "], ["0"]])
def test_create_use_command_rejects_missing_or_zero_selector(args: list[str]) -> None:
    """Test create_use_command() needs a name or a positive number."""
    with pytest.raises(ValidationError):
        _ = InventoryCommandFactory.create_use_command(args)
