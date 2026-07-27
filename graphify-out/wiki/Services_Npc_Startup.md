# Services Npc Startup

> 16 nodes · cohesion 0.12

## Key Concepts

- **_assign_container_get_instance()** (12 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_exception()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback_not_found()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_persistence()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_room_id_not_found()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_with_sub_zone()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_spawns_each_spawned_definition()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() uses sub_zone default when room_id not available.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() uses fallback room when no other option.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Attach a typed get_instance mock to a patched ApplicationContainer.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() returns None when persistence not available.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles room_id not found in database.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() returns None when fallback room not found.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles exceptions gracefully.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **One arena instance per definition_id present in required/optional spawned_npcs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [[Services Npc Startup]] (18 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 48 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
