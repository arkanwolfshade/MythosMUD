# Community 483

> 37 nodes

## Key Concepts

- **_handle_special_command_routing()** (17 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (17 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_run_expanded_alias()** (9 connections) — `server/command_handler_unified.py`
- **TestProcessAliasExpansion** (8 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestHandleSpecialCommandRouting** (7 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **asyncio** (7 connections)
- **CommandExecutionRequest** (6 connections)
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
- **Alias** (1 connections)
- **Handle special command routing (alias management, alias expansion, emote).…** (1 connections) — `server/command_handler_unified.py`
- **Validate, audit, and execute an expanded alias command.** (1 connections) — `server/command_handler_unified.py`
- **Process alias expansion if applicable. Returns result if alias processed.** (1 connections) — `server/command_handler_unified.py`
- **Test _handle_special_command_routing returns error when alias storage…** (1 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **Test _handle_special_command_routing converts single-word emotes.** (1 connections) — `server/tests/unit/commands/test_command_aliases.py`
- *... and 12 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (15 shared connections)
- [Community 455](Community_455.md) (9 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (5 shared connections)
- [Community 98](Community_98.md) (3 shared connections)
- [Community 836](Community_836.md) (3 shared connections)
- [Community 168](Community_168.md) (2 shared connections)
- [Community 262](Community_262.md) (1 shared connections)
- [Community 726](Community_726.md) (1 shared connections)
- [Community 1108](Community_1108.md) (1 shared connections)
- [Community 837](Community_837.md) (1 shared connections)
- [Community 41](Community_41.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`

## Audit Trail

- EXTRACTED: 84 (89%)
- INFERRED: 10 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*