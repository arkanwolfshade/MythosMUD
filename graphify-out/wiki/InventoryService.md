# InventoryService

> 50 nodes

## Key Concepts

- **InventoryService** (37 connections) — `server/services/inventory_service.py`
- **test_inventory_service.py** (21 connections) — `server/tests/unit/services/test_inventory_service.py`
- **InventorySplitError** (11 connections) — `server/services/inventory_service.py`
- **InventoryValidationError** (10 connections) — `server/services/inventory_service.py`
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- **Any** (7 connections)
- **._validate_and_clone_optional_fields()** (6 connections) — `server/services/inventory_service.py`
- **._can_merge()** (4 connections) — `server/services/inventory_service.py`
- **._extract_required_fields()** (4 connections) — `server/services/inventory_service.py`
- **._normalize_metadata()** (4 connections) — `server/services/inventory_service.py`
- **inventory_service()** (4 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_capacity_error()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_validation_error_invalid_quantity()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_validation_error_missing_field()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_capacity_error()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_invalid_index()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_invalid_quantity_negative()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_invalid_quantity_zero()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_quantity_too_large()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_merges_existing()** (2 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_new_item()** (2 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_begin_mutation_success()** (2 connections) — `server/tests/unit/services/test_inventory_service.py`
- *... and 25 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (24 shared connections)
- [inventory_unequip_command.py](inventory_unequip_command.py.md) (8 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (5 shared connections)
- [command_result_text](command_result_text.md) (3 shared connections)
- [ContainerService](ContainerService.md) (2 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (1 shared connections)
- [.begin_mutation](begin_mutation.md) (1 shared connections)
- [ContainerTransferToMixin](ContainerTransferToMixin.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 105 (86%)
- INFERRED: 17 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*