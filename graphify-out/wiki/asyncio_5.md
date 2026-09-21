# asyncio

> 25 nodes

## Key Concepts

- **asyncio** (26 connections)
- **test_determine_spawn_room_exception()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback_not_found()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_container()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_room_id_not_found()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_sub_zone_room_not_found()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_spawns_each_spawned_definition()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup_with_required_npcs()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_no_probability_attribute()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_no_spawn_room()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_skips_low_probability()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() skips NPCs with low probability.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() uses fallback room when no other option.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() handles missing spawn room.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() handles NPCs without spawn_probability attribute.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles room_id not found in database.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles sub-zone default room not found.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() returns None when fallback room not found.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles exceptions gracefully.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles no async_persistence available.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **One arena instance per definition_id present in required/optional spawned_npcs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() processes startup spawning.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() spawns required NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [test_npc_startup_service.py](test_npc_startup_service.py.md) (17 shared connections)
- [NPCStartupService](NPCStartupService.md) (12 shared connections)
- [_errors_len](_errors_len.md) (5 shared connections)
- [test_determine_spawn_room_with_sub_zone](test_determine_spawn_room_with_sub_zone.md) (1 shared connections)
- [test_spawn_arena_npcs_no_prior_spawns_returns_empty](test_spawn_arena_npcs_no_prior_spawns_returns_empty.md) (1 shared connections)
- [test_spawn_arena_npcs_skips_unknown_definition_id](test_spawn_arena_npcs_skips_unknown_definition_id.md) (1 shared connections)
- [test_spawn_required_npcs_spawn_failure](test_spawn_required_npcs_spawn_failure.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 50 (81%)
- INFERRED: 12 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*