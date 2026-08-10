# Player State Command Factory

> 32 nodes

## Key Concepts

- **test_look_npc_helpers.py** (34 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **_parse_npc_stats_dict()** (14 connections) — `server/commands/look_npc.py`
- **test_parse_npc_stats_dict_from_dict()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_from_json_string()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_invalid_json()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_non_dict_non_string()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_from_dict()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_npc_stats_dict_from_json_string()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_npc_stats_dict_invalid_json()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_npc_stats_dict_other_type()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_core_attributes()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_core_attributes_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_other_stats()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_other_stats_empty()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_lifecycle_info()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_format_lifecycle_info_no_lifecycle_state()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Parse NPC stats dictionary, handling both dict and JSON string formats.** (1 connections) — `server/commands/look_npc.py`
- **Test parsing NPC stats from dictionary.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test parsing NPC stats from JSON string.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test parsing NPC stats from invalid JSON.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test parsing NPC stats from non-dict, non-string.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Unit tests for look_npc helper functions.  Tests the helper functions in look_np** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _parse_npc_stats_dict() handles dict input.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _parse_npc_stats_dict() parses JSON string.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _parse_npc_stats_dict() returns empty dict for invalid JSON.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- *... and 7 more nodes in this community*

## Relationships

- [Container Repository CRUD](Container_Repository_CRUD.md) (13 shared connections)
- [Ground and Rescue Commands](Ground_and_Rescue_Commands.md) (6 shared connections)
- [Look NPC Command](Look_NPC_Command.md) (5 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (4 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (4 shared connections)
- [Logging System Planning](Logging_System_Planning.md) (4 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 106 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*