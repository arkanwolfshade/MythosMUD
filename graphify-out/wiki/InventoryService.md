# InventoryService

> 61 nodes

## Key Concepts

- **InventoryService** (37 connections) — `server/services/inventory_service.py`
- **InventoryStack** (36 connections) — `server/services/inventory_service.py`
- **test_inventory_service.py** (21 connections) — `server/tests/unit/services/test_inventory_service.py`
- **InventorySplitError** (11 connections) — `server/services/inventory_service.py`
- **InventoryValidationError** (10 connections) — `server/services/inventory_service.py`
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- **Any** (7 connections)
- **._validate_and_clone_optional_fields()** (6 connections) — `server/services/inventory_service.py`
- **.begin_mutation()** (5 connections) — `server/services/inventory_service.py`
- **InventoryStackRequired** (4 connections) — `server/services/inventory_service.py`
- **._can_merge()** (4 connections) — `server/services/inventory_service.py`
- **._extract_required_fields()** (4 connections) — `server/services/inventory_service.py`
- **._normalize_metadata()** (4 connections) — `server/services/inventory_service.py`
- **inventory_service()** (4 connections) — `server/tests/unit/services/test_inventory_service.py`
- **InnerContainer** (3 connections) — `server/services/inventory_service.py`
- **test_add_stack_capacity_error()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_validation_error_invalid_quantity()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_validation_error_missing_field()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_capacity_error()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_invalid_index()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_invalid_quantity_negative()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_invalid_quantity_zero()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- *... and 36 more nodes in this community*

## Relationships

- [inventory_command_helpers.py](inventory_command_helpers.py.md) (36 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [ContainerComponent](ContainerComponent.md) (8 shared connections)
- [ContainerSourceType](ContainerSourceType.md) (5 shared connections)
- [command_result_text](command_result_text.md) (3 shared connections)
- [ContainerTransferToMixin](ContainerTransferToMixin.md) (2 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (1 shared connections)
- [handle_unequip_command](handle_unequip_command.md) (1 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (1 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (1 shared connections)
- [test_container_helpers_inventory_display.py](test_container_helpers_inventory_display.py.md) (1 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (1 shared connections)

## Source Files

- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 130 (80%)
- INFERRED: 32 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*