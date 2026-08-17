# InventoryMutationGuard

> 33 nodes

## Key Concepts

- **InventoryMutationGuard** (33 connections) — `server/services/inventory_mutation_guard.py`
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
- **.__init__()** (1 connections) — `server/services/inventory_mutation_guard.py`
- **fixture** (1 connections)
- **Acquire sync mutation guard.** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Acquire async mutation guard.** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Get or create per-player guard state for sync contexts. Uses thread-safe…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Get or create per-player guard state for async contexts. Uses async lock to…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Clean up per-player guard state when no longer needed (sync context). Removes…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Clean up per-player guard state when no longer needed (async context). Removes…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Remove expired idempotency tokens from the guard state (sync context). Tokens…** (1 connections) — `server/services/inventory_mutation_guard.py`
- *... and 8 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [test_inventory_mutation_guard.py](test_inventory_mutation_guard.py.md) (3 shared connections)
- [ContainerService](ContainerService.md) (3 shared connections)
- [MetricsCollector](MetricsCollector.md) (2 shared connections)
- [test_inventory_mutation_guard_async.py](test_inventory_mutation_guard_async.py.md) (2 shared connections)
- [test_inventory_mutation_guard_error_handling.py](test_inventory_mutation_guard_error_handling.py.md) (2 shared connections)
- [test_inventory_mutation_guard_internal.py](test_inventory_mutation_guard_internal.py.md) (2 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (2 shared connections)
- [ContainerTransferToMixin](ContainerTransferToMixin.md) (1 shared connections)
- [InventoryService](InventoryService.md) (1 shared connections)

## Source Files

- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 65 (87%)
- INFERRED: 10 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*