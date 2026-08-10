# Test Optimization Insights

> 42 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **lifespan_event_subscriptions.py** (11 connections) — `server/app/lifespan_event_subscriptions.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **subscribe_quest_events()** (9 connections) — `server/app/lifespan_event_subscriptions.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **subscribe_room_occupants_refresh()** (7 connections) — `server/app/lifespan_event_subscriptions.py`
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
- **_cleanup_container_on_error()** (5 connections) — `server/app/lifespan.py`
- **_calculate_metrics_delta()** (4 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (4 connections) — `server/app/lifespan.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **FastAPI** (4 connections)
- **_persist_mythos_state_on_error()** (4 connections) — `server/app/lifespan.py`
- **.test_lifespan_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_shutdown()** (4 connections) — `server/tests/unit/test_main.py`
- **Any** (3 connections)
- **test_setup_connection_manager()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **test_setup_connection_manager_no_manager()** (3 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **.test_lifespan_initialization_failure()** (3 connections) — `server/tests/unit/test_main.py`
- **Application lifecycle management for MythosMUD server.  This module handles appl** (1 connections) — `server/app/lifespan.py`
- **Calculate metrics delta between startup and shutdown.** (1 connections) — `server/app/lifespan.py`
- **Persist metrics to file in JSON format.** (1 connections) — `server/app/lifespan.py`
- *... and 17 more nodes in this community*

## Relationships

- [MP Regeneration Service](MP_Regeneration_Service.md) (12 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (10 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (9 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (7 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (7 shared connections)
- [Invite and User Schemas](Invite_and_User_Schemas.md) (5 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (3 shared connections)
- [Party Service Management](Party_Service_Management.md) (3 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (3 shared connections)
- [Merge Refactoring Summary](Merge_Refactoring_Summary.md) (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_startup.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 188 (95%)
- INFERRED: 9 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*