# metrics memory leak

> 73 nodes

## Key Concepts

- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_memory_leak_metrics.py** (23 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
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
- **._check_subscriber_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **._check_task_alerts()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **collector()** (3 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collector_initialization()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_connection_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_connection_metrics_no_manager()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_event_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_event_metrics_no_bus()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_cache_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- **test_collect_task_metrics()** (2 connections) — `server/tests/unit/monitoring/test_memory_leak_metrics.py`
- *... and 48 more nodes in this community*

## Relationships

- [room cache services](room_cache_services.md) (6 shared connections)
- [Loot Generation](Loot_Generation.md) (5 shared connections)
- [aggro threat services](aggro_threat_services.md) (3 shared connections)
- [services chat logger](services_chat_logger.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (1 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (1 shared connections)
- [follow service game](follow_service_game.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (1 shared connections)
- [log structured logging](log_structured_logging.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/monitoring/test_memory_leak_metrics.py`

## Audit Trail

- EXTRACTED: 209 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*