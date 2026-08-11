# Docker PostgreSQL Typo Bug

> 57 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **lifespan()** (15 connections) — `server/app/lifespan.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **RestartInvalidatingJWTStrategy** (12 connections) — `server/auth/jwt_strategy.py`
- **_shutdown_with_error_handling()** (10 connections) — `server/app/lifespan.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_initialize_enhanced_systems()** (8 connections) — `server/app/lifespan.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **_cleanup_container_on_error()** (5 connections) — `server/app/lifespan.py`
- **test_read_token_accepts_matching_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_calculate_metrics_delta()** (4 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (4 connections) — `server/app/lifespan.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **FastAPI** (4 connections)
- **_persist_mythos_state_on_error()** (4 connections) — `server/app/lifespan.py`
- **conftest.py** (4 connections) — `server/tests/unit/auth/conftest.py`
- **test_read_token_rejects_wrong_epoch()** (4 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_read_token_rejects_missing_epoch()** (4 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **.test_lifespan_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_shutdown()** (4 connections) — `server/tests/unit/test_main.py`
- *... and 32 more nodes in this community*

## Relationships

- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (13 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (12 shared connections)
- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (7 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (7 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (4 shared connections)
- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (3 shared connections)
- [Player Cache](Player_Cache.md) (3 shared connections)
- [Merge Refactoring Summary](Merge_Refactoring_Summary.md) (3 shared connections)
- [Monitoring Bundle Services](Monitoring_Bundle_Services.md) (3 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (3 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (2 shared connections)
- [Container Repository CRUD](Container_Repository_CRUD.md) (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 238 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*