# Player Creation Service

> 44 nodes

## Key Concepts

- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **run_flee_effect()** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **spell_effect_flee.py** (17 connections) — `server/game/magic/spell_effect_flee.py`
- **Any** (10 connections)
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (8 connections)
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **._process_status_effect()** (6 connections) — `server/game/magic/spell_effects.py`
- **UUID** (6 connections)
- **_parse_status_effect_metadata()** (6 connections) — `server/game/magic/spell_effects_status.py`
- **_flee_effect_validate_room_exits()** (5 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_services_available()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_not_in_combat_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_success_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_failure_response()** (4 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_invalid_target_type_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_services_unavailable_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_invalid_target_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- **_flee_effect_room_error_response()** (3 connections) — `server/game/magic/spell_effect_flee.py`
- *... and 19 more nodes in this community*

## Relationships

- [Magic Service Bundle](Magic_Service_Bundle.md) (15 shared connections)
- [Player Respawn Service](Player_Respawn_Service.md) (9 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (9 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (5 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (4 shared connections)
- [Combat Death Handling](Combat_Death_Handling.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (1 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (1 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`

## Audit Trail

- EXTRACTED: 227 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*