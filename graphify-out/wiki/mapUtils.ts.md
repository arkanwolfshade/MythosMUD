# mapUtils.ts

> 71 nodes · cohesion 0.04

## Key Concepts

- **command_guards.py** (24 connections) — `server/command_handler/command_guards.py`
- **check_grace_period_block()** (18 connections) — `server/command_handler/command_guards.py`
- **check_casting_state()** (12 connections) — `server/command_handler/command_guards.py`
- **test_grace_period_blocking.py** (11 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **TestCheckGracePeriodBlock** (8 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler/command_guards.py`
- **_get_grace_check_context()** (7 connections) — `server/command_handler/command_guards.py`
- **_as_command_request()** (7 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **TestCheckCastingState** (7 connections) — `server/tests/unit/commands/test_command_validation.py`
- **_request_state()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_allows_commands_when_not_in_grace_period()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_blocks_commands()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_missing_services()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_check_grace_period_block_handles_player_not_found()** (6 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **_CastingStateManagerView** (5 connections) — `server/command_handler/command_guards.py`
- **_coerce_player_uuid()** (5 connections) — `server/command_handler/command_guards.py`
- **Protocol** (5 connections)
- **_raw_player_id()** (5 connections) — `server/command_handler/command_guards.py`
- **_CastingStateView** (4 connections) — `server/command_handler/command_guards.py`
- **_MagicServiceView** (4 connections) — `server/command_handler/command_guards.py`
- **_PlayerLookup** (4 connections) — `server/command_handler/command_guards.py`
- **CommandExecutionRequest** (4 connections)
- **UUID** (4 connections)
- **asyncio** (4 connections)
- **.testcheck_casting_state_allowed_command()** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- *... and 46 more nodes in this community*

## Relationships

- [go_command.py](go_command.py.md) (16 shared connections)
- [test_logging_file_categories.py](test_logging_file_categories.py.md) (6 shared connections)
- [look_container.py](look_container.py.md) (4 shared connections)
- [QuestService](QuestService.md) (3 shared connections)
- [test_look_npc_helpers.py](test_look_npc_helpers.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [player_connection_setup.py](player_connection_setup.py.md) (1 shared connections)

## Source Files

- `server/command_handler/command_guards.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 142 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*