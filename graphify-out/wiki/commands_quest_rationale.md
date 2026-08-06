# commands quest rationale

> 100 nodes

## Key Concepts

- **test_look_npc.py** (59 connections) — `server/tests/unit/commands/test_look_npc.py`
- **look_npc.py** (25 connections) — `server/commands/look_npc.py`
- **_format_npc_description()** (15 connections) — `server/commands/look_npc.py`
- **Any** (14 connections)
- **_parse_npc_stats_dict()** (14 connections) — `server/commands/look_npc.py`
- **_get_npc_room_id()** (14 connections) — `server/commands/look_npc.py`
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
- **test_parse_npc_stats_dict_from_dict()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_from_json_string()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_invalid_json()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_non_dict_non_string()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_core_attributes_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_core_attributes_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_other_stats_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_other_stats_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_format_lifecycle_info_success()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- *... and 75 more nodes in this community*

## Relationships

- [npc look commands](npc_look_commands.md) (32 shared connections)
- [commands inventory put](commands_inventory_put.md) (7 shared connections)
- [player helpers error](player_helpers_error.md) (7 shared connections)
- [look helpers commands](look_helpers_commands.md) (6 shared connections)
- [tick game processing](tick_game_processing.md) (4 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [commands admin mute](commands_admin_mute.md) (1 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`

## Audit Trail

- EXTRACTED: 391 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*