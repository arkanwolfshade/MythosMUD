# InventoryMutationGuard

> 45 nodes

## Key Concepts

- **InventoryMutationGuard** (33 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_sync.py** (11 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **.acquire()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire_async()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **_PlayerGuardState** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._emit_duplicate_mutation_alert()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_async_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._get_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **._cleanup_state()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **test_acquire_cleanup_empty_state()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_enforces_max_tokens()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_serializes_per_player()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_token_expiry()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_acquire_token_ttl_zero()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **.__init__()** (1 connections) — `server/services/inventory_mutation_guard.py`
- **fixture** (1 connections)
- **Acquire sync mutation guard.** (1 connections) — `server/services/inventory_mutation_guard.py`
- *... and 20 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [test_inventory_mutation_guard.py](test_inventory_mutation_guard.py.md) (3 shared connections)
- [ContainerSourceType](ContainerSourceType.md) (3 shared connections)
- [MetricsCollector](MetricsCollector.md) (2 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (2 shared connections)
- [test_inventory_mutation_guard_async.py](test_inventory_mutation_guard_async.py.md) (2 shared connections)
- [test_inventory_mutation_guard_error_handling.py](test_inventory_mutation_guard_error_handling.py.md) (2 shared connections)
- [test_inventory_mutation_guard_internal.py](test_inventory_mutation_guard_internal.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [ContainerTransferToMixin](ContainerTransferToMixin.md) (1 shared connections)
- [InventoryService](InventoryService.md) (1 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (1 shared connections)

## Source Files

- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 79 (89%)
- INFERRED: 10 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*