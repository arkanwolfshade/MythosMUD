# InventoryService

> 68 nodes

## Key Concepts

- **InventoryService** (37 connections) — `server/services/inventory_service.py`
- **InventoryStack** (36 connections) — `server/services/inventory_service.py`
- **inventory_service.py** (33 connections) — `server/services/inventory_service.py`
- **test_inventory_service.py** (21 connections) — `server/tests/unit/services/test_inventory_service.py`
- **InventoryCapacityError** (18 connections) — `server/services/inventory_service.py`
- **InventorySplitError** (11 connections) — `server/services/inventory_service.py`
- **InventoryValidationError** (10 connections) — `server/services/inventory_service.py`
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **InventoryServiceError** (7 connections) — `server/services/inventory_service.py`
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
- *... and 43 more nodes in this community*

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (16 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (12 shared connections)
- [equipment_service.py](equipment_service.py.md) (12 shared connections)
- [ContainerComponent](ContainerComponent.md) (9 shared connections)
- [ContainerService](ContainerService.md) (7 shared connections)
- [command_service.py](command_service.py.md) (6 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (4 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (4 shared connections)
- [command_result_text](command_result_text.md) (4 shared connections)
- [ContainerTransferFromMixin](ContainerTransferFromMixin.md) (2 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)

## Source Files

- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 168 (83%)
- INFERRED: 34 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*