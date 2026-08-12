# User Manager Mute Tests

> 113 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **lifespan_shutdown.py** (15 connections) — `server/app/lifespan_shutdown.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **FastAPI** (13 connections)
- **shutdown_services()** (12 connections) — `server/app/lifespan_shutdown.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **initialize_npc_services()** (10 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (10 connections) — `server/app/lifespan_startup.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **initialize_chat_service()** (9 connections) — `server/app/lifespan_startup.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
- **_cleanup_container_on_error()** (5 connections) — `server/app/lifespan.py`
- **FastAPI** (5 connections)
- **_get_item_prototype_count()** (5 connections) — `server/app/lifespan_startup.py`
- **_legacy_service_bindings()** (5 connections) — `server/app/lifespan_startup.py`
- **nats_service()** (5 connections) — `server/tests/unit/services/test_nats_service.py`
- **_calculate_metrics_delta()** (4 connections) — `server/app/lifespan.py`
- *... and 88 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (38 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (22 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (9 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (6 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (5 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (3 shared connections)
- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (3 shared connections)
- [NATS Subject Metrics](NATS_Subject_Metrics.md) (3 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (3 shared connections)
- [Catatonia Registry Service](Catatonia_Registry_Service.md) (3 shared connections)
- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (2 shared connections)
- [Monitoring Bundle Services](Monitoring_Bundle_Services.md) (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_shutdown.py`
- `server/app/lifespan_startup.py`
- `server/auth/token_epoch.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/services/test_nats_service.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 436 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*