"""
Unit tests for inventory command models.

Tests the inventory command models and their validators.
"""

import pytest
from pydantic import ValidationError

from server.models.command_inventory import (
    DropCommand,
    EquipCommand,
    GetCommand,
    InventoryCommand,
    PickupCommand,
    PutCommand,
    UnequipCommand,
)

# --- Tests for InventoryCommand ---


def test_inventory_command_no_fields():
    """Test InventoryCommand has no required fields."""
    command = InventoryCommand()

    # Reason: Enum values (str enums) are comparable to strings at runtime
    assert command.command_type == "inventory"  # type: ignore[comparison-overlap]


# --- Tests for PickupCommand ---


def test_pickup_command_with_index():
    """Test PickupCommand can be created with index."""
    command = PickupCommand(index=1)

    # Reason: Testing str enum direct comparison - valid at runtime for str enums, but mypy sees as non-overlapping
    assert command.command_type == "pickup"  # type: ignore[comparison-overlap]
    # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
    assert command.index == 1  # type: ignore[unreachable]
    assert command.search_term is None
    assert command.quantity is None


def test_pickup_command_with_search_term():
    """Test PickupCommand can be created with search_term."""
    command = PickupCommand(search_term="sword")

    assert command.search_term == "sword"
    assert command.index is None


def test_pickup_command_with_both():
    """Test PickupCommand can be created with both index and search_term."""
    command = PickupCommand(index=1, search_term="sword")

    assert command.index == 1
    assert command.search_term == "sword"


def test_pickup_command_validate_search_term_strips():
    """Test PickupCommand strips whitespace from search_term."""
    command = PickupCommand(search_term="  sword  ")

    assert command.search_term == "sword"


def test_pickup_command_validate_search_term_empty_string():
    """Test PickupCommand cannot accept empty search_term (fails min_length before validator)."""
    # Empty string fails min_length=1 validation before validator runs
    with pytest.raises(ValidationError):
        PickupCommand(index=1, search_term="")


def test_pickup_command_validate_search_term_whitespace_only():
    """Test PickupCommand converts whitespace-only search_term to None."""
    command = PickupCommand(index=1, search_term="   ")

    assert command.search_term is None


def test_pickup_command_validate_search_term_none():
    """Test PickupCommand accepts None for search_term."""
    command = PickupCommand(index=1, search_term=None)

    assert command.search_term is None


def test_pickup_command_validate_requirements_neither_provided():
    """Test PickupCommand requires either index or search_term."""
    with pytest.raises(ValidationError) as exc_info:
        PickupCommand()

    error_str = str(exc_info.value).lower()
    assert "item number" in error_str or "name" in error_str or "validation" in error_str


def test_pickup_command_validate_requirements_index_provided():
    """Test PickupCommand accepts index alone."""
    command = PickupCommand(index=1)

    assert command.index == 1


def test_pickup_command_validate_requirements_search_term_provided():
    """Test PickupCommand accepts search_term alone."""
    command = PickupCommand(search_term="sword")

    assert command.search_term == "sword"


def test_pickup_command_index_validation_min():
    """Test PickupCommand validates index is >= 1."""
    with pytest.raises(ValidationError):
        PickupCommand(index=0)  # Below minimum


def test_pickup_command_quantity_validation_min():
    """Test PickupCommand validates quantity is >= 1."""
    with pytest.raises(ValidationError):
        PickupCommand(index=1, quantity=0)  # Below minimum


def test_pickup_command_search_term_max_length():
    """Test PickupCommand validates search_term max length."""
    long_term = "a" * 121  # Exceeds max_length=120
    with pytest.raises(ValidationError):
        PickupCommand(search_term=long_term)


# --- Tests for DropCommand ---


def test_drop_command_required_fields():
    """Test DropCommand requires index."""
    command = DropCommand(index=1)

    # Reason: Enum values (str enums) are comparable to strings at runtime
    assert command.command_type == "drop"  # type: ignore[comparison-overlap]
    # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
    assert command.index == 1  # type: ignore[unreachable]
    assert command.quantity is None


def test_drop_command_with_quantity():
    """Test DropCommand can have optional quantity."""
    command = DropCommand(index=1, quantity=5)

    assert command.index == 1
    assert command.quantity == 5


def test_drop_command_index_validation_min():
    """Test DropCommand validates index is >= 1."""
    with pytest.raises(ValidationError):
        DropCommand(index=0)  # Below minimum


def test_drop_command_quantity_validation_min():
    """Test DropCommand validates quantity is >= 1."""
    with pytest.raises(ValidationError):
        DropCommand(index=1, quantity=0)  # Below minimum


