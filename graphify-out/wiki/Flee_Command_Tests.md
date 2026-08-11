# Flee Command Tests

> 35 nodes

## Key Concepts

- **test_flee_command.py** (28 connections) — `server/tests/unit/commands/test_flee_command.py`
- **FleeHandlerDeps** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_request_with_persistence()** (10 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_no_exits_returns_no_escape()** (8 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_fails_returns_failure_and_uses_action()** (8 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_roll_succeeds_returns_success()** (8 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_make_participant()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_standing_player_id()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_get_combat_command_handler_includes_flee()** (6 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_not_in_combat_returns_message()** (5 connections) — `server/tests/unit/commands/test_flee_command.py`
- **test_flee_not_standing_forces_stand_and_returns_message()** (5 connections) — `server/tests/unit/commands/test_flee_command.py`
- **UUID** (3 connections)
- **flee_handler_deps()** (3 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_FleeCmdAppState** (3 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_GetCombatHandlerLoaderContainer** (3 connections) — `server/tests/unit/commands/test_flee_command.py`
- **standing_player()** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_FleeCmdApp** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_FleeCmdRequest** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_GetCombatHandlerLoaderAppState** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **_GetCombatHandlerLoaderApp** (2 connections) — `server/tests/unit/commands/test_flee_command.py`
- **TypedDict** (1 connections)
- **Unit tests for /flee command (handle_flee_command).** (1 connections) — `server/tests/unit/commands/test_flee_command.py`
- **Typed fixture bundle for CombatCommandHandler flee tests (mocks).** (1 connections) — `server/tests/unit/commands/test_flee_command.py`
- **CombatCommandHandler deps for flee: combat_service, movement_service, player_pos** (1 connections) — `server/tests/unit/commands/test_flee_command.py`
- **Player that is standing and in a room.** (1 connections) — `server/tests/unit/commands/test_flee_command.py`
- *... and 10 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (6 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (2 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)

## Source Files

- `server/tests/unit/commands/test_flee_command.py`

## Audit Trail

- EXTRACTED: 136 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*