# command parser rationale

> 177 nodes

## Key Concepts

- **test_command_parser.py** (45 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_command_service.py** (36 connections) — `server/tests/unit/commands/test_command_service.py`
- **parse_command()** (24 connections) — `server/utils/command_parser.py`
- **CommandService** (20 connections) — `server/commands/command_service.py`
- **MythosValidationError** (8 connections)
- **test_command_parser_smoke.py** (8 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **._extract_parsed_fields()** (7 connections) — `server/commands/command_service.py`
- **.process_command()** (6 connections) — `server/commands/command_service.py`
- **._parse_command_string()** (5 connections) — `server/commands/command_service.py`
- **Command** (5 connections)
- **._prepare_command_data()** (5 connections) — `server/commands/command_service.py`
- **._execute_command_handler()** (5 connections) — `server/commands/command_service.py`
- **._fallback_parsed_fields()** (4 connections) — `server/commands/command_service.py`
- **._log_parsed_command_inspection()** (4 connections) — `server/commands/command_service.py`
- **test_parse_command_string_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_create_command_object_re_raises_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_process_command_string_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **._log_model_dump_result()** (3 connections) — `server/commands/command_service.py`
- **.register_command_handler()** (3 connections) — `server/commands/command_service.py`
- **command_service()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_parse_command_basic()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_with_args()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_with_pipes()** (3 connections) — `server/tests/unit/test_command_parser_smoke.py`
- **test_parse_command_empty_string()** (3 connections) — `server/tests/unit/utils/test_command_parser.py`
- *... and 152 more nodes in this community*

## Relationships

- [commands admin mute](commands_admin_mute.md) (7 shared connections)
- [command factories create](command_factories_create.md) (6 shared connections)
- [command inventory models](command_inventory_models.md) (5 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [Database Config](Database_Config.md) (2 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (2 shared connections)
- [command processor rationale](command_processor_rationale.md) (2 shared connections)
- [command commands handler](command_commands_handler.md) (1 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)
- [inventory commands command](inventory_commands_command.md) (1 shared connections)
- [room websocket updates](room_websocket_updates.md) (1 shared connections)

## Source Files

- `server/commands/command_service.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/test_command_parser_smoke.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 436 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*