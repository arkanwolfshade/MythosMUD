# test_follow_commands.py

> 46 nodes

## Key Concepts

- **test_follow_commands.py** (24 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **follow_commands.py** (18 connections) — `server/commands/follow_commands.py`
- **handle_follow_command()** (17 connections) — `server/commands/follow_commands.py`
- **asyncio** (13 connections)
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_following_command()** (10 connections) — `server/commands/follow_commands.py`
- **handle_unfollow_command()** (10 connections) — `server/commands/follow_commands.py`
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
- **test_handle_unfollow_no_container()** (4 connections) — `server/tests/unit/commands/test_follow_commands.py`
- *... and 21 more nodes in this community*

## Relationships

- [TargetResolutionService](TargetResolutionService.md) (11 shared connections)
- [AliasStorage](AliasStorage.md) (4 shared connections)
- [command_service.py](command_service.py.md) (4 shared connections)
- [TargetMatch](TargetMatch.md) (4 shared connections)
- [get_username_from_user](get_username_from_user.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/tests/unit/commands/test_follow_commands.py`

## Audit Trail

- EXTRACTED: 128 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*