def test_drop_command_missing_index():
    """Test DropCommand requires index."""
    with pytest.raises(ValidationError):
        # Reason: Intentionally testing Pydantic validation with missing required field
        DropCommand()  # type: ignore[call-arg]  # Missing required index


# --- Tests for PutCommand ---


def test_put_command_required_fields():
    """Test PutCommand requires item and container."""
    command = PutCommand(item="sword", container="backpack")

    # Reason: Testing str enum direct comparison - valid at runtime for str enums, but mypy sees as non-overlapping
    assert command.command_type == "put"  # type: ignore[comparison-overlap]
    # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
    assert command.item == "sword"  # type: ignore[unreachable]
    assert command.container == "backpack"
    assert command.quantity is None


def test_put_command_with_quantity():
    """Test PutCommand can have optional quantity."""
    command = PutCommand(item="sword", container="backpack", quantity=3)

    assert command.quantity == 3


def test_put_command_item_min_length():
    """Test PutCommand validates item min length."""
    with pytest.raises(ValidationError):
        PutCommand(item="", container="backpack")  # Empty string


def test_put_command_container_min_length():
    """Test PutCommand validates container min length."""
    with pytest.raises(ValidationError):
        PutCommand(item="sword", container="")  # Empty string


def test_put_command_quantity_validation_min():
    """Test PutCommand validates quantity is >= 1."""
    with pytest.raises(ValidationError):
        PutCommand(item="sword", container="backpack", quantity=0)  # Below minimum


# --- Tests for GetCommand ---


def test_get_command_required_fields():
    """Test GetCommand requires item and container."""
    command = GetCommand(item="sword", container="backpack")

    # Reason: Enum values (str enums) are comparable to strings at runtime
    assert command.command_type == "get"  # type: ignore[comparison-overlap]
    # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
    assert command.item == "sword"  # type: ignore[unreachable]
    assert command.container == "backpack"
    assert command.quantity is None


def test_get_command_with_quantity():
    """Test GetCommand can have optional quantity."""
    command = GetCommand(item="sword", container="backpack", quantity=2)

    assert command.quantity == 2


def test_get_command_item_min_length():
    """Test GetCommand validates item min length."""
    with pytest.raises(ValidationError):
        GetCommand(item="", container="backpack")  # Empty string


def test_get_command_container_min_length():
    """Test GetCommand validates container min length."""
    with pytest.raises(ValidationError):
        GetCommand(item="sword", container="")  # Empty string


def test_get_command_quantity_validation_min():
    """Test GetCommand validates quantity is >= 1."""
    with pytest.raises(ValidationError):
        GetCommand(item="sword", container="backpack", quantity=0)  # Below minimum


# --- Tests for EquipCommand ---


def test_equip_command_with_index():
    """Test EquipCommand can be created with index."""
    command = EquipCommand(index=1)

    assert command.command_type == "equip"  # type: ignore[comparison-overlap]  # Testing str enum comparison - valid at runtime
    # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
    assert command.index == 1  # type: ignore[unreachable]
    assert command.search_term is None
    assert command.target_slot is None


def test_equip_command_with_search_term():
    """Test EquipCommand can be created with search_term."""
    command = EquipCommand(search_term="sword")

    assert command.search_term == "sword"
    assert command.index is None


def test_equip_command_with_target_slot():
    """Test EquipCommand can have optional target_slot."""
    command = EquipCommand(index=1, target_slot="hand")

    assert command.target_slot == "hand"


def test_equip_command_validate_search_term_strips():
    """Test EquipCommand strips whitespace from search_term."""
    command = EquipCommand(search_term="  sword  ")

    assert command.search_term == "sword"


def test_equip_command_validate_search_term_empty_string():
    """Test EquipCommand cannot accept empty search_term (fails min_length before validator)."""
    # Empty string fails min_length=1 validation before validator runs
    with pytest.raises(ValidationError):
        EquipCommand(index=1, search_term="")


def test_equip_command_validate_search_term_whitespace_only():
    """Test EquipCommand converts whitespace-only search_term to None."""
    command = EquipCommand(index=1, search_term="   ")

    assert command.search_term is None


def test_equip_command_validate_requirements_neither_provided():
    """Test EquipCommand requires either index or search_term."""
    with pytest.raises(ValidationError) as exc_info:
        EquipCommand()

    error_str = str(exc_info.value).lower()
    assert "index" in error_str or "search_term" in error_str or "validation" in error_str


def test_equip_command_validate_slot_strips():
    """Test EquipCommand strips whitespace from target_slot."""
    command = EquipCommand(index=1, target_slot="  hand  ")

    assert command.target_slot == "hand"


