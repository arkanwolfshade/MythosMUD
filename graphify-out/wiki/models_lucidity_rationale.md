# models lucidity rationale

> 58 nodes

## Key Concepts

- **PerformanceMonitor** (32 connections) — `server/monitoring/performance_monitor.py`
- **measure_performance()** (22 connections) — `server/monitoring/performance_monitor.py`
- **performance_monitor.py** (21 connections) — `server/monitoring/performance_monitor.py`
- **test_performance_monitor.py** (18 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **get_performance_monitor()** (15 connections) — `server/monitoring/performance_monitor.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **PerformanceStats** (11 connections) — `server/monitoring/performance_monitor.py`
- **PerformanceMetric** (9 connections) — `server/monitoring/performance_monitor.py`
- **get_performance_stats()** (9 connections) — `server/monitoring/performance_monitor.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **.record_metric()** (8 connections) — `server/monitoring/performance_monitor.py`
- **record_performance_metric()** (8 connections) — `server/monitoring/performance_monitor.py`
- **reset_performance_metrics()** (7 connections) — `server/monitoring/performance_monitor.py`
- **Any** (6 connections)
- **.get_operation_stats()** (6 connections) — `server/monitoring/performance_monitor.py`
- **.get_all_stats()** (5 connections) — `server/monitoring/performance_monitor.py`
- **._trigger_alert()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.export_metrics()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.__init__()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.get_recent_metrics()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.add_alert_callback()** (4 connections) — `server/monitoring/performance_monitor.py`
- **test_module_level_helpers_use_global_monitor()** (4 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **.get_slow_operations()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.get_failed_operations()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.reset_metrics()** (3 connections) — `server/monitoring/performance_monitor.py`
- *... and 33 more nodes in this community*

## Relationships

- [room cache services](room_cache_services.md) (11 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (6 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (5 shared connections)
- [examples logging testing](examples_logging_testing.md) (4 shared connections)
- [add hashed password](add_hashed_password.md) (4 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (4 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (3 shared connections)
- [correct patterns examples](correct_patterns_examples.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)
- [nats services service](nats_services_service.md) (2 shared connections)
- [world loader room](world_loader_room.md) (2 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_performance_monitor.py`

## Audit Trail

- EXTRACTED: 254 (93%)
- INFERRED: 19 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*