# Magic Spell Service

> 179 nodes

## Key Concepts

- **lifespan.py** (43 connections) — `server/app/lifespan.py`
- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **ExceptionTracker** (29 connections) — `server/monitoring/exception_tracker.py`
- **monitoring_dashboard.py** (26 connections) — `server/monitoring/monitoring_dashboard.py`
- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **get_cache_manager()** (21 connections) — `server/caching/lru_cache.py`
- **correct_patterns.py** (20 connections) — `docs/examples/logging/correct_patterns.py`
- **get_monitoring_dashboard()** (20 connections) — `server/monitoring/monitoring_dashboard.py`
- **exception_tracker.py** (19 connections) — `server/monitoring/exception_tracker.py`
- **track_exception()** (17 connections) — `server/monitoring/exception_tracker.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **memory_leak_metrics.py** (13 connections) — `server/monitoring/memory_leak_metrics.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **get_exception_tracker()** (12 connections) — `server/monitoring/exception_tracker.py`
- **test_exception_tracker.py** (12 connections) — `server/tests/unit/monitoring/test_exception_tracker.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **PerformanceStats** (11 connections) — `server/monitoring/performance_monitor.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **Any** (10 connections)
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- *... and 154 more nodes in this community*

## Relationships

- [Loot Generation](Loot_Generation.md) (22 shared connections)
- [aggro threat services](aggro_threat_services.md) (21 shared connections)
- [room cache services](room_cache_services.md) (21 shared connections)
- [Error Conversion](Error_Conversion.md) (18 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (16 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (14 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (7 shared connections)
- [log structured logging](log_structured_logging.md) (6 shared connections)
- [nats services service](nats_services_service.md) (4 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (3 shared connections)
- [commands skills rationale](commands_skills_rationale.md) (3 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/app/lifespan.py`
- `server/caching/lru_cache.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_exception_tracker.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 753 (96%)
- INFERRED: 33 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*