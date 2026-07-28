# Player State Factories

> 90 nodes · cohesion 0.03

## Key Concepts

- **test_command_service.py** (36 connections) — `server/tests/unit/commands/test_command_service.py`
- **CommandService** (20 connections) — `server/commands/command_service.py`
- **Any** (10 connections)
- **._extract_parsed_fields()** (7 connections) — `server/commands/command_service.py`
- **.process_command()** (7 connections) — `server/commands/command_service.py`
- **._execute_command_handler()** (6 connections) — `server/commands/command_service.py`
- **._parse_command_string()** (5 connections) — `server/commands/command_service.py`
- **._prepare_command_data()** (5 connections) — `server/commands/command_service.py`
- **.process_validated_command()** (5 connections) — `server/commands/command_service.py`
- **._fallback_parsed_fields()** (4 connections) — `server/commands/command_service.py`
- **._log_model_dump_result()** (4 connections) — `server/commands/command_service.py`
- **._log_parsed_command_inspection()** (4 connections) — `server/commands/command_service.py`
- **.register_command_handler()** (3 connections) — `server/commands/command_service.py`
- **command_service()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_extract_parsed_fields_handles_missing_attributes()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_process_validated_command_validation_error()** (3 connections) — `server/tests/unit/commands/test_command_service.py`
- **.get_available_commands()** (2 connections) — `server/commands/command_service.py`
- **.unregister_command_handler()** (2 connections) — `server/commands/command_service.py`
- **mock_request()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **mock_user()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_error()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_returns_non_dict()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_execute_command_handler_success()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_extract_parsed_fields_basic()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- **test_extract_parsed_fields_with_pipe_target()** (2 connections) — `server/tests/unit/commands/test_command_service.py`
- *... and 65 more nodes in this community*

## Relationships

- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (7 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (3 shared connections)
- [Realtime Message Formatters](Realtime_Message_Formatters.md) (1 shared connections)
- [Command Request App State](Command_Request_App_State.md) (1 shared connections)
- [Admin Command Models](Admin_Command_Models.md) (1 shared connections)
- [Combat Taunt Tests](Combat_Taunt_Tests.md) (1 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)
- [Connection Disconnection Cleanup](Connection_Disconnection_Cleanup.md) (1 shared connections)

## Source Files

- `server/commands/command_service.py`
- `server/tests/unit/commands/test_command_service.py`

## Audit Trail

- EXTRACTED: 226 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*