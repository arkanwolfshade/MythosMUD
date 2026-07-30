# NATS

> 97 nodes

## Key Concepts

- **test_command_service.py** (36 connections) — `server/tests/unit/commands/test_command_service.py`
- **CommandService** (20 connections) — `server/commands/command_service.py`
- **Any** (10 connections)
- **MythosValidationError** (8 connections)
- **._extract_parsed_fields()** (7 connections) — `server/commands/command_service.py`
- **.process_command()** (7 connections) — `server/commands/command_service.py`
- **._execute_command_handler()** (6 connections) — `server/commands/command_service.py`
- **.process_validated_command()** (5 connections) — `server/commands/command_service.py`
- **._parse_command_string()** (5 connections) — `server/commands/command_service.py`
- **._prepare_command_data()** (5 connections) — `server/commands/command_service.py`
- **._fallback_parsed_fields()** (4 connections) — `server/commands/command_service.py`
- **._log_parsed_command_inspection()** (4 connections) — `server/commands/command_service.py`
- **._log_model_dump_result()** (4 connections) — `server/commands/command_service.py`
- **test_parse_command_string_validation_error()** (4 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_create_command_object_re_raises_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_parser.py`
- **test_process_command_string_mythos_validation_error()** (4 connections) — `server/tests/unit/utils/test_command_processor.py`
- **.register_command_handler()** (3 connections) — `server/commands/command_service.py`
- **command_service()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_extract_parsed_fields_handles_missing_attributes()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **.get_available_commands()** (2 connections) — `server/commands/command_service.py`
- **.unregister_command_handler()** (2 connections) — `server/commands/command_service.py`
- **mock_request()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **mock_user()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_success()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- *... and 72 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (4 shared connections)
- [DropResolved](DropResolved.md) (3 shared connections)
- [test magic commands](test_magic_commands.md) (3 shared connections)
- [.validate topic()](validate_topic%28%29.md) (2 shared connections)
- [convert pydantic error()](convert_pydantic_error%28%29.md) (2 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (1 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (1 shared connections)
- [Player Position Service](Player_Position_Service.md) (1 shared connections)
- [Spell Targeting](Spell_Targeting.md) (1 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (1 shared connections)
- [real time](real_time.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)

## Source Files

- `server/commands/command_service.py`
- `server/tests/unit/commands/test_command_service.py`
- `server/tests/unit/utils/test_command_parser.py`
- `server/tests/unit/utils/test_command_processor.py`

## Audit Trail

- EXTRACTED: 240 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*