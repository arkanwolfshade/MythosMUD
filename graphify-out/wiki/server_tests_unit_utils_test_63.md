# server tests unit utils test

> 38 nodes

## Key Concepts

- **validate_command_safety()** (17 connections) — `server/utils/command_helpers.py`
- **test_command_helpers_functions.py** (17 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
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
- **test_validate_command_safety_format_string_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_python_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_safe_commands()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_shell_metacharacters()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_sql_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_xss_attempts()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **Test validate_command_safety() returns False for SQL injection attempts.** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **Unit tests for command_helpers utility functions. Tests the utility functions…** (1 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **Test validate_command_safety() returns True for safe commands.** (1 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **Test validate_command_safety() returns False for shell metacharacters.** (1 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **Test validate_command_safety() returns False for format string injection.** (1 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- *... and 13 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [server tests unit utils test](server_tests_unit_utils_test.md) (7 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (4 shared connections)

## Source Files

- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*