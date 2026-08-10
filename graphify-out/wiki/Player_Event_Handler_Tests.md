# Player Event Handler Tests

> 35 nodes

## Key Concepts

- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_follow_command()** (18 connections) — `server/commands/follow_commands.py`
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_self_rejected()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_player_sends_request()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_npc_immediate()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_such_player_or_npc()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
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
- **Handle /follow <target>. Target must be a player or NPC in the same room.** (1 connections) — `server/commands/follow_commands.py`
- **Unit tests for follow command handlers.  Tests: follow (self rejected, same-room** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Build a mock container with optional follow_service, persistence, and player_ser** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Build request with app.state.container.** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Follow when container or follow_service missing returns not available.** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Follow when async_persistence missing returns not available.** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **Follow with no target asks 'Follow who?'.** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- *... and 10 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (17 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (6 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (4 shared connections)
- [Cursor Skills Harden](Cursor_Skills_Harden.md) (1 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (1 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/tests/unit/commands/test_follow_commands.py`

## Audit Trail

- EXTRACTED: 151 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*