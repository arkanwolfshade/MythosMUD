# lifespan

> 44 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **get_exception_tracker()** (10 connections) — `server/monitoring/exception_tracker.py`
- **subscribe_quest_events()** (9 connections) — `server/app/lifespan_event_subscriptions.py`
- **_initialize_enhanced_systems()** (8 connections) — `server/app/lifespan.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **get_log_aggregator()** (8 connections) — `server/structured_logging/log_aggregator.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **_cleanup_container_on_error()** (5 connections) — `server/app/lifespan.py`
- **_calculate_metrics_delta()** (4 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (4 connections) — `server/app/lifespan.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **FastAPI** (4 connections)
- **_persist_mythos_state_on_error()** (4 connections) — `server/app/lifespan.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- **.test_lifespan_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_shutdown()** (4 connections) — `server/tests/unit/test_main.py`
- **Any** (3 connections)
- **.test_lifespan_initialization_failure()** (3 connections) — `server/tests/unit/test_main.py`
- **Application lifecycle management for MythosMUD server.  This module handles appl** (1 connections) — `server/app/lifespan.py`
- **Calculate metrics delta between startup and shutdown.** (1 connections) — `server/app/lifespan.py`
- *... and 19 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (25 shared connections)
- [create npc services on app()](create_npc_services_on_app%28%29.md) (9 shared connections)
- [.shutdown()](shutdown%28%29.md) (8 shared connections)
- [BaseUserManager](BaseUserManager.md) (6 shared connections)
- [.initialize()](initialize%28%29.md) (6 shared connections)
- [memory leak metrics](memory_leak_metrics.md) (5 shared connections)
- [game tick processing](game_tick_processing.md) (3 shared connections)
- [lifespan shutdown](lifespan_shutdown.md) (3 shared connections)
- [Test exception tracking functionality.](Test_exception_tracking_functionality.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [time commands](time_commands.md) (2 shared connections)
- [.get instance()](get_instance%28%29.md) (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 207 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*