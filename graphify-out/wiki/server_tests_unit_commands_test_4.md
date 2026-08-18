# server tests unit commands test

> 20 nodes

## Key Concepts

- **MockPersistence** (7 connections) — `server/tests/unit/commands/test_rest_command.py`
- **fixture** (5 connections)
- **mock_persistence()** (4 connections) — `server/tests/unit/commands/test_rest_command.py`
- **mock_app()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **mock_connection_manager()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **mock_player()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **mock_request()** (3 connections) — `server/tests/unit/commands/test_rest_command.py`
- **.get_player_by_name()** (2 connections) — `server/tests/unit/commands/test_rest_command.py`
- **.get_room_by_id()** (2 connections) — `server/tests/unit/commands/test_rest_command.py`
- **.__setattr__()** (2 connections) — `server/tests/unit/commands/test_rest_command.py`
- **.__init__()** (1 connections) — `server/tests/unit/commands/test_rest_command.py`
- **Create a mock FastAPI app.** (1 connections) — `server/tests/unit/commands/test_rest_command.py`
- **Create a mock request.** (1 connections) — `server/tests/unit/commands/test_rest_command.py`
- **Mock persistence layer with async methods.** (1 connections) — `server/tests/unit/commands/test_rest_command.py`
- **Mock async method that uses configured mock.** (1 connections) — `server/tests/unit/commands/test_rest_command.py`
- **Mock method that uses configured mock.** (1 connections) — `server/tests/unit/commands/test_rest_command.py`
- **Allow setting get_player_by_name and get_room_by_id to mocks.** (1 connections) — `server/tests/unit/commands/test_rest_command.py`
- **Create a mock persistence layer.** (1 connections) — `server/tests/unit/commands/test_rest_command.py`
- **Create a mock connection manager.** (1 connections) — `server/tests/unit/commands/test_rest_command.py`
- **Create a mock player.** (1 connections) — `server/tests/unit/commands/test_rest_command.py`

## Relationships

- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (6 shared connections)

## Source Files

- `server/tests/unit/commands/test_rest_command.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*