def test_equip_command_validate_slot_empty_string():
    """Test EquipCommand rejects empty target_slot (validator raises ValueError)."""
    # Empty string gets normalized and validator raises ValueError
    with pytest.raises(ValidationError) as exc_info:
        EquipCommand(index=1, target_slot="")

    error_str = str(exc_info.value).lower()
    assert "slot cannot be empty" in error_str or "validation" in error_str


def test_equip_command_validate_slot_whitespace_only():
    """Test EquipCommand rejects whitespace-only target_slot (validator raises ValueError)."""
    # Whitespace-only gets normalized to empty and validator raises ValueError
    with pytest.raises(ValidationError) as exc_info:
        EquipCommand(index=1, target_slot="   ")

    error_str = str(exc_info.value).lower()
    assert "slot cannot be empty" in error_str or "validation" in error_str


def test_equip_command_index_validation_min():
    """Test EquipCommand validates index is >= 1."""
    with pytest.raises(ValidationError):
        EquipCommand(index=0)  # Below minimum


def test_equip_command_search_term_max_length():
    """Test EquipCommand validates search_term max length."""
    long_term = "a" * 121  # Exceeds max_length=120
    with pytest.raises(ValidationError):
        EquipCommand(search_term=long_term)


def test_equip_command_target_slot_max_length():
    """Test EquipCommand validates target_slot max length."""
    long_slot = "a" * 31  # Exceeds max_length=30
    with pytest.raises(ValidationError):
        EquipCommand(index=1, target_slot=long_slot)


# --- Tests for UnequipCommand ---


def test_unequip_command_with_slot():
    """Test UnequipCommand can be created with slot."""
    command = UnequipCommand(slot="hand")

    # Reason: Enum values (str enums) are comparable to strings at runtime
    assert command.command_type == "unequip"  # type: ignore[comparison-overlap]
    # Reason: Testing field assignment - mypy may see as unreachable but validates at runtime
    assert command.slot == "hand"  # type: ignore[unreachable]
    assert command.search_term is None


def test_unequip_command_with_search_term():
    """Test UnequipCommand can be created with search_term."""
    command = UnequipCommand(search_term="sword")

    assert command.search_term == "sword"
    assert command.slot is None


def test_unequip_command_with_both():
    """Test UnequipCommand can be created with both slot and search_term."""
    command = UnequipCommand(slot="hand", search_term="sword")

    assert command.slot == "hand"
    assert command.search_term == "sword"


def test_unequip_command_validate_slot_strips():
    """Test UnequipCommand strips whitespace from slot."""
    command = UnequipCommand(slot="  hand  ")

    assert command.slot == "hand"


def test_unequip_command_validate_slot_empty_string():
    """Test UnequipCommand cannot accept empty slot (fails min_length before validator)."""
    # Empty string fails min_length=1 validation before validator runs
    with pytest.raises(ValidationError):
        UnequipCommand(search_term="sword", slot="")


def test_unequip_command_validate_slot_whitespace_only():
    """Test UnequipCommand converts whitespace-only slot to None."""
    command = UnequipCommand(search_term="sword", slot="   ")

    assert command.slot is None


def test_unequip_command_validate_search_term_strips():
    """Test UnequipCommand strips whitespace from search_term."""
    command = UnequipCommand(search_term="  sword  ")

    assert command.search_term == "sword"


def test_unequip_command_validate_search_term_empty_string():
    """Test UnequipCommand cannot accept empty search_term (fails min_length before validator)."""
    # Empty string fails min_length=1 validation before validator runs
    with pytest.raises(ValidationError):
        UnequipCommand(slot="hand", search_term="")


def test_unequip_command_validate_search_term_whitespace_only():
    """Test UnequipCommand converts whitespace-only search_term to None."""
    command = UnequipCommand(slot="hand", search_term="   ")

    assert command.search_term is None


def test_unequip_command_validate_requirements_neither_provided():
    """Test UnequipCommand requires either slot or search_term."""
    with pytest.raises(ValidationError) as exc_info:
        UnequipCommand()

    error_str = str(exc_info.value).lower()
    assert "slot" in error_str or "search_term" in error_str or "validation" in error_str


def test_unequip_command_validate_requirements_slot_provided():
    """Test UnequipCommand accepts slot alone."""
    command = UnequipCommand(slot="hand")

    assert command.slot == "hand"


def test_unequip_command_validate_requirements_search_term_provided():
    """Test UnequipCommand accepts search_term alone."""
    command = UnequipCommand(search_term="sword")

    assert command.search_term == "sword"
