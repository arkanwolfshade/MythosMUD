# . get persistence from app()

> 76 nodes

## Key Concepts

- **get_username_from_user()** (49 connections) — `server/utils/command_helpers.py`
- **test_command_helpers.py** (27 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_command_helpers_functions.py** (17 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **validate_command_safety()** (17 connections) — `server/utils/command_helpers.py`
- **get_command_help()** (12 connections) — `server/utils/command_helpers.py`
- **.get_player_and_room()** (6 connections) — `server/commands/combat_handler.py`
- **AppWithState** (5 connections)
- **._get_persistence_from_app()** (5 connections) — `server/commands/combat_handler.py`
- **_username_from_dict()** (4 connections) — `server/utils/command_helpers.py`
- **test_validate_command_safety_safe_commands()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_shell_metacharacters()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_sql_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_python_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_format_string_injection()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_validate_command_safety_xss_attempts()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_no_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_specific_commands()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_unknown_command()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_command_help_case_insensitive()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_player_object()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_username_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_name_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_invalid()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- *... and 51 more nodes in this community*

## Relationships

- [Any](Any.md) (13 shared connections)
- [main()](main%28%29.md) (8 shared connections)
- [follow commands](follow_commands.md) (3 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [.check and interrupt rest()](check_and_interrupt_rest%28%29.md) (2 shared connections)
- [Player Position Service](Player_Position_Service.md) (2 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (2 shared connections)
- [disconnect player connections()](disconnect_player_connections%28%29.md) (2 shared connections)
- [ExitStack](ExitStack.md) (2 shared connections)
- [rescue commands](rescue_commands.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [.validate spell name()](validate_spell_name%28%29.md) (1 shared connections)

## Source Files

- `server/commands/combat_handler.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 245 (88%)
- INFERRED: 32 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*