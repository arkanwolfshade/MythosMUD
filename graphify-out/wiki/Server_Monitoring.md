# Server Monitoring

> 101 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_monitoring_dashboard()** (20 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_cache_manager()** (16 connections) — `server/caching/lru_cache.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **memory_leak_metrics.py** (12 connections) — `server/monitoring/memory_leak_metrics.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **PerformanceStats** (11 connections) — `server/monitoring/performance_monitor.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **Any** (10 connections)
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (9 connections) — `server/api/system_monitoring.py`
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **_initialize_enhanced_systems()** (8 connections) — `server/app/lifespan.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **SystemHealth** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **MonitoringSummary** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 76 more nodes in this community*

## Relationships

- [Server Api (5)](Server_Api_%285%29.md) (24 shared connections)
- [Docs Examples](Docs_Examples.md) (22 shared connections)
- [Server Monitoring (2)](Server_Monitoring_%282%29.md) (19 shared connections)
- [Server App](Server_App.md) (17 shared connections)
- [Server Commands](Server_Commands.md) (17 shared connections)
- [Server (6)](Server_%286%29.md) (10 shared connections)
- [Server Structured Logging (7)](Server_Structured_Logging_%287%29.md) (8 shared connections)
- [Server Api](Server_Api.md) (6 shared connections)
- [Server Admin](Server_Admin.md) (4 shared connections)
- [Server Services (22)](Server_Services_%2822%29.md) (4 shared connections)
- [Server Middleware](Server_Middleware.md) (3 shared connections)
- [Server App (3)](Server_App_%283%29.md) (3 shared connections)

## Source Files

- `server/api/system_monitoring.py`
- `server/app/lifespan.py`
- `server/caching/lru_cache.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 465 (92%)
- INFERRED: 38 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*