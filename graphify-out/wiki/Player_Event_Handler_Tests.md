# Player Event Handler Tests

> 45 nodes

## Key Concepts

- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_follow_command()** (18 connections) — `server/commands/follow_commands.py`
- **follow_commands.py** (17 connections) — `server/commands/follow_commands.py`
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_unfollow_command()** (11 connections) — `server/commands/follow_commands.py`
- **handle_following_command()** (11 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_self_rejected()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_player_sends_request()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_npc_immediate()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_get_container()** (6 connections) — `server/commands/follow_commands.py`
- **Any** (6 connections)
- **test_handle_follow_no_such_player_or_npc()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_load_follow_context()** (5 connections) — `server/commands/follow_commands.py`
- **_resolve_follow_target()** (5 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_no_persistence()** (5 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_target()** (5 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_player_not_in_game()** (5 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_success()** (5 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_was_not_following()** (5 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_following_display()** (5 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_container()** (3 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_no_container()** (3 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_following_no_container()** (3 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Follow commands for MythosMUD.  Handlers for /follow, /unfollow, and /following.** (1 connections) — `server/commands/follow_commands.py`
- *... and 20 more nodes in this community*

## Relationships

- [Container Open Events](Container_Open_Events.md) (16 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (14 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (1 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/tests/unit/commands/test_follow_commands.py`

## Audit Trail

- EXTRACTED: 206 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*