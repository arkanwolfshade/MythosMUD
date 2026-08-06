# models lucidity rationale

> 55 nodes

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
- **correct_performance_logging()** (5 connections) — `docs/examples/logging/correct_patterns.py`
- **.get_all_stats()** (5 connections) — `server/monitoring/performance_monitor.py`
- **._trigger_alert()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.export_metrics()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.__init__()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.get_recent_metrics()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.add_alert_callback()** (4 connections) — `server/monitoring/performance_monitor.py`
- **test_module_level_helpers_use_global_monitor()** (4 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **process_data()** (3 connections) — `docs/examples/logging/correct_patterns.py`
- **.get_slow_operations()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.get_failed_operations()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.reset_metrics()** (3 connections) — `server/monitoring/performance_monitor.py`
- **test_measure_performance_success_and_failure()** (3 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- *... and 30 more nodes in this community*

## Relationships

- [Magic Spell Service](Magic_Spell_Service.md) (16 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (8 shared connections)
- [examples logging testing](examples_logging_testing.md) (4 shared connections)
- [websocket examples logging](websocket_examples_logging.md) (4 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)
- [command parser rationale](command_parser_rationale.md) (3 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (2 shared connections)
- [correct patterns examples](correct_patterns_examples.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (1 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (1 shared connections)
- [examples migration logging](examples_migration_logging.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_performance_monitor.py`

## Audit Trail

- EXTRACTED: 240 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*