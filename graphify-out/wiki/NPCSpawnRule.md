# NPCSpawnRule

> 63 nodes · cohesion 0.06

## Key Concepts

- **lifespan.py** (51 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (28 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **_startup_application()** (18 connections) — `server/app/lifespan.py`
- **lifespan()** (16 connections) — `server/app/lifespan.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **asyncio** (10 connections)
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **update_logging_with_player_service()** (8 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_cleanup_dead_letter_queue_periodically()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **auth/conftest.py** (6 connections) — `server/tests/unit/auth/conftest.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **FastAPI** (4 connections)
- **_mock_task_registry()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_dead_letter_queue_periodically_runs_cleanup()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_dead_letter_queue_periodically_swallows_cleanup_errors()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_persist_metrics_to_file_writes_json()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_minimal()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_registers_dlq_cleanup_when_nats_available()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **set_auth_epoch_for_tests()** (4 connections) — `server/tests/unit/auth/conftest.py`
- *... and 38 more nodes in this community*

## Relationships

- [Room](Room.md) (9 shared connections)
- [ValueError](ValueError.md) (7 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (7 shared connections)
- [._create_grid_map](_create_grid_map.md) (6 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (5 shared connections)
- [useGameClientV2ContainerNetworkPhase.ts](useGameClientV2ContainerNetworkPhase.ts.md) (4 shared connections)
- [_prepare_command_for_processing](_prepare_command_for_processing.md) (3 shared connections)
- [PlayerDeathService](PlayerDeathService.md) (3 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [NPCThreadManager](NPCThreadManager.md) (3 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (3 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/auth/token_epoch.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/auth/conftest.py`

## Audit Trail

- EXTRACTED: 188 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*