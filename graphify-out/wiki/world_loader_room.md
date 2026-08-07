# world loader room

> 22 nodes

## Key Concepts

- **test_npc_startup_service.py** (39 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_npc_startup_service_init()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_required_npcs_success()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_with_probability()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_skips_low_probability()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_get_default_room_for_sub_zone_case_insensitive()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_optional_npcs_no_probability_attribute()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_npcs_on_startup_with_optional_npcs()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_no_prior_spawns_returns_empty()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_spawn_arena_npcs_skips_unknown_definition_id()** (3 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **test_arena_room_ids()** (2 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Unit tests for NPC startup service.  Tests the NPCStartupService class.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test ARENA_ROOM_IDS defines 121 arena rooms (11x11) and includes center.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test NPCStartupService initialization.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_required_npcs() successfully spawns required NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() spawns based on probability.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() skips NPCs with low probability.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _get_default_room_for_sub_zone() is case insensitive.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test _spawn_optional_npcs() handles NPCs without spawn_probability attribute.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Test spawn_npcs_on_startup() spawns optional NPCs.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Arena pass is skipped when required/optional passes spawned nothing.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`
- **Stale definition_id in spawned_npcs that is not in definitions list is ignored.** (1 connections) — `server/tests/unit/services/test_npc_startup_service.py`

## Relationships

- [room validator path](room_validator_path.md) (18 shared connections)
- [realtime player connection](realtime_player_connection.md) (11 shared connections)
- [realtime dead letter](realtime_dead_letter.md) (6 shared connections)
- [room look commands](room_look_commands.md) (1 shared connections)
- [aggro threat services](aggro_threat_services.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_startup_service.py`

## Audit Trail

- EXTRACTED: 79 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*