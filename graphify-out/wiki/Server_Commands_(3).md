# Server Commands (3)

> 248 nodes

## Key Concepts

- **command_handler_unified.py** (52 connections) — `server/command_handler_unified.py`
- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (18 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (18 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **Any** (14 connections)
- **get_help_content()** (14 connections) — `server/help/help_content.py`
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **CommandRequest** (11 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (11 connections)
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **handle_command()** (10 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified.py** (10 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- **command_execution_request.py** (9 connections) — `server/command_handler/command_execution_request.py`
- **process_command()** (9 connections) — `server/command_handler_unified.py`
- **_get_grace_check_context()** (8 connections) — `server/command_handler_unified.py`
- **test_grace_period_blocking.py** (8 connections) — `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- **test_command_aliases.py** (8 connections) — `server/tests/unit/commands/test_command_aliases.py`
- *... and 223 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (34 shared connections)
- [Server Commands (5)](Server_Commands_%285%29.md) (18 shared connections)
- [Server Command Handler](Server_Command_Handler.md) (15 shared connections)
- [Server Realtime (38)](Server_Realtime_%2838%29.md) (7 shared connections)
- [Server Realtime (34)](Server_Realtime_%2834%29.md) (3 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (2 shared connections)
- [Server Realtime (20)](Server_Realtime_%2820%29.md) (2 shared connections)
- [Server Utils (6)](Server_Utils_%286%29.md) (2 shared connections)
- [Server Realtime (17)](Server_Realtime_%2817%29.md) (2 shared connections)
- [Server Commands (83)](Server_Commands_%2883%29.md) (2 shared connections)
- [Docs Examples](Docs_Examples.md) (2 shared connections)
- [Server Utils (18)](Server_Utils_%2818%29.md) (1 shared connections)

## Source Files

- `server/command_handler/alias_expansion.py`
- `server/command_handler/command_execution_request.py`
- `server/command_handler_unified.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_preparation.py`
- `server/tests/unit/commands/test_command_validation.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 872 (98%)
- INFERRED: 19 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*