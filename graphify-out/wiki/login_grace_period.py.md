# login_grace_period.py

> 35 nodes

## Key Concepts

- **login_grace_period.py** (43 connections) — `server/realtime/login_grace_period.py`
- **UUID** (13 connections)
- **occupant_display.py** (11 connections) — `server/realtime/occupant_display.py`
- **handle_login_grace_period_expiration()** (10 connections) — `server/realtime/login_grace_period.py`
- **format_occupant_display_name()** (10 connections) — `server/realtime/occupant_display.py`
- **_as_grace()** (9 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_task()** (7 connections) — `server/realtime/login_grace_period.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **Protocol** (7 connections)
- **_trigger_room_occupants_update()** (6 connections) — `server/realtime/login_grace_period.py`
- **_try_start_effect_based_grace()** (6 connections) — `server/realtime/login_grace_period.py`
- **_apply_grace_badges()** (6 connections) — `server/realtime/occupant_display.py`
- **_GraceManager** (5 connections) — `server/realtime/login_grace_period.py`
- **_send_occupants_update_via_app()** (4 connections) — `server/realtime/login_grace_period.py`
- **UUID** (4 connections)
- **_EffectPersistence** (3 connections) — `server/realtime/login_grace_period.py`
- **_GracePlayer** (3 connections) — `server/realtime/login_grace_period.py`
- **_OccupantsHandler** (3 connections) — `server/realtime/login_grace_period.py`
- **.get_player()** (3 connections) — `server/realtime/login_grace_period.py`
- **_parse_occupant_player_id()** (3 connections) — `server/realtime/occupant_display.py`
- **_GraceApp** (2 connections) — `server/realtime/login_grace_period.py`
- **_GraceAppState** (2 connections) — `server/realtime/login_grace_period.py`
- **_GraceContainer** (2 connections) — `server/realtime/login_grace_period.py`
- **.add_player_effect()** (2 connections) — `server/realtime/login_grace_period.py`
- **Any** (2 connections)
- *... and 10 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (22 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (4 shared connections)
- [test_look_room.py](test_look_room.py.md) (3 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [test_rest_and_grace_period.py](test_rest_and_grace_period.py.md) (2 shared connections)
- [combat_service_attack.py](combat_service_attack.py.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [npc_combat_integration_service.py](npc_combat_integration_service.py.md) (1 shared connections)
- [test_look_player.py](test_look_player.py.md) (1 shared connections)
- [run_flee_effect](run_flee_effect.md) (1 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`
- `server/realtime/occupant_display.py`

## Audit Trail

- EXTRACTED: 117 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*