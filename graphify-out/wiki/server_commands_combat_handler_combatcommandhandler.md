# server commands combat handler combatcommandhandler

> 185 nodes

## Key Concepts

- **CombatCommandHandler** (51 connections) — `server/commands/combat_handler.py`
- **is_player_in_login_grace_period()** (51 connections) — `server/realtime/login_grace_period.py`
- **start_login_grace_period()** (42 connections) — `server/realtime/login_grace_period.py`
- **login_grace_period.py** (42 connections) — `server/realtime/login_grace_period.py`
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
- **._get_login_grace_period_status()** (7 connections) — `server/realtime/integration/game_state_provider.py`
- **_grace_period_task()** (7 connections) — `server/realtime/login_grace_period.py`
- **_remove_from_grace_period_tracking()** (7 connections) — `server/realtime/login_grace_period.py`
- **_try_start_effect_based_grace()** (7 connections) — `server/realtime/login_grace_period.py`
- **test_effect_based_grace_start_then_tick_expiration_clears_in_memory()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_can_be_cancelled()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_grace_period_expires_after_duration()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- **test_multiple_players_independent_grace_periods()** (7 connections) — `server/tests/integration/test_login_grace_period_flow.py`
- *... and 160 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (22 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (12 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (10 shared connections)
- [server api players](server_api_players.md) (9 shared connections)
- [server realtime integration game state](server_realtime_integration_game_state.md) (8 shared connections)
- [server app game tick processing](server_app_game_tick_processing.md) (8 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (7 shared connections)
- [server commands combat](server_commands_combat.md) (6 shared connections)
- [server commands look helpers get](server_commands_look_helpers_get.md) (6 shared connections)
- [server game magic spell effects](server_game_magic_spell_effects.md) (6 shared connections)
- [server realtime occupant display](server_realtime_occupant_display.md) (6 shared connections)
- [server realtime player occupant processor](server_realtime_player_occupant_processor.md) (6 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/realtime/integration/game_state_provider.py`
- `server/realtime/login_grace_period.py`
- `server/tests/integration/test_login_grace_period_flow.py`
- `server/tests/unit/commands/test_combat_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period.py`
- `server/tests/unit/realtime/test_login_grace_period_visual_indicator.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 445 (92%)
- INFERRED: 37 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*