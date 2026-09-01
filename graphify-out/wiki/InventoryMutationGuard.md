# InventoryMutationGuard

> 114 nodes

## Key Concepts

- **InventoryMutationGuard** (33 connections) — `server/services/inventory_mutation_guard.py`
- **inventory_mutation_guard.py** (21 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_internal.py** (16 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **test_inventory_mutation_guard_async.py** (11 connections) — `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- **test_inventory_mutation_guard_error_handling.py** (11 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_inventory_mutation_guard_sync.py** (11 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **.acquire()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **.acquire_async()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **Lock** (8 connections)
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **asyncio** (6 connections)
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
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- *... and 89 more nodes in this community*

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (7 shared connections)
- [test_inventory_mutation_guard.py](test_inventory_mutation_guard.py.md) (4 shared connections)
- [ContainerService](ContainerService.md) (4 shared connections)
- [pytest.md](pytest.md.md) (4 shared connections)
- [time.py](time.py.md) (3 shared connections)
- [HolidayService](HolidayService.md) (2 shared connections)
- [MetricsCollector](MetricsCollector.md) (2 shared connections)
- [test_npc_threading_messages.py](test_npc_threading_messages.py.md) (2 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [ContainerTransferToMixin](ContainerTransferToMixin.md) (1 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 177 (92%)
- INFERRED: 15 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*