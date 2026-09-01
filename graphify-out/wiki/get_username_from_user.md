# get_username_from_user

> 80 nodes

## Key Concepts

- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **test_command_helpers.py** (28 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **command_helpers.py** (18 connections) — `server/utils/command_helpers.py`
- **validate_command_safety()** (17 connections) — `server/utils/command_helpers.py`
- **test_command_helpers_functions.py** (17 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **get_command_help()** (12 connections) — `server/utils/command_helpers.py`
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
- **test_validate_command_safety_xss()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_command_help_case_insensitive()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_no_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_specific_commands()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_unknown_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- *... and 55 more nodes in this community*

## Relationships

- [ValidationError](ValidationError.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [CommandFactory](CommandFactory.md) (4 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (3 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (3 shared connections)
- [test_logout_commands.py](test_logout_commands.py.md) (2 shared connections)
- [quest_commands.py](quest_commands.py.md) (2 shared connections)
- [.state](state.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [handle_command](handle_command.md) (1 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 135 (80%)
- INFERRED: 34 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*