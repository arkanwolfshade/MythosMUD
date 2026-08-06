# command commands handler

> 255 nodes

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
- **command_execution_request.py** (9 connections) — `server/command_handler/command_execution_request.py`
- *... and 230 more nodes in this community*

## Relationships

- [command validation commands](command_validation_commands.md) (18 shared connections)
- [commands npc admin](commands_npc_admin.md) (17 shared connections)
- [combat attack handler](combat_attack_handler.md) (14 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (8 shared connections)
- [config models app](config_models_app.md) (8 shared connections)
- [request context realtime](request_context_realtime.md) (7 shared connections)
- [command validator validators](command_validator_validators.md) (6 shared connections)
- [combat npc services](combat_npc_services.md) (5 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (3 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (3 shared connections)
- [npc combat base](npc_combat_base.md) (3 shared connections)
- [persistence combat services](persistence_combat_services.md) (2 shared connections)

## Source Files

- `server/command_handler/command_execution_request.py`
- `server/command_handler/command_input.py`
- `server/command_handler_unified.py`
- `server/realtime/request_context.py`
- `server/tests/unit/command_handler/test_command_execution_request.py`
- `server/tests/unit/command_handler_unified/test_grace_period_blocking.py`
- `server/tests/unit/commands/test_command_aliases.py`
- `server/tests/unit/commands/test_command_handler_unified.py`
- `server/tests/unit/commands/test_command_handler_unified_helpers.py`
- `server/tests/unit/commands/test_command_input.py`
- `server/tests/unit/commands/test_command_preparation.py`

## Audit Trail

- EXTRACTED: 910 (98%)
- INFERRED: 20 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*