# test command service

> 47 nodes

## Key Concepts

- **TargetType** (31 connections) — `server/schemas/shared/target_resolution.py`
- **target_resolution_service.py** (27 connections) — `server/services/target_resolution_service.py`
- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_follow_command()** (19 connections) — `server/commands/follow_commands.py`
- **follow_commands.py** (15 connections) — `server/commands/follow_commands.py`
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_unfollow_command()** (11 connections) — `server/commands/follow_commands.py`
- **handle_following_command()** (11 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_self_rejected()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_player_sends_request()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_npc_immediate()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_get_container()** (6 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_no_such_player_or_npc()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_persistence()** (5 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_target()** (5 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_player_not_in_game()** (5 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_success()** (5 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_was_not_following()** (5 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_following_display()** (5 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Any** (4 connections)
- **test_handle_follow_no_container()** (3 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_no_container()** (3 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_following_no_container()** (3 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Follow commands for MythosMUD.  Handlers for /follow, /unfollow, and /following.** (1 connections) — `server/commands/follow_commands.py`
- *... and 22 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (17 shared connections)
- [CombatService](CombatService.md) (14 shared connections)
- [.end combat()](end_combat%28%29.md) (9 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (8 shared connections)
- [ContainerData](ContainerData.md) (5 shared connections)
- [test magic commands](test_magic_commands.md) (4 shared connections)
- [DropResolved](DropResolved.md) (4 shared connections)
- [Player Position Service](Player_Position_Service.md) (3 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (3 shared connections)
- [message handler factory](message_handler_factory.md) (3 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (2 shared connections)
- [Any](Any.md) (2 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/target_resolution_service.py`
- `server/tests/unit/commands/test_follow_commands.py`

## Audit Trail

- EXTRACTED: 252 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*