# get_username_from_user

> 39 nodes

## Key Concepts

- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **follow_commands.py** (17 connections) — `server/commands/follow_commands.py`
- **handle_following_command()** (10 connections) — `server/commands/follow_commands.py`
- **handle_unfollow_command()** (10 connections) — `server/commands/follow_commands.py`
- **_get_container()** (6 connections) — `server/commands/follow_commands.py`
- **Any** (6 connections)
- **_load_follow_context()** (5 connections) — `server/commands/follow_commands.py`
- **_resolve_follow_target()** (4 connections) — `server/commands/follow_commands.py`
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
- **_username_from_dict()** (3 connections) — `server/utils/command_helpers.py`
- **Follow commands for MythosMUD. Handlers for /follow, /unfollow, and /following.…** (1 connections) — `server/commands/follow_commands.py`
- **Handle /following - show who you follow and who follows you.** (1 connections) — `server/commands/follow_commands.py`
- **Get application container from request.** (1 connections) — `server/commands/follow_commands.py`
- **Load follow prerequisites or return an error payload.** (1 connections) — `server/commands/follow_commands.py`
- *... and 14 more nodes in this community*

## Relationships

- [test_command_helpers.py](test_command_helpers.py.md) (14 shared connections)
- [test_follow_commands.py](test_follow_commands.py.md) (13 shared connections)
- [AliasStorage](AliasStorage.md) (9 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (3 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (3 shared connections)
- [test_logout_commands.py](test_logout_commands.py.md) (2 shared connections)
- [quest_commands.py](quest_commands.py.md) (2 shared connections)
- [rescue_commands.py](rescue_commands.py.md) (2 shared connections)
- [CommandRequest](CommandRequest.md) (1 shared connections)
- [command_handler_unified.py](command_handler_unified.py.md) (1 shared connections)
- [test_channel_commands.py](test_channel_commands.py.md) (1 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/tests/unit/utils/test_command_helpers_functions.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 86 (72%)
- INFERRED: 33 (28%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*