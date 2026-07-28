# Server Commands (38)

> 34 nodes

## Key Concepts

- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_follow_command()** (19 connections) — `server/commands/follow_commands.py`
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_self_rejected()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_player_sends_request()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_same_room_npc_immediate()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **test_handle_follow_no_such_player_or_npc()** (6 connections) — `server/tests/unit/commands/test_follow_commands.py`
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
- **Follow when player not found (not in game) returns error.** (1 connections) — `server/tests/unit/commands/test_follow_commands.py`
- *... and 9 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (14 shared connections)
- [Server Game (2)](Server_Game_%282%29.md) (5 shared connections)
- [Server Commands (8)](Server_Commands_%288%29.md) (5 shared connections)
- [Docs Examples](Docs_Examples.md) (1 shared connections)
- [Server Services (12)](Server_Services_%2812%29.md) (1 shared connections)
- [Server Utils (6)](Server_Utils_%286%29.md) (1 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/tests/unit/commands/test_follow_commands.py`

## Audit Trail

- EXTRACTED: 146 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*