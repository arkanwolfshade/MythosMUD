# Test Inventory Service

> 55 nodes

## Key Concepts

- **InventoryStack** (37 connections) — `server/services/inventory_service.py`
- **test_inventory_service.py** (21 connections) — `server/tests/unit/services/test_inventory_service.py`
- **InventorySplitError** (11 connections) — `server/services/inventory_service.py`
- **InventoryValidationError** (10 connections) — `server/services/inventory_service.py`
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- **Any** (7 connections)
- **._validate_and_clone_optional_fields()** (6 connections) — `server/services/inventory_service.py`
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
- **test_split_stack_quantity_too_large()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_merges_existing()** (2 connections) — `server/tests/unit/services/test_inventory_service.py`
- *... and 30 more nodes in this community*

## Relationships

- [Equipment & Inventory Helpers](Equipment_&_Inventory_Helpers.md) (32 shared connections)
- [Container/Loot Events](Container-Loot_Events.md) (9 shared connections)
- [Container Service Helpers](Container_Service_Helpers.md) (7 shared connections)
- [Test Container Service](Test_Container_Service.md) (3 shared connections)
- [Container/Inventory Helpers](Container-Inventory_Helpers.md) (1 shared connections)
- [Container Helpers Inventory Display](Container_Helpers_Inventory_Display.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 106 (81%)
- INFERRED: 25 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*