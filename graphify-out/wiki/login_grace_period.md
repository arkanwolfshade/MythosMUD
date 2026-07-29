# login grace period

> 101 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (50 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (31 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period.py** (24 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_flow.py** (18 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_expiration_handler()** (11 connections) — `server/realtime/login_grace_period.py`
- **test_combat_grace_period.py** (11 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **UUID** (9 connections)
- **Any** (8 connections)
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_task()** (7 connections) — `server/realtime/login_grace_period.py`
- **test_warded_indicator_removed_after_expiration()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **_trigger_room_occupants_update()** (5 connections) — `server/realtime/login_grace_period.py`
- **test_grace_period_expires_after_duration()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_warded_indicator_in_game_state_provider()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_start_grace_period_removes_from_combat()** (4 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_blocks_combat_initiation()** (4 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_remaining_time_decreases()** (4 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_start_time_tracking()** (4 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_attack_command_blocked_during_grace_period()** (4 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- *... and 76 more nodes in this community*

## Relationships

- [disconnect grace period](disconnect_grace_period.md) (12 shared connections)
- [main()](main%28%29.md) (9 shared connections)
- [Spell Targeting](Spell_Targeting.md) (9 shared connections)
- [Connection Manager](Connection_Manager.md) (7 shared connections)
- [game tick processing](game_tick_processing.md) (7 shared connections)
- [Player Position Service](Player_Position_Service.md) (6 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (5 shared connections)
- [.state()](state%28%29.md) (5 shared connections)
- [get app instance()](get_app_instance%28%29.md) (4 shared connections)
- [look player](look_player.md) (3 shared connections)
- [look room](look_room.md) (3 shared connections)
- [Any](Any.md) (3 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 430 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*