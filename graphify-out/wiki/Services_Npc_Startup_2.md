# Services Npc Startup

> 15 nodes · cohesion 0.13

## Key Concepts

- **NPCStartupService** (32 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **npc_startup_service()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone_unknown()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_no_prior_spawns_returns_empty()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup_with_optional_npcs()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_no_spawn_room()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_skips_low_probability()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_with_probability()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() spawns based on probability.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() skips NPCs with low probability.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() returns None for unknown sub-zone.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() handles missing spawn room.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Create an NPCStartupService instance.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() spawns optional NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Arena pass is skipped when required/optional passes spawned nothing.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [[Services Npc Startup]] (31 shared connections)
- [[NPC Occupant Verification]] (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 59 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
