# .shutdown()

> 40 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **_initialize_enhanced_systems()** (8 connections) — `server/app/lifespan.py`
- **.reset_instance()** (6 connections) — `server/container/main.py`
- **test_application_container_set_instance()** (6 connections) — `server/tests/unit/test_application_container.py`
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
- **_cleanup_container_on_error()** (5 connections) — `server/app/lifespan.py`
- **_calculate_metrics_delta()** (4 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (4 connections) — `server/app/lifespan.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **FastAPI** (4 connections)
- **_persist_mythos_state_on_error()** (4 connections) — `server/app/lifespan.py`
- **.set_instance()** (4 connections) — `server/container/main.py`
- **test_application_container_get_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **test_application_container_reset_instance()** (4 connections) — `server/tests/unit/test_application_container.py`
- **.test_lifespan_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_shutdown()** (4 connections) — `server/tests/unit/test_main.py`
- **Any** (3 connections)
- **.test_lifespan_initialization_failure()** (3 connections) — `server/tests/unit/test_main.py`
- **Application lifecycle management for MythosMUD server.  This module handles appl** (1 connections) — `server/app/lifespan.py`
- **Calculate metrics delta between startup and shutdown.** (1 connections) — `server/app/lifespan.py`
- **Persist metrics to file in JSON format.** (1 connections) — `server/app/lifespan.py`
- **Log memory leak metrics periodically.      Args:         collector: MemoryLeakMe** (1 connections) — `server/app/lifespan.py`
- *... and 15 more nodes in this community*

## Relationships

- [NPCLifecycleManager](NPCLifecycleManager.md) (17 shared connections)
- [init](init.md) (8 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (7 shared connections)
- [PerformanceStats](PerformanceStats.md) (7 shared connections)
- [Any](Any.md) (4 shared connections)
- [world](world.md) (4 shared connections)
- [test command parser](test_command_parser.md) (4 shared connections)
- [Protocol](Protocol.md) (3 shared connections)
- [Connection Manager](Connection_Manager.md) (3 shared connections)
- [aggregate log entry()](aggregate_log_entry%28%29.md) (3 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (3 shared connections)
- [ConnectionsComponent](ConnectionsComponent.md) (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/container/main.py`
- `server/tests/unit/test_application_container.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 171 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*