# is_player_in_login_grace_period

> 153 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (51 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (45 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (43 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_visual_indicator.py** (28 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_login_grace_period.py** (25 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **get_login_grace_period_remaining()** (22 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period_flow.py** (21 connections) — `server/tests/integration/test_login_grace_period_flow.py`
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
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **_login_grace_period_seconds()** (7 connections) — `server/realtime/login_grace_period.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **_try_start_effect_based_grace()** (7 connections) — `server/realtime/login_grace_period.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_expires_after_duration()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- *... and 128 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (11 shared connections)
- [test_player_occupant_processor.py](test_player_occupant_processor.py.md) (9 shared connections)
- [GameStateProvider](GameStateProvider.md) (8 shared connections)
- [CombatParticipant](CombatParticipant.md) (8 shared connections)
- [players.py](players.py.md) (7 shared connections)
- [test_look_player.py](test_look_player.py.md) (6 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (6 shared connections)
- [PlayerNameExtractor](PlayerNameExtractor.md) (6 shared connections)
- [game_state_provider.py](game_state_provider.py.md) (4 shared connections)
- [.state](state.md) (4 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (4 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 389 (96%)
- INFERRED: 17 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*