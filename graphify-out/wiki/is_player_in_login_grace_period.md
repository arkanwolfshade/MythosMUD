# is_player_in_login_grace_period

> 61 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (50 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_visual_indicator.py** (29 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **game_state_provider.py** (22 connections) — `server/realtime/integration/game_state_provider.py`
- **test_login_grace_period_flow.py** (22 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **FakeGraceManager** (13 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **asyncio** (9 connections)
- **asyncio** (8 connections)
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_expires_after_duration()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_both_linkdead_and_warded_indicators()** (7 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_removed_after_expiration()** (7 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_grace_period_blocks_combat_initiation()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_remaining_time_decreases()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_start_time_tracking()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_start_grace_period_removes_from_combat()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_warded_indicator_in_game_state_provider()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_player_occupant_processor()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_look_player()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_look_room()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_in_websocket_room_updates()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_not_shown_for_reconnections()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- *... and 36 more nodes in this community*

## Relationships

- [login_grace_period.py](login_grace_period.py.md) (19 shared connections)
- [test_login_grace_period.py](test_login_grace_period.py.md) (17 shared connections)
- [GameStateProvider](GameStateProvider.md) (9 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_look_player.py](test_look_player.py.md) (5 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (5 shared connections)
- [test_damage_grace_period.py](test_damage_grace_period.py.md) (5 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (5 shared connections)
- [test_combat_grace_period.py](test_combat_grace_period.py.md) (4 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (3 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 236 (96%)
- INFERRED: 10 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*