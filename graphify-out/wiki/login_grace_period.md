# login grace period

> 116 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (52 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (32 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
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
- **test_both_linkdead_and_warded_indicators()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **_trigger_room_occupants_update()** (5 connections) — `server/realtime/login_grace_period.py`
- **test_grace_period_expires_after_duration()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (5 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_warded_indicator_in_game_state_provider()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_player_occupant_processor()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_start_grace_period_removes_from_combat()** (4 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_blocks_combat_initiation()** (4 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- *... and 91 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (11 shared connections)
- [world](world.md) (10 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (7 shared connections)
- [Protocol](Protocol.md) (7 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [look player](look_player.md) (6 shared connections)
- [look room](look_room.md) (6 shared connections)
- [.check and interrupt rest()](check_and_interrupt_rest%28%29.md) (6 shared connections)
- [.state()](state%28%29.md) (6 shared connections)
- [test combat persistence handler](test_combat_persistence_handler.md) (6 shared connections)
- [. init ()](_init_%28%29.md) (5 shared connections)
- [PanelManager](PanelManager.md) (4 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 493 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*