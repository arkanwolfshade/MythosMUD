# message nats handler

> 36 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **Any** (10 connections)
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_event_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **._calculate_single_growth_rate()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.calculate_growth_rates()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_connection_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_cache_alerts()** (4 connections) — `server/monitoring/memory_leak_metrics.py`
- **.__init__()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_subscriber_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_task_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_resolve_memory_leak_collector_singleton_resets_with_patch()** (3 connections) — `server/tests/unit/api/test_monitoring_endpoints.py`
- **collector()** (3 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **Unified metrics collector for memory leak detection.      Aggregates metrics fro** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Initialize the memory leak metrics collector.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect all metrics from all sources.          Returns:             Dictionary c** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect connection metrics from ConnectionManager.          Returns:** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect event metrics from EventBus.          Returns:             Dictionary wi** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect cache metrics from CacheManager.          Returns:             Dictionar** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- *... and 11 more nodes in this community*

## Relationships

- [room cache services](room_cache_services.md) (6 shared connections)
- [command combat models](command_combat_models.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [System Metrics](System_Metrics.md) (2 shared connections)
- [health models rationale](health_models_rationale.md) (2 shared connections)
- [metrics memory leak](metrics_memory_leak.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (1 shared connections)
- [Room Broadcast](Room_Broadcast.md) (1 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (1 shared connections)
- [follow service game](follow_service_game.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/api/test_monitoring_endpoints.py`
- `server/tests/unit/monitoring/test_memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 133 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*