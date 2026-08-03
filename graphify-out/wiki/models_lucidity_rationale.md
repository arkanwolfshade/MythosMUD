# models lucidity rationale

> 51 nodes

## Key Concepts

- **PerformanceMonitor** (32 connections) — `server/monitoring/performance_monitor.py`
- **measure_performance()** (22 connections) — `server/monitoring/performance_monitor.py`
- **performance_monitor.py** (21 connections) — `server/monitoring/performance_monitor.py`
- **test_performance_monitor.py** (18 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **get_performance_monitor()** (15 connections) — `server/monitoring/performance_monitor.py`
- **PerformanceMetric** (9 connections) — `server/monitoring/performance_monitor.py`
- **get_performance_stats()** (9 connections) — `server/monitoring/performance_monitor.py`
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
- **test_measure_performance_success_and_failure()** (3 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **test_record_metric_and_stats()** (2 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **test_get_operation_stats_missing_returns_none()** (2 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- *... and 26 more nodes in this community*

## Relationships

- [room cache services](room_cache_services.md) (8 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (6 shared connections)
- [examples logging testing](examples_logging_testing.md) (4 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (4 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (4 shared connections)
- [correct patterns examples](correct_patterns_examples.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (1 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (1 shared connections)

## Source Files

- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_performance_monitor.py`

## Audit Trail

- EXTRACTED: 230 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*