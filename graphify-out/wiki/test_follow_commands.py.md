# test_follow_commands.py

> 35 nodes

## Key Concepts

- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_follow_command()** (17 connections) — `server/commands/follow_commands.py`
- **asyncio** (13 connections)
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_npc_immediate()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_player_sends_request()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_self_rejected()** (8 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_such_player_or_npc()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_persistence()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_target()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_player_not_in_game()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_following_display()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_success()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_was_not_following()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_container()** (4 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_following_no_container()** (4 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_unfollow_no_container()** (4 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Handle /follow <target>. Target must be a player or NPC in the same room.** (1 connections) — `server/commands/follow_commands.py`
- **Unit tests for follow command handlers. Tests: follow (self rejected, same-room…** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Follow same-room player calls request_follow and returns result (uses…** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Follow same-room NPC returns immediate success with display name (uses…** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Follow when target not in room returns error from TargetResolutionService.** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Build a mock container with optional follow_service, persistence, and…** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Unfollow when container missing returns not available.** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- *... and 10 more nodes in this community*

## Relationships

- [get_username_from_user](get_username_from_user.md) (13 shared connections)
- [TargetMatch](TargetMatch.md) (9 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [CombatService](CombatService.md) (1 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/tests/unit/commands/test_follow_commands.py`

## Audit Trail

- EXTRACTED: 98 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*