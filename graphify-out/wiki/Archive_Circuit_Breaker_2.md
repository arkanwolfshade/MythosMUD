# Archive Circuit Breaker

> 16 nodes

## Key Concepts

- **get_command_help()** (12 connections) — `server/utils/command_helpers.py`
- **test_get_command_help_no_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_specific_commands()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_unknown_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_case_insensitive()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_specific_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_command_help_unknown_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_command_help_general()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **Test get_command_help with no command (general help).** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_command_help with specific command types.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_command_help with unknown command.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_command_help is case insensitive.** (1 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test get_command_help() returns help for specific command.** (1 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **Test get_command_help() returns error message for unknown command.** (1 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **Test get_command_help() returns general help when command_type is None.** (1 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **Get help text for commands.      Args:         command_type: Specific command to** (1 connections) — `server/utils/command_helpers.py`

## Relationships

- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (6 shared connections)
- [WebSocket Handler Helpers](WebSocket_Handler_Helpers.md) (4 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*