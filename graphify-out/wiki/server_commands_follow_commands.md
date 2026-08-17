# server commands follow commands

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
- **_get_container()** (7 connections) — `server/commands/follow_commands.py`
- **test_handle_follow_no_such_player_or_npc()** (7 connections) — `server/tests/unit/commands/test_follow_commands.py`
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

- [server commands admin commands](server_commands_admin_commands.md) (7 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (7 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (4 shared connections)
- [server commands combat taunt rationale](server_commands_combat_taunt_rationale.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (2 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (1 shared connections)
- [aliasrecord](aliasrecord.md) (1 shared connections)
- [server persistence repositories player repository](server_persistence_repositories_player_repository.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/follow_commands.py`
- `server/tests/unit/commands/test_follow_commands.py`

## Audit Trail

- EXTRACTED: 128 (95%)
- INFERRED: 7 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*