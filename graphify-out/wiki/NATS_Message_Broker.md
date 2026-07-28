# NATS Message Broker

> 77 nodes · cohesion 0.04

## Key Concepts

- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **test_command_helpers.py** (27 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_command_helpers_functions.py** (17 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **validate_command_safety()** (17 connections) — `server/utils/command_helpers.py`
- **command_helpers.py** (15 connections) — `server/utils/command_helpers.py`
- **get_command_help()** (12 connections) — `server/utils/command_helpers.py`
- **_username_from_dict()** (4 connections) — `server/utils/command_helpers.py`
- **test_get_command_help_general()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_command_help_specific_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_command_help_unknown_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_username_from_user_dict()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_username_from_user_with_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_username_from_user_with_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_format_string()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_python_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_safe()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_shell_metacharacters()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_sql_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_validate_command_safety_xss()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_command_help_case_insensitive()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_no_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_specific_commands()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_unknown_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- *... and 52 more nodes in this community*

## Relationships

- [Admin Command Models](Admin_Command_Models.md) (11 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (5 shared connections)
- [Rescue Service Tests](Rescue_Service_Tests.md) (3 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (2 shared connections)
- [Api Player Respawn](Api_Player_Respawn.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)
- [Command Request App State](Command_Request_App_State.md) (2 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (2 shared connections)
- [Logout and Quit Commands](Logout_and_Quit_Commands.md) (2 shared connections)
- [Room Planning Archive](Room_Planning_Archive.md) (2 shared connections)
- [Quest Journal Commands](Quest_Journal_Commands.md) (2 shared connections)
- [Api Player](Api_Player.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 245 (89%)
- INFERRED: 30 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*