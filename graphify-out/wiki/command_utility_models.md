# command utility models

> 100 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (52 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (32 connections) — `server/realtime/login_grace_period.py`
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
- **test_attack_command_works_when_not_in_grace_period()** (4 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- *... and 75 more nodes in this community*

## Relationships

- [player occupant processor](player_occupant_processor.md) (12 shared connections)
- [NPC Combat](NPC_Combat.md) (10 shared connections)
- [tick game processing](tick_game_processing.md) (9 shared connections)
- [Item Instances](Item_Instances.md) (7 shared connections)
- [command inventory factories](command_inventory_factories.md) (6 shared connections)
- [realtime game state](realtime_game_state.md) (5 shared connections)
- [combat services turn](combat_services_turn.md) (4 shared connections)
- [look helpers commands](look_helpers_commands.md) (4 shared connections)
- [room websocket updates](room_websocket_updates.md) (4 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (4 shared connections)
- [command factories exploration](command_factories_exploration.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 426 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*