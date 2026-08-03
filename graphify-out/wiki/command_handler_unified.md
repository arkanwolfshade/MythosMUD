# command handler unified

> 68 nodes

## Key Concepts

- **command_handler_unified.py** (52 connections) — `server/command_handler_unified.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (18 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (18 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **alias_expansion.py** (16 connections) — `server/command_handler/alias_expansion.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **Any** (14 connections)
- **__init__.py** (13 connections) — `server/command_handler/__init__.py`
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **process_command_with_validation()** (11 connections) — `server/command_handler/processing.py`
- **CommandExecutionRequest** (11 connections)
- **clean_command_input()** (10 connections) — `server/command_handler/command_input.py`
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **handle_command()** (10 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified.py** (10 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **process_command()** (9 connections) — `server/command_handler_unified.py`
- **handle_expanded_command()** (8 connections) — `server/command_handler/alias_expansion.py`
- **_get_grace_check_context()** (8 connections) — `server/command_handler_unified.py`
- **test_command_aliases.py** (8 connections) — `server/tests/unit/commands/test_command_aliases.py`
- **_get_casting_block_result()** (7 connections) — `server/command_handler_unified.py`
- *... and 43 more nodes in this community*

## Relationships

- [command commands handler](command_commands_handler.md) (37 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (25 shared connections)
- [command validation commands](command_validation_commands.md) (18 shared connections)
- [game chat service](game_chat_service.md) (15 shared connections)
- [command input commands](command_input_commands.md) (13 shared connections)
- [NATS Messaging](NATS_Messaging.md) (8 shared connections)
- [command commands validation](command_commands_validation.md) (8 shared connections)
- [commands command validation](commands_command_validation.md) (7 shared connections)
- [auth users rationale](auth_users_rationale.md) (6 shared connections)
- [persistence rationale player](persistence_rationale_player.md) (6 shared connections)
- [alias storage commands](alias_storage_commands.md) (5 shared connections)
- [command commands aliases](command_commands_aliases.md) (5 shared connections)

## Source Files

- `server/command_handler/__init__.py`
- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_input.py`
- `server/command_handler/processing.py`
- `server/command_handler_unified.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`

## Audit Trail

- EXTRACTED: 441 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*