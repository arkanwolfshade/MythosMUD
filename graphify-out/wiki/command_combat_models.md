# command combat models

> 35 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
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
- **Get system metrics from monitoring dashboard.** (1 connections) — `server/api/system_monitoring.py`
- **Unified metrics collector for memory leak detection.      Aggregates metrics fro** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Initialize the memory leak metrics collector.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect all metrics from all sources.          Returns:             Dictionary c** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect connection metrics from ConnectionManager.          Returns:** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect event metrics from EventBus.          Returns:             Dictionary wi** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Collect cache metrics from CacheManager.          Returns:             Dictionar** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- *... and 10 more nodes in this community*

## Relationships

- [room cache services](room_cache_services.md) (7 shared connections)
- [health models rationale](health_models_rationale.md) (6 shared connections)
- [System Metrics](System_Metrics.md) (5 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (4 shared connections)
- [metrics memory leak](metrics_memory_leak.md) (3 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (2 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [taunt combat commands](taunt_combat_commands.md) (1 shared connections)
- [follow service game](follow_service_game.md) (1 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (1 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (1 shared connections)

## Source Files

- `server/api/system_monitoring.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`

## Audit Trail

- EXTRACTED: 139 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*