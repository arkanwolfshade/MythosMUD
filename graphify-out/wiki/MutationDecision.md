# MutationDecision

> 33 nodes

## Key Concepts

- **MutationDecision** (17 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_transfer_to_container_mutation_guard_suppressed()** (6 connections) — `server/tests/unit/services/test_container_service.py`
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **asyncio** (4 connections)
- **test_acquire_async_different_players_same_token()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_acquire_async_with_duplicate_token()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_acquire_async_with_unique_token()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_acquire_async_without_token()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_inventory_mutation_guard_init_custom_params()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_mutation_decision_duplicate()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_mutation_decision_init()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_acquire_different_players_same_token()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_acquire_with_duplicate_token()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_acquire_with_unique_token()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_acquire_without_token()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_inventory_mutation_guard_init()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **fixture** (1 connections)
- **Result of attempting to acquire a guarded mutation context.** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Unit tests for inventory mutation guard - core functionality. Tests…** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **Test acquire_async without token allows mutation.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **Test acquire_async with unique token allows mutation.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **Test acquire_async with duplicate token suppresses mutation.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **Test acquire_async allows same token for different players.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **Create an InventoryMutationGuard instance.** (1 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- *... and 8 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (7 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [ContainerService](ContainerService.md) (3 shared connections)
- [InventoryService](InventoryService.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)

## Source Files

- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_container_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`

## Audit Trail

- EXTRACTED: 51 (88%)
- INFERRED: 7 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*