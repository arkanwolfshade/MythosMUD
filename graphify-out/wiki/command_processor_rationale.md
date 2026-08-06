# command processor rationale

> 119 nodes

## Key Concepts

- **test_command_processor.py** (39 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_command_service.py** (36 connections) — `server/tests/unit/commands/test_command_service.py`
- **MythosValidationError** (10 connections)
- **test_parse_command_string_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_create_command_object_re_raises_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_process_command_string_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **test_process_validated_command_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **mock_request()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **mock_user()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_success()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_no_command_type()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_unknown_command()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_handler_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_logging_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_parse_command_string_success()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_parse_command_string_with_subcommand()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_parse_command_string_unexpected_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_prepare_command_data_basic()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_prepare_command_data_with_pipe_target()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_extract_parsed_fields_basic()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_extract_parsed_fields_with_pipe_target()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_success()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_command_success()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_command_parse_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- *... and 94 more nodes in this community*

## Relationships

- [payload realtime optimizer](payload_realtime_optimizer.md) (7 shared connections)
- [command inventory models](command_inventory_models.md) (5 shared connections)
- [command models moderation](command_models_moderation.md) (3 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (2 shared connections)
- [combat services initialization](combat_services_initialization.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (1 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)
- [services nats service](services_nats_service.md) (1 shared connections)
- [rescue service services](rescue_service_services.md) (1 shared connections)
- [character creation service](character_creation_service.md) (1 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 253 (95%)
- INFERRED: 12 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*