# login_grace_period.py

> 25 nodes

## Key Concepts

- **login_grace_period.py** (40 connections) — `server/realtime/login_grace_period.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **UUID** (11 connections)
- **handle_login_grace_period_expiration()** (10 connections) — `server/realtime/login_grace_period.py`
- **_as_grace()** (9 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_task()** (7 connections) — `server/realtime/login_grace_period.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **Protocol** (7 connections)
- **_trigger_room_occupants_update()** (5 connections) — `server/realtime/login_grace_period.py`
- **_GraceManager** (4 connections) — `server/realtime/login_grace_period.py`
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
- **Handle grace period expiration - remove tracking and trigger updates.** (1 connections) — `server/realtime/login_grace_period.py`
- **Internal task that waits for grace period duration and handles expiration.** (1 connections) — `server/realtime/login_grace_period.py`
- **Cancel login grace period for a player (if needed). For effect-based grace…** (1 connections) — `server/realtime/login_grace_period.py`
- **Remove player from grace period tracking dictionaries.** (1 connections) — `server/realtime/login_grace_period.py`
- **Trigger room occupants update after grace period expiration.** (1 connections) — `server/realtime/login_grace_period.py`

## Relationships

- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (19 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_login_grace_period.py](test_login_grace_period.py.md) (5 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (2 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (1 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [test_look_player.py](test_look_player.py.md) (1 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (1 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (1 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (1 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (1 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (1 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`

## Audit Trail

- EXTRACTED: 92 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*