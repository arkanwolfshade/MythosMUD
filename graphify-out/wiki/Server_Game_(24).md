# Server Game (24)

> 42 nodes

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
- **.get_room_by_id()** (3 connections) — `server/game/magic/spell_effects.py`
- *... and 17 more nodes in this community*

## Relationships

- [Server Game (2)](Server_Game_%282%29.md) (18 shared connections)
- [Server Models (6)](Server_Models_%286%29.md) (8 shared connections)
- [Server Models (13)](Server_Models_%2813%29.md) (7 shared connections)
- [Server Game (7)](Server_Game_%287%29.md) (4 shared connections)
- [Server Realtime (8)](Server_Realtime_%288%29.md) (3 shared connections)
- [Server Services (28)](Server_Services_%2828%29.md) (2 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)
- [Server Services (29)](Server_Services_%2829%29.md) (1 shared connections)
- [Server Game (4)](Server_Game_%284%29.md) (1 shared connections)
- [Server Models (14)](Server_Models_%2814%29.md) (1 shared connections)
- [Server Models (36)](Server_Models_%2836%29.md) (1 shared connections)
- [Server Models (32)](Server_Models_%2832%29.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`

## Audit Trail

- EXTRACTED: 220 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*