# Look NPC Command

> 161 nodes · cohesion 0.02

## Key Concepts

- **test_look_npc.py** (58 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_look_npc_helpers.py** (33 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **look_npc.py** (22 connections) — `server/commands/look_npc.py`
- **_parse_stat_datetime()** (16 connections) — `server/commands/look_npc.py`
- **_format_npc_description()** (15 connections) — `server/commands/look_npc.py`
- **_parse_npc_stats_dict()** (14 connections) — `server/commands/look_npc.py`
- **Any** (14 connections) — `server/commands/look_npc.py`
- **_format_npc_stats_for_admin()** (12 connections) — `server/commands/look_npc.py`
- **_get_npc_room_id()** (12 connections) — `server/commands/look_npc.py`
- **_should_include_npc()** (12 connections) — `server/commands/look_npc.py`
- **_try_lookup_npc_implicit()** (12 connections) — `server/commands/look_npc.py`
- **_format_lifecycle_info()** (11 connections) — `server/commands/look_npc.py`
- **_format_core_attributes()** (10 connections) — `server/commands/look_npc.py`
- **_format_other_stats()** (10 connections) — `server/commands/look_npc.py`
- **_find_matching_npcs()** (9 connections) — `server/commands/look_npc.py`
- **_format_single_npc_result()** (9 connections) — `server/commands/look_npc.py`
- **_get_lifecycle_manager()** (9 connections) — `server/commands/look_npc.py`
- **_get_npcs_in_room()** (7 connections) — `server/commands/look_npc.py`
- **_format_multiple_npcs_result()** (6 connections) — `server/commands/look_npc.py`
- **test_format_core_attributes()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_core_attributes_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_lifecycle_info()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_lifecycle_info_no_lifecycle_state()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_npc_description()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_npc_description_fallback()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- *... and 136 more nodes in this community*

## Relationships

- [[NPC Occupant Verification]] (4 shared connections)
- [[Look Player Command]] (3 shared connections)
- [[Alias Expansion Logic]] (2 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Look Command Helpers]] (2 shared connections)
- [[NPC Database Sessions]] (1 shared connections)
- [[Room Look Formatting]] (1 shared connections)
- [[Commands Command Look]] (1 shared connections)
- [[NPC Combat Handler Tests]] (1 shared connections)
- [[Look Item Command Tests]] (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 566 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
