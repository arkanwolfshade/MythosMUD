# get_username_from_user

> 46 nodes

## Key Concepts

- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **teach_command.py** (15 connections) — `server/commands/teach_command.py`
- **handle_teach_command()** (14 connections) — `server/commands/teach_command.py`
- **test_teach_command.py** (6 connections) — `server/tests/unit/commands/test_teach_command.py`
- **_resolve_npc_teacher()** (4 connections) — `server/commands/teach_command.py`
- **test_handle_teach_command()** (4 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_target()** (4 connections) — `server/tests/unit/commands/test_teach_command.py`
- **_username_from_dict()** (4 connections) — `server/utils/command_helpers.py`
- **Any** (4 connections)
- **_format_teach_result()** (3 connections) — `server/commands/teach_command.py`
- **_get_teach_services()** (3 connections) — `server/commands/teach_command.py`
- **test_get_username_from_user_dict()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_username_from_user_with_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_username_from_user_with_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers_functions.py`
- **test_get_username_from_user_dict_name()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_dict_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_empty_dict()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_invalid()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_name_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_none()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_player_object()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_priority_player_over_username()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **test_get_username_from_user_username_attribute()** (3 connections) — `server/tests/unit/utils/test_command_helpers.py`
- **asyncio** (3 connections)
- *... and 21 more nodes in this community*

## Relationships

- [server/exceptions.py](server-exceptions.py.md) (13 shared connections)
- [AliasStorage](AliasStorage.md) (8 shared connections)
- [test_command_helpers_functions.py](test_command_helpers_functions.py.md) (4 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (3 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [test_logout_commands.py](test_logout_commands.py.md) (2 shared connections)
- [quest_commands.py](quest_commands.py.md) (2 shared connections)
- [.state](state.md) (2 shared connections)
- [CommandRequest](CommandRequest.md) (1 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)

## Source Files

- `server/commands/teach_command.py`
- `server/tests/unit/commands/test_teach_command.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 144 (82%)
- INFERRED: 32 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*