# server tests unit commands test

> 39 nodes

## Key Concepts

- **test_flee_command.py** (29 connections) — `server/tests/unit/commands/test_flee_command.py`
- **FleeHandlerDeps** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_request_with_persistence()** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_no_exits_returns_no_escape()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_fails_returns_failure_and_uses_action()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_succeeds_returns_success()** (9 connections) — `server/tests/unit/commands/test_flee_command.py`
- **handler()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_make_participant()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_standing_player_id()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_not_in_combat_returns_message()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_not_standing_forces_stand_and_returns_message()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_get_combat_command_handler_includes_flee()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **asyncio** (5 connections)
- **flee_handler_deps()** (4 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_FleeCmdAppState** (3 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_GetCombatHandlerLoaderContainer** (3 connections) — `server/tests/unit/commands/test_flee_command.py`
- **standing_player()** (3 connections) — `server/tests/unit/commands/test_flee_command.py`
- **fixture** (3 connections)
- **UUID** (3 connections)
- **_FleeCmdApp** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_FleeCmdRequest** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_GetCombatHandlerLoaderApp** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_GetCombatHandlerLoaderAppState** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **TypedDict** (1 connections)
- **Unit tests for /flee command (handle_flee_command).** (1 connections) — `server/tests/unit/commands/test_flee_command.py`
- *... and 14 more nodes in this community*

## Relationships

- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (7 shared connections)
- [server models combat combatinstance](server_models_combat_combatinstance.md) (4 shared connections)
- [server commands combat](server_commands_combat.md) (3 shared connections)
- [server models combat combataction](server_models_combat_combataction.md) (2 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (2 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_flee_command.py`

## Audit Trail

- EXTRACTED: 88 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*