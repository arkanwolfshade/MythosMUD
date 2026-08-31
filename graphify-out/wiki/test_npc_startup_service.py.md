# test_npc_startup_service.py

> 25 nodes

## Key Concepts

- **test_npc_startup_service.py** (38 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **npc_startup_service()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_exception()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_container()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_spawns_each_spawned_definition()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_no_spawn_room()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone_case_insensitive()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone_unknown()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_npc_startup_service_accepts_injected_async_persistence()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_npc_startup_service_init()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_arena_room_ids()** (2 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **fixture** (1 connections)
- **Unit tests for NPC startup service. Tests the NPCStartupService class.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() returns correct room for known sub-zone.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() returns None for unknown sub-zone.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() is case insensitive.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **#679: NPCStartupService no longer reaches ApplicationContainer.get_instance()…** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() handles missing spawn room.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Create an NPCStartupService instance.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test ARENA_ROOM_IDS defines 121 arena rooms (11x11) and includes center.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles exceptions gracefully.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles no async_persistence available.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test NPCStartupService initialization.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **One arena instance per definition_id present in required/optional spawned_npcs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [asyncio](asyncio.md) (17 shared connections)
- [NPCStartupService](NPCStartupService.md) (12 shared connections)
- [_errors_len](_errors_len.md) (6 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [test_spawn_required_npcs_success](test_spawn_required_npcs_success.md) (1 shared connections)
- [test_spawn_required_npcs_spawn_failure](test_spawn_required_npcs_spawn_failure.md) (1 shared connections)
- [test_determine_spawn_room_room_id_not_found](test_determine_spawn_room_room_id_not_found.md) (1 shared connections)
- [test_spawn_npcs_on_startup_with_optional_npcs](test_spawn_npcs_on_startup_with_optional_npcs.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 56 (88%)
- INFERRED: 8 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*