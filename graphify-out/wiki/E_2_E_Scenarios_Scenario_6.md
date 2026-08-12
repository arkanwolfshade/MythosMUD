# E 2 E Scenarios Scenario

> 16 nodes

## Key Concepts

- **OccupantFormatter** (37 connections) — `server/realtime/occupant_formatter.py`
- **.__init__()** (3 connections) — `server/realtime/occupant_formatter.py`
- **test_occupant_formatter_is_valid_name_for_occupant_empty()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_add_valid_name_to_lists()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_player_name_for_update_uuid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_npc_name_for_update_uuid()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_process_dict_occupant_for_update_npc()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **test_occupant_formatter_separate_occupants_by_type_dict_players()** (3 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Formats and separates occupants by type.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Initialize occupant formatter.** (1 connections) — `server/realtime/occupant_formatter.py`
- **Test OccupantFormatter._is_valid_name_for_occupant() returns False for empty str** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._add_valid_name_to_lists() adds name to both lists.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_player_name_for_update() skips UUID player name.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_npc_name_for_update() skips UUID NPC name.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter._process_dict_occupant_for_update() processes NPC dict.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`
- **Test OccupantFormatter.separate_occupants_by_type() separates dict players.** (1 connections) — `server/tests/unit/realtime/test_occupant_formatter.py`

## Relationships

- [Room Occupant Formatter](Room_Occupant_Formatter.md) (15 shared connections)
- [Quality Audit Report](Quality_Audit_Report.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [E 2 E Cleanup Troubleshooting](E_2_E_Cleanup_Troubleshooting.md) (2 shared connections)
- [LRU Cache Manager](LRU_Cache_Manager.md) (1 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (1 shared connections)
- [Warning Fixes Session](Warning_Fixes_Session.md) (1 shared connections)
- [Mythosmud Obsidian Agents](Mythosmud_Obsidian_Agents.md) (1 shared connections)
- [3. Systematic Investigation Approach](3._Systematic_Investigation_Approach.md) (1 shared connections)
- [Cursor Plans Structlog](Cursor_Plans_Structlog.md) (1 shared connections)
- [Cursor Plans Room](Cursor_Plans_Room.md) (1 shared connections)
- [Cursor Plans Address](Cursor_Plans_Address.md) (1 shared connections)

## Source Files

- `server/realtime/occupant_formatter.py`
- `server/tests/unit/realtime/test_occupant_formatter.py`

## Audit Trail

- EXTRACTED: 65 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*