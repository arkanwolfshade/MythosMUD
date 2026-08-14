# MetricsCollector

> 36 nodes

## Key Concepts

- **MetricsCollector** (18 connections) — `server/middleware/metrics_collector.py`
- **Lock** (8 connections)
- **.__init__()** (7 connections) — `server/time/tick_scheduler.py`
- **test_metrics_collector.py** (7 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **.get_metrics()** (3 connections) — `server/middleware/metrics_collector.py`
- **.get_summary()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (3 connections) — `server/middleware/metrics_collector.py`
- **.__init__()** (3 connections) — `server/npc/threading.py`
- **.get_lock()** (3 connections) — `server/services/inventory_mutation_guard.py`
- **.record_circuit_state_change()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_dlq()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_failed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_processed()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_message_retried()** (2 connections) — `server/middleware/metrics_collector.py`
- **.record_processing_time()** (2 connections) — `server/middleware/metrics_collector.py`
- **.reset_metrics()** (2 connections) — `server/middleware/metrics_collector.py`
- **test_circuit_state_change_trims_history()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_get_summary()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_record_and_get_metrics()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **test_reset_metrics()** (2 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **Any** (2 connections)
- **HolidayResolver** (1 connections)
- **Record a circuit breaker state change. Args: old_state: Previous circuit state…** (1 connections) — `server/middleware/metrics_collector.py`
- **Record message processing time. Args: duration_ms: Processing duration in…** (1 connections) — `server/middleware/metrics_collector.py`
- **Get current metrics snapshot. Returns: Dictionary containing all metrics AI:…** (1 connections) — `server/middleware/metrics_collector.py`
- *... and 11 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (2 shared connections)
- [InventoryMutationGuard](InventoryMutationGuard.md) (2 shared connections)
- [TaskRegistry](TaskRegistry.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [MythosChronicle](MythosChronicle.md) (1 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/middleware/test_metrics_collector.py`
- `server/time/tick_scheduler.py`

## Audit Trail

- EXTRACTED: 48 (89%)
- INFERRED: 6 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*