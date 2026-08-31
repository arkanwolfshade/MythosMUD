# asyncio

> 27 nodes

## Key Concepts

- **asyncio** (26 connections)
- **test_determine_spawn_room_fallback()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_fallback_not_found()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_no_persistence()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_sub_zone_room_not_found()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_with_room_id()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_determine_spawn_room_with_sub_zone()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_no_prior_spawns_returns_empty()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_skips_unknown_definition_id()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup_with_required_npcs()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_no_probability_attribute()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_skips_low_probability()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_with_probability()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() spawns based on probability.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() skips NPCs with low probability.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() uses NPC's room_id when available.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() uses sub_zone default when room_id not available.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() uses fallback room when no other option.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() returns None when persistence not available.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() handles NPCs without spawn_probability attribute.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() handles sub-zone default room not found.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _determine_spawn_room() returns None when fallback room not found.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Arena pass is skipped when required/optional passes spawned nothing.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() processes startup spawning.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- *... and 2 more nodes in this community*

## Relationships

- [test_npc_startup_service.py](test_npc_startup_service.py.md) (17 shared connections)
- [NPCStartupService](NPCStartupService.md) (13 shared connections)
- [_errors_len](_errors_len.md) (5 shared connections)
- [test_determine_spawn_room_room_id_not_found](test_determine_spawn_room_room_id_not_found.md) (1 shared connections)
- [test_spawn_npcs_on_startup_with_optional_npcs](test_spawn_npcs_on_startup_with_optional_npcs.md) (1 shared connections)
- [test_spawn_required_npcs_spawn_failure](test_spawn_required_npcs_spawn_failure.md) (1 shared connections)
- [test_spawn_required_npcs_success](test_spawn_required_npcs_success.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 52 (80%)
- INFERRED: 13 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*