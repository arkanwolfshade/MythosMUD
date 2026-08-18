# server npc aggressive mob npc

> 12 nodes

## Key Concepts

- **AggressiveMobNPC** (31 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_hunt_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.hunt_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **test_get_attack_damage_invalid_string_falls_back_to_one()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_hunt_target_avoids_duplicate_ids()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/aggressive_mob_npc.py`
- **Hunt a specific target.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Handle hunting target action.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Aggressive mob NPC type with hunting and territorial behaviors.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Get aggressive mob-specific behavior rules.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Non-digit attack_damage string in behavior_config falls back to 1.** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **hunt_target appends each id once; repeated calls keep a single _targets entry.** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Relationships

- [server npc aggressive mob npc](server_npc_aggressive_mob_npc.md) (13 shared connections)
- [server tests unit npc test](server_tests_unit_npc_test.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server npc npc base npcbase](server_npc_npc_base_npcbase.md) (2 shared connections)
- [server models room py any](server_models_room_py_any.md) (1 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 38 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*