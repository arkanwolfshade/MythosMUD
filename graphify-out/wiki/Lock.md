# Lock

> 96 nodes

## Key Concepts

- **InventoryMutationGuard** (42 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **.acquire_async()** (11 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire()** (10 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_error_handling.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_inventory_mutation_guard_sync.py** (10 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **test_inventory_mutation_guard_async.py** (9 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **Lock** (8 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **_PlayerGuardState** (5 connections) — `server/services/inventory_mutation_guard.py`
- **.get_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_state()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **guard()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_mutation_decision_init()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_mutation_decision_duplicate()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **test_inventory_mutation_guard_init_custom_params()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **guard()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- *... and 71 more nodes in this community*

## Relationships

- [AbstractContextManager](AbstractContextManager.md) (15 shared connections)
- [main()](main%28%29.md) (10 shared connections)
- [APIRouter](APIRouter.md) (7 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [test inventory mutation guard internal](test_inventory_mutation_guard_internal.md) (2 shared connections)
- [PerformanceStats](PerformanceStats.md) (2 shared connections)
- [.shutdown()](shutdown%28%29.md) (1 shared connections)
- [MetricsCollector](MetricsCollector.md) (1 shared connections)

## Source Files

- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 274 (93%)
- INFERRED: 21 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*