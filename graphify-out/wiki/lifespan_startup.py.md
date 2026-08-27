# lifespan_startup.py

> 69 nodes

## Key Concepts

- **lifespan_startup.py** (66 connections) — `server/app/lifespan_startup.py`
- **lifespan.py** (46 connections) — `server/app/lifespan.py`
- **test_lifespan_helpers.py** (27 connections) — `server/tests/unit/app/test_lifespan_helpers.py`
- **lifespan()** (17 connections) — `server/app/lifespan.py`
- **_startup_application()** (16 connections) — `server/app/lifespan.py`
- **FastAPI** (15 connections)
- **_shutdown_with_error_handling()** (12 connections) — `server/app/lifespan.py`
- **setup_connection_manager()** (11 connections) — `server/app/lifespan_startup.py`
- **_initialize_enhanced_systems()** (10 connections) — `server/app/lifespan.py`
- **asyncio** (10 connections)
- **initialize_nats_and_combat_services()** (9 connections) — `server/app/lifespan_startup.py`
- **initialize_npc_startup_spawning()** (9 connections) — `server/app/lifespan_startup.py`
- **_cleanup_container_on_error()** (8 connections) — `server/app/lifespan.py`
- **_attach_combat_service()** (8 connections) — `server/app/lifespan_startup.py`
- **_calculate_metrics_delta()** (7 connections) — `server/app/lifespan.py`
- **_cleanup_dead_letter_queue_periodically()** (7 connections) — `server/app/lifespan.py`
- **_persist_mythos_state_on_error()** (7 connections) — `server/app/lifespan.py`
- **_persist_metrics_to_file()** (6 connections) — `server/app/lifespan.py`
- **_load_npc_definitions_and_rules()** (6 connections) — `server/app/lifespan_startup.py`
- **_set_legacy_services()** (6 connections) — `server/app/lifespan_startup.py`
- **nats_is_connected()** (5 connections) — `server/app/lifespan_protocols.py`
- **_log_npc_startup_errors()** (5 connections) — `server/app/lifespan_startup.py`
- **_start_nats_message_handler()** (5 connections) — `server/app/lifespan_startup.py`
- **_log_memory_metrics_periodically()** (4 connections) — `server/app/lifespan.py`
- **_ensure_room_cache_before_npc_startup()** (4 connections) — `server/app/lifespan_startup.py`
- *... and 44 more nodes in this community*

## Relationships

- [test_lifespan_startup.py](test_lifespan_startup.py.md) (29 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (14 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [system_monitoring.py](system_monitoring.py.md) (7 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (7 shared connections)
- [AliasStorage](AliasStorage.md) (5 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (5 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [NPCDefinition](NPCDefinition.md) (4 shared connections)
- [.__post_init__](__post_init__.md) (4 shared connections)
- [models/player.py](models-player.py.md) (4 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_protocols.py`
- `server/app/lifespan_startup.py`
- `server/tests/unit/app/test_lifespan_helpers.py`

## Audit Trail

- EXTRACTED: 269 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*