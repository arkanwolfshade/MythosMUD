# InventoryMutationGuard

> 79 nodes

## Key Concepts

- **InventoryMutationGuard** (33 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_async.py** (11 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_inventory_mutation_guard_error_handling.py** (11 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **.acquire()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire_async()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **Lock** (8 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **asyncio** (6 connections)
- **_PlayerGuardState** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._emit_duplicate_mutation_alert()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **.__init__()** (4 connections) — `server/npc/threading.py`
- **._cleanup_async_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._get_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **asyncio** (4 connections)
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- *... and 54 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (3 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (3 shared connections)
- [test_inventory_mutation_guard.py](test_inventory_mutation_guard.py.md) (3 shared connections)
- [ContainerService](ContainerService.md) (3 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (3 shared connections)
- [test_inventory_mutation_guard_internal.py](test_inventory_mutation_guard_internal.py.md) (2 shared connections)
- [test_inventory_mutation_guard_sync.py](test_inventory_mutation_guard_sync.py.md) (2 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [MetricsCollector](MetricsCollector.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 121 (88%)
- INFERRED: 16 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*