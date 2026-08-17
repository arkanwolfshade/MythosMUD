# server monitoring init getattr

> 58 nodes

## Key Concepts

- **PerformanceMonitor** (32 connections) — `server/monitoring/performance_monitor.py`
- **measure_performance()** (21 connections) — `server/monitoring/performance_monitor.py`
- **performance_monitor.py** (21 connections) — `server/monitoring/performance_monitor.py`
- **test_performance_monitor.py** (19 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **get_performance_monitor()** (15 connections) — `server/monitoring/performance_monitor.py`
- **PerformanceStats** (9 connections) — `server/monitoring/performance_monitor.py`
- **PerformanceMetric** (8 connections) — `server/monitoring/performance_monitor.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **get_performance_stats()** (7 connections) — `server/monitoring/performance_monitor.py`
- **record_performance_metric()** (7 connections) — `server/monitoring/performance_monitor.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_metric()** (6 connections) — `server/monitoring/performance_monitor.py`
- **reset_performance_metrics()** (6 connections) — `server/monitoring/performance_monitor.py`
- **Any** (6 connections)
- **.export_metrics()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.get_operation_stats()** (5 connections) — `server/monitoring/performance_monitor.py`
- **._trigger_alert()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.add_alert_callback()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.get_all_stats()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.get_recent_metrics()** (4 connections) — `server/monitoring/performance_monitor.py`
- **test_module_level_helpers_use_global_monitor()** (4 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **.get_failed_operations()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.get_slow_operations()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.__init__()** (3 connections) — `server/monitoring/performance_monitor.py`
- **test_measure_performance_success_and_failure()** (3 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- *... and 33 more nodes in this community*

## Relationships

- [docs examples logging websocket integration](docs_examples_logging_websocket_integration.md) (9 shared connections)
- [docs examples logging correct patterns](docs_examples_logging_correct_patterns.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (5 shared connections)
- [server api monitoring models](server_api_monitoring_models.md) (4 shared connections)
- [performancestats](performancestats.md) (4 shared connections)
- [docs examples logging testing examples](docs_examples_logging_testing_examples.md) (4 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [server app lifespan](server_app_lifespan.md) (3 shared connections)
- [server services passive lucidity flux](server_services_passive_lucidity_flux.md) (2 shared connections)
- [attributeerror](attributeerror.md) (1 shared connections)
- [logentry](logentry.md) (1 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_performance_monitor.py`

## Audit Trail

- EXTRACTED: 134 (87%)
- INFERRED: 20 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*