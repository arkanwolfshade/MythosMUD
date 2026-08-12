# E2E Suite Spec Helpers

> 18 nodes

## Key Concepts

- **_parse_npc_stats_dict()** (14 connections) — `server/commands/look_npc.py`
- **test_parse_npc_stats_dict_from_dict()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_from_json_string()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_invalid_json()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_non_dict_non_string()** (3 connections) — `server/tests/unit/commands/test_look_npc.py`
- **test_parse_npc_stats_dict_from_dict()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_npc_stats_dict_from_json_string()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_npc_stats_dict_invalid_json()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **test_parse_npc_stats_dict_other_type()** (3 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Parse NPC stats dictionary, handling both dict and JSON string formats.** (1 connections) — `server/commands/look_npc.py`
- **Test parsing NPC stats from dictionary.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test parsing NPC stats from JSON string.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test parsing NPC stats from invalid JSON.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test parsing NPC stats from non-dict, non-string.** (1 connections) — `server/tests/unit/commands/test_look_npc.py`
- **Test _parse_npc_stats_dict() handles dict input.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _parse_npc_stats_dict() parses JSON string.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _parse_npc_stats_dict() returns empty dict for invalid JSON.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`
- **Test _parse_npc_stats_dict() returns empty dict for other types.** (1 connections) — `server/tests/unit/commands/test_look_npc_helpers.py`

## Relationships

- [Look NPC Command](Look_NPC_Command.md) (8 shared connections)
- [Character Stats Generator](Character_Stats_Generator.md) (5 shared connections)

## Source Files

- `server/commands/look_npc.py`
- `server/tests/unit/commands/test_look_npc.py`
- `server/tests/unit/commands/test_look_npc_helpers.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*