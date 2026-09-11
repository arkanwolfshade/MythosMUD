# InventoryMutationGuard

> 91 nodes

## Key Concepts

- **InventoryMutationGuard** (33 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_inventory_mutation_guard_async.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_inventory_mutation_guard_sync.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **.acquire()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire_async()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **asyncio** (6 connections)
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
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **asyncio** (4 connections)
- **._cleanup_state()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **test_acquire_async_cleanup_empty_state()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_acquire_async_concurrent_same_player()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- *... and 66 more nodes in this community*

## Relationships

- [inventory_equip_command.py](inventory_equip_command.py.md) (9 shared connections)
- [ContainerService](ContainerService.md) (6 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [MetricsCollector](MetricsCollector.md) (2 shared connections)
- [test_inventory_mutation_guard_error_handling.py](test_inventory_mutation_guard_error_handling.py.md) (2 shared connections)
- [test_inventory_mutation_guard_internal.py](test_inventory_mutation_guard_internal.py.md) (2 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (2 shared connections)
- [time.py](time.py.md) (1 shared connections)

## Source Files

- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 136 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*