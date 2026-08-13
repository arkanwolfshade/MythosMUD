# get_username_from_user

> 92 nodes

## Key Concepts

- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **command_parser.py** (45 connections) — `server/utils/command_parser.py`
- **test_command_helpers.py** (27 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **validate_command_safety()** (17 connections) — `server/utils/command_helpers.py`
- **test_command_helpers_functions.py** (17 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **channel_commands.py** (16 connections) — `server/commands/channel_commands.py`
- **command_helpers.py** (15 connections) — `server/utils/command_helpers.py`
- **get_command_help()** (12 connections) — `server/utils/command_helpers.py`
- **handle_channel_command()** (10 connections) — `server/commands/channel_commands.py`
- **_handle_default_channel_setting()** (6 connections) — `server/commands/channel_commands.py`
- **_get_persistence_and_player()** (5 connections) — `server/commands/channel_commands.py`
- **_extract_channel_from_command()** (4 connections) — `server/commands/channel_commands.py`
- **_username_from_dict()** (4 connections) — `server/utils/command_helpers.py`
- **Any** (4 connections)
- **_validate_channel_name()** (3 connections) — `server/commands/channel_commands.py`
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
- *... and 67 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (15 shared connections)
- [AliasStorage](AliasStorage.md) (13 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [test_command_parser.py](test_command_parser.py.md) (5 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (4 shared connections)
- [CommandFactory](CommandFactory.md) (4 shared connections)
- [PlayerPreferencesService](PlayerPreferencesService.md) (3 shared connections)
- [test_logout_commands.py](test_logout_commands.py.md) (3 shared connections)
- [quest_commands.py](quest_commands.py.md) (3 shared connections)
- [.state](state.md) (3 shared connections)
- [get_async_session](get_async_session.md) (2 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (2 shared connections)

## Source Files

- `server/commands/channel_commands.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`
- `server/utils/command_parser.py`

## Audit Trail

- EXTRACTED: 203 (87%)
- INFERRED: 31 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*