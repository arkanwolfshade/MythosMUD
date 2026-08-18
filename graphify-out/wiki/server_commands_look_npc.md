# server commands look npc

> 170 nodes

## Key Concepts

- **test_look_npc.py** (60 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_look_npc_helpers.py** (34 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **look_npc.py** (25 connections) — `server/commands/look_npc.py`
- **_parse_stat_datetime()** (16 connections) — `server/commands/look_npc.py`
- **_format_npc_description()** (15 connections) — `server/commands/look_npc.py`
- **_get_npc_room_id()** (14 connections) — `server/commands/look_npc.py`
- **_parse_npc_stats_dict()** (14 connections) — `server/commands/look_npc.py`
- **_should_include_npc()** (14 connections) — `server/commands/look_npc.py`
- **Any** (14 connections)
- **_format_npc_stats_for_admin()** (12 connections) — `server/commands/look_npc.py`
- **_try_lookup_npc_implicit()** (12 connections) — `server/commands/look_npc.py`
- **_find_matching_npcs()** (11 connections) — `server/commands/look_npc.py`
- **_format_lifecycle_info()** (11 connections) — `server/commands/look_npc.py`
- **_get_lifecycle_manager()** (11 connections) — `server/commands/look_npc.py`
- **_format_core_attributes()** (10 connections) — `server/commands/look_npc.py`
- **_format_other_stats()** (10 connections) — `server/commands/look_npc.py`
- **_format_single_npc_result()** (10 connections) — `server/commands/look_npc.py`
- **_get_npcs_in_room()** (7 connections) — `server/commands/look_npc.py`
- **asyncio** (7 connections)
- **_format_multiple_npcs_result()** (6 connections) — `server/commands/look_npc.py`
- **test_format_npc_stats_for_admin_no_npc_id()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_npc_stats_for_admin_success()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_single_npc_result_success()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_single_npc_result_with_admin_stats()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_try_lookup_npc_implicit_multiple_matches()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- *... and 145 more nodes in this community*

## Relationships

- [exitstack](exitstack.md) (9 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [server commands look room](server_commands_look_room.md) (3 shared connections)
- [server commands look command](server_commands_look_command.md) (3 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (1 shared connections)
- [server app lifespan startup](server_app_lifespan_startup.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 314 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*