# player cache rationale

> 32 nodes

## Key Concepts

- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **InventoryValidationError** (13 connections) — `server/services/inventory_service.py`
- **inventory_service()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_capacity_error()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_validation_error_missing_field()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_validation_error_invalid_quantity()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_invalid_index()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_invalid_quantity_zero()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_invalid_quantity_negative()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_quantity_too_large()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_capacity_error()** (3 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_new_item()** (2 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_add_stack_merges_existing()** (2 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_split_stack_success()** (2 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_begin_mutation_success()** (2 connections) — `server/tests/unit/services/test_inventory_service.py`
- **test_begin_mutation_with_string_id()** (2 connections) — `server/tests/unit/services/test_inventory_service.py`
- **Raised when item payloads are malformed or incomplete.** (1 connections) — `server/services/inventory_service.py`
- **Unit tests for inventory service.  Tests the InventoryService class for inventor** (1 connections) — `server/tests/unit/services/test_inventory_service.py`
- **Create an InventoryService instance.** (1 connections) — `server/tests/unit/services/test_inventory_service.py`
- **Test add_stack adds new item to inventory.** (1 connections) — `server/tests/unit/services/test_inventory_service.py`
- **Test add_stack merges with existing stack.** (1 connections) — `server/tests/unit/services/test_inventory_service.py`
- **Test add_stack raises InventoryCapacityError when at capacity.** (1 connections) — `server/tests/unit/services/test_inventory_service.py`
- **Test add_stack raises InventoryValidationError for missing fields.** (1 connections) — `server/tests/unit/services/test_inventory_service.py`
- **Test add_stack raises InventoryValidationError for invalid quantity.** (1 connections) — `server/tests/unit/services/test_inventory_service.py`
- **Test split_stack successfully splits a stack.** (1 connections) — `server/tests/unit/services/test_inventory_service.py`
- *... and 7 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (14 shared connections)
- [payload realtime optimizer](payload_realtime_optimizer.md) (2 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (2 shared connections)
- [commands inventory command](commands_inventory_command.md) (1 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)

## Source Files

- `server/services/inventory_service.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 73 (85%)
- INFERRED: 13 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*