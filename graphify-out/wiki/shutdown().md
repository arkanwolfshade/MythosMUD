# .shutdown()

> 110 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **get_monitoring_dashboard()** (20 connections) — `server/monitoring/monitoring_dashboard.py`
- **performance_monitor.py** (20 connections) — `server/monitoring/performance_monitor.py`
- **exception_tracker.py** (18 connections) — `server/monitoring/exception_tracker.py`
- **get_cache_manager()** (16 connections) — `server/caching/lru_cache.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **get_performance_monitor()** (13 connections) — `server/monitoring/performance_monitor.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **PerformanceStats** (11 connections) — `server/monitoring/performance_monitor.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **get_exception_tracker()** (10 connections) — `server/monitoring/exception_tracker.py`
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (9 connections) — `server/api/system_monitoring.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_initialize_enhanced_systems()** (8 connections) — `server/app/lifespan.py`
- *... and 85 more nodes in this community*

## Relationships

- [fetch container items()](fetch_container_items%28%29.md) (19 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (19 shared connections)
- [PerformanceStats](PerformanceStats.md) (19 shared connections)
- [Any](Any.md) (14 shared connections)
- [init](init.md) (13 shared connections)
- [. is npc in combat()](_is_npc_in_combat%28%29.md) (12 shared connections)
- [. init ()](_init_%28%29.md) (9 shared connections)
- [nats retry handler](nats_retry_handler.md) (9 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (8 shared connections)
- [websocket integration](websocket_integration.md) (8 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (7 shared connections)
- [test command parser](test_command_parser.md) (7 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/app/lifespan.py`
- `server/auth/token_epoch.py`
- `server/caching/lru_cache.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 559 (94%)
- INFERRED: 35 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*