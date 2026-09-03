# Test Command Aliases

> 48 nodes

## Key Concepts

- **command_handler_unified.py** (42 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (17 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (16 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (16 connections) — `server/command_handler_unified.py`
- **test_command_aliases.py** (9 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **process_command()** (7 connections) — `server/command_handler_unified.py`
- **_run_expanded_alias()** (7 connections) — `server/command_handler_unified.py`
- **AliasStorage** (7 connections)
- **asyncio** (7 connections)
- **TestProcessAliasExpansion** (6 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestHandleSpecialCommandRouting** (6 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **CommandExecutionRequest** (6 connections)
- **TestHandleSpecialCommandRouting** (5 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **_as_user_dict()** (5 connections) — `server/command_handler_unified.py`
- **.test_handle_special_command_routing_alias_command()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_handle_special_command_routing_alias_command_no_storage()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_handle_special_command_routing_emote_conversion()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_invalid_expanded()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_no_alias()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_no_alias_storage()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_unsafe_alias()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_handle_special_command_routing_alias_command()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_handle_special_command_routing_alias_storage_none()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_handle_special_command_routing_emote_conversion()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **.test_handle_special_command_routing_returns_none()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- *... and 23 more nodes in this community*

## Relationships

- [Test Command Handler Unified Helpers](Test_Command_Handler_Unified_Helpers.md) (20 shared connections)
- [Test Command Handler Unified](Test_Command_Handler_Unified.md) (12 shared connections)
- [Test Command Validation](Test_Command_Validation.md) (5 shared connections)
- [Command Guards](Command_Guards.md) (3 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (3 shared connections)
- [Websocket Handler Commands](Websocket_Handler_Commands.md) (2 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (2 shared connections)
- [Character Creation API](Character_Creation_API.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [Command Service](Command_Service.md) (1 shared connections)
- [Correlation Middleware](Correlation_Middleware.md) (1 shared connections)
- [Alias Storage](Alias_Storage.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`

## Audit Trail

- EXTRACTED: 143 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*