# Command Guards

> 49 nodes

## Key Concepts

- **command_guards.py** (20 connections) — `server/command_handler/command_guards.py`
- **check_grace_period_block()** (18 connections) — `server/command_handler/command_guards.py`
- **test_grace_period_blocking.py** (12 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **check_casting_state()** (11 connections) — `server/command_handler/command_guards.py`
- **_as_command_request()** (7 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **_get_casting_block_result()** (6 connections) — `server/command_handler/command_guards.py`
- **_get_grace_check_context()** (6 connections) — `server/command_handler/command_guards.py`
- **_request_state()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_allows_commands_when_not_in_grace_period()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_blocks_commands()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_missing_services()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_player_not_found()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **_CastingStateManagerView** (5 connections) — `server/command_handler/command_guards.py`
- **_coerce_player_uuid()** (5 connections) — `server/command_handler/command_guards.py`
- **_raw_player_id()** (5 connections) — `server/command_handler/command_guards.py`
- **Protocol** (5 connections)
- **_CastingStateView** (4 connections) — `server/command_handler/command_guards.py`
- **_MagicServiceView** (4 connections) — `server/command_handler/command_guards.py`
- **_PlayerLookup** (4 connections) — `server/command_handler/command_guards.py`
- **CommandExecutionRequest** (4 connections)
- **UUID** (4 connections)
- **asyncio** (4 connections)
- **_AppStateCommandGuards** (3 connections) — `server/command_handler/command_guards.py`
- **mock_request()** (3 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **.get_casting_state()** (2 connections) — `server/command_handler/command_guards.py`
- *... and 24 more nodes in this community*

## Relationships

- [Test Command Validation](Test_Command_Validation.md) (14 shared connections)
- [Test Command Aliases](Test_Command_Aliases.md) (3 shared connections)
- [Test Rest And Grace Period](Test_Rest_And_Grace_Period.md) (3 shared connections)
- [Test Request Context](Test_Request_Context.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/command_handler/command_guards.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`

## Audit Trail

- EXTRACTED: 105 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*