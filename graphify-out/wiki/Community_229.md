# Community 229

> 64 nodes

## Key Concepts

- **command_guards.py** (22 connections) — `server/command_handler/command_guards.py`
- **check_grace_period_block()** (18 connections) — `server/command_handler/command_guards.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **check_casting_state()** (12 connections) — `server/command_handler/command_guards.py`
- **test_grace_period_blocking.py** (11 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **TestCheckGracePeriodBlock** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler/command_guards.py`
- **_get_grace_check_context()** (7 connections) — `server/command_handler/command_guards.py`
- **_as_command_request()** (7 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
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
- **.testcheck_grace_period_block_handles_error()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_no_connection_manager()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_no_player_service()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.testcheck_grace_period_block_player_in_grace_period()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 39 more nodes in this community*

## Relationships

- [Community 214](Community_214.md) (11 shared connections)
- [Catatonia Status Checks](Catatonia_Status_Checks.md) (6 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (5 shared connections)
- [Community 327](Community_327.md) (4 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (3 shared connections)
- [Community 262](Community_262.md) (3 shared connections)
- [Community 218](Community_218.md) (1 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_guards.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 135 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*