# lock

> 47 nodes

## Key Concepts

- **MetricsCollector** (18 connections) — `server/middleware/metrics_collector.py`
- **.acquire_async()** (8 connections) — `server/services/inventory_mutation_guard.py`
- **Lock** (8 connections)
- **test_metrics_collector.py** (7 connections) — `server/tests/unit/middleware/test_metrics_collector.py`
- **_AsyncPlayerGuardState** (6 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_global_lock()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._get_async_state()** (5 connections) — `server/services/inventory_mutation_guard.py`
- **._cleanup_async_state()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._enforce_limit_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
- **._prune_tokens_async()** (4 connections) — `server/services/inventory_mutation_guard.py`
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
- *... and 22 more nodes in this community*

## Relationships

- [abstractcontextmanager](abstractcontextmanager.md) (8 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server npc init](server_npc_init.md) (2 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (1 shared connections)
- [server api container endpoints loot](server_api_container_endpoints_loot.md) (1 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (1 shared connections)
- [server realtime connection initialization initialize](server_realtime_connection_initialization_initialize.md) (1 shared connections)
- [holidayresolver](holidayresolver.md) (1 shared connections)

## Source Files

- `server/middleware/metrics_collector.py`
- `server/npc/threading.py`
- `server/services/inventory_mutation_guard.py`
- `server/tests/unit/middleware/test_metrics_collector.py`

## Audit Trail

- EXTRACTED: 63 (86%)
- INFERRED: 10 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*