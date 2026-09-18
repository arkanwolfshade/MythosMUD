# Community 256

> 60 nodes

## Key Concepts

- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (17 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (17 connections) — `server/command_handler_unified.py`
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (11 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_run_expanded_alias()** (9 connections) — `server/command_handler_unified.py`
- **test_command_aliases.py** (8 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **process_command()** (7 connections) — `server/command_handler_unified.py`
- **asyncio** (7 connections)
- **TestProcessAliasExpansion** (6 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestProcessCommandUnified** (6 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **CommandExecutionRequest** (6 connections)
- **TestEnsureAliasStorage** (5 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **TestHandleSpecialCommandRouting** (5 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **_as_user_dict()** (5 connections) — `server/command_handler_unified.py`
- **.test_handle_special_command_routing_alias_command()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_handle_special_command_routing_alias_command_no_storage()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_handle_special_command_routing_emote_conversion()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_invalid_expanded()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_no_alias()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_no_alias_storage()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_alias_expansion_unsafe_alias()** (4 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **.test_process_command_unified_blocked()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_normal_processing()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **.test_process_command_unified_rate_limited()** (4 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- *... and 35 more nodes in this community*

## Relationships

- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (17 shared connections)
- [Community 360](Community_360.md) (13 shared connections)
- [Community 25](Community_25.md) (7 shared connections)
- [Community 726](Community_726.md) (3 shared connections)
- [Community 832](Community_832.md) (3 shared connections)
- [Community 214](Community_214.md) (3 shared connections)
- [Community 306](Community_306.md) (2 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)
- [Community 615](Community_615.md) (1 shared connections)
- [Community 432](Community_432.md) (1 shared connections)
- [Community 442](Community_442.md) (1 shared connections)
- [Community 182](Community_182.md) (1 shared connections)

## Source Files

- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`

## Audit Trail

- EXTRACTED: 136 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*