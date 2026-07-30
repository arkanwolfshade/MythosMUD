# login grace period

> 138 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (52 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (32 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_login_grace_period.py** (24 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **test_login_grace_period_flow.py** (18 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_expiration_handler()** (11 connections) — `server/realtime/login_grace_period.py`
- **test_combat_grace_period.py** (11 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **UUID** (9 connections)
- **Any** (8 connections)
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_task()** (7 connections) — `server/realtime/login_grace_period.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **test_warded_indicator_removed_after_expiration()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_both_linkdead_and_warded_indicators()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **_trigger_room_occupants_update()** (5 connections) — `server/realtime/login_grace_period.py`
- **.__init__()** (5 connections) — `server/realtime/player_occupant_processor.py`
- **UUID** (5 connections)
- **test_grace_period_expires_after_duration()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- *... and 113 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (16 shared connections)
- [Any](Any.md) (16 shared connections)
- [look player](look_player.md) (10 shared connections)
- [process all status effects()](process_all_status_effects%28%29.md) (9 shared connections)
- [container websocket events](container_websocket_events.md) (8 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (7 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [look room](look_room.md) (6 shared connections)
- [UUID](UUID.md) (6 shared connections)
- [.state()](state%28%29.md) (6 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (6 shared connections)
- [world](world.md) (4 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`
- `server/realtime/player_occupant_processor.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 586 (99%)
- INFERRED: 7 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*