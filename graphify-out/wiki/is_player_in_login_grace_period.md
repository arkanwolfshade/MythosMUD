# is_player_in_login_grace_period

> 126 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (52 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (32 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_login_grace_period.py** (25 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_flow.py** (19 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **_grace_period_expiration_handler()** (11 connections) — `server/realtime/login_grace_period.py`
- **test_combat_grace_period.py** (11 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **asyncio** (10 connections)
- **UUID** (9 connections)
- **asyncio** (9 connections)
- **Any** (8 connections)
- **asyncio** (8 connections)
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **_grace_period_task()** (7 connections) — `server/realtime/login_grace_period.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **test_both_linkdead_and_warded_indicators()** (7 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_removed_after_expiration()** (7 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_expires_after_duration()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_warded_indicator_in_game_state_provider()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- *... and 101 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (12 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (9 shared connections)
- [GameStateProvider](GameStateProvider.md) (8 shared connections)
- [PlayerService](PlayerService.md) (7 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (7 shared connections)
- [test_look_player.py](test_look_player.py.md) (6 shared connections)
- [test_look_room.py](test_look_room.py.md) (6 shared connections)
- [combat_service.py](combat_service.py.md) (6 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (6 shared connections)
- [test_damage_grace_period.py](test_damage_grace_period.py.md) (6 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (6 shared connections)
- [CombatAttackHandler](CombatAttackHandler.md) (5 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 578 (99%)
- INFERRED: 6 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*