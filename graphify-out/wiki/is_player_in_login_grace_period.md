# is_player_in_login_grace_period

> 144 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (51 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (43 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_visual_indicator.py** (29 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
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
- **asyncio** (8 connections)
- **_grace_period_task()** (7 connections) — `server/realtime/login_grace_period.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_expires_after_duration()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_both_linkdead_and_warded_indicators()** (7 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_warded_indicator_removed_after_expiration()** (7 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **Protocol** (7 connections)
- *... and 119 more nodes in this community*

## Relationships

- [GameStateProvider](GameStateProvider.md) (10 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (9 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (7 shared connections)
- [test_look_player.py](test_look_player.py.md) (6 shared connections)
- [test_websocket_room_updates.py](test_websocket_room_updates.py.md) (6 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (6 shared connections)
- [SpellEffects](SpellEffects.md) (6 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (5 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (5 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (5 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (4 shared connections)
- [CombatService](CombatService.md) (4 shared connections)

## Source Files

- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 373 (96%)
- INFERRED: 14 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*