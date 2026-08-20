# login_grace_period.py

> 29 nodes

## Key Concepts

- **login_grace_period.py** (43 connections) — `server/realtime/login_grace_period.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **UUID** (13 connections)
- **handle_login_grace_period_expiration()** (10 connections) — `server/realtime/login_grace_period.py`
- **_as_grace()** (9 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_task()** (7 connections) — `server/realtime/login_grace_period.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **Protocol** (7 connections)
- **_trigger_room_occupants_update()** (6 connections) — `server/realtime/login_grace_period.py`
- **_try_start_effect_based_grace()** (6 connections) — `server/realtime/login_grace_period.py`
- **_GraceManager** (5 connections) — `server/realtime/login_grace_period.py`
- **_send_occupants_update_via_app()** (4 connections) — `server/realtime/login_grace_period.py`
- **_EffectPersistence** (3 connections) — `server/realtime/login_grace_period.py`
- **_GracePlayer** (3 connections) — `server/realtime/login_grace_period.py`
- **_OccupantsHandler** (3 connections) — `server/realtime/login_grace_period.py`
- **.get_player()** (3 connections) — `server/realtime/login_grace_period.py`
- **_GraceApp** (2 connections) — `server/realtime/login_grace_period.py`
- **_GraceAppState** (2 connections) — `server/realtime/login_grace_period.py`
- **_GraceContainer** (2 connections) — `server/realtime/login_grace_period.py`
- **.add_player_effect()** (2 connections) — `server/realtime/login_grace_period.py`
- **.send_room_occupants_update()** (1 connections) — `server/realtime/login_grace_period.py`
- **Login grace period management for MythosMUD. This module handles the 10-second…** (1 connections) — `server/realtime/login_grace_period.py`
- **Trigger room occupants update after grace period expiration.** (1 connections) — `server/realtime/login_grace_period.py`
- **Handle grace period expiration - remove tracking and trigger updates.** (1 connections) — `server/realtime/login_grace_period.py`
- **Internal task that waits for grace period duration and handles expiration.** (1 connections) — `server/realtime/login_grace_period.py`
- *... and 4 more nodes in this community*

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (22 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (4 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (3 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [User](User.md) (1 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (1 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (1 shared connections)
- [test_look_player.py](test_look_player.py.md) (1 shared connections)
- [server/models/game.py](server-models-game.py.md) (1 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`

## Audit Trail

- EXTRACTED: 102 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*