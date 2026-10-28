# test_combat_persistence_handler_persistence.py

> 36 nodes · cohesion 0.12

## Key Concepts

- **NPCStartupService** (54 connections) — `server/services/npc_startup_service.py`
- **npc_startup_service.py** (17 connections) — `server/services/npc_startup_service.py`
- **Any** (17 connections)
- **._determine_spawn_room()** (8 connections) — `server/services/npc_startup_service.py`
- **._spawn_required_npcs()** (8 connections) — `server/services/npc_startup_service.py`
- **._run_startup_pass()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_arena_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **._spawn_optional_npcs()** (7 connections) — `server/services/npc_startup_service.py`
- **.spawn_npcs_on_startup()** (6 connections) — `server/services/npc_startup_service.py`
- **_new_spawn_results()** (5 connections) — `server/services/npc_startup_service.py`
- **._try_spawn_npc()** (5 connections) — `server/services/npc_startup_service.py`
- **._spawn_one_arena_npc()** (4 connections) — `server/services/npc_startup_service.py`
- **._try_sub_zone_room()** (4 connections) — `server/services/npc_startup_service.py`
- **_record_spawned_npc()** (4 connections) — `server/services/npc_startup_service.py`
- **npc_startup_service()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **_merge_phase_into_startup()** (3 connections) — `server/services/npc_startup_service.py`
- **._get_default_room_for_sub_zone()** (3 connections) — `server/services/npc_startup_service.py`
- **._get_persistence_for_spawn()** (3 connections) — `server/services/npc_startup_service.py`
- **._handle_required_no_room()** (3 connections) — `server/services/npc_startup_service.py`
- **.__init__()** (3 connections) — `server/services/npc_startup_service.py`
- **._try_fallback_room()** (3 connections) — `server/services/npc_startup_service.py`
- **._try_specific_room()** (3 connections) — `server/services/npc_startup_service.py`
- **._warmup_room_cache_for_arena()** (3 connections) — `server/services/npc_startup_service.py`
- **test_npc_startup_service_accepts_injected_async_persistence()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **NPC Startup Service for MythosMUD. This module provides automatic NPC spawning…** (1 connections) — `server/services/npc_startup_service.py`
- *... and 11 more nodes in this community*

## Relationships

- [create_app](create_app.md) (34 shared connections)
- [CombatInstance](CombatInstance.md) (4 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (3 shared connections)
- [Room](Room.md) (3 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)
- [overrides](overrides.md) (1 shared connections)

## Source Files

- `server/services/npc_startup_service.py`
- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 92 (75%)
- INFERRED: 31 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*