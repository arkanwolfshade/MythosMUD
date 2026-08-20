# get_username_from_user

> 90 nodes

## Key Concepts

- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **test_admin_commands.py** (38 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_command_helpers.py** (28 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **command_helpers.py** (18 connections) — `server/utils/command_helpers.py`
- **validate_command_safety()** (17 connections) — `server/utils/command_helpers.py`
- **test_command_helpers_functions.py** (17 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **get_command_help()** (12 connections) — `server/utils/command_helpers.py`
- **handle_add_admin_command()** (10 connections) — `server/commands/admin_mute_commands.py`
- **test_handle_mute_command_exception()** (5 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_add_admin_command_no_user_manager()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_handle_add_admin_command_success()** (4 connections) — `server/tests/unit/commands/test_admin_commands.py`
- **test_get_username_from_user_empty_dict()** (4 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_invalid()** (4 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_none()** (4 connections) — `server/tests/unit/utils/test_command_helpers.py`
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
- *... and 65 more nodes in this community*

## Relationships

- [command_service.py](command_service.py.md) (38 shared connections)
- [ValidationError](ValidationError.md) (13 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [TargetResolutionResult](TargetResolutionResult.md) (3 shared connections)
- [test_logout_commands.py](test_logout_commands.py.md) (2 shared connections)
- [quest_commands.py](quest_commands.py.md) (2 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [test_admin_teleport_commands.py](test_admin_teleport_commands.py.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [handle_command](handle_command.md) (1 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)

## Source Files

- `server/commands/admin_mute_commands.py`
- `server/tests/unit/commands/test_admin_commands.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 184 (82%)
- INFERRED: 40 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*