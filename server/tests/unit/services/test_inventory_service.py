"""
Unit tests for inventory service.

Tests the InventoryService class for inventory management operations.
"""

import uuid

import pytest

from server.services.inventory_service import (
    InventoryCapacityError,
    InventoryService,
    InventorySplitError,
    InventoryValidationError,
)


@pytest.fixture
def inventory_service():
    """Create an InventoryService instance."""
    return InventoryService(max_slots=20)


def test_add_stack_new_item(inventory_service):
    """Test add_stack adds new item to inventory."""
    inventory = []
    new_stack = {
        "item_instance_id": "inst1",
        "item_id": "item1",
        "prototype_id": "proto1",
        "item_name": "sword",
        "slot_type": "weapon",
        "quantity": 1,
    }
    
    result = inventory_service.add_stack(inventory, new_stack)
    
    assert len(result) == 1
    assert result[0]["item_name"] == "sword"


def test_add_stack_merges_existing(inventory_service):
    """Test add_stack merges with existing stack."""
    inventory = [
        {
            "item_instance_id": "inst1",
            "item_id": "item1",
            "prototype_id": "proto1",
            "item_name": "potion",
            "slot_type": "consumable",
            "quantity": 3,
        }
    ]
    new_stack = {
        "item_instance_id": "inst1",
        "item_id": "item1",
        "prototype_id": "proto1",
        "item_name": "potion",
        "slot_type": "consumable",
        "quantity": 2,
    }
    
    result = inventory_service.add_stack(inventory, new_stack)
    
    assert len(result) == 1
    assert result[0]["quantity"] == 5


def test_add_stack_capacity_error(inventory_service):
    """Test add_stack raises InventoryCapacityError when at capacity."""
    # Create inventory at capacity
    inventory = [
        {
            "item_instance_id": f"inst{i}",
            "item_id": f"item{i}",
            "prototype_id": f"proto{i}",
            "item_name": f"item{i}",
            "slot_type": "inventory",
            "quantity": 1,
        }
        for i in range(20)
    ]
    new_stack = {
        "item_instance_id": "inst_new",
        "item_id": "item_new",
        "prototype_id": "proto_new",
        "item_name": "new_item",
        "slot_type": "inventory",
        "quantity": 1,
    }
    
    with pytest.raises(InventoryCapacityError, match="cannot exceed"):
        inventory_service.add_stack(inventory, new_stack)


def test_add_stack_validation_error_missing_field(inventory_service):
    """Test add_stack raises InventoryValidationError for missing fields."""
    inventory = []
    new_stack = {
        "item_name": "sword",
        # Missing required fields
    }
    
    with pytest.raises(InventoryValidationError, match="Missing required"):
        inventory_service.add_stack(inventory, new_stack)


def test_add_stack_validation_error_invalid_quantity(inventory_service):
    """Test add_stack raises InventoryValidationError for invalid quantity."""
    inventory = []
    new_stack = {
        "item_instance_id": "inst1",
        "item_id": "item1",
        "prototype_id": "proto1",
        "item_name": "sword",
        "slot_type": "weapon",
        "quantity": 0,  # Invalid quantity
    }
    
    with pytest.raises(InventoryValidationError, match="positive integer"):
        inventory_service.add_stack(inventory, new_stack)


def test_split_stack_success(inventory_service):
    """Test split_stack successfully splits a stack."""
    inventory = [
        {
            "item_instance_id": "inst1",
            "item_id": "item1",
            "prototype_id": "proto1",
            "item_name": "potion",
            "slot_type": "consumable",
            "quantity": 10,
        }
    ]
    
    result = inventory_service.split_stack(inventory, slot_index=0, split_quantity=3)
    
    assert len(result) == 2
    assert result[0]["quantity"] == 7
    assert result[1]["quantity"] == 3
    assert result[1]["item_name"] == "potion"


def test_split_stack_invalid_index(inventory_service):
    """Test split_stack with invalid slot index."""
    inventory = [{"item_name": "potion", "quantity": 10}]
    
    with pytest.raises(InventorySplitError, match="outside"):
        inventory_service.split_stack(inventory, slot_index=10, split_quantity=3)


def test_split_stack_invalid_quantity_zero(inventory_service):
    """Test split_stack with zero quantity."""
    inventory = [
        {
            "item_instance_id": "inst1",
            "item_id": "item1",
            "prototype_id": "proto1",
            "item_name": "potion",
            "slot_type": "consumable",
            "quantity": 10,
        }
    ]
    
    with pytest.raises(InventorySplitError, match="positive integer"):
        inventory_service.split_stack(inventory, slot_index=0, split_quantity=0)


def test_split_stack_invalid_quantity_negative(inventory_service):
    """Test split_stack with negative quantity."""
    inventory = [
        {
            "item_instance_id": "inst1",
            "item_id": "item1",
            "prototype_id": "proto1",
            "item_name": "potion",
            "slot_type": "consumable",
            "quantity": 10,
        }
    ]
    
    with pytest.raises(InventorySplitError, match="positive integer"):
        inventory_service.split_stack(inventory, slot_index=0, split_quantity=-1)


def test_split_stack_quantity_too_large(inventory_service):
    """Test split_stack with quantity >= stack size."""
    inventory = [
        {
            "item_instance_id": "inst1",
            "item_id": "item1",
            "prototype_id": "proto1",
            "item_name": "potion",
            "slot_type": "consumable",
            "quantity": 10,
        }
    ]
    
    with pytest.raises(InventorySplitError, match="less than"):
        inventory_service.split_stack(inventory, slot_index=0, split_quantity=10)


def test_split_stack_capacity_error(inventory_service):
    """Test split_stack raises InventoryCapacityError when at capacity."""
    # Create inventory at capacity
    inventory = [
        {
            "item_instance_id": f"inst{i}",
            "item_id": f"item{i}",
            "prototype_id": f"proto{i}",
            "item_name": f"item{i}",
            "slot_type": "inventory",
            "quantity": 1,
        }
        for i in range(20)
    ]
    
    with pytest.raises(InventoryCapacityError, match="already occupies"):
        inventory_service.split_stack(inventory, slot_index=0, split_quantity=1)


def test_begin_mutation_success(inventory_service):
    """Test begin_mutation returns context manager."""
    player_id = uuid.uuid4()
    
    context = inventory_service.begin_mutation(player_id, "token123")
    
    assert context is not None
    # Test that it can be used as context manager
    with context as decision:
        assert hasattr(decision, "should_apply")


def test_begin_mutation_with_string_id(inventory_service):
    """Test begin_mutation accepts string player_id."""
    player_id = "player123"
    
    context = inventory_service.begin_mutation(player_id, "token123")
    
    assert context is not None
    with context as decision:
        assert hasattr(decision, "should_apply")
