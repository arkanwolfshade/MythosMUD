# asyncio

> 19 nodes

## Key Concepts

- **asyncio** (7 connections)
- **TestProcessCommandUnified** (6 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **TestLegacyFunctions** (5 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_legacy()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_blocked()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_normal_processing()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_rate_limited()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_special_routing()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_get_help_content()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_get_help_content_none()** (3 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test process_command_unified handles special command routing.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test process_command_unified processes normal commands.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test legacy compatibility functions.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test process_command() legacy function.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test get_help_content() delegates to help system.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test get_help_content() with None command.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test process_command_unified function.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test process_command_unified returns rate limit result.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **Test process_command_unified returns block result.** (1 connections) — `server/tests/unit/commands/test_command_handler_unified.py`

## Relationships

- [TestHelperFunctions](TestHelperFunctions.md) (5 shared connections)
- [User](User.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_handler_unified.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*