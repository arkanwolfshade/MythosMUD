# verify_enhanced_logging_compliance.py

> 47 nodes

## Key Concepts

- **lifespan.py** (42 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (27 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (16 connections) — `server/app/lifespan.py`
- **_startup_application()** (15 connections) — `server/app/lifespan.py`
- **test_main.py** (15 connections) — `server/tests/unit/test_main.py`
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **asyncio** (10 connections)
- **_initialize_enhanced_systems()** (9 connections) — `server/app/lifespan.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_cleanup_dead_letter_queue_periodically()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (6 connections) — `server/app/lifespan.py`
- **update_logging_with_player_service()** (5 connections) — `server/structured_logging/enhanced_logging_config.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **test_cleanup_dead_letter_queue_periodically_runs_cleanup()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_dead_letter_queue_periodically_swallows_cleanup_errors()** (4 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **FastAPI** (4 connections)
- **test_cleanup_container_on_error_none()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_cleanup_container_on_error_with_container()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_initialize_enhanced_systems()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_lifespan_happy_path()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_shutdown_with_error_handling()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_minimal()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **test_startup_application_registers_dlq_cleanup_when_nats_available()** (3 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- *... and 22 more nodes in this community*

## Relationships

- [debrief_command.py](debrief_command.py.md) (10 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (8 shared connections)
- [test_who_commands.py](test_who_commands.py.md) (7 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (4 shared connections)
- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (3 shared connections)
- [NPCOccupantProcessor](NPCOccupantProcessor.md) (3 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (3 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (3 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (2 shared connections)
- [3. REFACTOR Findings (935 findings)](3._REFACTOR_Findings_935_findings.md) (2 shared connections)
- [useRespawnHandlers.ts](useRespawnHandlers.ts.md) (2 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/structured_logging/enhanced_logging_config.py`
- `server/tests/unit/app/test_lifespan_helpers.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 155 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*