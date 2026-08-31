# is_player_in_login_grace_period

> 79 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (51 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (43 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_flow.py** (22 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **FakeGraceManager** (13 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **UUID** (13 connections)
- **test_combat_grace_period.py** (12 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **handle_login_grace_period_expiration()** (10 connections) — `server/realtime/login_grace_period.py`
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
- **test_grace_period_remaining_time_decreases()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_start_time_tracking()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_start_grace_period_removes_from_combat()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- *... and 54 more nodes in this community*

## Relationships

- [test_login_grace_period.py](test_login_grace_period.py.md) (24 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (13 shared connections)
- [GameStateProvider](GameStateProvider.md) (7 shared connections)
- [PlayerService](PlayerService.md) (7 shared connections)
- [test_combat_attack_handler.py](test_combat_attack_handler.py.md) (6 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (5 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (5 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [NPCCombatIntegrationBase](NPCCombatIntegrationBase.md) (4 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (4 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (4 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 272 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*