# server commands look npc

> 77 nodes

## Key Concepts

- **test_look_npc.py** (60 connections) — `server/tests/unit/commands/test_look_npc.py`
- **look_npc.py** (25 connections) — `server/commands/look_npc.py`
- **_parse_npc_stats_dict()** (14 connections) — `server/commands/look_npc.py`
- **Any** (14 connections)
- **_format_npc_stats_for_admin()** (12 connections) — `server/commands/look_npc.py`
- **_find_matching_npcs()** (11 connections) — `server/commands/look_npc.py`
- **_format_lifecycle_info()** (11 connections) — `server/commands/look_npc.py`
- **_get_lifecycle_manager()** (11 connections) — `server/commands/look_npc.py`
- **_format_core_attributes()** (10 connections) — `server/commands/look_npc.py`
- **_format_other_stats()** (10 connections) — `server/commands/look_npc.py`
- **_format_single_npc_result()** (10 connections) — `server/commands/look_npc.py`
- **_try_lookup_npc_implicit()** (10 connections) — `server/commands/look_npc.py`
- **asyncio** (7 connections)
- **_format_multiple_npcs_result()** (6 connections) — `server/commands/look_npc.py`
- **test_format_npc_stats_for_admin_no_npc_id()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_npc_stats_for_admin_success()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_single_npc_result_success()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_single_npc_result_with_admin_stats()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_try_lookup_npc_implicit_multiple_matches()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_try_lookup_npc_implicit_no_npcs()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_try_lookup_npc_implicit_success()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **mock_lifecycle_manager()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_no_lifecycle_manager()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_no_match()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- *... and 52 more nodes in this community*

## Relationships

- [server commands look npc parse](server_commands_look_npc_parse.md) (24 shared connections)
- [server commands look npc format](server_commands_look_npc_format.md) (10 shared connections)
- [server commands look npc get](server_commands_look_npc_get.md) (8 shared connections)
- [server commands look npc rationale](server_commands_look_npc_rationale.md) (6 shared connections)
- [server commands quest commands](server_commands_quest_commands.md) (5 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server commands admin shutdown command](server_commands_admin_shutdown_command.md) (1 shared connections)
- [server commands exploration commands](server_commands_exploration_commands.md) (1 shared connections)
- [server app lifespan startup create](server_app_lifespan_startup_create.md) (1 shared connections)
- [server commands look room](server_commands_look_room.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`

## Audit Trail

- EXTRACTED: 198 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*