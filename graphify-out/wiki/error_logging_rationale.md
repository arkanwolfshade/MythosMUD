# error logging rationale

> 40 nodes

## Key Concepts

- **AggressiveMobNPC** (33 connections) — `server/npc/aggressive_mob_npc.py`
- **test_aggressive_mob_npc.py** (22 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **_make_aggro()** (13 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **.__init__()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._setup_aggressive_mob_behavior_rules()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **.flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
- **._handle_flee()** (3 connections) — `server/npc/aggressive_mob_npc.py`
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
- **test_attack_via_combat_integration_none_when_missing()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_attack_via_event_bus_without_running_loop()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_attack_via_dropped_without_loop_or_bus()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_attack_via_create_task_with_running_loop()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_attack_target_fallback_publishes_event()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- **test_attack_target_error_returns_false()** (2 connections) — `server/tests/unit/npc/test_aggressive_mob_npc.py`
- *... and 15 more nodes in this community*

## Relationships

- [services nats service](services_nats_service.md) (5 shared connections)
- [commands command validation](commands_command_validation.md) (5 shared connections)
- [game magic regeneration](game_magic_regeneration.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (2 shared connections)
- [headers middleware security](headers_middleware_security.md) (2 shared connections)
- [lucidity event services](lucidity_event_services.md) (1 shared connections)
- [room look commands](room_look_commands.md) (1 shared connections)
- [command models moderation](command_models_moderation.md) (1 shared connections)

## Source Files

- `server/npc/aggressive_mob_npc.py`
- `server/tests/unit/npc/test_aggressive_mob_npc.py`

## Audit Trail

- EXTRACTED: 135 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*