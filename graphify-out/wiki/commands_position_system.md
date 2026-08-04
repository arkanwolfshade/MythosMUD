# commands position system

> 42 nodes

## Key Concepts

- **test_follow_commands.py** (23 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_follow_command()** (18 connections) — `server/commands/follow_commands.py`
- **follow_commands.py** (15 connections) — `server/commands/follow_commands.py`
- **_make_container()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **_make_request()** (12 connections) — `server/tests/unit/commands/test_follow_commands.py`
- **handle_unfollow_command()** (10 connections) — `server/commands/follow_commands.py`
- **handle_following_command()** (10 connections) — `server/commands/follow_commands.py`
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
- **Get application container from request.** (1 connections) — `server/commands/follow_commands.py`
- **Handle /follow <target>. Target must be a player or NPC in the same room.** (1 connections) — `server/commands/follow_commands.py`
- *... and 17 more nodes in this community*

## Relationships

- [target resolution service](target_resolution_service.md) (10 shared connections)
- [commands whisper command](commands_whisper_command.md) (5 shared connections)
- [commands npc admin](commands_npc_admin.md) (4 shared connections)
- [spell game magic](spell_game_magic.md) (4 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [models player related](models_player_related.md) (1 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/tests/unit/commands/test_follow_commands.py`

## Audit Trail

- EXTRACTED: 192 (98%)
- INFERRED: 4 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*