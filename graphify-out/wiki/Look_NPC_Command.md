# Look NPC Command

> 68 nodes

## Key Concepts

- **test_look_npc.py** (59 connections) — `server/tests/unit/commands/test_look_npc.py`
- **look_npc.py** (25 connections) — `server/commands/look_npc.py`
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
- **_format_multiple_npcs_result()** (6 connections) — `server/commands/look_npc.py`
- **test_format_core_attributes_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_core_attributes_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_other_stats_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_other_stats_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_lifecycle_info_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_lifecycle_info_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_no_match()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_find_matching_npcs_no_lifecycle_manager()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_npc_stats_for_admin_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_npc_stats_for_admin_no_npc_id()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_single_npc_result_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- *... and 43 more nodes in this community*

## Relationships

- [Character Stats Generator](Character_Stats_Generator.md) (19 shared connections)
- [Architecture Review Plan](Architecture_Review_Plan.md) (10 shared connections)
- [E2E Suite Spec Helpers](E2E_Suite_Spec_Helpers.md) (8 shared connections)
- [Player Cache](Player_Cache.md) (7 shared connections)
- [Coverage Disconnect Grace](Coverage_Disconnect_Grace.md) (7 shared connections)
- [Client Event Store](Client_Event_Store.md) (7 shared connections)
- [Player GUID Formatter](Player_GUID_Formatter.md) (5 shared connections)
- [Commands Command Look](Commands_Command_Look.md) (3 shared connections)
- [Container Persistence Queries](Container_Persistence_Queries.md) (2 shared connections)
- [Room Drop Renderer](Room_Drop_Renderer.md) (1 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`

## Audit Trail

- EXTRACTED: 293 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*