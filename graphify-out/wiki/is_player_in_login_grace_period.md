# is_player_in_login_grace_period

> 128 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (51 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (43 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period.py** (26 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_login_grace_period_flow.py** (22 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **FakeGraceManager** (13 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **UUID** (13 connections)
- **test_combat_grace_period.py** (12 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **handle_login_grace_period_expiration()** (10 connections) — `server/realtime/login_grace_period.py`
- **asyncio** (10 connections)
- **_as_grace()** (9 connections) — `server/realtime/login_grace_period.py`
- **asyncio** (9 connections)
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **_grace_period_task()** (7 connections) — `server/realtime/login_grace_period.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_expires_after_duration()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **Protocol** (7 connections)
- **_trigger_room_occupants_update()** (6 connections) — `server/realtime/login_grace_period.py`
- **_try_start_effect_based_grace()** (6 connections) — `server/realtime/login_grace_period.py`
- **test_grace_period_blocks_combat_initiation()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- *... and 103 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [test_look_player.py](test_look_player.py.md) (9 shared connections)
- [PlayerOccupantProcessor](PlayerOccupantProcessor.md) (8 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [.state](state.md) (5 shared connections)
- [build_event](build_event.md) (5 shared connections)
- [CombatParticipant](CombatParticipant.md) (5 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (3 shared connections)
- [occupant_display.py](occupant_display.py.md) (3 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (3 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 336 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*