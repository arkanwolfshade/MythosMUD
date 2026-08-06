# error logging rationale

> 52 nodes

## Key Concepts

- **AggressiveMobNPC** (33 connections) — `server/npc/aggressive_mob_npc.py`
- **test_aggressive_mob_npc.py** (22 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **_make_aggro()** (13 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **._enrich_behavior_context()** (4 connections) — `server/npc/aggressive_mob_npc.py`
- **.__init__()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._setup_aggressive_mob_behavior_rules()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._log_context_enriched()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.hunt_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_hunt_target()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_patrol_territory()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **test_enrich_behavior_context_sets_player_in_range_when_players_in_room()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_enrich_behavior_context_sets_false_when_no_players_in_room()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_enrich_behavior_context_handles_no_current_room()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_get_attack_damage_from_behavior_config()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_get_attack_damage_invalid_string_falls_back_to_one()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_hunt_target_avoids_duplicate_ids()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_enrich_behavior_context_swallows_compute_errors()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_flee_error_returns_false()** (3 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **.get_behavior_rules()** (2 connections) — `server/npc/aggressive_mob_npc.py`
- **test_get_behavior_rules_returns_engine_rules()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_get_attack_damage_bool_and_float()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_compute_player_context_without_service()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- *... and 27 more nodes in this community*

## Relationships

- [envelope event game](envelope_event_game.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [lucidity event services](lucidity_event_services.md) (2 shared connections)
- [services nats service](services_nats_service.md) (1 shared connections)
- [room sync service](room_sync_service.md) (1 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 160 (97%)
- INFERRED: 5 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*