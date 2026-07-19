# Flee Command Tests

> 38 nodes · cohesion 0.10

## Key Concepts

- **test_flee_command.py** (25 connections) — `server/tests/unit/commands/test_flee_command.py`
- **FleeHandlerDeps** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_request_with_persistence()** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_no_exits_returns_no_escape()** (8 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_fails_returns_failure_and_uses_action()** (8 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_succeeds_returns_success()** (8 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_make_participant()** (7 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_standing_player_id()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_get_combat_command_handler_includes_flee()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **CombatCommandHandler** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **handler()** (5 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_not_in_combat_returns_message()** (5 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_not_standing_forces_stand_and_returns_message()** (5 connections) — `server/tests/unit/commands/test_flee_command.py`
- **flee_handler_deps()** (3 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_FleeCmdAppState** (3 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_GetCombatHandlerLoaderContainer** (3 connections) — `server/tests/unit/commands/test_flee_command.py`
- **UUID** (3 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_FleeCmdApp** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_FleeCmdRequest** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_GetCombatHandlerLoaderApp** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_GetCombatHandlerLoaderAppState** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **standing_player()** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **Unit tests for /flee command (handle_flee_command).** (1 connections) — `server/tests/unit/commands/test_flee_command.py`
- **Build request.app so _get_player_and_room gets player and room from persistence.** (1 connections) — `server/tests/unit/commands/test_flee_command.py`
- **Fields read by get_combat_command_handler via getattr(container, ...).** (1 connections) — `server/tests/unit/commands/test_flee_command.py`
- *... and 13 more nodes in this community*

## Relationships

- [[Combat Taunt Tests]] (7 shared connections)
- [[Player Domain Model]] (1 shared connections)
- [[Dependency Risk Analyzer]] (1 shared connections)
- [[Combat Command Handler]] (1 shared connections)
- [[Combat Command Helpers]] (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_flee_command.py`

## Audit Trail

- EXTRACTED: 145 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
