# Look NPC Command

> 146 nodes · cohesion 0.02

## Key Concepts

- **test_look_npc.py** (59 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_look_npc_helpers.py** (34 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **look_npc.py** (25 connections) — `server/commands/look_npc.py`
- **_parse_stat_datetime()** (16 connections) — `server/commands/look_npc.py`
- **_format_npc_description()** (15 connections) — `server/commands/look_npc.py`
- **_get_npc_room_id()** (14 connections) — `server/commands/look_npc.py`
- **_parse_npc_stats_dict()** (14 connections) — `server/commands/look_npc.py`
- **Any** (14 connections)
- **_format_npc_stats_for_admin()** (12 connections) — `server/commands/look_npc.py`
- **_try_lookup_npc_implicit()** (12 connections) — `server/commands/look_npc.py`
- **_find_matching_npcs()** (11 connections) — `server/commands/look_npc.py`
- **_format_lifecycle_info()** (11 connections) — `server/commands/look_npc.py`
- **_format_core_attributes()** (10 connections) — `server/commands/look_npc.py`
- **_format_other_stats()** (10 connections) — `server/commands/look_npc.py`
- **_format_single_npc_result()** (10 connections) — `server/commands/look_npc.py`
- **_format_multiple_npcs_result()** (6 connections) — `server/commands/look_npc.py`
- **test_format_core_attributes()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_core_attributes_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_lifecycle_info()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_lifecycle_info_no_lifecycle_state()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_npc_description()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_npc_description_fallback()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_npc_description_no_description()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_other_stats()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_other_stats_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- *... and 121 more nodes in this community*

## Relationships

- [Quest Journal Commands](Quest_Journal_Commands.md) (10 shared connections)
- [Logging Implementation Summary](Logging_Implementation_Summary.md) (10 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (6 shared connections)
- [Async Persistence Core](Async_Persistence_Core.md) (3 shared connections)
- [Room Look Formatting](Room_Look_Formatting.md) (3 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 515 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*