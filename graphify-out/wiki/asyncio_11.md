# asyncio

> 21 nodes

## Key Concepts

- **asyncio** (26 connections)
- **test_spawn_arena_npcs_spawns_each_spawned_definition()** (5 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_skips_unknown_definition_id()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup_with_optional_npcs()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup_with_required_npcs()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_no_probability_attribute()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_no_spawn_room()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_skips_low_probability()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_required_npcs_spawn_failure()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_required_npcs_success()** (4 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_required_npcs() successfully spawns required NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_required_npcs() handles spawn failures.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() skips NPCs with low probability.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() handles missing spawn room.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() handles NPCs without spawn_probability attribute.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() spawns optional NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **One arena instance per definition_id present in required/optional spawned_npcs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() processes startup spawning.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Stale definition_id in spawned_npcs that is not in definitions list is ignored.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() spawns required NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [test_npc_startup_service.py](test_npc_startup_service.py.md) (12 shared connections)
- [NPCStartupService](NPCStartupService.md) (10 shared connections)
- [mock_container](mock_container.md) (10 shared connections)
- [_errors_len](_errors_len.md) (5 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 47 (82%)
- INFERRED: 10 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*