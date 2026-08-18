# test_look_npc.py

> 80 nodes

## Key Concepts

- **test_look_npc.py** (60 connections) — `server/tests/unit/commands/test_look_npc.py`
- **look_npc.py** (25 connections) — `server/commands/look_npc.py`
- **_format_npc_description()** (15 connections) — `server/commands/look_npc.py`
- **_parse_npc_stats_dict()** (14 connections) — `server/commands/look_npc.py`
- **Any** (14 connections)
- **_format_npc_stats_for_admin()** (12 connections) — `server/commands/look_npc.py`
- **_try_lookup_npc_implicit()** (12 connections) — `server/commands/look_npc.py`
- **_find_matching_npcs()** (11 connections) — `server/commands/look_npc.py`
- **_format_lifecycle_info()** (11 connections) — `server/commands/look_npc.py`
- **_format_core_attributes()** (10 connections) — `server/commands/look_npc.py`
- **_format_other_stats()** (10 connections) — `server/commands/look_npc.py`
- **_format_single_npc_result()** (10 connections) — `server/commands/look_npc.py`
- **asyncio** (7 connections)
- **_format_multiple_npcs_result()** (6 connections) — `server/commands/look_npc.py`
- **test_format_npc_stats_for_admin_no_npc_id()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_npc_stats_for_admin_success()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_single_npc_result_success()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_single_npc_result_with_admin_stats()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_try_lookup_npc_implicit_multiple_matches()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_try_lookup_npc_implicit_no_npcs()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_try_lookup_npc_implicit_success()** (4 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_no_lifecycle_manager()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_no_match()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_core_attributes_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- *... and 55 more nodes in this community*

## Relationships

- [test_look_npc_helpers.py](test_look_npc_helpers.py.md) (28 shared connections)
- [_get_lifecycle_manager](_get_lifecycle_manager.md) (7 shared connections)
- [_get_npc_room_id](_get_npc_room_id.md) (6 shared connections)
- [_should_include_npc](_should_include_npc.md) (6 shared connections)
- [get_npc_instance_service](get_npc_instance_service.md) (3 shared connections)
- [quest_commands.py](quest_commands.py.md) (3 shared connections)
- [look_command.py](look_command.py.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [mock_lifecycle_manager](mock_lifecycle_manager.md) (2 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (1 shared connections)
- [NPCDefinition](NPCDefinition.md) (1 shared connections)
- [test_look_room.py](test_look_room.py.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`

## Audit Trail

- EXTRACTED: 203 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*