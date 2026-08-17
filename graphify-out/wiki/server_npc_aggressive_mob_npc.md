# server npc aggressive mob npc

> 14 nodes

## Key Concepts

- **AggressiveMobNPC** (31 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **test_enrich_behavior_context_swallows_compute_errors()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_get_attack_damage_invalid_string_falls_back_to_one()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_hunt_target_avoids_duplicate_ids()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/aggressive_mob_npc.py`
- **Patrol the NPC's territory.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Aggressive mob NPC type with hunting and territorial behaviors.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Handle patrolling territory action.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Get aggressive mob-specific behavior rules.** (1 connections) — `server/npc/aggressive_mob_npc.py`
- **Non-digit attack_damage string in behavior_config falls back to 1.** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **hunt_target appends each id once; repeated calls keep a single _targets entry.** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **Warnings path: failure in _compute_player_context must not raise.** (1 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Relationships

- [server npc aggressive mob npc](server_npc_aggressive_mob_npc.md) (14 shared connections)
- [server tests unit npc test](server_tests_unit_npc_test.md) (9 shared connections)
- [server events event bus eventbus](server_events_event_bus_eventbus.md) (3 shared connections)
- [server events event bus](server_events_event_bus.md) (1 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 31 (76%)
- INFERRED: 10 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*