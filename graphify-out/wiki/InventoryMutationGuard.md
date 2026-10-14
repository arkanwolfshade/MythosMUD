# InventoryMutationGuard

> 30 nodes

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
- **._cleanup_state()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **.__init__()** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Acquire sync mutation guard.** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Acquire async mutation guard.** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Get or create per-player guard state for sync contexts. Uses thread-safe…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Get or create per-player guard state for async contexts. Uses async lock to…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Clean up per-player guard state when no longer needed (sync context). Removes…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Clean up per-player guard state when no longer needed (async context). Removes…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Remove expired idempotency tokens from the guard state (sync context). Tokens…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Remove expired idempotency tokens from the guard state (async context). Tokens…** (1 connections) — `server/services/inventory_mutation_guard.py`
- **Enforce maximum token cache size by removing oldest entries (sync context).…** (1 connections) — `server/services/inventory_mutation_guard.py`
- *... and 5 more nodes in this community*

## Relationships

- [MutationDecision](MutationDecision.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [MetricsCollector](MetricsCollector.md) (2 shared connections)
- [test_inventory_mutation_guard_async.py](test_inventory_mutation_guard_async.py.md) (2 shared connections)
- [test_inventory_mutation_guard_error_handling.py](test_inventory_mutation_guard_error_handling.py.md) (2 shared connections)
- [test_inventory_mutation_guard_internal.py](test_inventory_mutation_guard_internal.py.md) (2 shared connections)
- [test_inventory_mutation_guard_sync.py](test_inventory_mutation_guard_sync.py.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [ContainerService](ContainerService.md) (1 shared connections)
- [InventoryService](InventoryService.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)

## Source Files

- `server/services/inventory_mutation_guard.py`

## Audit Trail

- EXTRACTED: 63 (88%)
- INFERRED: 9 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*