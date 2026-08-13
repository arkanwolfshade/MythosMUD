# is_player_in_login_grace_period

> 172 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (52 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (32 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **test_login_grace_period.py** (25 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **game_state_provider.py** (21 connections) — `server/realtime/integration/game_state_provider.py`
- **test_login_grace_period_flow.py** (19 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **UUID** (14 connections)
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **_grace_period_expiration_handler()** (11 connections) — `server/realtime/login_grace_period.py`
- **test_combat_grace_period.py** (11 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **asyncio** (10 connections)
- **.connection_manager()** (9 connections) — `server/realtime/nats_message_handler.py`
- **UUID** (9 connections)
- **asyncio** (9 connections)
- **._get_player_data_for_client()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **Any** (8 connections)
- **asyncio** (8 connections)
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 147 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (12 shared connections)
- [TargetMatch](TargetMatch.md) (10 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (9 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (9 shared connections)
- [CombatService](CombatService.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [test_look_player.py](test_look_player.py.md) (6 shared connections)
- [test_look_room.py](test_look_room.py.md) (6 shared connections)
- [AttributeError](AttributeError.md) (6 shared connections)
- [PlayerCombatService](PlayerCombatService.md) (6 shared connections)
- [is_player_in_grace_period](is_player_in_grace_period.md) (5 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (5 shared connections)

## Source Files

- `server/realtime/integration/__init__.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 449 (97%)
- INFERRED: 15 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*