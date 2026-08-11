# Docker PostgreSQL Typo Bug

> 84 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **MemoryLeakMetricsCollector** (33 connections) — `server/monitoring/memory_leak_metrics.py`
- **exception_tracker.py** (20 connections) — `server/monitoring/exception_tracker.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **track_exception()** (14 connections) — `server/monitoring/exception_tracker.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **get_exception_tracker()** (10 connections) — `server/monitoring/exception_tracker.py`
- **Any** (10 connections)
- **.collect_all_metrics()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **.check_alerts()** (9 connections) — `server/monitoring/memory_leak_metrics.py`
- **_initialize_enhanced_systems()** (8 connections) — `server/app/lifespan.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **get_log_aggregator()** (8 connections) — `server/structured_logging/log_aggregator.py`
- **track_exception_with_context()** (7 connections) — `server/monitoring/exception_tracker.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
- **_cleanup_container_on_error()** (5 connections) — `server/app/lifespan.py`
- **.collect_connection_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_event_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_cache_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_task_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **.collect_nats_metrics()** (5 connections) — `server/monitoring/memory_leak_metrics.py`
- **_calculate_metrics_delta()** (4 connections) — `server/app/lifespan.py`
- *... and 59 more nodes in this community*

## Relationships

- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (13 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (11 shared connections)
- [Client Event Store](Client_Event_Store.md) (10 shared connections)
- [Merge Refactoring Summary](Merge_Refactoring_Summary.md) (8 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (7 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (7 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (7 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (7 shared connections)
- [Monitoring Bundle Services](Monitoring_Bundle_Services.md) (4 shared connections)
- [Command Field Validators](Command_Field_Validators.md) (4 shared connections)
- [Command Alias Handling](Command_Alias_Handling.md) (3 shared connections)
- [E2E Playwright Conversion Plan](E2E_Playwright_Conversion_Plan.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/auth/token_epoch.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 367 (97%)
- INFERRED: 13 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*