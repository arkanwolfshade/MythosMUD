# InventoryMutationGuard

> 63 nodes

## Key Concepts

- **InventoryMutationGuard** (33 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_mutation_guard_error_handling.py** (11 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
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
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **guard()** (4 connections) — `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- **asyncio** (4 connections)
- **._cleanup_state()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **test_acquire_async_record_custom_alert_type_error_fallback()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_acquire_async_record_custom_alert_with_message_param()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_cleanup_async_state_lock_attribute_error()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_cleanup_async_state_lock_runtime_error()** (3 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- **test_acquire_record_custom_alert_type_error_fallback()** (2 connections) — `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- *... and 38 more nodes in this community*

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (7 shared connections)
- [test_inventory_mutation_guard.py](test_inventory_mutation_guard.py.md) (3 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [MetricsCollector](MetricsCollector.md) (2 shared connections)
- [test_inventory_mutation_guard_async.py](test_inventory_mutation_guard_async.py.md) (2 shared connections)
- [test_inventory_mutation_guard_internal.py](test_inventory_mutation_guard_internal.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [ContainerTransferToMixin](ContainerTransferToMixin.md) (1 shared connections)
- [get_monitoring_dashboard](get_monitoring_dashboard.md) (1 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_error_handling.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`

## Audit Trail

- EXTRACTED: 102 (92%)
- INFERRED: 9 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*