# is_player_in_login_grace_period

> 171 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (51 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (45 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (43 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_login_grace_period.py** (25 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **get_login_grace_period_remaining()** (22 connections) — `server/realtime/login_grace_period.py`
- **PlayerOccupantProcessor** (21 connections) — `server/realtime/player_occupant_processor.py`
- **test_login_grace_period_flow.py** (21 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **player_occupant_processor.py** (15 connections) — `server/realtime/player_occupant_processor.py`
- **FakeGraceManager** (13 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **cancel_login_grace_period()** (13 connections) — `server/realtime/login_grace_period.py`
- **UUID** (13 connections)
- **test_combat_grace_period.py** (11 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **handle_login_grace_period_expiration()** (10 connections) — `server/realtime/login_grace_period.py`
- **asyncio** (10 connections)
- **_as_grace()** (9 connections) — `server/realtime/login_grace_period.py`
- **asyncio** (9 connections)
- **_grace_period_task()** (8 connections) — `server/realtime/login_grace_period.py`
- **asyncio** (8 connections)
- **_login_grace_period_seconds()** (7 connections) — `server/realtime/login_grace_period.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **_try_start_effect_based_grace()** (7 connections) — `server/realtime/login_grace_period.py`
- **._create_player_occupant_info()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **.process_players_for_occupants()** (7 connections) — `server/realtime/player_occupant_processor.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- *... and 146 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (19 shared connections)
- [test_look_player.py](test_look_player.py.md) (10 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (8 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [websocket_room_updates.py](websocket_room_updates.py.md) (7 shared connections)
- [GameStateProvider](GameStateProvider.md) (6 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (5 shared connections)
- [CombatParticipantData](CombatParticipantData.md) (4 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (4 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`
- `server/realtime/player_occupant_processor.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/realtime/test_visual_indicator.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 431 (96%)
- INFERRED: 19 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*