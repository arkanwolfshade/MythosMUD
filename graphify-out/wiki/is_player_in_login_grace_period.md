# is_player_in_login_grace_period

> 149 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (50 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (40 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_visual_indicator.py** (29 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **GameStateProvider** (26 connections) — `server/realtime/integration/game_state_provider.py`
- **game_state_provider.py** (22 connections) — `server/realtime/integration/game_state_provider.py`
- **test_login_grace_period_flow.py** (22 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **UUID** (14 connections)
- **FakeGraceManager** (13 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **Any** (13 connections)
- **.send_initial_game_state()** (12 connections) — `server/realtime/integration/game_state_provider.py`
- **test_combat_grace_period.py** (12 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **UUID** (11 connections)
- **handle_login_grace_period_expiration()** (10 connections) — `server/realtime/login_grace_period.py`
- **_as_grace()** (9 connections) — `server/realtime/login_grace_period.py`
- **.connection_manager()** (9 connections) — `server/realtime/nats_message_handler.py`
- **asyncio** (9 connections)
- **._get_player_data_for_client()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_player_name_with_grace_periods()** (8 connections) — `server/realtime/integration/game_state_provider.py`
- **asyncio** (8 connections)
- **._add_grace_period_indicators()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **._get_quest_log_for_client()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- *... and 124 more nodes in this community*

## Relationships

- [test_login_grace_period.py](test_login_grace_period.py.md) (22 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (9 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (7 shared connections)
- [PlayerService](PlayerService.md) (7 shared connections)
- [CombatInstance](CombatInstance.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [build_event](build_event.md) (6 shared connections)
- [test_look_player.py](test_look_player.py.md) (6 shared connections)
- [test_look_room.py](test_look_room.py.md) (6 shared connections)
- [TargetMatch](TargetMatch.md) (6 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (6 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (5 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/realtime/nats_message_handler.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 426 (95%)
- INFERRED: 24 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*