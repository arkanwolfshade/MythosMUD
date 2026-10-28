# DialogueService

> 35 nodes · cohesion 0.07

## Key Concepts

- **_prepare_command_for_processing()** (20 connections) — `server/command_handler_unified.py`
- **_check_rate_limit()** (9 connections) — `server/command_handler_unified.py`
- **TestPrepareCommandForProcessing** (7 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **test_command_preparation.py** (4 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **TestCheckRateLimit** (4 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_rate_limit_allowed()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_check_rate_limit_blocked()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_for_processing_empty_after_cleaning()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_for_processing_rate_limited()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_for_processing_success()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_for_processing_validation_failed()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_prepare_command_empty_after_cleaning()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_empty_after_normalization()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_rate_limited()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_success()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_prepare_command_validation_failed()** (3 connections) — `server/tests/unit/commands/test_command_preparation.py`
- **.test_check_rate_limit_allowed()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **.test_check_rate_limit_blocked()** (3 connections) — `server/tests/unit/commands/test_command_validation.py`
- **Check if player is rate limited. Returns result dict if blocked, None if…** (1 connections) — `server/command_handler_unified.py`
- **Prepare command for processing. Returns (command_line, cmd, args,…** (1 connections) — `server/command_handler_unified.py`
- **Test _prepare_command_for_processing returns rate limit result.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _prepare_command_for_processing returns validation result.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _prepare_command_for_processing successfully prepares command.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _check_rate_limit returns None when allowed.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **Test _check_rate_limit returns result when blocked.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- *... and 10 more nodes in this community*

## Relationships

- [test_movement_service.py](test_movement_service.py.md) (9 shared connections)
- [QuestService](QuestService.md) (5 shared connections)
- [go_command.py](go_command.py.md) (2 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (2 shared connections)
- [command_parser.py](command_parser.py.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`
- `server/tests/unit/commands/test_command_validation.py`

## Audit Trail

- EXTRACTED: 59 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*