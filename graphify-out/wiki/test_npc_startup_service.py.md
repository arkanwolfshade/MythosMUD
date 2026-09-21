# test_npc_startup_service.py

> 24 nodes

## Key Concepts

- **test_npc_startup_service.py** (37 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_persistence()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_with_room_id()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup_with_optional_npcs()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_with_probability()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_required_npcs_success()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone_case_insensitive()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone_unknown()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_npc_startup_service_accepts_injected_async_persistence()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_npc_startup_service_init()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_arena_room_ids()** (2 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Unit tests for NPC startup service. Tests the NPCStartupService class.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_required_npcs() successfully spawns required NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() spawns based on probability.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() uses NPC's room_id when available.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() returns None when persistence not available.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() returns correct room for known sub-zone.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() returns None for unknown sub-zone.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() is case insensitive.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **#679: NPCStartupService no longer reaches ApplicationContainer.get_instance()…** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test ARENA_ROOM_IDS defines 121 arena rooms (11x11) and includes center.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() spawns optional NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test NPCStartupService initialization.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [asyncio](asyncio.md) (17 shared connections)
- [NPCStartupService](NPCStartupService.md) (11 shared connections)
- [_errors_len](_errors_len.md) (6 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [test_spawn_required_npcs_spawn_failure](test_spawn_required_npcs_spawn_failure.md) (1 shared connections)
- [test_determine_spawn_room_with_sub_zone](test_determine_spawn_room_with_sub_zone.md) (1 shared connections)
- [npc_startup_service](npc_startup_service.md) (1 shared connections)
- [test_spawn_arena_npcs_no_prior_spawns_returns_empty](test_spawn_arena_npcs_no_prior_spawns_returns_empty.md) (1 shared connections)
- [test_spawn_arena_npcs_skips_unknown_definition_id](test_spawn_arena_npcs_skips_unknown_definition_id.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 54 (86%)
- INFERRED: 9 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*