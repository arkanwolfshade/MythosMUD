# is_player_in_login_grace_period

> 97 nodes

## Key Concepts

- **is_player_in_login_grace_period()** (51 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **test_login_grace_period.py** (26 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **test_login_grace_period_flow.py** (22 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **get_login_grace_period_remaining()** (21 connections) — `server/realtime/login_grace_period.py`
- **FakeGraceManager** (13 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_combat_grace_period.py** (12 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **asyncio** (10 connections)
- **asyncio** (9 connections)
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_expires_after_duration()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_blocks_combat_initiation()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_remaining_time_decreases()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_start_time_tracking()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_start_grace_period_removes_from_combat()** (6 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_warded_indicator_in_game_state_provider()** (6 connections) — `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- **test_attack_command_blocked_during_grace_period()** (5 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_attack_command_works_when_not_in_grace_period()** (5 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_cancel_login_grace_period()** (5 connections) — `server/tests/unit/realtime/test_login_grace_period.py`
- **mock_connection_manager()** (4 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_attack_command_allowed_after_grace_period()** (4 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- **test_attack_command_blocked_when_incapacitated()** (4 connections) — `server/tests/unit/commands/test_combat_grace_period.py`
- *... and 72 more nodes in this community*

## Relationships

- [login_grace_period.py](login_grace_period.py.md) (22 shared connections)
- [test_login_grace_period_visual_indicator.py](test_login_grace_period_visual_indicator.py.md) (12 shared connections)
- [test_game_state_provider.py](test_game_state_provider.py.md) (9 shared connections)
- [User](User.md) (6 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (5 shared connections)
- [game_tick_processing.py](game_tick_processing.py.md) (4 shared connections)
- [CombatCommandHandler](CombatCommandHandler.md) (4 shared connections)
- [server/config/__init__.py](server-config-__init__.py.md) (3 shared connections)
- [CombatService](CombatService.md) (3 shared connections)
- [npc_combat_grace.py](npc_combat_grace.py.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (2 shared connections)

## Source Files

- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`

## Audit Trail

- EXTRACTED: 253 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*