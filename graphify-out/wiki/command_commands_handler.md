# command commands handler

> 293 nodes

## Key Concepts

- **command_handler_unified.py** (52 connections) — `server/command_handler_unified.py`
- **TestHelperFunctions** (33 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **_check_grace_period_block()** (24 connections) — `server/command_handler_unified.py`
- **_prepare_command_for_processing()** (21 connections) — `server/command_handler_unified.py`
- **process_command_unified()** (19 connections) — `server/command_handler_unified.py`
- **_check_casting_state()** (19 connections) — `server/command_handler_unified.py`
- **_process_alias_expansion()** (19 connections) — `server/command_handler_unified.py`
- **_handle_special_command_routing()** (18 connections) — `server/command_handler_unified.py`
- **_check_all_command_blocks()** (17 connections) — `server/command_handler_unified.py`
- **_validate_command_basics()** (16 connections) — `server/command_handler_unified.py`
- **get_help_content()** (15 connections) — `server/help/help_content.py`
- **command_request_app_state()** (14 connections) — `server/command_handler/command_execution_request.py`
- **command_input.py** (14 connections) — `server/command_handler/command_input.py`
- **Any** (14 connections)
- **_ensure_alias_storage()** (13 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified_helpers.py** (13 connections) — `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- **normalize_command()** (12 connections) — `server/command_handler/command_input.py`
- **TestCommandNormalization** (12 connections) — `server/tests/unit/commands/test_command_input.py`
- **CommandRequest** (11 connections) — `server/command_handler_unified.py`
- **CommandExecutionRequest** (11 connections)
- **clean_command_input()** (10 connections) — `server/command_handler/command_input.py`
- **should_treat_as_emote()** (10 connections) — `server/command_handler/command_input.py`
- **_check_rate_limit()** (10 connections) — `server/command_handler_unified.py`
- **handle_command()** (10 connections) — `server/command_handler_unified.py`
- **test_command_handler_unified.py** (10 connections) — `server/tests/unit/commands/test_command_handler_unified.py`
- *... and 268 more nodes in this community*

## Relationships

- [command validation commands](command_validation_commands.md) (20 shared connections)
- [Loot Generation](Loot_Generation.md) (19 shared connections)
- [commands party examples](commands_party_examples.md) (16 shared connections)
- [alias graph rationale](alias_graph_rationale.md) (11 shared connections)
- [config models app](config_models_app.md) (4 shared connections)
- [request context realtime](request_context_realtime.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (3 shared connections)
- [player disconnect handlers](player_disconnect_handlers.md) (3 shared connections)
- [combat schemas schema](combat_schemas_schema.md) (3 shared connections)
- [schemas validator rationale](schemas_validator_rationale.md) (2 shared connections)
- [logoutHandler logger App](logoutHandler_logger_App.md) (2 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (2 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_input.py`
- `server/command_handler_unified.py`
- `server/help/__init__.py`
- `server/help/help_content.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_input.py`
- `server/tests/unit/commands/test_command_preparation.py`
- `server/tests/unit/commands/test_command_validation.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_help.py`

## Audit Trail

- EXTRACTED: 1002 (98%)
- INFERRED: 20 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*