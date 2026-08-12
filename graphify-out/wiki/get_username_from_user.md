# get_username_from_user

> 69 nodes

## Key Concepts

- **get_username_from_user()** (50 connections) — `server/utils/command_helpers.py`
- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_follow_command()** (18 connections) — `server/commands/follow_commands.py`
- **follow_commands.py** (17 connections) — `server/commands/follow_commands.py`
- **asyncio** (13 connections)
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_following_command()** (11 connections) — `server/commands/follow_commands.py`
- **handle_unfollow_command()** (11 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_same_room_npc_immediate()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_player_sends_request()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_self_rejected()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_such_player_or_npc()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_get_container()** (6 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_no_persistence()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_target()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_player_not_in_game()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_following_display()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_success()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_was_not_following()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Any** (6 connections)
- **_load_follow_context()** (5 connections) — `server/commands/follow_commands.py`
- **_resolve_follow_target()** (4 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_no_container()** (4 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_following_no_container()** (4 connections) — `server/tests/unit/commands/test_follow_commands.py`
- *... and 44 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (16 shared connections)
- [TargetMatch](TargetMatch.md) (12 shared connections)
- [test_command_helpers.py](test_command_helpers.py.md) (10 shared connections)
- [test_command_helpers_functions.py](test_command_helpers_functions.py.md) (4 shared connections)
- [Player](Player.md) (3 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (2 shared connections)
- [BaseCommand](BaseCommand.md) (2 shared connections)
- [logout_commands.py](logout_commands.py.md) (2 shared connections)
- [quest_commands.py](quest_commands.py.md) (2 shared connections)
- [.state](state.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [CommandRequest](CommandRequest.md) (1 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/tests/unit/commands/test_follow_commands.py`
- `server/tests/unit/utils/test_command_helpers.py`
- `server/utils/command_helpers.py`

## Audit Trail

- EXTRACTED: 296 (89%)
- INFERRED: 36 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*